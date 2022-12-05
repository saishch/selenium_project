import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions



def login():
    #this is a function to change page  with auto click with css selector
    def click_on_page_with_css_selector(balise,classe,indice):
        driver.find_elements(By.CSS_SELECTOR, balise+"[class='"+ classe +"']")[indice].click()
        time.sleep(3)

    #this is a function to change page  with auto click with class name
    def click_on_page_with_class_name(classe):
        driver.find_element(By.CLASS_NAME,classe).click()
        time.sleep(3)
   

    #this is a function to change page  with auto click with id
    def click_on_page_with_id(id,keys):
        driver.find_element(By.ID,id).send_keys(keys)
        time.sleep(3)
   
    options = ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)

    driver.get('https://test.maplab.app/auth/login')

    click_on_page_with_id('email','luce@maplab.green')

    click_on_page_with_id('password','FVvUd48YT97O')
    
    click_on_page_with_class_name('v-btn__content')

    click_on_page_with_css_selector("a",'v-list-item v-list-item--link theme--light',1)

    click_on_page_with_css_selector("a",'v-tab',3)
  
    click_on_page_with_class_name('v-list-item__content')

    click_on_page_with_css_selector("i",'v-icon notranslate mr-1 mdi mdi-account theme--light',0)
    
    click_on_page_with_css_selector("a",'v-tab',0)
    

login()
 
