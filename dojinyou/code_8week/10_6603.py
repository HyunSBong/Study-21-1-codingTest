# https://www.acmicpc.net/problem/6603

from itertools import combinations
from sys import stdin
input = stdin.readline

while True :
	input_list = list(map(int, input().split()))
	if input_list[0] == 0 :
		break
	k, S = input_list[0], input_list[1:]
	for numbers in combinations(S,6):
		for number in numbers:
			print(number, end=' ')
		print()
	print()