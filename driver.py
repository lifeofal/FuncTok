from selenium.webdriver.remote import switch_to
from config import *

def main():
    #----------------------------------------------------------------------------------#
    #   Driver to initialize starter window. User will have menu to choose different
    #   info retrieval actions. Actions like Follower/Following comparison will run in
    #   multiprocessing module.
    #
    #
    # Created by Alejandro Cervantes (4/25/2021)
    #----------------------------------------------------------------------------------#

    print("Welcome to FuncTok")

    # ----------User Menu---------#

    print("""
________ ___  ___  ________   ________ _________  ________  ___  __       
|\  _____\\  \|\  \|\   ___  \|\   ____\\___   ___\\   __  \|\  \|\  \     
\ \  \__/\ \  \\\  \ \  \\ \  \ \  \___\|___ \  \_\ \  \|\  \ \  \/  /|_   
 \ \   __\\ \  \\\  \ \  \\ \  \ \  \       \ \  \ \ \  \\\  \ \   ___  \  
  \ \  \_| \ \  \\\  \ \  \\ \  \ \  \____   \ \  \ \ \  \\\  \ \  \\ \  \ 
   \ \__\   \ \_______\ \__\\ \__\ \_______\  \ \__\ \ \_______\ \__\\ \__\\
    \|__|    \|_______|\|__| \|__|\|_______|   \|__|  \|_______|\|__| \|__|
                                                                           
                                                                           
                                                                           
    
     Created by Alejandro Cervantes
    
    -----------------------------------------------------------------------------------------
    """)

    print("""
    
    Enter Credentials
    
                    Disclaimer: 
    InstaInfo does not save you username or password.
    InstaInfo is also not responsible for your account.
    """)
    #user = input("Username: ")
    #pw = input("Password: ")

    #answer = int(input())

    print("""
    Would you like to run in Headless mode? (y/n)
    
    
    
    """)

    HEADLESS = input()
    # -----Create Starter Driver -----
    url = 'http://www.tiktok.com/@{}'.format('lifeof_al')
    d1 = chrome_window_init.starter_driver('lifeof_al', 'TangoTango0722!', HEADLESS)

    while (d1.BROWSER_STATUS == -1):
        d1.driver.close()
        main()

    

    browser_creation.save_cookie(d1.driver)
    # print('Closing initial driver')

    print("Log in successful.. What task should FuncTok run? :)")

    USER_CHOICE = input("""
    
    1. Unliker (Unlikes all posts in your liked section. Cannot undo this!)
    
    2. Coming Soon

    3. Coming Soon
    
    """)

    if(USER_CHOICE is 1):
        pass




    d1.driver.close()
    


if __name__ == '__main__':
    main()
    
