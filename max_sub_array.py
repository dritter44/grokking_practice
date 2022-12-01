def max_sub_array_of_size_k(k,arr):
    max_sum, win_sum = 0,0
    win_start = 0
    for win_end in range(len(arr)):
        win_sum+=arr[win_end]
        #slide the window to the right. happens for the first time when win_end reaches K-1
        if win_end > k-1:
            max_sum = max(max_sum,win_sum)
            win_sum -= arr[win_start]
            win_start += 1

    return max_sum