import emoji

# Lista de emojis disponíveis com seus códigos correspondentes
emojis_disponiveis = {
    ":red_heart:": "❤️",
    ":thumbs_up:": "👍",
    ":thinking_face:": "🤔",
    ":partying_face:": "🥳"
}

# Apresentando os emojis disponíveis para o usuário
print("Emojis disponíveis:")
for emoji_codigo, emoji_visual in emojis_disponiveis.items():
    print(f"{emoji_visual} - {emoji_codigo}")

# Solicitando uma frase codificada ao usuário
frase_codificada = input("\nDigite uma frase e ela será emojizada: ")

# Decodificando e emojizando a frase
frase_emojizada = emoji.emojize(frase_codificada, use_aliases=True)

# Apresentando a frase emojizada
print("Frase emojizada:")
print(frase_emojizada)
