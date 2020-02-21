# Geo Distributed LRU Cache

### Implementation
Code is found in `cache.py` and `helper.py` and the test is found in `cache_test.py`

For the cache, I focused primarily on the properties of the caches itself. So, the caches are Geo distributed and use the LRU convention with time expiration. The implementation is extremely simple because it only contains 2 methods (get() and put()) which are used respectively to get data from the cache and add data to the cache.

Each cache contains 3 dictonaries where each dictionary share the same keys:
1. To hold the value
2. To hold the time it was placed in the cache
3. To hold the duration of the cache item 

And I also used to a deque (double-ended queue) to keep track of the least recently used item. Whenever you put or get an item from the cache, it pushes the item to the back of the deque() since it's the most recently used and when the cache is full, it pops the front of the deque() (i.e. the LRU item).

To check for expiration, I went for a simple approach where it will check for expiration and remove all expired items every time you use the cache (i.e. calling put() or get()).

### Missing Features
This implementation doesn't support network connections and it doesn't support data consistency across regions. I was thinking about linking them together in a circular linked list to write across all caches. I was also thinking about implementing a hash function when storing the keys in the caches since they're added directly from the user for this implementation and different users can use the same key and overwrite each other's cache items. The cache also doesn't handle cache misses since that's usually where you call the query method to access the database so it throws an error instead.

For the captials.csv, I was initially going to use it to create caches at random locations and try to simulate a real life environment with caches at various different locations. Ultimately, it wasn't useful since I didn't have any network features. I ended up using it for data in the tests.