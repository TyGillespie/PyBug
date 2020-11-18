"""PyBug
A simple debugging library for Python.

Copyright (C) 2020, Ty Gillespie. All rights reserved.
MIT Licensed.

Todo: Add the option of toggling writing of the time of said event to all functions that write to the log.
"""

import traceback
import datetime


file = None


def initialize(
    file_name: str, overwrite: bool = True, log_startup: bool = True
) -> bool:
    """Initializes the log system.
    Parems:
            file_name: The log file name.
            overwrite (optional): Specifies if the text that was already in the log gets overwritten or not.
            log_startup (optional): If the message that the debugging system gets written to the log file.
    Returns:
            True if successful, False otherwise.
    """
    global file
    if file != None:
        return False
    if overwrite:
        file = open(file_name, "w")
    else:
        file = open(file_name, "a")
    if log_startup:
        file.write(f"{datetime.datetime.now()}\n")
        file.write("Logging system initialized.")
    file.flush()
    return True


def write_message(message: str) -> bool:
    """Writes a standard message to the log.
    Parems:
            message: The message to write.
    Returns:
            True on success, False otherwise.
    """
    global file
    if file == None:
        return False
    file.write(f"{datetime.datetime.now()}\n")
    file.write(f"Message: {message}\n")
    file.flush()
    return True


def write_error(message: str) -> bool:
    """Writes an error to the log file.
    Useful if you want to write an error that isn't an exception.
    Parems:
            message: The message to write.
    Returns:
            True upon success, False otherwise.
    """
    global file
    if file == None:
        return False
    file.write(f"{datetime.datetime.now()}\n")
    file.write(f"Error: {message}\n")
    file.flush()


def write_exception(message: str) -> bool:
    """Writes an Exception to the log file.
    Normally used in try/catch blocks.
    Parems:
            message: The message to write along with the Exception.
    Returns:
            True on success, False if it fails.
    """
    global file
    if file == None:
        return False
    file.write(f"{datetime.datetime.now()}\n")
    file.write(f"Exception: {message}\n----\n{traceback.format_exc()}----\n")
    file.flush()
    return True


def stop() -> bool:
    """Stops the logging system.
    Parems:
            None.
    Returns:
            True on success, False on fail.
    """
    global file
    if file == None:
        return False
    file.close()
    return True
