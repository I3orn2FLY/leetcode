def wordBreak(s: str, wordDict) -> bool:
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s) + 1):
        for word in wordDict:
            if len(word) > i:
                continue

            if not dp[i - len(word)]:
                continue

            if word == s[i - len(word):i]:
                dp[i] = True
                break

    return dp[-1]


print(wordBreak(s="applepenapple", wordDict=["apple", "pen"]))
# wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"])
