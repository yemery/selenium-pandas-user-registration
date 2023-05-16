import csv
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
import random

Path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(Path)

existing_names = set()

with open('log.txt', 'r') as log_file:
    lines = log_file.readlines()

    last_registered_user = None
    for line in reversed(lines):
        if line.startswith("User '"):
            start_index = line.index("'") + 1
            end_index = line.index("'", start_index)
            last_registered_user = line[start_index:end_index]
            break

    for line in lines:
        if line.startswith("User '"):
            start_index = line.index("'") + 1
            end_index = line.index("'", start_index)
            name = line[start_index:end_index]
            existing_names.add(name)

driver.get('http://127.0.0.1:8000/register')

with open('users_csv_filling.csv', 'r') as f:
    reader = csv.reader(f)
    lines = list(reader)
    header = lines[0]
    data = lines[1:]
    line_counter = 0
    found_last_registered_user = False

    if last_registered_user:
        last_registered_line = None
        for i, row in enumerate(data):
            if row[0] == last_registered_user:
                last_registered_line = i
                break

        if last_registered_line is not None:
            data = data[last_registered_line + 1:]
            print(f"Resuming registration from line {last_registered_line + 2}")

    for row in data:
        full_name = row[0]
        if found_last_registered_user:
            # Start from the next line after the last registered user
            if full_name == last_registered_user:
                found_last_registered_user = False
            continue

        if full_name in existing_names:
            print(f"User '{full_name}' already exists in the logs. Skipping.")
            continue
        
        email = row[1]
        password = row[0]
        user_role = "3"
        direction = row[2]
        position = row[3]
        entity = row[4]
        date_affectation = (datetime.now()).strftime('%m/%d/%Y')

        print(full_name, email, password, position, direction, entity, date_affectation)
        # Rest of the registration code...
        name = driver.find_element(By.NAME, 'name')
        name.send_keys(full_name)

        email_field = driver.find_element(By.NAME, 'email')
        email_field.send_keys(email)

        password_field = driver.find_element(By.NAME, 'password')
        password_field.send_keys(password)

        confirmed_password_field = driver.find_element(By.NAME, 'password_confirmation')
        confirmed_password_field.send_keys(password)

        role = Select(driver.find_element(By.NAME, 'user_role'))
        role.select_by_value(user_role)

        direction_select = Select(driver.find_element(By.NAME, 'direction'))
        direction_select.select_by_value(direction)

        position_select = Select(driver.find_element(By.NAME, 'position'))
        position_select.select_by_value(position)

        entity_select = Select(driver.find_element(By.NAME, 'entity'))
        entity_select.select_by_value(entity)

        date_field = driver.find_element(By.NAME, 'date_affectation')
        date_field.send_keys(date_affectation)

        submit_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/form/div[10]/button')
        submit_button.click()
        time.sleep(2)

       
        line_counter += 1
        if line_counter % 10 == 0:
            print("Waiting for 1 minute...")
            time.sleep(60)

        dropdown = driver.find_element(By.XPATH, '/html/body/div[2]/nav/div[1]/div/div[2]/div/div/div[1]/span/button')
        dropdown.click()
        time.sleep(2)
        logout_button = driver.find_element(By.XPATH, '/html/body/div[2]/nav/div[1]/div/div[2]/div/div/div[2]/div/form/a')
        logout_button.click()
        time.sleep(2)
        # driver.close()
        with open('log.txt', 'a') as log_file:
            log_file.write(f"User '{full_name}' with email '{email}' was successfully registered.\n")

        driver.get('http://127.0.0.1:8000/register')


driver.quit()
