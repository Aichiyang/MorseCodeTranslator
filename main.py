#encoding=utf-8

"""
摩斯电码翻译器
全名：摩斯电码翻译器v1.0
作者：Aichiyang(Github用户名)
版本：1.0.1
制作日期：2025.8.4
版权：©2025 张嘉宁 保留所有权利

上一个版本:MorseCodeTranslator

声明：
本程序完全免费，未经原作者允许，禁止任何形式的商业使用、再分发或修改

作者原创，侵权必究
"""

import tkinter as tk
import tkinter.messagebox as message
import time as t

# 用于存储用户输入的文本
input_text = ""

# 摩斯电码翻译字典，键为字符，值为对应的摩斯电码
Morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
    ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
}


# 反转摩斯电码字典，用于摩斯电码转文本
Reverse_Morse = {value: key for key, value in Morse.items()}

def close_info_window():
    info.destroy()
    root.wm_attributes("-topmost", 1)

# 创建主窗口
root = tk.Tk()
# 设置主窗口标题
root.title('摩斯电码翻译器')
# 设置主窗口初始大小
root.geometry('400x300')

info = tk.Toplevel(root)
info.wm_attributes("-topmost", 1)  # 置顶
info.title("欢迎")
info.geometry('200x90')
tk.Label(info, text="欢迎使用摩斯电码翻译器").pack()
tk.Label(info, text="本作品为Aichiyang原创，侵权必究",bg="red").pack()
tk.Button(info, text='我知道了',command=close_info_window).pack()


def about():
    """
    待更新
    """
    about = tk.Toplevel(root)
    about.wm_attributes("-topmost", 1)
    about.title("关于")
    tk.Label(about,text='摩斯电码翻译器\n全名：摩斯电码翻译器v1.0\n作者：张嘉宁\n版本：1.0\n制作日期：2025.8.4').pack()
    tk.Label(about,text='\n版权：©2025 Aichiyang 保留所有权利\n\n声明：\n本程序完全免费，未经原作者允许，禁止任何形式的商业使用、再分发或修改\n\n作者原创，侵权必究',bg='red').pack()


# 定义文本转摩斯电码的函数
def text_to_morse(text):
    """
    将输入的文本转换为摩斯电码。
    :param text: 输入的文本，包含字母、数字、标点符号和空格
    :return: 转换后的摩斯电码字符串
    """
    morse_code = []
    # 遍历输入文本的每个字符
    for char in text.upper():
        if char in Morse:
            # 如果字符在摩斯电码字典中，添加对应的摩斯电码
            morse_code.append(Morse[char])
        elif char == ' ':
            # 如果字符是空格，添加一个斜杠分隔（摩斯电码中词间用 7 个点长度空格，这里用斜杠代替）
            morse_code.append('/')
        else:
            # 对于字典中没有的字符，添加一个问号表示无法翻译
            morse_code.append('?')
            message.showwarning('警告', f'字符 "{char}" 无法翻译为摩斯电码!')
    # 用空格连接所有摩斯电码片段
    return ' '.join(morse_code)

# 定义摩斯电码转文本的函数
def morse_to_text(morse_code):
    """
    将输入的摩斯电码转换为文本。
    :param morse_code: 输入的摩斯电码，不同字符用空格分隔，不同词用斜杠分隔
    :return: 转换后的文本字符串
    """
    text = []
    # 按斜杠分割不同的词
    words = morse_code.split('/')
    for word in words:
        # 按空格分割不同的字符
        chars = word.strip().split()
        for char in chars:
            if char in Reverse_Morse:
                text.append(Reverse_Morse[char])
            else:
                text.append('?')
        text.append(' ')
    # 去除最后一个多余的空格
    return ''.join(text).strip()

