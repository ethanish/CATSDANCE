import os 

class directory_crawler: 
    def __init__(self, init_path: str): 
        self._root_directory = init_path 
         
    def set_file_paths(self, return_flag:bool=False) -> list: 
        self._file_list = [] 
        # crawling through directory and subdirectories 
        for root, directories, files in os.walk(self._root_directory): 
            for filename in files: 
                filepath = os.path.join(root, filename)
                self._file_list.append(filepath) 
        
        if return_flag:
            return self._file_list

    def generate_file_paths(self) -> object: 
        # crawling through directory and subdirectories 
        for root, directories, files in os.walk(self._root_directory): 
            for filename in files: 
                filepath = os.path.join(root, filename)
                yield filepath

