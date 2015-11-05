import time
import copy

def coin_combinations(total_value, denominations):
    denominations = list(reversed(denominations))
    coin_counts = []
    for index in range(len(denominations)):
        coin_counts.append(0)

    coin_counts[-1] = total_value / denominations[-1]
    combinations = 0
    while coin_counts[0] < 200:

        combinations += 1
        for index in range(1, len(coin_counts)):
            if coin_counts[index] > 0:
                value = multiple_values_sum(denominations[:index], coin_counts[:index]) + denominations[index]
                for k in range(index):
                    coin_counts[k] = 0
                coin_counts[index] -= 1
                coin_counts[index - 1] = value / denominations[index - 1]
                if value % denominations[index - 1] > 0:
                    coin_counts[index - 2] = (value % denominations[index - 1]) / denominations[index - 2]
                break
    return combinations + 1


def multiple_values_sum(lista, listb):
    product_sum = 0
    for index in range(len(lista)):
        product_sum += lista[index] * listb[index]
    return product_sum

start = time.time()
print coin_combinations(200, [200, 100, 50, 20, 10, 5, 2, 1])
print time.time() - start
