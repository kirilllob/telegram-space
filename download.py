import requests
import os


def download_image(url, filename, folder="images"):
    os.makedirs(folder, exist_ok=True)
    response = requests.get(url)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)
