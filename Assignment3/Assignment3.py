# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the bestbuy homepage
driver.get("https://www.bestbuy.ca/en-ca")
time.sleep(3)

# Maximizing window
driver.maximize_window()

#Clicking the shop drop down
link = driver.find_element("xpath","/html/body/div[1]/div/div[3]/header/div/div/div[2]/div/div/div[1]/div/div[2]/div/ul[1]/li[1]/button/span")
link.click()
time.sleep(3)


#Clicking on cameras
Secondlink = driver.find_element("xpath","/html/body/div[1]/div/div[3]/header/div/div/div[2]/div/div/div[1]/div/div[2]/div/ul[1]/li[1]/div[2]/div/a[9]")
Secondlink.click()
time.sleep(3)

#Click on subdivision in camera
Thirdlink = driver.find_element("xpath","/html/body/div[1]/div/div[3]/header/div/div/div[2]/div/div/div[1]/div/div[2]/div/ul[1]/li[1]/div[2]/div/div[9]/div/a[4]")
Thirdlink.click()
time.sleep(5)

#Give input in search bar
search_bar = driver.find_element("name","search")
search_bar.send_keys("Polaroid Go Instant Camera - White")
time.sleep(5)

# Submitting the search query
search_bar.send_keys(Keys.RETURN)

# Waiting for the search results page to load
time.sleep(5)

#Selecting the needed image
image_src = "/en-ca/product/polaroid-go-instant-camera-everything-box-white/15480905"
image_element = driver.find_element(By.XPATH, "//a[@href='" + image_src + "']")
image_element.click()
time.sleep(5)

#Scrolling down the webpage
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)

#Selecting pick up instead of delivery
pick_up = driver.find_element("xpath","/html/body/div[1]/div/div[4]/section[4]/div[3]/div[1]/div[1]/button[2]/h2")
pick_up.click()
time.sleep(5)

#Selecting pick up at the store
Fourthlink = driver.find_element("xpath","/html/body/div[1]/div/div[4]/section[4]/div[3]/div[1]/div[2]/div/div[2]/div[2]/button/span")
Fourthlink.click()
time.sleep(10)
#Printing the title to show the last step is being executed
print(driver.title)


# Closing the webdriver
driver.close()
