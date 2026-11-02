# Experiment A2: Customer Account ID Search
# Group A: Arrays and Searching Sorting Algorithms

def linear_search(arr, target):
    """Sequentially checks each customer account ID in the list."""
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1


def binary_search(arr, target):
    """Performs binary search on a sorted list of customer account IDs."""
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


if __name__ == "__main__":
    account_ids = [1045, 1012, 1089, 1023, 1056, 1001]
    target_id = 1056

    print("--- E-Commerce Customer Search ---")
    print(f"Original Account IDs : {account_ids}")
    
    # Linear Search
    lin_idx = linear_search(account_ids, target_id)
    print(f"Linear Search        : ID {target_id} found at index {lin_idx}")

    # Binary Search (requires sorted list)
    sorted_ids = sorted(account_ids)
    print(f"Sorted Account IDs   : {sorted_ids}")
    bin_idx = binary_search(sorted_ids, target_id)
    print(f"Binary Search        : ID {target_id} found at index {bin_idx}")
