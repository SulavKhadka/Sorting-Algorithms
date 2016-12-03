import random
import sys
sys.setrecursionlimit(7000)


def selection_sort(array, counter):
    for i in range(0,len(array)):
        min_val = array[i:len(array)+1][0]
        for j in array[i:len(array)+1]:
            counter += 1
            if j < min_val:
                min_val = j
        k = array[i:len(array)+1].index(min_val)+i
        counter += 2
        array[k], array[i] = array[i], array[k]
    return [array, counter]


def insertion_sort(array, counter):
    for i in range(1, len(array)):
        k = i-1
        x = array[i]
        counter += 1
        while k >= 0 and x < array[k]:
            counter += 1
            array[k+1] = array[k]
            k -= 1
        array[k+1] = x
    return [array, counter]


def quick_sort_random(array, counter):
    n = len(array)
    if n <= 50:
        return insertion_sort(array, counter)
    rand_num = random.randrange(len(array))
    pivot = array[rand_num]

    L_lst = []
    R_lst = []
    M_lst = []
    for i in array:
        counter += 1
        if i < pivot:
            L_lst.append(i)
        elif i > pivot:
            R_lst.append(i)
        else:
            M_lst.append(i)
    return quick_sort_random(L_lst, counter) + M_lst + quick_sort_random(R_lst, counter)


def quick_sort_first(array, counter):
    n = len(array)
    if n <= 50:
        return insertion_sort(array, counter)
    pivot = array[0]

    L_lst = []
    R_lst = []
    M_lst = []
    for i in array:
        counter += 1
        if i < pivot:
            L_lst.append(i)
        elif i > pivot:
            R_lst.append(i)
        else:
            M_lst.append(i)
    return quick_sort_first(L_lst, counter) + M_lst + quick_sort_first(R_lst, counter)


def merge_sort(array, counter):
    n = len(array)
    if n > 1:
        return merge(merge_sort(array[0:n/2], counter), merge_sort(array[n/2:n], counter), counter)
    else:
        return array


def merge(arr1, arr2, counter):

    k = len(arr1)
    l = len(arr2)
    counter += 1
    if k == 0: return arr2
    if l == 0: return arr1
    if arr1[0] <= arr2[0]:
        return [arr1[0]] + merge(arr1[1:k], arr2[0:l], counter)
    else:
        return [arr2[0]] + merge(arr1[0:k], arr2[1:l], counter)


def print_menu():
    print  "\n>Press A to run Selection Sort"
    print  ">Press B to run Insertion Sort"
    print  ">Press C to run Quick Sort with random pivot selection"
    print  ">Press D to run Quick Sort with first pivot selection"
    print  ">Press E to run Merge Sort"
    print  ">Press F to change the initial list to sort"
    print  ">Press Q to Quit"
    print  "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"


def print_list(array):
    print "[",
    for i in array[0]:
        print i,
    print "] --> comparisons: {}".format(array[1])


def user_input_list():
    user_lst = []
    try:
        while True:
            sort_input = int(raw_input("Please enter a number: "))
            user_lst.append(sort_input)
    except ValueError:
        pass
    return user_lst

if __name__ == "__main__":
    print "~~~~ WELCOME TO THE SORTER ~~~~"
    opt_input = ""
    input_list = user_input_list()
    og_list = list(input_list)
    while opt_input.upper() != 'Q':
        print_menu()
        opt_input = raw_input("Enter an option from the menu above: ")
        input_list = list(og_list)
        print "INIT:", input_list
        counter = 0
        if opt_input.upper() == 'A':
            array = selection_sort(input_list, counter)
            print_list(array)
        elif opt_input.upper() == 'B':
            array = insertion_sort(input_list, counter)
            print_list(array)
        elif opt_input.upper() == 'C':
            array = quick_sort_random(input_list, counter)
            print_list(array)
        elif opt_input.upper() == 'D':
            array = quick_sort_first(input_list, counter)
            print_list(array)
        elif opt_input.upper() == 'E':
            array = merge_sort(input_list, counter)
            print_list(array)
        elif opt_input.upper() == 'F':
            og_list = user_input_list()
        elif opt_input.upper() == 'Q':
            exit()
        else:
            print "Your input is invalid. Try again."
