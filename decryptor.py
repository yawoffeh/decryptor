import os
import pyAesCrypt as pc

files = [x for x in os.listdir() if x != "decryptor.py" and ".out" in x]
def main():
    passw = 'solstice'
    filext = 'py'
    bufferSize = 64 * 1024
    for file in files:
	try:
	    pc.decryptFile(file, file.replace("py.out", filext), passw, bufferSize)
	    print("decrypted")
	except:
	    print("decryption unsucessful")

if __name__ == '__main__':
	main()
