import pika
import json
import psycopg2
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
dbconnection = psycopg2.connect(user="sysadmin",
                                  password="pynative@#29",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres_db")
cursor = dbconnection.cursor()
channel.queue_declare(queue='hello')
postgres_insert_query = """ INSERT INTO ride (from_lat, from_long, to_lat, to_long, time) VALUES (%s,%s,%s, %s, %s)"""

def callback(ch, method, properties, body):
    data = json.loads(body)    
    record_to_insert = (data['from_lat'], data['from_long'], data['to_lat'], d['to_long'], data['time'])
    cursor.execute(postgres_insert_query, record_to_insert)
    dbconnection.commit()

channel.basic_consume(
    queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()