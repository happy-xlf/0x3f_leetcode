class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict={}
        for it in strs:
            key=tuple(sorted(it))
            print(key)
            print(dict.get(key,[])+[it])
            dict[key]=dict.get(key,[])+[it]
        return list(dict.values())
    




if __name__ == '__main__':
    solution = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(solution.groupAnagrams(strs))





