import pika
from flask import Flask, request
import json
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
app = Flask(__name__)
channel.queue_declare(queue='hello')
@app.route("/ride_data", methods=['POST'])
def ride_data():
    from_lat = request.form['from_lat']
    from_long = request.form['from_long']
    to_lat = request.form['to_lat']
    to_long = request.form['to_long']
    time = request.form['time']
    d = {"from_lat":from_lat, "from_long":from_long, "to_lat":to_lat, "to_long":to_long, "time":time}
    channel.basic_publish(exchange='', routing_key='hello', body=json.dumps(d))
    return json.dumps({'status':'success'})

if __name__ == "__main__":
    app.run(port=5000)