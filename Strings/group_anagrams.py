from collections import defaultdict


def groupAnagrams(strs):
    ans = defaultdict(list)

    for str in strs:
        count = [0] * 26
        
        for char in str:
            count[ord(char) - ord('a')] += 1 
        ans[tuple(count)].append(str)

    return ans.values()



if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    result = groupAnagrams(strs)
    print(result)