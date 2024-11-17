# Космический Телеграм
Проект создан для загрузки изображений космоса, запуска космических кораблей и планеты "Земля".
Программа создаёт отдельные директории для каждого набора изображений автоматически, без участия пользователя.


## Как установить
Скачайте необходимые файлы, затем используйте рiр (или рiр3 ‚ если есть конфликт с Python2) для установки
зависимостей и установить зависимости. Зависимости можно установить командой, представленной ниже.
Создайте бота у отца ботов. Создайте новый канал в Telegram.

Python3 должен быть уже установлен.Затем используйте pip (или pip3, есть есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
## Пример запуска
Для запуска скрипта у вас уже должен быть установлен Python3.
Для получения необходимых изображений необходимо написать:
```
python tgBot.py
```
Чтобы загрузить фотографии из конкретного запуска, нужно передать функции Fetch_spacex_last_launch ID
запуска в аргументе `--id` при запуске скрипта:
```
python fetch_spacex_images.py
```
где `launch_id`- ID запуска, из которого нужно загрузить фотографии. Если аргумент `--launch` не указан, будут
загружены фотографии из последнего запуска.

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Переменные окружения - это переменные,
значения которых присваиваются программе Рупоп извне. Чтобы их определить, создайте файл `.env` с

`tgBpt.py` и запишите туда данные в таком формате: ПЕРЕМЕННАЯ = значение.

Пример содержания файла `.env`:
```
NASA_API_KEY = "nasa-token"
TG_TOKEN = "bot-token"
TG_CHAT_ID = "@chat_id"
```
Получить токен `NASA_APY_KEY` можно получить на сайте NASA. Получить токен `TG_TOKEN` можно получить у отца ботов.В описании канала получите название и роложите в переменную `TG_CHAT_IG`

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.
