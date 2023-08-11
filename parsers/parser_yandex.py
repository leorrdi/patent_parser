from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from parsers.Patent import Patent

def parseYandex(numberPatents, name, document='', applications='', namePatent='', author='', patentHolder='',
                 startDate='', endDate='', applicationBool=True, patentBool=True):
   try:
       driver = webdriver.Chrome()
       driver.get('https://yandex.ru/patents')
   except:
       driver = webdriver.Ie()
       driver.get('https://yandex.ru/patents')

   driver.find_element(By.XPATH, '/html/body/div[1]/div/div[6]/div[2]/div[1]/div[3]/div[2]/span/input').send_keys(document)
   driver.find_element(By.XPATH, '/html/body/div[1]/div/div[6]/div[2]/div[1]/div[4]/span/input').send_keys(applications)
   driver.find_element(By.XPATH, '/html/body/div[1]/div/div[6]/div[2]/div[1]/div[6]/div[1]/span/input').send_keys(startDate)
   driver.find_element(By.XPATH, '/html/body/div[1]/div/div[6]/div[2]/div[1]/div[6]/div[2]/span/input').send_keys(endDate) 
   driver.find_element(By.XPATH, '/html/body/div[1]/div/div[6]/div[2]/div[1]/div[7]/span/input').send_keys(namePatent)
   driver.find_element(By.XPATH, '/html/body/div[1]/div/div[6]/div[2]/div[1]/div[8]/span/input').send_keys(author)
   driver.find_element(By.XPATH, '/html/body/div[1]/div/div[6]/div[2]/div[1]/div[9]/span/input').send_keys(patentHolder) 
   if applicationBool == False:
       driver.find_element(By.XPATH, '/html/body/div[1]/div/div[6]/div[2]/div[1]/div[2]/span[1]/span/span/input').click()
   if patentBool == False:
       driver.find_element(By.XPATH, '/html/body/div[1]/div/div[6]/div[2]/div[1]/div[2]/span[2]/span/span/input').click()
    
   driver.find_element(By.XPATH, '/html/body/div[1]/div/div[4]/div/div/header/div/div[1]/div[2]/form/div[1]/span/span/input').send_keys(name)

   driver.find_element(By.XPATH, '/html/body/div[1]/div/div[4]/div/div/header/div/div[1]/div[2]/form/div[2]/button').click()
 
   sleep(3)

   result = [] 

   while len(result) < numberPatents-1:
        patents_cards = driver.find_elements(By.CLASS_NAME, 'snippet-block')
        for patent_card in patents_cards: 
            title = patent_card.find_element(By.CLASS_NAME, 'snippet-title').text
            date = patent_card.find_elements(By.CLASS_NAME, 'date')[1].text.split(' ')[1]
            link = patent_card.find_element(By.TAG_NAME, 'a').get_attribute("href")
            description = patent_card.find_element(By.CLASS_NAME, 'snippet-text').text 

            result.append(Patent(title, link, date, description, 'Яндекс.Патенты'))
            if len(result) == numberPatents: break

        try:
           driver.implicitly_wait(10)
           driver.find_element(By.XPATH, '/html/body/div[1]/div/div[6]/div[1]/div[4]/div[1]/div[5]').click()
        except:
           break

        sleep(2)

   driver.quit()
   return result

