class Node():
    def __init__(self, key, parent):
        self.key = key
        self.parent = parent


class Trie():
    def __init__(self, parent=None, key=None):
        self.parent = parent
        self.key = key
        self.value = {}
    
    def insert(self, word: str) -> None:
        if word == '':
            self.value['.'] = True
        if word:
            letter = word[0]

            if not self.value.get(letter):
                predecessor = Trie(self, letter)
                self.value[letter] = predecessor
            else:
                predecessor = self.value[letter]        
            predecessor.insert(word[1:])

    def search(self, word: str) -> bool:
        trie = self
        try:
            for letter in word:
                trie = trie.value[letter]
        except KeyError:
            return False
        return trie.value.get('.', False)
    
    def startsWith(self, prefix: str) -> bool:
        trie = self
        try:
            for letter in prefix:
                trie = trie.value[letter]
        except KeyError:
            return False
        return True


if __name__ == "__main__":
    tr = Trie()
    tr.insert('Addiction')
    tr.insert('Amine')
    tr.insert('Ad')
    print(tr.value['A'].value['d'].value)
    print(tr.startsWith('Ac'))
    print(tr.startsWith('Ad'))
    print(tr.search('Addict'))