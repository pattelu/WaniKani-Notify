import os
import time

from plyer import notification
from apscheduler.schedulers.background import BackgroundScheduler

import wk

def main():
    if not os.path.exists("config.json"):
        wk.add_wk_api_key()

    verification = True
    while verification:
        verification = wk.wk_api_key_verification()

    # Check review with app start
    user_notification()

    scheduler = BackgroundScheduler()
    start_scheduler(scheduler)

    try:
        while True:
            time.sleep(1)
    except(KeyboardInterrupt, SystemExit):
        scheduler.shutdown()


def user_notification():
    print(f"Script run on: {time.strftime('%H:%M:%S')}")

    level = wk.get_user_level()
    assignments = wk.get_assignments()
    review = wk.get_items_to_review(level, assignments)

    print(f"Current user level: {level}")
    print(f"All kanji and radicals to review: {len(assignments)}")
    print(f"Current level kanji and radicals to review: {len(review)}")

    if len(review) > 0:
        notification.notify(
            title=f"Critical review is ready!",
            message=f"You have {len(review)} critical items to review.",
            app_name="WaniKani Notify",
            timeout=0,
        )

def start_scheduler(scheduler):
    scheduler.add_job(user_notification, "cron", minute=00, second=10)
    scheduler.start()
    print(f"Scheduler started. \n {scheduler.get_jobs()}")


if __name__ == "__main__":
    main()