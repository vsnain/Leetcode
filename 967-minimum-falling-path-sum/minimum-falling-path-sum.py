class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        n = len(A)
        
        for i in range(1,n):
            for j in range(n):
                x,y,z = j,max(0,j-1),min(j+1,n-1)
                A[i][j] += min(A[i-1][x],A[i-1][y],A[i-1][z])
        
        return min(A[-1])