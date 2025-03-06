
try:
    import sys
    import calculator.operations as cal
    
    print(cal.add(4, 5))
except ModuleNotFoundError as mnfe:
    print(mnfe)
    print('please run:\nuv pip install -e .')
    print('OR')
    print(f'uv run {sys.argv[0]}')