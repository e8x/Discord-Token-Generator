import os
import string
import random
import uuid
import selenium
import requests
import urllib.request
import urllib.request, urllib.parse, urllib.error 
import time
from time import sleep, time
from random import uniform, randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from python_anticaptcha import AnticaptchaClient, NoCaptchaTaskProxylessTask
from selenium.webdriver import Firefox








rand = str(uuid.uuid4())
link = 'fyii.de/trashmail/' 
email_address = '@fyii.de'
email_link = link+rand+'.html'
email = rand+email_address
xx = input('How Many Tokens To generate:')
username = input("type the username of account:")
print('Generating ...')
print(email+'\n')



driver = Firefox()
driver.get("https://discordapp.com/register")

element = driver.find_element_by_name("email")
element.send_keys(email)

element = driver.find_element_by_name("username")
element.send_keys(username)

element = driver.find_element_by_name("password")
element.send_keys(rand)




element.send_keys(Keys.RETURN)

url = 'https://discordapp.com/register'
driver.execute_script('document.getElementById("g-recaptcha-response").innerHTML = "%s"' % response)
driver.find_element_by_xpath('//button[@type="submit" and @class="btn-std"]').click()

