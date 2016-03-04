# coding=utf-8
from thrift.server.TServer import TSimpleServer, TThreadedServer, TThreadPoolServer
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TJSONProtocol, TCompactProtocol
from users import userservice


class ThriftServiceHandler:
    def __init__(self):
        pass

    def ping(self):
        print 'ping'
        return 'pong'

    def inc(self, value):
        print 'inc'
        return value + 1


def server(host, port, transport_type='buffered', protocol_type='binary', server_type='simple'):
    handler = ThriftServiceHandler()
    processor = ThriftService.Processor(handler)
    transport = TSocket.TServerSocket(host, port)

    tfactory_map = {
        'buffered': TTransport.TBufferedTransportFactory(),
        'framed': TTransport.TFramedTransportFactory()
    }
    pfactory_map = {
        'binary': TBinaryProtocol.TBinaryProtocolFactory(),
        'json': TJSONProtocol.TJSONProtocolFactory(),
        'compact': TCompactProtocol.TCompactProtocolFactory()
    }
    tfactory = tfactory_map[transport_type]
    pfactory = pfactory_map[protocol_type]

    server_map = {
        'simple': TSimpleServer,
        'threaded': TThreadedServer,
        'pool': TThreadPoolServer
    }
    thrift_server = server_map[server_type](processor, transport, tfactory, pfactory)
    print 'Starting server at %s:%d, transport: %s, protocol: %s, type: %s' \
          % (host, port, transport_type, protocol_type, server_type)
    thrift_server.serve()


def client(host, port, transport_type='buffered', protocol_type='binary'):
    transport_map = {
        'buffered': TTransport.TBufferedTransport,
        'framed': TTransport.TFramedTransport
    }
    protocol_map = {
        'binary': TBinaryProtocol.TBinaryProtocol,
        'json': TJSONProtocol.TJSONProtocol,
        'compact': TCompactProtocol.TCompactProtocol
    }

    socket = TSocket.TSocket(host, port)
    transport = transport_map[transport_type](socket)
    protocol = protocol_map[protocol_type](transport)
    transport.open()

    thrift_client = userservice.Client(protocol)

    pong = thrift_client.ping()
    print 'ping => %s' % pong

    # user = thrift_client.login('13699851562', '000999', '')
    # user = thrift_client.login('haizi.zh@qq.com', '123456', '')
    try:
        # user = thrift_client.login('13699851562', '000999', '')
        # user = thrift_client.login('15313380327', '123456', '')
        # print user.secretKey
        # u2 = thrift_client.loginByOAuth('011331690e7c6ccee1e8bee05fbac255', 'weixin')

        # print thrift_client.login('haizi.zh@qq.com', '123456', 'app')
        from users import ttypes

        print thrift_client.login('10000000000', '69982400', 'app')
        user = thrift_client.getUserById(100056, [ttypes.UserInfoProp.PROMOTION_CODE], 100056)
        print user
        # print thrift_client.login('15313380327', '123456', 'app')
        # print thrift_client.acceptContactRequest(u'56989c80b36c28ff3a0cfa36')
        # thrift_client.isContact(100012, 100056)
    except Exception, e:
        print e


def main():
    import argparse

    parser = argparse.ArgumentParser(description='ThriftPy tutorials')
    parser.add_argument('mode', choices=['server', 'client'], help='Whether to start a server or a client')
    parser.add_argument('--host', type=str, default='localhost', help='The address of the thrift server')
    parser.add_argument('--port', type=int, default=8473, help='The port of the thrift server')
    parser.add_argument('--transport', '-t', type=str, choices=['framed', 'buffered'], default='buffered',
                        help='The type of the transport')
    parser.add_argument('--protocol', '-p', type=str, choices=['binary', 'json', 'compact'], default='binary',
                        help='The type of the protocol')
    parser.add_argument('--server-type', '-s', type=str, choices=['simple', 'threaded', 'pool'], default='simple',
                        help='Type of the thrift server')

    args = parser.parse_args()

    if args.mode == 'server':
        server(args.host, args.port, args.transport, args.protocol, args.server_type)
    elif args.mode == 'client':
        client(args.host, args.port, args.transport, args.protocol)


if __name__ == '__main__':
    main()
