from enum import Enum


class State(Enum):
    RUNNING = 1
    TERMINATED = 2
    READY = 3
    ONQUEUE = 4


class Process:
    pid = 0
    burstTime = 0
    waitingTime = 0
    arrivalTime = 0
    turnaround_time = 0
    state = State.READY

    def __init__(self, *args, **kwargs):
        self.pid = kwargs['pid']
        self.burstTime = kwargs['burst_time']
        if 'arrival_time' in kwargs:
            self.arrivalTime = kwargs['arrival_time']

    def tostring(self):
        return "PID {}, Burst time: {}, Waiting time: {}, Arrival Time: {}, Turn around time: {}".format(self.pid,
                                                                                                         self.burstTime,
                                                                                                         self.waitingTime,
                                                                                                         self.arrivalTime,
                                                                                                         self.turnaround_time)
