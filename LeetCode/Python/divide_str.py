class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        str_len = len(s)
        mod = str_len % k
        idx_fill = mod and k - mod
        idx_range = (str_len - mod)
        
        new_list = []
        prev_idx = 0
        for i in range(k,idx_range+1,k):
            new_list.append(s[prev_idx:i])
            prev_idx = i
            
        remain = s[idx_range:] + fill * idx_fill
        if len(remain):
            new_list.append(remain)

        return new_list
