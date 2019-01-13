import pyqrcode

def qrcode():

 #qr=pyqrcode.create('hello')#
 #qr.png('hello.png',scale=7)#
 print('Qr corde generated')
 big_code = pyqrcode.create('hello',mode='binary')
 big_code.png('code.png', scale=4, module_color='#FFD700', background='#000000' )

if __name__=='__main__':
    qrcode()