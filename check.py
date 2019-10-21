import os
from array import *
from struct import *

ranges = loop = fil = counter = temp = 0 
now = 0
end = 0
iterator = 0 
intp = float(0) 
output = []
with open("OOF.brr", "rb") as in_file:
    length = os.path.getsize("OOF.brr")
    ranges = in_file.read(length)
    #print(length)
    while True:
    	current = 0 
    	#ranges = in_file.read(length)
    	temp = format(ranges[now], 'b')
    	check = '{0:08d}'.format(int(temp))
    	backString = str(check)
    	end = int(backString[7])
    	loop = int(backString[6])
    	addFilter = backString[4] + backString[5]
    	fil = int(addFilter,2)
    	#print(addFilter)
    	addRange = backString[0] + backString[1] + backString[2] + backString[3]
    	#rangeNumber = '{0:04d}'.format(int(addRange))
    	#print(addRange)
    	decRangeVal = int(addRange, 2) #convert binary to decimal 
    	now = now + 1 	
    	for counter in range(8):
    	 	# newBytes = format(ranges[now], 'b')
    	 	# print('{0:08d}'.format(int(newBytes)))
    	 	first_nibble = ranges[now]>>4
    	 	first_nibble = first_nibble & 0xF
    	 	#print(first_nibble)
    	 	if first_nibble >= 8:
    	 		first_nibble = first_nibble | 0xFFF0
    	 	first_nibble =  first_nibble << decRangeVal
    	 	first_nibble = first_nibble / (2 ** 16)
    	 	#print(first_nibble)
    	 	output.append(first_nibble)
    	 	if iterator != 0:
    	 		iterator = iterator + 1   
    	 	if current != 0:
    	 		if fil == 1:
    	 			output[iterator] = output[iterator] + int(float(output[iterator - 1]) * 15/16)
    	 		elif fil == 2:
    	 			output[iterator] = output[iterator] + int(float(output[iterator - 1]) * 61/32) - int(float(output[iterator - 2]) * 15/16)
    	 		elif fil == 3:
    	 			output[iterator] = output[iterator] + int(float(output[iterator - 1]) * 115/64) - int(float(output[iterator - 2]) * 13/16)
    	 	#print(output[iterator])
    	 	second_nibble = ranges[now] & 0xF
    	 	#print(second_nibble)
    	 	if second_nibble >= 8:
    	 		second_nibble = second_nibble | 0xFFF0
    	 	second_nibble = second_nibble << decRangeVal
    	 	second_nibble = second_nibble / (2 ** 16)
    	 	output.append(second_nibble)
    	 	iterator += 1
    	 	#print(output[iterator])
    	 	#print('\n')
    	 	now += 1  
    	 	current += 1
    	 	if now == length:
    	 		break
    	if now == length:
    		break
result = []
outfile = open("result.bin", "wb")
for x in range(len(output)):
	outfile.write(x.to_bytes(4, byteorder='big'))

outfile.close()
    			 

