def shortest_cont_sub_arr_for_val(s,arr):
    #returns the length of the smallest sub-array whose sum is equal to or greater than s
    # at start window only moves when sum of window is greater than s
    # window end starts at index 0
    wind_end = 0
    # window start starts at 0
    wind_start = 0
    # smallest window length starts at inf
    small_sub_arr_len = len(arr) + 1
    #EDGE CASE:empty arr
    if len(arr) is None:
        return -1
    win_sum = 0
    # begin incrementing the index of the window end, starting at 0, until the len of the arr
    for wind_end in range(len(arr)):
        sub_arr_len = small_sub_arr_len
        win_sum += arr[wind_end]
        if win_sum >= s:
            sub_arr_len = len(arr[wind_start:wind_end]) + 1
            if sub_arr_len < small_sub_arr_len:
                small_sub_arr_len = sub_arr_len
            wind_start += 1
    #EDGE CASE: if sum of arr still less than s:
    if small_sub_arr_len > len(arr):
        return -1
    #EDGE CASE: 

    return small_sub_arr_len