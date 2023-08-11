from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from parsers.Patent import Patent

def parseWipo(numberPatents, name, language='', stemmingBool=True, onlyFamilyMemberBool=False, nplBool=False):
   try:
       driver = webdriver.Chrome()
       driver.get('https://patentscope.wipo.int/search/ru/advancedSearch.jsf')
   except:
       driver = webdriver.Ie()
       driver.get('https://patentscope.wipo.int/search/ru/advancedSearch.jsf')

   result = []
   driver.implicitly_wait(10)

   driver.find_element(By.XPATH, '/html/body/div[2]/div[5]/div/div[1]/form/div[2]/div/div[1]/div/div/div/div/div/div/div[1]/div/textarea').send_keys(name)
   dropdownbox = driver.find_element(By.ID, 'advancedSearchForm:queryLanguage:input').find_elements(By.TAG_NAME, 'Option') 
   if language == "English":
      dropdownbox[0].click()
   elif language == "Русский":
      dropdownbox[10].click() 

   if stemmingBool == False:
      driver.find_element(By.XPATH, '/html/body/div[2]/div[5]/div/div[1]/form/div[3]/div[1]/div[1]/div/div/span[3]/div/div/div[1]/fieldset/div/label/input').click() 

   if onlyFamilyMemberBool:
      driver.find_element(By.XPATH, '/html/body/div[2]/div[5]/div/div[1]/form/div[3]/div[1]/div[1]/div/div/span[4]/div/div/div[1]/fieldset/div/label/input').click() 

   if nplBool:
      driver.find_element(By.XPATH, '/html/body/div[2]/div[5]/div/div[1]/form/div[3]/div[1]/div[1]/div/div/span[5]/div/div/div[1]/fieldset/div/label/input').click() 

   driver.find_element(By.XPATH, '/html/body/div[2]/div[5]/div/div[1]/form/div[3]/div[2]/div/button[2]/span').click()


   while len(result) < numberPatents-1:
       names = driver.find_elements(By.CLASS_NAME, 'ps-patent-result--title--title')
       dates = driver.find_elements(By.CLASS_NAME, 'ps-patent-result--title--ctr-pubdate')
       links = driver.find_elements(By.CLASS_NAME, 'ps-patent-result--title')
       descriptions = driver.find_elements(By.CLASS_NAME, 'ps-patent-result')
       for i in range(len(names)):
           link = (links[i].find_element(By.TAG_NAME, 'a').get_attribute('href'))
           date = dateStandardization((dates[i].text.split(' ')[2]))
           title = (names[i].text)
           description = descriptions[i].find_elements(By.TAG_NAME, 'div')[6].text
           result.append(Patent(title, link, date, description, 'Випо'))
           if len(result) == numberPatents: break

       try:
        driver.find_element(By.CLASS_NAME, 'js-paginator-next').click()
       except:
        break

       sleep(2)

   driver.quit()
   return result

def dateStandardization(date):
    a = date.split('.')
    a.reverse()
    return '-'.join(a)


