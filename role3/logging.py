import logging #logging 도구 import

logger = logging.getLogger("main") #main에 대해서 logger 설정
logger.setLevel(logging.INFO) #logging.INFO 설정

formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s') #logger 출력 형식

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger. addHandler(stream_handelr) #logger 출력 3줄코딩