# HMS(Hospital Management System)
This project aims at to develop the software that covers all the aspects of management and operations of hospital. This fully complete demo project of the hospital management system allows authenticated users manage the statutory components of a health system.
Table of Contents

## About The Project
HMS is a web application using flask. You can use this project for free. The Documentation is given with the code.
### Built With
    • Bootstrap
    • Flask
    • Jinja
#### Getting Started
Follow the installation steps to open project without error
##### Installation
    1. Download and extract the project
    2. Download python 3.x and install on your PC. My pc is 64bit so I installed Python3(64bit). Set environmental variable for both python and pip or else you get command not found.
    3. I've used virtual environment. It's not necessary, but using virtual environment is preferable.
Note: You can skip the 5th step if you don't want virtual environment
(i) Make sure you've set your python path in environmental variable and then install
python -m venv venv
(ii) I've already created. So now you want to activate it. I'm using windows. so I used CMD. Now open the cmd of your current project folder. My project folder is HMS.
D:\flask\HMS> cd venv/Scripts/activate

After venv is activated

(venv) D:\flask\HMS>
(iii) Once you can close the project, this command is user to open the venv again and for deactivation command also given.
D:\flask\HMS>workon venv

If not working again activate your venv

(venv) D:\flask\HMS>

For Deactivating,

D:\flask\HMS> cd venv/Scripts/deactivate
    4. Install the following requirements by following command.
D:\flask\HMS> pip install -r requirements.txt
    5. To run the the code, use this command
D:\flask\HMS>python app.py

or

D:\flask\HMS>flask run

    6. If you get any error, make sure you've done following things
    ```
1. Python version should be 3.x.
2. Setting up Environment variables.
3. Installed all requirements without errors.
4. I am using 64 bit. If you are using 32 Bit google it and fix it.
5. Check the server is active or not.
6. Imported sql file.
7. Everything is done.
```
    7.  Login.
url : http://127.0.0.1:5000/login
For desk executive
	Username => 12345671,
	Password => abc@hospital,
For pharmacist
	Username => 12345672,
	Password => abc@hospital,
For diagnostic
	Username => 12345673,
	Password => abc@hospital,

Usage
HMS is a web application. This HMS is very simple to use.
Roadmap
See the open issues for a list of proposed features (and known issues).
Contributing
Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are greatly appreciated.
