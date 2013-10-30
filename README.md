quicksend
=========

Tiny utility for sending files insecurely on your local network

The idea is that to start a server, you can run

```
$ quick receive [port]
```

and then people on your local network can send you a file using 

```
$ quick send your_ip[:port] filename
```

TODO: 

* make it possible to send more than one file at once
* don't read the whole file into memory before sending it
