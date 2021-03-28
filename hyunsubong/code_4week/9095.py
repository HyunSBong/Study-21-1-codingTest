# 1,2,3 더하기

n = int(input())
l = [int(input()) for _ in range(n)]
dp = [0,1,2,4]
# dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
for i in range(4, max(l)+1):
    next = dp[i-1] + dp[i-2] + dp[i-3]
    dp.append(next)

for i in l:
    print(dp[i])