import requests
from download import download_images


def fetch_spacex_last_launch():
    url = "https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a"
    response = requests.get(url)
    response.raise_for_status()
    url_images = response.json()["links"]["flickr"]["original"]

    for image_number, image in enumerate(url_images):
        download_images(image, f"images/spacex{image_number}.jpg")


def main():
    fetch_spacex_last_launch()


if __name__ == '__main__':
    main()