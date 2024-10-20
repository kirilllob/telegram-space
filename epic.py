import requests
from datetime import datetime
from download import download_images


def download_epic():
    payload = {"api_key":"QiCsHOaKtCuOjPcGxtwU2j5fda66eGXyS3485lol", "count":30}
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for epic in response.json():
        date_image = epic["date"]
        date_image = datetime.fromisoformat(date_image).strftime("%Y/%m/%d")
        name_image = epic["image"]
        url_epic_images = f"https://api.nasa.gov/EPIC/archive/natural/{date_image}/png/{name_image}.png?api_key=QiCsHOaKtCuOjPcGxtwU2j5fda66eGXyS3485lol"
        download_images(url_epic_images, f"images/{name_image}.png")


def main():
    download_epic()


if __name__ == '__main__':
    main()