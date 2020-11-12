import tkinter as tk
import requests


class Skype(object):
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('skype搜索')
        self.window.geometry('300x150')
    def get_data(self,name):
        url = 'https://skypegraph.skype.com/v2.0/search?searchString={}&requestId=时间戳&locale=zh-CN&sessionId=自己的sessionID&resultmaxcount=100'.format(
            name
            )
        headers = {
                    # 自己的信息
                    }

        resp = requests.get(url, headers=headers)
        data = resp.json()
        f = open('skype.txt', 'w', encoding='utf8')
        print('数量:', len(data['results']))
        for i in data['results']:
            print(i['nodeProfileData']['skypeId'])
            f.write(i['nodeProfileData']['skypeId'] + '\n')
        f.close()
    def main(self):
        # 创建下拉菜单
        frame = tk.LabelFrame(self.window)
        frame.pack(side='top', fill='both')
        # 拉开距离
        tk.Label(frame, width=40).grid(row=0, column=3)
        search_ent = tk.Entry(frame, width=10)
        search_ent.grid(row=0, column=1)
        search_but = tk.Button(frame, text='搜索', command=lambda: self.get_data(search_ent.get()))
        search_but.grid(row=0, column=2)
        self.window.mainloop()

if __name__ == '__main__':
    f = Skype()
    f.main()