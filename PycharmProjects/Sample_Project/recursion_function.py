import os

path = 'C:\Users\mkullampalay\PycharmProjects\Sample_Project'

print "Given Path: %s", path


def print_directory_contents(sPath):
    # type: (object) -> object
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath, sChild)
        if os.path.isdir(sChildPath):
            print "Child Path"
            print_directory_contents(sChildPath)
        else:
            print sChildPath


print_directory_contents(path)
