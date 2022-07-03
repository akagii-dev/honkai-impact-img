import cv2
import requests
import tempfile
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import datetime

options = Options()
options.add_argument("--headzsless")
url = "https://honkaiimpact3.hoyoverse.com/global/en-us/media/wallpaper"
options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(),  chrome_options=options)
driver.set_window_size('1200', '1000')
driver.get(url)

def get_image_url():
    el = driver.find_elements(By.CLASS_NAME, "img-container")
    for i in el:
        imgurl = i.find_element(By.TAG_NAME, "img").get_attribute("src").split("?")[-2]
        imgre = requests.get(imgurl)
        fp = tempfile.NamedTemporaryFile(dir='./img', delete=False)
        fp.write(imgre.content)
        img = cv2.imread(fp.name)
        fp.close()
        fpname = "./img/" + datetime.datetime.now().strftime("%H-%M-%S") + ".png"
        cv2.imwrite(fpname, img)
        os.remove(fp.name)

for j in range(29):
    get_image_url()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "next-btn").find_element(By.TAG_NAME, "a").click()
    time.sleep(3)
driver.close()
print("task was done!")