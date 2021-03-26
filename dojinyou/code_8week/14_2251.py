# https://www.acmicpc.net/problem/2251

from collections import deque
from sys import stdin
input = stdin.readline

A,B,C = map(int, input().split())
result = [0 for _ in range(201)]
visited = [[0]*201 for _ in range(201)]
q = deque([(0,0,C)])
is_first = True
while q:
	cur_A,cur_B,cur_C = q.popleft()
	if visited[cur_A][cur_B] :
		continue
	visited[cur_A][cur_B] = 1
	if cur_A == 0 :
		print(f'{cur_A=},{cur_B=},{cur_C=}')
		result[cur_C] = 1
	if cur_A != 0 :
		if cur_B != B :
			q.append()
		if cur_C != C :
			q.append(pour_water([cur_A,A],[cur_C,C],[cur_B,B]))
	
	if cur_B != 0 :
		if cur_A != A :
			q.append(pour_water([cur_B,B],[cur_A,A],[cur_C,C]))
		if cur_C != C :
			q.append(pour_water([cur_B,B],[cur_C,C],[cur_A,A]))

	if cur_C != 0 :
		if cur_A != A :
			q.append(pour_water([cur_C,C],[cur_A,A],[cur_B,B]))
		if cur_B != B :
			q.append(pour_water([cur_C,C],[cur_B,B],[cur_A,A]))
for i in range(201):
	if result[i]:
		print(i, end=' ')