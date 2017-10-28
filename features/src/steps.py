"""
Lettuce reads quoted input from features instructions to use with
correlating Python methods. These Python methods should be setup here in this file.

Python methods pull input from the Gherkin story by using the @step decorator

"""
# -*- coding: utf-8 -*-

import time
import urlparse

from terrain import contains_content
from config import TWITTER_HOST, USERS, PATH

from lettuce import step
from lettuce import world
from lettuce_webdriver.util import assert_true
from lettuce_webdriver.util import assert_false
from lettuce_webdriver.util import AssertContextManager

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@step('I am logged in as "(.*?)"$')
def I_am_logged_in_as(step, user_id):
    with AssertContextManager(step):
        world.browser.get(urlparse.urljoin(TWITTER_HOST, 'login'))
        time.sleep(3)
        if  world.browser.current_url == TWITTER_HOST:
            pass
        else:
            user = USERS[user_id]
            world.browser.find_element_by_class_name("js-username-field").send_keys(user['username'])
            world.browser.find_element_by_class_name("js-password-field").send_keys(user['password'])
            wait = WebDriverWait(world.browser, 5)
            world.browser.find_element_by_css_selector("button.submit").click()


@step('I write the tweet "(.*?)"$')
def I_write_twitter_post(step, tweet):
    with AssertContextManager(step):
        WebDriverWait(world.browser, 10).until(
            EC.presence_of_element_located((By.ID, "tweet-box-home-timeline")))
        element = world.browser.find_element_by_id("tweet-box-home-timeline")
        element.clear()
        element.send_keys(tweet)


@step('I should see the message "([^"]+)"$')
def should_see(step, text):
    world.browser.implicitly_wait(10)
    assert_true(step, contains_content(world.browser, text.encode('utf-8')))

@step('I should not be able to submit the tweet$')
def dont_tweet(step):
    element = world.browser.find_element_by_class_name('js-tweet-btn')
    assert_false(step, element.is_enabled())

@step('I press "(.*?)" button$')
def press_button(step, button_id):
    button = world.browser.find_element_by_class_name('js-tweet-btn')
    assert_true(step, button.is_enabled())
    button.click()

@step('I should see my tweet$')
def see_tweet(step):
    assert_true(step, WebDriverWait(world.browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "my-tweet")))
    )