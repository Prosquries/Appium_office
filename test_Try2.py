import pytest

def setup_function(module):
    print("setup_function in module")

def teardown_function(function):
    print("Closing teardown function")

def setup_module(module):
    print("module level")

def teardown_module(module):
    print("closing teardown in module")

def test_demo1():
    print("Demo pytest")

def test_demo2():
    print("Demo pytest2")