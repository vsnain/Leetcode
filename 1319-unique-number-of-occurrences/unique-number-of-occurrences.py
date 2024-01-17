class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = collections.Counter(arr)
        v = c.values()
        
        s = set()
        for i in v:
            if i in s:
                return False
            else:
                s.add(i)
        return True