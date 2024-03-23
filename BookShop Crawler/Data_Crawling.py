from selenium import webdriver

from selenium.webdriver.common.by import By

import schedule

import time

Options = webdriver.ChromeOptions()

Options.add_argument("start-maximized")

def job():

    driver = webdriver.Chrome(chrome_options=Options, executable_path=r"E:\Chrome Driver\chromedriver.exe")

    URL = "https://bookshop.org/lists/new-books"

    driver.get(URL)

    Books = driver.find_elements(By.CSS_SELECTOR,".py-8")

    Title = driver.find_elements(By.CSS_SELECTOR,".text-xl a")

    Author = driver.find_elements(By.CSS_SELECTOR,".text-sm")

    Price = driver.find_elements(By.CSS_SELECTOR,".font-sans-bold")

    for i in range(len(Books)):
        
        print("Title: " + Title[i].text + "\nAuthor: " + Author[i].text + "\nPrice: " + Price[i].text + "\n-----------------------------------------")
    
    driver.close()

# job()

schedule.every(30).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(30)

