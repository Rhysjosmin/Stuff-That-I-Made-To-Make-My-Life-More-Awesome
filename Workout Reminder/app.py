from win10toast import ToastNotifier
import random
import schedule
import urllib.request  

import time
Amount_Of_Workouts=0
toaster = ToastNotifier()
Videos=['https://www.youtube.com/watch?v=ho8fvPH_Ro0']
workouts=['Pushups','Diamond Pushups','Planks','Inclined Pushups','Squats','Jaw Thing']
def Workout():
    global Amount_Of_Workouts
    Amount_Of_Workouts+=1
    toaster.show_toast(f"Workout {Amount_Of_Workouts}",
    f"do {random.randrange(1,6)*5} {workouts[random.randint(0,len(workouts)-1 )]},{random.randrange(1,3)} Sets",
    icon_path=None,
    duration=8)
    # Importing urllib request module in the program  
    # Using urlopen() function with url in it  
    webUrl = urllib.request.urlopen(Videos[random.randint(0,len(Videos)-1 )])  

toaster.show_toast("Workout",
    "Become Buff",
    icon_path=None,
    duration=1)
webUrl = urllib.request.urlopen(Videos[random.randint(0,len(Videos)-1 )])  

# schedule.every(5).to(10).minutes.do(Workout)
schedule.every(5).to(20).minutes.do(Workout)

while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(10)