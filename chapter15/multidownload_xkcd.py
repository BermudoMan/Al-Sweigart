#! python3
# multidownload_xkcd.py -загружает все комиксы xkcd с использованием нескольких потоков выполнения

import requests, os, bs4, threading
url = 'https://xkcd.com' # начальный url
os.makedirs('xkcd', exist_ok=True) # куда сохранять

def download_xkcd(start_comic, end_comic):
    for url_number in range(start_comic, end_comic):
        # загрузка страницы
        print('Загрузка страницы https://xkcd.com/%s...' % (url_number))
        res = requests.get('https://xkcd.com/%s' % (url_number))
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

#    # получение url кнопки Prev.
#    prev_link = soup.select('a[rel="prev"]')[0]
#    url = 'https://xkcd.com' + prev_link.get('href')

# создание и запуск объектов thread
download_threads = [] # список всех объектов thread
for i in range(0, 1400, 100): # 14 итераций, создающих 14 потоков
    download_thread = threading.Thread(target=download_xkcd, args=(i, i + 99))
    download_threads.append(download_thread)

# ожидание завершения всех потоков выполнения
for download_thread in download_threads:
    download_thread.join()
print('Готово')