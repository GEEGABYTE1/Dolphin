Dolphin 🐬

A Cache Simulator to mimic different policies, associativities, and methods of cache hitting, missing, and fetching data between the cache and the memory.

# FIFO

The First-In-First-Out (FIFO) policy replaces the entries in the order that they came into the cache.

An Index is maintained by the cache that points to the next entry to be replaced. After replacement, the index is incremented to keep flow.


## N-way (2)

For FIFO, there is an *n-Way Set Associative* that breaks the cache into `n` blocks (in our case, 2). Each location in the main memory is mapped to a specified set of blocks. In our program, there are 2 sets (Set 0, and Set 1). 

Set 0 are for values that are multiples of 2, and Set 1 are for the rest. 

*Note*: The size of the Memory depends on the number of data values the uesr inputs.


# Random

## Full Associative

## Write-Through Policy


# LRU

## Direct-Mapped

## Write-Back Policy