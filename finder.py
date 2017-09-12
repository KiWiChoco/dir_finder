import os


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

        if self.input_path == '..':
            os.chdir("..")
            print(os.getcwd())

        if os.path.isdir(self.input_path):
            os.chdir(a + '\\' + self.input_path)
            #print(os.getcwd())
            a = os.getcwd()
            print(a)
            print(os.listdir(a))
            start = role(a)
            start.login()

    def search_file(self,a):
        print(self.curr_path)

    def delete_directory(self,a):
        pass

    def quit(self,a):
        print(a)