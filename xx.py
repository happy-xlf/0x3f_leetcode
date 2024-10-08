def mc(arr):
    odd_cost = 0
    even_cost = 0
    s_odd = 0
    s_even = 0
    
    # 计算将数组转为全奇数的代价
    for num in arr:
        if num % 2 == 0:  # 如果是偶数，+1代价为1
            odd_cost += 1
            s_odd += num
        else:  # 如果是奇数，不需要操作
            even_cost += 1
            s_even += num
    
    # 返回转换为全奇数或全偶数的最小代价
    return min(odd_cost + s_odd, even_cost + s_even)

# 输入

n = int(sys.stdin.readline())  # 数组大小
arr = list(map(int, sys.stdin.readline().split()))  # 输入数组

# 输出最小转换代价
print(mc(arr))
