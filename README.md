# instabot
Instagram bot que informa:
- Quem não te segue de volta
- Quem você não segue de volta

## Pré-requisitos
É necessário ter o [Firefox Selenium Geckodriver](https://github.com/mozilla/geckodriver/releases) instalado

## Rodar o projeto

#### 1. Clone o repositório
`git clone https://github.com/xavierigor/progame.git`

#### 2. Crie a virtual env
> `cd instabot`
>
> `pipenv shell`

#### 3. Instale as bibliotecas
> `pipenv install`

#### 4. Crie o arquivo secrets.py na raíz do projeto
> `touch secrets.py`

#### 5. Coloque suas credenciais do instagram no arquivo secrets.py para que o bot logue
> `username = "example_username"`
>
> `password = "example_password"`

#### 6. Rode o projeto
> `python instabot.py`
