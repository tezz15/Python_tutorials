if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    large = max(arr)
    count = 0
    for i in range(0,n):
        if arr[i]==large:
            count += 1
    for i in range(count):
        arr.remove(max(arr))
    
    print(max(arr))