import cmd, sys
from turtle import bye
from opera import Opera
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

class QueueShell(cmd.Cmd):
    intro = "Welcome to the Queue"
    prompt = "(Queue) "
    file = None
    operators = [Opera("A"), Opera("B")]
    queue = []
    def do_call(self,id):
        sys.stdout.write("call {} received\n".format(id))
        for op in self.operators:
            if op.getNumber() == None:
                call = Call(id)
                op.setNumber(call)
                sys.stdout.write("Call {} ringing for operator {}\n".format(id,op.getOperator()))
                return
        call = Call(id)
        call.alternateState("waiting")
        sys.stdout.write("Call {} waiting in queue\n".format(id))
        self.queue.append(call)
        return

    def do_answer(self,operator):
        for op in self.operators:
            if op.compareTo(operator):
                if op.getNumber()==None:
                    sys.stdout.write("Operator {} is not busy\n".format(operator))
                else:
                    op.busy()
                    sys.stdout.write("Call {} answered by operator {}\n".format(op.getNumber(), op.getOperator()))
                return
        sys.stdout.write("This operator does not exist\n")
        return
    def do_reject(self,operator):
        for op in self.operators:
            if op.compareTo(operator):
                sys.stdout.write("Call {} rejected by operator {}\n".format(op.getNumber(),operator))
                for i in self.operators:
                    if i.getNumber() == None:
                        call = Call(op.getNumber())
                        i.setNumber(call)
                        sys.stdout.write("Call {} ringing for operator {}\n".format(i.getNumber(), i.getOperator()))
                        op.free()
                        return
                sys.stdout.write("Call {} ringing for operator {}\n".format(op.getNumber(),operator))
                return
        sys.stdout.write("Operator {} is not busy\n".format(operator))
        return
    def do_hangup(self,id):
        for op in self.operators:
            if op.getNumber() == id:
                if op.numberState() == "answered":
                    sys.stdout.write("Call {} finished and operator {} available\n".format(id,op.getOperator()))
                else:
                    sys.stdout.write("Call {} missed\n".format(id))
                op.free()
                if len(self.queue) != 0:
                    op.setNumber(self.queue[0])
                    self.queue.remove(self.queue[0])
                    sys.stdout.write("Call {} ringing for operator {}\n".format(op.getNumber(), op.getOperator()))
                return
        for op in self.queue:
            if op.getId() == id:
                self.queue.remove(op)
                sys.stdout.write("Call {} missed\n".format(id))

        return
    def do_close(self, arg):
        print('closing the queue')
        bye()
        return True
    def do_printQueue(self,arg):
        for op in self.operators:
            sys.stdout.write("Operador: {}\n"
                  "Operator disponivel: {}\n"
                  "Number called: {}\n"
                  "Number state: {}\n".format(op.getOperator(),op.isAvailable(),op.getNumber(),op.numberState()))
        i = 0
        for ca in self.queue:
            sys.stdout.write("Fila: {}\n"
                  "Number called: {}\n"
                  "Number state: {}\n".format(i, ca.getId(), ca.getState()))
            i+=1
        return