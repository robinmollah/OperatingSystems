from processor import Processor
import copy

class SRTProcessor(Processor):
    ready = []
    queue = []
    running = None

    def calculate_times(self):
        self.ready = copy.deepcopy(self.processes)
        while self.ready:
            if not self.running:
                self.running = self.ready[0]
                self.queue.append(self.running)
            else:
                r_process = self.running
                arrivals_in_burst_time = self.get_arrivals(r_process)
                if arrivals_in_burst_time:
                    self.queue.extend(arrivals_in_burst_time)
                    next_arrival_time = arrivals_in_burst_time[0].arrivalTime
                    if next_arrival_time < self.elapsed_time + r_process.burstTime:
                        r_process.burstTime -= next_arrival_time - self.elapsed_time
                        self.get_process_queue(r_process.pid).burstTime = r_process.burstTime
                        self.get_process(r_process.pid).waitingTime = self.elapsed_time - r_process.arrivalTime
                        self.elapsed_time += next_arrival_time - self.elapsed_time
                    else:
                        self.queue.pop(0).burstTime = 0
                else:
                    mainProcess = self.get_process(r_process.pid)
                    alreadyProcessed = mainProcess.burstTime - r_process.burstTime
                    # FIXME
                    mainProcess.waitingTime = max(0, self.elapsed_time - r_process.arrivalTime - alreadyProcessed)
                    self.elapsed_time += r_process.burstTime
                    self.ready.pop(0)
                if self.ready:
                    self.running = self.get_shortest()

    def get_process_queue(self, pid):
        for pr in self.queue:
            if pr.pid == pid:
                return pr
        pass

    def get_arrivals(self, r_process):
        result = []
        for pr in self.ready:
            if r_process.burstTime + self.elapsed_time > pr.arrivalTime > self.elapsed_time:
                result.append(pr)
        return result
        pass

    def get_shortest(self):
        self.ready.sort(key=lambda k: k.burstTime)
        return self.ready[0]
        pass
