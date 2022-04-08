from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Login into the page
browser = webdriver.Chrome()
browser.get("https://autel-cloud-pc-web-base-prod.autel.com/home/accountLogin?redirectUrl=http%3A%2F%2Fre-us.autel."
            "com%2F&app_code=remoteexpert&fbclid=IwAR0Zmz3XZ3lkXwoqKmhn74FbffnllzDtwNiBxSp2mRVC20nKw1VNKoSjrGw/")
username = WebDriverWait(browser, 40).until(EC.presence_of_element_located((By.XPATH, "//input[@type='text']")))
username.send_keys("username")
password = browser.find_element(By.XPATH, "//input[@type='password']")
password.send_keys("password")
login = browser.find_element(By.CSS_SELECTOR, ".loginBtn")
login.click()

browser.maximize_window()

while True:
    # Grab order
    try:
        detail = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/'
                                                                                            'div[2]/div[2]/section/div/'
                                                                                            'div[1]/div[2]/div[2]/'
                                                                                            'div[5]/div[2]/table/tbody/'
                                                                                            'tr/td[11]/div/button[1]')))
        if detail:
            detail.click()
            time.sleep(5)

            grab = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/'
                                                                                          'div[2]/section/div/div[2]/div/'
                                                                                          'button')))
            grab.click()

            input_price = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]'
                                                                                                     '/div[2]/div[2]/'
                                                                                                     'section/div/div[5]/'
                                                                                                     'div/div[2]/div/div[2]'
                                                                                                     '/div[1]/div/div/'
                                                                                                     'input')))
            input_price.send_keys("100")
            time.sleep(2)

            confirm = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/"
                                                                                             "div[2]/div[2]/section/"
                                                                                             "div/div[5]/div/div[3]/div/"
                                                                                             "button[2]")))
            confirm.click()
            time.sleep(2)

            okay = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'OK')])"
                                                                                          "[1]")))
            okay.click()
            time.sleep(2)

            message = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div[2]/"
                                                                                             "div[2]/section/div/div[1]/"
                                                                                             "div[1]/div[2]/div[2]/div[2]/"
                                                                                             "img")))
            message.click()
            time.sleep(2)

            input_message = WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/"
                                                                                                       "div[1]/div[2]/"
                                                                                                       "div[2]/section/div/"
                                                                                                       "div[6]/div[3]/div/"
                                                                                                       "div/textarea")))
            input_message.send_keys("Hello, my name is Sheldon from Autel Remote Expert. "
                                    "If it's easier for you please text me at +17782277652 Thank you.")
            time.sleep(1)

            send = browser.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/section/div/div[6]/'
                                                  'div[3]/div/div/button')
            send.click()
            time.sleep(5)

            home = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/a")
            home.click()
        else:
            browser.refresh()
    except:
        pass
    browser.refresh()
