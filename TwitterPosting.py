from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Twitter():
    def typing(self):
        url = "https://twitter.com/"
        driver = webdriver.Firefox(executable_path=r'/Users/laiwei/Desktop/WebScrapping/geckodriver')
        driver.implicitly_wait(30)
        driver.get(url)
        driver.maximize_window()


        login=driver.find_element_by_class_name("js-login")
        login.click()
        time.sleep(2)

        userName = driver.find_element(By.XPATH, "//*[@id='login-dialog-dialog']/div[2]/div[2]/div[2]/form/div[1]/input")
        userName.clear()
        userName.send_keys("Your account")

        time.sleep(1)

        password = driver.find_element(By.XPATH, "//*[@id='login-dialog-dialog']/div[2]/div[2]/div[2]/form/div[2]/input")
        password.clear()
        password.send_keys("Your password")

        time.sleep(1)
        confirm = driver.find_element(By.XPATH, "//*[@id='login-dialog-dialog']/div[2]/div[2]/div[2]/form/input[1]")
        confirm.click()
        time.sleep(1)

        for loop in range(5):
            post = driver.find_element(By.XPATH, "//*[@id='global-new-tweet-button']")
            post.click()
            time.sleep(1)


            content =  driver.find_element(By.XPATH, "//*[@id='tweet-box-global']")
            content.clear()
            content.send_keys("automated testing post "+ str(loop))
            time.sleep(1)

            submit = driver.find_element(By.XPATH, "//*[@id='global-tweet-dialog-dialog']/div[2]/div[4]/form/div[3]/div[2]/button/span[1]")
            submit.click()
            time.sleep(1)


twitter = Twitter()
twitter.typing()