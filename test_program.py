from program import add 
import pytest

def test_add():
    assert add('2,2')==4

def test_add_nothing():
    assert add(',2')==2

def test_add_greater_than_thousand():
    assert add('5, 3000 \n 5')==10

def test_multiple_delimeters():
    assert add("//[*][%]\n1*2%3")==6

def test_negatives():
    with pytest.raises(ValueError) as ve:
        add('5, 9, -2, 9, -32')
    assert 'Negative' in str(ve.value)


