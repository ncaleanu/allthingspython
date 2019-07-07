def diagonalDifference(arr):
    """
    @hr practising algorithms
    """
    sum1 = 0
    sum2 = 0
    for i in range(len(arr[0])):
        sum1 += arr[i][i]  # diagonal 1 sum
        sum2 += arr[i][n-1-i]
    return abs(sum1-sum2)

T = [[11, 12, 2], [15, 6, 10], [10, 8, 12]]

print(diagonalDifference(T))
