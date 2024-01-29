import requests
import img2pdf

# Посмотреть ответы страницы и найти картинку которую присылает сервер и взять ее url


def get_data():
    headers = {
        'Accept': '*/*',
        'User_agent': "..."
    }

    img_list = []
    for i in range(1, 49):  # 49 картинок
        url = f'kakayota_ssylka{i}'.jpg
        req = requests.get(url, headers=headers)
        responce = req.content

        with open(f"media/{i}.jpg", 'wb') as file:
            file.write(responce)
            img_list.append(f"media/{i}.jpg")
    with open("result.pdf", "wb") as file:
        file.write(img2pdf.convert(img_list))


def main():
    get_data()


if __name__ == '__main__':
    main()
