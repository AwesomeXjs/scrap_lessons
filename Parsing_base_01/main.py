

# pip install beautifulsoup4 lxml
# from bs4 import BeautifulSoup
# import requests
# import re


# with open('bolvanka/index.html') as file:
#     src = file.read()


# soup = BeautifulSoup(src, 'lxml')


# ДЛЯ КИРИЛЛИЦЫ
# url = 'https://www.cyberforum.ru/python-beginners/thread2961078.html'

# req = requests.get(url)

# print("Declared Encoding:", req.encoding)
# req.encoding = 'windows-1251'
# print("Redeclared Encoding:", req.encoding)

# print(req.text)
# soup = BeautifulSoup(html, 'lxml')

# print(soup)
# title = soup.title
# print(title)  # <title>Mogo</title>
# print(title.text)  # Mogo


# # .find()  .find_all()
# page_h1 = soup.find('h1')  # находит первый элемент h1
# print(page_h1)  # <h1 class="intro__title">Welcome to MoGo</h1>
# print(page_h1.text)  # Welcome to MoGo

# # находит все нужные обьекты и помещает их в список
# # page_all_h1 = soup.find_all('h1')
# # print(page_all_h1)

# # for item in page_all_h1:
# #     print(item.text)

# # ===============если в коде только в нужном диве все нужные классы то див можно не указывать
# all_titles = soup.find('div', class_='slider__inner')
# # =================возвращает блок кода в интерпритации Python (обьект soup)
# print(all_titles.text.strip())


# # =========углубление в блок кода
# all_titles = soup.find('div', class_='slider__inner').find(
#     'span', class_='slider__text')

# print(all_titles.text.strip())  # Intro

# # ===================передача с помощью словаря
# stats = soup.find('div', {'class': 'stat'}).find_all(
#     'div', class_='stat__text')


# new = [item.text for item in stats]
# # ['Web Design Projects', 'happy client', 'award winner', 'cup of coffee', 'members']
# print(new)


# ======== парсинг атрибутов (href, class  и тд) Метод get
# social_links = soup.find('div', class_='social').find_all('a')
# print(social_links)

# for item in social_links:
#     text = item.text.strip()
#     url = item.get('href')
#     url = item['href']  # упрощенная запись
#     # facebook.com twitter.com pinterest.com instagram.com
#     print(f"{text} : {url}")


# find_parent()  find_parrents()
# находит блок родителя - find_parrent()
# находит все блоки вплоть до боди и html тега - find_parrents()

# post_div = soup.find('a', class_='nav__link').find_parent("nav")
# print(post_div)


# post_div = soup.find('a', class_='nav__link').find_parents("div")
# print(post_div)


# =========== next_element  .previous_element
# следующий элемент в иерархии

# find_el = soup.find('nav', class_='nav').next_element.next_element.text
# find_el = soup.find('nav', class_='nav').find_next().text
# print(find_el)  # <a class="nav__link" data-scroll="#about" href="#">About</a> // About


# =======find_next_sibling()  .find_previous_sibling()
# ищут и возвращают след и пред элементы внутри искомого (текущего) блока
# next_sib = soup.find(class_='header__logo').find_next_sibling()
# print(next_sib)

# prev_sib = next_sib.find_previous_sibling()
# print(prev_sib)


# # комбинирование методов
# prac = soup.find(class_='header__logo').find_next_sibling().find_next().text
# print(prac)  # About


# поиск по словам с помощью re
# re_search = soup.find_all('div', text=re.compile('consectetur'))

# print(re_search)
# чтобы поиск выполнялся в разных регистрах:
# re_search = soup.find_all(string=re.compile('([Оо]дежда)'))
# print(re_search)
# re_search = soup.find_all(string=re.compile('([Aa]bout)'))
# print(re_search)
