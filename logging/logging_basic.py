import logging

def execute():
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(filename="hello.log", level=logging.DEBUG, format=format, datefmt="%d/%m/%y %I:%M:%S %p")


    log = logging.getLogger(__name__)

    log.info("Info message")
    log.debug("Debug messega")
    log.warning("Warning message")
    log.error("Error message")

if __name__ == '__main__':
   execute() 
