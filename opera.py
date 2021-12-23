class Opera:
    number = None
    operator = None
    available = True
    def __init__(self, operator):
        self.operator = operator

    def getNumber(self):
        if self.number == None:
            return None
        else:
            return self.number.getId()

    def numberState(self):
        if self.number == None:
            return None
        else:
            return self.number.getState()

    def setNumber(self,number):
        self.number = number
        self.number.alternateState('ringing')

    def cleanNumber(self):
        self.number = None
        self.available =True

    def busy(self):
        self.available = False
        self.number.alternateState('answered')

    def free(self):
        self.available = True
        self.number = None

    def getOperator(self):
        return self.operator

    def isAvailable(self):
        return self.available

    def compareTo(self,operator):
        if self.operator == operator:
            return True
        return False