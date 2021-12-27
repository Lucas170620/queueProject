import json
import cmd
from twisted.internet import reactor, protocol

class Client_shell(cmd.Cmd):
    intro = "Welcome to the Queue"
    prompt = "(queue) "

    def do_call(self,id):
        cmd_raw = {"command": "call", "id": str(id)}
        cmd_json = json.dumps(cmd_raw)
        f = QueueFactory(cmd_json)
        reactor.callFromThread(reactor.connectTCP, "localhost", 5678, f)

    def do_answer(self,id):
        cmd_raw = {"command": "answer", "id": str(id)}
        cmd_json = json.dumps(cmd_raw)
        f = QueueFactory(cmd_json)
        reactor.callFromThread(reactor.connectTCP, "localhost", 5678, f)

    def do_reject(self,id):
        cmd_raw = {"command": "reject", "id": str(id)}
        cmd_json = json.dumps(cmd_raw)
        f = QueueFactory(cmd_json)
        reactor.callFromThread(reactor.connectTCP, "localhost", 5678, f)

    def do_hangup(self,id):
        cmd_raw = {"command": "hangup", "id": str(id)}
        cmd_json = json.dumps(cmd_raw)
        f = QueueFactory(cmd_json)
        reactor.callFromThread(reactor.connectTCP, "localhost", 5678, f)

    def do_printQueue(self,arg):
        cmd_raw = {"command": "printQueue", "id": ""}
        cmd_json = json.dumps(cmd_raw)
        f = QueueFactory(cmd_json)
        reactor.callFromThread(reactor.connectTCP, "localhost", 5678, f)

    def do_close(self, arg):
        cmd_raw = {"command": "close", "id": ""}
        cmd_json = json.dumps(cmd_raw)
        f = QueueFactory(cmd_json)
        reactor.callFromThread(reactor.connectTCP, "localhost", 5678, f)

class QueueClient(protocol.Protocol):

    def connectionMade(self):
        self.transport.write(self.factory.command.encode())

    def dataReceived(self, data):
        response = json.loads(data.decode())
        for x in response["response"]: print (x)

    def connectionLost(self, reason):
        print("connection lost")
        exit()

class QueueFactory(protocol.ClientFactory):
    protocol = QueueClient

    def __init__(self, command):
        self.command = command

    def clientConnectionFailed(self, connector, reason):
        print("Connection failed - goodbye!")
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print("Connection lost - goodbye!")
        reactor.stop()