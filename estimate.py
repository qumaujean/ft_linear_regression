from array import array
import csv

def normalize_data(data_x, data_y):
    new_x_set = []
    new_y_set = []
    for i in range(len(data_x)):
        normalized_x_data = (data_x[i] - min(data_x)) / (max(data_x) - min(data_x))
        normalized_y_data = (data_y[i] - min(data_y)) / (max(data_y) - min(data_y))
        new_x_set.append(normalized_x_data)
        new_y_set.append(normalized_y_data)
    for i in range(len(data_x)):
        print(data_x[i], new_x_set[i])
    return new_x_set, new_y_set

def get_data_set():
    with open('data.csv') as csv_file:
        data_x = array('L', [])
        data_y = array('L', [])
        csv_reader = csv.reader(csv_file, delimiter=',')
        first_line = True
        for row in csv_reader:
            if first_line == False:
                data_x.append(int(row[0]))
                data_y.append(int(row[1]))
            else:
                first_line = False
    return data_x, data_y

def get_minimize_cost_tetas():
    cost = None
    with open('results_file.csv') as results_file:
        csv_reader = csv.reader(results_file, delimiter=',')
        first_line = True
        for row in csv_reader:
            if first_line == False:
                if (cost == None):
                    cost = row[0]
                    teta0 = row[1]
                    teta1 = row[2]
                else:
                    if abs(float(cost)) > abs(float(row[0])):
                        cost = row[0]
                        teta0 = row[1]
                        teta1 = row[2]
            else:
                first_line = False
    return teta0, teta1

def main(input):
    teta0, teta1 = get_minimize_cost_tetas()
    data_x, data_y = get_data_set()
    xmin = min(data_x)
    xmax = max(data_x)
    ymin = min(data_y)
    ymax = max(data_y)
    normalized_input = (float(input) - min(data_x)) / (max(data_x) - min(data_x))
    print(float(normalized_input))
    print("teta0 ",teta0)
    print("teta1 ", teta1)
    test1 = float(teta1) * float(normalized_input) + float(teta0)
    print("test1 => ", test1)
    test = ((test1 * (float(ymax) - float(ymin))) + (float)(ymin))
    print(test)
    
main(20000)