def rolling_4sum(n, m):

    n = str(n)
    for i in range(len(n)-3):
        if sum(int(x) for x in n[i:i+4]) > m:
            return False
    return True


def max_sumDig(nMax, maxSum):

    nums = []
    for i in range(1000, nMax + 1):
        if rolling_4sum(i, maxSum):
            nums.append(i)
    var1 = len(nums)
    var2 = min(nums, key = lambda x: abs(x - (sum(nums)/var1)))
    var3 = sum(nums)
    return [var1, var2, var3]
