#coding=utf8
import unittest
import MinesWeeper
import random

class TestMinesWeeper(unittest.TestCase):
    def set_escenario_1(self):
        matrix_test = [[1,2],[3,4]]
        MinesWeeper.ancho = 2
        MinesWeeper.altura = 2
        MinesWeeper.num_minas = 1
        MinesWeeper.matrix = matrix_test
        MinesWeeper.num_minas = 0
        MinesWeeper.list_posiciones_minas = (random.sample(range(0, (MinesWeeper.altura*MinesWeeper.ancho)), MinesWeeper.num_minas))
        MinesWeeper.list_marcados = []

    def test_tuple_parser(self):
        self.set_escenario_1()
        self.assertEqual(MinesWeeper.tuple_parser(0,0), 0)
        self.assertEqual(MinesWeeper.tuple_parser(0, 1), 1)
        self.assertEqual(MinesWeeper.tuple_parser(0, 2), 2) #El método no verifica que se pase una dupla dentro del las dimensiones adecuadas
        self.assertEqual(MinesWeeper.tuple_parser(1, 0), 2)
        self.assertEqual(MinesWeeper.tuple_parser(1, 1), 3)

    def test_tuple_parser_1(self):
        self.set_escenario_1()
        self.assertNotEqual(MinesWeeper.tuple_parser(0, 0), 1)
        self.assertNotEqual(MinesWeeper.tuple_parser(0, 0), 2)
        self.assertNotEqual(MinesWeeper.tuple_parser(0, 0), 3)

        self.assertNotEqual(MinesWeeper.tuple_parser(0, 1), 0)
        self.assertNotEqual(MinesWeeper.tuple_parser(0, 1), 2)
        self.assertNotEqual(MinesWeeper.tuple_parser(0, 1), 3)

        self.assertNotEqual(MinesWeeper.tuple_parser(1, 0), 0)
        self.assertNotEqual(MinesWeeper.tuple_parser(1, 0), 1)
        self.assertNotEqual(MinesWeeper.tuple_parser(1, 0), 3)

        self.assertNotEqual(MinesWeeper.tuple_parser(1, 1), 0)
        self.assertNotEqual(MinesWeeper.tuple_parser(1, 1), 1)
        self.assertNotEqual(MinesWeeper.tuple_parser(1, 1), 2)

    def test_number_parser(self):
        self.set_escenario_1()
        self.assertEqual(MinesWeeper.number_parser(0), [0,0])
        self.assertEqual(MinesWeeper.number_parser(1), [0, 1])
        self.assertEqual(MinesWeeper.number_parser(2), [1, 0])
        self.assertEqual(MinesWeeper.number_parser(3), [1, 1])

    def test_adjacent_cells(self):
        self.set_escenario_1()
        self.assertEqual(MinesWeeper.adjacent_cells(0,0), [(-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0, -1)])
        self.assertEqual(MinesWeeper.adjacent_cells(0, 1), [(-1, 0), (-1, 1), (-1, 2), (0, 2), (1, 2), (1, 1), (1, 0), (0, 0)])
        self.assertEqual(MinesWeeper.adjacent_cells(1, 0), [(0, -1), (0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (2, -1), (1, -1)])
        self.assertEqual(MinesWeeper.adjacent_cells(1, 1), [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (1, 0)])

    def test_count_adjacent_mines(self):
        self.set_escenario_1()
        #Esta función no se prueba acá debido a que las minas son aleatorias.

    def test_in_matrix(self):
        self.set_escenario_1()
        self.assertTrue(MinesWeeper.in_matrix((0, 0)))
        self.assertTrue(MinesWeeper.in_matrix((0, 1)))
        self.assertTrue(MinesWeeper.in_matrix((1, 0)))
        self.assertTrue(MinesWeeper.in_matrix((1, 1)))

    def test_in_matrix_1(self):
        self.set_escenario_1()
        self.assertFalse(MinesWeeper.in_matrix((-1, -1)))
        self.assertFalse(MinesWeeper.in_matrix((-1, 0)))
        self.assertFalse(MinesWeeper.in_matrix((-1, 1)))
        self.assertFalse(MinesWeeper.in_matrix((-1, 2)))
        self.assertFalse(MinesWeeper.in_matrix((0, 2)))
        self.assertFalse(MinesWeeper.in_matrix((1, 2)))
        self.assertFalse(MinesWeeper.in_matrix((2, 2)))
        self.assertFalse(MinesWeeper.in_matrix((2, 1)))
        self.assertFalse(MinesWeeper.in_matrix((2, 0)))
        self.assertFalse(MinesWeeper.in_matrix((2, -1)))
        self.assertFalse(MinesWeeper.in_matrix((1, -1)))
        self.assertFalse(MinesWeeper.in_matrix((0, -1)))

if __name__ == '__main__':
    unittest.main()