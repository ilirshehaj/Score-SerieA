# Here are all the functions used to retrieve data from SofaScore for our purpose
import global_var
import pandas 
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import pdb

seriea_page = global_var.seriea_page

# Get HTML from a web address
def get_html(page):
    #create new driver
    driver = webdriver.Chrome()
    # get page source from driver
    driver.get(page)
    source = driver.page_source
    #get html from the source
    html = BeautifulSoup(source, 'html.parser')
    return html