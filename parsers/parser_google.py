from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def parseGoogle(numberPatents, name, date='', author='', assign='', language='', status='', type='', litigation=''):
    try:
        driver = webdriver.Chrome()
        driver.get('https://patents.google.com/advanced')
    except:
        driver = webdriver.Ie()
        driver.get('https://patents.google.com/advanced')

    result = []

    driver.find_element(By.XPATH, '/html/body/search-app/search-results/search-ui/div/div/div[1]/div/'
                        'div/workspace-ui-search/div/mat-keyword-editor/outlined-textarea[1]/span[1]/textarea').send_keys(name)
    
    driver.find_element(By.XPATH, '/html/body/search-app/search-results/search-ui/div/div/div[1]/div/'
                        'div/workspace-ui-search/div/metadata-editor/div[1]/date-editor/div/div[2]/input[1]').send_keys(date)
    
    driver.find_element(By.XPATH, '/html/body/search-app/search-results/search-ui/div/div/div[1]/div/'
                        'div/workspace-ui-search/div/metadata-editor/div[2]/chips-input/input-chip/div[1]/textarea').send_keys(author)
    
    driver.find_element(By.XPATH, '/html/body/search-app/search-results/search-ui/div/div/div[1]/div/'
                        'div/workspace-ui-search/div/metadata-editor/div[3]/chips-input/input-chip/div[1]/textarea').send_keys(assign)
    
    driver.find_element(By.XPATH, '/html/body/search-app/search-results/search-ui/div/div/div[1]/div/'
                        'div/workspace-ui-search/div/metadata-editor/div[4]/restrict-editor/div/div[1]/dropdown-menu[2]/span'
                        ).click()
    languages_dropdown = driver.find_element(By.XPATH, '/html/body/search-app/search-results/search-ui/div/div/div[1]/div/div/workspace-ui-search/div/'
                                             'metadata-editor/div[4]/restrict-editor/div/div[1]/dropdown-menu[2]/iron-dropdown/div/div/div'
                                             ).find_elements(By.TAG_NAME, 'div')
    if language == "English":
        languages_dropdown[0].click()
    elif language == "Русский":
        languages_dropdown[9].click()
    
    driver.find_element(By.XPATH, '/html/body/search-app/search-results/search-ui/div/div/div[1]/div/div/workspace-ui-search/div/'
                                          'metadata-editor/div[4]/restrict-editor/div/div[2]/dropdown-menu[1]/span/span[1]'
                                          ).click()
    status_dropdown = driver.find_element(By.XPATH, '/html/body/search-app/search-results/search-ui/div/div/div[1]/div/div/workspace-ui-search/'
                                          'div/metadata-editor/div[4]/restrict-editor/div/div[2]/dropdown-menu[1]/iron-dropdown/div/div/div'
                                          ).find_elements(By.TAG_NAME, 'div')
    if status == "Грант":
        status_dropdown[0].click()
    elif status == "Заявка":
        status_dropdown[1].click()

    driver.find_element(By.XPATH, '/html/body/search-app/search-results/search-ui/div/div/div[1]/div/div/workspace-ui-search/div/'
                     'metadata-editor/div[4]/restrict-editor/div/div[2]/dropdown-menu[2]/span'
                     ).click()
    type_dropdown = driver.find_element(By.XPATH, '/html/body/search-app/search-results/search-ui/div/div/div[1]/div/div/workspace-ui-search/'
                                        'div/metadata-editor/div[4]/restrict-editor/div/div[2]/dropdown-menu[2]/iron-dropdown/div/div/div'
                                        ).find_elements(By.TAG_NAME, 'div')
    if type == 'Патент':
        type_dropdown[0].click()
    elif type == 'Проект':
        type_dropdown[1].click()

    driver.find_element(By.XPATH, '/html/body/search-app/search-results/search-ui/div/div/div[1]/div/div/workspace-ui-search/div/'
                        'metadata-editor/div[4]/restrict-editor/div/div[3]/dropdown-menu/span'
                        ).click()
    litigation_dropdown = driver.find_element(By.XPATH, '/html/body/search-app/search-results/search-ui/div/div/div[1]/div/div/workspace-ui-search/div/'
                                              'metadata-editor/div[4]/restrict-editor/div/div[3]/dropdown-menu/iron-dropdown/div/div/div'
                                              ).find_elements(By.TAG_NAME, 'div')
    if litigation == 'Имеет судебные разбирательства':
        litigation_dropdown[0].click()
    elif litigation == 'Не имеет судебные разбирательства':
        litigation_dropdown[1].click()
    
    while len(result) < numberPatents-1:
        patents = driver.find_elements(By.TAG_NAME, 'search-result-item')
        for patent in patents:
             link = f"https://patents.google.com/{patent.find_element(By.TAG_NAME, 'state-modifier').get_attribute('data-result')}"
             title = patent.find_element(By.ID, 'htmlContent').text
             description = patent.find_elements(By.TAG_NAME, 'raw-html')[-1].find_element(By.ID, 'htmlContent').text
             source = 'Google'


parseGoogle(10,"engine", litigation='Не имеет судебные разбирательства')