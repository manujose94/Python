import selectors
import sys
from time import time
 
 
def process_input(stream):
    text = stream.readline()
    n = text.strip()
    print(n)
 
def print_hello():
    print("{} - Hello world!".format(int(time())))
 
 
def main():
    selector = selectors.DefaultSelector()
    # Register the selector to poll for "read" readiness on stdin
    selector.register(sys.stdin, selectors.EVENT_READ)
    last_hello = 0  # Setting to 0 means the timer will start right away
    while True:
        # Wait at most 100 milliseconds for input to be available
        for event, mask in selector.select(0.1):
            process_input(event.fileobj)
        if time() - last_hello > 3:
            last_hello = time()
            print_hello()
 
 
if __name__ == '__main__':
    main()

#https://sahandsaba.com/understanding-asyncio-node-js-python-3-4.html
#https://www.reddit.com/r/learnprogramming/comments/4l6i79/nodejs_python_two_way_communication_via_stdin/

#https://medium.com/@HolmesLaurence/integrating-node-and-python-6b8454bfc272
