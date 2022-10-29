#Program to find width of highest mountain.
def mountain(array):
    ans = 0
    i = 1
    while i < len(array) - 1:
        isPeak = array[i] > array[i-1] and array[i] > array[i+1]
        if isPeak:
            cnt = 1
            j = i

            # go backward
            while j > 0 and array[j-1] < array[j]:
                cnt += 1
                j -= 1

            # go forward
            j = i
            while j < len(array) - 1 and array[j] > array[j+1]:
                cnt += 1
                j += 1
            # breadth of mountain
            ans = max(cnt, ans)
            i = j
        else:
            i += 1

    return ans

Example:
array = [5, 6, 1, 2, 3, 4, 5, 4, 3, 2, 0, 1, 2, 3, -2, 4]
print(mountain(array))
