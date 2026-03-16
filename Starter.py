import time

def lcs_recursive(seq1, seq2):

    if len(seq1) == 0 or len(seq2) == 0:
        return 0

    if seq1[-1] == seq2[-1]:
        return 1 + lcs_recursive(seq1[:-1], seq2[:-1])

    return max(
        lcs_recursive(seq1[:-1], seq2),
        lcs_recursive(seq1, seq2[:-1])
    )

def lcs_memoization(seq1, seq2):

    memo = {}

    def helper(i, j):

        if i == 0 or j == 0:
            return 0

        if (i, j) in memo:
            return memo[(i, j)]

        if seq1[i-1] == seq2[j-1]:
            memo[(i, j)] = 1 + helper(i-1, j-1)
        else:
            memo[(i, j)] = max(
                helper(i-1, j),
                helper(i, j-1)
            )

        return memo[(i, j)]

    return helper(len(seq1), len(seq2))


def lcs_tabulation(seq1, seq2):

    n = len(seq1)
    m = len(seq2)

    dp = [[0]*(m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):

            if seq1[i-1] == seq2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]

            else:
                dp[i][j] = max(
                    dp[i-1][j],
                    dp[i][j-1]
                )

    return dp[n][m]


def test_small_cases():

    seq1 = "AGGTAB"
    seq2 = "GXTXAYB"

    print("Sequence 1:", seq1)
    print("Sequence 2:", seq2)

    print("\nRecursive:", lcs_recursive(seq1, seq2))
    print("Memoization:", lcs_memoization(seq1, seq2))
    print("Tabulation:", lcs_tabulation(seq1, seq2))
  
def compare_all_approaches():

    seq1 = "AGGTAB" * 10
    seq2 = "GXTXAYB" * 10

    start = time.time()
    lcs_memoization(seq1, seq2)
    print("Memoization time:", time.time() - start)

    start = time.time()
    lcs_tabulation(seq1, seq2)
    print("Tabulation time:", time.time() - start)

if __name__ == "__main__":

    test_small_cases()

    compare_all_approaches()
