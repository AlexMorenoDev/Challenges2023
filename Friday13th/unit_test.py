"""
 * Crea tres test sobre el reto 12: "Viernes 13".
 * - Debes emplear un mecanismo de ejecución de test que posea
 *   el lenguaje de programación que hayas seleccionado.
 * - Los tres test deben de funcionar y comprobar
 *   diferentes situaciones (a tu elección).
"""

import unittest
from calendar import IllegalMonthError
from functions.functions import is_friday_13th, is_friday_13th_2


class TestFriday13th(unittest.TestCase):
    def test_false(self):
        self.assertFalse(is_friday_13th(11, 2010))

    def test_true(self):
        self.assertTrue(is_friday_13th(10, 2023))

    def test_calendar_exception(self):
        self.assertRaises(IllegalMonthError, is_friday_13th, 42, 2023)

    def test_datetime_exception(self):
        self.assertRaises(ValueError, is_friday_13th_2, 75, 2023)


def main():
    unittest.main()


if __name__ == "__main__":
    main()