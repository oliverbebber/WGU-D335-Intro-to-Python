# Define your function here.
def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    result = (miles_driven / miles_per_gallon) * dollars_per_gallon
    return result

if __name__ == '__main__':
    # Type your code here.
    miles_per_gallon = float(input())
    dollars_per_gallon = float(input())

    # call the function using 10, 50, and 400 miles
    cost_10 = driving_cost(miles_per_gallon, dollars_per_gallon, 10.0)
    cost_50 = driving_cost(miles_per_gallon, dollars_per_gallon, 50.0)
    cost_400 = driving_cost(miles_per_gallon, dollars_per_gallon, 400.0)

    # print each cost with two digits after the decimal point
    print(f'{cost_10:.2f}')
    print(f'{cost_50:.2f}')
    print(f'{cost_400:.2f}')
