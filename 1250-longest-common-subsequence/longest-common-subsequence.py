class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        a = len(text1)
        b = len(text2)
        dp = [[0]*(b+1) for _ in range(a+1)]
        # print(dp)
        for i in range(1,a+1):
            for j in range(1,b+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
                
                
                # print((i,j), dp)
        
        return dp[-1][-1]