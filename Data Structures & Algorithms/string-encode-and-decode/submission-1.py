class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for char in strs:
            encoded_str += str(len(char)) + "#" + char
        return encoded_str

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded_str = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            num = int(s[i:j])
            decoded_str.append(s[j+1:j+num+1])
            i = j + 1 + num
        return decoded_str
                
