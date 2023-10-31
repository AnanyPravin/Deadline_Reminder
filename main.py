from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import smtplib
import time as tm
import schedule
from email.message import EmailMessage


def log():
    username = 'apravin2@illinois.edu'
    password = 'warriorX_9901TiNy201119'
    chrome_options = Options()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get("https://smart.physics.illinois.edu/Course/Calendar?enrollmentID=126787")
    driver.maximize_window()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".input.text-box"))).send_keys(username)
    driver.find_element(By.CSS_SELECTOR,'input[type=\'submit\']').click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "passwd"))).send_keys(password)
    driver.find_element(By.CSS_SELECTOR,'input[type=\'submit\']').click()
    innerHTML = driver.page_source
    tm.sleep(20)
    driver.quit
    soup = BeautifulSoup(innerHTML, 'html.parser')
    duedate = soup.find_all('span', class_ = 'ehfi-duedate')
    list1 = []
    for date in duedate:
        list1.append(date.text)
    list2set = sorted(set(list1), key=list1.index)
    return list2set


def send_email():
    pw = 'mqvg dtoa scqy etgh'
    user = 'ananypravin2004@gmail.com'
    receiver = 'ananypravin2004n@gmail.com'
    final_set = log()
    email_sender = user
    email_password = pw
    email_receiver = receiver
    subject = 'Deadlines for this week!'
    temp_list = list(final_set)
    while temp_list:
        msg = temp_list[0:2]
        body = str(msg)
        del temp_list[0:2]
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['subject'] = subject
        em.set_content(body)
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
            smtp.quit()
            smtp.close()
        tm.sleep(604800)
    
schedule.every(7).days.do(send_email)