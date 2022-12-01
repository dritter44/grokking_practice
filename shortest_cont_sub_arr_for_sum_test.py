from shortest_cont_sub_arr_for_sum_val import shortest_cont_sub_arr_for_val 

def main():
    #test an array of [2,1,5,2,3,2], s = 7, 
    print("The longest continuous sub array for which the sum is greater than s is: " + str(shortest_cont_sub_arr_for_val(7,[2,1,5,2,3,2])))
    #test an array of [3,3,4,5,1,5], s = 15, two answers here, should get 4 
    print("The longest continuous sub array for which the sum is greater than s is: " + str(shortest_cont_sub_arr_for_val(15,[3,3,4,5,1,5])))
    # edge case: empty array return -1
    print("The longest continuous sub array for which the sum is greater than s is: " + str(shortest_cont_sub_arr_for_val(7,[])))

    #edge case: 1 val in array > s return 1
    print("The longest continuous sub array for which the sum is greater than s is: " + str(shortest_cont_sub_arr_for_val(7,[8])))
    #edge case: 1 val in array < s return -1
    print("The longest continuous sub array for which the sum is greater than s is: " + str(shortest_cont_sub_arr_for_val(7,[5])))