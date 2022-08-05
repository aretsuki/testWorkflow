import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

username = "alexkoval"
email = "a.koval508@gmail.com"
password = "login123"
url = "https://juno.one"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# launch URL and go to https://juno.one
driver.get(url)
# maximize the Chrome window
driver.maximize_window()

# on the website click on the "sign in" button
driver.find_element(By.CSS_SELECTOR, ".pointer[data-v-3cdce82b]").click()
driver.implicitly_wait(3)

# enter the username and click "log-in"
driver.find_element(By.CSS_SELECTOR, ".form_input[data-v-1214690c]").send_keys(username)
driver.find_element(By.CSS_SELECTOR, ".login-button[data-v-1214690c]").click()

# enter the e-mail and password and click "log-in"
driver.find_element(By.NAME, "email").send_keys(email)
driver.find_element(By.NAME, "password").send_keys(password)
driver.find_element(By.CSS_SELECTOR, ".login-container .el-button").click()

# press the "add items" button
driver.find_element(By.ID, "add-items-btn").click()
driver.implicitly_wait(1)

# select "Projects"
projects = driver.find_element(By.LINK_TEXT, "Projects")
projects.click()
# select a project name, in this case "TestProject"
addProject = driver.find_element(By.ID, "input-183")
addProject.clear()
addProject.send_keys("TestProject")
addProject.send_keys(Keys.RETURN)

# click on the Add Labels button
addLabels = driver.find_element(By.XPATH, "//*[contains(text(), '+ Add labels')]")
addLabels.click()
# click on the Create Project Label button
createLabel = driver.find_element(By.XPATH, "//*[contains(text(), 'Create project label')]")
createLabel.click()
driver.implicitly_wait(5)
# select a name for the new label, in this case "TestLabel" | BUG FOUND - even after deleting an existing label, it still exists
nameLabel = driver.find_element(By.ID, "input-252")
nameLabel.click()
nameLabel.send_keys("TestLabel")
driver.implicitly_wait(1)

# select a color for the label by inserting RGB values between 0 and 255
red = driver.find_element(By.XPATH, "//*[@id='list-item-531']/div/div/div/div[1]/div[2]/div[1]/input")
red.clear()
red.send_keys("150")
green = driver.find_element(By.XPATH, "//*[@id='list-item-531']/div/div/div/div[1]/div[2]/div[2]/input")
green.clear()
green.send_keys("150")
blue = driver.find_element(By.XPATH, "//*[@id='list-item-531']/div/div/div/div[1]/div[2]/div[3]/input")
blue.clear()
blue.send_keys("150")

# or select a color by inserting HSL values
# click on the button with two arrows to change format
changeColorFormat = driver.find_element(By.XPATH, "//*[@id='list-item-531']/div/div/div/div[1]/div[2]/button/span/i")
changeColorFormat.click()
# insert a value for Hue between 0 and 360
hue = driver.find_element(By.XPATH, "//*[@id='list-item-531']/div/div/div/div[1]/div[2]/div[1]/input")
hue.clear()
hue.send_keys("250")
# insert a value for Saturation between 0 and 1
saturation = driver.find_element(By.XPATH, "//*[@id='list-item-531']/div/div/div/div[1]/div[2]/div[2]/input")
saturation.clear()
saturation.send_keys("0.5")
# insert a value for Lightness between 0 and 1
lightness = driver.find_element(By.XPATH, "//*[@id='list-item-531']/div/div/div/div[1]/div[2]/div[3]/input")
lightness.clear()
lightness.send_keys("0.5")

# select the Alpha value between 0 and 1 (for RGB and HSL formats)
Alpha = driver.find_element(By.XPATH, "//*[@id='list-item-531']/div/div/div/div[1]/div[2]/div[4]/input")
Alpha.clear()
Alpha.send_keys("1")



# or select an already existing color
driver.find_element(By.XPATH, "//*[@id='list-item-531']/div/div/div/div[2]/div/div[3]/div[1]/div")
# click Create
driver.find_element(By.XPATH, "//*[@id='list-item-267']/div/div[1]/button/span").click()
# click the exit button
driver.find_element(By.XPATH, "//*[@id='list-item-256']/div/div[2]/button/span/i").click()


addDescription = driver.find_element(By.ID, "input-245")
addDescription.clear()
addDescription.send_keys("...")
time.sleep(2)

driver.find_element(By.XPATH, "//*[contains(text(), 'Create')]").click()

driver.implicitly_wait(10)


time.sleep(500)