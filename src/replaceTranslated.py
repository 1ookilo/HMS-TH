import os
import pandas as pd

root = os.path.dirname(os.path.realpath(__file__))
path_csv_translated = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'csv_translated')
path_csv_base = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'HMS_00', 'Content', 'Etc', 'Localization')

def pdread_csv_base(path):
    db = pd.read_csv(path, encoding='utf-8-sig')
    return db

def pdread_csv_translated(path):
    db = pd.read_csv(path)
    return db.dropna(subset=['Translated']).reset_index(drop=True)


def main():
    base_files = os.listdir(path_csv_base)
    for base_file in base_files:
        if base_file.endswith('.csv'):
            base_path = os.path.join(path_csv_base, base_file)
            translated_path = os.path.join(path_csv_translated, base_file)
            process_single_file(base_path, translated_path)

def process_single_file(base_path, translated_path):
    filtered_base_db = pdread_csv_base(base_path)
    filtered_translated_db = pdread_csv_translated(translated_path)

    for index, row in filtered_base_db.iterrows():
        key_value = row.iloc[0]
        matched_rows = filtered_translated_db[filtered_translated_db['key'] == key_value]
        if not matched_rows.empty:
            translated_row = matched_rows.iloc[0]
            translated_value = translated_row['Translated']
            filtered_base_db.at[index, 'col2'] = translated_value

    # Save the updated data back to the CSV file
    filtered_base_db.to_csv(base_path, index=False, encoding='utf-8-sig')

if __name__ == '__main__':
    main()