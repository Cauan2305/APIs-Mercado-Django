# APIs-Mercado-Django
*APIs Django Rest para Super Mercados com cadastro de produtos e banco de dados*
*Projeto Simples mais visando ao conhecimento ao django rest fiz um cadastro de produtos de mercados onde voçê Escolhe categoria foto, preço*


## Como rodar Projeto
*Vamos Instalar as depedencias do nosso Projeto*
```
$ pip install -r requirements.txt
```

*Vamos Fazer migrações do nosso banco de dados*
```
python manage.py makemigrations
```

*E depois run*
```
python manage.py migrate
```

### Vamos Rodar a aplicação 
```
python manage.py runserver
```

*Vamos na url admin para poder acessar a api*
```
http://127.0.0.1:8000/admin
```
*Use esse login*
```
Usuario:teste
Senha:cauan123
```

*Agora vá para url*
```
http://127.0.0.1:8000/
```
*Já vai Aparecer a url da api *
*Fiquei a vontade para adcionar dados*