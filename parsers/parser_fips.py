from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from parsers.Patent import Patent

def parseFips(numberPatents, name, nameParameter='', documentNumber='', datePublication='', mpk='', applicant='', author='' , patentHolders='', datePublicationApp=''):
  try:
    driver = webdriver.Chrome()
    driver.get('https://www1.fips.ru/iiss/')
  except:
    driver = webdriver.Ie()
    driver.get('https://www1.fips.ru/iiss/')

  driver.implicitly_wait(5)
  driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[1]/div[2]/div/div[2]/form/div[1]/div[1]').click()
  driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[1]/div[2]/div/div[2]/form/div[1]/div[3]/div[1]/div/table/tbody/tr[1]/td[1]/div/div[1]/input').click()
  driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/form/ul[1]/li[2]/a').click()
  driver.implicitly_wait(10)

  driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[1]/div[2]/div/div/form/div[1]/div[1]/div[2]/textarea').send_keys(name)
  driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[1]/div[2]/div/div/form/div[1]/div[3]/div[2]/input').send_keys(nameParameter)
  driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[1]/div[2]/div/div/form/div[1]/div[4]/div[2]/input').send_keys(documentNumber)
  driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[1]/div[2]/div/div/form/div[1]/div[5]/div[2]/input').send_keys(datePublication)
  driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[1]/div[2]/div/div/form/div[1]/div[6]/div[2]/input').send_keys(mpk)
  driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[1]/div[2]/div/div/form/div[1]/div[7]/div[2]/input').send_keys(applicant)
  driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[1]/div[2]/div/div/form/div[1]/div[8]/div[2]/input').send_keys(author)
  driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[1]/div[2]/div/div/form/div[1]/div[9]/div[2]/input').send_keys(patentHolders)
  driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[1]/div[2]/div/div/form/div[1]/div[10]/div[2]/input').send_keys(datePublicationApp)

  driver.find_element(By.NAME, 'j_idt92').click()


  result = [] 

  id = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[1]/div[2]/div/form/div[5]/a[6]').get_attribute('id')

  while len(result) < numberPatents-1:
    els = driver.find_elements(By.CLASS_NAME, 'tr')
    driver.implicitly_wait(5)
    for el in els:
      data = el.text.split(' ', 3)
      if (data[1] != 'Номер'):
        date = dateStandardization(data[2][1:-1])
        title = data[3]
        link = data[1]
        result.append(Patent(title, link, date, description='', source='Фипс'))
        if len(result) == numberPatents: break

    driver.implicitly_wait(5)

    #id = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[1]/div[2]/div/form/div[5]/a[6]').get_attribute('id')

    try:
      driver.find_element(By.ID, id).click()
    except:
      break

    sleep(2)

  driver.quit()
  return result


def dateStandardization(date):
    a = date.split('.')
    a.reverse()
    return '-'.join(a)
