from selenium.webdriver.chrome.webdriver import WebDriver
from traceback import format_exc
from utils.waits import Waits

class PythonPage:
    
    def __init__(self, driver:WebDriver):
        self._driver:WebDriver = driver
        self._waits:Waits = Waits(self._driver)
        
    def search_version(self) -> dict:
        try:
            search_input = self._waits.wait_visibility({"css_selector" : 'input[id="id-search-field"]'})
            search_input.send_keys("3.11.9")
            
            search_button = self._waits.wait_clickable({"css_selector" : 'fieldset[title="Search Python.org"] button[id="submit"]'})
            search_button.click()
            
            return {"error" : False, "type" : "", "data" : ""}
            
        except Exception:
            return {"error" : True, "type" : "Erro ao pesquisar versão do Python", "data" : f"{format_exc()}"}
        
    def open_page_version(self) -> dict:
        try:
            
            versions = self._waits.wait_visibility_all({"css_selector" : 'ul[class="list-recent-events menu"] h3 a'})
            
            for version in versions:
                if version.text == "Python 3.11.9":
                    version.click()
                    break
                
            else:
                return {"error" : True, "type" : "Erro version correta do Python não encontrada!", "data" : "Erro version correta do Python não encontrada!"}
            
            return {"error" : False, "type" : "", "data" : ""}
                    
        except Exception:
            return {'error' : True, "type" : "Erro inesperado ao abrir tela da versão do python", "data" : f"{format_exc()}"}
        
    def download_version(self) -> dict:
        try:
            all_version = self._waits.wait_visibility_all({"css_selector" : 'div[id="content"] div[class="container"] table tr td:nth-child(1) a'})
            
            url = ""
            
            for version in all_version:
                
                if version.text == "Windows installer (64-bit)":
                    return {"error" : False, "type" : "", "data" : "", "url" : f'{version.get_attribute("href")}'}
                    break
            else:
                return {"error" : True, "type" : "Erro versão de Windows 64 Bits não encontrada!", "data" : "Erro versão de Windows 64 Bits não encontrada!"}
            
            return {"error" : False, "type" : "", "data" : ""}
        
        except Exception:
            return {"error" : True, "type" : "Erro inesperado ao encontrar url do python 64 bits windows", "data" : f"{format_exc()}"}
                
