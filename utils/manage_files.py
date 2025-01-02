from time import time, sleep
from pathlib import Path
from traceback import format_exc
from requests import get

class ManageFiles:
    
    def __init__(self):
        self.download_path = Path(Path(__file__).parent.parent , "downloads")
        self.verify_path_exists()

    def verify_path_exists(self) -> None:
        """Verificar se a pasta download existe, se não existir cria.
        """
         
        if not self.download_path.exists():
            self.download_path.mkdir()
        
        return
    
    def verify_download(self, timeout:int = 120) -> dict:
        """Verifica se o download do exe python foi concluido!

        Args:
            timeout (int, optional): tempo limite de espera para conclusão do download. Defaults to 120.

        Returns:
            dict: {bool, str, str}
        """
        
        try:
            start = time()
            
            while True:
                
                download_progress = any(file.suffix == ".crdownload" for file in self.download_path.iterdir())
                
                if not download_progress:
                    print("Download Concluido!")
                    return {"error" : False, "type" : "", "data" : ""}
                
                elapsed = time() - start
                
                if elapsed > timeout:
                    return {"error" : True, "type" : "O tempo limite para o download ser concluido foi execiddo", "data" : "O tempo limite para o download ser concluido foi execiddo"}
                
                sleep(1)
                
        except Exception:
            return {"error" : True, "type" : "Erro inesperado ao realizar Download do python", "data" : f"{format_exc()}"}
        
    def script_download_file(self, url:str) -> dict:
        """Responsavel por fazer download do exe do Python

        Args:
            url (str): URL de download do site oficial do Python

        Returns:
            dict: {bool, str, str}
        """
        
        try:
            download = get(url=url, stream=True)
            download.raise_for_status()
            
            with open(f"{self.download_path}/python_windows_64bits.exe", "wb") as file_exe:
                for chunk in download.iter_content(chunk_size=8192):
                    if chunk:
                        file_exe.write(chunk)
                        
            return {"error" : False, "type" : "", "data" : ""}
            
        except Exception:
            return {"error" : True, "type" : "Erro inesperado ao baixar python", "data" : ""}
    
    def infos(self) -> dict:
        """Exibe nome do arquivo do exe Python e o caminho completo do arquivo

        Returns:
            dict: {bool, str, str, str, str}
        """
        
        try:
            sleep(1)
            
            for file in self.download_path.iterdir():
                if file.is_file():
                    name_file = file.name
                    print(f"Nome do arquivo: {file.name}")
                    
                    path_file = file.absolute()
                    print(f"Caminhos completo do arquivo: {file.absolute()}")
                    
            return {"error" : False, "type" : "", "data" : "", "name_file" : name_file, "path_file" : path_file}
        except Exception:
            return {"error" : True, "type" : "Erro inesperado ao buscar informaçoes do arquivo", "data" : f"{format_exc()}"}