def less_equal_than(x, y):
    return x <= y

def greater_than(x, y):
    return x > y

def total_hours(data):
    total_h = 0

    for task in data:
        total_h+=task['hora_t']
    return total_h