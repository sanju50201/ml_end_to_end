import sys
import traceback
import re


class CustomException(Exception):
    def __init__(self, error_message):
        formatted_traceback = traceback.format_exc()
        self.error_message = self._error_message_detail(
            error_message, formatted_traceback)
        super().__init__(error_message)

    @staticmethod
    def _error_message_detail(error, formatted_traceback: str) -> str:
        # Using regular expression to extract filename and line number from the traceback
        match = re.search(r'File "(.+)", line (\d+)', formatted_traceback)
        if match:
            file_name, line_number = match.groups()
            error_message = (f"Error occurred in python script name [{file_name}] "
                             f"line number [{line_number}] error message[{str(error)}]")
            return error_message
        else:
            # Fallback message if parsing fails
            return f"Error message: {str(error)}"
