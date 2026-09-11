class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """Naive solution
        groups: List[List[str]] = []
        hashmap: dict[str,List[str]] = {}
        for s in strs:
            sorted_str = "".join(sorted(s))
            if sorted_str in hashmap:
                hashmap[sorted_str].append(s)
            else:
                hashmap[sorted_str] = [s]
        return [str_list for str_list in hashmap.values()]
        """
        groups: List[List[str]] = []
        hashmap: dict[tuple[int], list[str]] = {}
        base = ord("a")
        for s in strs:
            strarr = [0] * 26
            for ch in s:
                strarr[ord(ch) - base] += 1

            strtuple = tuple(strarr)
            if strtuple in hashmap:
                hashmap[strtuple].append(s)
            else:
                hashmap[strtuple] = [s]
        return list(hashmap.values())

        

        