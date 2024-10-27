import requests
import argparse
from download import download_images


def fetch_spacex_last_launch(launch_id):
    url = f"https://api.spacexdata.com/v5/launches/{launch_id}"
    response = requests.get(url)
    response.raise_for_status()
    url_images = response.json()["links"]["flickr"]["original"]

    for image_number, image in enumerate(url_images):
        download_images(image, f"images/spacex{image_number}.jpg")


def main():
    parser = argparse.ArgumentParser(description='этот скрипт позволяет скачивать фотографии spacex по указанному id запуска')
    parser.add_argument('--launch_id', type=str, help='укажите id запуска', default='5eb87d47ffd86e000604b38a')
    args = parser.parse_args()
    fetch_spacex_last_launch(args.launch_id)


if __name__ == '__main__':
    main()
