from array import array

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

def update_tetas(teta0, teta1, current_cost, data_x,data_y):
    temp0, temp1 = derivate_terms(data_x, data_y, teta0, teta1)
    return temp0, temp1

def main(data_x, data_y, teta0, teta1):
    cost = cost_function(data_x, data_y, teta0, teta1)
    i = 0
    while cost != 0:
        cost = cost_function(data_x, data_y, teta0, teta1)
        teta0, teta1 = update_tetas(teta0, teta1, cost, data_x, data_y)
        if cost < 0.0001:
            break
        i += 1
        print(i, ". Training... Actual cost is ", cost, "\n")
    print(i, teta0, teta1)



# data_x = array('l', [240000,
# 139800,
# 150500,
# 185530,
# 176000,
# 114800,
# 166800,
# 89000,
# 144500,
# 84000,
# 82029,
# 63060,
# 74000,
# 97500,
# 67000,
# 76025,
# 48235,
# 93000,
# 60949,
# 65674,
# 54000,
# 68500,
# 22899,
# 61789]
# )

# data_y = array('l', [3650,
# 3800,
# 4400,
# 4450,
# 5250,
# 5350,
# 5800,
# 5990,
# 5999,
# 6200,
# 6390,
# 6390,
# 6600,
# 6800,
# 6800,
# 6900,
# 6900,
# 6990,
# 7490,
# 7555,
# 7990,
# 7990,
# 7990,
# 8290]
# )

# train(data_x, data_y, -0.3, -0.0014, 0.1, 100)

data_x = array('l', [1, 2, 3])

data_y = array('l', [1, 2, 3])

main(data_x, data_y, 0, 1)