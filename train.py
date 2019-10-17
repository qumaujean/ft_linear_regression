from array import array
import csv
from utils import normalize_data, get_data_set

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
    learning_rate = 0.2
    data_len = len(data_x)
    x_cost = 0.0
    y_cost = 0.0
    for i in range(data_len):
        x_cost += (predict_price(data_x[i], teta0, teta1) - data_y[i])
        y_cost += (predict_price(data_x[i], teta0, teta1) - data_y[i]) * data_x[i]
    temp0 = teta0 - learning_rate * (x_cost / data_len)    
    temp1 = teta1 - learning_rate * (y_cost / data_len)
    return temp0, temp1

def update_tetas(teta0, teta1, current_cost, data_x,data_y):
    temp0, temp1 = derivate_terms(data_x, data_y, teta0, teta1)
    return temp0, temp1

## data_x correspond to input -- data_y correspond to observations

def main(teta0, teta1, iteration):
    data_x, data_y = get_data_set()
    normalized_data_x, normalized_data_y = normalize_data(data_x, data_y)
    cost = cost_function(normalized_data_x, normalized_data_y, teta0, teta1)
    teta_history = [[], []]
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

main(0, 0, 1000)