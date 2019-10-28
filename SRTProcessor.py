from processor import Processor
import copy


class SRTProcessor(Processor):
    ready = []
    queue = []
    running = None

    def calculate_times(self):
        self.ready = copy.deepcopy(self.processes)
        self.running = self.ready[0]
        self.queue.append(self.running)
        while self.queue:
            r_process = self.running
            print("Running process: " + str(r_process.pid))
            next_arriving_process = self.next_arriving_process(r_process)
            if next_arriving_process:
                self.queue.append(next_arriving_process)
                next_arrival_time = next_arriving_process.arrivalTime
                r_process.burstTime -= next_arrival_time - self.elapsed_time
                self.get_process(r_process.pid).waitingTime = self.elapsed_time - r_process.arrivalTime
                self.elapsed_time += next_arrival_time - self.elapsed_time
            else:
                mainProcess = self.get_process(r_process.pid)
                alreadyProcessed = mainProcess.burstTime - r_process.burstTime
                # FIXME
                mainProcess.waitingTime = self.elapsed_time - (r_process.arrivalTime + alreadyProcessed)
                self.elapsed_time += r_process.burstTime
                self.ready.remove(self.queue.pop(0))
                for pr in self.ready:
                    if pr.arrivalTime == self.elapsed_time:
                        self.queue.append(pr)
            if self.ready:
                self.running = self.get_shortest(self.queue)

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

    def get_shortest(self, queue):
        if not queue:
            self.ready.sort(key=lambda k: k.burstTime)
            return self.ready[0]
        else:
            self.queue.sort(key=lambda k: k.burstTime)
            return self.queue[0]
        pass

    def next_arriving_process(self, r_process):
        for pr in self.ready:
            if pr.pid == r_process.pid:
                continue
            if self.elapsed_time < pr.arrivalTime < self.elapsed_time + r_process.burstTime:
                return pr
        pass
