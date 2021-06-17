from . import socket

@socket.on( "connect" )
def connect():
    print( "A user has connected to our socket" )

@socket.on( "disconnect" )
def disconnected():
    print( "Socket has been disconnected" )

