from datetime import timedelta
from doctest import master

import requests
import json
import wk_notify as wkn

headers = {}


def get_headers():
    with open("config.json", "r", encoding="utf-8") as file:
        config = json.load(file)

    api_key = config.get("wk_api_key")
    global headers
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Wanikani-Revision": "20170710",
    }


def get_user_level():
    user_request = "https://api.wanikani.com/v2/user"
    user_response = requests.get(user_request, headers=headers)

    if user_response.status_code == 200:
        user_data = user_response.json()
        user_level = user_data["data"]["level"]
        return user_level
    elif user_response.status_code == 401:
        raise Exception("invalid API key")
    else:
        raise Exception("exception")


def get_assignments(query_list):

    assignments_list = []

    for query in query_list:
        assignment_request = f"https://api.wanikani.com/v2/assignments?{query}"

        while assignment_request:
            try:
                assignment_response = requests.get(assignment_request, headers=headers)
                assignment_data = assignment_response.json()

                for assignment in assignment_data["data"]:
                    assignment_type = assignment["data"].get("subject_type")
                    if assignment_type == "radical":
                        assignments_list.append(assignment)
                    if assignment_type == "kanji":
                        assignments_list.append(assignment)
                    if (
                        assignment_type == "vocabulary"
                        or assignment_type == "kana_vocabulary"
                    ):
                        assignments_list.append(assignment)

                next_url = assignment_data.get("pages", {}).get("next_url")

                if next_url:
                    assignment_request = next_url
                else:
                    assignment_request = None
            except Exception as e:
                wkn.error_notification(e)

    return assignments_list


def count_assignments(assignments_list):
    radical = 0
    kanji = 0
    vocabulary = 0
    radical_burn = 0
    kanji_burn = 0
    vocabulary_burn = 0
    apprentice_1 = 0
    apprentice_2 = 0
    apprentice_3 = 0
    apprentice_4 = 0
    guru_1 = 0
    guru_2 = 0
    master_s = 0
    enlightened = 0

    for assignment in assignments_list:
        if assignment["data"]["subject_type"] == "radical":
            radical += 1
            if assignment["data"]["srs_stage"] == 8:
                radical_burn += 1
        if assignment["data"]["subject_type"] == "kanji":
            kanji += 1
            if assignment["data"]["srs_stage"] == 8:
                kanji_burn += 1
        if (
            assignment["data"]["subject_type"] == "vocabulary"
            or assignment["data"]["subject_type"] == "kana_vocabulary"
        ):
            vocabulary += 1
            if assignment["data"]["srs_stage"] == 8:
                vocabulary_burn += 1

        if assignment["data"]["srs_stage"] == 1:
            apprentice_1 += 1
        if assignment["data"]["srs_stage"] == 2:
            apprentice_2 += 1
        if assignment["data"]["srs_stage"] == 3:
            apprentice_3 += 1
        if assignment["data"]["srs_stage"] == 4:
            apprentice_4 += 1
        if assignment["data"]["srs_stage"] == 5:
            guru_1 += 1
        if assignment["data"]["srs_stage"] == 6:
            guru_1 += 1
        if assignment["data"]["srs_stage"] == 7:
            master_s += 1
        if assignment["data"]["srs_stage"] == 8:
            enlightened += 1

    total = radical + kanji + vocabulary

    assignment_items = {
        "radical": radical,
        "kanji": kanji,
        "vocabulary": vocabulary,
        "radical_burn": radical_burn,
        "kanji_burn": kanji_burn,
        "vocabulary_burn": vocabulary_burn,
        "total": total,
        "srs_stage": {
            "A1": apprentice_1,
            "A2": apprentice_2,
            "A3": apprentice_3,
            "A4": apprentice_4,
            "G1": guru_1,
            "G2": guru_2,
            "M": master_s,
            "E": enlightened,
        },
    }

    return assignment_items


def get_future_assignments(query_future, local_tz, current_time):
    while True:
        query_new = []

        next_time = current_time + timedelta(hours=1)

        available_after = next_time.replace(minute=0, second=0, microsecond=0)
        available_before = next_time.replace(minute=59, second=0, microsecond=0)

        after_str = available_after.strftime("%Y-%m-%dT%H:%M:%SZ")
        before_str = available_before.strftime("%Y-%m-%dT%H:%M:%SZ")

        for i in range(len(query_future)):
            query_item = (
                query_future[i]
                + f"&available_after={after_str}&available_before={before_str}"
            )
            query_new.append(query_item)

        future_assignment = get_assignments(query_new)

        future_review = count_assignments(future_assignment)

        if not future_assignment:
            current_time = next_time
            continue
        else:
            local_time = available_after.astimezone(local_tz).strftime("%H:%M")
            future_review["time"] = local_time

            return future_review
