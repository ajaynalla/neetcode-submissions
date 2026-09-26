class TimeMap:

    def __init__(self):
        self.cap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.cap:
            self.cap[key] = []
        self.cap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        arr = self.cap.get(key, [])
        l, r = 0, len(arr) - 1
        best = ""
        while l <= r:
            mid = (l+r)//2
            if arr[mid][1] <= timestamp:
                best = arr[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return best