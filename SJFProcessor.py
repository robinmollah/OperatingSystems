from processor import Processor
import copy

class SJFProcessor(Processor):
    total_waiting_time = 0
    queue = []
    ready = []

    def calculate_times(self):
        self.processes.sort(key=lambda pr: (pr.arrivalTime, pr.burstTime))
        self.ready = copy.deepcopy(self.processes)
        while self.ready or self.queue:
            if not self.queue:
                process = self.ready.pop(0)
                self.queue.append(process)
            else:
                self.queue.sort(key=lambda pr: pr.burstTime)
                process = self.queue.pop(0)
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