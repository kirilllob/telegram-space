from urllib.parse import unquote, urlparse
import requests
import os
from download import download_images


def split_get(url):
    decoding_url = unquote(url)
    parsed_url = urlparse(decoding_url)
    path, full_name = os.path.split(parsed_url.path)
    name, extension = os.path.splitext(full_name)
    return name, extension


def download_nasa(api_key):
    payload = {"api_key":api_key, "count":30}
    url = "https://api.nasa.gov/planetary/apod"
    response = requests.get(url, params=payload)
    response.raise_for_status()
    apod_params = response.json()

    for apod in apod_params:
        if apod.get("media_type") == "image":
            apod_link_image = apod["url"] or apod["hdurl"]
        name, extension = split_get(apod_link_image)
        download_images(apod_link_image, f"images/{name}{extension}")


def main():
    api_key = os.environ["NASA_APY_KEY"]
    download_nasa(api_key)


if __name__ == '__main__':
    main()
