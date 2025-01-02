from robot.robot import Robot
import logging
from datetime import datetime
from models.db_model import DBModel
from uuid import uuid4

logging.basicConfig(filename="robot.log", filemode="a", format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)

def run_robot():
    
    db_automation_logs = DBModel("automation_logs", True)
    
    now = datetime.now()
    
    
    id = str(uuid4())
    
    print(f'Executando robo download python id: {id} Inicio: {now.strftime("%d/%m/%Y %H:%M:%S")}')
    
    job = {
        "id_job" : id,
        "robo" : "robot_download_python",
        "inicio" : f'{now.strftime("%d/%m/%Y %H:%M:%S")}',
        "status_download" : "",
        "nome_arquivo" : "",
        "diretorio" : "",
        "fim" : "",
    }
    
    db_automation_logs.create(job)
    
    robo = Robot()
    robo.start(id)
    
    fim = datetime.now()
    
    db_automation_logs.update({"id_job" : id}, {"fim" : f'{fim.strftime("%d/%m/%Y %H:%M:%S")}'})

if __name__ == "__main__":
    run_robot()