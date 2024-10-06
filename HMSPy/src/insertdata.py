#####Draft version
import os
import pandas as pd
root =  os.path.join(os.path.dirname(os.path.dirname(__file__)), 'csv')
path_input = os.path.join(root, 'clean')
path_out = os.path.join(root, 'output')
def merge_and_save(input_folder, output_folder):
    files = os.listdir(input_folder)

    for file in files:
        if file.endswith('_zh-Hans.csv'):
            file_en = os.path.join(input_folder, file.replace('_zh-Hans', '_en'))
            if os.path.exists(file_en):
                df_zh = pd.read_csv(os.path.join(input_folder, file), skiprows=0, encoding='utf-8-sig')
                df_en = pd.read_csv(file_en, skiprows=0, encoding='utf-8-sig')

                # Merge ข้อมูลจากไฟล์ _zh-Hans กับไฟล์ _en โดยใช้คอลัมน์ original_chs และ original_en
                merged_df = pd.merge(df_en, df_zh[['key', 'original']], on='key', suffixes=('_en', '_chs'))

                # เปลี่ยนชื่อคอลัมน์ original_chs เป็น context
                merged_df = merged_df.rename(columns={'original_chs': 'context'})

                # บันทึกข้อมูลลงไฟล์ใหม่ที่ลงท้ายด้วย _edit
                output_file = os.path.join(output_folder, file.replace('_zh-Hans', '_en'))
                merged_df.to_csv(output_file, index=False)

def main():
    merge_and_save(path_input, path_out)

if __name__ == '__main__':
    main()