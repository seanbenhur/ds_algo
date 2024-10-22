class TimeMap:

    def __init__(self):
        self.timestamp_dict = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timestamp_dict:
            self.timestamp_dict[key] = []
        self.timestamp_dict[key].append((value,timestamp))
    
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.timestamp_dict.get(key,[])

        if len(values) == 0:
            return res



        left, right = 0, len(values) - 1
        while left <= right:
            mid = (left+right)//2
            if values[mid][1] == timestamp:
                res = values[mid][0]
                return res
            elif values[mid][1] < timestamp:
                res = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return res


      