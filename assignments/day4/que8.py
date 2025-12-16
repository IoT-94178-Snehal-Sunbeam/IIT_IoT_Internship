
data = ((10, 10, 10, 12),
        (30, 45, 56, 45),
        (81, 80, 39, 32),
        (1, 2, 3, 4))
def column_averages(tuples_data):
    num_rows = len(tuples_data)
    num_cols = len(tuples_data[0])
    
    averages = []
    for col in range(num_cols):
        col_sum = 0
        for row in range(num_rows):
            col_sum += tuples_data[row][col]
        averages.append(col_sum / num_rows)
    
    return averages
avg_values = column_averages(data)
print(avg_values)
