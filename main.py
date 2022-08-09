from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent
import time, os, datetime, urllib.request

options = Options()
url = "https://honkaiimpact3.hoyoverse.com/global/en-us/media/wallpaper"
options.add_argument('--headless')
ua = UserAgent(verify_ssl=False)
userAgent = ua.random
options.add_argument(f'user-agent={userAgent}')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.set_window_size('1200', '1000')
driver.get(url)

def getImg():
    el = driver.find_elements(By.CLASS_NAME, "img-container")
    for j in el:
        imgurl = j.find_element(By.TAG_NAME, "img").get_attribute("src").split("?")[-2]
        savetime = time.strftime("%d%H%M%S", time.localtime())
        urllib.request.urlretrieve(imgurl, "./img/"+savetime+".jpg")
        time.sleep(0.5)

count = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/div[2]/div[3]/div[2]/ul/li[15]/a").text    
count = int(count)
for i in range(count):
    getImg()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "next-btn").find_element(By.TAG_NAME, "a").click()
    time.sleep(3)
driver.close()
print("task was done!")
