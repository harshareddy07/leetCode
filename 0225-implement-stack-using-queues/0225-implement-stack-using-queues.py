class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x) :
        self.q1.append(x)

    def pop(self):
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        
        popped_element = self.q1.popleft()
        
        # Swap q1 and q2
        self.q1, self.q2 = self.q2, self.q1
        
        return popped_element

    def top(self) :
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        
        top_element = self.q1[0]
        
        self.q2.append(self.q1.popleft())
        
        # Swap q1 and q2
        self.q1, self.q2 = self.q2, self.q1
        
        return top_element

    def empty(self) :
        return len(self.q1) == 0