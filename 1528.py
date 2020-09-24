def restoreString(self, s: str, indices: List[int]) -> str:
    result = ['']*len(s) 
    for i,charx in zip(indices, s): 
        result[i] = charx 
    return ''.join(result)