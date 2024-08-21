import logging

# 로거 설정
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)  # 로그 레벨 설정 (DEBUG, INFO, WARNING, ERROR, CRITICAL)

# 콘솔 핸들러 설정
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# 파일 핸들러 설정 (파일에 로그 기록)
file_handler = logging.FileHandler('my_log.log')
file_handler.setLevel(logging.INFO)

# 포맷터 설정
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# 핸들러를 로거에 추가
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# 로그 메시지 출력
logger.debug('')
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

# 핸들러 제거 (필요시)
logger.removeHandler(console_handler)
logger.removeHandler(file_handler)

