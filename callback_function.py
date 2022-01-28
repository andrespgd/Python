def callbackFunc(text):
    print('Length of the text file is : ', text)

def printFileLength(path, callback):
    f = open(path, 'r')
    length = len(f.read())
    f.close()
    callback(length)

if __name__ == '__main__':
    printFileLength('callback_function.py', callbackFunc)