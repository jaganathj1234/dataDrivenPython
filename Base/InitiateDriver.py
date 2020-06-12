from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from Library import configReader


def startBrowser():
    global driver1
    if (configReader.readConfigData('Details', 'Browser') == 'Chrome'):

        path = "./Driver/chromedriver.exe"
        driver1 = Chrome(executable_path=path)

    elif (configReader.readConfigData('Details', 'Browser') == 'Firefox'):
        path = "./Driver/geckodriver.exe"
        driver1 = Firefox(executable_path=path)

    driver1.get(configReader.readConfigData('Details', 'Url'))
    driver1.maximize_window()
    return driver1

def closeBrowser():
    driver1.close()
