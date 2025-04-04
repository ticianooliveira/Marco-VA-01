import unittest
from app.validacao import validar_cpf

class TestValidarCPF(unittest.TestCase):

    def test_cpf_valido(self):
        self.assertTrue(validar_cpf("529.982.247-25"))
        self.assertTrue(validar_cpf("168.995.350-09"))
        self.assertFalse(validar_cpf("000.000.000-00"))
        self.assertFalse(validar_cpf("111.111.111-11"))

    def test_cpf_invalido_formato(self):
        self.assertFalse(validar_cpf("1234567890"))
        self.assertFalse(validar_cpf("123.456.789-0"))
        self.assertFalse(validar_cpf("abc.def.ghi-jk"))
        self.assertFalse(validar_cpf("1111.22222-12"))

    def test_cpf_invalido_digito(self):
        self.assertFalse(validar_cpf("123.456.789-00"))
        self.assertFalse(validar_cpf("111.222.333-44"))
        self.assertFalse(validar_cpf("999.999.999-99"))

if __name__ == "__main__":
    unittest.main()
