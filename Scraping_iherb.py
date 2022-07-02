import requests
import xlsxwriter
from bs4 import BeautifulSoup
import json
from time import sleep

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

r = requests.get('https://ua.iherb.com/', headers=headers)

soup = BeautifulSoup(r.text, 'lxml')


def one_block():
    sleep(3)

    data_0 = soup.find('div', class_='carousel-container product-carousel home-module').find('div',
                                                                                             class_='carousel slide iherb-carousel-items clearfix')
    data = data_0.find_all(class_='product-inner')

    items = []
    for i in data:
        name = i.find(class_='absolute-link-wrapper').find('div', class_='product-title').text.strip()
        rank = i.find('div', class_='rating').find('a', class_='rating-count').find('span').text + ' відгуків'
        price = i.find('div', class_='product-price').find('bdi').text

        items.append({
            'name': name,
            'rank': rank,
            'price': price,
        })

    book = xlsxwriter.Workbook('Promotions_1.xlsx')
    page = book.add_worksheet()

    row = 0
    colum = 0

    page.set_column('A:A', 60)
    page.set_column('B:B', 30)
    page.set_column('C:C', 30)

    for i in items:
        page.write(row, colum, i['name'])
        page.write(row, colum + 1, i['rank'])
        page.write(row, colum + 2, i['price'])
        row += 1

    book.close()


def two_block():
    sleep(3)

    data_0 = soup.find(class_='personalized-reorder').find('div', id='hp-module-trending').find(class_='carousel').find(
        'div', id='trending-inner')
    data = data_0.find_all(class_='product-inner')

    item = []
    for i in data:
        name = i.find(class_='absolute-link-wrapper').find('div', class_='product-title').text.strip()
        rank = i.find('div', class_='rating').find('a', class_='rating-count').find('span').text + ' відгуків'
        price = i.find('div', class_='product-price').find('bdi').text

        item.append({
            'name': name,
            'rank': rank,
            'price': price,
        })

    book = xlsxwriter.Workbook('Trend.xlsx')
    page = book.add_worksheet()

    row = 0
    colum = 0

    page.set_column('A:A', 60)
    page.set_column('B:B', 30)
    page.set_column('C:C', 30)

    for i in item:
        page.write(row, colum, i['name'])
        page.write(row, colum + 1, i['rank'])
        page.write(row, colum + 2, i['price'])
        row += 1

    book.close()


def three_block():
    sleep(3)

    data_0 = soup.find(id='hp-module-best-selling').find(
        class_='carousel-inner product-carousels rounded-product-cells col-xs-24 col-md-24')
    data = data_0.find_all(class_='product-inner')

    item = []
    for i in data:
        name = i.find(class_='absolute-link-wrapper').find('div', class_='product-title').text.strip()
        rank = i.find('div', class_='rating').find('a', class_='rating-count').find('span').text + ' відгуків'
        price = i.find('div', class_='product-price').find('bdi').text

        item.append({
            'name': name,
            'rank': rank,
            'price': price
        })

    book = xlsxwriter.Workbook('Hits.xlsx')
    page = book.add_worksheet()

    row = 0
    colum = 0

    page.set_column('A:A', 60)
    page.set_column('B:B', 30)
    page.set_column('C:C', 30)

    for i in item:
        page.write(row, colum, i['name'])
        page.write(row, colum + 1, i['rank'])
        page.write(row, colum + 2, i['price'])
        row += 1

    book.close()


def main():
    one_block()
    two_block()
    three_block()


if __name__ == '__main__':
    main()
