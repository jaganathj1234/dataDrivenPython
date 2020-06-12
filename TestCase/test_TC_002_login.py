from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from Base import InitiateDriver
from Library import configReader
from Pages import loginPage
import openpyxl
import pytest
from DataGen import dataGenLogin


@pytest.mark.parametrize('data', dataGenLogin.dataGeneratorLogin())
def loginWebsite(data):
    driver1 = InitiateDriver.startBrowser()
    login = loginPage.loginPageClass(driver1)
    login.loginLink()
    login.emailId(data[0])
    login.password(data[1])
    login.loginBut()
    driver1.close()
