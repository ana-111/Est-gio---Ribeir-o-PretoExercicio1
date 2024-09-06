def pertence_fibonacci(numero):
  # Inicializa os dois primeiros números da sequência de Fibonacci
  a, b = 0, 1
  # Continua gerando a sequência enquanto o valor de 'a' for menor ou igual ao número informado
  while a <= numero:
      # Se o número informado for igual a algum valor da sequência, ele pertence
      if a == numero:
          return f"O número {numero} pertence à sequência de Fibonacci."
      # Atualiza os valores de 'a' e 'b' (a sequência de Fibonacci)
      a, b = b, a + b
  # Se sair do loop, o número não pertence
  return f"O número {numero} NÃO pertence à sequência de Fibonacci."

# Exemplo: Número definido no código
numero_informado = 21

# Alternativamente, você pode solicitar a entrada do usuário descomentando a linha abaixo
# numero_informado = int(input("Informe um número: "))

# Chama a função e imprime o resultado
print(pertence_fibonacci(numero_informado))
