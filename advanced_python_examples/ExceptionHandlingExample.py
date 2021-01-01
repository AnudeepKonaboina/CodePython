# Exception -An unwanted unexpected event which causes abnormal termination of the program is an Exception
# whenever an exception is generated a default exeption object is created by the PVM and is displayed on the console.
# Once PVM generates the exception object it will look whether any handling code is present or not.
# Exception handling is done using try ,except ,else and finally.
# try-risky code,catch- handling code ,Finally-clean up code,else-if no exception in try block
# order of blocks is try-except-else-finally


# Example of try-except
try:
    print(10 / 2)  # 5.0 no exception so no except
    print(10 / 0)  # divide by zero exception
except ArithmeticError as e:
    print(e)  # name of the error
    print(type(e))  # type of Exception
    print(e.__class__.__name__)  # classname
print('code done')  # this will be ececuted as the exception is handled

# Example try with multiple excepts until exception is matched pvm will search for required handling exeption
try:
    x = int(input('provide value of x:'))
    y = int(input('provide value of y:'))
    print(x / y)
except ArithmeticError as ae:
    print(ae)
except ValueError as ve:
    print('provide int values only')

# Default except block example
try:
    x = int(input('provide value of x:'))
    y = int(input('provide value of y:'))
    print(x / y)
except ArithmeticError as ae:
    print(ae)
except:  # Executes only if other than Zero Div error is raised.Can handle any kind of Exception.Compulsory it must be the last block or we will get syntax error
    print('provide int values only')

# Various combinations of except block
try:
    x = int(input('provide value of x:'))
    y = int(input('provide value of y:'))
    print(x / y)
except ArithmeticError as ae:
    print(ae)
except (ArithmeticError) as ae:  # other way
    print(ae)
except ValueError as ve:
    print('provide int values only')
except:  # Executes only if other than Zero Div error is raised.Can handle any kind of Exception.
    # Compulsory it must be the last block or we will get syntax error
    print('provide int values only')

# Finally--cleanup code always .Cant be written in try or catch block.
try:
    print(10 / 2)  # 5.0 no exception so no except
    print(10 / 0)  # diviide by zero exception
except ArithmeticError as e:
    print(e)  # name of the error
    print(type(e))  # type of Exception
    print(e.__class__.__name__)  # classname
finally:
    print('code done')

# Else block-is executed when there is no exception in try
# Else and except are contradicting parts
# else block cannot be written without except or befor except- we
try:
    print('try')
except:
    print('Except')
else:
    print('else')
finally:
    print('finally')

# user defined exceptions using raise keyword
try:
    raise Exception("My exception")  # similar to throw in java for explicitly raising an exception
except:
    print("exception handled")
