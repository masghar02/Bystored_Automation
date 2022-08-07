from selenium import  webdriver
from selenium.webdriver.common.by import By
from  selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path=
                          'C:/Users/HP/AppData/Local/Programs/Python/Python310/chromedriver.exe')

driver.get("https://google.com")