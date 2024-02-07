import heapq
from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')


class IQueue(ABC, Generic[T]):
    @abstractmethod
    def empty(self):
        pass
    
    @abstractmethod
    def top(self) -> T:
        pass

    @abstractmethod
    def put(self, item: T):
        pass

    @abstractmethod
    def get(self) -> T:
        pass

class IMetered(ABC):
    @abstractmethod
    def __len__(self):
        pass
    
    @abstractmethod
    def get_count(self):
        pass

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

class MeteredQueue(Queue, IMetered, Generic[T]):
    def __init__(self):
        super().__init__()
        self.counter = 0

    def put(self, item: T):
        self.counter += 1
        self.elements.append(item)

    def __len__(self):
        return len(self.elements)

    def get_count(self):
        return self.counter
    

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

    
class MeteredPriorityQueue(PriorityQueue, IMetered, Generic[T]):
    def __init__(self):
        super().__init__()
        self.counter = 0

    def put(self, item):
        self.counter += 1
        heapq.heappush(self.elements, item)
    
    def __len__(self):
        return len(self.elements)
    
    def get_count(self):
        return self.counter
    
    