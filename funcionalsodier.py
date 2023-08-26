def read_audio(file_path):
    with open(file_path, "rb") as file:
        data = file.read()
    return data

def calculate_similarity(audio_data1, audio_data2):
    # Certifique-se de que os áudios têm o mesmo comprimento
    min_length = min(len(audio_data1), len(audio_data2))
    audio_data1 = audio_data1[:min_length]
    audio_data2 = audio_data2[:min_length]

    # Calcula a diferença entre os áudios
    difference = sum(abs(a - b) for a, b in zip(audio_data1, audio_data2))

    # Define um limite de diferença
    similarity_threshold = 1000

    if difference < similarity_threshold:
        return "Os áudios são considerados similares, podem ser do mesmo pássaro."
    else:
        return "Os áudios são diferentes, não são do mesmo pássaro."

# Caminhos dos arquivos de áudio
audio_path1 = "c:\\Users\\userl\\Downloads\\aud1.mpeg"
audio_path2 = "c:\\Users\\user1\\Downloads\\aud2.mpeg"

# Lê os dados dos arquivos de áudio
audio_data1 = read_audio(audio_path1)
audio_data2 = read_audio(audio_path2)

# Calcula e imprime a similaridade
result = calculate_similarity(audio_data1, audio_data2)
print(result)
