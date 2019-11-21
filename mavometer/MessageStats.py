#!/usr/bin/env python

import sys, collections, time
from builtins import object


class MessageStats(object):
    """Track number of messages, count, frequency (msgs/sec), bandwidth (bytes/sec)"""
    def __init__(self, msgType):
        self.msgType = msgType
        self.nRxMsgs = 0
        self.nRxBytes = 0
        self.frequency = 0.0
        self.bandwidth = 0.0
        self.prevTimestamp = 0.0
        self.initTimestamp = 0.0
        self.lastInterval = 0.0
    '''
    def consume(self, msg, timestamp=0):
        """consume one message"""
        try:
            nBytes = len(msg._msgbuf)

            self.nRxMsgs += 1
            self.nRxBytes += nBytes

            #print(f"MessageStats.update: {msg.keys()}" )
            if timestamp == 0:
                timestamp = time.time()

            if self.initTimestamp == 0:
                self.initTimestamp = timestamp
                
            if self.prevTimestamp:
                diffTime = timestamp - self.prevTimestamp
                #instantaneousFreq = 1.0 / diffTime
                #self.frequency = (self.frequency * self.nRxMsgs + instantaneousFreq) / self.nRxMsgs
                if timestamp != self.initTimestamp:
                    self.frequency = self.nRxMsgs / (timestamp - self.initTimestamp)
                    self.bandwidth = self.nRxBytes / (timestamp - self.initTimestamp)
                self.lastInterval = diffTime

            self.prevTimestamp = timestamp
        except:
            pass
    '''

    def consume(self, msg, timestamp=0):
        """consume one message"""
        nBytes = len(msg._msgbuf)

        self.nRxMsgs += 1
        self.nRxBytes += nBytes

        #print(f"MessageStats.update: {msg.keys()}" )
        if timestamp == 0:
            timestamp = time.time()

        if self.initTimestamp == 0:
            self.initTimestamp = timestamp

        self.prevTimestamp = timestamp


    def update(self):
        """Compute the bandwidth and frequency"""
        try:                
            if self.prevTimestamp:
                self.frequency = self.nRxMsgs / (self.prevTimestamp - self.initTimestamp)
                self.bandwidth = self.nRxBytes / (self.prevTimestamp - self.initTimestamp)

        except:
            pass

if __name__ == '__main__':

    stats = MessageStats("FOO", 0)
    pass
