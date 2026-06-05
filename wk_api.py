import datetime
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

    return headers

def get_user_level():
    user_request = "https://api.wanikani.com/v2/user"
    user_response = requests.get(user_request, headers=headers)

    if user_response.status_code == 200:
        user_data = user_response.json()
        user_level = user_data["data"]["level"]
        return user_level
    elif user_response.status_code == 401:
        raise Exception("invalid API Key")
    else:
        raise Exception("exception")


def get_assignments():
    assignment_request = "https://api.wanikani.com/v2/assignments"

    assignment_items = []
    now = datetime.datetime.now(datetime.timezone.utc)

    while assignment_request:
        assignment_response = requests.get(assignment_request, headers=headers)

        if assignment_response.status_code == 200:
            assignment_data = assignment_response.json()

            for assignment in assignment_data["data"]:
                available_at_str = assignment["data"].get("available_at")
                assignment_type = assignment["data"].get("subject_type")

                if assignment_type == "kanji" or assignment_type == "radical":
                    if available_at_str:
                        available_at = datetime.datetime.fromisoformat(available_at_str.replace("Z", "+00:00"))

                        if available_at <= now:
                            assignment_items.append(assignment["data"].get("subject_id"))

            next_url = assignment_data.get("pages", {}).get("next_url")

            if next_url:
                assignment_request = next_url
            else:
                assignment_request = None
        else:
            raise Exception(f"HTTP error: {assignment_response.status_code}")
    return assignment_items


def get_items_to_review(user_level, assignment_items):
    subjects_request = f"https://api.wanikani.com/v2/subjects?levels={user_level}"
    subjects_response = requests.get(subjects_request, headers=headers)

    items_to_review = []

    if subjects_response.status_code == 200:
        subject_data = subjects_response.json()

        for subject in subject_data["data"]:
            current_level_subject_id = subject["id"]

            for item in assignment_items:
                if item == current_level_subject_id:
                    items_to_review.append(subject["data"])
        return items_to_review
    else:
        raise Exception(f"Error with status code: {subjects_response.status_code}")