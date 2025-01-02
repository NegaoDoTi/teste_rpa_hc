from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from traceback import format_exc
from utils.waits import Waits

class SearchPage:
    def __init__(self, driver:WebDriver):
        self._driver:WebDriver = driver
        self._waits:Waits = Waits(self._driver)
        
    def search(self) -> dict:
        try:
            self._driver.get('https://www.google.com.br/')
            
            textarea = self._waits.wait_visibility({"css_selector" : 'textarea[title="Pesquisar"]'})
            textarea.send_keys("baixar Python")
            
            textarea.send_keys(Keys.ENTER)
            
            return {"error" : False, "type" : "", "data" : ""}
            
        except Exception:
            return {"error" : True, "type" : "Erro ao fazer pesquisa", "data" : f"{format_exc()}"}
    
    def open_python_website(self) -> dict:
        try:
            
            a = self._waits.wait_clickable({"css_selector" : f'a[href="https://www.python.org/downloads/"]'})
            
            a.click()
            
            return {"error" : False, "type" : "", "data" : ""}
            
        except Exception:
            return {"error" : True, "type" : "Erro ao carregar site do Python", "data" : f"{format_exc()}"}

        