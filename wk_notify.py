import time
from plyer import notification
import wk_api as wk


def start_notification():
    notification.notify(
        title=f"WaniKani Notify started!",
        message=f"Application will inform you if critical reviews are ready!",
        app_name="WaniKani Notify",
        timeout=5,
    )

def error_notification(e):
    notification.notify(
        title=f"WaniKani Notify error!",
        message=f"WaniKani Notify encounter error: {e}. Check your configuration file.",
        app_name="WaniKani Notify",
        timeout=10,
    )

def review_notification():
    print(f"Script run on: {time.strftime('%H:%M:%S')}")

    wk.get_headers()
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
    scheduler.add_job(review_notification, "cron", minute=00, second=10)
    # scheduler.add_job(review_notification, "interval", minutes=1)
    scheduler.start()
    print(f"Scheduler started")
