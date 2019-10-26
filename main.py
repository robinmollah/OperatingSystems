from tkinter import *
from processview import ProcessView

root = Tk()
# Window configurations
root.title("Operating Systems")
root.minsize(500, 500)

processes = []

# Header
headerFrame = Frame(root)
pIdLabel = Label(headerFrame, text="Process ID")
pIdLabel.grid(row=0, column=0, sticky=W, padx=8)
pBurstTime = Label(headerFrame, text="Burst time")
pBurstTime.grid(row=0, column=1, padx=8)
pArrivalTime = Label(headerFrame, text="Arrival time")
pArrivalTime.grid(row=0, column=2, sticky=E, padx=8)
headerFrame.grid(row=1, column=0, columnspan=3)

process1 = ProcessView(root)
process1.grid(row=ProcessView.index + 1, column=0, columnspan=3)
processes.append(process1)


def add_process():
    new_process = ProcessView(root)
    processes.append(new_process)
    new_process.grid(row=ProcessView.index + 1, column=0, columnspan=3)
    addProcessButton.grid(row=ProcessView.index + 2, column=0, columnspan=3)
    print("BurstTIme: " + str(processes[-2].burstTime))
    pass


addProcessButton = Button(root, text="Add Process", command=add_process)
addProcessButton.grid(row=ProcessView.index + 2, column=0, columnspan=3)


def remove_process():
    # TODO remove process
    print("This function is not yet implemented")
    pass


removeProcessButton = Button(root, text="Remove Process", command=remove_process)

methods = {'FCFS', 'SJF-Non preemptive', 'SJF-Preemtive'}
ddvar = StringVar(root)
ddvar.set('FCFS')
selectMethod = OptionMenu(root, ddvar, *methods)
selectMethod.grid(row=ProcessView.index + 3, column=0, columnspan=3)



# centers alignment
# root.grid_rowconfigure(0, weight=1)
# root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(2, weight=1)

root.mainloop()
