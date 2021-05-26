'''
@File: matrix_app.py
@author: Dawson C. Branch
@since: 4/7/21
@summary: A program that asks for user information and allows them to perform matrix operations.
'''

import re
import numpy as np


PLAYING = ""
OPTION =''

USERS = []

MATRIX_ONE = []
MATRIX_TWO = []
RESULTS = []


def play_or_nay():
    '''Asks the user if they want to play and returns the answer string'''
    option = ""
    while option.lower() not in {"yes","y","no","n"}:
        if option != "":
            print("Invalid answer.")
        option = str(input("Do you want to play the Matrix Game (Yes/No)?\n"))
    return option.lower()


def grab_info():
    '''Prompts the user for and stores their name, number, and zip code'''
    user = {
    "name": "",
    "phone": "",
    "zip_code": ""
    }
    temp_name = ""
    temp_num = ""
    temp_zip = ""

    while temp_name == "":
        temp_name = str(input("Enter your name: "))

    while not re.fullmatch("^[0-9]{3}-[0-9]{3}-[0-9]{4}$", temp_num) or temp_num == "":
        if not re.fullmatch("^[0-9]{3}-[0-9]{3}-[0-9]{4}$", temp_num) and temp_num != "":
            print("Invalid input.")
        temp_num = str(input("Enter your phone number (XXX-XXX-XXXX): "))

    while not re.fullmatch("^[0-9]{5}-[0-9]{4}$", temp_zip) or temp_zip == "":
        if not re.fullmatch("^[0-9]{5}-[0-9]{4}$", temp_zip) and temp_zip != "":
            print("Invalid input.")
        temp_zip = str(input("Enter your zip code+4 (XXXXX-XXXX): "))

    user['name'] = temp_name
    user['phone'] = temp_num
    user['zip_code'] = temp_zip
    return user


def matrix_maker (row_num , col_num):
    '''Creates and returns a matrix of the passed row and column numbers'''
    temp_matrix =[]
    temp_row = []
    temp_in = ""
    any_number_expr = "[+-]?([0-9]+([.][0-9]*)?|[.][0-9]+)"
    row_regex = "^("+any_number_expr+" ){"+str(col_num - 1)+"}"+any_number_expr+"$"

    for _ in range(row_num):
        while not re.fullmatch(row_regex, temp_in):
            if not re.fullmatch(row_regex, temp_in) and temp_in != "":
                print("Invalid row. Please reenter:")
            temp_in = input()
        temp_row = temp_in.split(' ', col_num)
        temp_matrix += [temp_row]
        temp_in = ""

    return temp_matrix


def matrix_to_string (arg_matrix):
    '''Returns a reformatted matrix string'''
    temp_str = ""

    for j in arg_matrix:
        temp_str += (str(j)
                        .replace("[", "")
                        .replace("]", "")
                        .replace("'", "")
                        .replace("  ", "")
                        .replace(",", " "))
        temp_str += "\n"

    return temp_str


def matrix_addition(arg_matrix_1, arg_matrix_2):
    '''Adds two matrices together and returns them'''
    result_matrix = []
    temp_row = []
    temp_element = 0

    for j in range(arg_matrix_1.shape[0]):
        temp_row = []
        for i in range(arg_matrix_1.shape[1]):
            temp_element = float(arg_matrix_1[j,i]) + float(arg_matrix_2[j,i])
            temp_row.append(temp_element)
        result_matrix.append(temp_row)
    return result_matrix


def matrix_subtraction(arg_matrix_1, arg_matrix_2):
    '''Subtracts one matrix from another and returns the difference'''
    result_matrix = []
    temp_row = []
    temp_element = 0

    for j in range(arg_matrix_1.shape[0]):
        temp_row = []
        for i in range(arg_matrix_1.shape[1]):
            temp_element = float(arg_matrix_1[j,i]) - float(arg_matrix_2[j,i])
            temp_row.append(temp_element)
        result_matrix.append(temp_row)
    return result_matrix


