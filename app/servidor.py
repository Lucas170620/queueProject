import json
from twisted.internet import reactor, protocol
from app.queue import Queue

class Servidor(protocol.Protocol):
    app = Queue()

    def dataReceived(self, data):
        print('received: ' + data.decode())
        message = data.decode()
        call = json.loads(message)
        case = call["command"]
        if case == "call":
            message = self.app.do_call(int(call["id"]))
        elif case == "answer":
            message = self.app.do_answer(call["id"])
        elif case == "reject":
            message = self.app.do_reject(call["id"])
        elif case == "hangup":
            message = self.app.do_hangup(int(call["id"]))
        elif case == "close":
            message = self.app.do_close(0)
        elif case == "printQueue":
            message = self.app.do_printQueue(0)
        else:
            message = ["command not accepted"]

        response_raw = {"response": message}
        response_json = json.dumps(response_raw)
        self.transport.write(response_json.encode())
