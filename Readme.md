BackEnd Task-

Develop an API for accepting ride data.
This API should be able to accept the requests and respond to the clients quickly.

Approach- 

Approach i am taking to solve this problem is using Queuing. 
Take in the requests and push them into the queue and respond to the client.
This part of the system which will push into the queue is Producer.
The part of the system which will fetch from the queue and do the processing is called Consumer which will take the data from Queue and push into the PostgreSQL data base.
This solution follows Producer-Consumer pattern.

For queuing RabbitMQ can be used.
The server for accepting requests can be made using Flask.
Producer and consumer can be made using Pika(AMPQ client library).
psycopg2 can be used for working with PostgreSQL.