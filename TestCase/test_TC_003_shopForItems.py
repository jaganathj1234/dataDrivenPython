from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from Base import InitiateDriver
from Library import configReader
import time
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Pages import addtoshoppincartPage


def addItemsToCart():
    driver1 = InitiateDriver.startBrowser()
    driver1.execute_script("window.scrollTo(0, 200);")
    shopcart = addtoshoppincartPage.addToCartClass(driver1)
    shopcart.bookLink()
    shopcart.additems()
    driver1.execute_script("window.scrollTo(0, 0);")
    shopcart.moveToCart()
    driver1.close()



    #
    #driver1.execute_script("window.scrollTo(0, 400);")

    #
