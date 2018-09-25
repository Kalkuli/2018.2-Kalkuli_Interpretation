# Serviço de Interpretação de Dados de Notas Fiscais  

<div style="text-align: center"> 

<a href="https://travis-ci.com/Kalkuli/2018.2-Kalkuli_Interpretation"><img src="https://travis-ci.com/Kalkuli/2018.2-Kalkuli_Interpretation.svg?branch=master" /></a>
<a href="https://codeclimate.com/github/Kalkuli/2018.2-Kalkuli_Interpretation/test_coverage"><img src="https://api.codeclimate.com/v1/badges/68cde8f95e18a9bd9d8e/test_coverage" /></a>
<a href="https://codeclimate.com/github/Kalkuli/2018.2-Kalkuli_Interpretation/maintainability"><img src="https://api.codeclimate.com/v1/badges/68cde8f95e18a9bd9d8e/maintainability" /></a>
<a href="https://opensource.org/licenses/GPL-3.0"><img src="https://img.shields.io/badge/license-GPL-%235DA8C1.svg"/></a>

 </div> 



# Configurando o ambiente
Para instruções de como instalar o _Docker_ e o _Docker-compose_ clique [aqui](https://github.com/Kalkuli/2018.2-Kalkuli_Front-End/blob/master/README.md).


## Colocando no ar
Com o _Docker_ e _Docker-Compose_ instalados, basta apenas utilizar os comandos:

```
docker-compose -f docker-compose-dev.yml build
```

e

```
docker-compose -f docker-compose-dev.yml up
```

Acesse o servidor local no endereço apresentado abaixo:

[localhost:5002](http://localhost:5002/)


Agora você já pode começar a contribuir!


## Testando    

Execute o comando abaixo para executar os testes:

```
docker-compose -f docker-compose-dev.yml run base python manage.py test
```   

Execute o comando abaixo para checar a cobertura:   

```
 docker-compose -f docker-compose-dev.yml run base python manage.py cov   
 ```