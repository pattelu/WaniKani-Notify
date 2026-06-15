from functools import partial
from plyer import notification
import wk_api as wk
import json
from datetime import datetime, timezone, timedelta, time
import tzlocal


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
    reviews = future_assignments(query)
    future_notification(reviews)


def future_assignments(query_future):
    local_tz = tzlocal.get_localzone()
    now_local = datetime.now(local_tz)
    if time(0, 0) <= now_local.time() < time(3, 0):
        limit_local = datetime.combine(now_local.date(), time(3, 0), tzinfo=local_tz)
    else:
        limit_local = datetime.combine(
            now_local.date() + timedelta(days=1), time(3, 0), tzinfo=local_tz
        )

    middle_local = now_local + (limit_local - now_local) / 2

    current_time = datetime.now(timezone.utc)
    middle_utc = middle_local.astimezone(timezone.utc)
    limit_utc = limit_local.astimezone(timezone.utc)

    current_plus = current_time.replace(
        hour=current_time.hour + 1, minute=00, second=0, microsecond=0
    )
    middle_utc_start = middle_utc.replace(
        hour=middle_utc.hour + 1, minute=00, second=0, microsecond=0
    )
    middle_utc_end = middle_utc.replace(minute=59, second=0, microsecond=0)
    limit_utc = limit_utc.replace(minute=59, second=0, microsecond=0)

    current_plus_str = current_plus.strftime("%Y-%m-%dT%H:%M:%SZ")
    middle_utc_end_str = middle_utc_end.strftime("%Y-%m-%dT%H:%M:%SZ")
    middle_utc_start_str = middle_utc_start.strftime("%Y-%m-%dT%H:%M:%SZ")
    limit_utc_str = limit_utc.strftime("%Y-%m-%dT%H:%M:%SZ")

    query_first_half = [
        f"&available_after={current_plus_str}&available_before={middle_utc_end_str}"
    ]
    query_second_half = [
        f"&available_after={middle_utc_start_str}&available_before={limit_utc_str}"
    ]

    if wk.get_assignments(query_first_half):
        future_review = wk.get_future_assignments(query_future, local_tz, current_time)
        return future_review
    elif wk.get_assignments(query_second_half):
        future_review = wk.get_future_assignments(query_future, local_tz, current_time)
        return future_review
    else:
        no_review = {"time": 0}
        return no_review


# Scheduler
def start_scheduler(scheduler):
    scheduler.add_job(
        partial(check_available_items, "review"), "cron", minute=00, second=10
    )
    scheduler.start()


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


# Notifications
def error_notification(e):
    notification.notify(
        title=f"WaniKani Notify error!",
        message=f"WaniKani Notify encounter error: {e}.",
        app_name="WaniKani Notify",
        timeout=10,
    )


def check_in_progress_notification(time_limit=2):
    notification.notify(
        message=f"Checking...",
        app_name="WaniKani Notify",
        timeout=time_limit,
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

        gen_notification += "\n-----\n"
        for key, value in assignments["srs_stage"].items():
            if value != 0:
                gen_notification += f"{key}: {value}, "
        gen_notification = gen_notification.strip(", ")

    if task_type == "future":
        gen_notification += (
            f"Closest {assignments["total"]} review{plural} at {assignments["time"]}.\n"
        )
        gen_notification += "-----\n"

        if assignments["radical"] != 0:
            gen_notification += f"Radicals: {assignments["radical"]} "
            if assignments["radical_burn"] != 0:
                gen_notification += f"(Ready to burn: {assignments["radical_burn"]}) "
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
