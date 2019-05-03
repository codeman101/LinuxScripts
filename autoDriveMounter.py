# About: This script simplifies the process of adding a drive to the fstab file so it can be automatically mounted every time the computer
# Note for use: Due to the nature of the directory it accesses it needs to be ran as root

import subprocess as p
import string as s
fstype = ''
label = ''
uuid = ''
mntptr = ''
driveNum = 0
drives = {}
pieces = []
mountPoints = []

cmd = ['lsblk', '-f'] #using sudo on the file gives root power
output = p.Popen( cmd, stdout= p.PIPE).communicate()[0]
data = str(output)

ptr=0
i=0
k=1
letters = s.ascii_lowercase
nums = s.digits
while ptr < len(data):
    if data.find('sd' + letters[i] + nums[k], ptr) == -1:
        k += 1 # increment the number
        if data.find('sd' + letters[i] + nums[k], ptr) == -1: # if the number part wasn't found increment the letter
            k = 1
            i += 1
            if data.find('sd' + letters[i] + nums[k], ptr) == -1:
                break # the last letter was reached and passed so end of string
            else:
                ptr = data.find('sd' + letters[i] + nums[k], ptr)
        else:
            ptr = data.find('sd' + letters[i] + nums[k], ptr)
    else:
        ptr = data.find('sd' + letters[i] + nums[k], ptr)
    ptr += 5
    if data[ptr] == ' ':
        continue # skip because this dev dir doesn't have a drive
    while data[ptr] != ' ':
        fstype += data[ptr] # get filesystem type
        ptr += 1
    while data[ptr] == ' ': # move to uuid
        ptr += 1
    while data[ptr] != ' ': # get uuid.
        uuid += data[ptr]
        ptr += 1
        if data[ptr] == ' ' and data[ptr+1].isalpha(): # if there's a space in what is actually a label
            uuid += data[ptr]
            ptr += 1
    if uuid.isalpha() or ' ' in uuid: # checking if drive had a label
        label = uuid # it did so got to move string to correct var and go get actual uuid
        uuid = '' # reset var
        while data[ptr] == ' ':
            ptr += 1 # move to actual uuid
        while data[ptr] != ' ':
            uuid += data[ptr]
            ptr += 1
    if data.find('/', ptr) < data.find('sd', ptr) or data.find('sd', ptr) == -1: # checking if drive was assigned a mount point
        while data[ptr] != '/': # there is a mount point
            ptr += 1
        while data[ptr] != '\\' and data[ptr+1] != 'n':
            mntptr += data[ptr]
            ptr += 1
        if data[ptr+1] == 'n' and data[ptr+2] == 't':
            mntptr = '/mnt'
        mountPoints.append(mntptr)
    # components obtained!
    pieces = [label, uuid, fstype]
    drives[driveNum] = pieces
    driveNum += 1
    label = ''
    uuid = ''
    fstype = ''
    mntptr = ''
i =0
while i < driveNum:
    if drives[i][0] != '':
        print( str(i + 1) + ')' + drives[i][0])
    i += 1
ans = input(' which drive do you want to auto-mount? (Type the number of the drive)\n')
choice = int(ans)
choice -= 1
newMnt = input('where do you want to mount it to?\n')
while newMnt in mountPoints:
    newMnt = input('that mount point is taken pick a different one\n')
newLine = 'UUID=' + drives[choice][1] + ' '

newLine += newMnt + ' '
newLine += drives[choice][2] + ' defaults,nofail 0 0'
f = open('/etc/fstab', 'a')
f.write(newLine)
f.close()

