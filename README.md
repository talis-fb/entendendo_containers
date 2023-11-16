Para rodar o exemplo básico
```sh
$ cd basic_example

# Backend
$ docker build -t backend_api api_python/
$ docker run --rm -it -p 8080:8080 backend_api


# Frontend
$ docker build -t frontend_server frontend/
$ docker run --rm -it -p 3000:8080 frontend_server
```

Pode-se ao inves de rodar todos esse comando utilizar apenas o docker compose
```sh
$ cd basic_example
$ docker compose up -d
```

---
Para rodar o exemplo usando um proxy...
```sh
$ cd advanced_example
$ docker compose up -d
```
