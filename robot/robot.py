from utils.config_driver import Driver
from selenium.webdriver.chrome.webdriver import WebDriver
from robot.pages.search_page import SearchPage
from robot.pages.python_page import PythonPage
from utils.manage_files import ManageFiles
from traceback import format_exc
from time import sleep
import logging

class Robot:
    
    def __init__(self):
        self.driver:WebDriver
        self.manage_files = ManageFiles()
        
    def start(self) -> None:
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
                return
            
            open_website = self.search_page.open_python_website()
            if open_website["error"] == True:
                logging.error(f'{open_website["type"]}, {open_website["data"]}')
                return 
            
            search_version_python = self.python_page.search_version()
            if search_version_python["error"] == True:
                logging.error(f'{search_version_python["type"]}, {search_version_python["data"]}')
                return
            
            open_page_version = self.python_page.open_page_version()
            if  open_page_version["error"] == True:
                logging.error(f'{open_page_version["type"]}, {open_page_version["data"]}')
                return
            
            download_python = self.python_page.download_version()
            if download_python["error"] == True:
                logging.error(f'{download_python["type"]}, {download_python["data"]}')
                return
            
            url = download_python["url"]
            
            download_file = self.manage_files.script_download_file(url)
            if download_file["error"] == True:
                logging.error(f'{download_file["type"]}, {download_file["data"]}')
                return
            
            verify_download = self.manage_files.verify_download()
            if verify_download["error"] == True:
                logging.error(f'{verify_download["type"]}, {verify_download["data"]}')
                return
            
            self.manage_files.infos()
            
        except Exception:
            ...
