class Call:
    id = None
    state = None
    #states: answered , ringing , waiting , received
    def __init__(self,id):
        self.state = "received"
        self.id = id
    def alternateState(self,state):
        self.state = state

    def getId(self):
        return self.id

    def getState(self):
        return self.state