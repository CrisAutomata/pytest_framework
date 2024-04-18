
## Prerequisites:
python>= 3.10

## Install Libs
```sh
pip install -r requirements.txt
```

## Running command
Run these commands to execute test and you can see new result comes up in a new sheet of "test_report.xlsx" file:
there are 2 different test suites you can test:

The 1st test suite include: test_1, test_2, test_3
```sh
pytest test/test_suite_1.py -rA -v --junitxml=test_result.xml
```
The 2nd test suite include: test_4, test_5, test_6
```sh
pytest test/test_suite_2.py -rA -v --junitxml=test_result.xml
```

