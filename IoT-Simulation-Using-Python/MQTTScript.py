import subprocess as sp
import os
import time
import pyautogui


def make_json_forx(for_x: pyautogui.Point) -> str:
    return '\"{\\"x\\": ' + str(for_x.x) + '}\"'


def make_json_fory(for_y: pyautogui.Point) -> str:
    return '\"{\\"y\\": ' + str(for_y.y) + '}\"'


def combined_json(point: pyautogui.Point):
    return '\"{\\"x\\" : ' + str(point.x) + ', \\"y\\": ' + str(point.y) + '}\"'


access_key = "DEVICE_ACCESS_KEY"

print(os.getcwd())
os.chdir("C:/Program Files/Mosquitto")

for i in range(200):
    point: pyautogui.Point = pyautogui.position()
    command = "mosquitto_pub -d -q 1 -h \"localhost\" -t \"v1/devices/me/telemetry\" -u " + access_key + " -m " + combined_json(
        point)
    print(command)
    sp.run(command)
    time.sleep(0.1)
