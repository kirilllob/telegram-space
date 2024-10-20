import telegram
import random
import os
from time import sleep


def main():
    bot = telegram.Bot(token="7913301689:AAGELmKkdM2fDvWpqfDATB4JeNKqXoBsO3M")
    while True:
        pictures = os.listdir("images")
        random.shuffle(pictures)
        for picture in pictures:
            file_path = os.path.join("images", picture)
            with open(file_path, "rb") as file:
                bot.send_photo(chat_id="@download_space_foto", photo=file)
            sleep(4200)


if __name__ == '__main__':
    main()