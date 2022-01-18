from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://chromedino.com/")

canvas = driver.find_element_by_xpath("/html/body/header/div[2]/canvas")
canvas.send_keys(Keys.ARROW_UP)
