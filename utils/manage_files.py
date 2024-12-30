from time import time, sleep
from pathlib import Path
from traceback import format_exc

class ManageFiles:
    
    def __init__(self):
        self.download_path = Path(Path(__file__).parent.parent , "downloads")
        self.verify_path_exists()

    def verify_path_exists(self) -> None:
         
        if not self.download_path.exists():
            self.download_path.mkdir()
        
        return
    
    def verify_download(self, timeout:int = 120) -> dict:
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
        
    def infos(self) -> None:
        
        sleep(1)
        
        for file in self.download_path.iterdir():
            if file.is_file():
                print(f"Nome do arquivo: {file.name}")
                
                print(f"Caminhos completo do arquivo: {file.absolute()}")