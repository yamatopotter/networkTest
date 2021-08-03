# **NetworkStatus**

Olá, o **network status** é um conjunto de arquivos em Python3 que realiza testes periódicos na sua rede (Cabeada e WiFi) através de um Raspberry Pi e envia o relatório. É uma maneira de realizar o monitoramento de clientes específicos e até mesmo de sua casa.

Funciona em sistemas baseado em linux, em específico RaspberryOs com Raspberry Pi (+versão3)

Após a instalação do sistema base (não é preciso instalar o RaspberryOs com interface gráfica) é necessário atualizar o sistema e repositorios para o mais recente

Requisitos de softwares:

  - apache
- php
 - mysql
 - phpmyadmin
 - speedtest (https://www.speedtest.net/pt/apps/cli)
 - python3-pip
 - pip3 install mysql-connector-python

Após a instalaćão e configuraćão dos requisitos mínimos, copie a pasta com os arquivos para a home ou seu local de preferência.

Cire uma base chamada ***network_data*** e importe as configuraćões da base de dados para o mysql através do phpmyadmin (ou manualmente se preferir).

## Descrićão dos arquivos

Todos os arquivos iniciados por **f_** são funćões, utilizados por outras partes de códigos.

- *checkLanStability.py*: Verifica a conexão dos disposivos físicos e insere dados no banco de dados caso haja alguma desconexão física em alguma das interfaces.
- *f_checkDevice.py*: É responsável por retornar se o dispositivo está conectado fisicamente ou não.
- *f_configureNetwork.py*: É responsável por desabilitar ou habilitar as interfaces. Necessária configuraćão da senha do **sudo**.
- *f_dbManager.py*: Responsável pelos comandos de inserćão de dados na base de dados.
- *getExternalIp.py*: Arquivo para capturar o IP externo.
- *internetSpeed.py*: Realiza o teste de velocidade (download e upload) com speedtest insere as informaćões no banco de dados.
  - Nos testes são capturadas as seguintes informaćões: 
    - Servidor de destino (nome do provedor)
    - Servidor de origem (nome do provedor)
    - download
    - upload
    - jitter
    - delay
    - Data de realizaćão dos testes
- *mainSystem.py*: É o arquivo principal, deve ser utilizado de tempos em tempos para a geraćão do relatório e envio do mesmo por e-mail. (A ser removida)
- *pingNetwork.py*: Realiza testes de Ping, insere as informaćões no banco de dados e retorna o resultado.
- *sendStatistic.py*: Realiza os envios de emails com os resultados do teste.
- *traceroute.py*: Realiza os testes de rota inserindo os dados no banco de dados.



## Como fazer o sistema rodar

Para rodar ele, edit o crontab (`sudo crontab -e`) e não esqueća de dar o comando de sudo antes de cada script Python para ter certeza de que todos os scripts rodarão com sucesso.

*pingNetwork.py*: `* * * * * sudo python3 /home/<seu diretorio>/<network status>/pingNetwork.py`

*traceroute.py*: `*/3 * * * * sudo python3 /home/<seu diretorio>/<network status>/traceroute.py`

*internetSpeed.py*:  `0 */1 * * * sudo python3 /home/<seu diretorio>/<network status>/internetSpeed.py`

*sendStatistic.py*:  `5 */1 * * * sudo python3 /home/<seu diretorio>/<network status>/internetSpeed.py`



A configuraćão do cron é flexível. Eu usei dessa forma porque realizar teste de velocidade de minuto a minuto inviabliza o uso da própria rede ou o resultado da mesma. Mas caso queira com mais frequência, basta ajustar o cron para o desejado.



