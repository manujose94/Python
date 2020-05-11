## How to create a installer

In this case, it's necessary to create one compiled file to we to able to exec the myssh.py file without installing nothing. Then, if we want to use directly the functionality that our code in Python provides us, we need to create an installer based on that file.

		pyinstaller --onefile myssh.py

**Note**: if there is any problem like "command not found"

`python -m PyInstaller --onefile myssh.py --name myssh` 

If we won't have enough permissions, we would change them with the following command:

		sudo chmod +x myssh.py

For this example, once it's created the installer, we can launch it in the following manner:

		./myssh -u student -h 192.168.225.130 -p student -c 'rosversion -d,rosnode list' 

This python supports both python 2 and python 3.