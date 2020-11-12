import tkinter as tk
import requests
from cqfd import *


class Skype(object):
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('skype搜索')
        self.window.geometry('300x150')

    def get_data(self, name):
        data = cqfd(name)
        f = open('{}.txt'.format(name), 'w', encoding='utf8')
        print('数量:', len(data))
        for i in data:
            print(i['username'])
            f.write(i['username'] + '\n')
        f.close()

    def main(self):
        # 创建下拉菜单
        frame = tk.LabelFrame(self.window)
        frame.pack(side='top', fill='both')
        # 拉开距离
        search_ent = tk.Entry(frame, width=10)
        search_ent.grid(row=0, column=1)
        search_but = tk.Button(frame, text='搜索', command=lambda: self.get_data(search_ent.get()))
        search_but.grid(row=0, column=2)

        self.window.mainloop()


if __name__ == '__main__':
    f = Skype()
    f.main()
