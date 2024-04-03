from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import time
import requests
import os

chrome_options = Options()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("--disable-images")
chrome_options.add_argument("--user-data-dir=C:\\Users\\Jaber\\AppData\\Local\\Google\\Chrome\\User Data")

driver = webdriver.Chrome(options=chrome_options)


level2 = []

def save_page_to_file(filename):
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(driver.page_source)
    print("Saved to file: ", filename)
    
def get_level_2(link):
    for i in range(1, 100):
        done = False 
        Done = False
        while done == False:
            try:
                print("Level 3: ", link, " ", i)
                driver.get(link + "?limit=50&page=" + str(i))
                time.sleep(2)
                menus = WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((By.TAG_NAME, "i")))
                ok = 0
                for m in menus:
                    if m.get_attribute("class") == "icon icon-listing01":
                        ok = 1
                if ok == 0:
                    if driver.page_source.find("takiej strony") != -1 and driver.page_source.find("wyszukiwarki lub menu, aby znal") != -1:
                      Done = True
                      break
                    else:
                      raise ValueError("x should be a positive integer")
                else:
                    name = link.replace("https://www.mediaexpert.pl/", "").replace("/", "_") + "-" + str(i) + ".html"
                    save_page_to_file(name)
                    done = True
            except:
                input("Error, press enter to continue ..." + str(i))    
                
            if Done:
                break
        if Done:
            break

    
def save_to_file(filename, data):
    with open(filename, 'w') as f:
        for item in data:
            f.write("%s\n" % item)
    print("Saved to file: ", filename)
    
def append_to_file(filename, data):
    with open(filename, 'a') as f:
        for item in data:
            f.write("%s\n" % item)
    print("Appended to file: ", filename)
    
def load_from_file(filename):
    with open(filename, 'r') as f:
        return f.readlines()

level2 = load_from_file("links.txt")

for i in range(0, len(level2)):
    l = level2[i].strip()
    print("Level 2: ", l, " ", i + 1, "/", len(level2))
    get_level_2(l)
    done = True

