import sys
import numpy as np

pooling_number = int(input('Please enter the pooling number: '))

positive_slices=int(input('How many slices are positive? '))

positive_slice_number={}
for i in range(0,positive_slices):
    positive_slice_number[i+1]=int(input('Please enter positive slice number: '))


slices27={}
slices27[1] = [1,2,3,4,5,6,7,8,9]
slices27[2] = [10,11,12,13,14,15,16,17,18]
slices27[3] = [19,20,21,22,23,24,25,26,27]
slices27[4] = [1,2,3,10,11,12,19,20,21]
slices27[5] = [4,5,6,13,14,15,22,23,24]
slices27[6] = [7,8,9,16,17,18,25,26,27]
slices27[7] = [1,4,7,10,13,16,19,22,25]
slices27[8] = [2,5,8,11,14,17,20,23,26]
slices27[9] = [3,6,9,12,15,18,21,24,27]

#print(slices27)

slices81={}
slices81[1] = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
slices81[2] = [28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54]
slices81[3] = [55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81]
slices81[4] = [1,2,3,4,5,6,7,8,9,28,29,30,31,32,33,34,35,36,55,56,57,58,59,60,61,62,63]
slices81[5] = [10,11,12,13,14,15,16,17,18,37,38,39,40,41,42,43,44,45,64,65,66,67,68,69,70,71,72]
slices81[6] = [19,20,21,22,23,24,25,26,27,46,47,48,49,50,51,52,53,54,73,74,75,76,77,78,79,80,81]
slices81[7] = [1,2,3,10,11,12,19,20,21,28,29,30,37,38,39,46,47,48,55,56,57,64,65,66,73,74,75]
slices81[8] = [4,5,6,13,14,15,22,23,24,31,32,33,40,41,42,49,50,51,58,59,60,67,68,69,76,77,78]
slices81[9] = [7,8,9,16,17,18,25,26,27,34,35,36,43,44,45,52,53,54,61,62,63,70,71,72,79,80,81]
slices81[10] = [1,4,7,10,13,16,19,22,25,28,31,34,37,40,43,46,49,52,55,58,61,64,67,70,73,76,79]
slices81[11] = [2,5,8,11,14,17,20,23,26,29,32,35,38,41,44,47,50,53,56,59,62,65,68,71,74,77,80]
slices81[12] = [3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48,51,54,57,60,63,66,69,72,75,78,81]
#print(slices27)

#all_samples=list(slices27[positive_slice1])+(list(slices27[positive_slice2]))+list(slices27[positive_slice3])
#print(all_samples)





if pooling_number==27:
    all_samples=[]
    for i in range(0,positive_slices):
        all_samples=all_samples+list(slices27[positive_slice_number[i+1]])
    unique_samples = list(np.unique(np.array(all_samples)))
    #print(unique_samples)
    for samples in unique_samples:
        count=all_samples.count(samples)
        if count >= 3:
            print()
            print('Sample ID '+str(samples)+' is positive')
elif pooling_number==81:
    all_samples=[]
    for i in range(0,positive_slices):
        all_samples=all_samples+list(slices81[positive_slice_number[i+1]])
    unique_samples = list(np.unique(np.array(all_samples)))
    #print(unique_samples)
    for samples in unique_samples:
        count=all_samples.count(samples)
        if count >= 4:
            print()
            print('Sample ID '+str(samples)+' is positive')

else:
    print('Wrong pooling number entered. Either 27 or 81 required.')
