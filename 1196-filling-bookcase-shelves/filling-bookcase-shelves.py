class Solution:
    def minHeightShelves(self, books, shelfWidth):
        n = len(books)
        f = [0] * (n + 1)
        for i in range(1, n + 1):
            w = books[i - 1][0]
            h = books[i - 1][1]
            f[i] = f[i - 1] + h
            for j in range(i - 1, 0, -1):
                w += books[j - 1][0]
                if w > shelfWidth:
                    break
                h = max(h, books[j - 1][1])
                f[i] = min(f[i], f[j - 1] + h)
        return f[n]
