from functools import partial
from plyer import notification
import wk_api as wk
import json


def check_available_items(task_type, notify_zero=False):
    wk.get_headers()

    # Requests
    user_level = wk.get_user_level()
    query = create_query(task_type, user_level)
    assignments = wk.get_assignments(query)

    items_notification(assignments, task_type, notify_zero)


def create_query(task_type, user_level, subject_type=None):
    with open("config.json", "r") as file:
        data = json.load(file)

    query_list = []

    if task_type == "lesson":
        query = "immediately_available_for_lessons"

        if data["lessons"]["only_user_level"]:
            query += f"&levels={user_level}"

        query += "&subject_types="
        items = list(data["lessons"].items())
        for key, value in items[:-1]:
            if value:
                query += f"{key},"

        query_list.append(query)

    if task_type == "review":

        base = "immediately_available_for_review&subject_types="

        rev_types = []
        for key, value in data["reviews"].items():
            if value["is_checked"]:
                rev_types.append(key)

        for item in rev_types:
            if item == "radical":
                query = (
                    base
                    + f"radical&srs_stages={data["reviews"]["radical"]["srs_stages"]}"
                )
                if data["reviews"]["radical"]["only_user_level"]:
                    query += f"&levels={user_level}"
                query_list.append(query)
            if item == "kanji":
                query = (
                    base + f"kanji&srs_stages={data["reviews"]["kanji"]["srs_stages"]}"
                )
                if data["reviews"]["kanji"]["only_user_level"]:
                    query += f"&levels={user_level}"
                query_list.append(query)
            if item == "vocabulary":
                query = (
                    base
                    + f"vocabulary,kana_vocabulary&srs_stages={data["reviews"]["vocabulary"]["srs_stages"]}"
                )
                if data["reviews"]["vocabulary"]["only_user_level"]:
                    query += f"&levels={user_level}"
                query_list.append(query)

    return query_list


# Scheduler
def start_scheduler(scheduler):
    scheduler.add_job(
        partial(check_available_items, "review"), "cron", minute=00, second=10
    )
    scheduler.start()


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


def items_notification(assignments, task_type, notify_zero=False):
    gen_notification = generate_specific_notification(assignments, task_type)

    if assignments["total"] > 0:
        notification.notify(
            title=f"{task_type}s are ready!".capitalize(),
            message=gen_notification,
            app_name="WaniKani Notify",
            timeout=0,
        )

    if assignments["total"] == 0 and notify_zero:
        notification.notify(
            message=f"No new {task_type}s",
            app_name="WaniKani Notify",
            timeout=5,
        )


def generate_specific_notification(assignments, task_type):
    with open("config.json", "r") as file:
        data = json.load(file)

    gen_notification = ""

    if task_type == "lesson":
        if data["lessons"]["only_user_level"]:
            gen_notification += (
                f"On your user level you have {assignments["total"]} lessons ready. \n"
            )
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
        gen_notification += f"You have {assignments["total"]} reviews ready. \n"
        gen_notification += "-----\n"

        if data["reviews"]["radical"]["is_checked"]:
            if assignments["radical"] > 0:
                gen_notification += f"Radicals: {assignments["radical"]} "
                if assignments["radical_burn"] > 0:
                    gen_notification += (
                        f"(Ready to burn: {assignments["radical_burn"]})\n"
                    )
                else:
                    gen_notification += "\n"

        if data["reviews"]["kanji"]["is_checked"]:
            if assignments["kanji"] > 0:
                gen_notification += f"Kanji: {assignments["kanji"]} "
                if assignments["kanji_burn"] > 0:
                    gen_notification += (
                        f"(Ready to burn: {assignments["kanji_burn"]})\n"
                    )
                else:
                    gen_notification += "\n"

        if data["reviews"]["vocabulary"]["is_checked"]:
            if assignments["vocabulary"] > 0:
                gen_notification += f"Vocabulary: {assignments["vocabulary"]} "
                if assignments["vocabulary_burn"] > 0:
                    gen_notification += (
                        f"(Ready to burn: {assignments["vocabulary_burn"]})"
                    )

    return gen_notification
