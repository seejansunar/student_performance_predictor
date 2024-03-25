import sys
from src.logger import logging

def error_message_detail(error, error_detail:sys):
    _,_,exec_tb = error_detail.exc_info()
    file_name   = exec_tb.tb_frame.f_code.co_filename
    line_number = exec_tb.tb_lineno
    error       = str(error)
    error_message = "Error occured in python script name {} line number {} error message {}".format(file_name, line_number, error)
    return error_message

class CustomException(Exception):
    def __init__(self, error, error_detail:sys):
        super().__init__(error)
        self.error = error_message_detail(error, error_detail=error_detail)

    def __str__(self):
        return self.error