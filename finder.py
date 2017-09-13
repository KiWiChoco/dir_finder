import os
import glob
import sys
import shutil

class role():

    def __init__(self, a):
        self.curr_path = a

    def login(self):

        print("Welcome")
        print(" 1 : change directory\n"
              " 2 : search file\n"
              " 3 : delete directory or file\n"
              " 4 : quit")

        do = int(input("please input number want to do : "))

        switcher = {
            1: self.change_directory,
            2: self.search_file,
            3: self.delete_directory,
            4: self.quit
        }

        role_menu = switcher.get(do)
        role_menu(self.curr_path)


    def change_directory(self, a):
        print("current directory : ", self.curr_path)


        print("enter '..' for the parent dir, and q to exit ")
        self.input_path = input('enter a directory or path : ')

        if not os.path.isdir(self.input_path):
            print('That is wrong dir')
            a = os.getcwd()
            start = role(a)
            start.login()

        if self.input_path == '..':
            os.chdir("..")
            print(os.getcwd())

        if os.path.isdir(self.input_path):
            os.chdir(a + '\\' + self.input_path)
            a = os.getcwd()
            #print(a)
            #print(os.listdir(a))
            try:
                os.listdir(a)
                print(os.listdir(a))
            except PermissionError:
                os.chdir("..")
                ch_path = os.getcwd()
                print(os.listdir(ch_path))

            start = role(a)
            start.login()

    def search_file(self,a):
        self.input_path = input('enter a directory for searching (enter q to exit) : ')
        if self.input_path == 'q':
            start = role(a)
            start.login()
        else:
            files = glob.iglob(a + '\\' + '**' + '\\' + '*' + self.input_path + '*' + '\\' + '*', recursive=True)
            for file in files:
                print(file)
            start = role(a)
            start.search_file(a)

    def delete_directory(self,a):
        self.input_dir = input('enter a directory or file name want to delete (enter q to exit) : ')

        if self.input_dir == 'q':
            start = role(a)
            start.login()
        else: pass

        try:
            os.rmdir(a + '\\' + self.input_dir)
            print('delete clearly')
            self.delete_directory(a)

        except OSError:
            self.input_select = input('enter y or n (y is delete, n is dont delete : ')
            if self.input_select == 'y':
                shutil.rmtree(a + '\\' + self.input_dir)
                self.delete_directory(a)
            else:
                self.delete_directory(a)




    def quit(self,a):
        sys.exit()