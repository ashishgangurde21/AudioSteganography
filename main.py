import wave
from lsb import *
from phase import *

encode_LSB('trial.wav', 'Hello This is ashish trying to hide some data')

decode=decode_LSB("encoded.wav")
print("The decoded String is : - ")
print(decode)

encode_phase("trial.wav","Hello this is ashish and This is a trial")
decode_phase("Phase_encoded.wav")

