import datetime
import os

from requests import Response


class Logger:
    """Methods for logging API requests and responses"""

    # Get the project root directory
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Set the directory for log files
    logs_directory = os.path.join(project_root, "logs")

    # Create a unique log file name using the current date and time
    file_name = os.path.join(logs_directory, "log_" + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".log")

    @classmethod
    def write_log_to_file(cls, data: str):
        """Write log data to the log file"""

        # Create the logs directory if it does not exist
        os.makedirs(cls.logs_directory, exist_ok=True)

        # Open the log file and append new data
        with open(cls.file_name, "a", encoding="utf-8") as logger_file:
            logger_file.write(data)

    @classmethod
    def add_request(cls, url: str, method: str):
        """Add information about an API request to the log"""

        # Get the current test name from pytest environment variables
        test_name = os.environ.get("PYTEST_CURRENT_TEST")

        data_to_add = f"\n-----\n"
        data_to_add += f"Test: {test_name}\n"
        data_to_add += f"Time: {datetime.datetime.now()}\n"
        data_to_add += f"Request method: {method}\n"
        data_to_add += f"Request URL: {url}\n"
        data_to_add += "\n"

        cls.write_log_to_file(data_to_add)

    @classmethod
    def add_response(cls, result: Response):
        """Add information about an API response to the log"""

        # Convert response cookies and headers to dictionaries
        cookies_as_dict = dict(result.cookies)
        headers_as_dict = dict(result.headers)

        data_to_add = f"Response code: {result.status_code}\n"
        data_to_add += f"Response text: {result.text}\n"
        data_to_add += f"Response headers: {headers_as_dict}\n"
        data_to_add += f"Response cookies: {cookies_as_dict}\n"
        data_to_add += f"\n-----\n"

        cls.write_log_to_file(data_to_add)