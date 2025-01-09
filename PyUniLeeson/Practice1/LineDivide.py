import re
s = str(input('Enter the line: '))
print(re.split('[,; ]',s))