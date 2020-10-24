import os

# Written by Tanmay Mishra.  See filepackager module for more information.


def copy_file(
    source: str, destination: str, byte_start: int = None, byte_end: int = None
):
    """
    Copies file content from source to destination with optional byte truncation.
    """
    try:
        with open(str(destination), "wb") as write_file:
            with open(str(source), "rb") as open_file:
                write_file.write(open_file.read()[byte_start:byte_end])

        return True

    except:
        return False


def file_to_bytes(file_name: str, byte_start: int = None, byte_end: int = None):
    """
    Reads a file and returns a string of bytes.
    """
    try:
        with open(file_name, "rb") as open_file:
            my_bytes = open_file.read()[byte_start:byte_end]
        return my_bytes

    except:
        return b""


def bytes_to_file(file_name: str, my_bytes: bytes):
    """
    Writes a string of bytes to file_name.
    """
    try:
        with open(file_name, "wb") as write_file:
            write_file.write(my_bytes)
        return True
    except:
        return False


def bytes_or_files_to_bytes(items: list = []):
    """
    Converts a list of bytes and filepaths to a string of bytes.
    Reads the file content, converting it to bytes and appending it in order.
    """
    bytes_return = b""

    for item in items:
        if type(item) is bytes:
            bytes_return += item
        if type(item) is str and os.path.isfile(item):
            bytes_return += file_to_bytes(item)

    return bytes_return


def bytes_or_files_to_file(file_name: str, items: list = []):
    """
    Takes a list of byte strings and filepaths, converting them all to bytes, and then writes it all to one file.
    """

    try:
        my_bytes = bytes_or_files_to_bytes(items)
        return bytes_to_file(file_name, my_bytes)
    except:
        try:
            os.remove(str(file_name))
        except:
            return False
        return False


def separate_file_name(file_name: str = ""):
    index_ext = 0
    len_file = len(file_name)

    for i in range(len_file):
        if file_name[(len_file - i) : len_file - i + 1] == ".":
            index_ext = len_file - i
            break

    if file_name[index_ext:] == file_name:
        return [file_name[index_ext:], file_name[0:index_ext]]
    else:
        return [file_name[0:index_ext], file_name[index_ext:]]
