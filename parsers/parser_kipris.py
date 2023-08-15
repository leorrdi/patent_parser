from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from parsers.Patent import Patent


def parseKipris(numberPatents, name, patentBool=True, untilityModelBool=True,
                unexaminedBool=True, withDrawnBool=True, endedBool=True, abandoendBool=True,
                invalidatedBool=True, rejectedBool=True, registered=True, ipc='', cpc='',
                publicationStartDate='', publicationEndDate='', registrationStartDate='', registrationEndDate=''):
    try:
        driver = webdriver.Chrome()
        driver.get('http://engpat.kipris.or.kr/engpat/searchLogina.do?next=MainSearch')
    except:
        driver = webdriver.Ie()
        driver.get('http://engpat.kipris.or.kr/engpat/searchLogina.do?next=MainSearch')

    result = []
    driver.implicitly_wait(20)

    parameterSetting(driver, name, patentBool, untilityModelBool,
                unexaminedBool, withDrawnBool, endedBool, abandoendBool,
                invalidatedBool, rejectedBool, registered, ipc, cpc,
                publicationStartDate, publicationEndDate, registrationStartDate, registrationEndDate)
    driver.find_element(By.ID, 'btnItemizedSearch').click()
    sleep(10)
    

    pageCounter = 2
    while len(result) < numberPatents-1:
        patents = driver.find_element(By.NAME, 'listForm').find_elements(By.TAG_NAME, 'article')        
        for patent in patents:
            title = patent.find_element(By.CLASS_NAME, 'stitle').text
            date = patent.find_element(By.CLASS_NAME, 'point01').text.split()[1].replace('(', '').replace(')', '')
            link = patent.find_element(By.CLASS_NAME, 'point01').text.split()[0]
            descriprion = patent.find_element(By.CLASS_NAME, 'search_txt').text
            
            result.append(Patent(title, link, date, descriprion, "Киприс"))
            if len(result) == numberPatents: break
        
        try:
            driver.find_element(By.XPATH, f'/html/body/div[2]/div/section[3]/section/div[2]/form/div/a[{pageCounter}]').click()
            sleep(10)
            pageCounter+=1
        except:
            break

    driver.quit()
    print(len(result))
    return result 


def parameterSetting(driver, name, patentBool=True, untilityModelBool=True,
                unexaminedBool=True, withDrawnBool=True, endedBool=True, abandoendBool=True,
                invalidatedBool=True, rejectedBool=True, registered=True, ipc='', cpc='',
                publicationStartDate='', publicationEndDate='', registrationStartDate='', registrationEndDate=''):
    driver.find_element(By.ID, 'ToggleSmartFinder').click()

    if not patentBool: driver.find_element(By.ID, 'smartGubn00').click()
    if not untilityModelBool: driver.find_element(By.ID, 'smartGubn01').click()

    if not unexaminedBool: driver.find_element(By.ID, 'smartHangjung01').click()
    if not withDrawnBool: driver.find_element(By.ID, 'smartHangjung02').click()
    if not endedBool: driver.find_element(By.ID, 'smartHangjung03').click()
    if not abandoendBool: driver.find_element(By.ID, 'smartHangjung04').click()
    if not invalidatedBool: driver.find_element(By.ID, 'smartHangjung05').click()
    if not rejectedBool: driver.find_element(By.ID, 'smartHangjung06').click()
    if not registered: driver.find_element(By.ID, 'smartHangjung07').click()

    driver.find_element(By.XPATH, '/html/body/div[2]/div/section[1]/form/fieldset/div[1]/div[1]/table/tbody/tr[3]/td/input').send_keys(name)

    driver.find_element(By.ID, 'IPC').send_keys(ipc)
    driver.find_element(By.ID, 'CPC').send_keys(cpc)

    driver.find_element(By.ID, 'PD_FROM').send_keys(publicationStartDate)
    driver.find_element(By.ID, 'PD_TO').send_keys(publicationEndDate)

    driver.find_element(By.ID, 'GD_FROM').send_keys(registrationStartDate)
    driver.find_element(By.ID, 'GD_TO').send_keys(registrationEndDate)


