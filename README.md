# Como rodar?

# Inicie o docker
docker build -t exchange-api .
docker run -d -p 8000:8000 --name exchange-api exchange-api

# Faça a chamada para api
curl -H "Authorization: Bearer seu_token_aqui" http://127.0.0.1:8000/exchange/USD/BRL

# Token de teste

token_secretoooo