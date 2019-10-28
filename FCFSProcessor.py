from processor import Processor


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