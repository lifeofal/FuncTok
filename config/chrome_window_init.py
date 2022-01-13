from logging import log
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from config import chrome_options
from webdriver_manager.chrome import ChromeDriverManager


class starter_driver:

    def __init__(self, user, pw, answer) -> None:
        self.user = user
        self.chrome_options = chrome_options.chromeOptions()

        # Init headless or webbrowser run

        # headless is experimental

        if answer == 'n' or answer == 'N':
            print("Creating Driver - Browser")
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
        else:
            print("Creating Driver - Headless")
            self.driver = webdriver.Chrome(
                ChromeDriverManager().install(), options=self.chrome_options)

        self.driver.get("https://www.tiktok.com")
        self.driver.implicitly_wait(5)

        try:
            self.driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/div[2]/button").click()

        except Exception:
            print("xpath not found with: \"//*[@id=\"app\"]/div[1]/div/div[2]/button\"")
            print("Trying to log in with button path")
            self.driver.find_element_by_class_name("e13wiwn62 tiktok-1mm63h3-Button-StyledLoginButton ehk74z00").click()

        self.driver.find_element_by_xpath("//*[@id=\"root\"]/div/div[1]/div/div[1]/div[2]/div[2]/div[2]").click()
        self.driver.find_element_by_xpath("//*[@id=\"root\"]/div/div[1]/form/div[1]/a").click()

        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/form/div[2]/div/input').send_keys(self.user)
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/form/div[3]/div/input').send_keys(self.pw)
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/form/button').click()

        


