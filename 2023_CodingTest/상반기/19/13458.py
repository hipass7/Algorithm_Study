import unittest
from unittest.mock import Mock

mock = Mock()

class prob(object):
    def __init__(self, num, people, a, b):
        self.num = num
        self.people = people
        self.a = a
        self.b = b
        self.cnt = 0

    def result(self):
        self.cnt = 0
        for i in range(self.num):
            self.people[i] -= self.a
            if self.people[i] < 0:
                self.cnt += 1
                continue
            else:
                div = self.people[i] // self.b
                th = self.people[i] % self.b
                self.cnt += (div + 1)
                while th > 0:
                    th -= self.b
                    self.cnt += 1
        mock.return_value = self.cnt
        return mock()

class Test(unittest.TestCase):
    def test_1(self):
        t = prob(1, [1], 1, 1)
        self.assertEqual(1, t.result())

    def test_2(self):
        t = prob(3, [3, 4, 5], 2, 2)
        self.assertEqual(7, t.result()) # 정답은 원래 7


if __name__ == '__main__':
    unittest.main()
    

