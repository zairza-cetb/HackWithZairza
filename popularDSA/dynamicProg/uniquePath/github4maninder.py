# This is the solution for the unique path problem using Dynamic Programming approach
def uniquePaths(m: int, n: int) -> int:
    # Create a 2D list initialized to 0
    dp = [[0] * n for _ in range(m)]
    
    # Fill the first row and the first column with 1
    for i in range(m):
        dp[i][0] = 1  # Only one way to reach any cell in the first column
    for j in range(n):
        dp[0][j] = 1  # Only one way to reach any cell in the first row

    # Fill the dp table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    
    # The number of unique paths to reach the bottom-right corner
    return dp[m - 1][n - 1]

# Example usage
print(uniquePaths(3, 7))  # Output: 28
print(uniquePaths(3, 2))  # Output: 3
