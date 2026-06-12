from datetime import datetime, timezone, timedelta
import tzlocal

import requests
import json

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
            assignment_response = requests.get(assignment_request, headers=headers)

            if assignment_response.status_code == 200:
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
            else:
                raise Exception(f"HTTP error: {assignment_response.status_code}")

    return assignments_list


def count_assignments(assignments_list):
    radical = 0
    kanji = 0
    vocabulary = 0
    radical_burn = 0
    kanji_burn = 0
    vocabulary_burn = 0

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

    total = radical + kanji + vocabulary

    assignment_items = {
        "radical": radical,
        "kanji": kanji,
        "vocabulary": vocabulary,
        "radical_burn": radical_burn,
        "kanji_burn": kanji_burn,
        "vocabulary_burn": vocabulary_burn,
        "total": total,
    }

    return assignment_items


def get_future_assignments(query_future):
    current = datetime.now(timezone.utc)
    now = datetime.now(timezone.utc)

    radicals = 0
    kanji = 0
    vocabulary = 0
    radicals_burn = 0
    kanji_burn = 0
    vocabulary_burn = 0

    result = []
    query = ["immediately_available_for_review"]

    all_assignments = get_assignments(query)
    all_assignments_ids = []

    for item in all_assignments:
        all_assignments_ids.append(item["id"])

    while True:
        query_new = []

        next_time = current + timedelta(hours=1)
        limit_time = now.replace(
            day=now.day + 1, hour=3, minute=0, second=0, microsecond=0
        )
        available_after = next_time.replace(minute=0, second=0, microsecond=0)
        available_before = next_time.replace(minute=59, second=0, microsecond=0)

        after_str = available_after.strftime("%Y-%m-%dT%H:%M:%SZ")
        before_str = available_before.strftime("%Y-%m-%dT%H:%M:%SZ")

        for i in range(len(query_future)):
            query_item = (
                query_future[i]
                + f"&avaliable_after={after_str}&available_before={before_str}"
            )
            query_new.append(query_item)

        future_assignment = get_assignments(query_new)

        for element in future_assignment:
            if element["id"] not in all_assignments_ids:
                result.append(future_assignment)
                if element["data"]["subject_type"] == "radical":
                    radicals += 1
                    if element["data"]["srs_stage"] == 8:
                        radicals_burn += 1
                if element["data"]["subject_type"] == "kanji":
                    kanji += 1
                    if element["data"]["srs_stage"] == 8:
                        kanji_burn += 1
                if (
                    element["data"]["subject_type"] == "vocabulary"
                    or element["data"]["subject_type"] == "kana_vocabulary"
                ):
                    vocabulary += 1
                    if element["data"]["srs_stage"] == 8:
                        vocabulary_burn += 1

        if available_after == limit_time:
            no_review = {"time": 0}
            return no_review
        if not result:
            current = next_time
            continue
        else:

            local_tz = tzlocal.get_localzone()
            local_time = available_after.astimezone(local_tz).strftime("%H:%M")

            future_review = {
                "time": local_time,
                "total": len(result),
                "radicals": radicals,
                "kanji": kanji,
                "vocabulary": vocabulary,
                "radicals_burn": radicals_burn,
                "kanji_burn": kanji_burn,
                "vocabulary_burn": vocabulary_burn,
            }

            return future_review
