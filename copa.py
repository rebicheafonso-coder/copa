print("=== QUIZ DA COPA DO MUNDO ===\n")

score = 0

# Pergunta 1
print("1) Quantos times participam da Copa do Mundo 2026?")
print("a) 32")
print("b) 48")
print("c) 64")
answer = input("Resposta: ").lower()

if answer == "b":
    print("Correto!\n")
    score += 1
else:
    print("Errado! A resposta certa é b)\n")

# Pergunta 2
print("2) Em que ano será a Copa do Mundo 2026?")
print("a) 2024")
print("b) 2026")
print("c) 2028")
answer = input("Resposta: ").lower()

if answer == "b":
    print("Correto!\n")
    score += 1
else:
    print("Errado! A resposta certa é b)\n")

# Pergunta 3
print("3) Qual país NÃO é sede da Copa 2026?")
print("a) Canadá")
print("b) México")
print("c) Brasil")
answer = input("Resposta: ").lower()

if answer == "c":
    print("Correto!\n")
    score += 1
else:
    print("Errado! A resposta certa é c)\n")

# Resultado final
print("=== RESULTADO FINAL ===")
print(f"Você acertou {score} de 3 perguntas")

if score == 3:
    print("🏆 Excelente! Você é fã de futebol!")
elif score == 2:
    print("👍 Bom trabalho!")
else:
    print("📚 Tente novamente e estude mais!")