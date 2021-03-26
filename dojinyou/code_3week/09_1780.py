# https://www.acmicpc.net/problem/1780

import sys
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]
result = [0]*3

def checkPaper(x,y,n):
	if n == 1:
		return True
	value = matrix[x][y]
	for i in range(n):
		for j in range(n):
			if value != matrix[x+i][y+j]:
				return False
	return True

def divide(x,y,n):
	if checkPaper(x,y,n):
		result[matrix[x][y]+1] += 1
	else :
		for i in range(3):
			for j in range(3):
				divide(x+i*n//3,y+j*n//3, n//3)

divide(0,0,n)
[print(i) for i in result]