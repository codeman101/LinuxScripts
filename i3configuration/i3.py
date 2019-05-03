#About: This script automates the process of customizing the i3 environment

import os
import shutil

print('hello I will help you configure your i3 environment\n')
print("let's start with the main configuration file and work our way down it\n")
filepath = os.environ['HOME'] + '/.i3/config'
shutil.copy(filepath, os.environ['HOME'])
print("I've made a backup copy of the original i3 config file and put in your home folder\n")
f = open(filepath, 'r')
newData = ''
data = f.read()
f.close()
ptr = 0
newData += data[ptr:data.find('set $ws2 2')]  # go to where workspaces are set
ptr = data.find('set $ws2 2')
newData += data[ptr:data.find('set $ws1 1', ptr)]
ans = input('for starters, do you want to rename any of your workspaces? [y/n]')
if ans == 'y':
    print("there's a total of 8")
    i = 1
    while i < 9:
        name = input(
            "what do you want workspace " + str(i) + " to be (note if you don't to change the name just press enter)\n")
        if name != '':
            newData += 'set $ws' + str(i) + ' ' + str(name) + '\n'  # add new name
        else:
            newData += "set $ws" + str(i) + ' ' + str(i) + '\n'
        i += 1
    newData += '\n'
ptr = data.find('# switch to workspace')
newData += data[ptr:data.find('# Open applications on specific workspaces', ptr)]
ans = input('do you want to have apps startup in certain workspaces when you boot?[y/n]')
if ans == 'y':
    print('I need the ID names of the apps you want to have startup when you '
          'boot and which workspace you want them to boot into\n')
    print('open the app(s) you want to have startup at boot.\n Type xprop in the terminal  ')
    print('then click on the window of the app you want to have assigned\n')
    add = True
    ptr = data.find('# Open applications on specific workspaces')
    newData += data[ptr: data.find('# assign', ptr)]  # get right up to assign for forcing app to open in certain workspace
    while add:
        app = input('give me the name of the app you want to have boot in the workspace.\n')
        ws = input('give me the workspace number that you want to have the app boot into. '
                   'Also if you do not want to do anymore put a space and type ' + "'" + "stop" + "'" + '\n')
        if 'stop' in ws:
            add = False
            ws = ws[0:ws.find(' stop')]  # strip out the word stop so you can extract the workspace number
        newData += "assign [class=" + '"' + app + '"] $ws' + ws + '\n'

