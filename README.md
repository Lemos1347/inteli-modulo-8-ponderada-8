# Atividade ponderada 7 Inteli Módulo 8

Este repositório contém os códigos para a seguinte atividade:

> [!NOTE]
> Criar uma aplicação que integra um tradutor de texto (pode ser baseado em LLM ou não), uma aplicação de speech-to-text e uma aplicação de text-to-speech.

## Vídeo demonstrativo

https://github.com/Lemos1347/inteli-modulo-8-ponderada-8/assets/99190347/1b2e952f-3e38-481b-a811-06e7b5606b24

## Sobre os arquivos

Nesse repositório você encontrará um arquivo python que é uma aplicação de terminal que integra funcionalidades de speech-to-text, tradução de texto, e text-to-speech. O objetivo é receber um arquivo de áudio, transformá-lo em texto, traduzir o texto para um idioma escolhido e, por fim, gerar um novo arquivo de áudio com a tradução. Além disso, há um arquivo de audio para teste (caso queira testar o programa com outros audios é necessário fazer o upload do arquivo, obrigatoriamente em formato .mp3, para o diretório do projeto) e dois outros arquivos com um audio traduzido do audio de teste original.

## Como executar

> [!IMPORTANT]
> Para executar os códigos é necessário ter o Python 3.6 ou superior instalado em sua máquina.

Para instalar e executar este projeto, siga estas etapas:

1. Clone o repositório:

   ```
   git clone https://github.com/Lemos1347/inteli-modulo-8-ponderada-8.git
   ```

2. Navegue até o diretório do projeto:

   ```
   cd inteli-modulo-8-ponderada-8
   ```

3. Instale as dependências:

   ```
   pip install -r requirements.txt
   ```

Por fim, execute o seguinte comando no terminal:

```
python3 main.py
```

Você será guiado por um menu interativo para escolher um arquivo de áudio e o idioma de destino para a tradução.
