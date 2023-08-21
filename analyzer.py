from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
import time

# Function to navigate to a group by name
def goToGroup(driver, name):
    inp_xpath_search = '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p'
    input_box_search = WebDriverWait(driver, 50).until(
        lambda driver: driver.find_element(By.XPATH, inp_xpath_search)
    )
    input_box_search.click()
    time.sleep(1)
    input_box_search.send_keys(Keys.COMMAND + "a")
    input_box_search.send_keys(Keys.DELETE)
    time.sleep(1)
    input_box_search = WebDriverWait(driver, 50).until(
        lambda driver: driver.find_element(By.XPATH, inp_xpath_search)
    )
    input_box_search.send_keys(name)
    time.sleep(1)
    input_box_search.send_keys(Keys.ENTER)

# Function to retrieve names from a group
def getFromGroup(driver):
    driver.find_element(By.XPATH, '//*[@id="main"]/header').click()
    time.sleep(1)
    allbar = driver.find_element(
        By.CLASS_NAME,
        "_1UABU.q1n4p668.ln8gz9je.ddw6s8x9.p357zi0d.gndfcl4n.pm5hny62.os03hap6",
    )

    ar = []
    ext = False
    try:
        allbar.find_element(By.CLASS_NAME, "ggj6brxn.ljrqcn24.jq3rn4u7")
        ext = True
    except:
        ext = False

    if ext:
        allbar.click()
        time.sleep(2)
        for i in range(10):
            names = driver.find_element(
                By.XPATH, '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div'
            ).find_elements(
                By.CLASS_NAME,
                "ggj6brxn.gfz4du6o.r7fjleex.g0rxnol2.lhj4utae.le5p0ye3.l7jjieqr._11JPr",
            )
            for name in names:
                ar.append(str(name.text))

            driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;",
                driver.find_element(
                    By.XPATH,
                    '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div/div[2]',
                ),
            )
            time.sleep(1)
            ar = list(set(ar))
        ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    else:
        allbar.click()
        time.sleep(1)
        names = driver.find_element(
            By.XPATH,
            '//*[@id="app"]/div/div/div[6]/span/div/span/div/div/div/section/div[7]',
        ).find_elements(
            By.CLASS_NAME,
            "ggj6brxn.gfz4du6o.r7fjleex.g0rxnol2.lhj4utae.le5p0ye3.l7jjieqr._11JPr",
        )
        for name in names:
            ar.append(str(name.text))

    return ar

# Function to retrieve names from the community
def getFromCommunity(driver):
    driver.find_element(By.XPATH, '//*[@id="main"]/header/div[2]').click()
    time.sleep(1)
    driver.find_element(
        By.XPATH,
        '//*[@id="app"]/div/div/div[6]/span/div/span/span/div/div/section/div[2]/div/div/button[1]',
    ).click()
    time.sleep(1)
    driver.find_element(
        By.CLASS_NAME,
        "_1UABU.q1n4p668.ln8gz9je.ddw6s8x9.p357zi0d.gndfcl4n.pm5hny62.os03hap6",
    ).click()
    time.sleep(2)
    ar = []
    for i in range(10):
        names = driver.find_element(
            By.XPATH, '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div/div'
        ).find_elements(
            By.CLASS_NAME,
            "ggj6brxn.gfz4du6o.r7fjleex.g0rxnol2.lhj4utae.le5p0ye3.l7jjieqr._11JPr",
        )
        for name in names:
            ar.append(str(name.text))

        driver.execute_script(
            "arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;",
            driver.find_element(
                By.XPATH,
                '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div/div/div[2]',
            ),
        )
        time.sleep(1)
        ar = list(set(ar))
    ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    return ar

# Function to get names from a group
def getNamesFromGroup(driver, name):
    goToGroup(driver, name)
    return getFromGroup(driver)

# Function to get names from a community
def getNamesFromCommunity(driver, name):
    goToGroup(driver, name)
    return getFromCommunity(driver)

# Function to get names from a group and write them to a file
def getAndWriteToFile(driver, fname):
    names = getNamesFromGroup(driver, fname)
    with open(fname + ".txt", "w") as file:
        for item in names:
            file.write(item + "\n")
    print("Finished " + fname + "!")

# Function to get names from multiple groups and write them to files
def getAndWriteToFiles(arr):
    for i in arr:
        getAndWriteToFile(i)