# coloring portion
white = '#ffffff'  # 1
black = '#000000'  # 2
red = '#ff0000'  # 3
yellow = '#ffff00'  # 4
purple = '#2B1C54'  # 5
orange = '#ffa500'  # 6
pink = '#ffc0cb'  # 7
grey = '#808080'  # 8
green = '#008000'  # 9
blue = '#0000ff'  # 10
brown = '#a52a2a'  # 11
colors = [white, black, red, yellow, purple, orange, pink, grey, green, blue, brown]
newData += data[data.find('# Open specific applications in floating mode'): data.find('colors {')]
ans = input('do you want to change the colors of the default i3 look? [y/n]')
if ans == 'y':  # this is for all colors
    print('here are the colors \n white, black, red, yellow, purple, orange, pink, grey, green, blue, brown '
          '\n I will ask you about changing the color for the different parts of the look. Please type the respective '
          'number of each color for example white=1 black=2 and so on\n')
    ans = input('do you want to change the colors of the i3 bar? (not including workspace tabs) [y/n]')
    if ans == 'y':  # this is for the bar
        ans = input('do you want to change the background color of the i3 bar? [y/n]')
        if ans == 'y':
            color = 0
            while color < 1 or color > 11:
                ans = input('what color do you want the background to be\n')
                color = int(ans)
            ptr = data.find('colors {')
            newData += data[data.find('colors {'): data.find('background', ptr)]
            newData += 'background ' + str(colors[color]) + '\n'
        else:
            newData += data[data.find('colors {'): data.find('statusline')]
        ans = input('do you want to change the text of the part that times time, disk usage, cpu usage ect.? [y/n]')
        if ans == 'y':
            color = 0
            while color < 1 or color > 11:
                ans = input('what color do you want the text to be\n')
                color = int(ans)
            newData += '\tstatusline ' + str(colors[color]) + '\n'
        else:
            newData += data[data.find('statusline'): data.find('separator')]
        ans = input(
            'do you want to change the separator which separates the pieces of info like the cpu and disk usage? [y/n]')
        if ans == 'y':
            color = 0
            while color < 1 or color > 11:
                ans = input('what color do you want the it to be\n')
                color = int(ans)
            newData += '\tseparator ' + str(colors[color]) + '\n'
            newData += ' # \t \t \t ' + 'border' + '\t' + 'backgr' + '\t' + 'text' + '\n'
        else:
            newData += data[data.find('separator'): data.find('focused_workspace')]
    else:
        newData += data[data.find('colors {'): data.find('focused_workspace')]
    ans = input(
        'do you want to change the way a workspace looks when you are using it? (meaning the box in the buttom right corner of it) [y/n]')
    if ans == 'y':  # workspace head if
        border = 0
        background = 0
        text = 0
        ans = input('do you want to change border color of it? [y/n]')
        if ans == 'y':
            while border < 1 or border > 11:
                ans = input('what color do you want the text to be\n')
                border = int(ans)
        else:
            border = 0
        ans = input('do you want to change the background color of it? [y/n] ')
        if ans == 'y':
            while background < 1 or background > 11:
                ans = input('what color do you want the text to be\n')
                background = int(ans)
        else:
            background = 0
        ans = input('do you want to change the text color of it? [y/n] ')
        if ans == 'y':
            while text < 1 or text > 11:
                ans = input('what color do you want the text to be\n')
                text = int(ans)
        else:
            text = 0
        if border == 0 and background == 0 and text > 0:
            newData += ' \t focused_workspace  #F9FAF9 #16a085 ' + colors[text] + '\n'
            newData += ' \t active_workspace  #595B5B #353836 ' + colors[text] + '\n'
        elif border == 0 and background > 0 and text == 0:
            newData += ' \t focused_workspace  #F9FAF9 ' + colors[background] + '#292F34' + '\n'
            newData += ' \t active_workspace  #595B5B ' + colors[background] + '#FDF6E3' + '\n'
        elif border > 0 and background == 0 and text == 0:
            newData += ' \t focused_workspace ' + colors[border] + ' #16a085 ' + '#292F34' + '\n'
            newData += ' \t active_workspace ' + colors[border] + ' #353836 ' + '#FDF6E3' + '\n'
        elif border == 0 and background > 0 and text > 0:
            newData += ' \t focused_workspace #F9FAF9' + colors[background] + colors[text] + '\n'
            newData += ' \t active_workspace #595B5B' + colors[background] + colors[text] + '\n'
        elif border > 0 and background > 0 and text == 0:
            newData += ' \t focused_workspace ' + colors[border] + colors[background] + '#292F34' + '\n'
            newData += ' \t active_workspace ' + colors[border] + colors[background] + '#FDF6E3' + '\n'
        elif border > 0 and background == 0 and text > 0:
            newData += ' \t focused_workspace ' + colors[border] + ' #16a085 ' + colors[text] + '\n'
            newData += ' \t active_workspace ' + colors[border] + ' #353836 ' + colors[text] + '\n'
        else:
            print('I see you did not make any changes. I will copy everything from the original file')
            newData += data[data.find('focused_workspace'): data.find('inactive_workspace')]

        ans = input('do you want to change the color of workspaces when they are inactive? [y/n]')
        if ans == 'y':
            newData += 'inactive_workspace '
            ans = input('do you want to change the border color of inactive workspaces? [y/n]')
            if ans == 'y':
                border = 0
                while border < 1 or border > 11:
                    ans = input('what color do you want it to be?\n')
                    border = int(ans)
                newData += colors[border]
            else:
                newData += '#595B5B'
            ans = input('do you want to change the background color of inactive workspaces? [y/n]')
            if ans == 'y':
                background = 0
                while background < 1 or background > 11:
                    ans = input('what color do you want it to be?\n')
                    background = int(ans)
                newData += colors[background]
            else:
                newData += '#222D31'
            ans = input('do you want to change the text color of inactive workspaces? [y/n]')
            if ans == 'y':
                text = 0
                while text < 1 or text > 11:
                    ans = input('what color do you want it to be?\n')
                    text = int(ans)
                newData += colors[text]
            else:
                newData += '#EEE8D5'
            newData += '\n'
        else:
            newData += data[data.find('inactive_workspace'):data.find('urgent_workspace')]
        print('do you want to change the colors of an urgent workspace')
        ans = input(
            '(this happens when the computer tries to tell you that some event occurred in that workspace) [y/n]')
        if ans == 'y':
            newData += 'urgent_workspace\t'
            ans = input('do you want to change the border color of the urgent_workspace? [y/n]')
            if ans == 'y':
                border = 0
                while border < 1 or border > 11:
                    ans = input('what color do you want it to be?\n')
                    border = int(ans)
                newData += colors[border]
            else:
                newData += '#16a085'
            ans = input('do you want to change the background color of the urgent_workspace? [y/n]')
            if ans == 'y':
                background = 0
                while background < 1 or background > 11:
                    ans = input('what color do you want it to be?\n')
                    background = int(ans)
                newData += colors[background] + ' '
            else:
                newData += '#FDF6E3 '
            ans = input('do you want to change the border color of the urgent_workspace? [y/n]')
            if ans == 'y':
                text = 0
                while text < 1 or text > 11:
                    ans = input('what color do you want it to be?\n')
                    text = int(ans)
                newData += colors[text]
            else:
                newData += '#E5201D'
            newData += '\n \t } \n } \n # hide/unhide i3status bar\nbindsym $mod+m bar mode toggle\n\n# Theme colors\n# class\n'
            newData += '\t\t border  backgr.  text   indic.\n '
        else:
            newData += data[data.find('urgent_workspace'):data.find('client.focused')]

        ans = input("do you want to change the colors of a window when it's in focus (active)? [y/n]")
        if ans == 'y':
            newData += 'client.focused\t'
            ans = input('do you want change the border color? [y/n]')
            if ans == 'y':
                border = 0
                while border < 1 or border > 11:
                    ans = input('what color do you want it to be?\n')
                    border = int(ans)
                newData += colors[border] + ' '
            else:
                newData += '#556064 '
            ans = input('do you want to change background color? [y/n]')
            if ans == 'y':
                background = 0
                while background < 1 or background > 11:
                    ans = input('what color do you want it to be?\n')
                    background = int(ans)
                newData += colors[background] + ' '
            else:
                newData += '#556064 '
            ans = input('do you want to change text color? [y/n]')
            if ans == 'y':
                text = 0
                while text < 1 or text > 11:
                    ans = input('what color do you want it to be?\n')
                    text = int(ans)
                newData += colors[text] + ' '
            else:
                newData += '#80FFF9 '
            ans = input(
                'do you want to change indication color? (which occurs when an event happened in another window) [y/n]')
            if ans == 'y':
                indicator = 0
                while indicator < 1 or indicator > 11:
                    ans = input('what color do you want it to be?\n')
                    indicator = int(ans)
                newData += colors[indicator] + '\n'
            else:
                newData += '#FDF6E3\n'
        else:
            newData += data[data.find('client.focused'):data.find('client.focused_inactive')]

        ans = input("do you want to change the colors of a window when it's in focus but inactive? [y/n]")
        if ans == 'y':
            newData += 'client.focused_inactive '
            ans = input('do you want change the border color? [y/n]')
            if ans == 'y':
                border = 0
                while border < 1 or border > 11:
                    ans = input('what color do you want it to be?\n')
                    border = int(ans)
                newData += colors[border] + ' '
            else:
                newData += '#2F3D44 '
            ans = input('do you want to change background color? [y/n]')
            if ans == 'y':
                background = 0
                while background < 1 or background > 11:
                    ans = input('what color do you want it to be?\n')
                    background = int(ans)
                newData += colors[background] + ' '
            else:
                newData += '#2F2D44 '
            ans = input('do you want to change text color? [y/n]')
            if ans == 'y':
                text = 0
                while text < 1 or text > 11:
                    ans = input('what color do you want it to be?\n')
                    text = int(ans)
                newData += colors[text] + ' '
            else:
                newData += '#1ABC9C '
            ans = input(
                'do you want to change indication color? (which occurs when an event happened in another window) [y/n]')
            if ans == 'y':
                indicator = 0
                while indicator < 1 or indicator > 11:
                    ans = input('what color do you want it to be?\n')
                    indicator = int(ans)
                newData += colors[indicator] + '\n'
            else:
                newData += '#454948\n'
        else:
            newData += data[data.find('client.focused_inactive'):data.find('client.unfocused')]

        ans = input("do you want to change the colors of a window when it's unfocused? [y/n]")
        if ans == 'y':
            newData += 'client.unfocused\t'
            ans = input('do you want change the border color? [y/n]')
            if ans == 'y':
                border = 0
                while border < 1 or border > 11:
                    ans = input('what color do you want it to be?\n')
                    border = int(ans)
                newData += colors[border] + ' '
            else:
                newData += '#2F3D44 '
            ans = input('do you want to change background color? [y/n]')
            if ans == 'y':
                background = 0
                while background < 1 or background > 11:
                    ans = input('what color do you want it to be?\n')
                    background = int(ans)
                newData += colors[background] + ' '
            else:
                newData += '#2F2D44 '
            ans = input('do you want to change text color? [y/n]')
            if ans == 'y':
                text = 0
                while text < 1 or text > 11:
                    ans = input('what color do you want it to be?\n')
                    text = int(ans)
                newData += colors[text] + ' '
            else:
                newData += '#1ABC9C '
            ans = input(
                'do you want to change indication color? (which occurs when an event happened in another window) [y/n]')
            if ans == 'y':
                indicator = 0
                while indicator < 1 or indicator > 11:
                    ans = input('what color do you want it to be?\n')
                    indicator = int(ans)
                newData += colors[indicator] + '\n'
            else:
                newData += '#454948\n'
        else:
            newData += data[data.find('client.unfocused'):data.find('client.urgent')]

        ans = input("do you want to change the colors of a window when it's urgent? [y/n]")
        if ans == 'y':
            newData += 'client_urgent\t\t'
            ans = input('do you want change the border color? [y/n]')
            if ans == 'y':
                border = 0
                while border < 1 or border > 11:
                    ans = input('what color do you want it to be?\n')
                    border = int(ans)
                newData += colors[border] + ' '
            else:
                newData += '#CB4B16 '
            ans = input('do you want to change background color? [y/n]')
            if ans == 'y':
                background = 0
                while background < 1 or background > 11:
                    ans = input('what color do you want it to be?\n')
                    background = int(ans)
                newData += colors[background] + ' '
            else:
                newData += '#FDF6E3 '
            ans = input('do you want to change text color? [y/n]')
            if ans == 'y':
                text = 0
                while text < 1 or text > 11:
                    ans = input('what color do you want it to be?\n')
                    text = int(ans)
                newData += colors[text] + ' '
            else:
                newData += '#1ABC9C '
            ans = input(
                'do you want to change indication color? (which occurs when an event happened in another window) [y/n]')
            if ans == 'y':
                indicator = 0
                while indicator < 1 or indicator > 11:
                    ans = input('what color do you want it to be?\n')
                    indicator = int(ans)
                newData += colors[indicator] + '\n'
            else:
                newData += '#268BD2\n'
        else:
            newData += data[data.find('client.urgent'):data.find('client.placeholder')]

        ans = input("do you want to change the colors of a window when it's being restored? [y/n]")
        if ans == 'y':
            newData += 'client.placeholder\t'
            ans = input('do you want change the border color? [y/n]')
            if ans == 'y':
                border = 0
                while border < 1 or border > 11:
                    ans = input('what color do you want it to be?\n')
                    border = int(ans)
                newData += colors[border] + ' '
            else:
                newData += '#000000 '
            ans = input('do you want to change background color? [y/n]')
            if ans == 'y':
                background = 0
                while background < 1 or background > 11:
                    ans = input('what color do you want it to be?\n')
                    background = int(ans)
                newData += colors[background] + ' '
            else:
                newData += '#0C0C0C '
            ans = input('do you want to change text color? [y/n]')
            if ans == 'y':
                text = 0
                while text < 1 or text > 11:
                    ans = input('what color do you want it to be?\n')
                    text = int(ans)
                newData += colors[text] + ' '
            else:
                newData += '#FFFFFF '
            ans = input(
                'do you want to change indication color? (which occurs when an event happened in another window) [y/n]')
            if ans == 'y':
                indicator = 0
                while indicator < 1 or indicator > 11:
                    ans = input('what color do you want it to be?\n')
                    indicator = int(ans)
                newData += colors[indicator] + '\n'
            else:
                newData += '#000000\n'
        else:
            newData += data[data.find('client.placeholder'):data.find('client.background')]

        ans = input('do you want to change the background of the windows? [y/n]')
        if ans == 'y':
            newData += 'client.background\t'
            background = 0
            while background < 1 or background > 11:
                ans = input('what do you want the color of it to be? ')
                background = int(ans)
            newData += colors[background] + '\n'
        else:
            newData += 'client.background\t#2B2C2B\n'
    else:
        newData += data[data.find('focused_workspace'): data.find('# Set inner/outer gaps')]
