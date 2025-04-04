import unittest
from app.validacao import validar_cpf

class TestValidarCPF(unittest.TestCase):

    def test_cpf_valido(self):
        self.assertTrue(validar_cpf("529.982.247-25"))  # CPF real válido
        self.assertTrue(validar_cpf("012.345.678-90"))  # Outro CPF válido
        self.assertFalse(validar_cpf("000.000.000-00"))  # CPF inválido com números repetidos
        self.assertFalse(validar_cpf("111.111.111-11"))  # Outro CPF inválido

    def test_cpf_invalido_formato(self):
        self.assertFalse(validar_cpf("1234567890"))  # CPF com menos de 11 dígitos
        self.assertFalse(validar_cpf("123.456.789-0"))  # CPF incompleto
        self.assertFalse(validar_cpf("abc.def.ghi-jk"))  # CPF com letras
        self.assertFalse(validar_cpf("1111.22222-12"))  # Formato incorreto

    def test_cpf_invalido_digito(self):
        self.assertFalse(validar_cpf("123.456.789-00"))  # CPF com dígitos errados
        self.assertFalse(validar_cpf("111.222.333-44"))  # Outro CPF inválido
        self.assertFalse(validar_cpf("999.999.999-99"))  # Outro CPF inválido

if __name__ == "__main__":
    unittest.main()
