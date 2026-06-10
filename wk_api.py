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
    radical = 0
    kanji = 0
    vocabulary = 0
    radical_burn = 0
    kanji_burn = 0
    vocabulary_burn = 0

    for query in query_list:
        assignment_request = f"https://api.wanikani.com/v2/assignments?{query}"

        while assignment_request:
            assignment_response = requests.get(assignment_request, headers=headers)

            if assignment_response.status_code == 200:
                assignment_data = assignment_response.json()

                for assignment in assignment_data["data"]:

                    assignment_type = assignment["data"].get("subject_type")
                    assignment_srs = assignment["data"].get("srs_stage")
                    if assignment_type == "radical":
                        radical += 1
                        if assignment_srs == 8:
                            radical_burn += 1
                    if assignment_type == "kanji":
                        kanji += 1
                        if assignment_srs == 8:
                            kanji_burn += 1
                    if (
                        assignment_type == "vocabulary"
                        or assignment_type == "kana_vocabulary"
                    ):
                        vocabulary += 1
                        if assignment_srs == 8:
                            vocabulary_burn += 1

                next_url = assignment_data.get("pages", {}).get("next_url")

                if next_url:
                    assignment_request = next_url
                else:
                    assignment_request = None
            else:
                raise Exception(f"HTTP error: {assignment_response.status_code}")

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
