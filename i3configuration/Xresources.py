# About: This script automates the process of making color changes to the default terminal on a Manjaro i3 system

import os
import shutil

print('hello this program will help you change the look of the default terminal in i3\n')
filepath = os.environ['HOME'] + '.Xresources'
shutil.copy(filepath, os.environ['HOME'])
print("I've made a copy of the file and put it directly in your home directory just in case")
filepath = '/home/user/Documents/.Xresources' # test path
f = open(filepath, 'r')
data = f.read()
f.close()
newData = data[0:data.find('URxvt.background:')]
colors = ['#222D31', '#585858', '#ab4642', '#ab4642', '#7E807E', '#8D8F8D', '#f7ca88', '#f7ca88', '#7cafc2', '#7cafc2',
          '#1ABB9B', '#1ABB9B', '#d8d8d8', '#f8f8f8']
print('you can pick from an array of colors. The colors are sorted dark/light and the colors are as follows in order:\n')
print('black, red, green, yellow, blue, magenta, cyan and white\n')
print('pick the number of the color and shade you want (for example if you want light green you would type the number')
print(' 6 or if you wanted dark blue you would pick the number 10\n')
print('(Please note some color shades are the same)\n')
ans = input("what color do you want for the background of the terminal to be (if you don't want to change it just press enter)\n")
if ans == '':
    newData += data[data.find('URxvt.background:'):data.find('URxvt.cursorColor:')]
else:
    color = int(ans)
    newData += 'URxvt.background:\t\t[100]' + colors[color] + '\n'


ans = input(
    "what color do you want for the cursor color of the terminal to be (if you don't want to change it just press enter)\n")
if ans == '':
    newData += data[data.find('URxvt.cursorColor:'):data.find('URxvt.foreground:')]
else:
    color = int(ans)
    newData += 'URxvt.cursorColor:\t\t' + colors[color] + '\n'
    newData += data[data.find('URxvt.cursorColr2'):data.find('URxvt.foreground:')]


ans = input(
    "what color do you want for the foreground of the terminal to be (if you don't want to change it just press enter)\n")
if ans == '':
    newData += data[data.find('URxvt.foreground:'):]
else:
    color = int(ans)
    newData += 'URxvt.foreground:\t\t' + colors[color] + '\n'
    newData += data[data.find('URxvt*saveLines:'):]
f = open(filepath, 'w')
f.write(newData)
f.close()
