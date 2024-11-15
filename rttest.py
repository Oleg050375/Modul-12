import runner_and_tournament as rat
import unittest


class TournamentTest(unittest.TestCase):
    is_frozen = True  # атрибут заморозки тестов

    @classmethod
    def setUpClass(cls):  # создание атрибута класса тестирования в виде пустого списка результатов соревнований
        TournamentTest.all_results = []

    def setUp(self):  # создание объектов-бегунов и забегов
        self.runner1 = rat.Runner('Усэйн', 10)
        self.runner2 = rat.Runner('Андрей', 9)
        self.runner3 = rat.Runner('Ник', 3)
        self.beg1 = rat.Tournament(90, self.runner1, self.runner3)
        self.beg2 = rat.Tournament(90, self.runner2, self.runner3)
        self.beg3 = rat.Tournament(90, self.runner1, self.runner2, self.runner3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):  # тестирование метода run
        self.runner1.run()
        self.assertEqual(self.runner1.distance, 20)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):  # тестирование метода walk
        self.runner2.walk()
        self.assertEqual(self.runner2.distance, 9)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tr_1(self):  # тестирование метода start 1-го забега
        a = self.beg1.start()  # применение метода start
        for i in range(1, len(a)+1):  # трансоформация формата результатов забега
            a[i] = str(a.get(i))
        self.all_results.append(a)  # добавление результатов забега в общий список результатов соревнований
        self.assertTrue(a.get(len(a)) == 'Ник')  # тетсирование на корректность

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tr_2(self):  # тестирование метода start 2-го забега
        b = self.beg2.start()
        for i in range(1, len(b)+1):
            b[i] = str(b.get(i))
        self.all_results.append(b)
        self.assertTrue(b.get(len(b)) == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tr_3(self):  # тестирование метода start 3-го забега
        c = self.beg3.start()
        for i in range(1, len(c)+1):
            c[i] = str(c.get(i))
        self.all_results.append(c)
        self.assertTrue(c.get(len(c)) == 'Ник')

    @classmethod
    def tearDownClass(cls):
        for i in TournamentTest.all_results:  # цикл печати результатов соревнований
            print(i)

if __name__ == '__main__':
    unittest.main
