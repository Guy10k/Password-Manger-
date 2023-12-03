import csv
from database import *
from password_manager import *

def export_csv(row_list, file_path):
    print(file_path)
    file_path = f"{file_path}/data.csv"
    with open(file_path, 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(row_list)

def import_csv(file_path):
    tmp = file_path.split(".")
    prefix =tmp[len(tmp)-1]
    print(prefix[len(prefix)-1])
    if prefix == 'csv':
        with open(file_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                print(row)
                save_pass(row[0],row[2],row[3],row[4])
    else:
        raise UnSupportedFileFormat




