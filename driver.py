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

    headless = input()
    # -----Create Starter Driver -----
    url = 'http://www.tiktok.com/@{}'.format('lifeof_al')
    d1 = chrome_window_init.starter_driver('lifeof_al', 'TangoTango0722!', headless)

    browser_creation.save_cookie(d1.driver)
    # print('Closing initial driver')

    
    d1.driver.close()
    


if __name__ == '__main__':
    main()
    
