from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import platform

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--headless')  # Add this line for headless mode

system_os = platform.system()

if system_os == 'Windows':
    driver = webdriver.Chrome(service=Service(r"tests/chromedriver.exe"), options=options)
else:
    driver = webdriver.Chrome(service=Service(r"tests/chromedriver"), options=options)

def test_scores_service(driver):
    driver.get("http://127.0.0.1:5000/")
    score_element = int(driver.find_element(By.ID, "score").text)
    if 1000 >= score_element >= 1:
        return True, score_element
    else:
        return False, score_element

def main_function(driver):
    test = test_scores_service(driver)
    if test[0]:
        return 0, test[1]
    else:
        return -1, test[1]

if __name__ == "__main__":
    try:
        result = main_function(driver=driver)
        print(f'Test Completed Successfully. Score: {result[1]}')
    except Exception as e:
        print(f'Error: {e}')
    finally:
        driver.quit()  # Make sure to close the browser window
