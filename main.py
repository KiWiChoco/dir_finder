from finder import *
import os
if __name__ == "__main__":
    os.chdir('C:\\Users\\User')
    a = os.getcwd()

    start = role(a)
    start.login()