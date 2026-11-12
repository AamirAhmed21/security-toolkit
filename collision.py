import string
from hasher import ToyHash

class collisionFinder:
    def __init__(self, alphabet=string.ascii_letters) -> None:
        self.toy = ToyHash()
        self.alphabet = alphabet
    def find_two_letter(self):
        seen = {}
        collision = []
        for first in self.alphabet:
            for second in self.alphabet:
                letter = first + second
                hash = self.toy.djb2(letter)
                if hash in seen:
                    collision.append((seen[hash],hash,letter))
                seen[hash] = letter
        return collision
if __name__ == "__main__":
    finder = collisionFinder()
    result = finder.find_two_letter()
    for text,h,text2 in result[:10]:
        print(f"{text} and {text2} → {h}")
