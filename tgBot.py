import telegram
import random
import os
from time import sleep
from dotenv import load_dotenv


def main():
    load_dotenv()
    bot = telegram.Bot(token=os.environ["TG_TOKEN"])
    departure_time = "4200"
    chat_id = os.environ["TG_CHAT_ID"]
    while True:
        pictures = os.listdir("images")
        random.shuffle(pictures)
        for picture in pictures:
            file_path = os.path.join("images", picture)
            with open(file_path, "rb") as file:
                bot.send_photo(chat_id=chat_id, photo=file)
            sleep(departure_time)


if __name__ == '__main__':
    main()

