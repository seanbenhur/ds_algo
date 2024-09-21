class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1_count = defaultdict(int)
        window_count = defaultdict(int)


        for char in s1:
            s1_count[char] += 1

        for char in range(len(s1)):
            window_count[s2[char]] += 1


        print("s1",s1_count)
        print("window",window_count)
        if s1_count == window_count:
            return True

        for i in range(len(s1),len(s2)):
            # add the count of the next char
            window_count[s2[i]] += 1
            
            # remove the oldest character from the window
            window_count[s2[i-len(s1)]] -= 1

            if window_count[s2[i-len(s1)]] == 0:
                del window_count[s2[i-len(s1)]]

            if s1_count == window_count:
                return True
        return False


