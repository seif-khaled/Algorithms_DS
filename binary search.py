import math


def binary_search(arr,element):
    low=0
    high=len(arr)-1
    mid=int((low+high)/2)
    flag=0
    while(flag==0):
        print(mid)
        if high<low:
            flag=1
            return -1,"could find element"
        if element==arr[mid]:
            flag=1
            return arr[mid],mid
        else:
            if element<arr[mid]:
                high=mid-1
            elif element>arr[mid]:
                low=mid+1
        mid=int((low+high)/2)
        
x=[223, 553, 46, 289, 94, 843, 692, 419, 753, 133, 178
   , 237, 310, 692, 278, 504, 230
   , 223, 402, 606, 567, 491, 237, 391, 357, 667, 818, 419, 317, 422, 517, 725, 742, 67, 242, 500, 
   515, 108, 840, 431, 341, 178, 427, 633, 95, 996, 852, 516, 916, 46, 338, 644, 155, 333, 538, 691, 968, 380, 49, 90, 832, 644, 804,
   727, 198, 857, 694, 120, 617, 874, 534, 732, 891, 163, 517, 5, 771, 414, 969, 786, 898, 868, 254, 993, 901, 670, 457, 436, 350, 86, 770, 158,
   292, 528, 715, 109, 649, 695, 790, 323, 178, 462, 223, 708, 605, 94, 380, 296, 597, 622, 563, 250, 94, 799, 733, 627, 68, 861, 966, 130, 430, 533, 316, 228,
   528, 239, 935, 932, 47, 274, 5, 244, 172, 240, 288, 113, 197, 347, 61, 334, 911, 629, 609, 44, 970, 527, 226, 178, 431, 347, 551, 240, 239, 273, 475, 50, 241, 143
   , 188, 790, 263, 204, 802, 416, 911, 494, 927, 287, 350, 403, 246, 230, 450, 996, 376, 483, 539, 577, 701, 699, 483, 570, 345, 795, 960, 428, 978, 897, 185, 960, 
   510, 493, 660, 250, 399, 743, 933, 257, 367, 426, 156, 75, 414, 284, 437, 899, 543, 58, 183, 112, 780, 365, 905, 659, 221, 690, 361, 925, 198, 123, 177, 572, 959, 
   573, 715, 411, 586, 530, 741, 846, 266, 994, 803, 63, 37, 580, 704, 149, 351, 428, 282, 396, 9, 603, 226, 766, 176, 45, 410, 170, 
   711, 804, 482, 712, 550, 467, 697, 5, 726, 799, 640, 332, 757, 384, 781, 544, 414, 146, 723, 565, 489,
   87, 897, 975, 621, 210, 444, 76, 705, 634, 281, 528, 423, 571, 361, 656, 983, 913, 210, 796, 301, 907, 962, 226, 541, 475, 663, 110, 275, 960, 907, 479, 867, 
   421, 850, 251, 855, 435, 125,125, 335, 542, 821, 305, 133]
# x=[1,2,3]
# print(x.count(125))
# print(len(x))
x.sort()
print(binary_search(x,125))