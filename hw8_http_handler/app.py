
import sys
from utils import string_to_operator
from logger_helper import get_logger
#from log_config import dict_config
import logging
from logging_tree import printout, format





def calc(args):
    #print("Arguments: ", args)
    calculator_logger.info(f'Arguments: {args}')

    num_1 = args[0]
    operator = args[1]
    num_2 = args[2]

    try:
        num_1 = float(num_1)
    except ValueError as e:
        calculator_logger.error(f'Error while converting number 1. Код ошибки - {e}')
        #print("Error while converting number 1")
        #print(e)

    try:
        num_2 = float(num_2)
    except ValueError as e:
        calculator_logger.error(f'Error while converting number 2. Код ошибки - {e}')
        #print("Error while converting number 2")
        #print(e)

    operator_func = string_to_operator(operator)

    result = operator_func(num_1, num_2)
    calculator_logger.info(f"Result: {result} " )
    calculator_logger.info(f"{num_1} {operator} {num_2} = {result}")

    #print("Result: ", result)
    #print(f"{num_1} {operator} {num_2} = {result}")


if __name__ == '__main__':
    #logging.config.dictConfig(dict_config)
    #calculator_logger = logging.getLogger('calculator_logger')
    calculator_logger = get_logger('calculator_logger')
    utils_logger = get_logger('utils_logger')
    #printout()
    #with open('logging_tree.txt' , 'w') as tree_file:
    #    tree_file.write(format.build_description())
    calculator_logger.info('Привет')
    utils_logger.info('hello')

    calc('5**3')
