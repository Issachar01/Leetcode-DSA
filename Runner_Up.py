if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    clean_sorted_list = sorted(list(set(arr)))
    
    print(clean_sorted_list[-2])
    
