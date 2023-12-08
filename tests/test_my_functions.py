import pytest
import myfunctions.myfunctions as mf
import create_database_master.wrangle_database_master as wd
import create_database_master.excel_io_dataframe as xl



def test_add():
    result = mf.add(4, 1)
    assert result == 5

def test_divide():
    result = mf.divide(10,5)
    assert result == 2

def test_divideByZero():
    with pytest.raises(ValueError):
        mf.divide(10,0)

def test_concat_case1():
    with pytest.raises(AttributeError):
        result = mf.concatStr(1,'hello')

def test_concat_case2():
    with pytest.raises(AttributeError):
        result = mf.concatStr('Hello',1)

def test_concat_case3():
    result = mf.concatStr('hello','World')
    assert result == 'hello world'

