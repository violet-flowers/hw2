

starting_point_for_life = [['*' if row >=k or col >=k else 'O' for col in range(n)] for row in range(n)]
for row in starting_point_for_life:
    print(row)