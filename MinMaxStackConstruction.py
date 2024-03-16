class MinMaxStack:
    def __init__(self):
        self.stack = []
        self.minMaxStack = []

    def peek(self):
        if self.stack: 
            return self.stack[-1]

    def pop(self):
            if self.stack:
                self.minMaxStack.pop()
                return self.stack.pop()
    
    def push(self, value):
         newMinMax = {'min': value, 'max': value}
         if self.minMaxStack:
            lastMinMax = self.minMaxStack[-1]
            newMinMax['min'] = min(lastMinMax['min'], value)
            newMinMax['max'] = max(lastMinMax['max'], value)
            self.stack.append(value)
            self.minMaxStack.append(newMinMax)
    def getMin(self):
        if not self.minMaxStack:
            return None
         
        return self.minMaxStack[-1]['min']
    
    def getMax(self):
         if not self.minMaxStack:
              return None
         return self.minMaxStack[-1]['max']

         
                 
