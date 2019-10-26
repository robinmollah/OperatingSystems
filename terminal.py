import processor as P


number_of_process = input("Number of processes: ")
has_arrival_time = bool(input("Has arrival time? Press enter to skip "))

scheduling_method = int(input("Scheduling method:\n"
                              "1. FCFS\n"
                              "2. SJF Non preemptive\n"
                              "3. SJF Preemptive\n"))
if scheduling_method == 1:
    processor = P.FCFSProcessor()
elif scheduling_method == 2:
    processor = P.SJFProcessor()
else:
    processor = P.SRTProcessor()

for x in range(int(1), int(number_of_process) + 1):
    burst_time = int(input("PID {} Burst Time: ".format(x)))
    if has_arrival_time:
        arrival_time = int(input("PID {} Arrival TIme: ".format(x)))
        processor.add(P.Process(pid=x, burst_time=burst_time, arrival_time=arrival_time))
    else:
        processor.add(P.Process(pid=x, burst_time=burst_time))

processor.calculate_times()
print("Avg waiting time: " + str(processor.get_avg_waiting_time()))
# processor.processes.sort(key=lambda process: process.arrivalTime)
for y in processor.processes:
    print(y.tostring())
