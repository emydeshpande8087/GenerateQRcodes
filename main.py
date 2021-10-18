import datetime
from os import *
import time

from MyQR import myqr as mq

#declaring global variables
ROOT_PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_PATH=os.path.join(ROOT_PATH,'results')
OUTPUT_NAME='outputQR_'+str(time.strftime('%M%S'))+'.png'


def createQRcode(inpURL):
    'Function to create QR image from the URL input'
    print('The given URL is : ', inpURL)
    mq.run(words=inpURL,save_dir=OUTPUT_PATH,save_name=OUTPUT_NAME)



if(__name__=='__main__'):
    if((os.path.exists(OUTPUT_PATH)==False)):
        os.mkdir(OUTPUT_PATH)
    print('Welcome to QR Code Generator')
    cmdURL=input('Please enter the link --> ')
    createQRcode(cmdURL)