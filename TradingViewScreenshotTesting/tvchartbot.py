"""
tvchartbot.py - Tradingview scraper module

Uses Selenium to open a headless Chrome window, look up a ticker, and return a screenshot of its chart.

Original script idea from:
https://stackoverflow.com/questions/51653344/taking-screenshot-of-whole-page-with-python-selenium-and-firefox-or-chrome-headl
"""
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from PIL import Image
import time


print('STARTING')


USER = "groupmebot"
PASS = "groupmebot1"


testing = False
# testing = True


url = "https://www.tradingview.com/chart/UzJ9PCY8/#"


class TradingViewScraper:
    def __init__(self):
        print("TradingViewScraper IS INIT'ing")
        self.testing = False
        self.driver = None

    def start(self):
        ### OPENING A HEADLESS BROWSER ###
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument(f"--window-size=800,800")
        chrome_options.add_argument("--hide-scrollbars")
        if not self.testing:
            chrome_options.binary_location = '/app/.apt/usr/bin/google-chrome'
            self.driver = webdriver.Chrome(chrome_options=chrome_options)
        else:
            self.driver = webdriver.Chrome("/Program Files/chromedriver", chrome_options=chrome_options)
        self.driver.get(url)

        ### LOGGING IN ###

        # finds "log in" hyperlink (if currently on error page)
        login = self.driver.find_element_by_class_name('js-login-link')
        print("Login:")
        print(login)
        login.click()

        # wait for js login prompt
        username = WebDriverWait(self.driver, 5, 0.05).until(
            EC.presence_of_element_located((By.NAME, 'username')))
        print("Username:")
        print(username)

        # find password
        password = self.driver.find_element_by_name('password')  # if username box is found, then password is visible too


        # put in da details
        username.send_keys(USER)
        password.send_keys(PASS)
        password.send_keys(Keys.RETURN)
        print("Login info entered")

        print("Sleeping for 4....")
        time.sleep(4)



        ### CHECK AUTHENTICATION ERROR MESSAGE ###
        try:
            max_device_dialog = self.driver.find_element_by_class_name('tv-dialog__modal-container')
            connect = max_device_dialog.find_element_by_css_selector('[data-name=no]')
            connect.click()
        except NoSuchElementException:
            print("No max_devices dialog box found.")


    def get_chart_screenshot_binary(self, parsedinput):
        # first, resolve the user's input
        rawsym = parsedinput[0]
        propersym = rawsym

        # add "USD" for the big blue chips
        if rawsym == 'eth' or rawsym == 'btc' or rawsym == 'xbt':
            propersym += 'usd'

        # if not sym.endswith('btc'): # ltcusdt
        #     # either:   1. no pair (just "xrp" or "doge")
        #     #           2. btc pair (xrp/btc) or eth, etc..
        #     if len(sym) <= 4:
        #         # ...probably a no pair (eg. "XRP")
        #         sym_name = sym
        #         # already set to BTC pair by default
        #     elif sym.endswith('btc' or 'eth'):
        #         # ...then we know it's "xxBTC" or "xxETH" at least
        #         sym_pair = sym[-3:]  # last 3 chars
        #         sym_name = sym[:-3]
        #     #
        #     propersym = sym_name + sym_pair
        # elif sym is "btc" or sym is "eth":


        # symbol input box (top-left)
        symbolinput = WebDriverWait(self.driver, 10, 0.05).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'input-3lfOzLDc-')))
        print("symbolinput:")
        print(symbolinput)

        symbolinput.click()
        # WebDriverWait(self.driver, 10, 0.05).until(
        #     EC.presence_of_element_located((By.CLASS_NAME, 'isExpanded-1pdStI5Z-')))
        symbolinput.send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

        ### EXCHANGE ###

        # THIS IS ALSO WHERE THE PROBLEM IS ###########################################################

        # if exchange is specified, loop through to find the correct line
        if len(parsedinput) > 1:    # exchange
            exchange = parsedinput[1]
            symbolinput.send_keys(exchange, ':')

        # finally, enter symbol
        symbolinput.send_keys(propersym)
        symbolinput.send_keys(Keys.RETURN)



        # ### SELECTING THE RIGHT SYMBOL ###
        #
        # # entire drop-down table of matching symbols
        # symboleditpopup = WebDriverWait(self.driver, 10, 0.05).until(
        #     EC.visibility_of_element_located((By.CLASS_NAME, 'symbol-edit-popup'))
        # )
        # print(symboleditpopup)
        # symboleditpopup.screenshot('symboleditpopup.png')
        #
        # # the symboleditpopup menu is up, but may be still loading
        # # these lines might not be visible yet
        #
        # table_of_results = symboleditpopup.find_elements_by_css_selector('tr.symbol-edit-popup')
        # target = table_of_results[0]
        #
        # # if exchange is specified, loop through to find the correct line
        # if len(parsedinput) > 1:    # exchange
        #     exchange = parsedinput[1]
        #     for line in table_of_results:
        #         name_and_exchange = line.get_attribute('data-item-ticker')
        #         print(name_and_exchange)    #
        #         if "lol" is exchange:
        #             # target = line
        #             break
        #
        # target.click()

        # locate the main chart element, for screenshot & Key-sending use
        # chart_itself = self.driver.find_element_by_class_name("chart-container")

        ### CHANGING TIME INTERVAL ###
        if len(parsedinput) > 2:  # time interval
            interval = parsedinput[2]
            ActionChains(self.driver).send_keys(',', interval).perform()
        else:
            ActionChains(self.driver).send_keys(',', '4h').perform()
        ActionChains(self.driver).send_keys(Keys.RETURN).perform()

        ### SCREENSHOT ###
        screenshot_binary = self.driver.get_screenshot_as_png()
        # self.driver.close()
        return screenshot_binary



if testing is True:
    tv = TradingViewScraper()
    tv.testing = True
    tv.start()
    bindata = tv.get_chart_screenshot_binary("ltcusd bitfinex 1d")

    churt = tv.driver.find_element_by_class_name("chart-container")
    churt.screenshot('screen_shot_chart.png')
    print("Screenshot of chart saved")