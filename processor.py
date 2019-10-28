from process import Process
import copy


class Processor:
    processes = []
    avg_waiting_time = 0
    elapsed_time = 0

    def __init__(self):
        pass

    def add(self, process):
        self.processes.append(process)

    def get_process(self, pid):
        for pr in self.processes:
            if pr.pid == pid:
                return pr
        pass

    def printProcessList(self, queue):
        for pr in queue:
            print("P" + str(pr.pid) + ", ")
        pass

    def get_avg_waiting_time(self):
        total_waiting_time = 0
        for pr in self.processes:
            total_waiting_time += pr.waitingTime
        return total_waiting_time / len(self.processes)


