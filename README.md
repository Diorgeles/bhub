# BHub

## Frameworks e Bibliotecas
- [Django](https://www.djangoproject.com)
- [Docker](https://www.docker.com)
- [PostgreSQL](https://www.postgresql.org)

## Possivel Infra-estrutura
- App engine (GCP)
    - Com ele poderemos ter um frontend rodando em container gerenciado pelo google com muitos recursos como por exemplo teste A/B
- Google Cloud Run
    - Colocamos a imagen do backend
    - Aqui tambem podemos colocar o celery pra rodar a aplicação em workers
    - Subimos uma imagem do rabbitmq que vai estar ligado ao celery do django
- Google Cloud SQL Ou Neon - https://neon.tech
    -  Provisionar uma versão de postgres

## Architetura base
- Alguns modulos podem funcionar de forma assincrona e com isso é necessario balacear quais funções poderiam ser executadas em filas de processamentos
    - Funções que poderiam ser em filas
        - Processamento de pagamentos
        - Notificações, como emails e sms
        - Geração de relatórios

## Observações
- Só existe 2 modulos com tabelas criadas, Order e Payment, a ideia é mostrar como eu pensei na solução do problema
    - Na minha ideia, cada "pos pagamento" gera uma chamada para uma função subsequente responsavel por executar algo.
    - Cada tipo de pedido tem sua regra em uma class, exemplo:
        - Se o pagamento for um *livro* preciso criar uma *guia de remessa* e gerar um *pagamento de comissão*,
        então foi feito uma class separada que só vai lidar com isso, e toda a regra de negocio pode ir nesta class
- A melhor forma de ver as coisas funcionando é executando os testes unitários, deixei prints pra facilitar o entendimento da ideia
- Pastas que no mundo real seriam modulos porem foram abstraido nesta solução
    - associates
    - notifications
    - products
    - shipments

## Desenvolvimento
- O projeto foi desenvolvido sobre o framework Django e roda em um container Docker

- Ao baixar o projeto siga as instruções abaixo

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements/base.txt
```

### Para executar o sistema basta rodar o comando abaixo

```bash
make run
```
- O django vai ser executado e será acessar atraves de `http://localhost:8000/admin/`
- Login: admin
- Senha: admin

### Para executar os testes unitários siga as instruções abaixo

```bash
make run-db
make only
```
