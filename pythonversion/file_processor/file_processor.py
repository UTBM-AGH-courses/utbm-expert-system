import re
# Handle the file reading process
class FileProcessor:
    def __init__(self, file_path):
        self.__path_file = file_path
        self.__stream = open(file_path, "r")

    # Get the stream file (public)
    def get_stream(self):
        return self.__stream



