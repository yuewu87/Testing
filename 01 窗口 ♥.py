
import tkinter

# =========================创建一个主窗口 添加元素========================
win = tkinter.Tk()    # win 可自定义

# 标题
win.title("♥哈～♥哈～")

# 窗口大小+窗口位置xy
win.geometry("400x300+650+250")

# 改图标，输地址
win.iconbitmap("D:\python1\窗口\素材\icon.ico")

# 窗口背景颜色设置  win["background"] = "英文"或“十六进制”
win.configure(bg="pink")

# 窗口透明度：0-1， Df = R， 0：透明 1：不透明
win.attributes("-alpha", 0.9)

# ==================label函数，可显示文本， 图片==================
label = tkinter.Label(win, text="♥だい ——すきだよ♥", bg="pink", font=("Arial", 12), fg="purple",  width=15, height=2)
#                     目标  内容                  背景颜色     文本                 字体颜色       宽        高

label.pack()
# label.place()

# ===============第二个窗口================
def hi():
    win2 = tkinter.Tk()
    win2.geometry("400x100+650+250")
    win2.iconbitmap("D:\python1\窗口\素材\icon.ico")
    win2.configure(bg="pink")
    win2.attributes("-alpha", 0.8)
    win2.title("♥やだよ～♥へんたい～♥")
    lable = tkinter.Label(win2, text="哎哟～你干嘛～\n嗨害嗨，你以为是啥", bg="pink", font=("Arial", 12), fg="purple",  width=15, height=2)
    lable.pack()
    win2.mainloop()

# ==============按钮定义===================
def create_button():
    # button 按钮
    # command 参数事件绑定
    button = tkinter.Button(win, text="♥别戳我～♥", bg="pink", command=hi)
    button.pack()
    return win

label2 = tkinter.Label(win, text="そ、そこはだめだ！\nすんなこと、恥かしいです、、、", bg="pink", font=("Arial", 12), fg="purple")
label2.pack()

# pack 组件的布局，绑定到win界面窗口
win = create_button()

win.mainloop()