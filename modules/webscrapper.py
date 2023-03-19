from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import os

firefox_options = Options()
firefox_options.add_argument("--width=200, 250")
firefox_options.add_argument("--height=250")
firefox_options.headless = True
# firefox_options.add_experimental_option("detach", True)


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)

html_path = os.path.abspath('dot/dot.html')

driver.get(f'file://{html_path}')

driver.execute_script("window.scrollTo(500, 500)") 

def Get():
	try:
		element = WebDriverWait(driver, 5).until(
			EC.presence_of_element_located((By.XPATH, "/html")))
		driver.save_screenshot('dot/dot.png')
		opened_image = Image.open('dot/dot.png')
		cropped_image = opened_image.crop(box=(20, 20, 100, 100))
		cropped_image.save('dot/dot.png', 'png')
	except:
		print("Couldn't save PNG")

def Refresh():
	driver.refresh()
	driver.execute_script("window.scrollTo(500, 500)")	

def Shutdown():
	driver.close()
	print('brower exited')

