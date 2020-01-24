# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 18:32:07 2020

@author: CEC
"""

aclNum=int(input("What is the IPv4 ACL number?"))
if aclNum>=1 and aclNum <=99:
        print("This is a stamdart IPv4 ACL.")
elif aclNum >=100 and aclNum <= 199:
    print("This is a extended IPv4 ACL.")
else:
    print("This is not a standard or extended IPv4 ACL.")
    