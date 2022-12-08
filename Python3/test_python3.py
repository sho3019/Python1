import pytest
import pytest
import json

from Python3.python3_1 import Check, Evaluation, Make_json, Error
check = Check()
evaluation = Evaluation()
make_json = Make_json()
error = Error()
#def test_check_teacher():
    #assert check.check_teacher(2, 8) == ([1, 1], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 1, 0, 0, 0, 0])

def test_check_error():
    assert error.check_error([0 ,0 ,0, 0, 0, 0, 0, 0, 0, 0], 2) == "OK"
    assert error.check_error([0 ,0 ,0, 0, 0, 0, 0, 1, 0, 0], 2) == "error data is contain"

def test_judge_evaluation():
    assert evaluation.judge_evaluation([57, 493, 250, 145, 333]) == ["E", "A", "C", "D", "B"]

def test_output_json():
    assert make_json.output_json(["E", "A", "C", "D", "B", "B", "A", "C"], 2) == 0

def test_total_score():
    assert evaluation.total_score(2) 

