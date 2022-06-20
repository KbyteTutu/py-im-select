#!/usr/bin/python
# -*- coding: utf-8 -*-
# @ 南无阿弥陀佛，不要有太多bug……
# @ Author: tukechao
# @ Date: 2022-06-21 00:12:30
# @ LastEditors: tukechao
# @ LastEditTime: 2022-06-21 01:36:23
# @ FilePath: \Python\py-im-select\win\im-select.py
# @ Description: vim 输入法切换工具(配合搜狗输入法)
# @ 如有疑问请联系 tukechao@gmail.com

import win32api
import win32gui
import win32con
import sys
from win32con import WM_INPUTLANGCHANGEREQUEST


def get_current_im():
    hwnd = win32gui.GetForegroundWindow()
    if hwnd:
        thread_id = win32api.GetWindowLong(hwnd, 0)
        klid = win32api.GetKeyboardLayout(thread_id)
        current_lid = klid & (2**16 - 1)
        return current_lid
    else:
        return 0


def switch_im_to_needed(lid):
    lang = {"2052": 0x804, "1033": 0x409}

    hwnd = win32gui.GetForegroundWindow()
    if hwnd:
        win32api.SendMessage(hwnd, WM_INPUTLANGCHANGEREQUEST, 0, eval(lid))
    # if lid == hex(2052):
    #     simulate_press_shift()


# def simulate_press_shift():
#     win32api.keybd_event(16, 0, win32con.KEYEVENTF_KEYUP, 0)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        lid = hex(int(sys.argv[1]))
        switch_im_to_needed(lid)
    else:
        print(get_current_im())
