# https://www.acmicpc.net/problem/1074

import sys
input = sys.stdin.readline

N,r,c = map(int, input().split())
cnt = 0
length = 2**N
target_x,target_y = 0,0
for i in range(N+1):
	if target_y+(length//2) <= r :
		cnt += length**2//2
		target_y += length//2
	if target_x+(length//2) <= c :
		cnt += length**2//4
		target_x += length//2
	length //= 2
print(cnt)

# 메모리 초과
# board = [[0]*(2**N) for _ in range(2**N)]
# cnt = 0
# def search_Z(x,y,size):
# 	global cnt
# 	global board
# 	if size == 1 :
# 		for i in range(2):
# 			for j in range(2):
# 				board[x+i][y+j] = cnt
# 				cnt += 1
# 	else :
# 		half = 2**(size-1)
# 		for i in range(2):
# 			for j in range(2):
# 				search_Z(x+i*half, y+j*half,size-1)
# search_Z(0,0,N)
# print(board[r][c])