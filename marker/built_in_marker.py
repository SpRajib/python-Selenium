import pytest
#----------------------
# skip marker
#---------------------

###################
## function level
# ###################
def test_TC1():
    print("Test case 1")
@pytest.mark.skip(reason="low priority")
def test_TC2():
    print("Test case 2")

def test_TC3():
    print("Test case 3")

@pytest.mark.skip(reason="not important")
def test_TC4():
    print("Test case 4")

###################
## class level
# ###################
@pytest.mark.skip(reason="all method are not required")
class TestSample:
    def test_tc1(self):
        print("testcase1")
    def test_tc2(self):
        print("testcase2")
class TestSimple:
    def test_tc3(self):
        print("testcase3")
    def test_tc4(self):
        print("testcase4")


#----------------------
# skip if marker
#---------------------

###################
## function level
# ###################

testid = 3423
def test_TC1():
    print("testcas1")
@pytest.mark.skipif(testid in [5671, 2233, 3423, 7890], reason="test_case not required")
def test_TC2():
    print("testcas2")
def test_TC3():
    print("testcas3")


testid = 3428
def test_TC1():
    print("testcas1")
@pytest.mark.skipif(testid in [5671, 2233, 3423, 7890], reason="test_case not required")
def test_TC2():
    print("testcas2")
def test_TC3():
    print("testcas3")

###################
## class level
# ###################
browser="IE"
class TestDemo:
    def test_Tc1(self):
        print("method1 testcase")
    def test_Tc2(self):
        print("method2 testcase")
@pytest.mark.skipif(browser=="IE", reason="IE not exists")
class TestSample:
    def test_Tc3(self):
        print("method3 testcase")
    def test_Tc4(self):
        print("method4 testcase")

#----------------------
# XFAIL marker
#---------------------
def test_chat():
    print("chat module")
def test_status():
    print("status module")
@pytest.mark.xfail
def test_channel():
    print("channel module")


brw = "IE"
def test_chat():
    print("chat module")
def test_status():
    print("status module")
@pytest.mark.xfail(brw in ["mozilla","chrome", "IE"], reason="not implemented")
def test_channel():
    print("channel module")
"""
>pytest -vs pytestconcept.py
collected 3 items
pytestconcept.py::test_chat chat module
PASSED
pytestconcept.py::test_status status module
PASSED
pytestconcept.py::test_channel channel module
XPASS (not implemented)
"""

brw = "safari"
def test_chat():
    print("chat module")
def test_status():
    print("status module")
@pytest.mark.xfail(brw in ["mozilla","chrome", "IE"], reason="not implemented")
def test_channel():
    print("channel module")

"""
>pytest -vs pytestconcept.py
collected 3 items
pytestconcept.py::test_chat chat module
PASSED
pytestconcept.py::test_status status module
PASSED
pytestconcept.py::test_channel channel module
PASSED
"""