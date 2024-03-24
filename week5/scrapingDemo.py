import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

driver = webdriver.Firefox()
page = driver.get("https://jgifford.dev")
page_source = driver.page_source
portfolioSoup = BeautifulSoup(page_source, "html5lib")

links = portfolioSoup.find_all("href")

print(links)
