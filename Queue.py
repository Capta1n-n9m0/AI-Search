import heapq
from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')

# Abstract class for a queue
class IQueue(ABC, Generic[T]):
    # Check if the queue is empty
    @abstractmethod
    def empty(self):
        pass
    
    # Get the top element of the queue
    @abstractmethod
    def top(self) -> T:
        pass

    # Put an item in the queue
    @abstractmethod
    def put(self, item: T):
        pass

    # Get an item from the queue
    @abstractmethod
    def get(self) -> T:
        pass

# Abstract class for a class that can be metered
class IMetered(ABC):
    # Get the size of a collection
    @abstractmethod
    def __len__(self):
        pass
    
    # Get the count of the collection
    @abstractmethod
    def get_count(self):
        pass

# Queue implementation
class Queue(IQueue, Generic[T]):
    def __init__(self):
        self.elements: list[T] = []

    def empty(self):
        return len(self.elements) == 0

    def top(self) -> T:
        return self.elements[0]

    def put(self, item: T):
        self.elements.append(item)

    def get(self) -> T:
        return self.elements.pop(0)

# Metered queue implementation using the queue
class MeteredQueue(Queue, IMetered, Generic[T]):
    def __init__(self):
        super().__init__()
        self.counter = 0

    # Put the item in the queue and increment the counter
    def put(self, item: T):
        self.counter += 1
        self.elements.append(item)

    # Get the size of the queue
    def __len__(self):
        return len(self.elements)

    # Get the count of the queue
    def get_count(self):
        return self.counter
    
# Priority queue implementation
# It uses the heapq module to implement the priority queue
# This is a min-heap implementation
class PriorityQueue(IQueue, Generic[T]):
    def __init__(self):
        self.elements: list[T] = []

    def empty(self):
        return len(self.elements) == 0

    def top(self) -> T:
        return self.elements[0]

    def put(self, item):
        heapq.heappush(self.elements, item)

    def get(self) -> T:
        return heapq.heappop(self.elements)

# Metered priority queue implementation using the priority queue
class MeteredPriorityQueue(PriorityQueue, IMetered, Generic[T]):
    def __init__(self):
        super().__init__()
        self.counter = 0

    # Put the item in the queue and increment the counter
    def put(self, item):
        self.counter += 1
        heapq.heappush(self.elements, item)
    
    def __len__(self):
        return len(self.elements)
    
    def get_count(self):
        return self.counter
    
    