ans = input('do you want to keep i3-gaps? [y/n]')
if ans == 'y':
    newData += data[data.find('# Set inner/outer gaps'):] + '\n'
else:
    newData += data[data.find('# Set inner/outer gaps'):data.find('gaps inner 14')]
    newData += '#gaps inner 14\n#gaps outer -2'
    newData += data[data.find('# Additionally, you can issue commands with the following syntax.'):] + '\n'
    print("Ok in case you change your mind in the future I've kept that gap settings in the file")
    print(" and just commented them out so you won't see any gaps")
print(
    "Finally we're almost done! I'm not going to ask you anymore questions (well expect one but that's it. I promise) ")
print("we've made it to end of the default config file with ours configurations. ")
print("the only thing left that I'm going to is add a couple more things to the config file. ")
print("after I'm done and close out hit Ctrl+Shift+R to apply the changes we made ")
print(
    "from this point on I'm just going to add a couple standard configurations that aren't included in the default file\n ")
print(
    "first I'm going to add involves the one question I have left for you because if you say no then I don't need to add this\n ")
ans = input('when you installed manjaro i3 did you have to change the resolution settings? [y/n]')
if ans == 'y':
    newData += 'exec xrandr --size 1920x1080\nexec xrandr --dpi 111\n'
    print(
        "Ok I've added the fixes for your resolution but you made need to restart your computer in order for them to take effect\n")
print(
    "Now I'm going to add controls for your keyboard on the F row so the music and audio buttons on there will work. ")
print("You'll need to install a program called playerctl for this to work so run sudo pacman -S playerctl")
newData += "# Media player controls\nbindsym XF86AudioPlay exec playerctl play\nbindsym F7 exec playerctl pause\n"
newData += 'XF86AudioNext exec playerctl next\nbindsym XF86AudioPrev exec playerctl previous'
f = open(filepath, 'w')
f.write(newData)
f.close()

