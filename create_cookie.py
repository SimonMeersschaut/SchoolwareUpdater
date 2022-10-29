from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import time

def search_element(driver, xpath=""):
  element = None
  while not element:
    try:
      element = driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
      pass
  return element

def create_cookie():
  chrome_options = Options()
  chrome_options.add_argument("--headless")
  chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
  chrome_options.add_argument("--disable-logging")
  driver = webdriver.Chrome(options=chrome_options)
  driver.get("https://login.microsoftonline.com/leerling.hhscholen.be/oauth2/authorize?resource=https%3A%2F%2Fgraph.microsoft.com%2F&redirect_uri=https%3A%2F%2Fschoolware.hhscholen.be%2Fwebleerling%2Fbin%2Fserver.fcgi%2Foauth2%2Fcallback%2Foffice365&client_id=64031947-a8be-4784-ae7f-abc2c25ff9cc&response_type=code&state=c2Vzc2lvbj05RjM5MDNEMC1DRUFFLTQwRjMtOEE4Ri1EMzEzNkYyRjU2MDc%3D&sso_reload=true")

  # search_element(driver, "/html/body/div[2]/div/div/div/div/div/div/div[1]/div/div/div[3]/div/div/div[1]/em/button").click()
  search_element(driver, "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[2]/div[2]/div/input[1]").send_keys("simon.meersschaut@leerling.hhscholen.be")
  search_element(driver, "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[4]/div/div/div/div[2]/input").click()
  search_element(driver, "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div/div[2]/input").send_keys('MK*nr*94\n')
  search_element(driver, "/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[1]/input").click()
  # search_element(driver, "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[4]/div[2]/div/div/div/div/input").click()

  time.sleep(2)
  cookie = driver.get_cookie('FPWebSession')['value']
  
  # input(cookie)
  driver.quit()
  return cookie

if __name__ == '__main__':
  print(create_cookie())