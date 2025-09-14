class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        '''res = {}

        for s in strs:
            key = tuple(sorted(s))
            if key in res.keys():
                res[key].append(s)
            else:
                res[key]=[s]
        return list(res.values())'''
        
        res = defaultdict(list)

        for s in strs:
            sortedword = ''.join(sorted(s))
            res[sortedword].append(s)

        return list(res.values())
            