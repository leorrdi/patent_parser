from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from parsers.Patent import Patent


def parseRospatent(numberPatents, name, patentNumber='', startDate='', endDate='', author='', patentHolder='', applicant='', russiaBefot1944=True, russiaSince1944=True, cisPatents=True):
    try:
        driver = webdriver.Chrome()
        driver.get('https://searchplatform.rospatent.gov.ru/patents')
    except:
        driver = webdriver.Ie()
        driver.get('https://searchplatform.rospatent.gov.ru/patents')

    result = []
    driver.implicitly_wait(10)

    parameterSetting(driver, name, patentNumber, startDate, endDate, author, patentHolder, applicant, russiaBefot1944, russiaSince1944, cisPatents)
    sleep(1)
    driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div/div[2]/div/div/button').click()

    while len(result) < numberPatents-1:
        patents = driver.find_element(By.CLASS_NAME, 'report_results').find_elements(By.CLASS_NAME, 'report_wrap')
        for patent in patents:
            documentInformation = patent.find_element(By.CLASS_NAME, 'report_info').find_elements(By.TAG_NAME, 'li')[1].text.split()
            documentNumber = documentInformation[1] + documentInformation[2] + documentInformation[3]

            date = documentInformation[-1]
            link =  f"https://searchplatform.rospatent.gov.ru/doc/{documentNumber}_{date.replace('.', '')}"
            title = patent.find_element(By.CLASS_NAME, 'report_caption ').text
            description = patent.find_element(By.CLASS_NAME, 'report_snippet').text

            result.append(Patent(title, link, date, description, 'Rospatent'))
            if len(result) == numberPatents: break
        try:
            driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div/div[4]/div[4]/div/div[3]/ul/li[9]').click()
            sleep(3)
        except:
            break
        
    driver.quit()
    print(len(result))
    return result


def parameterSetting(driver, name, patentNumber='', startDate='', endDate='', author='', patentHolder='', applicant='', russiaBefot1944=True, russiaSince1944=True, cisPatents=True):
    driver.find_element(By.ID, 'simple_search_input').send_keys(name)
    driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div/div[3]/div[1]/div[1]/div[1]/input').send_keys(patentNumber)
    driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div/div[3]/div[1]/div[2]/div/input').send_keys(author)
    driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div/div[3]/div[1]/div[3]/div/input').send_keys(patentHolder)
    driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div/div[3]/div[1]/div[4]/div/input').send_keys(applicant)
    driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div/div[3]/div[1]/div[1]/div[2]/div[2]/div/div/input'
                        ).send_keys(startDate)
    driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div/div[3]/div[1]/div[1]/div[3]/div[2]/div/div/input'
                        ).send_keys(endDate)
    driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div/div[3]/div[2]/div[2]/form/div/div[1]/div[1]').click()
    if russiaBefot1944 == False:
        driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div/div[3]/div[2]/div[2]/form/div/div[2]/label[1]').click()
    if russiaSince1944 == False:
        driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div/div[3]/div[2]/div[2]/form/div/div[2]/label[2]').click()
    if cisPatents == False:
        driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div/div[3]/div[2]/div[2]/form/div/div[2]/label[3]').click()
