# Problem: Insertion Sort - https://www.hackerrank.com/challenges/insertionsort1/problem

def insertionSort1(n, arr):
    for i in range(n-1, 0, -1):
        temp=arr[i]
        j=i-1
        while j>=0 and temp<arr[j]:
            arr[j+1]=arr[j]
            print(*arr)
            j-=1
        arr[j+1]=temp
    print(*arr)