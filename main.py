import wave
from LSB import *
from phase import *

encode_LSB('trial.wav', 'Hello This is ashish trying to hide some data')

decode=decode_LSB("encoded.wav")
print("The decoded String is : - ")
print(decode)


