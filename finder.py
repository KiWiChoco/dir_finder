import os


class role():
    # os.chdir('C:\\Users\\User')

    def __init__(self, a):
        # self.os.chdir('C:\\Users\\User')
        self.curr_path = a

    def login(self):
        # os.chdir('C:\\Users\\User')
        # print(os.environ['HOMEPATH'])
        # curr_path = os.getcwd()
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
        #eval('self.' + self.role_menu + '(' + self.curr_path + ')')

    # login()
    # a = change_directory()
    # a=  delete_directory()

    def change_directory(self, a):
        print("current directory : ", self.curr_path)
        # print(os.path.isdir(a))

        # if os.path.isdir(a):

        print("enter '..' for the parent dir, and q to exit ")
        self.input_path = input('enter a directory or path : ')

        if not os.path.isdir(self.input_path):
            print('That is wrong dir')

        if self.input_path == '..':
            os.chdir("..")
            print(os.getcwd())

        if os.path.isdir(self.input_path):
            os.chdir(a + '\\' + self.input_path)
            print(os.getcwd())
            a = os.getcwd()

            print(os.listdir(a))

    def search_file(self,a):
        pass

    def delete_directory(self,a):
        pass

    def quit(self,a):
        print(a)