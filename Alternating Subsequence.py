import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
    
    t = int(data[0])
    idx = 1
    out = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        
        a = [int(x) for x in data[idx:idx + n]]
        idx += n
        
        total_sum = 0
        current_max = a[0]
        
        for i in range(1, n):
            if (a[i] > 0 and current_max > 0) or (a[i] < 0 and current_max < 0):
                current_max = max(current_max, a[i])
            else:
                total_sum += current_max
                current_max = a[i]
                
        total_sum += current_max
        out.append(str(total_sum))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
