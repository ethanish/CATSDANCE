import gzip

from directory_crawler import directory_crawler

class file_loader(directory_crawler):
    total_sdf = -1
    file_name_list = []
    current_file_name = None
    file_cursor = -1
    current_contents = None
    contents_cursor = -1

    def __init__(self, init_path, file_format=".sdf"):
        #Parameter
        self._root_directory = init_path
        self._file_format = file_format
        #Init Function
        self.filter_file_format()

    def filter_file_format(self) -> None:
        full_file_list = self.set_file_paths(return_flag = True)
        # Generate Decorator for each file extension
        for file_name in full_file_list:
            if (self.is_file_format(file_name, self._file_format)):
                self.file_name_list.append(file_name)
            # Compression file
            if (self.is_file_format(file_name, self._file_format + ".gz")):
                self.file_name_list.append(file_name)
            # Archive file
            if (self.is_file_format(file_name, self._file_format + ".zip")):
                self.file_name_list.append(file_name)
        self.total_sdf = len(self.file_name_list)

    def is_file_format(self, file_name: str, file_format: str) -> bool:
        # TODO: Change to uppder case automatically
        # TODO: Create decoratro class for further wide implementation
        return True if file_name.upper().endswith(file_format.upper()) else False

    def get_next_file_cursor(self) -> object:
        self.file_cursor += 1
        self.load_sdf(self.file_name_list[self.file_cursor])

    def load_sdf(self, file_name: str) -> None:
        if (self.is_file_format(file_name, ".gz")):
            self.current_file_name = file_name
            self.current_contents = gzip.open(file_name, 'rb')
        else:
            self.current_file_name = file_name
            self.current_contents = open(file_name, "r")

    def get_sdf_item(self, num_of_mol:int = 1, decode_type:str = 'utf-8') -> str:
        contents_buffer = ""
        temp_read_line = None
        if self.current_contents is None:
            raise TypeError("SDF file is not loaded")

        while(self.current_file_name != None):
            byte_read_line = self.current_contents.readline()
            str_read_line = byte_read_line.decode(decode_type)
            self.contents_cursor += 1

            if not str_read_line:
                pass
            else:
                contents_buffer += str_read_line

            # After Last Line, Check Return Value ""
            # TODO: change this logic to check the number of line compare to full length of file.
            # if not str_read_line:
            #     break

            # For each molecular, mol file format return "$$$$"
            if str_read_line.startswith("$"):
                num_of_mol -= 1
            if num_of_mol == 0:
                break

        return contents_buffer
