from selenium import webdriver
#from selenium.webdriver.chrome.service import Service as ChromeService
import warnings
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


def createDriver():
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    driver = webdriver.Chrome('')

    return driver


def NBC26(driver, email):
    driver.get("https://www.nbc26.com/account/manage-email-preferences")

    # Fill email textbox.
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/form/div[2]/input").send_keys(email)

    # Select all checkboxes.
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/div["
                                                                              "2]/form/div[3]/fieldset/div/div["
                                                                              "2]/div/div[1]/input")))
    driver.find_element(By.XPATH,
                        "/html/body/div[3]/div/div/div[2]/form/div[3]/fieldset/div/div[2]/div/div[1]/input").click()
    driver.find_element(By.XPATH,
                        "/html/body/div[3]/div/div/div[2]/form/div[3]/fieldset/div/div[2]/div/div[2]/input").click()
    driver.find_element(By.XPATH,
                        "/html/body/div[3]/div/div/div[2]/form/div[3]/fieldset/div/div[2]/div/div[3]/input").click()
    driver.find_element(By.XPATH,
                        "/html/body/div[3]/div/div/div[2]/form/div[3]/fieldset/div/div[2]/div/div[4]/input").click()

    # Click submit button.
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/form/div[3]/div/input").click()

    print("Signed up for NBC26")


def crosswalk(driver, email):
    driver.get("https://www.crosswalk.com/newsletters/")

    try:
        WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.XPATH, "//input[@type='checkbox']")))
        checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

        for checkbox in checkboxes:
            checkbox.click()

    except TimeoutException:
        print("Timeout - No tags found")

    try:
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div["
                                                                                  "4]/div/div["
                                                                                  "1]/div/div/div/div/div/div/div["
                                                                                  "7]/input[2]")))
        driver.find_element(By.XPATH, "/html/body/div[3]/div/div[4]/div/div[1]/div/div/div"
                                      "/div/div/div/div[7]/input[2]").send_keys(email)
    except TimeoutException:
        print("Timeout - No tag found for email")

    try:
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div[4]/div/"
                                                                                  "div[1]/div/div/div/div/div/div/div"
                                                                                  "[7]/a")))
        driver.find_element(By.XPATH, "/html/body/div[3]/div/div[4]/div/div[1]/div/div/div"
                                      "/div/div/div/div[7]/a").click()
    except TimeoutException:
        print("Timeout - No tag found for sign up")

    print("Signed up for Crosswalk")


def wsj(driver, email):
    def wsjHelper(subscribePath, touPath, emailPath, signUpPath, closePath):

        try:
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, subscribePath)))
            element = driver.find_element(By.XPATH, subscribePath)

            driver.execute_script("arguments[0].scrollIntoView();", element)
            element.click()
        except TimeoutException:
            print("Timeout - No tag found")

        try:
            WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, touPath))).click()
        except TimeoutException:
            print("Timeout - No tag for Terms of Use found")

        try:
            WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, emailPath))).send_keys(email)
        except TimeoutException:
            print("Timeout - No tag for email found")

        time.sleep(1)

        try:
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, signUpPath))).click()
        except TimeoutException:
            print("Timeout - No tag for sign up found")

        try:
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, closePath)))
        except TimeoutException:
            print("Timeout - No tag for close found")

    driver.get("https://www.wsj.com/newsletters")

    for count in range(3, 34):
        wsjHelper("/html/body/div[1]/div/div/div/div/div[2]/div[1]/div[{}]/div/div[2]/div/div/div".format(str(count)),
                  "/html/body/div[1]/div/div[2]/div/div[1]/div/div[1]/div[1]/div/label/span",
                  "/html/body/div[1]/div/div[2]/div/div[1]/div/div[2]/div[2]/input",
                  "/html/body/div[1]/div/div[2]/div/div[1]/div/div[2]/div[3]/button",
                  "/html/body/div[1]/div/div[2]/div/div[1]/div/button")

    for count in range(39, 45):
        wsjHelper("/html/body/div[1]/div/div/div/div/div[2]/div[1]/div[{}]/div/div[2]/div/div/div".format(str(count)),
                  "/html/body/div[1]/div/div[2]/div/div[1]/div/div[1]/div[1]/div/label/span",
                  "/html/body/div[1]/div/div[2]/div/div[1]/div/div[2]/div[2]/input",
                  "/html/body/div[1]/div/div[2]/div/div[1]/div/div[2]/div[3]/button",
                  "/html/body/div[1]/div/div[2]/div/div[1]/div/button")

    for count in range(2, 19):
        if count == 12:
            continue

        wsjHelper("/html/body/div[1]/div/div/div/div/div[2]/div[2]/div[{}]/div/div[2]/div/div/div".format(str(count)),
                  "/html/body/div[1]/div/div[2]/div/div[1]/div/div[1]/div[1]/div/label/span",
                  "/html/body/div[1]/div/div[2]/div/div[1]/div/div[2]/div[2]/input",
                  "/html/body/div[1]/div/div[2]/div/div[1]/div/div[2]/div[3]/button",
                  "/html/body/div[1]/div/div[2]/div/div[1]/div/button")
    time.sleep(10)
    print("Signed up for Wall Street Journal")


def main(email):
    # Forcing email to be a string.
    email = str(email)

    driver = createDriver()

    # NBC26(driver, email)
    crosswalk(driver, email)
    # wsj(driver, email)

    # Destroy driver.
    driver.quit()
