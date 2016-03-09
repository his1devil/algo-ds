```python
# 快排首先要选择一个pivot value用来调校list splited (这里选第一个)
# pivot value最终所处位置称为split point，用来分割子列表
# 快排的关键在于partition function
# 首先partitioning标记两个位置 leftmark和rightmark(pivot value外列表的左端和右端) 
# 遍历增加leftmark，直到找到> pivot value的值的位置，然后遍历递减rightmark，直到找到 < pivot value的位置
# when rightmark < leftmark, stop, rightmark即为split point
# 然后对splited list各自递归quick sort

```
复杂度分析: 对于长度为n的list，如果partition总是出现在middle处，将会产生logn次divisions，为了找到split point
每一个item都需要进行和pivot value对比，即nlogn，而且在merge阶段不需要额外的存储空间

不过，最坏的情况是split points不在middle位，靠近左端或是右端，造成非常不均衡的division，结果可能就是O(n²)

选择pivot value的方法不止一种，这里使用median of three方法减少uneven division:
    首先考虑list中first, middle和last的值，实例54, 77, 20
    选择median value，即54作为pivot value
```

def quickSort(L):
    quickSortHelper(L, 0, len(L) - 1)

def quickSortHelper(L, first, last):
    if first < last:
        splitpoint = partition(L, first, last)
        quickSortHelper(L, first, splitpoint - 1)
        quickSortHelper(L, splitpoint + 1, last)

```
