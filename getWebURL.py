from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select # type: ignore
from time import sleep
import datetime

header = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15"
ser = Service('.\chromedriver.exe')# type: ignore
op = webdriver.ChromeOptions()
op.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
op.add_experimental_option('useAutomationExtension', False)
op.add_experimental_option("detach", True)
op.add_experimental_option("prefs", {"profile.password_manager_enabled": False, "credentials_enable_service": False})

def waitXpath(xpath, driver):
    locator = (By.XPATH, xpath)
    WebDriverWait(driver, 2).until(EC.presence_of_all_elements_located(locator))

txt_path="/Users/ro9air/VScode/test_scratchTSMC/webURL.txt"

if __name__ == "__main__":
    driver=webdriver.Chrome(service=ser,options=op)
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
        Object.defineProperty(navigator, 'webdriver', {
        get: () => undefined
        })
    """
    })
    driver.maximize_window()
    #目標網址
    driver.get('https://webpro.twse.com.tw/WebPortal/search/investor/?searchPageUrl=%2FWebPortal%2Fsearch%2Finvestor%2F&keyword=%E6%96%B0%E5%85%89%E9%87%91&eventDateFrom=&eventDateTo=&topCategoryId=&subCategoryId=&industryCode=&market=&speaker=&description=&order=eventDate&queryType=normal')
    try:
        for i in range(0,4):#總共8頁
            res_url = []
            driver.implicitly_wait(20)
            sleep(3)
            for i in range(1, 11):  # Assuming there are 10 videos per page
                url_xpath = f"/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div[1]/ul/li[{i}]/div[1]/a"
                time_xpath = f"/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div[1]/ul/li[{i}]/div[2]/ul/li[1]"
                company_xpath = f"/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div[1]/ul/li[{i}]/div[2]/ul/li[2]"
                title_xpath = f"/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div[1]/ul/li[{i}]/div[2]/ul/li[3]/span"
                try:
                    url_element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, url_xpath)))
                    url = url_element.get_attribute('href') if url_element else "N/A"
                    time_element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, time_xpath)))
                    time = time_element.text if time_element else "N/A"
                    company_element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, company_xpath)))
                    company = company_element.text if company_element else "N/A"
                    title_element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, title_xpath)))
                    title = title_element.text if title_element else "N/A"
                except Exception as e:
                    print(f"Error when scraping video {i} on page {driver.current_url}: {e}")
                    continue
                res_url.append(f"{time},{company},{title},{url}\n")
            next_page_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="arrow_right"]')))
            next_page_button.click()
            
            with open(txt_path,'r',encoding="utf-8") as f:
                a = f.readlines()
                a.extend(res_url)
            with open(txt_path,'w',encoding="utf-8") as f:
                f.writelines(a)
                
        driver.close()
    except Exception as e:
        print(e)
