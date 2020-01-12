def wordBreak(s: str, wordDict) -> bool:
    L = len(s)
    space = [False] * L

    for i in range(L):
        for word in wordDict:
            wl = len(word)
            if i + 1 - wl < 0: continue
            if s[i + 1 - wl: i + 1] == word and (space[i - wl] or i == wl - 1):
                space[i] = True
                break

    return space[-1]


wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"])
