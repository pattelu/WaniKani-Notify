import time
from functools import partial

from plyer import notification
import wk_api as wk
import json

def check_available_items(task_type, notify_zero=False):
    print(f"Script run on: {time.strftime('%H:%M:%S')}")

    wk.get_headers()

    user_level = wk.get_user_level()
    query = create_query(task_type, user_level)
    assignments = wk.get_assignments(query)

    print(f"Current user level: {user_level}")
    print(f"You have: {assignments["total"]} {task_type} items.")
    for key, value in assignments.items():
        print(f"{key}: {value}".capitalize())

    items_notification(assignments, task_type, notify_zero)

    print(f"Script ends on: {time.strftime('%H:%M:%S')}")

def create_query(task_type, user_level):
    with open("config.json", "r") as file:
        data = json.load(file)

    query = ""
    if task_type == "lesson":
        query += "immediately_available_for_lessons"

        if data["only_user_level"]:
            query += f"&levels={user_level}"

        query += "&subject_types="
        for key, value in data["lessons"].items():
            if value:
                query += f"{key},"

    if task_type == "review":
        query += f"immediately_available_for_review&srs_stages="

        srs = data["max_srs"]
        while srs > 0:
            query += f"{srs},"
            srs -= 1

        if data["only_user_level"]:
            query += f"&levels={user_level}"

        query += "&subject_types="
        for key, value in data["reviews"].items():
            if value:
                query += f"{key},"
    return query


# Scheduler
def start_scheduler(scheduler):
    scheduler.add_job(partial(check_available_items, "review"), "cron", minute=00, second=10)
    # scheduler.add_job(review_notification, "interval", minutes=1)
    scheduler.start()
    print(f"Scheduler started")


# Notifications
def error_notification(e):
    notification.notify(
        title=f"WaniKani Notify error!",
        message=f"WaniKani Notify encounter error: {e}. \nCheck your configuration file.",
        app_name="WaniKani Notify",
        timeout=10,
    )

def check_in_progress_notification():
    notification.notify(
        message=f"Checking...",
        app_name="WaniKani Notify",
        timeout=2,
    )

def items_notification(assignments,task_type, notify_zero=False):
    gen_notification = generate_specific_notification(assignments, task_type)

    if notify_zero and assignments["total"] == 0:
        notification.notify(
            message=f"Nothing to do",
            app_name="WaniKani Notify",
            timeout=5,
        )
    else:
        notification.notify(
            title=f"{task_type}s are ready!".capitalize(),
            message=gen_notification,
            app_name="WaniKani Notify",
            timeout=0,
        )

def generate_specific_notification(assignments, task_type):
    with open("config.json", "r") as file:
        data = json.load(file)

    gen_notification = ""

    srs_translate = {
        1: "Apprentice I",
        2: "Apprentice II",
        3: "Apprentice III",
        4: "Apprentice IV",
        5: "Guru I",
        6: "Guru II",
        7: "Master",
        8: "Enlightened"
    }

    srs = str(srs_translate[data["max_srs"]])

    if task_type == "lesson":
        if data["only_user_level"]:
            gen_notification += f"On your user level you have {assignments["total"]} lessons ready. \n"
        else:
            gen_notification += f"You have {assignments["total"]} lessons ready. \n"

        gen_notification += "-----\n"

        if data["lessons"]["radical"]:
            if assignments["radical"] > 0:
                gen_notification += f"Radicals: {assignments["radical"]} \n"

        if data["lessons"]["kanji"]:
            if assignments["kanji"] > 0:
                gen_notification += f"Kanji: {assignments["kanji"]} \n"

        if data["lessons"]["vocabulary"]:
            if assignments["vocabulary"] > 0:
                gen_notification += f"Vocabulary: {assignments["vocabulary"]} \n"

    if task_type == "review":
        if data["only_user_level"]:
            gen_notification += f"On your user level you have {assignments["total"]} items below SRS {srs} ready to review. \n"
        else:
            gen_notification += f"You have {assignments["total"]} items below SRS {srs} ready to review. \n"

        gen_notification += "-----\n"

        if data["reviews"]["radical"]:
            if assignments["radical"] > 0:
                gen_notification += f"Radicals: {assignments["radical"]} \n"

        if data["reviews"]["kanji"]:
            if assignments["kanji"] > 0:
                gen_notification += f"Kanji: {assignments["kanji"]} \n"

        if data["reviews"]["vocabulary"]:
            if assignments["vocabulary"] > 0:
                gen_notification += f"Vocabulary: {assignments["vocabulary"]} \n"

    return gen_notification