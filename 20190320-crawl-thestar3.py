#! /usr/bin/python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from lxml import html

class AppCrawler:
    def __init__(self, starting_url, depth):
        self.starting_url = starting_url
        self.depth = depth
        self.apps = []
        
    def crawl(self):
        self.get_app_from_link(self.starting_url)
        return

    def get_app_from_link(self, link):
        symbol = link.split("=",1)[1] 
        start_page = requests.get(link)
        tree = html.fromstring(start_page.text)
        board = tree.xpath('//*[@id="slcontent_0_ileft_0_info"]/ul/div[1]/li[1]/text()')[0]
        name = tree.xpath('//h1[@class="stock-profile f16"]/text()')[0]
        code = tree.xpath('//li[@class="f14"]/text()')[1]
        fundamental = tree.xpath('//*[@id="slcontent_0_ileft_0_stockprofile_fundamentals_profiletxt"]/text()')
        date_announced = tree.xpath('//tbody[@id="slcontent_0_ileft_0_stockprofile_financialresult_tblFinancial"]//tr[1]/td[1]/text()')
        financial_year_end = tree.xpath('//*[@id="slcontent_0_ileft_0_stockprofile_financialresult_tblFinancial"]/tr[1]/td[2]/text()')
        qtr = tree.xpath('//*[@id="slcontent_0_ileft_0_stockprofile_financialresult_tblFinancial"]/tr[1]/td[3]/text()')
        period_end = tree.xpath('//*[@id="slcontent_0_ileft_0_stockprofile_financialresult_tblFinancial"]/tr[1]/td[4]/text()')
        revenue = tree.xpath('//*[@id="slcontent_0_ileft_0_stockprofile_financialresult_tblFinancial"]/tr[1]/td[5]/text()')
        pl = tree.xpath('//*[@id="slcontent_0_ileft_0_stockprofile_financialresult_tblFinancial"]/tr[1]/td[6]/text()')
        eps = tree.xpath('//*[@id="slcontent_0_ileft_0_stockprofile_financialresult_tblFinancial"]/tr[1]/td[7]/text()')
    
        data = (str(board[3:]) + ';' + str(symbol) + ';' + str(name) + ';' + str(code[3:]) + (str(fundamental)).strip("['']") + ';' + (str(date_announced)).strip("['']") + ';' +
        (str(financial_year_end)).strip("['']") + ';' + (str(qtr)).strip("['']") + ';' + (str(period_end)).strip("['']")
              + ';' + (str(revenue)).strip("['']") + ';' + (str(pl)).strip("['']") + ';' + (str(eps)).strip("['']") + "\n")
        print(data)
        with open("C:\\Users\\Wai Shin\\Desktop\\stock-financial-results.txt", "a") as f:
            f.write(data)

        return

alphabets = ["A","B", "C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0-9"]
#alphabets = ["A"]

for alphabet in alphabets:
    driver = webdriver.Chrome(executable_path=r"C:\Users\Wai Shin\Desktop\protgen\chromedriver_win32\chromedriver.exe")
    driver.get("https://www.thestar.com.my/business/marketwatch/stock-list/?alphabet=" + alphabet)
    companyLinks = driver.find_elements_by_xpath('//tr[@class="linedlist"]//a')
    for link in companyLinks:
           value = link.get_attribute('href')
           crawler = AppCrawler(value, 0)
           crawler.crawl()

