#coding = utf-8

'''
堆排序
'''

class Solution:
    def heap_sort(self, heap): #将根节点取出与最后一位做对调，对前面len-1个节点继续进行对调整过程
        self.build_max_heap(heap)
        print(heap)
        for i in range(len(heap)-1, -1, -1):
            heap[0], heap[i] = heap[i], heap[0]
            self.max_heapify(heap, i, 0)
        return heap

    def build_max_heap(self, heap):  #构造一个堆，将堆中所有数据重新排序
        heapsize = len(heap)
        for i in range((heapsize - 2)//2, -1, -1):  #从后往前出数
            self.max_heapify(heap, heapsize, i)

    def max_heapify(self, heap, heapsize, root):  #在堆中做结构调整使得父节点的值大于子节点
        left = 2*root + 1
        right = left + 1
        larger = root
        if left < heapsize and heap[larger] < heap[left]:
            larger = left
        if right < heapsize and heap[larger] < heap[right]:
            larger = right
        if larger != root:  #如果做了堆调整则larger的值等于左节点或者右节点的，这个时候做对调值操作
            heap[larger], heap[root] = heap[root], heap[larger]
            self.max_heapify(heap, heapsize, larger)

print(Solution().heap_sort([2,4,6,7,1,2,5]))