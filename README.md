Dolphin 🐬

A Cache Simulator to mimic different policies, associativities, and methods of cache hitting, missing, and fetching data between the cache and the memory.

# FIFO

The First-In-First-Out (FIFO) policy replaces the entries in the order that they came into the cache.

An Index is maintained by the cache that points to the next entry to be replaced. After replacement, the index is incremented to keep flow.


## N-way (2)

For FIFO, there is an *n-Way Set Associative* that breaks the cache into `n` blocks (in our case, 2). Each location in the main memory is mapped to a specified set of blocks. In our program, there are 2 sets (Set 0, and Set 1). 

Set 0 are for values that are multiples of 2, and Set 1 are for the rest. 

*Note*: The size of the Memory depends on the number of data values the uesr inputs.

## Write-Back Policy

The FIFO structure has an integrated write-back policy, where it will only write the data to the main memory when the memory address in the associated cache entry is written.

Since our memory is a hashmap, we only have 4 memory blocks in this case (1 - 4). This is to keep each value organized and make the replacement easy.


# Random Replacement

This policy chooses a cache entry at random. The program uses the default `Random` Library to fetch a random index.

It should be noted that the random replacements policy is simple, but might cause more cache misses than the other 2 policies.

## Full Associative

Along with the Random Replacement Implementation, each location in the main memory can go to any block in the cache -> called Fully Associative.

*Note*: Associating Memory locations to specified cache blocks is called cache *associativity*.

## Write-Through Policy

With the Random Replacement, a Write-Policy has been implemented called Write-Through. Unlike Write-Back, the write-through policy will write the data to the main memory at the same time it is written to cache.

# LRU

This policy is unique compared to the other ones. The class `LRU` imitates the nature of *Least Recently Used* Replacement where the entry with the most time passed since it was last accessed. 

## Direct-Mapped

It made sense that by the complexity of the LRU, to keep the program simple, a direct-mapped approach had to be used. 

This association is where every location in the main memory can only be placed in *one* specified block in the cache.

# More Information

Each Cache is in the form of a Stack and an Array for comparision factors.

The Memory is a Hashmap for fetching and setting values.

If you have questions, or concerns, feel free to reach out to me! 