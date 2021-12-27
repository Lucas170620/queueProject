from twisted.internet import reactor, protocol
from app.servidor import Servidor
def runServer():
    factory = protocol.Factory()
    factory.protocol = Servidor
    reactor.listenTCP(5678, factory)
    reactor.run()

if __name__=="__main__":
    runServer()