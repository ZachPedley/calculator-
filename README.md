
A Python 3 calculator used from the Terminal, built step by step in SCCM4910.

## What it will do
Add, subtract, multiply and divide two numbers; display the result.

## How to run it
From Week 3: python3 calculator.py
Enter the first number, operator (+ - * /), then second number.
The program prints Result: followed by the answer.

## prerequisits
python3 

##What to run and expect
Run:
./run.sh   --> run the calculator
./check.sh --> test the outputs of the calculator (expect 5 passed tests)
echo $?    --> check the exit status
0 = Success
1= Something failed
5 = No test collected

Example test:
6 * 7
expected result:
42.0
enter Ctrl C to exit the running calculator 

Activate SCCM4910 environment:
source /opt/python-venv/sccm-4910/bin/activate
python3 -m pytest --version (Expect a version to be displayed)
