class Solution:
    def kthCharacter(self, k: int) -> str:
        initial_str=["a"]
        while len(initial_str)<k:
            print(len(initial_str),k)
            for char in initial_str.copy():
                print(char)
                if char=="z":
                    initial_str.append("a")
                else:
                    initial_str.append(chr(ord(char)+1))
        return initial_str[k-1]