import subprocess as sp
import time
import pyautogui


def make_json_forx(for_x: pyautogui.Point) -> str:
    return '\"{\\"x\\": ' + str(for_x.x) + '}\"'


def make_json_fory(for_y: pyautogui.Point) -> str:
    return '\"{\\"y\\": ' + str(for_y.y) + '}\"'


def combined_json(point: pyautogui.Point):
    return '\"{\\"x\\" : ' + str(point.x) + ', \\"y\\": ' + str(point.y) + '}\"'


access_key = "DEVICE_ACCESS_KEY"

for i in range(200):
    point: pyautogui.Point = pyautogui.position()
    command = 'curl -v -X POST -d ' + combined_json(
        point) + ' https://demo.thingsboard.io/api/v1/' + access_key + '/telemetry --header "Content-Type:application/json"'
    print(command)
    sp.run(command)
    time.sleep(0.1)
