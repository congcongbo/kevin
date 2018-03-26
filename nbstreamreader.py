# h/t http://eyalarubas.com/python-subproc-nonblock.html

from threading import Thread
from Queue import Queue, Empty
import time

class NonBlockingStreamReader:

    def __init__(self, stream):
        '''
        stream: the stream to read from.
                Usually a process' stdout or stderr.
        '''

        self._s = stream
        self._q = Queue()

        def _populateQueue(stream, queue):
            '''
            Collect lines from 'stream' and put them in 'queue'.
            '''

            while True:
                line = stream.readline()
                if line:
                    queue.put(line)
                    print line
                else:
                    raise UnexpectedEndOfStream
                time.sleep(0.1)

        self._t = Thread(target = _populateQueue,
                args = (self._s, self._q))
        self._t.daemon = True
        self._t.start() #start collecting lines from the stream

    def readline(self, timeout = None):
        # return None
        try:
            return  self._q.get(block = timeout is not None,
                    timeout = timeout)
        except Empty:
            return None

class UnexpectedEndOfStream(Exception): pass