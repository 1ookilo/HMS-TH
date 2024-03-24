import os
import csv

root = os.path.dirname(os.path.realpath(__file__))
path_csv_translated = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'csv_translated')

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        data = f.readlines()
        cleaned_data = [line.replace('\ufeff', '') for line in data]
        cleaned_data = [line.replace('key,Source,Translated\n', '') for line in data]
    # Insert the new line at the beginning
    new_line = "key,Source,Translated\n"
    cleaned_data.insert(0, new_line)

    return cleaned_data

def write_file(file_path, data):
    with open(file_path, 'w', encoding='utf8') as f:
        f.writelines(data)

def process_files_in_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            file_path = os.path.join(directory, filename)
            cleaned_data = read_file(file_path)
            write_file(file_path, cleaned_data)

def main():
    process_files_in_directory(path_csv_translated)

if __name__ == '__main__':
    main()
