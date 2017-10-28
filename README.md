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

### Instalando pip ###

Pip é o gerenciador de pacotes para python. As depêndencias de um projeto python
ficam localizadas no arquivo requirements.txt. Pip irá ler esse arquivo e
instalar as dependências.

Se você não tem ainda instalado os pacotes de desenvolvimento, instale-os agora:

    $ sudo apt-get install -y build-essential python-dev

Instalando dependências (selenium, lettuce, chromedriver) do projeto usando o pip:

    $ pip install -r requirements.txt

Executando os testes
--------------------

Para executar os testes:

    # Considerando que você está na raiz do projeto

    # Para executar todos os testes:
    $ lettuce

    # Para executar os testes de uma funcionalidade:
    $ lettuce features/twitter

    # Para executar os testes de uma única feature
    $ lettuce features/twitter/post.feature

    # Para executar alguns cenários de uma feature
    $ lettuce features/twitter/post.feature -s 1,3

Leia mais sobre Lettuce e BDD

* http://code.tutsplus.com/tutorials/behavior-driven-development-in-python--net-26547
* http://lettuce.it/tutorial/simple.html

Obs: Lettuce ainda não possui suporte a python3 :(

Alternativa ao lettuce: [behave](https://pythonhosted.org/behave/tutorial.html) (Suporte a python3)

