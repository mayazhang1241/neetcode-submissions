class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        node.endOfWord = True

    # j represents beginning of word

    # Use DFS search to recursively search for other possible words
    # Check each character in the word
    # if character is not a ".", we look for that exact character in
    # node's children
    # if character is a ".", we try every child node recursively 
    # to see if any path can match the word

    # If character is missing at any point in the trie, return False

    def search(self, word: str) -> bool:
        
        def dfs(j, root):
            node = root

            for i in range(j, len(word)):
                char = word[i]

                if char == ".":
                    for child in node.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if char not in node.children: 
                        return False

                    node = node.children[char] 
            
            return node.endOfWord

        return dfs(0, self.root)








