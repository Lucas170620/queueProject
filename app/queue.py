import cmd
from turtle import bye
from app.operador import Opera
from app.call import Call

class Queue(cmd.Cmd):
    intro = "Welcome to the Queue"
    prompt = "(Queue) "
    file = None
    operators = [Opera("A"), Opera("B")]
    queue = []

    def do_call(self, id):
        stdout =[]
        stdout.append("Call {} received".format(id))
        for op in self.operators:
            if op.getNumber() is None:
                call = Call(id)
                op.setNumber(call)
                stdout.append("Call {} ringing for operator {}".format(id, op.getOperator()))
                return stdout
        call = Call(id)
        call.alternateState("waiting")
        stdout.append("Call {} waiting in queue".format(id))
        self.queue.append(call)
        return stdout

    def do_answer(self, operator):
        stdout = []
        for op in self.operators:
            if op.compareTo(operator):
                if op.getNumber() is None:
                    stdout.append("Operator {} is not busy".format(operator))
                else:
                    op.busy()
                    stdout.append("Call {} answered by operator {}".format(op.getNumber(), op.getOperator()))
                return stdout
        stdout.append("This operator does not exist")
        return stdout

    def do_reject(self, operator):
        stdout = []
        for op in self.operators:
            if op.compareTo(operator):
                stdout.append("Call {} rejected by operator {}".format(op.getNumber(), operator))
                for i in self.operators:
                    if i.getNumber() is None:
                        call = Call(op.getNumber())
                        i.setNumber(call)
                        stdout.append("Call {} ringing for operator {}".format(i.getNumber(), i.getOperator()))
                        op.free()
                        return stdout
                stdout.append("Call {} ringing for operator {}".format(op.getNumber(), operator))
                return stdout
        stdout.append("Operator {} is not busy".format(operator))
        return stdout

    def do_hangup(self, id):
        stdout = []
        for op in self.operators:
            if op.getNumber() == id:
                if op.numberState() == "answered":
                    stdout.append("Call {} finished and operator {} available".format(id, op.getOperator()))
                else:
                    stdout.append("Call {} missed".format(id))
                op.free()
                if len(self.queue) != 0:
                    op.setNumber(self.queue[0])
                    self.queue.remove(self.queue[0])
                    stdout.append("Call {} ringing for operator {}".format(op.getNumber(), op.getOperator()))
                return stdout
        for op in self.queue:
            if op.getId() == id:
                self.queue.remove(op)
                stdout.append("Call {} missed".format(id))
        return stdout

    def do_close(self, arg):
        stdout = []
        stdout.append('closing the queue')
        bye()
        return stdout

    def do_printQueue(self, arg):
        stdout = []
        for op in self.operators:
            stdout.append("Operador: {}\n"
                             "Operator disponivel: {}\n"
                             "Number called: {}\n"
                             "Number state: {}".format(op.getOperator(), op.isAvailable(), op.getNumber(),
                                                         op.numberState()))
        i = 0
        for ca in self.queue:
            stdout.append("Fila: {}\n"
                             "Number called: {}\n"
                             "Number state: {}".format(i, ca.getId(), ca.getState()))
            i += 1
        return stdout
