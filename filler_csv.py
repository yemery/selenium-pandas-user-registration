import time
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import pandas as pd
from selenium.webdriver.common.by import By
import random
from datetime import datetime, timedelta

with open('users_db.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  
    for row in reader:
        print(row)
        full_name = row[0]
        email = row[1]
        password = row[0]
        user_role = "3"
        direction = row[3]
        position = row[4]
        date_affectation = (datetime.now() + timedelta(days=random.randint(0, 3650))).strftime('%m/%d/%Y')

        Path="C:\Program Files (x86)\chromedriver.exe"
        driver=webdriver.Chrome(Path)

        driver.get('http://127.0.0.1:8000/register')

        name = driver.find_element(By.NAME, 'name')
        name.send_keys(full_name)

        email_field = driver.find_element(By.NAME, 'email') 
        email_field.send_keys(email)

        password_field = driver.find_element(By.NAME, 'password')  
        password_field.send_keys(password)

        confirmed_password_field = driver.find_element(By.NAME, 'password_confirmation')  
        confirmed_password_field.send_keys(password)

        role = Select(driver.find_element(By.NAME, 'user_role') )
        role.select_by_value(user_role)

        direction_select = Select(driver.find_element(By.NAME, 'direction') )
        direction_select.select_by_value(direction)

        position_select = Select(driver.find_element(By.NAME, 'position'))
        position_select.select_by_value(position)

        date_field = driver.find_element(By.NAME, 'date_affectation')  
        date_field.send_keys(date_affectation)

        submit_button = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/form/div[9]/button')
        submit_button.click()

        # time.sleep(60)

        with open('log.txt', 'a') as f:
            f.write(f"User '{full_name}' with email '{email}' was successfully registered.\n")

        logout_button = driver.find_element(By.XPATH,'/html/body/div[2]/nav/div[1]/div/div[2]/div/div/div[1]/span/button')
        logout_button.click()

        driver.close()
        driver.get('http://127.0.0.1:8000/register')




driver.quit()
