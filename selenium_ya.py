import time
import re
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from settings import YA_LOGIN, YA_PASS


def correct_login(login_=YA_LOGIN):
    return len(re.findall(r"\w[\w\d]+@.*", login_)) == 1


def selenium_login(login_=YA_LOGIN, password_=YA_PASS):
    if correct_login(login_):
        try:
            result = dict()

            options = webdriver.ChromeOptions()
            options.add_argument('--disable-blink-features=AutomationControlled')
            options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                                 'like Gecko) Chrome/111.0.0.0 Safari/537.36')
            # options.add_argument('--headless')

            driver = webdriver.Chrome(
                service=Service(ChromeDriverManager().install()),
                options=options)

            driver.get('https://passport.yandex.ru/auth/')
            time.sleep(3)
            elem = driver.find_element('name', 'login')
            elem.send_keys(login_)
            elem.send_keys(webdriver.common.keys.Keys.ENTER)
            time.sleep(3)
            result['login'] = driver.current_url
            elem = driver.find_element('name', 'passwd')
            elem.send_keys(password_)
            elem.send_keys(webdriver.common.keys.Keys.ENTER)
            time.sleep(3)
            result = driver.current_url
            return result
        except Exception as ex:
            print(ex)
        finally:
            driver.close()
            driver.quit()


if __name__ == '__main__':
    print(correct_login())
