

def deleteBlankItems(items):
    i = 0
    while i < len(items):
        if len(items[i]) == 0:
            del items[0]
        i += 1
names = ['rachel', '', 'M', '', '', 'Tim']


print(deleteBlankItems(names))