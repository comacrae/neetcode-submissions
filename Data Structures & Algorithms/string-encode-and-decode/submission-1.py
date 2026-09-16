class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        encoded_str:str = ""
        for word in strs:
            encoded_str += f"{len(word)}#{word}" # use hashtag for delim
        return encoded_str

        
    def decode(self, s: str) -> List[str]:
        print(f"encoded_input:{s}")
        if s == "":
            return []

        output: List[str] = []
        idx: int = 0
        word_len:str = ""
        word: str = ""
        while idx < len(s):

            while s[idx] != "#": # get the len of the word str -> int
                word_len += s[idx]
                idx +=1

            idx += 1 # now we are at the word
            print(idx)
            for i in range(0, int(word_len)): # get X chars
                word += s[idx]
                idx += 1
            print(word)
            output.append(word)

            word_len = ""
            word = ""
        return output




        
