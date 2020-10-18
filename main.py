# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
import pandas as pd

OUTPUT_INDEX = 10
ATTRIBUTE_BEGIN = 0
ATTRIBUTE_END = 9

df = pd.read_csv("./Admission.csv")

class Node:
    def __init__(self):
        value = None
        attribute = None
        leaves = None

def sum_dict(my_dict):
   sum_ = 0
   for i in my_dict:
      sum_ = sum_ + my_dict[i]
   return sum_

def calc_entropy(value_dict):
    #Entropy(S)=SUM(1,c,-(pi * log(2,pi)) )
    #c is the # of classifications for the attribute
    #pi is the proportion of data with classification i (0-1)

    sum_values = sum_dict(value_dict)

    entropy = 0
    for item in value_dict:
        pi = value_dict[item] / sum_values
        entropy -= (pi * math.log2(pi))

    #return entropy
    return entropy

def count_values(data, index):
    outputs = dict()
    for i in data:
        if i[index] in outputs:
            outputs[i[index]] += 1
        else:
            outputs[i[index]] = 1
    return outputs

def get_entry_list(data, attribute_index, entry):
    new_list = []
    for datum in data:
        if datum[attribute_index] == entry:
            new_list.append(datum)
    return new_list

def calc_info_gain(data, attribute_index):
    info_gain = calc_entropy(count_values(data, OUTPUT_INDEX))

    entries = count_values(data, attribute_index)
    for entry in entries:
        entry_list = get_entry_list(data, attribute_index, entry)
        info_gain -= (entries[entry] / len(data)) * calc_entropy(count_values(entry_list, OUTPUT_INDEX))

    return info_gain


def build_tree(data, curr_node, depth):
    classifications = count_values(data, OUTPUT_INDEX)
    if count_values['no'] == 0:
        curr_node.value = 'Yes'
    elif count_values['yes'] == 0:
        curr_node.value = 'No'
    else:
        #find best attribute A
        max_gain = -1
        max_gain_index = -1
        for i in range(ATTRIBUTE_BEGIN, ATTRIBUTE_END):
            attr_info_gain = calc_info_gain(data, i)
            if attr_info_gain > max_gain:
                max_gain = attr_info_gain
                max_gain_index = i

        #assign A as decision attribute for node N
        curr_node.attribute = max_gain_index

        #for each value of A, create leaves of node N
        values_dict = count_values(data, max_gain_index)
        for value in values_dict:
            new_node = Node()
            new_node.value = value
            curr_node.leaves.append(new_node)
            build_tree(get_entry_list(data, max_gain_index, value), new_node, depth + 1)
    return curr_node

def print_tree(node, depth, attribute):
    for child in node.leaves:
        print_tree(child, depth + 1, node.attribute)
    print(str(depth) + ": " + attribute + "=" + node.value)

print_tree(build_tree(data, Node(), 1)) #FIXME