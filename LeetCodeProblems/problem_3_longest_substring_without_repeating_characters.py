def lengthOfLongestSubstring(s: str) -> int:

    max_len = 0
    subset = ""

    for i in s:
        if i not in subset:
            subset += i
        else:
            if len(subset) > max_len:
                max_len = len(subset)
            subset = subset[subset.index(i)+1:] + i

    if subset and (len(subset) > max_len):
        max_len = len(subset)

    return max_len


print(lengthOfLongestSubstring("dvdf"))     # 3
