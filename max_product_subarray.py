# Maximum Product Subarray 

# T.C = O(n)
def max_product_subarray_prefix_suffix(arr):
    n = len(arr)
    if n == 0:
        return 0

    prefix_product = 1
    suffix_product = 1
    max_product = float('-inf')

    for i in range(n):
        # Multiply prefix product
        prefix_product *= arr[i]
        # Multiply suffix product (from end)
        suffix_product *= arr[n - 1 - i]

        # Update maximum product seen so far
        max_product = max(max_product, prefix_product, suffix_product)

        # Reset to 1 if product becomes 0
        if arr[i] == 0:
            prefix_product = 1
        if arr[n - 1 - i] == 0:
            suffix_product = 1

    return max_product

