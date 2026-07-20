class Solution:
    def similarPairs(self, words: List[str]) -> int:
        output = []
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if set(words[j]) == set(words[i]):
                    output.append((i, j))
        return len(output)
