# 파도반 수열

t = int(input())
dp = [1,1,1,2,2]

for _ in range(96):
    dp.append(0)
for _ in range(t) :
    n = int(input())
    for i in range(5,n+1):
        dp[i] = dp[i-1] + dp[i-5]
    print(dp[n-1])