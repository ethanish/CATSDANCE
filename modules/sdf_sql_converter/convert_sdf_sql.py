from file_loader import file_loader

class convert_sdf_sql(file_loader):
    def __init__(self, init_path, file_format=".sdf"):
        #Parameter
        self._root_directory = init_path
        self._file_format = file_format
        #Init Function
        self.filter_file_format()
        self.get_next_file_cursor()
        self.current_mol_content = self.get_sdf_item()

    def create_sdf_sql(self):
        # create as pandas df 
        # pandas df to sql

        pass

    def generate_sdf_sql(self):
        # Create to yield for generate function

        pass

    def save_as(self, type=".sql"):
        # Type: .sql, .txt, ...

        pass


