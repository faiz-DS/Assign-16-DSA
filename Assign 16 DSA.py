def max_absolute_difference(arr):
    n = len(arr)
    left_smaller = [0] * n
    right_smaller = [0] * n
    stack = []

    # Populate left_smaller array
    for i in range(n):
        while stack and arr[i] <= arr[stack[-1]]:
            stack.pop()

        left_smaller[i] = arr[stack[-1]] if stack else 0
        stack.append(i)

    stack.clear()

    # Populate right_smaller array
    for i in range(n - 1, -1, -1):
        while stack and arr[i] <= arr[stack[-1]]:
            stack.pop()

        right_smaller[i] = arr[stack[-1]] if stack else 0
        stack.append(i)

    # Calculate the maximum absolute difference
    max_diff = max(abs(left_smaller[i] - right_smaller[i]) for i in range(n))

    return max_diff

# Test cases
arr1 = [2, 1, 8]
arr2 = [2, 4, 8, 7, 7, 9, 3]
arr3 = [5, 1, 9, 2, 5, 1, 7]

print(max_absolute_difference(arr1))  # Output: 1
print(max_absolute_difference(arr2))  # Output: 4
print(max_absolute_difference(arr3))  # Output: 1
