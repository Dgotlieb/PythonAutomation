from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


def double_click(driver):
    action = ActionChains(driver)
    my_button = driver.find_element(By.ID, value="myButton")
    action.double_click(my_button)
    action.perform()


def move_to_element(driver):
    action = ActionChains(driver)
    my_button = driver.find_element(By.ID, value="myButton")
    action.move_to_element(my_button)
    action.perform()


def select_multiple(driver):
    action = ActionChains(driver)
    my_button1 = driver.find_element(By.ID, value="myButton")
    my_button2 = driver.find_element(By.ID, value="myButton")
    my_button3 = driver.find_element(By.ID, value="myButton")
    action.click_and_hold(on_element=my_button1).click_and_hold(on_element=my_button2).click_and_hold(my_button3)
    action.perform()


driver = webdriver.Chrome()
driver.get('https://dgotlieb.github.io/RelativeLocator/index.html')
double_click(driver)
move_to_element(driver)
select_multiple(driver)
driver.quit()
