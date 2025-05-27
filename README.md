# 🐍 DSA Using Python

This repository is a structured collection of Python programs to help understand **Data Structures and Algorithms (DSA)**. It's organized by topics like basic math logic, hash maps, and recursion—ideal for beginners and intermediate programmers.

## 📁 Folder Structure
### 01_Basic_Maths_Logic
  - [Count_Digits.py](./01_Basic_Maths_Logic/01_Count_Digits.py)
  - [Reverse_Number.py](./01_Basic_Maths_Logic/02_Reverse_Number.py)
  - [Check_Palindrome.py](./01_Basic_Maths_Logic/03_Check_Palindrome.py)
  - [Factors.py](./01_Basic_Maths_Logic/04_Factors.py)
  - [Factorial.py](./01_Basic_Maths_Logic/05_Factorial.py)
  - [Armstrong_Number.py](./01_Basic_Maths_Logic/06_Armstrong_Number.py)
  - [LCM.py](./01_Basic_Maths_Logic/07_LCM.py)
  - [GCD.py](./01_Basic_Maths_Logic/08_GCD.py)
  - [Fibonacci_Series.py](./01_Basic_Maths_Logic/09_Fibonacci_Series.py)

### 02_Hash_Map_Python
  - [HashMapBasics.py](./02_Hash_Map_Python/01_HashMapBasics.py)
  - [UniqueNumber1.py](./02_Hash_Map_Python/02_UniqueNumber1.py)
  - [UniqueNumber2.py](./02_Hash_Map_Python/03_UniqueNumber2.py)
  - [UniqueNumber3.py](./02_Hash_Map_Python/04_UniqueNumber3.py)
  - [FrequencyCount.py](./02_Hash_Map_Python/05_FrequencyCount.py)

### 03_Recursion
  - [RecursionBasics.md](./03_Recursion/01_RecursionBasics.md)
  - [PowerFunction.py](./03_Recursion/02_PowerFunction.py)
  - [Factorial.py](./03_Recursion/03_Factorial.py)
  - [SumOfCubes.py](./03_Recursion/04._SumOfCubes.py)
  - [FibonacciSeries.py](./03_Recursion/05_FibonacciSeries.py)
  - [ReverseArrayUsingRecursion.py](./03_Recursion/06_ReverseArrayUsingRecursion.py)
  - [StringReversal.py](./03_Recursion/07_StringReversal.py)


### 04_Searching

| Algorithm                | Time (Best) | Time (Avg)   | Time (Worst) | Space | Requirement                            |
| ------------------------ | ----------- | ------------ | ------------ | ----- | -------------------------------------- |
| [**Linear Search**](./04_Searching/01_LinearSearch.py)        | O(1)        | O(n)         | O(n)         | O(1)  | None                                   |
| [**Binary Search** ](./04_Searching/02_BinarySearch)       | O(1)        | O(log n)     | O(log n)     | O(1)  | Sorted array                           |
| [**Interpolation Search**](./04_Searching/03_InterpolationSearch.py) | O(1)        | O(log log n) | O(n)         | O(1)  | Sorted and uniformly distributed array |


### 05_Sorting

| Algorithm          | Time (Best) | Time (Avg) | Time (Worst) | Space    | Stable? |
| ------------------ | ----------- | ---------- | ------------ | -------- | ------- |
| [**Bubble Sort**](./05_Sorting/01_BubbleSort.py)    | O(n)        | O(n²)      | O(n²)        | O(1)     | Yes     |
| [**Selection Sort**](./05_Sorting/02_SelectionSort.py) | O(n²)       | O(n²)      | O(n²)        | O(1)     | No      |
| [**Insertion Sort**](./05_Sorting/03_InsertionSort.py) | O(n)        | O(n²)      | O(n²)        | O(1)     | Yes     |
| [**Merge Sort**](./05_Sorting/04_MergeSort.py)     | O(n log n)  | O(n log n) | O(n log n)   | O(n)     | Yes     |
| [**Quick Sort**](./05_Sorting/05_QuickSort.py)     | O(n log n)  | O(n log n) | O(n²)        | O(log n) | No      |
| [**Heap Sort**](./05_Sorting/08_HeapSort.py)      | O(n log n)  | O(n log n) | O(n log n)   | O(1)     | No      |
| [**Counting Sort**](./05_Sorting/06_CountSort.py)  | O(n + k)    | O(n + k)   | O(n + k)     | O(k)     | Yes     |
| [**Radix Sort**](./05_Sorting/07_RadixSort.py)    | O(nk)       | O(nk)      | O(nk)        | O(n + k) | Yes     |
| [**Bucket Sort**](./05_Sorting/09_BucketSort.py)   | O(n + k)    | O(n + k)   | O(n²)        | O(n + k) | Yes     |

### 06_Array
  Easy
  - [Reverse an array](./06_Array/01_reverse_array.py)  
  - [Check if the array is sorted](./06_Array/02_check_sorted.py)
  - [Find the maximum and minimum element in an array](./06_Array/03_max_min_of_array.py)  
  - [Second Largest Element in an Array without sorting](./06_Array/04_second_largest.py) 
  - [Remove Duplicates from Sorted Array](./06_Array/05_remove_duplicate.py) 
  - [Right rotate an array by K places](./06_Array/06_right_rotate_k.py)  
  - [Move Zeros to end](./06_Array/07_moves_zeros_to_end.py)
  - [Move all negative number to end](./06_Array/08_move_negative_to_end.py) 
  - [Sort an array of 0, 1, & 2](./06_Array/09_sort_array_of_012.py) 
  - Merge 2 sorted Arrays  
  - Find missing number in an array  
  - Maximum Consecutive Ones  
  - Find whether an array is a subset of another array  

  Medium
  - Union of two arrays  
  - Intersection of two arrays  
  - Find the "Kth" max and min element of an array  
  - Merge 2 sorted arrays without using extra space  
  - Find duplicate in an array of N+1 Integers  
  - Merge Intervals  
  - Next Permutation  
  - Find if there is any subarray with sum equal to 0  
  - Rearrange the array in alternating positive and negative items with O(1) extra space  
  - Find the triplet that sum to a given value  
  - Find all pairs on integer array whose sum is equal to given number  
  - Find factorial of a large number  
  - Find longest consecutive subsequence  
  - Find all elements that appear more than " n/k " times  
  - Smallest Subarray with sum greater than a given value  
  - Three way partitioning of an array around a given value  
  - Minimum swaps required bring elements less equal K together  
  - Minimum no. of operations required to make an array palindrome  

  Hard
  - Kadane's Algorithm [V.V.V.V.V IMP]  
  - Find Largest sum contiguous Subarray [V. IMP]  
  - Minimise the maximum difference between heights [V.IMP]  
  - Minimum no. of Jumps to reach end of an array  
  - Count Inversion  
  - Best time to buy and Sell stock  
  - Maximum profit by buying and selling a share at most twice  
  - Find maximum product subarray  
  - Trapping Rain water problem  
  - Chocolate Distribution problem  
  - Find common elements in 3 sorted arrays  
  - Median of 2 sorted arrays of equal size
  - Median of 2 sorted arrays of different size





## ✅ Prerequisites

- Python 3.x
- Basic knowledge of Python syntax


## 🔔 Stay Tuned

More topics like **Sorting**, **Searching**, **Linked Lists**, **Stacks**, **Queues**, and **Trees** will be added soon.

**Stay tuned for more! 🚀**

---

Happy Coding! 💻✨


