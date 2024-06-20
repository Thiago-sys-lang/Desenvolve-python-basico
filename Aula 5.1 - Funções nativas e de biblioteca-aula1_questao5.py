import emoji

# Lista de emojis disponíveis com os textos correspondentes
emojis_disponiveis = {
    ":red_heart:": "❤️",
    ":thumbs_up:": "👍",
    ":thinking_face:": "🤔",
    ":partying_face:": "🥳"
}

# Apresentar a lista de emojis disponíveis para o usuário
print("Emojis disponíveis:")
for texto, emoji_unicode in emojis_disponiveis.items():
    print(f"{emoji_unicode} - {texto}")

# Solicitar uma frase codificada ao usuário
frase_codificada = input("\nDigite uma frase e ela será emojizada: ")

# Decodificar a frase e apresentá-la emojizada
frase_emojizada = emoji.emojize(frase_codificada, use_aliases=True)
print("Frase emojizada:")
print(frase_emojizada)
