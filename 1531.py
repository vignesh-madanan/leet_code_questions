from collections import Counter
def run_process(s,k):
    s_counter = Counter(s)
    if not k: return 0
    result = ''
    for char, ix in s_counter.items():
        result+='{char}{ix}'
    
      


if __name__ == "__main__":
    ips = [("aaabcccd", 2),("aabbaa", 2) ,("aaaaaaaaaaa",0)]
    print(list(map(run_process, ips)))
