import os
print("Waiting")
pro= os.wait()
print("Child process of %d is executed" % (pro[0]))
print("Parent process of %d is executed" % (os.getpid()))
print("The parent process is", (os.getpid()))