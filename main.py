def calcular_imposto(valor_compra):
  taxa_imposto = 0.17 if valor_compra < 50 else 0.92
  valor_imposto = valor_compra * taxa_imposto
  return valor_imposto


def converter_real_para_dolar(valor_em_real, taxa_de_conversao):
  valor_em_dolar = valor_em_real / taxa_de_conversao
  return valor_em_dolar


def converter_dolar_para_real(valor_em_dolar, taxa_de_conversao):
  valor_em_real = valor_em_dolar * taxa_de_conversao
  return valor_em_real


def calcular_total(valor_produto, valor_imposto):
  return valor_produto + valor_imposto


def main():
  cotacao_dolar = float(
      input("Digite a cotação do dólar do dia: ").replace(",", "."))
  valor_em_real = float(
      input("Digite o valor da compra em Real Brasileiro: ").replace(",", "."))

  valor_em_dolar = converter_real_para_dolar(valor_em_real, cotacao_dolar)
  valor_imposto_dolar = calcular_imposto(valor_em_dolar)
  valor_imposto_real = converter_dolar_para_real(valor_imposto_dolar,
                                                 cotacao_dolar)

  valor_total_dolar = calcular_total(valor_em_dolar, valor_imposto_dolar)
  valor_total_real = calcular_total(valor_em_real, valor_imposto_real)

  print(f"O valor da compra em dólares é: {valor_em_dolar:.2f} USD")
  print(f"O valor do imposto em dólares é: {valor_imposto_dolar:.2f} USD")
  print(
      f"O valor do imposto em Real Brasileiro é: {valor_imposto_real:.2f} BRL")
  print(f"O valor total em dólares a ser pago é: {valor_total_dolar:.2f} USD")
  print(
      f"O valor total em Real Brasileiro a ser pago é: {valor_total_real:.2f} BRL"
  )


if __name__ == "__main__":
  main()
