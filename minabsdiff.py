def minimumAbsoluteDifference(n, arr):
    min_sum = abs(arr[0] - arr[1])
    if min_sum != 0 and len(arr) > 2:
        for x in range(n):
            for y in range(x+1,n):
                min_sum = min(abs(arr[x] - arr[y]),min_sum)
    return min_sum

if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    print minimumAbsoluteDifference(n, arr)
