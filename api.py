#ALL PROGRAM FUNCTIONS ARE IN THIS FILE
import numpy.random


def api(flipamount): #todo add bias coin system
    head = 0
    tail = 0
    while flipamount >0:
        hort = numpy.random.randint(0, 50)
        if hort > 25:
            head = head + 1

        elif hort < 25:
            tail = tail + 1
        flipamount = flipamount - 1
    return head, tail