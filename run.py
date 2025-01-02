from robot.robot import Robot
import logging

logging.basicConfig(filename="robot.log", filemode="a", format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)

if __name__ == "__main__":
    logging.error("TESTE IMENSO!!!!")
    robo = Robot()
    robo.start()