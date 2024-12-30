from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from pathlib import Path
from traceback import format_exc

class Driver():
    
    def __init__(self):
        self.__driver:ChromeWebDriver
        
    def get_chrome_driver(self) -> ChromeWebDriver|dict:
        """Retorna um driver de navegador Chrome com configuraoes padrao.
        
        As configuraoes padrao para maximizar a janela do navegador
        e configurar o diretorio padrao para salvar os arquivos e desativação
        do prompt para download.
        
        Caso nao consiga retornar um driver, retorna um dicionario com 
        as informaoes de erro.
        
        Returns:
            ChromeWebDriver|dict: Driver de navegador Chrome configurado ou 
            dicionario com informaoes de erro.
        """
        
        try:
        
            self.__service = ChromeService(executable_path=ChromeDriverManager().install())
            
            self.__options = ChromeOptions()
            
            self.__options.add_argument("--no-sandbox")
            self.__options.add_argument("--disable-dev-shm-usage")
            
            self.__options.add_experimental_option('prefs' , {
                'download.default_directory': str(Path(Path(__file__).parent.parent, "downloads")),
                'download.prompt_for_download': False,
                'download.directory_upgrade': True
            })
            
            self.__driver = ChromeWebDriver(service=self.__service, options=self.__options)
            
            self.__driver.maximize_window()
            
            return self.__driver
        
        except Exception:
            return {'error' : True, "type" : "Erro inesperado ao iniciar o Navegador", "data" : f'{format_exc()}'}
