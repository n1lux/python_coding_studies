import logging

format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.DEBUG, format=format)


log = logging.getLogger(__name__)

log.info("Info message")
log.debug("Debug messega")
log.warning("Warning message")
log.error("Error message")
