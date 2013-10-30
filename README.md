quicksend
=========

Tiny utility for sending files insecurely on your local network

The idea is that to start a server, you should run

```
$ quick receive [port]
```

and then people on your local network can send you a filename using 

```
$ quick send your_ip[:port] filename
```

TODO: make it possible to send multiple files. 
