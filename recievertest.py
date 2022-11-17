import pika
parameters = pika.URLParameters('amqp://bitwise:bitwise2017@52.8.27.199:5672') #URL GOES HERE

# connection creation
connection = pika.BlockingConnection(parameters)
channel = connection.channel()          

method , properties , body = channel.basic_get('my_queue')      # receiving data from the sender queue 

#message = format(body)
#message = message[2:-1]     #formatting data for removing extra characters added by rabbitmq

print(message) 
