import requests
import bs4
from bs4 import BeautifulSoup as soup
import time
import os


url = "https://www.malaysiastock.biz/Market-Watch.aspx?type=A&value="
pages = ["A","B", "C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0"]

filename = str(time.strftime("stock_%Y%m%d.txt"))
f = open(filename,"w")

for page in pages:
 print('---', page, '---')
 uClient = requests.get(url + str(page))
 print(uClient)
 page_soup = soup(uClient.content, "html.parser")
 table = page_soup.find("table",{"id":"MainContent_tbStockWithAlphabet"})
 for row in table.findAll("tr"):
  cells = row.findAll("td")
  if len(cells) == 8:
   stock_code = cells[0].find(text=True)
   stock_name = cells[1].find(text=True)
   stock_ref = cells[2].find(text=True)
   stock_open = cells[3].find(text=True)
   stock_last = cells[4].find(text=True)
   stock_change = cells[5].find(text=True)
   stock_change_perc = cells[6].find(text=True)
   stock_volume = cells[7].find(text=True)
   f.write(stock_code + "|" + stock_name + "|" + stock_ref + "|" + stock_open + "|" + stock_last + "|" + stock_change + "|" + stock_change_perc + "|" + stock_volume + "\n")

f.close()

