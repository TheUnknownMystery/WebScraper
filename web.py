from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import time
import pandas as pd
start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# opening the link we want to scrape with crome browser using selenium...
# Crome driver is a driver which will help us to open chrome browser
browser = webdriver.Chrome("C:/Users/sengu/Downloads/chromedriver")
browser.get(start_url)

# Letting the code sleep
time.sleep(40)


def Scrape():
    Headers = ["Index","Name", "Distance", "Mass", "Radius"]

    soup = BeautifulSoup(browser.page_source, "html.parser")
    Stars_Table = soup.find("table")

    tem_list = []

    table_rows = Stars_Table.find_all("tr")

    for tr in table_rows:
        td = tr.find_all("td")
        row = [i.text.rstrip() for i in td]
        # print(row)

        tem_list.append(row)
    Name     = []
    Distance = []
    Mass     = []
    Radius   = []
    for i in range(1, len(tem_list)):
        Name.append(tem_list[i][1])
        Distance.append(tem_list[i][3])
        Mass.append(tem_list[i][5])
        Radius.append(tem_list[i][6])
    df = pd.DataFrame(list(zip(Name, Distance, Mass, Radius)), columns=Headers)
    print(df)

    df.to_csv("Scraper.csv")
Scrape()
