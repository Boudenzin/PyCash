import unittest
from main import buscar_produto
from decimal import Decimal

class TestCaixaRegistradora(unittest.TestCase):

    def test_produto_existente(self):
        """Testa se um produto existente é retornado corretamente"""
        codigo_valido = "7123456789012" 
        resultado = buscar_produto(codigo_valido)
        self.assertIsNotNone(resultado, "Produto existente não foi encontrado.")
        self.assertIsInstance(resultado, tuple)
        self.assertEqual(len(resultado), 2)
        self.assertIsInstance(resultado[0], str)  # nome
        self.assertIsInstance(resultado[1], (float, int, Decimal))  # preco

    def test_produto_inexistente(self):
        """Testa se buscar um produto inexistente retorna None"""
        codigo_invalido = "0000000000000"
        resultado = buscar_produto(codigo_invalido)
        self.assertIsNone(resultado, "Produto inexistente deveria retornar None")

if __name__ == '__main__':
    unittest.main()
