import requests
from datetime import datetime
from download import download_image
import os


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
    download_epic(api_key)
    api_key=os.environ["NASA_APY_KEY"]


if __name__ == '__main__':
    main()
