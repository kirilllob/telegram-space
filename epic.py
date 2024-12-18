import requests
from datetime import datetime
from download import download_image
import os
from dotenv import load_dotenv


def download_epic(api_key):
    payload = {"api_key":api_key, "count":30}
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for epic in response.json():
        date_image = epic["date"]
        date_image = datetime.fromisoformat(date_image).strftime("%Y/%m/%d")
        name_image = epic["image"]
        url_epic_images = f"https://api.nasa.gov/EPIC/archive/natural/{date_image}/png/{name_image}.png"
        download_image(url_epic_images, f"images/{name_image}.png", payload)


def main():
    load_dotenv()
    api_key=os.environ["NASA_APY_KEY"]
    download_epic(api_key)
    


if __name__ == '__main__':
    main()
