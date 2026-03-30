class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for char in strs:
            encoded_str += str(len(char)) + "#" + char
        return encoded_str

    def decode(self, s: str) -> List[str]:
        count = ""
        i = 0
        decoded_str = []
        while i < len(s):
            if s[i].isnumeric():
                count += s[i]
                i += 1
            elif s[i] == '#':
                num = int(count)
                decoded_str.append(s[i+1:i+num+1])
                i += num + 1
                count = ""
        return decoded_str
                
