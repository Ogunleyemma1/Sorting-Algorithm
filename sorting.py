def quick_sort(arr: list[int]) -> list[int]:
    # QuickSort Helper Function
    # Introducing a helper function to find the pivot and rearrange the elements from the pivot
    def quick_sort_partition(arr: list[int], low: int, high: int) -> int:
        # Defining an arbitrary pivot
        pivot = arr[low]

        # Defining an integer "i" which counts all values greater than pivot from the left and moves them to the right
        # Defining an integer "j" which counts all values less than pivot from the right and moves them to the left
        i = low + 1
        j = high

        # Implementing a loop to rearrange "i and j" values as described above
        while i <= j:
            # Implementing another loop to move the values of "i" greater than pivot to the RHS
            while i <= j and arr[i] <= pivot:
                i += 1

            # Implementing another loop to move the values of "j" lesser than pivot to the LHS
            while i <= j and arr[j] > pivot:
                j -= 1

            # Implementing a condition to swap "i" for "j" when it arrives at a value of "i" greater than pivot and "j" less than pivot to sort the list
            if i <= j:
                # Swapping variable of "j" for "i"
                arr[i], arr[j] = arr[j], arr[i]
            else:
                break

        # Swapping the pivot element with the smallest element in "j"
        arr[low], arr[j] = arr[j], arr[low]
        # Returning the index of the pivot
        return j

    # Implementing the iterative part of the quick sorting algorithm
    def quick_sort_iteration(arr: list[int], low = 0, high = len(arr) -1):
        if low < high:
            # Partition the array and get the index where the pivot is now located
            pivot = quick_sort_partition(arr, low, high)

            # Sorting the left Sub array
            quick_sort_iteration(arr, low, pivot - 1)

            # Sorting the right Sub array
            quick_sort_iteration(arr, pivot + 1, high)

    quick_sort_iteration(arr)
    return arr


def counting_sort(arr: list[int]) -> list[int]:
    # Implementing a condition to return the array if length is zero
    if len(arr) == 0:
        return arr

    # For the array, we proceed to find the maximum, minimum numbers and range
    max_number = max(arr)
    min_number = min(arr)
    range_of_numbers = max_number - min_number + 1

    # Initialize an array "Count" to count the numbers of occurrences of each element in the array
    count = [0] * range_of_numbers

    # Implementing a loop to count the numbers of occurrences of each element
    for element in arr:
        count[element - min_number] += 1

    # Updating the count array as the sum of values in count
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Initialize a temporary array to store output
    temp = [0] * len(arr)

    for element in reversed(arr):
        temp[count[element - min_number] - 1] = element
        count[element - min_number] -= 1

    # Copying back the temporary array into the original array
    arr = temp
    return arr
