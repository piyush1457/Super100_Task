def most_frequent(lst):
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    return max(freq, key=freq.get)

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("Most frequent element:", most_frequent(numbers))
