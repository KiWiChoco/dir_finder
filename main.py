from finder import *
import os
if __name__ == "__main__":
    os.chdir('C:\\Users\\User')
    a = os.getcwd()
    while True:
        #a = os.chdir('C:\\Users\\User')
        start = role(a)
        start.login()