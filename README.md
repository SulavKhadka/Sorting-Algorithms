# Sorting-Algorithms
An assignment for my Algorithm Design/Analysis class.

## How to run the sorting algorithms
Open the terminal and navigate to the assignment folder.
```
python sort_algos.py
```
You should see a menu like this:
```
~~~~ WELCOME TO THE SORTER ~~~~
Please enter a number:
```
Enter the number you would like to insert to your list and when you are done press enter instad of entering another number
That should take you to the program menu:
```
~~~~ WELCOME TO THE SORTER ~~~~
Please enter a number: 5
Please enter a number: 4
Please enter a number: 3
Please enter a number: 2
Please enter a number: 1
Please enter a number: 

>Press A to run Selection Sort
>Press B to run Insertion Sort
>Press C to run Quick Sort with random pivot selection
>Press D to run Quick Sort with first pivot selection
>Press E to run Merge Sort
>Press F to change the initial list to sort
>Press Q to Quit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```
Enter an option from the menu above:
```
Follow instructions as they appear on the terminal. and when ready to exit--> Press Q and Enter

## How to run the Testing program
Open the terminal and navigate to the assignment folder.
```
python testProg.py
```
It should run and give you an output chart similar to this:

*It took the script 1:44 minutes to finish computations on my computer 

SS = Selection Sort

QSR = Quick Sort Random

QSF = Quick Sort First

IS = Insertion Sort
```
Pair_Swap_Order:

|          | SS       | QSR      | IS       | QSF      | 
|----------|----------|----------|----------|----------|
| 200      | 20500    | 345      | 5050     | 300      | 
| 6400     | 20496000 | 7540     | 5121600  | 9600     | 
| 3200     | 5128000  | 5475     | 1280800  | 4800     | 
| 1600     | 1284000  | 2140     | 320400   | 2400     | 
| 400      | 81000    | 1034     | 20100    | 600      | 
| 100      | 5250     | 253      | 1275     | 100      | 
| 800      | 322000   | 1158     | 80200    | 1200     | 


Pre_Sorted_Order:

|          | SS       | QSR      | IS       | QSF      | 
|----------|----------|----------|----------|----------|
| 200      | 20500    | 267      | 0        | 200      | 
| 6400     | 20496000 | 12919    | 0        | 6400     | 
| 3200     | 5128000  | 6809     | 0        | 3200     | 
| 1600     | 1284000  | 2034     | 0        | 1600     | 
| 400      | 81000    | 991      | 0        | 400      | 
| 100      | 5250     | 262      | 0        | 100      | 
| 800      | 322000   | 1259     | 0        | 800      | 

Random_n_Order:

|          | SS       | QSR      | IS       | QSF      | 
|----------|----------|----------|----------|----------| 
| 200      | 20500    | 436      | 9613     | 296      | 
| 6400     | 20496000 | 16921    | 10263345 | 12073    | 
| 3200     | 5128000  | 10282    | 2603490  | 5573     | 
| 1600     | 1284000  | 1976     | 652145   | 2761     | 
| 400      | 81000    | 736      | 40471    | 839      | 
| 100      | 5250     | 108      | 2442     | 512      | 
| 800      | 322000   | 1332     | 156404   | 1598     | 

Reverse_Sort_Order:

|          | SS       | QSR      | IS       | QSF      | 
|----------|----------|----------|----------|----------|
| 200      | 20500    | 336      | 19900    | 20050    | 
| 6400     | 20496000 | 11198    | 20476800 | 20483150 | 
| 3200     | 5128000  | 7392     | 5118400  | 5121550  | 
| 1600     | 1284000  | 3373     | 1279200  | 1280750  | 
| 400      | 81000    | 1716     | 79800    | 80150    | 
| 100      | 5250     | 400      | 4950     | 5000     | 
| 800      | 322000   | 1348     | 319600   | 320350   | 

```
## Discussion
                      Best Case           Average Case            Worst Case
```
Selection Sort:       ~(n^2)/2            ~(n^2)/2               `~(n^2)/2

Insertion Sort:       n                   ~(n^2)/2                ~(n^2)/2

Quick Sort Random:    ~n*log(n)           ~n*log(n)               ~n*log(n)

Quick Sort First:     n                   ~n*log(n)               ~n^2

Merge Sort:           N/A                 N/A                     N/A
```

After looking at comparisions over several runs it seems that these algorithm are for the most part relatively close to the Big O times we discussed in class about each algorithm. It always seems to be below the discussed runtime a constant factor some of which I couldn't pin-point. But overall they do seem to follow the runtime estimates we discussed in class. 
