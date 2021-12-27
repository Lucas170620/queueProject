from twisted.internet import reactor, protocol
from app.client_shell import Client_shell

def runClient():
    reactor.callInThread(Client_shell().cmdloop)
    reactor.run()

if __name__=="__main__":
    runClient()