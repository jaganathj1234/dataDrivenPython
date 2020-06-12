from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from Base import InitiateDriver
from Library import configReader
from Pages import registrationPage
import openpyxl
import pytest
from DataGen import dataGenRegister


@pytest.mark.parametrize('data', dataGenRegister.dataGeneratorRegister())
def ValidateRegistration(data):
    driver1 = InitiateDriver.startBrowser()
    register = registrationPage.registrationPageClass(driver1)
    register.registerLink()
    register.enterGender()
    register.enterFirstName(data[0])
    register.lastName(data[1])
    register.emailId(data[2])
    register.password(data[3])
    register.confirmPass(data[4])
    register.registerButton()
    # InitiateDriver.closeBrowser()
