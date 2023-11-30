import csv
from database import *
from password_manager import *

def export_csv(row_list):
    with open('data.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(row_list)

def import_csv():

    with open('data.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            save_pass(row[0],row[1],row[2])

export_csv(fetch_to_csv())
# import_csv()