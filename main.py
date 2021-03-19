# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from selenium import webdriver
import requests
import time
import os
import re
import urllib.request
from urllib.request import urlretrieve

def obtenir_html():
    b=webdriver.Chrome()
    b.get('https://www.matchesfashion.com/fr/womens/shop/bags/tote-bags')
    data = b.page_source
    with open("test.txt", "wt", encoding='utf-8') as out_file:
        out_file.write(data)
    time.sleep(10)
    b.quit()


def precedure(k,p,l):
    per=100.0*k*p/l
    if per>100:
        per=100
    print('%.2f%%' % per)

def picture(jpgs):
    file_name = "matchesfashion.com_fr_womens_shop_bags_tote-bags"
    if not os.path.exists(file_name):
        os.mkdir(file_name)
    url= jpgs[0]
    dir=os.path.abspath('matchesfashion.com_fr_womens_shop_bags_tote-bags')
    work_path=os.path.join(dir, 'test.jpg')
    urlretrieve(url, work_path, precedure)

def marques(text):
    marques1=re.findall('%3A%3Adesigner%3A(.*?)" >', text)
    marques1=[marque+"\n" for marque in marques1]
    marques = list(set(marques1))
    marques.sort(key=marques1.index)
    if not os.path.exists("marques.txt"):
        os.mkdir("marques.txt")
    with open("marques.txt", "wt") as out_file:
        out_file.write("Il y a des marques:"+"\n")
        for marque in marques:
            print(marque)
            out_file.write(marque)
def main():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
    }
    with open("test.txt", "rt", encoding='utf-8') as in_file:
        text = in_file.read()
    source=re.findall('data-original="(.*?).jpg"', text)
    jpgs=[" http:"+jpg+".jpg" for jpg in source]
    print(jpgs)
    marques(text)
if __name__ == '__main__':
    main()
