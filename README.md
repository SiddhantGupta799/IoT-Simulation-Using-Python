
# IoT MQTT I2C Simulation Using Python

This project is a simulation of an IoT device that plots sensor data on a Dashboard on ThingsBoard.io Platform.
Its also a step-by-step guide.

## Authors

- [@Siddhant Gupta](https://github.com/SiddhantGupta799)


## Getting Started
### We will discuss how to make our PC the ‘Microcontroller’ and our mouse the ‘Sensor’. We will be using a python library named as pyautogui which is an open-source library.

### Pre-Requisites:
- [Things Board Demo Account](https://demo.thingsboard.io/signup)
- [Python](https://www.python.org/downloads/) + [PyCharm](https://www.jetbrains.com/pycharm/download/#section=windows )


#### Setting Up thingsboard demo account
-	Create an account, by default thingsboard gives a Tenant Administrator Account.
-	On the left side go to Devices.
- 	Click on the '+' button on the top right. Select Add new Device.
-	Give name as you suit.
-	Select Add.

#### Setting Up Python
-	Download and install the package.
-	Hit Install Now, but do ensure the boxes at the bottom are ticked.
-	Python will get installed on your PC.

#### Setting Up PyCharm
-	Download the Community Version.
-	Check all the boxes.
-	Click Next and then Install.
-	Reboot your PC.



#### Sending Telemetry to the thingsboard demo server via HTTPS protocol
-	For this we will be using the ‘os’ and ‘subprocess’ libraries. These libraries are built-in in python.
-	Head to PyCharm, Create a Project.
-	Expand the python interpreter option.
-	Select the virtual env, PyCharm will automatically find the Python3 interpreter installed on the PC. Hit ‘Create’.
-	Next import os library and import subprocess library, also import ‘pyautogui’ PyCharm will show an error as this file doesn’t exist so right click and show context actions and then install the module from there.

```
import os
import subprocess
import pyautogui
import time
```

- Define a make_json_function () which will return a json string populated with the current mouse pointer position, every time it’s called.

```
def make_json():
    """ here we will fetch the current mouse pointer position using the pyautogui module
    and then will make a json string out of it. """
    point: pyautogui.Point = pyautogui.position()        # returns a pyautogui.Point object
    return '\"{\\"x\\" : ' + str(point.x) + ', \\"y\\": ' + str(point.y) + '}\"'
```

- Go to thingsboard and copy the device access token.
-	Fill the access token in the device_access_key variable.

```
os.chdir("C:/Program Files/Mosquitto")
device_access_key = DEVICE_ACCESS_KEY
server = "demo.thingsboard.io"
```
- write the following script

```
for i in range(200):
    command = "mosquitto_pub -d -q 1 -h \"" + server + "\" -t " \
                "\"v1/devices/me/telemetry\" -u \"" + device_access_key + "\" -m " + make_json()
    print(command)
    subprocess.run(command)
    time.sleep(0.1)     # optional for this import time library
```
-	Run the script.
-	Go to your devices latest telemetry section there you’ll find the plotted mouse pointer positions, select both of them and you can see them on any widget that you prefer.
- click on x and y you’ll see 'Show on widget' option. 
- Select any widget of your choice and add it to dashboard.
