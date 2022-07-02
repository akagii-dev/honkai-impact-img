import cv2
import requests
import tempfile
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import datetime

options = Options()
path = "./chromedriver.exe"
url = "https://honkaiimpact3.hoyoverse.com/global/en-us/media/wallpaper"
options.add_argument('--headless')
driver = webdriver.Chrome(path, chrome_options=options)
driver.set_window_size('1200', '1000')
driver.get(url)

def get_image_url():
    el = driver.find_elements_by_class_name("img-container")
    for i in el:
        imgurl = i.find_element_by_tag_name("img").get_attribute("src").split("?")[-2]
        imgre = requests.get(imgurl)
        fp = tempfile.NamedTemporaryFile(dir='./img', delete=False)
        fp.write(imgre.content)
        img = cv2.imread(fp.name)
        fp.close()
        fpname = "./img/" + datetime.datetime.now().strftime("%H-%M-%S") + ".png"
        cv2.imwrite(fpname, img)
        os.remove(fp.name)

for j in range(28):
    get_image_url()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    driver.find_element_by_class_name("next-btn").find_element_by_tag_name("a").click()
    time.sleep(1)
driver.close()
print("task was done!")