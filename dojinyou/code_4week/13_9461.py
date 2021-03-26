# https://www.acmicpc.net/problem/9461

from sys import stdin
input = stdin.readline

def P(n):
    if n < 4 :
        return 1
    if n < 6 :
        return 2
    dp = [1]*(n+1)
    dp[4] = 2
    dp[5] = 2
    for i in range(6,n+1):
        dp[i] = dp[i-1]+dp[i-5]
    return dp[n]
n = int(input())
for i in range(n):
    print(P(int(input())))