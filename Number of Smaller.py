import sys

def main():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    
    n, m = map(int, lines[0].split())
    a = list(map(int, lines[1].split()))
    b = list(map(int, lines[2].split()))
    
    i = 0
    res = []
    
    for val in b:
        while i < n and a[i] < val:
            i += 1
        res.append(str(i))
        
    print(" ".join(res))

if __name__ == "__main__":
    main()
