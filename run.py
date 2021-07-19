import time
import pyautogui as pag

from selenium import webdriver

h = 75
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
# options.add_argument("user-data-dir=./chromeprofile")
options.add_argument('--disable-extensions')
options.add_argument("--incognito")
options.add_argument("--disable-infobars")
options.add_argument("--disable-plugins-discovery")
options.add_argument("--start-maximized")
driver = webdriver.Chrome("./chromedriver.exe", options=options)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    const newProto = navigator.__proto__
    delete newProto.webdriver
    navigator.__proto__ = newProto
    """
})

print(driver.title)


def login():
    print('login')
    driver.get('https://rollercoin.com/game')
    time.sleep(3)
    mail = driver.find_element_by_id('mail')
    mail.send_keys('artur.hatoka@yandex.ru')
    password = driver.find_element_by_id('password')
    password.send_keys('12902389Fhxb!')
    keep = driver.find_element_by_id('keepSigned').location
    time.sleep(1)
    pag.click(keep['x'], keep['y'] + h)

    try:
        geetest = driver.find_element_by_class_name('geetest_ring').location
        time.sleep(1)
        pag.click(geetest['x'], geetest['y'] + h)
    except:
        login()
    finally:
        print('success')


def go_to_game():
    driver.get('https://rollercoin.com/game/choose_game')
    time.sleep(3)
    try:
        game = driver.find_element_by_css_selector('.choose-game-item button').location
        pag.click(game['x'], game['y'] + h)
    finally:
        print('go game')


login()
time.sleep(15)
go_to_game()
