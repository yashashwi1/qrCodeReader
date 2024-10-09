import printMessages
from qreader import QReader
import cv2 
import os
import sys
from pathlib import Path

n = len(sys.argv)
print(sys.argv)
if n > 2 or n < 2:
  printMessages.printError("Send argument like : python3 src/qrCodeReader 1/0 or True:False")
  sys.exit()

parameter=""
n = sys.argv[1]
if n == '1' or n == 'True':
  parameter="/src/putQR_Here"
elif n == '0' or n == 'False':
  parameter="src/putQR_Here"

def main(path):
   printMessages.printMessage("QR Code Reader!!!")
   printMessages.printMessage("Reading all the QRs at the provided path...")
   directoryPath=path
   files={}
   for path in os.listdir(directoryPath):
       # check if current path is a file
       if os.path.isfile(os.path.join(directoryPath, path)):
           files[path]=os.path.join(directoryPath, path)

   try:
        for file in files:
          outPath = files[file].replace(file, file + "_output.txt")        
         # printMessages.printWarning(outPath)
         # printMessages.printWarning(file)
          try:
            if ("output" in  file) or ( "error" in file):
               continue        
            # Create a QReader instance
            qreader = QReader()

            # Get the image that contains the QR code
            image = cv2.cvtColor(cv2.imread(files[file]), cv2.COLOR_BGR2RGB)

            # Use the detect_and_decode function to get the decoded QR data
            decoded_text = qreader.detect_and_decode(image, return_detections = False)
            print(decoded_text)
            #if decoded_text is not null                 
            if decoded_text is not None:
               outPath= Path(outPath)
               print(outPath)
               if Path(outPath).exists():
                  os.remove(outPath)
               f = open(outPath, "w")
               
               for decodedValue in decoded_text:
                  printMessages.printMessage(decodedValue)                
                  f.write(decodedValue)
               f.close();     
               p = str(Path(outPath).absolute())
               printMessages.printMessage("The qr code is decoded, it is printed @:" + p)

          except Exception as e:
            outputPath = files[file].replace(file, file + "_error.txt")
            f = open(outputPath, "w")
            f.write(e)
            f.close()   
          
   except Exception as e:
        printMessages.printError(str(e))


main(parameter)
