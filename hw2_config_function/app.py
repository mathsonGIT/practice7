import sys
from utils import string_to_operator
import logging

#calculator_logger = logging.getLogger('Calculator Logger')
custom_handler = logging.StreamHandler(stream=sys.stdout)
custom_handler.setFormatter(logging.Formatter(fmt = '%(levelname)s | %(name)s | %(asctime)s | %(lineno)s| %(message)s'))
#calculator_logger.addHandler(custom_handler)

logging.basicConfig(handlers=[custom_handler], level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
calculator_logger = logging.getLogger('Calculator Logger')

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
    # calc(sys.argv[1:])
    logging.basicConfig(level='INFO')
    calc('2^a')
