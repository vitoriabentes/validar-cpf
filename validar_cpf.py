cpf = "" #Coloque um cpf qualquer sem pontuação para verifica-lo
nove_digitos = cpf[:9]
contador_regressivo = 10
resultado_primeiro_digito = 0
for digito in nove_digitos:
    resultado_primeiro_digito += (contador_regressivo * int(digito))
    contador_regressivo -= 1
primeiro_digito = (resultado_primeiro_digito * 10) % 11
primeiro_digito = primeiro_digito if primeiro_digito <=9 else 0

dez_digitos = nove_digitos + str(primeiro_digito)
contador_regressivo = 11
resultado_segundo_digito = 0
for digito in dez_digitos:
    resultado_segundo_digito += (contador_regressivo * int(digito))
    contador_regressivo -= 1
segundo_digito = (resultado_segundo_digito * 10) % 11
segundo_digito = segundo_digito if segundo_digito <= 9 else 0

cpf_gerado = f"{nove_digitos}{primeiro_digito}{segundo_digito}"
if cpf == cpf_gerado:
    print("CPF válido !")
else:
    print("CPF inválido !")