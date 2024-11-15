import unittest
import rttest  # подключение файла, содержащего test case
import vintest  # подключение файла, содержащего test case

TS = unittest.TestSuite()  # объект класса suite

TS.addTest(unittest.TestLoader().loadTestsFromTestCase(vintest.RunnerTest))  # подключение теста
TS.addTest(unittest.TestLoader().loadTestsFromTestCase(rttest.TournamentTest))  # подключение теста

TR = unittest.TextTestRunner(verbosity=2)  # объект запускальщик )))

TR.run(TS)  # запуск тестирования