from models.logger import Logger

def setup_logger_obj():
    my_logger = Logger('logs.txt')
    my_logger.setup()

def log_get_req(route, result):
    my_logger = Logger('logs.txt')
    my_logger.log_change('GET', route, result)

def log_post_req(route, result):
    my_logger = Logger('logs.txt')
    my_logger.log_change('POST', route, result)