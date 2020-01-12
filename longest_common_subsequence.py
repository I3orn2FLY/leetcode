def longestCommonSubsequence(text1: str, text2: str) -> int:
    l1 = len(text1)
    l2 = len(text2)

    if l1 == 0 or l2 == 0:
        return 0

    LCS = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]
    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            if text1[i - 1] == text2[j - 1]:
                LCS[i][j] = 1 + LCS[i - 1][j - 1]
            else:
                LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])


    return LCS[l1][l2]


longestCommonSubsequence("pmjghexybyrgzczy", "hafcdqbgncrcbihkd")
