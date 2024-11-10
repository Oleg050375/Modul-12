import runner  # импорт модуля, где находится тестируемый класс
import unittest


class RunnerTest(unittest.TestCase):  # тестовый класс
    def test_walk(self):
        obj1 = runner.Runner('cup')
        for i in range(10):
            obj1.walk()
        self.assertEqual(obj1.distance, 50)

    def test_run(self):
        obj2 = runner.Runner('table')
        for i in range(10):
            obj2.run()
        self.assertEqual(obj2.distance, 100)

    def test_challenge(self):
        obj3 = runner.Runner('milk')
        obj4 = runner.Runner('beer')
        for i in range(10):
            obj3.walk()
        for i in range(10):
            obj4.run()
        self.assertNotEqual(obj3.distance, obj4.distance)


if __name__ == '__main__':
    unittest.main
