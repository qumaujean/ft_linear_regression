from array import array
import csv

def predict_price(value, teta0, teta1):
    return teta1 * value + teta0

## Minimize cost function return is finding right teta's for the given data set

def cost_function(data_x, data_y, teta0, teta1):
    data_len = len(data_x)
    cost = 0.0
    for i in range(data_len):
        cost += (predict_price(data_x[i], teta0, teta1) - data_y[i])**2
    return cost / (2 * data_len)

def derivate_terms(data_x, data_y, teta0, teta1):
    learning_rate = 0.25
    data_len = len(data_x)
    x_cost = 0.0
    y_cost = 0.0
    for i in range(data_len):
        x_cost += (predict_price(data_x[i], teta0, teta1) - data_y[i])
        y_cost += (predict_price(data_x[i], teta0, teta1) - data_y[i]) * data_x[i]
    temp0 = teta0 - learning_rate * (x_cost / data_len)    
    temp1 = teta1 - learning_rate * (y_cost / data_len)
    return temp0, temp1

def normalize_data(data_x, data_y):
    new_x_set = []
    new_y_set = []
    for i in range(len(data_x)):
        normalized_x_data = (data_x[i] - min(data_x)) / (max(data_x) - min(data_x))
        normalized_y_data = (data_y[i] - min(data_y)) / (max(data_y) - min(data_y))
        new_x_set.append(normalized_x_data)
        new_y_set.append(normalized_y_data)
    return new_x_set, new_y_set
        


def update_tetas(teta0, teta1, current_cost, data_x,data_y):
    temp0, temp1 = derivate_terms(data_x, data_y, teta0, teta1)
    return temp0, temp1

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

## data_x correspond to input -- data_y correspond to observations

def main(teta0, teta1, iteration):
    data_x, data_y = get_data_set()
    normalized_data_x, normalized_data_y = normalize_data(data_x, data_y)
    cost = cost_function(data_x, normalized_data_y, teta0, teta1)
    i = 0
    with open('results_file.csv', mode='w') as results_file:
        results = csv.writer(results_file, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
        print("Training model...")
        results.writerow(['Cost', ' teta0',' teta1'])
        while iteration != 0:
            cost = cost_function(normalized_data_x, normalized_data_y, teta0, teta1)
            teta0, teta1 = update_tetas(teta0, teta1, cost, normalized_data_x, normalized_data_y)
            if cost == 0:
                break
            i += 1
            iteration -= 1
            results.writerow([cost, teta0, teta1])
    print("Training complete.")

main(0, 0, 100)