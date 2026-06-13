from functools import partial
from plyer import notification
import wk_api as wk
import json


def check_available_items(task_type, notify_zero=False):
    count = []
    wk.get_headers()

    # Requests
    try:
        user_level = wk.get_user_level()
        query = create_query(task_type, user_level)
        assignments_list = wk.get_assignments(query)
        count = wk.count_assignments(assignments_list)
    except Exception as e:
        error_notification(e)

    items_notification(count, task_type, notify_zero)


def check_closest_review():
    user_level = wk.get_user_level()
    query = create_query("review", user_level, True)
    reviews = wk.get_future_assignments(query)
    future_notification(reviews)


def create_query(task_type, user_level, future=False):
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
        if future:
            base = "subject_types="
        else:
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


def check_in_progress_notification(time=2):
    notification.notify(
        message=f"Checking...",
        app_name="WaniKani Notify",
        timeout=time,
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


def future_notification(info):
    if info["time"] == 0:
        notification.notify(
            message=f"No more new reviews for today!",
            app_name="WaniKani Notify",
            timeout=5,
        )
    else:
        gen_notification = generate_specific_notification(info, "future")
        notification.notify(
            message=gen_notification,
            app_name="WaniKani Notify",
            timeout=0,
        )


def generate_specific_notification(assignments, task_type):
    with open("config.json", "r") as file:
        data = json.load(file)

    gen_notification = ""
    plural = ""

    if assignments["total"] > 1:
        plural = "s"

    if task_type == "lesson":
        if data["lessons"]["only_user_level"]:
            gen_notification += f"On your user level you have {assignments["total"]} lesson{plural} ready. \n"
        else:
            gen_notification += (
                f"You have {assignments["total"]} lesson{plural} ready. \n"
            )

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
        gen_notification += f"You have {assignments["total"]} review{plural} ready. \n"
        gen_notification += "-----\n"

        if data["reviews"]["radical"]["is_checked"]:
            if assignments["radical"] > 0:
                gen_notification += f"Radicals: {assignments["radical"]} "
                if assignments["radical_burn"] > 0:
                    gen_notification += (
                        f"(Ready to burn: {assignments["radical_burn"]}) "
                    )
                if data["reviews"]["radical"]["only_user_level"]:
                    gen_notification += f"- only user level."
        gen_notification += "\n"

        if data["reviews"]["kanji"]["is_checked"]:
            if assignments["kanji"] > 0:
                gen_notification += f"Kanji: {assignments["kanji"]} "
                if assignments["kanji_burn"] > 0:
                    gen_notification += f"(Ready to burn: {assignments["kanji_burn"]}) "
                if data["reviews"]["kanji"]["only_user_level"]:
                    gen_notification += f"- only user level."
        gen_notification += "\n"

        if data["reviews"]["vocabulary"]["is_checked"]:
            if assignments["vocabulary"] > 0:
                gen_notification += f"Vocabulary: {assignments["vocabulary"]} "
                if assignments["vocabulary_burn"] > 0:
                    gen_notification += (
                        f"(Ready to burn: {assignments["vocabulary_burn"]}) "
                    )
                if data["reviews"]["vocabulary"]["only_user_level"]:
                    gen_notification += f"- only user level."

    if task_type == "future":
        gen_notification += (
            f"Closest {assignments["total"]} review{plural} at {assignments["time"]}.\n"
        )
        gen_notification += "-----\n"

        if assignments["radicals"] != 0:
            gen_notification += f"Radicals: {assignments["radicals"]} "
            if assignments["radicals_burn"] != 0:
                gen_notification += f"(Ready to burn: {assignments["radicals_burn"]}) "
        gen_notification += "\n"

        if assignments["kanji"] != 0:
            gen_notification += f"Kanji: {assignments["kanji"]} "
            if assignments["kanji_burn"] != 0:
                gen_notification += f"(Ready to burn: {assignments["kanji_burn"]}) "
        gen_notification += "\n"

        if assignments["vocabulary"] != 0:
            gen_notification += f"Vocabulary: {assignments["vocabulary"]} "
            if assignments["vocabulary_burn"] != 0:
                gen_notification += (
                    f"(Ready to burn: {assignments["vocabulary_burn"]}) "
                )

    return gen_notification
