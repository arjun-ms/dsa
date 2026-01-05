"""
You are given a stream of stock price updates as (timestamp, price) pairs.
- Timestamps are not sorted.
- The same timestamp may appear multiple times with updated prices.

Design a system that supports:
1. input(timestamp, price)  → record or update the price at a timestamp
2. get_max()               → return the maximum valid price so far
3. get_min()               → return the minimum valid price so far

Assume MaxHeap and MinHeap are already implemented and expose only:
- push()
- pop()

You may not modify heap internals.
"""

# We are explicitly assuming that MaxHeap and MinHeap are already implemented and provided these operations:

# max_heap.push()
# max_heap.pop()
# min_heap.push()
# min_heap.pop()

class Stocks:
    def __init__(self):
        self.max_heap = MaxHeap()
        self.min_heap = MinHeap()
        self.latest_price = {} 
        # we use this because heaps cant efficiently update without traversing the whole list, its only efficient for getting max and min element.

        # We use latest_price to tell which heap values are still valid, because heaps can’t update or remove old values efficiently.

        # Every time we insert a new value, we push it into the heap ignoring the old ones
        # and update the dictionary, so the dictionary always knows the latest valid 
        # while the heap keeps all historical ones.

        # So instead of updating, we insert new values and ignore old ones later.
        # A hashmap keeps track of the latest valid value.
        # This pattern is called lazy deletion.


    def input(self, timestamp,price):
        self.latest_price[timestamp] = price # This overwrites old prices 
        
        self.max_heap.push((price,timestamp))
        self.min_heap.push((price,timestamp))


    def get_max(self):
        while True:
            price, timestamp = self.max_heap.pop() # get the maximum price
            if self.latest_price.get(timestamp) == price: # checks whether the value we just popped from the heap is still the latest price for that timestamp.

                # We push it back because we only wanted to peek at the top, but since the heap API gives us only pop, we simulate a peek by popping and immediately pushing it back.
                self.max_heap.push((price, timestamp))
                return price, timestamp


    def get_min(self):
        price, timestamp = self.min_heap.pop()

        if self.latest_price.get(timestamp) == price:
            self.min_heap.push((price,timestamp))
            return price,timestamp


    # we dont put negative sign as we do for heapq when implementing a max_heap because we assume maxheap DS already exists
