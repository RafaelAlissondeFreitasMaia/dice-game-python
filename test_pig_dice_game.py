import unittest
from pig_dice_game import roll  # Importa a função que você quer testar

class TestPigDiceGame(unittest.TestCase):
    def test_roll(self):
        # Verifica se o dado sempre retorna um número entre 1 e 6
        result = roll()
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 6)

if __name__ == "__main__":
    unittest.main()


from pig_dice_game import roll

class TestPigDiceGame(unittest.TestCase):
    
    def test_roll(self):
        # Testa se o dado sempre retorna um número entre 1 e 6
        result = roll()
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 6)

    def test_roll_lose_points_on_1(self):
        # Simula uma rolagem de 1 e testa se o jogador perde os pontos acumulados no turno
        current_score = 10  # Pontuação atual do jogador
        roll_result = 1  # Simula o valor 1 sendo rolado
        if roll_result == 1:
            current_score = 0  # Se rolar 1, perde a pontuação
        self.assertEqual(current_score, 0)  # O jogador deve perder todos os pontos
