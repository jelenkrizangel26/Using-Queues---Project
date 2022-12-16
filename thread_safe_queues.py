import argparse
from queue import LifoQueue, PriorityQueue, Queue

queue_types = {
    "fifo": Queue,
    "lifo": LifoQueue,
    "heap": PriorityQueue
}

def main(args):
    buffer = queue_types[args.queue]()