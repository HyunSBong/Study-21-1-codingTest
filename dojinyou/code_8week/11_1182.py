# https://www.acmicpc.net/problem/1182

from itertools import combinations
from sys import stdin
input = stdin.readline

N, S = map(int, input().split())
array = list(map(int, input().split()))

cnt = 0
for i in range(1,N+1):
	for numbers in combinations(array, i):
		if sum(numbers) == S :cnt += 1
print(cnt)