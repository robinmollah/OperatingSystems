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


class FCFSProcessor(Processor):
    def calculate_times(self):
        total_waiting_time = 0
        self.elapsed_time = 0
        for process in self.processes:
            process.waitingTime = self.elapsed_time
            total_waiting_time += process.waitingTime
            self.elapsed_time += process.burstTime
            process.turnaround_time = self.elapsed_time
        self.avg_waiting_time = total_waiting_time / len(self.processes)


class SJFProcessor(Processor):
    total_waiting_time = 0
    queue = []
    ready = []

    def calculate_times(self):
        self.processes.sort(key=lambda pr: (pr.arrivalTime, pr.burstTime))
        self.ready = copy.deepcopy(self.processes)
        while self.ready or self.queue:
            if not self.queue:
                print("Queue is empty. Enqueuing: " + str(self.elapsed_time))
                process = self.ready.pop(0)
                self.queue.append(process)
                print("Enqueued: P" + str(process.pid))
            else:
                print("On queue: ")
                self.printProcessList(self.queue)
                self.queue.sort(key=lambda pr: pr.burstTime)
                process = self.queue.pop(0)
                print("Running: P" + str(process.pid))
                process = self.get_process(process.pid)
                process.waitingTime = self.elapsed_time - process.arrivalTime
                self.elapsed_time += process.burstTime
                process.turnaround_time = self.elapsed_time - process.arrivalTime
                # enqueue meanwhile arrived processes
                copy_ready = copy.copy(self.ready)
                for pro in copy_ready:
                    if pro.arrivalTime < self.elapsed_time:
                        self.queue.append(pro)
                        self.ready.remove(pro)
                self.printProcessList(self.queue)


number_of_process = input("Number of processes: ")
has_arrival_time = bool(input("Has arrival time? "))

processor = SJFProcessor()

for x in range(int(1), int(number_of_process) + 1):
    burst_time = int(input("PID {} Burst Time: ".format(x)))
    if has_arrival_time:
        arrival_time = int(input("PID {} Arrival TIme: ".format(x)))
        processor.add(Process(pid=x, burst_time=burst_time, arrival_time=arrival_time))
    else:
        processor.add(Process(pid=x, burst_time=burst_time))

processor.calculate_times()
print("Avg waiting time: " + str(processor.get_avg_waiting_time()))
# processor.processes.sort(key=lambda process: process.arrivalTime)
for y in processor.processes:
    print(y.tostring())
