#! /usr/bin/env python

import json
import sys
import time
import getopt
    
USAGE = "Usage: python {sys.argv[0]} [--help] | [-u <user> ] [-h <host> ] [-p <password> ] [-c '<command>,<command>']"
MESSAGE = {}
ROBOT = None #MODEL NAME
TOPICS=None

def parse(args):
    print(args)
    options, arguments = getopt.getopt(
        args,                             
        'r:j:',                            
        ["robot=,json="])
    commands= None
    content=None
    param_json=0
    param_model_name=0
    for o, a in options:
        if o in ("-j", "--json"):
            content = a
            param_json+=1
        if o in ("-r", "--robot"):
            ROBOT = a
            param_model_name+=1
            
   
    if param_json == 0:
            print("Arguments are not used rigth now") # Argument example -c 'cat' halo.txt, so arguemnts lenght is 1 
            return json.dumps({'message': 'Missing arguments at launch [json]', 'succes': 'false'})
    try:
        #VER EL JSON
       # print(content)
        TOPICS=eval(content)
        MESSAGE=json.dumps({'message': TOPICS['safety_module'], 'succes': 'true'})
    except:
        MESSAGE=json.dumps({'message': 'Error on json on python file', 'succes': 'false'})
    return MESSAGE

def main(topics):
    #global tiempo
    #rospy.Subscriber('clock',Clock ,tiempo)
    print(topics)
    global vel_mon
    vel_mon=0
    vel = Twist()
    vel.angular.z=0.2
    rospy.init_node(robot+'_velocity_check')
    pub = rospy.Publisher('/'+robot+'/robotnik_base_control/cmd_vel', Twist, queue_size=10)
    rospy.Subscriber('/'+robot+'/robotnik_base_control/odom',Odometry, callback)
    if (diff < 0.10):
        respuesta_json = {
            "message": diff,
            "succes": True
        }
    else:
        respuesta_json = {
            "message": diff,
            "succes": False
        }
    
    respuesta_json = json.dumps(respuesta_json)
    print(respuesta_json)

if __name__ == '__main__':
    try:
        if len(sys.argv) > 2:
            #SI HAY MAS DE 3 ARGUMENTOS
            if len(sys.argv) > 3 :
                print(len(sys.argv))
                array=sys.argv
                ## -j "{ key: value }" SERA SIEMPRE LOS DOS ULTIMOS
                print( parse(array[len(sys.argv)-2:len(sys.argv)]) )
                
            #main(sys.argv[1])       
        else:
            print("You must Usage: Angular_Velocity_Check.py robot_name")
            respuesta_json = {
            "message": "You must Usage: Angular_Velocity_Check.py robot_name",
            "succes": False
            }
            respuesta_json = json.dumps(respuesta_json)
            print(respuesta_json)

    except:
        respuesta_json = {
            "message": "Exception: " + str(sys.exc_info()[1]),
            "succes": False
        }
        respuesta_json = json.dumps(respuesta_json)
        print(respuesta_json)
