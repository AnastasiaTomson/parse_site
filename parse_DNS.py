import urllib.request, csv
from bs4 import BeautifulSoup
nout = []
price = []


def csv_writer(rows, path):
    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        for line in rows:
            writer.writerow(line)


def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()


def parse(html):

    soup = BeautifulSoup(html, 'lxml')
    div = soup.find('div', class_="catalog-items-list view-list")
    for row in div.find_all('div', class_='catalog-item-inner catalog-product view-list has-avails'):
        cols = row.find_all('div')
        a = row.find('div', class_='price_g')
        name = cols[0].h3.text
        pr = a.span.text
        nout.append(name)
        price.append(pr)


def main(x):
    parse(get_html('https://www.dns-shop.ru/catalog/17a892f816404e77/noutbuki/?p='+str(x)+'&i=1'))


for i in range(1, 45):
    main(i)
rows = zip(nout, price)
path = "dict.csv"
csv_writer(rows, path)
