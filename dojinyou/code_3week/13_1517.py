# https://www.acmicpc.net/problem/1517

import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
swap = 0

def mergeSort(array, s, e):
	global swap
	if s + 1 < e :
		mid = (s+e)//2
		sortedLeftArray = mergeSort(array,s,mid)
		sortedRightArray= mergeSort(array,mid,e)
		i = 0
		j = 0
		newArray = [0]*(e-s)
		for k in range(e-s):
			if  i < mid-s and (j == e-mid or sortedLeftArray[i] <= sortedRightArray[j]):
				newArray[k] = sortedLeftArray[i]
				i += 1
			else :
				newArray[k] = sortedRightArray[j]
				if k < mid+j :
					swap += mid+j-k-s
				j += 1
	else :
		newArray = array[s:e]
	return newArray
mergeSort(array,0,n)
print(swap)