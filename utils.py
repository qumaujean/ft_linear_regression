from array import array
import csv

def normalize_data(data_x, data_y):
    new_x_set = array('f', [])
    new_y_set = array('f', [])
    for i in range(len(data_x)):
        normalized_x_data = (data_x[i] - min(data_x)) / (max(data_x) - min(data_x))
        normalized_y_data = (data_y[i] - min(data_y)) / (max(data_y) - min(data_y))
        new_x_set.append(normalized_x_data)
        new_y_set.append(normalized_y_data)
    return new_x_set, new_y_set

def get_data_set():
    with open('data.csv') as csv_file:
        data_x = array('f', [])
        data_y = array('f', [])
        csv_reader = csv.reader(csv_file, delimiter=',')
        first_line = True
        for row in csv_reader:
            if first_line == False:
                data_x.append(float(row[0]))
                data_y.append(float(row[1]))
            else:
                first_line = False
    return data_x, data_y