import unittest

from matrix import neighbor
from weather_chaos import w_chaos
from longest_word import find_longest


class TestMatrix(unittest.TestCase):

    @unittest.skip('Not now')
    def test_34(self):
        matrix = []
        for i in range(3):
            matrix.append([])
            for j in range(4):
                matrix[i].append(i+j)
        call = neighbor(3,4,matrix,0,0)
        result = (1,2)
        self.assertEqual(
            call, result, 'matrix fail'
        )


class TestChaos(unittest.TestCase):

    test_list = [5,3,4,2,5,6,7,2,4,5,6,8,4,3,2,4,6,4,7,8,6,9,7,9,77]
    
    def test_1(self):
        n = 10
        t = self.test_list[0:n]
        call = w_chaos(n,t)
        result = 4
        self.assertEqual(call, result, 'chaos test 1')

    def test_2(self):
        n = 1
        t = self.test_list[0:n]
        call = w_chaos(n,t)
        result = 1
        self.assertEqual(call, result, 'chaos test 2')

    def test_3(self):
        n = 7
        t = [-1, -10, -8, 0, 2, 0, 5]#self.test_list[0:n]
        call = w_chaos(n,t)
        result = 3
        self.assertEqual(call, result, 'chaos test 3')

    def test_4(self):
        n = 10
        t = [-243, -178, -50, -35, 244, -246, -70, 156, -48, 186]
        call = w_chaos(n,t)
        result = 3
        self.assertEqual(call, result, 'chaos test 4')


class TestLongestWord(unittest.TestCase):

    def test_1(self):
        input = 'One two three'
        text = list(map(str, input.strip().split()))
        l = len(text)

        call = find_longest(l,text)
        result = 'three', 5
        self.assertEqual(call, result, 'longest word test 1')

    def test_2(self):
        input = 'frog jumps from river'
        text = list(map(str, input.strip().split()))
        l = len(text)

        call = find_longest(l,text)
        result = ('jumps', 5)
        self.assertEqual(call, result, 'longest word test 2')

if __name__ == '__main__':
    unittest.main()
