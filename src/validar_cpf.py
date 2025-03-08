import re


def validar_cpf(cpf):
    cpf = re.sub(r'\D', '', cpf)  # Remove caracteres não numéricos
    if len(cpf) != 11 or len(set(cpf)) == 1:
        return False
    # Cálculo dos dígitos verificadores
    def calcular_digito(cpf, peso):
        soma = sum(int(cpf[i]) * (peso - i) for i in range(peso - 1))
        resto = soma % 11
        return '0' if resto < 2 else str(11 - resto)
    return cpf[-2:] == calcular_digito(cpf, 10) + calcular_digito(cpf, 11)