import os
import signal
import threading

# Vulnerable opensources
import certifi
import priority
import requests
import scrapy
import urllib3
import yaml
from cryptography.fernet import Fernet
from loguru import logger
from lxml import etree
from twisted.names import client

# Set up a flag to track whether the loop should continue running
running = True
animals_yaml = """
    - 'lion'
    - 'dog'
    - 'cat'
    """
xml = '<a xmlns="test"><b xmlns="test"/></a>'

# Set up a signal handler to catch the kill signal
def signal_handler(sig, frame):
    # Set the running flag to False
    print("Got kill signal... exiting")
    global running
    running = False


signal.signal(signal.SIGTERM, signal_handler)


def parse(self, response):
    # trunk-ignore(flake8/F841)
    page = response.url.split("/")[-2]


def run_loop():
    for i in range(10):
        # Open a file for writing
        print("Opening file")
        fd = os.open("/tmp/test.txt", os.O_WRONLY | os.O_CREAT)

        # Write to the file
        print("Writing to file")
        os.write(fd, b"Hello, world!\n")

        # Close the file
        print("closing file")
        os.close(fd)

        print("Opens URL")
        print(urllib3.__version__)
        http = urllib3.PoolManager()
        # trunk-ignore(flake8/F841)
        response = http.request("GET", "http://www.google.com")

        print("Opens URL with CA")
        # trunk-ignore(flake8/F841)
        cafile = certifi.where()

        print("Requests URL")
        print(requests.__version__)
        # trunk-ignore(flake8/F841)
        x = requests.get("http://www.google.com")

        print("Loads YAML")
        # trunk-ignore(flake8/F841)
        names = yaml.safe_load(animals_yaml)

        print("Generate Fernet key")
        Fernet.generate_key()

        print("Uses logging")
        # trunk-ignore(flake8/F541)
        logger.info(f"Hello World")

        print("Uses scrapy")
        url = "https://quotes.toscrape.com/page/1/"
        scrapy.Request(url=url, callback=parse)

        print("Using priority")
        # trunk-ignore(flake8/F841)
        p = priority.PriorityTree()

        print("Parsing XML")
        # trunk-ignore(flake8/F841)
        root = etree.fromstring(xml)

        print("Using Twisted")
        # trunk-ignore(flake8/F841)
        d = client.lookupAddress("http://www.google.com")


## While kill signal is not sent to container run loop

while running:
    threads = []
    for i in range(10):
        t = threading.Thread(target=run_loop)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()