#!/bin/python
import sys
import getopt
#pip install pexpect
from pexpect import pxssh
import getpass
import json
import re
#To create a excutable python
#https://realpython.com/pyinstaller-python/ 
## Python2.7
# python -m PyInstaller --onefile myssh.py --name myssh 
## Python 3
# pyinstaller --onefile myssh.py --name myssh

#data = {"user": "student",
      #  "host": "192.168.225.130",
      #  "password": "student",
      #  "commands": " " .join(sys.argv[1:])}
USAGE = "Usage: python {sys.argv[0]} [--help] | [-u <user> ] [-h <host> ] [-p <password> ] [-c '<command>,<command>']"
MESSAGE = {}


def parse(args):
    options, arguments = getopt.getopt(
        args,                              # Arguments
        'iu:h:p:c:',                            # Short option definitions
        ["info", "user=","host=", "password=" "commands="]) # Long option definitions
    commands= None
    user=None
    host=None
    password=None
    all_params=0
    for o, a in options:
        if o in ("-i", "--help"):
            print(USAGE)
        if o in ("-u", "--user"):
            user = a
            all_params+=1  
        if o in ("-h", "--host"):
            host = a
            all_params+=1  
        if o in ("-p", "--password"):
            password = a
            all_params+=1       
        if o in ("-c", "--commands"):
            commands=a.split(",")
            all_params+=1  
           
    if all_params < 4:
            print("Arguments are not used rigth now") # Argument example -c 'cat' halo.txt, so arguemnts lenght is 1 
            return json.dumps({'message': 'Missing arguments at launch', 'succes': False})
    try:
        output_command=launch(commands,user,host,password)
        MESSAGE=json.dumps({'message': output_command, 'succes': True})
    except:
        MESSAGE=json.dumps({'message': 'ssh failed on login', 'succes': False})
    return MESSAGE

def escape_ansi(line):
    ansi_escape = re.compile(r'(?:\x1B[@-_]|[\x80-\x9F])[0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', line)

def  launch(commands,username,hostname,password):
    if len(commands) < 1:
        return None
    _output=""
    try:
        s = pxssh.pxssh()
        s.login(hostname, username, password)
        if sys.version_info[0] > 2:
            for position in range(len(commands)):
                s.sendline(commands[position])   # run a command
                s.prompt()             # match the prompt
                a=escape_ansi(s.before.decode('utf-8')).split('\r\n')
                a=a[1:len(a)]
                for p in range(len(a)): # Making to commands like ls or ll
                    _output+=a[p]+'\n'
        else:
            for position in range(len(commands)):
                s.sendline(commands[position])   # run a command
                s.prompt()             # match the prompt
                a=escape_ansi(s.before).split('\r\n')
                a=a[1:len(a)]
                for p in range(len(a)):
                    _output+=a[p]+'\n'            
        s.logout()
        return _output
    except pxssh.ExceptionPxssh as e:
        raise e
       

def main():
    args = sys.argv[1:]
    print(parse(args))

if __name__ == '__main__':
    main()
 # Example: /usr/bin/python3 /home/student/Documents/project/ssh.py -u student -h 192.168.225.130 -p student -c 'rosversion -d,rosnode list' 
    