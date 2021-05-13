import libscrc
import json
from kafka import KafkaProducer
import os
import logging

class RaphtoryKafkaProxy:

    __instance = None

    def __init__(self):
        if not RaphtoryKafkaProxy.__instance:
            RaphtoryKafkaProxy.__instance = RaphtoryKafkaProxy.__KafkaProxy()

    def getInstance(self):
        return self.__instance

    class __KafkaProxy:

        __producer = None

        def __init__(self):
            self.__connect()

        def __connect(self):
            # insert os.environ.get("KAFKA_HOST")
            try:
                self.__producer = KafkaProducer(bootstrap_servers = ["kafka:9092"], api_version=(0, 10),
                                                value_serializer=lambda x: json.dumps(x).encode('utf-8'))

                print("Connection to kafka server established")
            except Exception as ex:
                logging.error('Exception while connecting Kafka')
                logging.error(str(ex))

        def __publish(self, topic, data):
            try:
                self.__producer.send(topic, str(data)).get(timeout=30)
                self.__producer.flush()
                print('Message published successfully')
                logging.info('Message published successfully')

            except Exception as ex:
                logging.error('Exception in publishing message')
                logging.error(str(ex))

        def addVertex(self, byteVertexName, time, properties):

            data = {'command': 'VertexAdd',
                    'vertexId': libscrc.ecma182(str.encode(byteVertexName)),
                    'msgTime': time,
                    'properties': properties,
                    }
            self.__publish('multiplex-mointor-mainqueue', data)

        def addEdge(self, byteVertexSrcName, byteVertexDstName, time, properties):

            data = {'command': 'EdgeAdd',
                    'srcId': libscrc.ecma182(str.encode(byteVertexSrcName)),
                    'dstId': libscrc.ecma182(str.encode(byteVertexDstName)),
                    'msgTime': time,
                    'properties': properties,
                    }
            self.__publish('multiplex-monitor-mainqueue', data)
