import schedule
import pyautogui
import time
import datetime

def Screenshot():
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(
        f"./Keep Progress with Screenshots/Screenshots/{str(datetime.datetime.now()).replace('-', '').replace(':', '').replace('.', '').replace(' ', '')+str(time.time_ns())}.png")


Screenshot()
schedule.every(13).minutes.do(Screenshot)

while True:
    schedule.run_pending()
    time.sleep(10)
