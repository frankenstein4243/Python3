# Solicita o nome e a idade do usuário
nome = input("📝 Digite seu nome: ").strip()
idade = input("🎂 Digite sua idade: ").strip()

# Verifica se ambos foram preenchidos
if nome and idade:
    print(f"\n👤 Nome: {nome}")
    print(f"🔄 Nome invertido: {nome[::-1]}")
    print(f"🔍 Contém espaços? {'✅ Sim' if ' ' in nome else '❌ Não'}")
    print(f"🔡 Contém a letra 'n'? {'🟢 Sim' if 'n' in nome.lower() or 'N' in nome.upper() else '🔴 Não'}")
    print(f"📌 Primeira letra: {nome[0]}")
    print(f"📍 Última letra: {nome[-1]}")
else:
    print("\n⚠️ Dados inexistentes.")
