import os.path
import sys
from PP1_2 import *

def test_q1(capsys):

  try:
    exists = os.path.exists("PP1_2.py")
    assert exists
  except:
    sys.exit()

  q1()
  captured = capsys.readouterr()
  assert captured.out == "Alex\n"

def test_q2(capsys):

  try:
    exists = os.path.exists("PP1_2.py")
    assert exists
  except:
    sys.exit()

  q2()
  captured = capsys.readouterr()
  assert captured.out == "10\n"

def test_q3(capsys):

  try:
    exists = os.path.exists("PP1_2.py")
    assert exists
  except:
    sys.exit()

  q3()
  captured = capsys.readouterr()
  assert captured.out == "5\n"

def test_q4(capsys):

  try:
    exists = os.path.exists("PP1_2.py")
    assert exists
  except:
    sys.exit()

  q4()
  captured = capsys.readouterr()
  assert captured.out == "2.1\n"

def test_q5(capsys):

  try:
    exists = os.path.exists("PP1_2.py")
    assert exists
  except:
    sys.exit()

  q5()
  captured = capsys.readouterr()
  assert captured.out == "Hello World\nGoodbye World\n"

def test_q6(capsys):

  try:
    exists = os.path.exists("PP1_2.py")
    assert exists
  except:
    sys.exit()

  q6()
  captured = capsys.readouterr()
  assert captured.out == "true\n"

def test_q7(capsys):

  try:
    exists = os.path.exists("PP1_2.py")
    assert exists
  except:
    sys.exit()

  q7()
  captured = capsys.readouterr()
  assert captured.out == "1\n"
