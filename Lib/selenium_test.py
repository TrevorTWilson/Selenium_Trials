import datetime
from datetime import date, timedelta
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionBuilder
from Xpath_locations import *
import time

s = Service("C:\Program Files (x86)\chromedriver.exe")
browser = webdriver.Chrome(service=s)

# Set website address
url = "https://accounts.goformz.com/login?ReturnUrl=https%3A%2F%2Faccounts.goformz.com%2Fconnect%2Fauthorize" \
      "%2Fcallback%3Fclient_id%3Dfec39629-2cf9-4ed7-a1b5-aa44833c50dd%26redirect_uri%3Dhttps%253A%252F%252Fapp" \
      ".goformz.com%26response_type%3Dcode%26scope%3Dopenid%2520profile%2520basic%26state" \
      "%3Db9ee0637543e4089821e1f8404b8e76f%26code_challenge%3DM3NIBtRZrOovNa82tOX3sWwyCtq9dIp_BdcP5UF25Uw" \
      "%26code_challenge_method%3DS256%26response_mode%3Dquery "
url2 = "https://app.goformz.com/forms?page=1&pageSize=25&sortDir=desc&sortBy=lastUpdatedDate"

# Load Initial view of Website and give time to load
browser.get(url)

# set wait time
wait = 25

# Function to log in to GoFormz
def login():
    for _ in range(2):
        try:
            element = WebDriverWait(browser, wait).until(
                EC.presence_of_element_located((By.ID, "username"))
            )
        finally:
            #  Enter Username and Password and click Login First time
            user_name = browser.find_element(By.ID, "username")
            user_name.send_keys('dragonfire.inspection@gmail.com')
            pass_word = browser.find_element(By.ID, "password")
            pass_word.send_keys('TrevorWilson1972!')
            click_login = browser.find_element(By.ID, "login")
            click_login.click()


# function to make selection on website
def next_selection(website_element, answer='', txt_entry=''):
    # Wait for website
    try:
        element = WebDriverWait(browser, wait).until(
            EC.presence_of_element_located((By.XPATH, website_element))
        )
    finally:
        # center element
        browser.execute_script(
            "arguments[0].scrollIntoView({'block':'center','inline':'center'})", browser.find_element
            (By.XPATH, website_element))

        # make selection
        time.sleep(2)
        new_selection = browser.find_element(By.XPATH, website_element)
        new_selection.click()
        if txt_entry != '':
            new_selection.send_keys(txt_entry)
        if answer != '':
            try:
                element = WebDriverWait(browser, wait).until(
                    EC.presence_of_element_located((By.XPATH, answer))
                )
            finally:
                # make selection
                time.sleep(2)
                new_selection = browser.find_element(By.XPATH, answer)
                new_selection.click()


# function to open new report on GoFormz
def new_report(steps, report_date = date.today()):
    for item in steps:
        next_selection(item)
    set_report_date(report_date)


# Function to insert date
def set_report_date(report_date):
    # set report date
    report_date -= timedelta(days=1)
    month = report_date.strftime('%B')
    year = str(report_date.year)
    day = str(report_date.day)

    # open datepicker
    next_selection(date_button)
    time.sleep(1)

    # select month
    new_selection = Select(browser.find_element(By.XPATH, month_attribute))
    new_selection.select_by_visible_text(month)
    #time.sleep(1)

    # select year
    new_selection = Select(browser.find_element(By.XPATH, year_attribute))
    new_selection.select_by_visible_text(year)
    #time.sleep(1)

    #select day
    next_selection(f'//*[text()="{day}"]')

    next_selection(date_done_button)


def add_signature():
    # initialize action chain
    next_selection(signature_field)
    action = ActionChains(browser)
    action.move_to_element(browser.find_element(By.XPATH, signature_field_sign))
    action.move_by_offset(-200, 0)
    action.click_and_hold()
    action.move_by_offset(100, -60).move_by_offset(-50, 120).move_by_offset(0, -60)
    action.release()
    action.move_by_offset(0, 0).move_by_offset(0, 0)
    action.click_and_hold()
    action.move_by_offset(200, 0).move_by_offset(200, 0)
    action.release()
    action.perform()
    return








# function to complete report
def write_report(list_of_items):
    for item in list_of_items:
        next_selection(*item)


# Log in to Go Formz
login()

# Generate blank report
new_report(generate_report)

# Complete writing Report
write_report(full_report)

# enter signature
#time.sleep(8)
add_signature()

# pause for inspection
input('Enter when done')
