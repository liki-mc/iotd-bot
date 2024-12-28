import subprocess
import time
from datetime import datetime, timedelta

def main():
    while True:
        now = datetime.now()
        next_run = now.replace(hour = 0, minute = 0, second = 0, microsecond = 0) + timedelta(days = 1)
        wait_time = (next_run - now).total_seconds()
        
        print("Starting subprocess")
        process = subprocess.Popen(["python", "bot.py"])
        process.wait()
        print("Subprocess finished")
        
        time.sleep(wait_time)

if __name__ == "__main__":
    main()