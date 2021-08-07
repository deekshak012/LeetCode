class MyQueue(object):
    def __init__(self):
        self.stack=[]
        self.tempstack=[]

    def push(self, x):
        self.stack.append(x)
        

    def pop(self):
        if self.tempstack==[]:
            while(self.stack!=[]):
                self.tempstack.append(self.stack.pop())
        return self.tempstack.pop();
            

    def peek(self):
        if self.tempstack==[]:
            while(self.stack!=[]):
                self.tempstack.append(self.stack.pop())
        return self.tempstack[-1];
        

    def empty(self):
        return self.stack==[] and self.tempstack==[]
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()