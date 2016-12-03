import sort_algos as SA
import random


def sort_comparison(lst):
    cd = {}

    og_array = list(lst)

    lst = list(lst)
    counter = 0
    comp1 = SA.insertion_sort(lst, counter)
    cd['IS'] = comp1[1]

    counter = 0
    lst = list(og_array)
    comp2 = SA.selection_sort(lst, counter)
    cd['SS'] = comp2[1]

    '''
    counter = 0
    lst = list(og_array)
    comp3 = SA.merge_sort(lst, counter)
    cd['merge_sort'] = comp3
    '''

    counter = 0
    lst = list(og_array)
    comp4 = SA.quick_sort_first(lst, counter)
    cd['QSF'] = comp4[1]

    counter = 0
    lst = list(og_array)
    comp5 = SA.quick_sort_random(lst, counter)
    cd['QSR'] = comp5[1]
    return cd


def reverse_sort_order(n, main_dict):
    n_dict = {}
    for i in n:
        test_list = []
        for j in range(i, 0, -1):
            test_list.append(j)
        results = sort_comparison(test_list)
        n_dict[str(i)] = results
    main_dict['Reverse_Sort_Order'] = n_dict
    return main_dict


def pre_sorted_order(n, main_dict):
    n_dict = {}
    for i in n:
        test_list = []
        for j in range(1, i+1):
            test_list.append(j)
        results = sort_comparison(test_list)
        n_dict[str(i)] = results
    main_dict['Pre_Sorted_Order'] = n_dict
    return main_dict


def pair_swap_order(n, main_dict):
    n_dict = {}
    for i in n:
        test_list = []
        for j in range(2, i+1, 2):
            test_list.append(j)
            test_list.append(j-i)
        results = sort_comparison(test_list)
        n_dict[str(i)] = results
    main_dict['Pair_Swap_Order'] = n_dict
    return main_dict


def random_n_order(n, main_dict):
    n_dict = {}
    for i in n:
        test_list = []
        for j in range(0, i):
            rand_num = random.randrange(999999)
            test_list.append(rand_num)
        results = sort_comparison(test_list)
        n_dict[str(i)] = results
    main_dict['Random_n_Order'] = n_dict
    return main_dict


def output_tables(main_dict):
    for i in main_dict:
        print i
        print "_______________________"
        print "|     |",
        for j in main_dict[i]:
            for k in main_dict[i][j]:
                print k, "|",
            print ""
            break
        for j in main_dict[i]:
            print "|", j, "|",
            for k in main_dict[i][j]:
                print main_dict[i][j][k], "|",
            print ""
        print "_______________________"
        print "\n"

def main():
    n = [100, 200, 400, 800, 1600, 3200, 6400]
    main_dict = {}
    rso = reverse_sort_order(n, main_dict)
    pstdo = pre_sorted_order(n, main_dict)
    pswpo = pair_swap_order(n, main_dict)
    rnd = random_n_order(n, main_dict)

    output_tables(main_dict)

main()
