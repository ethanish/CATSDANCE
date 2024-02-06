from convert_sdf_sql import convert_sdf_sql

def test_code(): 
    sdf_full_path = '/mnt/d/DATABASES/PubChem/Compound/FULL/' 
    # calling function to get all file paths in the directory
    iidb_obj = convert_sdf_sql(sdf_full_path, '.sdf')
    
    # print(iidb_obj.current_mol_content)

    test_line = iidb_obj.current_mol_content

    splited_mol_file = test_line.split("\n")
    # Removed index & last end motif $$$$
    current_contents = "\n".join(splited_mol_file[1:-2])
    # Split again with appendix information indicator ">"
    splited_current_contents = current_contents.split(">")

    current_mol_dict = {}
    current_mol_dict['index'] = splited_mol_file[0]
    current_mol_dict['mol'] = splited_current_contents[0]

    print(current_mol_dict)

if __name__ == "__main__": 
    test_code() 
