import sys

from consumer import Consumer
from producer import Producer
from monitor import Monitor

print("Main - Initializing")

arguments = sys.argv
number_of_entries = 25
if len(arguments) > 1:
    # blindly assuming this will be the number of entries parameter
    number_of_entries = arguments[1]

print("Main - Creating Monitor")
monitor = Monitor()
print("Main - Creating Consumer")
consumer = Consumer(monitor, number_of_entries)
print("Main - Creating Producer")
producer = Producer(monitor, number_of_entries)

print("Main - Starting Threads")

# start the producer thread
producer.start()
# start the consumer thread
consumer.start()

# join threads to the main thread
producer.join()
consumer.join()


print("Main - Simulation Complete")
