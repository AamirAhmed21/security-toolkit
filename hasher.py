class ToyHash:
    def djb2(self, text):
        hash = 5381
        mask = 0xFFFFFFFF
        for ch in text:
            hash = hash * 33
            hash = hash + ord(ch)
            hash = hash & mask
        return hash
if __name__ == "__main__":
    toyhash = ToyHash()
    print(toyhash.djb2("hi"))
    print(toyhash.djb2("hello"))
