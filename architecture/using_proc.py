import multiprocessing
import time
def daemonProcess():
    print("Starting my Daemon Process")
    print("Daemon process started:{}".format(multiprocessing.current_process()))
    time.sleep(3)
    print("Daemon process terminating")
    print("Main process: {}".format(multiprocessing.current_process()))

if __name__ == '__main__':
    # multiprocessing runs a SEPARATE copy of Python for EVERY new process

    myProcess = multiprocessing.Process(target=daemonProcess)
    myProcess.daemon = True
    myProcess.start() # we have a separate instsance of Python with its own separate memory
    print("We can carry on as per usual and our daemon will continue to execute")
    time.sleep(11)