import time
from os import wait
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from config import chrome_options
from webdriver_manager.chrome import ChromeDriverManager



class starter_driver:
    BROWSER_STATUS = 0

    def __init__(self, user, pw, answer) -> 'int':
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
        self.driver.implicitly_wait(6)

        try:
            time.sleep(10)
            self.driver.find_element_by_class_name(
                "captcha_verify_container style__CaptchaWrapper-sc-1gpeoge-0 rUVoM")
            print("PLEASE COMPLETE THE CAPTCHA IN ORDER TO CONTINUE")
            

        except NoSuchElementException:
            print("No Captcha detected.. Continuing")

    
        finally:
            time.sleep(10)

        try:
            self.driver.find_element_by_xpath(
                "//*[@id=\"app\"]/div[1]/div/div[2]/button").click()

        except NoSuchElementException:
            print(
                "xpath not found with: \"//*[@id=\"app\"]/div[1]/div/div[2]/button\"")
            print("Trying to log in with button path")
            self.driver.find_element_by_class_name(
                "e13wiwn62 tiktok-1mm63h3-Button-StyledLoginButton ehk74z00").click()

        finally:
            time.sleep(10)
        
        # try:

        #     self.driver.find_element_by_class_name(
        #         "captcha_verify_container style__CaptchaWrapper-sc-1gpeoge-0 rUVoM")
        #     print("PLEASE COMPLETE THE CAPTCHA IN ORDER TO CONTINUE")
            

        # except NoSuchElementException:
        #     print("No Captcha detected.. Continuing")

        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[1]/div/div[1]/div[2]/div[2]/div[2]").click()
        self.driver.find_element_by_xpath(
            "//*[@id=\"root\"]/div/div[1]/form/div[1]/a").click()

        self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[1]/form/div[2]/div/input').send_keys(self.user)
        self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[1]/form/div[3]/div/input').send_keys(self.pw)
        self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[1]/form/button').click()

        try:
            time.sleep(10)
            self.driver.find_element_by_class_name(
                "captcha_verify_container style__CaptchaWrapper-sc-1gpeoge-0 rUVoM")
            print("PLEASE COMPLETE THE CAPTCHA IN ORDER TO CONTINUE")
            

            try:
                self.driver.find_element_by_class_name(
                    "captcha_verify_container style__CaptchaWrapper-sc-1gpeoge-0 rUVoM")
                print(
                    "You did not complete the Captcha in time.. Program is resetting..")
                BROWSER_STATUS = -1
            except NoSuchElementException:
                pass
        except NoSuchElementException:
            print("No Captcha detected.. Continuing")

        print("Thank you.. Saving cookies for this page.. If you chose the option to save log in session, your profile should show up the next time you run FuncTok!")
        BROWSER_STATUS = 1
