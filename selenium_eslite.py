from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait #網站等待 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options #瀏覽器設定
from selenium.webdriver.common.keys import Keys #直接按 Enter
from time import sleep

option = webdriver.ChromeOptions()#讀取預設設定
prefs = {"profile.default_content_setting_values":{"notifications":2}}#創建設定
option.add_experimental_option("prefs",prefs)#合併設定
#開啟瀏覽器(位置,設定)
driver = webdriver.Chrome("D:\\yuhsiuching\\Download\\chromedriver.exe",options = option) 

#--------------------------------設定-------------------------------------------------#

#開啟網址
driver.get("https://www.eslite.com/best-sellers/online/3?type=2") 
                    #設置讀取網站的時間,直到(判斷可被點擊((選取目標)) #selector:tag[attr_name = attr_value]        
#keyword = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"textarea[type=search]")))
#keyword.send_keys("german shepherd") 

#webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
login = WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div[class=close-btn]")))
login.click()

book_elements = driver.find_elements(By.CLASS_NAME,"product-list-wrapper")

for book_element in book_elements:
    book_element.click()
    #booka_elements = driver.find_elements(By.CLASS_NAME,"product-item border-bottom d-flex search-list-display")
    
'''    for booka_element in booka_elements:
        booka_element.click()
        href = []        
    for booka_element in booka_elements:
        booka_element.click()
        href.append(book_element.get_attribute("href"))
        sleep(0.1)
'''

        
#print(href)

#book = WebDriverWait(driver,6).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div[class=product-list-wrapper]")))
#book.click()
#&page=1&per_page=100
#/html/body/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[1]