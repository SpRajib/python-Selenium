import pytest
#############
# module level
#################
# pytestmark = pytest.mark.imp

@pytest.mark.smoke
def test_login():
    print("login page testcase")

@pytest.mark.p3
@pytest.mark.smoke
def test_trash():
    print("trash page testcase")

@pytest.mark.reg
def test_compose():
    print("compose page testcase")

@pytest.mark.p3
def test_bin():
    print("bin page testcase")

#############################
# Method Level
############################

class TestInsta:
    @pytest.mark.regression
    @pytest.mark.high
    def test_post(self):
        print("post page testcase")

    @pytest.mark.critical
    def test_story(self):
        print("story page testcase")

    @pytest.mark.regression
    @pytest.mark.low
    def test_chat(self):
        print("chat page testcase")

    # @pytest.mark.regression
    # def chat(self):
    #     print("chat page testcase")

    @pytest.mark.high
    def test_register(self):
        print("register page testcase")

#######################
# class level
########################
@pytest.mark.imp
class TestInsta:
    @pytest.mark.m1
    def test_post(self):
        print("post page testcase")

    def test_story(self):
        print("story page testcase")

class TestFb:
    @pytest.mark.m2
    def test_chat(self):
        print("chat page testcase")

    @pytest.mark.m1
    def test_register(self):
        print("register page testcase")

@pytest.mark.imp
class TestSample:
    def test_sample(self):
        print("sample page testcase")