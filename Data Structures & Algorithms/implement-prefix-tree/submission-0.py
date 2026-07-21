# Each node contains hashmap to store references to child nodes
# Child nodes represent characters

# Each node has boolean flag to indicate whether current node 
# marks end of a valid word

# Need to define TrieNode() class

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    # Start from root node
    # If character doesn't exist in children, create new TrieNode
    # Move to that child node
    # After full word is added, mark final node as end of valid word
    def insert(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.endOfWord = True
            
    # Start from root node
    # If character doesn't exist in children, return False
    # Move down the Trie
    # After processing all characters, if endOfWord is True,
    # return True bc the entire word exists
    def search(self, word: str) -> bool:
        node = self.root

        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.endOfWord

    # Start from root node
    # If characters in prefix are all in the Trie, return True
    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]

        return True
        