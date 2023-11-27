from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=Service(r"tests/chromedriver.exe"), options=options)

def test_scores_service(driver):
    driver.get("http://127.0.0.1:5000/")
    score_element = int(driver.find_element(By.ID, "score").text)
    if 1000 >= score_element >= 1:
        return True, score_element
    else:
        return False


def main_function(driver):
    # The main function will return -1 as an OS exit
    # code if the tests failed and 0 if they passed.
    test = test_scores_service(driver)
    if test[0]:
        return 0, test[1]
    else:
        return -1

try:
    result = main_function(driver=driver)
    print(f'Test Completed Successfully. Score: {result[1]}')
except Exception as e:
    print(f'Error: {e}')