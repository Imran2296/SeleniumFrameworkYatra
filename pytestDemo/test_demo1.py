#any pytest file should start with ' test_' or end with '_test'
#pytest required test method name
#any code should be wrapped in method only
#methid name should have sense
# -k stands for method ma,es execution, -s logs in output -v stands for more info metadata
#you can run specific file with py.test <filename>
#fixtures are used as setup and tear down methods for test cases - conftest file to generalize-
#fixture and make it available to all test cases
#data driven and parameterization can be done with return statements in tuple format
#when you define fixture scope to class only, it will run once before class is initiated and at the end

def test_firstPrgrm():
    print("gud mrng")

def test_secondPage():
    print("bad mrng")