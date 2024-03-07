#!/usr/bin/python3
"""pascals triangle"""
def pascal_triangle(n):
    """function to generate the pascal triangle"""
    triangle = []

    if n <= 0:
        return triangle

    for i in range(n):
        temp_list = []

        for j in range(i+1):
            if j == 0 or j == i:
                temp_list.append(1)
            else:
                temp_list.append(triangle[i-1][j-1] + triangle[i-1][j])

        triangle.append(temp_list)

    return triangle

# example usage
if __name__ == '__main__':
    n = int(input("Enter the number of rows for Pascal's triangle: "))
    result = pascal_triangle(n)
    for row in result:
        print(row)