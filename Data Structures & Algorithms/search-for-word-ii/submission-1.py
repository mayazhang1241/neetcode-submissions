class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

    def addWord(self, word):
        node = self

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        node.endOfWord = True


class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        root = TrieNode()

        # Add all words to a trie
        for w in words:
            root.addWord(w)

        rows, cols = len(board), len(board[0])
        result, visit = set(), set()

        # DFS search
        # Base case: If cell is out of bounds, alr visited, or 
        # letter is not a child in Trie, return early
        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visit or board[r][c] not in node.children):
                return

            # Add cell to visited and move down to child node
            visit.add((r, c))
            node = node.children[board[r][c]]

            # Add character to word
            # If end of word is reached, add the word to result array
            word += board[r][c]
            if node.endOfWord:
                result.add(word)

            # Explore all four directions of the board
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            visit.remove((r, c))

        # Call dfs() from every cell on the board
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")

        return list(result)






