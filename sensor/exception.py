import sys, os


def error_message_detial(error, error_detial:sys):
    _, _, exc_tb = error_detial.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred python script name[{0}] line number[{1}] error message [{2}] ".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message


class SensorException(Exception):

    def __init__(self, error_message, error_detial:sys):
        self.error_message = error_message_detial(
            error_message, error_detial = error_detial
        )

    def __str__(self):
        return self.error_message