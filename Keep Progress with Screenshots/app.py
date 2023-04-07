import schedule
import pyautogui
import time
import datetime
i=0
MAX_PICS=500
def Screenshot():
    global i
    i=i+1
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(
        f"./Keep Progress with Screenshots/Screenshots/{str(datetime.datetime.now()).replace('-', '').replace(':', '').replace('.', '').replace(' ', '')+str(time.time_ns())}.png")


Screenshot()
schedule.every(5).minutes.do(Screenshot)

while True:
    
    schedule.run_pending()
    time.sleep(10)

    if(i>=MAX_PICS):
        print(i)
        break
