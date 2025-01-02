from utils.config_driver import Driver
from selenium.webdriver.chrome.webdriver import WebDriver
from robot.pages.search_page import SearchPage
from robot.pages.python_page import PythonPage
from utils.manage_files import ManageFiles
from traceback import format_exc
from models.db_model import DBModel
import logging

class Robot:
    
    def __init__(self):
        self.driver:WebDriver
        self.manage_files = ManageFiles()
        self.db_automation_logs = DBModel("automation_logs")
        
    def start(self, id_job) -> None:
        try:
            self.driver = Driver().get_chrome_driver()
            if isinstance(self.driver, dict):
                if self.driver['error'] == True:
                    logging.critical(f'{self.driver["type"]}, {self.driver["data"]}')
                    return
            
            self.search_page = SearchPage(self.driver)
            self.python_page = PythonPage(self.driver)
            
            result_search = self.search_page.search()
            if result_search["error"] == True:
                logging.error(f'{result_search["type"]}, {result_search["data"]}')
                self.db_automation_logs.update({"id_job" : id_job}, {"status_download" : result_search["type"]})
                return
            
            open_website = self.search_page.open_python_website()
            if open_website["error"] == True:
                logging.error(f'{open_website["type"]}, {open_website["data"]}')
                self.db_automation_logs.update({"id_job" : id_job}, {"status_download" : open_website["type"]})
                return 
            
            search_version_python = self.python_page.search_version()
            if search_version_python["error"] == True:
                logging.error(f'{search_version_python["type"]}, {search_version_python["data"]}')
                self.db_automation_logs.update({"id_job" : id_job}, {"status_download" : search_version_python["type"]})
                return
            
            open_page_version = self.python_page.open_page_version()
            if  open_page_version["error"] == True:
                logging.error(f'{open_page_version["type"]}, {open_page_version["data"]}')
                self.db_automation_logs.update({"id_job" : id_job}, {"status_download" : open_page_version["type"]})
                return
            
            download_python = self.python_page.download_version()
            if download_python["error"] == True:
                logging.error(f'{download_python["type"]}, {download_python["data"]}')
                self.db_automation_logs.update({"id_job" : id_job}, {"status_download" : download_python["type"]})
                return
            
            url = download_python["url"]
            
            download_file = self.manage_files.script_download_file(url)
            if download_file["error"] == True:
                logging.error(f'{download_file["type"]}, {download_file["data"]}')
                self.db_automation_logs.update({"id_job" : id_job}, {"status_download" : download_file["type"]})
                return
            
            verify_download = self.manage_files.verify_download()
            if verify_download["error"] == True:
                logging.error(f'{verify_download["type"]}, {verify_download["data"]}')
                self.db_automation_logs.update({"id_job" : id_job}, {"status_download" : verify_download["type"]})
                return
            
            result = self.manage_files.infos()
            if result["error"] == True:
                logging.error(f'{result["type"]}, {result["data"]}')
                self.db_automation_logs.update({"id_job" : id_job}, {"status_download" : result["type"]})
                return
            
            self.db_automation_logs.update({"id_job" : id_job}, {"status_download" : "Download concluido com Sucesso!"})
            self.db_automation_logs.update({"id_job" : id_job}, {"nome_arquivo" : f'{result["name_file"]}'})       
            self.db_automation_logs.update({"id_job" : id_job}, {"diretorio" : f'{result["path_file"]}'})
            
            print("Conclui com sucesso sem erros!")
            
            return        
            
        except Exception:
            print(format_exc())
            
            self.db_automation_logs.update({"id_job" : id_job}, {"status_download" : "Erro inesperado!"})
            
            logging.critical(f'Erro inesperado: {format_exc()}')
            
            return

