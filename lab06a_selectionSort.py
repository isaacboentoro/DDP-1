def minIndex(lst, startIndex):
    # base case: only one element to consider
    if startIndex == len(lst) - 1:
        return startIndex
    # Find minimum of remaining elements recursively
    k = minIndex(lst, startIndex + 1)
    # Return the minimum of all
    if lst[startIndex] < lst[k]:
        return startIndex
    else:
        return k  # Return sorted list


def selection_sort(lst, startIndex=0):
    if startIndex == len(lst) - 1:
        return
    min_index = minIndex(lst, startIndex)
    lst[startIndex], lst[min_index] = lst[min_index], lst[startIndex]
    selection_sort(lst, startIndex + 1)


def main():  # Call function to use sort function
    input_string = input("Type a sequence of numbers separated by commas:\n")
    if input_string == '':  # Take formatted input and append them to a list
        values = []  # with consideration for empty input
    else:
        values = input_string.split(",")

    for i in range(len(values)):  # Iterate through values list and convert type to integer
        values[i] = int(values[i])
    print('Input list:\n', values)  # Print final messages
    selection_sort(values)  # Apply sorting
    print('Sorted list:\n', values)


if __name__ == '__main__':  # Conditional execution
    main()
