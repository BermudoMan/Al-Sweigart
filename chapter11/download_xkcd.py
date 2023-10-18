#! python3
# download_xkcd.py -загружает все комиксы xkcd

import requests, os, bs4

url = 'https://xkcd.com' # начальный url
os.makedirs('xkcd', exist_ok=True) # куда сохранять

while not url.endswith('#'):
    # загрузка страницы
    print('Загружается страница %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, features="html.parser")

    # поиск url изображения комикса
    comic_elem = soup.select('#comic img')
#    print(comic_elem)
    if comic_elem == []:
        print('Нет изображения')
    else:
        comic_url = comic_elem[0].get('src')
        print(comic_url)
        # загрузка изображения
        print('Загружается изображение %s...' % (comic_url))
        res = requests.get('https:' + comic_url)
#        print(res)
        res.raise_for_status()

        # Сохранение изображения в папке xkcd
        image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
        for chunk in res.iter_content(100000):
            image_file.write(chunk)
        image_file.close()

    # получение url кнопки Prev.
    prev_link = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prev_link.get('href')

print('Готово')