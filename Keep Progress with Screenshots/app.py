import random
import schedule
import urllib.request  
import pyautogui
import time
import datetime




# print(time.time_ns())

def Screenshot():
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(f"./Keep Progress with Screenshots/Screenshots/{str(datetime.datetime.now()).replace('-', '').replace(':', '').replace('.', '').replace(' ', '')+str(time.time_ns())}.png")
# toaster.show_toast("Workout",
#     "Become Buff",
#     icon_path=None,
#     duration=1)
# webUrl = urllib.request.urlopen(Videos[random.randint(0,len(Videos)-1 )])  

Screenshot()
schedule.every(1).seconds.do(Screenshot)

while True:
    schedule.run_pending()
    time.sleep(1)
    