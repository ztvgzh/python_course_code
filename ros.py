# import the necessary libraries
import zmq

# define the address that will be used for communication
address = "tcp://localhost:5555"

# define the publisher
def publisher():
    # create a ZeroMQ context
    context = zmq.Context()
    # create a publisher socket
    publisher_socket = context.socket(zmq.PUB)
    # bind the publisher socket to the address
    publisher_socket.bind(address)
    # wait for a subscriber to connect
    input("Waiting for subscribers to connect...")
    # send messages
    while True:
        message = input("Enter a message to publish ('exit' to quit): ")
        if message == 'exit':
            break
        publisher_socket.send_string(message)

# define the subscriber
def subscriber(subscriber_id):
    # create a ZeroMQ context
    context = zmq.Context()
    # create a subscriber socket
    subscriber_socket = context.socket(zmq.SUB)
    # connect the subscriber socket to the publisher's address
    subscriber_socket.connect(address)
    # set the subscriber's ID filter
    subscriber_socket.setsockopt_string(zmq.SUBSCRIBE, subscriber_id)
    # receive messages
    while True:
        message = subscriber_socket.recv_string()
        print(f"Subscriber {subscriber_id}: received message '{message}'")

# define the main function to run the code
def main():
    # start the publisher in a separate thread
    import threading
    threading.Thread(target=publisher).start()
    # start two subscribers
    subscriber("subscriber1")
    subscriber("subscriber2")

# run the code
if __name__ == "__main__":
    main