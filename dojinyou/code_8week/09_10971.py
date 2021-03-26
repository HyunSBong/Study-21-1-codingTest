# https://www.acmicpc.net/problem/10971

from sys import stdin, maxsize
input = stdin.readline

N = int(input().rstrip())
adj = [list(map(int,input().split())) for _ in range(N)]

min_value = maxsize


def dfs(i, visited, cur_value):
	global adj, min_value
	visited = visited[:]
	visited[i] = True
	if sum(visited) == len(visited) :
		if adj[i][0] :
			min_value = min(min_value, cur_value+adj[i][0])
		return
	for j, cost in enumerate(adj[i]):
		if not visited[j] and cost :
			if cur_value + cost < min_value:
				dfs(j, visited, cur_value+cost)
dfs(0,[False]*N, 0)
print(min_value)