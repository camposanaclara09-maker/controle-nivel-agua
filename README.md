Controle de Níveis de Água
Descrição
Este projeto simula o monitoramento dos níveis de água de um reservatório utilizando Python e a biblioteca Colorama. As mensagens são exibidas no terminal com cores diferentes conforme o nível informado.
Objetivo
Representar cinco níveis de água, do muito baixo ao muito alto, usando mensagens coloridas para facilitar a identificação de cada situação.
Tecnologias utilizadas
- Python
- Biblioteca Colorama
- Visual Studio Code
Funcionalidades
- Armazena os cinco níveis e suas situações em uma lista.
- Utiliza a função definir_cor() para escolher a cor de cada nível.
- Exibe as mensagens no terminal.
- Restaura o estilo padrão com Style.RESET_ALL após cada mensagem.
Níveis do reservatório
Nível	Situação	Cor
1	Muito baixo (crítico)	Vermelho
2	Baixo	Amarelo
3	Médio	Verde
4	Alto	Ciano
5	Muito alto (alerta)	Azul


Como instalar a biblioteca
No terminal, execute:
python -m pip install colorama
Como executar o programa
Na pasta do projeto, execute:
python app.py
Se o comando python não funcionar, tente:
py app.py
Observação
Este projeto é uma simulação com níveis definidos no código. Ele não mede o nível de um reservatório real.
Conclusão
A atividade demonstra o uso de listas, funções, estruturas condicionais, repetição e biblioteca externa em Python para apresentar mensagens coloridas no terminal.