# Reencontra — Sistema de Achados e Perdidos

Aplicação acadêmica com Flask e Redis para registrar objetos perdidos/encontrados, pesquisar ocorrências, sugerir possíveis correspondências, atualizar registros, registrar devoluções e exportar dados.

## Modelo de dados Redis

O projeto usa estruturas nativas do Redis, não um banco de documentos:

- `ocorrencia:<id>` — **Hash** com os campos de uma ocorrência.
- `ocorrencias:ids` — **Set** com IDs cadastrados.
- `ocorrencias:proximo_id` — **String** usada como contador atômico.
- `ocorrencias:por_data` — **Sorted Set** para ordenar registros por data de criação.

## Requisitos

- Python 3.10 ou superior
- Redis em execução na porta 6379
- Windows, Linux ou macOS

## Instalação (Windows PowerShell)

Na pasta do projeto:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Confirme que o Redis está rodando. Se vocês já criaram o contêiner `redis-achados`:

```powershell
docker start redis-achados
docker exec -it redis-achados redis-cli PING
```

A resposta esperada é `PONG`.

## Executar

```powershell
python app.py
```

Abra `http://127.0.0.1:5000`.

## Funcionalidades

1. Criar ocorrência de objeto perdido ou encontrado.
2. Consultar e filtrar por texto, tipo e status.
3. Visualizar detalhes e código de ocorrência.
4. Editar campos.
5. Registrar devolução de um achado.
6. Encerrar ou excluir ocorrência.
7. Sugerir possíveis correspondências com pontuação explicável.
8. Exibir estatísticas e exportar os registros em JSON.

## Observações importantes

- O protótipo não possui autenticação, autorização nem proteção CSRF. Use apenas localmente e com dados fictícios para a apresentação.
- As sugestões de correspondência são heurísticas, não prova de propriedade.
- O botão de exportação JSON é uma exportação lógica dos registros da aplicação, não substitui um backup nativo do Redis.
- O primeiro protótipo pode ter criado `objeto:1` em vez de `ocorrencia:1`. O registro antigo continuará no Redis, mas não é convertido automaticamente para o novo modelo. Ele pode ser mantido como demonstração ou apagado manualmente depois de confirmar que não é necessário.
- Não apague o contêiner ou o volume do Redis sem antes salvar os dados.

## Backup nativo para demonstração

O Redis precisa estar configurado com persistência para que os dados sobrevivam a reinícios conforme a configuração. Consulte a documentação oficial: https://redis.io/docs/latest/operate/oss_and_stack/management/persistence/

Para pedir um snapshot RDB dentro do contêiner:

```powershell
docker exec redis-achados redis-cli BGSAVE
```

Verifique o arquivo de snapshot:

```powershell
docker exec redis-achados redis-cli CONFIG GET dir
docker exec redis-achados redis-cli CONFIG GET dbfilename
```

Em uma configuração comum da imagem oficial, o diretório é `/data` e o arquivo é `dump.rdb`. Confirme os valores antes de copiar:

```powershell
docker cp redis-achados:/data/dump.rdb .\dump.rdb
```

Se o caminho for diferente, use o diretório retornado pelo comando `CONFIG GET dir`. Não execute o backup ao mesmo tempo que outras operações administrativas sem verificar o estado do Redis.

## Redundância

Para a apresentação, expliquem que o Redis suporta replicação primário-réplica e outras opções de alta disponibilidade, mas a aplicação local deste projeto não configura redundância automaticamente. Backup e replicação resolvem problemas diferentes.

## Ideias para evolução

- Autenticação de responsáveis.
- Histórico/auditoria de alterações.
- Testes automatizados.
- Docker Compose com volume persistente.
- Paginação para muitos registros.
