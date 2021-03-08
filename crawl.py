import requests
from bs4 import BeautifulSoup
import json
import sqlite3
conn = sqlite3.connect('familug.db')
conn.commit()

def craw_data(label):
    link = 'https://www.familug.org/search/label/'
    conn.execute('CREATE TABLE {} (title text, link text);'.format(label))
    r = requests.get(link + label)
    tree = BeautifulSoup(markup=r.text)
    data = tree.find_all(attrs={'class':'post-title entry-title'})
    for value in data:
        conn.execute("INSERT INTO {} VALUES ('{}', '{}')".format(label, value.text, value.a.get('href')))
        conn.commit()


def craw_latest():
    link = 'https://www.familug.org/search/'
    conn.execute('CREATE TABLE latest(title text, link text);')
    r =requests.get(link)
    tree = BeautifulSoup(markup=r.text)
    data = tree.find_all(attrs={'class':'post-title entry-title'}, limit=10)
    for value in data:
        conn.execute("INSERT INTO latest VALUES('{}', '{}');".format(value.text, value.a.get('href')))
        conn.commit()
    

def main():
    labels = ['Python', 'Command', 'sysadmin']
    for label in labels:
        craw_data(label)
    craw_latest()


if __name__ == "__main__":
    main()
