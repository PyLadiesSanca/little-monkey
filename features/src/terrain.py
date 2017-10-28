"""
We need to ensure that our tests are pointed to CBT!
Lettuce uses python to instantiate a RemoteWebDriver,
we just need to make sure its pointed at our hub and uses our API names
to pick out a OS/Browser configuration.

flag --no-sandbox para testes especiais como no Jenkins, ou dentro do Docker
Configs para rodar com o docker, basta descomentar tudo a seguir:
chrome_options.add_argument("--no-sandbox")
"""

import time
from config import BROWSER, PATH, CHROMEDRIVER

from lettuce import before, after, world

from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException


@before.all
def setup_browser():
    """" Setup browsers """

    if BROWSER == 'chrome':
        print("BROWSER:" + '\x1b[7;30;43m' + "CHROME" + '\x1b[0m')
        chrome_options = webdriver.ChromeOptions()
        world.browser = webdriver.Chrome(executable_path=CHROMEDRIVER,
                                         chrome_options=chrome_options)
        world.browser.set_window_size(1280,800)
    elif BROWSER == 'chrome_headless':
        print("BROWSER:" + '\x1b[7;30;43m' + "CHROME HEADLESS" + '\x1b[0m')
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        chrome_options.add_argument('window-size=1280,800')
        world.browser = webdriver.Chrome(executable_path=CHROMEDRIVER,
                                         chrome_options=chrome_options)
    else:
        print("Invalid browser!!!")
                                        

@after.all
def tear_down_feature(self):
    """" Function to close the browser """
    world.browser.quit()


def contains_content(browser, content):
    """
    Search for an element that contains the whole of the text we're looking
    for in it or its subelements, but whose children do NOT contain that
    text - otherwise matches <body> or <html> or other similarly useless things.
    """

    for elem in browser.find_elements_by_xpath(unicode(
            u'//*[contains(normalize-space(.),"{content}") '
            u'and not(./*[contains(normalize-space(.),"{content}")])]'
            .format(content=content))):
        try:
            if elem.is_displayed():
                return True
        except StaleElementReferenceException:
            pass

    return False