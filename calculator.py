def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def isValidNum(string):
        if string.isdigit() or isFloat(string):
            return True
        else:
            return False

class Calculator:

    def __init__(self):
        super().__init__()
        self.memory = "0"
        self.workingMemory = []
        self.lastButtonClicked = ""
    
    def changeLastButtonClicked(self, string):
        self.lastButtonClicked = string
    
    def getLastButtonClicked(self):
        return self.lastButtonClicked

    def isWorkingMemoryEmpty(self):
        """Check if working memory is empty"""
        if self.workingMemory == []:
            return True
        else:
            return False

    def getMemory(self):
        """Return number in memory"""
        return self.memory
    
    def getWorkingMemory(self):
        """Return value in working memory"""
        if self.isWorkingMemoryEmpty():
            return eval(''.join(self.workingMemory))
        else:
            return self.workingMemory

    def multiply(self, num):
        """Adds number and multiplying operator to working memory"""
        self.workingMemory.append(num)
        self.workingMemory.append("*")

    def divide(self, num):
        """Adds number and division operator to working memory"""
        self.workingMemory.append(num)
        self.workingMemory.append("/")

    def add(self, num):
        """Adds number and addition operator to working memory"""
        self.workingMemory.append(num)
        self.workingMemory.append("+")

    def substract(self, num):
        """Adds number and subtraction operator to working memory"""
        self.workingMemory.append(num)
        self.workingMemory.append("-")

    def equals(self):
        """Returns the result of numbers and operations stored in working memory"""
        if self.isWorkingMemoryEmpty():
            return "0"
        else:
            return eval(''.join(self.workingMemory))

    def clearMemory(self):
        """Clears long term memory"""
        self.memory = "0"

    def clearWorkingMemory(self):
        """Clears working memory"""
        self.workingMemory = []
    
    def addToWorkingMemory(self, num):
        """Add number to working memory"""
        if isValidNum(num):
            self.workingMemory.append(num)

    def addToMemory(self, num):
        """Add number to working memory"""
        if isValidNum(num):
            self.memory = eval(f"{self.memory} + {num}")

    def addResultToMemory(self, num):
        """Replace number in memory with current result"""
        self.memory = num
