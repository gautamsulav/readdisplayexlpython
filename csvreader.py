import csv
import openpyxl
#import traceback


#function to read and display Excel file
def read_display_csv(filename):
    try:
        #For .xlsx file format
        if (".xlsx" in filename):
            wb = openpyxl.load_workbook(filename)
            ws = wb.active

            for row in ws.iter_rows(values_only=True):
                print(row)
        
        #For .csv file format
        elif(".csv in filename"):
            with open(filename) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                for row in csv_reader:
                    print(','.join(row))

        else:
            print("Sorry File type not Supported");

    except FileNotFoundError:
        print("File Does Not exists")

    except Exception as e:
        #print(traceback.format_exc())
        print(e)


#sample tests with different file
read_display_csv('test.xlsx')
print('--------------')
read_display_csv('cities.csv')
print('--------------')
read_display_csv('xyz.xlsx')