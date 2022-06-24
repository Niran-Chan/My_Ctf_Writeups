import os

disks = [None for _ in range(10)]
for i in range(10):
    #Opening each disk. :02d is string formatting where u always want 2 digit numbers, rb is read bytes mode
    with open(f'disk{i+1:02d}.img', 'rb') as f:
        disks[i] = f.read()
#List of strings to search for
searches = [
    b"Than these poor compounds that thou mayst not sell.",
    b"I sell thee poison; thou hast sold me none.",

    b"Live, and be prosperous; and farewell, g",
    b"Bal. [aside] For all this same, I'll hide me hereabout.",

    b"Friar. Saint Francis be my speed! how oft to-night",
    b"Have my old feet stumbled at graves! Who's there?",
    b"Bal. Here's one, a friend, and one that knows you well.",

    b"Wife. The people in the street cry 'Romeo,'",
    b"Some 'Juliet,' and some 'Paris'; and all run,",
    b"With open outcry, toward our monument.",

    b"If I departed not and left him there.",
    b"Prince. Give me the letter. I will look on it.",
    b"Where is the County's page that rais'd the watch?",


    b"Why, Belman is as good as he, my",
    b"upon it at the merest loss",
    b"And twice today",


    b"And give them friendly welcome every",
    b"Let them want nothing that my house affords.",


    b"Or wilt thou ride? Thy horses shall be trapp'd,",
    b"Their harness studded all with gold and pearl.",
    b"Dost thou love hawking? Thou hast hawks will soar",


    b"Ay, it stands so that I may hardly tarry so long. But I",
    b"be loath to fall into my dreams again: I will therefore tarry in",
    b"despite of the flesh and the blood.",


    b"If either of you both love Katherina,",
    b"Because I know you well and love you well,",
    b"Leave shall you have to court her at your pleasure.",


    b"shall be so far forth friendly maintained, till by helping",
    b"Baptista's eldest daughter to a husband, we set his youngest free",
    b"for a husband, and then have to't afresh. Sweet Bianca! Happy man",
    ]

#2048 sectors data offset ( as indicated by mdadm ) and each sector is 512 bytes  ( as indicated by documentation ) so 2048*512  = 1048576 bytes offset = 0x100000 hex offset
disks_data = [x[0x100000:] for x in disks]

disks_data_slices = []

#Going through each disk data
for i in range(10):
    diskslices = []
    current_disk_data = disks_data[i]
    #0x1000 is equivalent to 4096 bytes
    #Since the start of each superblock is 4Kb (4096 bytes = 0x1000) from the start of the device, we are calculating the number of possible slices we can make of 
    #4kb data and store into an array called diskslices and in their own respective multidimensional array
    number_of_slices = len(current_disk_data)//0x1000  
    for slicenum in range(number_of_slices):
        diskslices.append(current_disk_data[0x1000*slicenum:0x1000*(slicenum+1)])
    disks_data_slices.append(diskslices)

#python enumerate method returns si as the counter and search as the iterable

#Traverse the 2D array to find whether string matches and once it does,print out value
#Enumerating through each search string
for si, search in enumerate(searches):
    #Enumerating through each disk
    for didx, diskslices in enumerate(disks_data_slices):
        #Enumerating through each disk slice
        for slicenum, pslice in enumerate(diskslices):
            if search in pslice:
                print(f'{didx} ', end='')

# order: 0 6 3 5 2 4 1 7 8 9

disks_data = [
    disks_data[0],
    disks_data[6],
    disks_data[3],
    disks_data[5],
    disks_data[2],
    disks_data[4],
    disks_data[1],
    disks_data[7],
    disks_data[8],
    disks_data[9],
]

with open('unraid.img', 'wb') as f:
    #Number of Slices
    for slicenum in range(len(disks_data[0])//0x1000):
        print(f'slice {slicenum}: ', end='')
        #For each disk we are going to take each slice of data and write it out
        for i in range(10):
            #10 disks - column of left-symmetric layout
            parity_in_slice = 10 - (slicenum % 10) - 1
            slloc = slicenum
            #
            if i >= parity_in_slice:
                slloc += 1
            #If last disk, then continue
            if parity_in_slice == 0:
                continue
            print(slloc, ",", end='')
            f.write(disks_data[i][0x1000*slloc:0x1000*(slloc+1)])
        print()