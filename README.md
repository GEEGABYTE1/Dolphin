Dolphin 🐬

A Cache Simulator to mimic different policies, associativities, and methods of cache hitting, missing, and fetching data between the cache and the memory.

# FIFO

The First-In-First-Out (FIFO) policy replaces the entries in the order that they came into the cache.

An Index is maintained by the cache that points to the next entry to be replaced. After replacement, the index is incremented to keep flow.


## N-way (2)

For FIFO, there is an *n-Way Set Associative* that breaks the cache into `n` blocks (in our case, 2). Each location in the main memory is mapped to a specified set of blocks. In our program, there are 2 sets (Set 0, and Set 1). 

Set 0 are for values that are multiples of 2, and Set 1 are for the rest. 

*Note*: The size of the Memory depends on the number of data values the uesr inputs.


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

## Write-Back Policy

Although Direct-Mapped associativity does not need write-back policies