# 定义翻译窗口函数
def translator(translate_type):
    """
    创建翻译子窗口，包含输入框、翻译按钮和显示翻译结果的多行文本组件。
    :param translate_type: 翻译类型，'text_to_morse' 或 'morse_to_text'
    """
    # 创建翻译子窗口
    child_window = tk.Toplevel(root)
    # 设置子窗口标题
    if translate_type == 'text_to_morse':
        child_window.title('文本转摩斯电码')
        prompt_text = '请输入要翻译的文本：'
    else:
        child_window.title('摩斯电码转文本')
        prompt_text = '请输入要翻译的摩斯电码：'
    # 设置子窗口大小
    child_window.geometry('350x300')
    # 创建并显示提示标签
    tk.Label(child_window, text=prompt_text, font=('宋体', 15)).place(x=15, y=15)
    # 创建输入框组件
    entry_input = tk.Entry(child_window, font=('楷体', 12), width=30)
    # 设置输入框位置
    entry_input.place(x=15, y=50)

    # 定义获取输入并翻译的函数
    def get_input():
        global input_text
        # 调用 Entry 组件的 get() 方法获取输入内容
        input_text = entry_input.get()
        if translate_type == 'text_to_morse':
            result = text_to_morse(input_text)
        else:
            result = morse_to_text(input_text)
        # 清空多行文本组件内容
        result_text.delete(1.0, tk.END)
        # 将翻译结果插入到多行文本组件
        result_text.insert(tk.END, result)
        # 复制按钮可用
        copy_button.config(state=tk.NORMAL)

    # 创建翻译按钮，点击时调用 get_input 函数
    tk.Button(child_window, text='翻译', font=('楷体', 12), command=get_input).place(x=15, y=90)
    # 创建显示翻译结果的多行文本组件
    result_text = tk.Text(child_window, font=('楷体', 12), wrap=tk.WORD, height=8, width=38)
    # 设置多行文本组件位置
    result_text.place(x=15, y=130)

    # 定义复制结果的函数
    def copy_result():
        result = result_text.get(1.0, tk.END).strip()
        child_window.clipboard_clear()
        child_window.clipboard_append(result)

    # 创建复制按钮，初始状态为禁用
    copy_button = tk.Button(child_window, text='复制结果', font=('楷体', 12), command=copy_result, state=tk.DISABLED)
    copy_button.place(x=15, y=280)

# 定义翻译主菜单函数
def translator_menu():
    """
    创建翻译主菜单子窗口，提供翻译方式选择按钮。
    """
    # 创建翻译主菜单子窗口
    child_window = tk.Toplevel(root)
    # 设置子窗口标题
    child_window.title('翻译主菜单')
    # 设置子窗口大小
    child_window.geometry('300x200')
    # 创建并显示提示标签
    tk.Label(child_window, text='选择翻译方式：', font=('宋体', 15)).place(x=15,y=15)
    # 创建文本转摩斯电码按钮，点击时调用 translator 函数
    tk.Button(child_window, text='将文本翻译为摩斯电码', font=('楷体', 12), command=lambda: translator('text_to_morse')).place(x=15, y=50)
    # 创建摩斯电码转文本按钮，点击时调用 translator 函数
    tk.Button(child_window, text='将摩斯电码翻译为文本', font=('楷体', 12), command=lambda: translator('morse_to_text')).place(x=15, y=90)

# 定义主菜单函数
def main_menu():
    """
    创建主菜单，包含标题标签和开始使用按钮。
    """
    # 创建并显示标题标签
    tk.Label(root,text='摩斯电码翻译器',font = ('宋体',30)).place(x=60,y=30)
    # 创建开始使用按钮，点击时调用 translator_menu 函数
    tk.Button(root, text='开始使用',font = ('楷体',25), command=translator_menu).place(x=125,y=150)
    # 创建关于按钮，点击时调用 about 函数
    tk.Button(root, text='关于',font = ('楷体',25), command=about).place(x=160,y=215)

# 定义主函数
def main():
    """
    程序入口函数，调用主菜单函数。
    """
    main_menu()

if __name__ == '__main__':
    # 调用主函数
    main()
    # 进入主事件循环，保持窗口显示
    root.mainloop()