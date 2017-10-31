import csv
import sys
import os

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

#def read_data(numeric_col, data, nominal_dictionary, cols_size):
def read_data():
    for row in content:
        # replacing empty data with '?'
        row_content = []
        for index, cell in enumerate(row):
            # ignoring the weight column, index: 5
            if index == 5:
                row_content.append('?')
            elif cell == '':
                row_content.append('?')
            else:
                if index in diag_col:
                    if isfloat(cell):
                        cell = int(float(cell))
                        if cell == 250:
                            cell = "Diabetes"
                        elif cell in range(390, 460) or cell == 785:
                            cell = "Circulatory"
                        elif cell in range(460, 520) or cell == 786:
                            cell = "Respiratory"
                        elif cell in range(520, 580) or cell == 787:
                            cell = "Digestive"
                        elif cell in range(800, 1000):
                            cell = "Injury"
                        elif cell in range(710, 740):
                            cell = "Musculoskeletal"
                        elif cell in range(580, 630) or cell == 788:
                            cell = "Genitourinary"
                        elif cell in range(140, 239):
                            cell = "Neoplasms"
                        else:
                            cell = "Other"
                    else:
                        cell = "Other"
                row_content.append(cell)
            
#         row = ['?' if cell == '' else cell for cell in row]
        # adding the row to a data list
        data.append(row_content)
        for index, cell in enumerate(row):
            if index not in numeric_col and cell != '?':
                if index not in nominal_dictionary.keys():
                    nominal_dictionary[index] = set()
                if index in diag_col:
                    if isfloat(cell):
                        cell = int(float(cell))
                        if cell == 250:
                            cell = "Diabetes"
                        elif cell in range(390, 460) or cell == 785:
                            cell = "Circulatory"
                        elif cell in range(460, 520) or cell == 786:
                            cell = "Respiratory"
                        elif cell in range(520, 580) or cell == 787:
                            cell = "Digestive"
                        elif cell in range(800, 1000):
                            cell = "Injury"
                        elif cell in range(710, 740):
                            cell = "Musculoskeletal"
                        elif cell in range(580, 630) or cell == 788:
                            cell = "Genitourinary"
                        elif cell in range(140, 239):
                            cell = "Neoplasms"
                        else:
                            cell = "Other"
                    else:
                        cell = "Other"
                nominal_dictionary[index].add(cell)
                
def write_data_to_console():
    # Printing @relation
    print('@relation', name)
    # Printing @attributes
    for col in range(len(header)):
        if col in numeric_col:
            print('@attribute', header[col], 'numeric')
        else:
            print('@attribute', header[col], '{' + ','.join(sorted(nominal_dictionary[col])) + '}')
    # Printing @data
    print('@data')
    for row in data:
        print(','.join(row))

if len(sys.argv) != 2:
    print('Usage: csv2arff.py <path to a csv file>')
    sys.exit(0)
    
file_path = sys.argv[1]

try:
    with open(file_path, 'r') as csvfile:
        content = csv.reader(csvfile, delimiter = ',')
        file_name = os.path.basename(file_path)

        # name of the csv file.
        name = os.path.splitext(file_name)[0]
        # Numeric columns: 
        # 0 - Encounter ID, 1 - Patient number, 5 - Weight, 9 - Time in hospital, 12 - Number of lab procedures
        # 13 - Number of procedures, 14 - Number of medications, 15 - Number of outpatient visits
        # 16 - Number of emergency visits, 17 - Number of inpatient visits, 21 - Number of diagnoses
        numeric_col = {0, 1, 5, 9, 12, 13, 14, 15, 16, 17, 21}
        diag_col = {18, 19, 20}
        data = []
        nominal_dictionary = {}
        header = next(content);
        cols_size = len(header)
        
        read_data()
        write_data_to_console()
                        
except IOError:
    print('File not found')
    sys.exit(0)
    





