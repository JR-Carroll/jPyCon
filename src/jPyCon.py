#!/usr/bin/python

#Author J. R. Carroll
#Date:  July 18, 2012
#
#Instructions:  Run this file in-place and move the resulting desktop.ini file
#to the appropriate folder of which you want to alter the original folder type!

import os
import Tkinter
import tkFileDialog

def iconsLocation():

    root2 = Tkinter.Tk()
    root2.withdraw()
    
    #Config file name - this file has settings saved
    iconConfig = "jIcon.con"

    #List that will later be used to check to see if config file is there!
    directory = os.listdir(os.getcwd())
    
    if iconConfig in directory:
        configCreated = open('jIcon.con')
        configList = {}
        for line in configCreated:
            v = line.split("=")
            configList[v[0].strip()] = v[1]

        myIconLocation = configList["IconDirectory"]
        myIcon = tkFileDialog.askopenfilename(parent=root2, title="Select \
the Icon!", initialdir=myIconLocation)

        compareDIR = myIcon.split("\\")
        compareDIR.pop(-1)

        if compareDIR != myIconLocation.split("\\"):
            createConfig = open('jIcon.con', 'w')
            createConfig.write("IconDirectory = " + myIconLocation)
            createConfig.close() 
        
        return myIcon
           
    else:
        
        #Bring a windows explorer up to select ICON (should be .ico)
        myIconLocation = tkFileDialog.askdirectory(parent=root2, title='Location of \
your Windows ICONs?')

        myIcon = tkFileDialog.askopenfilename(parent=root2, title="Select \
the Icon!", initialdir=myIconLocation)
        
        print myIcon

        createConfig = open('jIcon.con', 'w')
        createConfig.write("IconDirectory = " + myIcon)
        createConfig.close()
        
        return myIcon

def main():

    root = Tkinter.Tk()
    root.withdraw()

    myIcon2 = iconsLocation()
    #Bring a windows explorer up to select the DIR (change attrib to +r)
    myDir = tkFileDialog.askdirectory(parent=root, title="Which folder do you \
want to edit?")
    
    #String to be formated with the information above!
    writeOut = (
    """[.ShellClassInfo]
ConfirmFileOp=0
NoSharing=1
IconFile={0}
IconIndex=0""")

    #Format the string with the correct variables
    rewriteOut = writeOut.format(myIcon2)

    try:
        cmd0Attrib = 'attrib -h -r {0}'
        cmd0Command = cmd0Attrib.format('"' + (str(myDir) + '/Desktop.ini"'))

        cmd0 = os.popen(cmd0Command)
        cmd0.close()
    except:
        pass
    
    #Name the .ini file for writing purposes!
    myDeskINIFile = open((str(myDir) + '/Desktop.ini'), 'w')

    #Write-out to the file
    myDeskINIFile.writelines(rewriteOut)
    myDeskINIFile.close()


    cmd1Attrib = 'attrib +h +r {0}'
    cmd1Command = cmd1Attrib.format('"' + (str(myDir) + '/Desktop.ini"'))

    cmd1 = os.popen(cmd1Command)
    cmd1.close()

    cmd2Attrib = 'attrib {0} +r'
    cmd2Command = cmd2Attrib.format('"' + str(myDir) + '"')

    cmd2 = os.popen(cmd2Command)
    cmd2.close()
    
if __name__ == "__main__":
    main()
    

