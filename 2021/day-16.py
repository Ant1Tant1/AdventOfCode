from os import error
from utils import readfile
import numpy as np

# read data
data = readfile(r"2021/day-16.txt", my_type=str)
data = data[0]

# data = "26014c875864c464dc64cc643070"

# put data to binary
dt = "".join([bin(int(l, 16))[2:].zfill(4) for l in data])

def get_header(array):
    version = int(array[:3], 2)
    type_id = int(array[3:6], 2)
    return array[6:], version, type_id

def get_litteral_value(array):
    i = 0
    bin_nb = []
    packet_nbs = 0 
    # loop on 1 headers
    while(int(array[i]) == 1):
        bin_nb.append(array[i+1: i+5])
        i += 5
        packet_nbs += 1
    
    # when a 0 arrives
    bin_nb.append(array[i+1: i+5])
    # get literal value
    lit_val = int("".join(bin_nb), 2)
    print(" --> literal value:", lit_val)
    return array[i+5:], lit_val

    # I thought tails counted to write a packet with a given number
    # of hex values but no... 
    packet_nbs += 1
    tail_of_0 = 0#np.mod(packet_nbs*5+6, 4) # +6 for the header
    if (tail_of_0 != 0): tail_of_0 = 4 - tail_of_0
    
    i += 5 + tail_of_0
    lit_val = int("".join(bin_nb), 2)
    print("literal value:", lit_val)
    print("tail", tail_of_0)
    return array[i:], lit_val


def other_packet(array):
    # get type ID
    length_type_ID = int(array[0])
    # print("lenght type ID:", length_type_ID)

    # first case
    if length_type_ID == 0:
        # get total length
        total_length_subpackets = int(array[1:16], 2)
        # print("length subpackets:", total_length_subpackets)

        # defines sub array of wanted length
        sub_array = array[16: 16+total_length_subpackets]

        # while subarray is not empty -> look into it
        vals = []
        while sub_array != "":
            sub_array, val = get_packet(sub_array)
            vals.append(val)
            print(" ** vals:", vals)
        return array[16+total_length_subpackets:], vals

    # second case
    elif length_type_ID == 1:
        # get number of sub array
        nb_subpackets = int(array[1:12], 2)
        # print("nb of subpackets:", nb_subpackets)

        # define new array
        array = array[12:]

        # loop through subarrays
        vals = []
        for i in range(nb_subpackets):
            # print("Loop:", i, nb_subpackets)
            array, val = get_packet(array)
            vals.append(val)
            print(" ** vals:", vals)
        print("end subpacket")
        return array, vals
    else:
        print("ERROR")

def get_packet(array):
    global total_sum_version
    # analyze header
    array, version, type_id = get_header(array)
    # print("len array (minus header):", len(array), "version:", version, "type ID", type_id)
    total_sum_version += version # add to total
    
    val = -1
    # litteral value
    if type_id == 4:
        array, lit_val = get_litteral_value(array)
        return array, lit_val

    # sum subpacket values
    elif type_id == 0:
        print("### SUM")
        array, vals = other_packet(array)
        val = np.sum(vals, dtype=float)
        print("## SUM is:", val, vals)


    # product of sub values
    elif type_id == 1:
        print("### PROD")
        array, vals = other_packet(array)
        val = np.product(vals, dtype=float)
        print("## PROD is:", val, vals)

    # min of sub values
    elif type_id == 2:
        print("### MIN")
        array, vals = other_packet(array)
        val = np.min(vals)
        print("## MIN is:", val, vals)

    # max of sub values
    elif type_id == 3:
        print("### MAX")
        array, vals = other_packet(array)
        val = np.max(vals)
        print("## MAX is:", val, vals)

    # subpacket 1 greater than sub 2 (always 2)
    elif type_id == 5:
        print("### GREATER THAN")
        array, vals = other_packet(array)
        if vals[0] > vals[1]: val = 1 
        else: val = 0
        print("## GREATER THAN is:", val, vals)

    # subpacket 1 less than sub 2 (always 2)
    elif type_id == 6:
        print("### LESS THAN")
        array, vals = other_packet(array)
        if vals[0] < vals[1]: val = 1 
        else: val = 0
        print("## LESS THAN is:", val, vals)

    # subpacket 1  equal to sub 2 (always 2)
    elif type_id == 7:
        print("### EQUAL")
        array, vals = other_packet(array)      
        if vals[0] == vals[1]: val = 1 
        else: val = 0
        print("## EQUAL is:", val, vals)

    if val == -1: return array, None
    return array, val
    


d = dt
total_sum_version = 0
array, val = get_packet(d)
print("First PB:", total_sum_version)
print("2nd PB:", val)
