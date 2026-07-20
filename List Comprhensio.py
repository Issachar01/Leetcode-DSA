if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    def coid(l, m, o, n):
        arr = [[a, b, c] for a in range(l + 1) for b in range(m + 1) for c in range(o + 1) if a + b + c != n]
        return arr
    
    print(coid(x, y, z, n))
