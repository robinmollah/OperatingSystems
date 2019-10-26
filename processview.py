import tkinter as tk


class ProcessView(tk.Frame):
    index = 0
    burstTime = 0
    arrivalTime = 0

    # Static
    avg_waitingTimeFCFS = 0
    avg_waitingTimeSJFNP = 0
    avg_waitingTimeSJFP = 0
    elapsedTime = 0

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent)
        ProcessView.index += 1
        self.pidLabel = tk.Label(self, text="PID " + str(ProcessView.index))
        self.pidLabel.grid(row=0, column=0, sticky=tk.W, padx=8)
        self.burstTimeSV = tk.StringVar()
        self.burstTimeSV.trace("w", self.set_burst_time)
        # TODO only allow numbers
        self.pBurstTime = tk.Entry(self, textvariable=self.burstTimeSV)
        self.pBurstTime.grid(row=0, column=1, padx=8)
        self.pArrivalTime = tk.Entry(self)
        self.pArrivalTime.grid(row=0, column=2, sticky=tk.E, padx=8)

    def set_burst_time(self, *args):
        print(args)
        self.burstTime = self.burstTimeSV.get()
