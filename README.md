# Instruções

Após clonar o projeto, é necessário acertar o arquivo de configuração. Crie uma
cópia do arquivo ```config.py.dist``` e altere como precisar.

    $ cp features/src/config.py{.dist,}

É possível rodar os testes tanto localmente quanto dentro de um container do
docker. As instruções para executar localmente ou via docker encontram-se abaixo.

Dependências do projeto
-----------------------

### Instalando virtualenv ###

O virtualenv permite ter um ambiente python isolado para o projeto:

    $ sudo apt-get install -y virtualenv
    # Crie um ambiente do virtualenv
    $ virtualenv -p python2 venv
    # Ative o ambiente
    $ . ./venv/bin/activate
    # Você deve ver (venv) no início do seu prompt.

### Instalando o chromedriver ###

O chormedriver permite enviar comandos do python para o google chrome.

Baixe o [chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) e coloque-o no PATH:

    # Exemplo de código para colocar o chormedriver dentro do PATH do seu ambiente virtual
    $ wget http://chromedriver.storage.googleapis.com/2.23/chromedriver_linux64.zip -O temp.zip \
    && unzip temp.zip \
    && rm -f temp.zip \
    && mv chromedriver venv/bin/

### Instalando geckodriver (opicional)

Novas versões do Firefox requerem o geckodriver + selenium3.* para funcionar corretamente.

    $ wget https://github.com/mozilla/geckodriver/releases/download/v0.10.0/geckodriver-v0.10.0-linux64.tar.gz
    tar xzvf geckodriver-v0.10.0-linux64.tar.gz
    cp geckodriver /usr/bin/
    pip install selenium==3.0.0b3

### Instalando o phantomjs (opcional)

Phantomjs é um navegador baseado em webkit (mesma engine que o chrome). O diferêncial é
a ausência de um ambiente gráfico, facilitando testes automatizados.

    1. Instale o [nodejs](https://nodejs.org/en/download/) (usando [gerenciador de pacotes](https://nodejs.org/en/download/package-manager/#debian-and-ubuntu-based-linux-distributions))
    2. Instale phantomjs usando ```npm```

    $ npm -g install phantomjs-prebuilt #If you are not using virtualenv
    $ npm install phantomjs-prebuilt #If you are using virtualenv

### Instalando pip ###

Pip é o gerenciador de pacotes para python. As depêndencias de um projeto python
ficam localizadas no arquivo requirements.txt. Pip irá ler esse arquivo e
instalar as dependências.

Se você não tem ainda instalado os pacotes de desenvolvimento, instale-os agora:

    $ sudo apt-get install -y build-essential python-dev

Instalando dependências do projeto usando o pip:

    $ pip install -r requirements.txt

Executando os testes
--------------------

Para executar os testes:

    # Considerando que você está na raiz do projeto

    # Para executar todos os testes:
    $ lettuce

    # Para executar os testes de uma funcionalidade:
    $ lettuce features/login/

    # Para executar os testes de uma única feature
    $ lettuce features/login/login-simple.feature

    # Para executar alguns cenários de uma feature
    $ lettuce features/login/login-simple.feature -s 1,3

Leia mais sobre Lettuce e BDD

* http://code.tutsplus.com/tutorials/behavior-driven-development-in-python--net-26547
* http://lettuce.it/tutorial/simple.html

Alternativa ao lettuce: [behave](https://pythonhosted.org/behave/tutorial.html)