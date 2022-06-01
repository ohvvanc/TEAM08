import logging #logging 도구 import

logger = logging.getLogger("main") #main에 대해서 logger 설정
logger.setLevel(logging.INFO) #logging.INFO 설정
logger.info("Info Log")
