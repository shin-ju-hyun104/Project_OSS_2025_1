import tkinter as tk
import threading
import random

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("타이머 계산기")
        self.root.geometry("300x400")
        self.expression = ""
        self.timer = None  # 타이머 객체 저장용

        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 버튼 배열
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=']
        ]

        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 18),
                    command=lambda ch=char: self.on_click(ch)
                )
                btn.pack(side="left", expand=True, fill="both")

    def start_timer(self):
        if self.timer:  # 기존 타이머 제거
            self.timer.cancel()
        self.timer = threading.Timer(5.0, self.time_out)  # 5초 타이머 시작
        self.timer.start()

    def time_out(self):
        self.expression = "시간 초과"
        self.update_entry()
        self.expression = ""

    def update_entry(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

    def on_click(self, char):
        if char == 'C':
            if self.timer:
                self.timer.cancel()
            self.expression = ""
        elif char == '=':
            if self.timer:
                self.timer.cancel()
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"
        else:
            self.expression += str(char)
            self.start_timer()  # 타이머 시작 또는 리셋

        self.update_entry()