from os import popen
from pathlib import Path
import subprocess

# get expected input/output file
current_folder = Path(__file__).parent

'''
There are three test parts in the Create_product test which are the
input test, output test and function test.
test_update_profile_1 represents the test of input, test all possibilities
of input(one test case for each category)
test_update_profile_2 represents the test of output, test all possibilities
of out(one test case for each category)
test_update_profile_3 represents the test of function, to test the function,
we need to make sure that the profile has been updated.
To test that, we can relogin.
'''


def test_update_profile_1():
    """capsys -- object created by pytest to
    capture stdout and stderr"""

    # read expected in/out
    expected_in = open(current_folder.joinpath(
        'test_update_profile_1.in'))
    expected_out = open(current_folder.joinpath(
        'test_update_profile_1.out')).read().replace('\n', '')
    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode().replace('\r', '').replace('\n', '')
    print('outputs', output)
    assert output.strip() == expected_out.strip()


def test_update_profile_2():
    """capsys -- object created by pytest to
    capture stdout and stderr"""

    # read expected in/out
    expected_in = open(current_folder.joinpath(
        'test_update_profile_2.in'))
    expected_out = open(current_folder.joinpath(
        'test_update_profile_2.out')).read().replace('\n', '')
    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode().replace('\r', '').replace('\n', '')
    print('outputs', output)
    assert output.strip() == expected_out.strip()


def test_update_profile_3():
    """capsys -- object created by pytest to
    capture stdout and stderr"""

    # read expected in/out
    expected_in = open(current_folder.joinpath(
        'test_update_profile_3.in'))
    expected_out = open(current_folder.joinpath(
        'test_update_profile_3.out')).read().replace('\n', '')
    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode().replace('\r', '').replace('\n', '')
    print('outputs', output)
    assert output.strip() == expected_out.strip()