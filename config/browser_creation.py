import os
import pickle
from multiprocessing import Pool
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from chrome_options import chromeOptions_args
from webdriver_manager.chrome import ChromeDriverManager
from chrome_window_init import starter_driver
from definitions import ROOT_DIR

cookie_path = os.path.join(ROOT_DIR, "resources/cookies.txt")
list_path = os.path.join(ROOT_DIR, "resources/")


def save_cookie(driver):
    with open(cookie_path, 'wb') as filehandler:
        print(cookie_path)
        pickle.dump(driver.get_cookies(), filehandler)


def load_cookie(driver, path):
    with open(path, 'rb') as cookiesfile:
        cookies = pickle.load(cookiesfile)
        for cookie in cookies:
            driver.add_cookie(cookie)
    return driver


def create_browser_with_cookies(headless, url):
    if headless == 'n' or headless == 'N':
        driver = webdriver.Chrome(ChromeDriverManager().install())
    else:
        chromeOptions = chromeOptions_args.chromeOptions()
        driver = webdriver.Chrome(
            ChromeDriverManager().install(), chrome_options=chromeOptions)
    driver.implicitly_wait(5)
    driver.get('http://www.tiktok.com')
    driver = load_cookie(driver, cookie_path)
    driver.get(url)

    return driver
