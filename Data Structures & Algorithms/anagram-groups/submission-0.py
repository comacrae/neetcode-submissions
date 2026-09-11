class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups: List[List[str]] = []
        hashmap: dict[str,List[str]] = {}
        for s in strs:
            sorted_str = "".join(sorted(s))
            if sorted_str in hashmap:
                hashmap[sorted_str].append(s)
            else:
                hashmap[sorted_str] = [s]
        return [str_list for str_list in hashmap.values()]


        

        