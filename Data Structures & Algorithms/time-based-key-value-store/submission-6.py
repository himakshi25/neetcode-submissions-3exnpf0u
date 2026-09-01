import bisect
class TimeMap:

    def __init__(self):
        self.d = defaultdict(dict)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key]["set"]=[]
        self.d[key][timestamp] = value
        self.d[key]["set"].append(timestamp)
        #print(self.d)
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.d:
            key_set=list(self.d[key]["set"])
            #print(key_set)
            if timestamp in key_set:
                return self.d[key][timestamp]
            else:
                idx = bisect.bisect_left(key_set, timestamp)
                #result = lst[idx - 1] if idx > 0 else None
                if idx>0:
                    return self.d[key][key_set[idx - 1]]
                
        return ""
        
