from datetime import datetime, timedelta
import time

from apscheduler.schedulers.background import BackgroundScheduler


def alarm(time):
    print(datetime.now())
    print("Alarm! This alarm was scheduled at %s." % time)


if __name__ == "__main__":
    sched = BackgroundScheduler()
    alarm_time = datetime.now() + timedelta(seconds=10)
    print(alarm_time)
    sched.add_job(alarm, "date", run_date=alarm_time, args=[datetime.now()])

    try:
        sched.start()
        while True:
            time.sleep(9)
    except (KeyboardInterrupt, SystemExit):
        pass
