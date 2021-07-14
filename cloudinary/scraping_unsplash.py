import os
import requests
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor

load_dotenv()
ACCESS_KEY = os.environ.get("ACCESS_KEY")

# URL = "https://unsplash.com/t/architecture"
URL = "https://api.unsplash.com/search/photos"


def download_image(session, id, img_url):
    request = session.get(img_url)
    filepath = f"./pictures/{id}.jpg"
    if request.status_code == 200:
        with open(filepath, "wb") as f:
            f.write(request.content)


payload = {"client_id": ACCESS_KEY,
           "per_page": 30,
           "query": "architecture",
           "orientation": "landscape"
           }

with ThreadPoolExecutor(max_workers=10) as executor:
    with requests.Session() as session:
        r = session.get(URL, params=payload)
        raw_data = r.json()["results"]
        # print(r.text)

        for data in raw_data:
            id = data["id"]
            img_url = data["urls"]["full"]
            executor.submit(download_image, session, id, img_url)
