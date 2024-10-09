
# QRCode Reader
## It reads and extracts the value from QRCodes in bulk.
**Written in Python. Using https://pypi.org/project/qreader/**

***Usage Mode***
1. ## Use Source Code:
   _You can clone this public git repo. Extend the source code per your will, or use it as is_
   _If you wish to go this way, update the qrCodeReader.py file, by default it is expecting collection of qrs to be in putQR_Here, execute below command:_
   ## python3 src/qrCodeReader.py 0##
2. ## Use Docker: For this you need docker cli installed, refer the documentation https://docs.docker.com/desktop/install/mac-install/
   _A Dockerfile is also provided in the repo, if you have access to docker cli, clone this repo and simply run:_
   **docker build -t <your_choice_image_name> .**
   **_For example:Lets assume qr_extractor is the image name and version is:1.0.0_**
   ## docker build -t qr_extractor:1.0.0 . ##
   **_Once image is created using above command you can invoke the container like below: In below command -v is the argument and the value is the actual path of your QRcollection folder._**
   ## docker run -it -v {fully qualified path to your QRcode collection folder}:/src/putQR_Here qr_extractor:1.0.0 ##
   **_example:_**
   ## docker run -it -v /home/vagrant/qrCodeReader/src/putQR_Here:/src/putQR_Here qr_extractor:1.0.0

