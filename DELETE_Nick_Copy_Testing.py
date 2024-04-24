# Import pytest
import pytest, sys

def method_under_test():
    print("Hallo, Welt!")
    return 41

# Write a test function to test the modified readouterr() method
def test_readouterr_no_reset(capsys):
    result = method_under_test()
    print(dir(capsys))
    out, err = capsys.copyouterr()
    sys.stdout.write(out)
    sys.stderr.write(err)
    assert out.startswith("Hello")
    assert result == 42