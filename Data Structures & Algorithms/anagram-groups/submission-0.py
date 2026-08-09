class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for slowo in strs:
            podpis = "".join(sorted(slowo))
            if podpis not in groups:
                groups[podpis] = []
            groups[podpis].append(slowo)
        return list(groups.values())
