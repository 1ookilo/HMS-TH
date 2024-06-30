import os
import pandas as pd

root =  os.path.join(os.path.dirname(os.path.dirname(__file__)), 'csv')
path_inputen = os.path.join(root, 'input', 'EN')
path_inputchs = os.path.join(root, 'input', 'CHS')
path_output = os.path.join(root, 'clean')

def pdread_csv(path, path_output, header_rows):
    db = pd.read_csv(path, header=0, skiprows=header_rows)
    newdb = pd.DataFrame({
        "key": db["id"],
        "original": db["text"],
        "translation": ""
    })
    newdb.to_csv(path_output, index=False)

def process_edit_file(file, lang, header_rows):
    filename = os.path.basename(file)
    output_path = os.path.join(path_output, filename)
    pdread_csv(file, output_path, header_rows)

def main():
    process_files(path_inputen, 'en', 2)
    process_files(path_inputchs, 'chs', 3)

def process_files(input_path, lang, header_rows):
    files = os.listdir(input_path)
    for file in files:
        if file.endswith('.csv'):
            fileinput = os.path.join(input_path, file)
            process_edit_file(fileinput, lang, header_rows)

if __name__ == '__main__':
    main()