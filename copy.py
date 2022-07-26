import copy
a="Hello World "  # way of coping a string 
b=a                # id same        
b=str(a)           # id same
b=a[:]             # id same
b=a + ""           # id same
b=copy.copy(a)     # id same
b=a[::-1][::-1]     # id differ
