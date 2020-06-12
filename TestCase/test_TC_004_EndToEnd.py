from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.common.by import By
from Pages import *
from Base import InitiateDriver
from Library import configReader
import time
import pytest
from DataGen import *


@pytest.mark.parametrize('data', dataGenBillingAddress.dataGeneratorBillingAddress())
def test_e2e(data):
    login(data)
    addItems()
    checkOut()
    BillingAddress(data)
    shipping_Address()
    shipping_Method()
    payment_Method()
    payment_Info()
    confirm_Order()


def login(data):
    global driver1
    driver1 = InitiateDriver.startBrowser()
    log = loginPage.loginPageClass(driver1)
    log.loginLink()
    log.emailId(data[0])
    log.password(data[1])
    log.loginBut()


def addItems():
    addi = addtoshoppincartPage.addToCartClass(driver1)
    addi.bookLink()
    addi.additems()
    addi.moveToCart()


def checkOut():
    chk = checkOutPage.checkOutClass(driver1)
    chk.countrySet()
    chk.TAC()
    chk.checkOutBut()


#('data', dataGenBillingAddress.dataGeneratorBillingAddress())
def BillingAddress(data):
    ba = billingAddress.billingAddressClass(driver1)
    #ba.enterCompany(data[2])
    #ba.enterCountry()
    #ba.enterCity(data[3])
    #ba.address(data[4], data[5])
    #ba.zip(data[6])
    #ba.phoneFax(data[7], data[8])
    ba.ContniueBut()



def shipping_Address():

    wait = WebDriverWait(driver1, 5)
    wait.until(ec.element_to_be_clickable((By.XPATH, configReader.readElementData('ShippingAddress', 'continue_but'))))
    sh = shippingAddress.shippindAddressClass(driver1)
    sh.continuebut()




def shipping_Method():
    wait = WebDriverWait(driver1, 5)
    wait.until(ec.element_to_be_clickable((By.XPATH, configReader.readElementData('ShippingMethod', 'continue_but'))))
    sh1 = shippingMethod.shippingMethodClass(driver1)
    sh1.shipMethod()
    sh1.ContniueBut()



def payment_Method():
    wait = WebDriverWait(driver1, 5)
    wait.until(ec.element_to_be_clickable((By.XPATH, configReader.readElementData('Paymentmode', 'continue_but'))))
    pm = paymentMethod.paymentMethodClass(driver1)
    pm.paymentmeth()
    pm.ContniueBut()



def payment_Info():
    wait = WebDriverWait(driver1, 5)
    wait.until(ec.element_to_be_clickable((By.XPATH, configReader.readElementData('PaymentInfo', 'continue_but'))))
    payi = paymentInfo.paymentInfoClass(driver1)
    payi.ContniueBut()



def confirm_Order():
    wait = WebDriverWait(driver1, 5)
    wait.until(ec.element_to_be_clickable((By.XPATH, configReader.readElementData('ConfirmOrder', 'continue_but'))))
    cono = confirmOrder.confirmOrderClass(driver1)
    cono.ContniueBut()
