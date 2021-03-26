# https://www.acmicpc.net/problem/7490

import sys
input = sys.stdin.readline

def get_operator_list(array,n):
	global operators_list
	if len(array)==n:
		operators_list.append(array[:])
	else :
		array.append(' ')
		get_operator_list(array,n)
		array.pop()

		array.append('+')
		get_operator_list(array,n)
		array.pop()

		array.append('-')
		get_operator_list(array,n)
		array.pop()

for _ in range(int(input())):
	n = int(input())
	operators_list = []
	get_operator_list([],n-1)
	for operators in operators_list:
		string = ''
		for i in range(n-1):
			string += str(i+1)+operators[i]
		string += str(n)
		if eval(string.replace(' ','')) == 0 :
			print(string)
	print()