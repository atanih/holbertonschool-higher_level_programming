[5:05 PM, 5/17/2026] AJTorres:     return new_string
[5:18 PM, 5/17/2026] AJTorres: #!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        print(" ".join(["{:d}".format(num) for num in row]))
