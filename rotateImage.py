# You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).
# Try to use O(1) memory.
# Example:
#
# a = [[1, 2, 3]
#      [4, 5, 6],
#      [7, 8, 9]]
# the output should be
#
# solution(a) =
# [[7, 4, 1],
#  [8, 5, 2],
#  [9, 6, 3]]
#
# Solution is O(1) memory complexity and O(n**2) time complexity

def solution(a):

    min = -1
    length = len(a)
    max = length
    next = 0
    rotated = True

    while rotated:
        min += 1
        max -= 1
        rotationsRemaining = length - 1

        if min == max or max < min:
            break

        while rotationsRemaining > 0:

            i = min
            j = min
            prev = a[min][min]
            swapsRemaining = (length-1) * 4

            while swapsRemaining > 0:

                if j < min:
                    j = min

                # Move the top row east
                if i == min and j < max:

                    next = a[i][j+1]
                    a[i][j+1] = prev
                    prev = next
                    j += 1

                # Move the right column sout
                elif j == max and i < max:

                    next = a[i+1][j]
                    a[i+1][j] = prev
                    prev = next
                    i += 1

                # Move the bottom row west
                elif i == max and j > min:

                    next = a[i][j-1]
                    a[i][j-1] = prev
                    prev = next
                    j -= 1

                # Move the left column north
                elif j == min and i >= min:

                    next = a[i-1][j]
                    a[i-1][j] = prev
                    prev = next
                    i -= 1

                swapsRemaining -= 1

            rotationsRemaining -= 1

        length -= 2

    return a


arr3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
arr3 = solution(arr3)
for row in arr3:
    print(row)

arr4 = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]]
arr4 = solution(arr4)
print()
for row in arr4:
    print(row)

arr10 = [[40, 12, 15, 37, 33, 11, 45, 13, 25, 3],
         [37, 35, 15, 43, 23, 12, 22, 29, 46, 43],
         [44, 19, 15, 12, 30, 2, 45, 7, 47, 6],
         [48, 4, 40, 10, 16, 22, 18, 36, 27, 48],
         [45, 17, 36, 28, 47, 46, 8, 4, 17, 3],
         [14, 9, 33, 1, 6, 31, 7, 38, 25, 17],
         [31, 9, 17, 11, 29, 42, 38, 10, 48, 6],
         [12, 13, 42, 3, 47, 24, 28, 22, 3, 47],
         [38, 23, 26, 3, 23, 27, 14, 40, 15, 22],
         [8, 46, 20, 21, 35, 4, 36, 18, 32, 3]]
arr10 = solution(arr10)
print()
for row in arr10:
    print(row)
