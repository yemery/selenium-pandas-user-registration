import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import pandas as pd
from selenium.webdriver.common.by import By
import random
from datetime import datetime, timedelta
df = pd.read_excel('users_updt.xlsx')

Path="C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(Path)


driver.get('http://127.0.0.1:8000/register')


for index, row in df.iterrows():
    driver.get('http://127.0.0.1:8000/register')

    name = driver.find_element(By.NAME, 'name')
    name.send_keys(row['full_name'])

    email =driver.find_element(By.NAME, 'email') 
    email.send_keys(row['email'])

    password =driver.find_element(By.NAME, 'password')  
    password.send_keys(row['full_name'])

    confirmed_password =driver.find_element(By.NAME, 'password_confirmation')  
    confirmed_password.send_keys(row['full_name'])

    role = Select(driver.find_element(By.NAME, 'user_role') )
    role.select_by_value("1")

   

    direction = Select(driver.find_element(By.NAME, 'direction') )
 
    direction.select_by_value("1")

    position = Select(driver.find_element(By.NAME, 'position'))
    position.select_by_value("1")

 
    date =driver.find_element(By.NAME, 'date_affectation')  
    date.send_keys((datetime.now() + timedelta(days=random.randint(0, 3650))).strftime('%m/%d/%Y'))

    # Submit the form
    submit = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/form/div[9]/button')
    submit.click()

    with open('log.txt', 'a') as f:
        f.write(f"User '{row['full_name']}' with email  was successfully registered.\n")

    logout = driver.find_element(By.XPATH,'/html/body/div[2]/nav/div[1]/div/div[2]/div/div/div[2]/div/form/a')
    logout.click()
    driver.get('http://127.0.0.1:8000/register')

driver.quit()
