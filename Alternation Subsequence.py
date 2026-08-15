t = int(input())

while t > 0:
    n = int(input())
    arr = list(map(int, input().split()))

    total_sum = 0
    i = 0

    while i < n:
        j = i
        current_max = arr[i]

        while j < n and ((arr[j] > 0) == (arr[i] > 0)):
            current_max = max(current_max, arr[j])
            j += 1
        total_sum += current_max
        i = j

    print(total_sum)

    t -= 1