def ele_by_ele_mul(arg_matrix_1, arg_matrix_2):
    '''Multiplies the elements of two matrices to form and return a resulting matrix'''
    result_matrix = []
    temp_row = []
    temp_element = 0

    for j in range(arg_matrix_1.shape[0]):
        temp_row = []
        for i in range(arg_matrix_1.shape[1]):
            temp_element = float(arg_matrix_1[j,i]) * float(arg_matrix_2[j,i])
            temp_row.append(temp_element)
        result_matrix.append(temp_row)
    return result_matrix


def elements_to_float(arg_matrix):
    '''Converts all of a matrix's elements into ints and returns the resulting matrix'''
    result_matrix = []
    temp_row = []
    temp_element = 0

    for j in range(arg_matrix.shape[0]):
        temp_row = []
        for i in range(arg_matrix.shape[1]):
            temp_element = float(arg_matrix[j,i])
            temp_row.append(temp_element)
        result_matrix.append(temp_row)
    return result_matrix





print("********* Welcome to Dawson's Python Matrix Application *********")

while True:
    PLAYING = play_or_nay()
    if PLAYING.lower() in {"no","n"}:
        break
    USERS += [grab_info()]
    print("Enter your first 3x3 matrix (Elements separated a space, rows on separate lines):")
    MATRIX_ONE = np.array(matrix_maker(3, 3))

    print("Your first 3x3 matrix is:")
    print(matrix_to_string(MATRIX_ONE))

    print("Enter your second 3x3 matrix (Elements separated a space, rows on separate lines):")
    MATRIX_TWO = np.array(matrix_maker(3, 3))

    print("Your second 3x3 matrix is:")
    print(matrix_to_string(MATRIX_TWO))

    print("Select a Matrix Operation from the list below:")
    print("a. Addition")
    print("b. Subtraction")
    print("c. Matrix Multiplication")
    print("d. Element by element multiplication")
    OPTION = ""
    while re.fullmatch("^[a-d]{1}$", OPTION.lower()) is None:
        if OPTION != "":
            print("Invalid input.")
        OPTION = input()

    if OPTION == 'a':
        print("You selected Addition. The results are:")
        RESULTS = matrix_addition(MATRIX_ONE, MATRIX_TWO)
        print(matrix_to_string(RESULTS))

        print("The Transpose is:")
        print(matrix_to_string(np.transpose(RESULTS)))

        print("The row and column mean values of the results are:")
        print("Row: "+str(np.mean(RESULTS,axis=1)))
        print("Column: "+str(np.mean(RESULTS,axis=0)))

    elif OPTION == 'b':
        print("You selected Subtraction. The results are:")
        RESULTS = matrix_subtraction(MATRIX_ONE, MATRIX_TWO)
        print(matrix_to_string(RESULTS))

        print("The Transpose is:")
        print(matrix_to_string(np.transpose(RESULTS)))

        print("The row and column mean values of the results are:")
        print("Row: "+str(np.mean(RESULTS,axis=1)))
        print("Column: "+str(np.mean(RESULTS,axis=0)))

    elif OPTION == 'c':
        print("You selected Matrix Multiplication. The results are:")
        RESULTS = np.matmul(elements_to_float(MATRIX_ONE), elements_to_float(MATRIX_TWO))
        print(matrix_to_string(RESULTS))

        print("The Transpose is:")
        print(matrix_to_string(np.transpose(RESULTS)))

        print("The row and column mean values of the results are:")
        print("Row: "+str(np.mean(RESULTS,axis=1)))
        print("Column: "+str(np.mean(RESULTS,axis=0)))

    elif OPTION == 'd':
        print("You selected Element-By-Element Multiplication. The results are:")
        RESULTS = ele_by_ele_mul(MATRIX_ONE, MATRIX_TWO)
        print(matrix_to_string(RESULTS))

        print("The Transpose is:")
        print(matrix_to_string(np.transpose(RESULTS)))

        print("The row and column mean values of the results are:")
        print("Row: "+str(np.mean(RESULTS,axis=1)))
        print("Column: "+str(np.mean(RESULTS,axis=0)))

print("**************** Thanks for PLAYING Python Numpy ****************")
