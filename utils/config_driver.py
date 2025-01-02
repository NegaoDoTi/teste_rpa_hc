from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from traceback import format_exc

class Driver():
    """Classe responsavel pro gerenciar driver selenium que o robo irá utilizar!
    """
    
    def __init__(self):
        self.__driver:webdriver
        
    def get_chrome_driver(self) -> webdriver.Remote | dict:
        """Responsavel por conectar Python ao driver Selenium, e definir as opções 

        Returns:
            webdriver.Remote | dict: {bool, str, str}
        """
        
        
        try:
        
            #self.__service = ChromeService(executable_path=ChromeDriverManager().install())
            
            self.__options = ChromeOptions()
            
            self.__options.add_argument("--no-sandbox")
            self.__options.add_argument("--disable-dev-shm-usage")
            
            self.__driver = webdriver.Remote("http://selenium:4444/wd/hub", DesiredCapabilities.CHROME, options=self.__options)
            
            self.__driver.maximize_window()
            
            return self.__driver
        
        except Exception:
            return {'error' : True, "type" : "Erro inesperado ao iniciar o Navegador", "data" : f'{format_exc()}'}
