import pytest

from models.logger import Logger

# Fixtures
@pytest.fixture
def my_logger():
    my_logger = Logger("logs.txt")
    return my_logger

# Logger
def test_logger_setup(my_logger):
    my_logger.setup()
    file = open(my_logger.log, 'r')
    assert file.readline() == "LOGGING\n"

@pytest.mark.parametrize("test_log", [
    {'method':"GET",
    'route':'/',
    'results': None},
    {'method':"POST",
    'route':'/',
    'results': "render_template('example.html')"}
])
def test_logger_log(my_logger, test_log):
    my_logger.setup()
    my_logger.log_change(test_log['method'], test_log['route'], test_log['results'])
    file = open(my_logger.log, 'r')
    line = file.readline()
    line = file.readline()
    line = file.readline()
    assert test_log['method'] in line
    assert test_log['route'] in line
    if(test_log['results'] is not None):
        assert str(test_log['results']) in line