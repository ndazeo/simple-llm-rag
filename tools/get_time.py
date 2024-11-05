import time
from langchain.tools import tool


@tool
def get_time():
    """Gets current time"""
    return time.ctime()