from searching_alg import condense_list, search
import unittest
import time

teacher = {'a': 1, 'b': 0, 'c': 1, 'd': 0, 'e': 2, 'f': 0, 'g': 0, 'h': 1, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 1, 's': 0, 't': 1, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

rndomlettres = {'a': 0, 'b': 0, 'c': 0, 'd': 1, 'e': 2, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 1, 'm': 1, 'n': 1, 'o': 1, 'p': 0, 'q': 0, 'r': 2, 's': 1, 't': 2, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

class TestCondenseList(unittest.TestCase):
  def test_teacher(self):
    self.assertTrue(teacher == condense_list(list("teacher")))

  def test_rndomlettres(self):
    self.assertTrue(rndomlettres == condense_list(list("rndomlettres")))

  def test_perf(self):
    start_time = time.time()
    search("techer")
    end_time = time.time()

    elapsed_time = end_time-start_time
    print("test_perf took "+str(elapsed_time)+" seconds.")


if __name__ == '__main__':
  unittest.main()