import os
import datetime
import requests

from plyer import notification
from dotenv import load_dotenv

load_dotenv()

headers = {
    "Authorization": f"Bearer {os.getenv("WK_API_KEY")}",
    "Wanikani-Revision": "20170710",
}

user_level = 0
available_items = []
items_to_review = []

now = datetime.datetime.now(datetime.timezone.utc)

# User data
user_request = "https://api.wanikani.com/v2/user"
user_response = requests.get(user_request, headers=headers)

if user_response.status_code == 200:
    user_data = user_response.json()
    user_level = user_data['data']['level']
else:
    print(f"Error with status code: {user_response.status_code}")


# Items data
assignment_request = "https://api.wanikani.com/v2/assignments"

while assignment_request:
    assignment_response = requests.get(assignment_request, headers=headers)

    if assignment_response.status_code == 200:
        assignment_data = assignment_response.json()

        for item in assignment_data['data']:
            available_at_str = item['data'].get('available_at')
            item_type = item['data'].get('subject_type')

            if item_type == "kanji" or item_type == "radical":
                if available_at_str:
                    available_at = datetime.datetime.fromisoformat(available_at_str.replace('Z', '+00:00'))

                    if available_at <= now:
                        available_items.append(item['data'].get('subject_id'))

        next_url = assignment_data.get('pages', {}).get('next_url')

        if next_url:
            assignment_request = next_url
            params = {}
        else:
            assignment_request = None

    else:
        print(f"HTTP error: {assignment_response.status_code}")
        break


subjects_request = f"https://api.wanikani.com/v2/subjects?levels={user_level}"
subjects_response = requests.get(subjects_request, headers=headers)

if subjects_response.status_code == 200:
    subject_data = subjects_response.json()

    for subject in subject_data['data']:
        current_level_subject_id = subject['id']

        for item in available_items:
            if item == current_level_subject_id:
                items_to_review.append(subject['data'])


print(f"User level: {user_level}")
print(f"Available items: {len(available_items)}")
print(f"Kanji and Radicals items to review: {len(items_to_review)}")

if len(items_to_review) > 0:
    notification.notify(
        title=f"You have {len(items_to_review)} critical items to review.",
        message=f"頑張れ！",
        app_name="WaniKani Notify",
        timeout=0,
    )
