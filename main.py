import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

chrome_driver_path = "C:\Development\chromedriver_win32\chromedriver.exe"

ser = Service(executable_path=chrome_driver_path)

GOOGLE_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSfD4cAmJLXLU-L9wqpjJwQO7wEPg5ZVK311qf09JFzI7tJhDA/viewform" \
              "?usp=sf_link "
ZILLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C" \
             "%22mapBounds%22%3A%7B%22west%22%3A-122.8563026328125%2C%22east%22%3A-122.0103553671875%2C%22south%22" \
             "%3A37.491439942495816%2C%22north%22%3A38.05805731365078%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState" \
             "%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B" \
             "%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C" \
             "%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value" \
             "%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C" \
             "%22isListVisible%22%3Atrue%7D "

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url=ZILLOW_URL, headers=headers)
zillow_content = response.text

soup = BeautifulSoup(zillow_content, "html.parser")

price_list = [price.text.split("/")[0].split("+")[0] for price in soup.find_all(class_="list-card-price")]
link_list = [link['href'] for link in soup.find_all(class_="list-card-link list-card-link-top-margin list-card-img",
                                                    href=True)]
address_list = [add.text for add in soup.find_all(class_="list-card-addr")]

driver = webdriver.Chrome(service=ser)
driver.get(GOOGLE_FORM)

i = 0
while i < len(price_list):
    time.sleep(2)
    addr_question = driver.find_element(by="xpath",
                                        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div['
                                              '1]/div/div[1]/input')
    price_question = driver.find_element(by="xpath",
                                         value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div['
                                               '1]/div/div[1]/input')
    link_question = driver.find_element(by="xpath",
                                        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div['
                                              '1]/div/div[1]/input')
    submit_btn = driver.find_element(by="xpath",
                                     value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    addr_question.send_keys(address_list[i])
    price_question.send_keys(price_list[i])
    link_question.send_keys(link_list[i])
    submit_btn.click()
    i += 1
    time.sleep(1)
    driver.find_element(by="xpath", value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()

