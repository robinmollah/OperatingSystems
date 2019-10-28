from SRTProcessor import SRTProcessor
from process import Process

processor = SRTProcessor()
processor.add(Process(pid=1, burst_time=7, arrival_time=0))
processor.add(Process(pid=2, burst_time=4, arrival_time=2))
processor.add(Process(pid=3, burst_time=1, arrival_time=4))
processor.add(Process(pid=4, burst_time=4, arrival_time=5))
processor.calculate_times()
print("Average waiting time: " + str(processor.get_avg_waiting_time()))
assert processor.get_avg_waiting_time() == 3.0, "Average time should 3.0"
assert processor.get_process(1).waitingTime == 9, "Waiting time should be 9"
for y in processor.processes:
    print(y.tostring())
