import urllib.request, csv
from bs4 import BeautifulSoup
path = "street.csv"
street = []


def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()


def parse(html):
    soup = BeautifulSoup(html, 'lxml')
    div = soup.find('div', class_="row")
    for row in div.find_all('div', class_="col-xs-6 col-md-4"):
        cols = row.find_all('div')
        st = cols[0].a.text
        street.append(st)


def csv_writer(street, path):
    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter='\n')
        writer.writerow(street)


def main(x):
    parse(get_html('https://mapdata.ru/krim/kerch/ulicy/stranica-'+str(x)+'/'))


for i in range(1, 9):
    main(i)
csv_writer(street, path)
