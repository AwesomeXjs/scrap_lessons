import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from pathlib import Path

# ============ ВАРИАНТ 1
# Если сайт не возвращает нужный html (с запретом на парсинг) - смотрим что принимает этот сайт и ищем html в запросах.
# Либо смотреть в JSe какие дивы добавляются изза запросов и каких


# def get_data(url):
#     headers = {
#         'Accept': '*/*',
#         'User_agen': ''
#     }

#     r = requests.get(url=url, headers=headers)
#     with open('index.html', 'w', encoding='utf-8') as file:
#         file.write(r.text)

#     # get hotels urls
#     r = requests.get('hotels_url_from_get', headers=headers)
#     soup = BeautifulSoup(r.text, 'lxml')
#     # выдергиваем из полученых блоков ссылки и уже с них берем данные


# def main():
#     get_data('url')


# if __name__ == '__main__':
#     main()


# ВАРИАНТ 2. SELENIUM
# Селениум + драйвер заходят в веб браузер на нужную страницу и сохраняют код


def get_data_with_selenium(url):
    options = webdriver.ChromeOptions()
    options.set_capability('general.useragent.override',
                           'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')

    try:
        driver = webdriver.Chrome(
            executable_path='./chromedriver',
            options=options
        )
        driver.get(url=url)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
        sleep(5)


def main():
    # get_data('url')

    get_data_with_selenium('https://www.tury.ru/hotels/most_luxe.php')


if __name__ == '__main__':
    main()
