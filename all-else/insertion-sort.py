def insertion_sort_with_explanation(arr):
    print("Initial array:", arr)
    print("\nBeginning Insertion Sort:\n")

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        print(f"Step {i}:")
        print(f"  Current element to insert: {key}")
        print(f"  Current array state: {arr}")
        
        if arr[j] <= key:
            print(f"  {key} is already in the correct position.")
        else:
            print(f"  Finding the correct position for {key}:")
        
        while j >= 0 and arr[j] > key:
            print(f"    Comparing {key} with {arr[j]}")
            print(f"    {arr[j]} > {key}, so moving {arr[j]} to the right")
            arr[j + 1] = arr[j]
            j -= 1
            print(f"    Current array state: {arr}")
        
        if j + 1 != i:
            arr[j + 1] = key
            print(f"  Inserted {key} at index {j + 1}")
            print(f"  Array after insertion: {arr}")
        
        print()  # Empty line for readability

    print("Sorting complete. Final array:", arr)

# Test the function
test_array = [64, 34, 25, 12, 22, 11, 90]
insertion_sort_with_explanation(test_array)