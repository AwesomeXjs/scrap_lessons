import json
import random
from pathlib import Path
from time import sleep


import requests
from bs4 import BeautifulSoup


def get_data(url):
    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0"
    }

    project_data_list = []
    itteration_count = 23
    print(f"Всего иттераций: #{itteration_count}")
    for item in range(1, 24):  # range - рейндж динамической табуляции
        req = requests.get(
            # item - динамическая переменная отвечающая за пагинацию, на каждой итерации будет запрос на отдельную страницу столько раз сколько у нас страниц
            url + f"&PAGEN_1={item}&PAGEN_2={item}", headers=headers)

        # Для каждой динамической пагинеции своя папка
        folder_name = f"data/data_{item}"

        if Path('.').joinpath(folder_name).exists:
            print('Папка существует!')
        else:
            Path('.').joinpath(folder_name).mkdir()

        # сохраням в отдельный файл чтобы не долбить реквесты
        with open(f'{folder_name}/project_{item}.html', 'w') as file:
            file.write(req.text)

        # читаем файл и сохраняем в переменную src
        with open(f'{folder_name}/project_{item}.html') as file:
            src = file.read()

        # src пердаем в soup  и находим в soup все нужные элементы
        soup = BeautifulSoup(src, 'lxml')
        articles = soup.find_all('articles', class_='ib19')

        # пробегаемся циклом по нужным элементам и вытаскиваем ссылки
        project_urls = []
        for article in articles:
            project_url = "http://www.edutainme.ru" + article.find(
                # в каждом элементе ищем дочерний див => дочерний а и берем ссылку
                'div', class_='txtBlock').find('a').get('href')
            project_urls.append(project_url)

        # бежим циклом по списку с сылками и вытягиваем в каждом ответе нужную информацию
        for project_url in project_urls[0:1]:
            req = requests(url, headers)

            # разбиваем ссылку на список где каждый элемент идет после "/" и вытягиваем оттуда имя
            project_name = project_url.split('/')[-2]

            with open(f"{folder_name}/{project_name}.html", 'w') as file:
                file.write(req.text)
            with open(f"{folder_name}/{project_name}.html") as file:
                src = file.read()

            soup = BeautifulSoup(src, 'lxml')
            # ищем нужный враппер
            project_data = soup.find(class_='inside')

            # нужное лого в враппере и забераем ее ссылку
            try:
                project_logo = "http://www.edutainme.ru" + project_data.find(
                    'div', class_='img_logo').find('img').get('src')
            except Exception:
                project_logo = 'No project logo'

            # нужное название проекта в враппере
            try:
                project_name = project_data.find(
                    class_='project_name').find('h1').text
            except Exception:
                project_name = 'No project name'

                # забираем нужный текст
            try:
                project_short_description = project_data.find(
                    class_='description').find('p').text

            except Exception:
                project_short_description = 'Project has no description'

            # забираем нужную ссылку на проект

            try:
                project_website = project_data.find(
                    'div', class_='txt').find('p').find('a').text
            except Exception:
                project_website = 'Project has no website'

            try:
                project_full_subscription = project_data.find(
                    'div', class_='textWrap').find('div', class_='rBlock').find('p').text
            except Exception:
                project_full_subscription = 'Project has no description'

            # добавляем на каждой иттерации словарь с данными в список
            project_data_list.append({
                "Имя проекта": project_name,
                "URL логотипа проекта": project_logo,
                "Короткое описание проекта": project_short_description,
                "Вебсайт проекта": project_website,
                "Полное описание проекта": project_full_subscription.strip()
            })
        itteration_count -= 1
        if itteration_count == 0:
            print('Сбор данных завершен')
            break
        print(f"Иттерация #{item} завершена, осталось иттераций {
              itteration_count}")
        sleep(random.randrange(2, 4))

        # Превращаем весь список словарей в JSON и сохраняем в файл
    with open('data/projects_data.json', 'w', encoding='utf-8') as file:
        json.dump(project_data_list, file, indent=4, ensure_ascii=False)


def main():
    get_data('URL из get запросса исключая ПАГИНАЦИЮ!!!')
    # как получить ссылку с пагинацией:

    # При достижении определенного места при скролле мы отсылпаем запрос на сервер с определенными параметрами где написана ссылка с пагинацией
    pass


# if __name__ == '__main__':
#     main('')


# ЗАМЕЧАНИЯ

# 1. Довольно странно постоянно сохранять html файл, потом открывать его и парсить данные из него (по сути просто лишние движения). Правильно будет просто использовать responce.text и доставать информацию оттуда (но возможно у заказчика было требования сохранить html файлы)
# 2. Хардкод пагинации может привести к тому что в будущем не все стартапы будут пасриться (на сайт банально добавят новые стартапы и пагинаций станет больше). Правильно будет проверять ответ на каждой итерации цикла, и если responce.status_code == 404 то выходим из цикла
# 3. Это уже ошибка в стиле написания кода. Абсолютно весь код находится в одной функции. Получения запроса с основного сайта и распарсивание карточек стартапов должно быть отдельно (для сумасшедших можно даже на 2 функции разбить). Парсинг данных со страницы стартапа так же должно производится отдельной функцией. Сохранения json, так же должно быть отдельной функцией.
# 4. Это скорее совет чем ошибка. На сайте не так много карточек, но если учесть что в будующем их вероятно станет больше (запросов станет больше), то код может выполняться несколько десятков минут. Если вы пишите парсер и либо он уже делает много запросов, либо есть вероятность что в будующем он будет делать много запросов, то просто необходимо использовать aiohttp (или любую другую асинхронную библиотеку). Если парсер одноразовый, это можно упустить.
# 5.Было бы правильно вывести базовый URL в отдельную переменную, а не копировать его к каждой относительной ссылке.
# 6. Считается неправильным отлавливать все исключения в блоке try except, так как если пользователь нажмёт CTRL+C, то это не прекратит работу программы, а выкинет исключение. Если вам нужно поймать конкретное исключение, укажите его в блоке except, если нужно отловить все (за исключением нажатия CTRL+C), то просто внутри блока except выполняйте проверку.
# 7. Заголовки лучше прописывать вне функции как константу (в ином случаи вы либо используете одну функцию на всю программу (что неправильно) либо копипастите headers в тело каждой функции)
# 8. Что бы не заниматься лишними телодвижениями, можно использовать XPATH для указания необходимого блока.
