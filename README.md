# tutorial-thrift-py
Tutorials of Thrift clients and servers in Python

## Command line arguments

* `server`/`client`: whether to start a server or connect to an existing one
* `host`: the address of the Thrift server, default is `localhost`
* `port`: the port of the Thrift server, default is `8473`
* `transport`: the transport type, default is `buffered`
* `protocol`: the protocol type, default is `binary`
* `server-type`: the type of the Thrift server, default is `simple`

## Usage

### As a server

```
python main.py server --transport framed --server-type pool
```

### As a client

```
python main.py client --transport framed
```
