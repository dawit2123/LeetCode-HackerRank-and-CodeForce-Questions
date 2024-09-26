class Codec:
    def __init__(self):
        self.encode_book={}
        self.decode_book={}
        self.base="https://tiny.url/"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.encode_book:
            shortUrl= self.base+str(len(self.encode_book)+1)
            self.encode_book[longUrl]=shortUrl    
            self.decode_book[shortUrl]=longUrl    
        return self.encode_book[longUrl]
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.decode_book[shortUrl]        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))