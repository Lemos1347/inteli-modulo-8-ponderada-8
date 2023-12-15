import whisper
from googletrans import Translator
from gtts import gTTS
import os
import inquirer

LANGUAGES_OPTIONS = [
    ("Francês", "fr"),
    ("Espanhol", "es"),
    ("Inglês", "en"),
    ("Italiano", "it"),
    ("Japonês", "ja"),
]


def listar_arquivos_mp3(diretorio):
    # Lista todos os arquivos .mp3 no diretório especificado
    return [arquivo for arquivo in os.listdir(diretorio) if arquivo.endswith('.mp3')]


def choose_files(files):
    # Cria uma pergunta com as opções dos arquivos .mp3
    perguntas = [inquirer.List(
        'file', message="Escolha um arquivo de audio disponível", choices=files)]
    resposta = inquirer.prompt(perguntas)
    return resposta['file']


def choose_language(choices):
    perguntas = [inquirer.List(
        'language', message="Escolha um idioma para qual o audio sera traduzido", choices=choices)]
    resposta = inquirer.prompt(perguntas)
    return resposta['language']


class Tradutor:
    def __init__(self, audio_path, language) -> None:
        self.translated_count = 0
        self._whisper = whisper.load_model("base")
        self.language = language
        self.audio = audio_path
        self.supported_languages = [
            "fr",
            "es",
            "en",
            "it",
            "ja",
        ]

    def change_audio(self, audio_path):
        self.audio = audio_path

    def change_language(self, language):
        if language in self.supported_languages:
            self.language = language

    def translate(self):
        print("\nTransformando audio para texto...")
        self._generate_text_from_audio()
        print("Traduzindo texto...")
        self._translate_text()
        print("Gerando audio...")
        audio_path = self._generate_audio()

        print(f"Audio gerado com sucesso! ✅ \n")
        print(f"O audio traduzido está em: {audio_path} 📺 \n")

        self.ask_keep_translating()

        if (self.keep_translating):
            self.audio = choose_files(listar_arquivos_mp3(
                os.path.dirname(os.path.abspath(__file__))))
            self.language = choose_language(LANGUAGES_OPTIONS)
            self.translate()

    def _generate_text_from_audio(self):
        print("Carregando modelo do whisper...")
        model = whisper.load_model("medium")
        self.text_to_translate = model.transcribe(self.audio)["text"]
        print("Audio transformado em texto com sucesso! ✅ \n")

    def _translate_text(self):
        trans = Translator()
        result = trans.translate(self.text_to_translate, dest=self.language)
        self._translated_text = result.text
        print("Texto traduzido com sucesso! ✅ \n")

    def _generate_audio(self):
        self.translated_audio = gTTS(
            text=self._translated_text, lang=self.language)
        audio_path = f"translated_audio_{self.translated_count}.mp3"
        self.translated_audio.save(audio_path)
        self.translated_count += 1

        return audio_path

    def ask_keep_translating(self):
        perguntas = [inquirer.List(
            'keep', message="Deseja traduzir outro audio?", choices=[("Sim", True), ("Não", False)])]
        resposta = inquirer.prompt(perguntas)
        self.keep_translating = resposta['keep']


def main():
    print("Seja bem vindo ao tradutor!")
    print("Primeiro de tudo precisamos definir algumas coisas: \n")

    audio_path = choose_files(listar_arquivos_mp3(
        os.path.dirname(os.path.abspath(__file__))))
    language = choose_language(LANGUAGES_OPTIONS)

    tradutor = Tradutor(audio_path, language)

    tradutor.translate()

    print("Obrigado por usar nosso tradutor! 😄")


if __name__ == "__main__":
    main()
