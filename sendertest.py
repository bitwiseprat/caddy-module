import pika
parameters = pika.URLParameters('amqp://bitwise:bitwise2017@52.8.27.199:5672') #URL GOES HERE


connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.basic_publish('',
                    'my_queue',
                    body ='Test for Error', 
                    )

                                                    # creating connection with the sender queue , and sending the data
connection.close()
