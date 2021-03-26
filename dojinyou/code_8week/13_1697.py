# https://www.acmicpc.net/problem/1697

from collections import deque
from sys import stdin
input = stdin.readline

def BFS(start, target):
	visited = [False]*(100001)
	visited[start] = True
	q = deque([(start,0)])
	while q :
		cur, cnt = q.popleft()
		if cur == target :
			return cnt
		next_curs = [cur-1,cur+1,cur*2]
		for next_cur in next_curs:
			if 0 <= next_cur <= 100000 and not visited[next_cur]:
				q.append([next_cur, cnt+1])
				visited[next_cur] = True
N, K = map(int, input().split())
if N < K :
	print(BFS(N,K))
elif N > K :
	print(N-K)
else :
	print(0)