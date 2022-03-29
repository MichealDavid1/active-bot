from selenium import webdriver
import time

# Login into the page
browser = webdriver.Chrome()
browser.get("https://autel-cloud-pc-web-base-prod.autel.com/home/accountLogin?redirectUrl=http%3A%2F%2Fre-us.autel."
            "com%2F&app_code=remoteexpert&fbclid=IwAR0Zmz3XZ3lkXwoqKmhn74FbffnllzDtwNiBxSp2mRVC20nKw1VNKoSjrGw/")
username = browser.find_element_by_xpath("//input[@type='text']")
username.send_keys("username")
password = browser.find_element_by_xpath("//input[@type='password']")
password.send_keys("password")
login = browser.find_element_by_css_selector(".loginBtn")
login.click()

browser.maximize_window()
time.sleep(16)

while True:
    # Grab order
    try:
        grab = browser.find_element_by_xpath("//body[1]/div[1]/div[1]/div[2]/div[2]/section[1]/div[1]/div[1]/div[2]/"
                                             "div[2]/div[5]/div[2]/table[1]/tbody[1]/tr[1]/td[11]/div[1]/button[2]/"
                                             "span[1]")

        grab.click()

        time.sleep(1)
        input_price = browser.find_element_by_xpath("//div[@class='price-input el-input el-input--medium "
                                                    "el-input-group el-input-group--prepend']//input[@type='text']")
        time.sleep(1)
        input_price.send_keys("85")
        time.sleep(1)
        confirm = browser.find_element_by_xpath("(//span[contains(text(),'Confirm')])[2]")
        confirm.click()
        time.sleep(1)
        okay = browser.find_element_by_xpath("(//span[contains(text(),'OK')])[1]")
        okay.click()
    except:
        pass

    browser.refresh()
    time.sleep(2)
