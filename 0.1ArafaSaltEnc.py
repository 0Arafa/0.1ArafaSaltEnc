#!usr/bin/python

import crypt

print("\t"*4,"#### By: Abd Almoen Arafa (0.1Arafa) ####"),print("\t"*4,"#### Age: 15                          ####\n")
text=input("Enter The String to salt it: ")
Text=input("Enter The Letters to salt: ")
print(crypt.crypt(text,Text),"\n")
#By: Abd Almoen Arafa (0.1Arafa)
#Age: 15
