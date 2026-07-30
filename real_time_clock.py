from datetime import datetime
import time
import os
while True:
    os.system("cls") #os.system("cls") will cleaar the screen in terminal
    print(datetime.now().strftime("%H:%M:%S"))
    time.sleep(1)
