try:
    import calculator.operations as cal
    
    print(cal.add(4, 5))
except ModuleNotFoundError:
    print('please run:\nuv pip install -e .')
