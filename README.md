# Reencontra — Sistema de Achados e Perdidos

**Aplicação web para gerenciamento de objetos perdidos e encontrados utilizando Redis como banco de dados NoSQL.**

---

## 1. Integrantes do projeto

**Integrantes:**
- Ana Laura Ferreira Cavalcante
- Guilherme Gomes Rebouças Lima
- Sthefany Maria de Morais Jerônimo

---

## 2. Sobre o projeto

O **Reencontra** é uma aplicação web desenvolvida para facilitar o registro, a consulta e o gerenciamento de objetos perdidos e encontrados.

A aplicação permite que os usuários cadastrem informações sobre objetos que perderam ou encontraram, consultem registros existentes, atualizem informações e acompanhem a situação de cada ocorrência.

A proposta é oferecer uma maneira simples e organizada de centralizar informações que, em situações comuns, acabam espalhadas por grupos de mensagens, avisos físicos ou conversas informais.

O sistema foi desenvolvido utilizando Python, Flask, HTML, CSS e Redis, com foco na aplicação prática de conceitos de bancos de dados NoSQL.

## 3. Problema que o projeto busca resolver

Perder um objeto ou encontrar algo que pertence a outra pessoa é uma situação comum em escolas, universidades, empresas, eventos e espaços públicos.

Sem um sistema centralizado, localizar o proprietário de um objeto pode ser difícil. As informações podem ficar desorganizadas, ser divulgadas em diferentes lugares ou deixar de ser encontradas por quem precisa delas.

O Reencontra busca reduzir esse problema por meio de um sistema que permite:

- Registrar objetos perdidos e encontrados.
- Armazenar informações importantes sobre cada ocorrência.
- Consultar e filtrar registros.
- Atualizar a situação dos objetos cadastrados.
- Identificar possíveis correspondências entre objetos perdidos e encontrados.
- Manter os registros organizados em um banco de dados.

## 4. Objetivos

### 4.1. Objetivo geral

Desenvolver uma aplicação web de achados e perdidos utilizando um banco de dados NoSQL do tipo chave-valor, demonstrando sua utilização em uma situação prática.

### 4.2. Objetivos específicos

- Aplicar o Redis no armazenamento e na recuperação de informações.
- Implementar operações CRUD (*Create, Read, Update e Delete*).
- Utilizar diferentes estruturas de dados nativas do Redis.
- Criar uma interface web simples e organizada.
- Implementar mecanismos de pesquisa e filtragem de ocorrências.
- Desenvolver uma funcionalidade de identificação de possíveis correspondências.
- Documentar a instalação, a execução e os recursos necessários para utilizar a aplicação.

---

## 5. Funcionalidades

O sistema disponibiliza as seguintes funcionalidades:

| Funcionalidade | Descrição |
|---|---|
| Cadastro de ocorrências | Permite registrar objetos perdidos ou encontrados. |
| Listagem de registros | Apresenta as ocorrências cadastradas. |
| Consulta de detalhes | Exibe as informações de uma ocorrência específica. |
| Edição | Permite atualizar os dados de um registro. |
| Exclusão | Permite remover uma ocorrência. |
| Pesquisa e filtros | Auxilia na localização de registros por texto, tipo ou situação. |
| Identificação de correspondências | Calcula uma pontuação de similaridade entre objetos perdidos e encontrados. |
| Atualização da situação | Permite registrar que um objeto foi devolvido ou encerrar uma ocorrência. |
| Estatísticas | Apresenta informações resumidas sobre os registros. |
| Exportação JSON | Permite exportar os registros para um arquivo no formato JSON. |

**Observação:** a identificação de correspondências utiliza critérios de comparação e similaridade implementados na aplicação. Não se trata de inteligência artificial generativa.

A exportação JSON é um recurso de exportação de dados e não substitui o backup nativo do Redis.

---

## 6. Tecnologias utilizadas

### 6.1. Python

Linguagem utilizada para implementar a lógica da aplicação, manipular os dados e integrar o sistema ao banco de dados.

**Versão recomendada:** Python 3.11.x.

Outras versões modernas do Python podem funcionar, desde que sejam compatíveis com as dependências utilizadas.

### 6.2. Flask

Framework web utilizado para criar as rotas, processar as requisições e integrar a lógica da aplicação às páginas HTML.

**Versão prevista nas dependências:** Flask 3.x.

### 6.3. Redis

Banco de dados NoSQL utilizado para armazenar e consultar as ocorrências.

O Redis trabalha com pares chave-valor e oferece estruturas de dados que permitem organizar informações de diferentes maneiras.

Neste projeto, são utilizadas as seguintes estruturas:

- **Hashes:** armazenam os campos de cada ocorrência.
- **Sets:** mantêm o conjunto de identificadores das ocorrências.
- **Strings:** armazenam o contador utilizado na geração de identificadores.
- **Sorted Sets:** organizam os identificadores de acordo com os valores de ordenação associados, permitindo recuperar registros por data.

Essas estruturas são utilizadas diretamente no Redis. O projeto não simula um banco de dados chave-valor usando um banco documental.

**Versão recomendada para execução local:** Redis 7, por meio de uma imagem Docker.

### 6.4. Docker

Utilizado para executar o Redis em um contêiner, evitando a necessidade de instalar e configurar manualmente o servidor Redis no sistema operacional.

O Docker também facilita a reprodução do ambiente em outros computadores.

### 6.5. HTML

Utilizado para estruturar as páginas da aplicação, incluindo formulários, listas, informações detalhadas e elementos de navegação.

### 6.6. CSS

Responsável pela apresentação visual da aplicação, incluindo cores, espaçamentos, organização dos componentes e adaptação do layout a diferentes tamanhos de tela.

### 6.7. Jinja

Mecanismo de templates integrado ao Flask, utilizado para inserir informações dinâmicas nas páginas HTML.

### 6.8. Biblioteca redis-py

Biblioteca Python utilizada para estabelecer a conexão com o Redis e executar operações de leitura e escrita.

### 6.9. Git

Pode ser utilizado para versionar o código-fonte e facilitar o trabalho colaborativo da equipe. Não é obrigatório para executar a aplicação.

---

## 7. Requisitos para executar a aplicação

Antes de iniciar, verifique se o computador possui os seguintes programas instalados.

| Requisito | Versão recomendada | Obrigatório? |
|---|---|---|
| Python | 3.11.x | Sim |
| Docker Desktop, no Windows/macOS, ou Docker Engine, no Linux | Versão estável atual | Sim, para o método de execução documentado |
| Git | Versão estável atual | Não |
| Navegador web atualizado | Versão atual | Sim |
| Editor de código | VS Code ou equivalente | Recomendado |

### 7.1. Verificar o Python

Abra um terminal e execute:

```bash
python --version
```

Em alguns sistemas, o comando pode ser:

```bash
python3 --version
```

O resultado esperado para a versão recomendada é semelhante a:

```text
Python 3.11.x
```

### 7.2. Verificar o Docker

Execute:

```bash
docker --version
```

Em seguida, confirme se o serviço está funcionando:

```bash
docker info
```

Se o comando `docker info` apresentar um erro de conexão com o servidor, inicie o Docker Desktop ou o serviço Docker do sistema operacional antes de continuar.

---

## 8. Como obter o projeto

Se o projeto foi disponibilizado em um arquivo ZIP, extraia seu conteúdo para uma pasta de sua preferência.

Se o código estiver em um repositório Git, clone o repositório:

```bash
git clone <URL_DO_REPOSITORIO>
```

Entre na pasta do projeto:

```bash
cd reencontra
```

**Importante:** o nome da pasta deve corresponder ao local em que os arquivos foram extraídos ou clonados.

A pasta principal deve conter o arquivo `app.py`, o arquivo `requirements.txt` e os demais diretórios da aplicação.

A estrutura esperada é:

```text
reencontra/
├── app.py
├── app_factory.py
├── config.py
├── extensions.py
├── requirements.txt
├── README.md
├── .gitignore
├── repositories/
│   ├── __init__.py
│   └── occurrence_repository.py
├── services/
│   ├── __init__.py
│   └── matching_service.py
├── routes/
│   ├── __init__.py
│   └── main.py
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── form.html
│   └── detail.html
└── static/
    └── style.css
```

Não renomeie nem remova os arquivos Python e os diretórios listados, pois eles fazem parte da estrutura utilizada pela aplicação.

---

## 9. Instalação e configuração

As instruções a seguir apresentam o procedimento para executar o sistema em um computador local.

### 9.1. Etapa 1 — Preparar o Redis com Docker

Primeiro, certifique-se de que o Docker está em execução.

Em seguida, crie e inicie um contêiner Redis com o comando:

```bash
docker run -d --name redis-achados -p 6379:6379 redis:7-alpine
```

Esse comando:

- Cria um contêiner chamado `redis-achados`.
- Utiliza uma imagem do Redis 7.
- Executa o contêiner em segundo plano.
- Disponibiliza a porta 6379 do contêiner na porta 6379 do computador.

A porta 6379 é a porta padrão utilizada pelo Redis.

**Atenção:** o comando acima deve ser executado apenas na primeira criação do contêiner. Se o contêiner `redis-achados` já existir, utilize o comando de inicialização apresentado a seguir.

Para iniciar um contêiner que já existe, execute:

```bash
docker start redis-achados
```

Para verificar se o contêiner está em execução:

```bash
docker ps
```

O contêiner `redis-achados` deverá aparecer na listagem.

### 9.2. Etapa 2 — Testar a conexão com o Redis

Execute:

```bash
docker exec -it redis-achados redis-cli PING
```

Se estiver tudo correto, o resultado será:

```text
PONG
```

Essa resposta indica que o servidor Redis está disponível e respondendo às solicitações.

Se o resultado for um erro, verifique se o Docker está funcionando e se o contêiner foi iniciado corretamente.

### 9.3. Etapa 3 — Criar um ambiente virtual Python

Dentro da pasta do projeto, crie um ambiente virtual:

```bash
python -m venv .venv
```

O ambiente virtual mantém as dependências da aplicação isoladas de outros projetos Python instalados no computador.

#### Windows — PowerShell

Ative o ambiente virtual:

```powershell
.\.venv\Scripts\Activate.ps1
```

Se o PowerShell bloquear a execução do script de ativação, consulte as políticas de execução do seu ambiente ou utilize outro terminal Python disponível, como o Prompt de Comando.

No Prompt de Comando do Windows, o comando é:

```bat
.venv\Scripts\activate.bat
```

#### Linux ou macOS

Execute:

```bash
source .venv/bin/activate
```

Depois da ativação, o terminal geralmente passa a exibir `(.venv)` no início da linha.

### 9.4. Etapa 4 — Instalar as dependências

Com o ambiente virtual ativado, atualize o instalador de pacotes:

```bash
python -m pip install --upgrade pip
```

Em seguida, instale as dependências declaradas no projeto:

```bash
python -m pip install -r requirements.txt
```

O arquivo `requirements.txt` deve conter as dependências necessárias para executar a aplicação:

```text
Flask>=3.0,<4.0
redis>=5.0,<7.0
```

Essas restrições permitem instalar versões compatíveis das bibliotecas Flask e redis-py dentro dos intervalos especificados.

Não é necessário instalar Flask e redis-py manualmente se o comando de instalação do arquivo `requirements.txt` for concluído com sucesso.

### 9.5. Etapa 5 — Conferir a configuração do Redis

A aplicação utiliza as seguintes configurações de conexão:

| Parâmetro | Valor padrão |
|---|---|
| Host | `localhost` |
| Porta | `6379` |
| Banco lógico Redis | `0` |

Esses valores devem corresponder à configuração local do Redis e às definições do arquivo `config.py`.

O arquivo `extensions.py` é responsável por disponibilizar o cliente Redis utilizado pela aplicação.

O arquivo `config.py` centraliza as configurações do sistema.

Se você alterou a porta publicada no Docker ou configurou o Redis em outro endereço, ajuste as configurações da aplicação para que correspondam ao servidor em execução.

---

## 10. Como executar a aplicação

Depois de concluir as etapas anteriores, verifique se:

- O ambiente virtual Python está ativado.
- As dependências foram instaladas.
- O contêiner Redis está em execução.
- O terminal está na pasta principal do projeto.

Execute:

```bash
python app.py
```

Se tudo estiver configurado corretamente, o Flask iniciará o servidor de desenvolvimento.

Abra um navegador e acesse:

**http://127.0.0.1:5000/**

A página inicial do Reencontra deverá ser exibida.

**Importante:** mantenha o terminal aberto enquanto estiver utilizando a aplicação. O servidor será encerrado quando o processo for interrompido.

Para parar o servidor, pressione:

```text
Ctrl + C
```

Para voltar a executar a aplicação posteriormente, basta iniciar o Docker, ativar o ambiente virtual e executar novamente `python app.py`.

---

## 11. Como utilizar o sistema

### 11.1. Página inicial

A página inicial apresenta as ocorrências cadastradas e informações resumidas sobre os registros.

Nela, é possível consultar os objetos registrados e utilizar os filtros disponíveis.

### 11.2. Cadastrar uma ocorrência

Acesse a opção de criação de uma nova ocorrência.

Preencha os campos disponíveis, que podem incluir:

- Tipo da ocorrência: objeto perdido ou encontrado.
- Nome do objeto.
- Descrição.
- Categoria.
- Local.
- Data da ocorrência.

Após preencher as informações, envie o formulário para cadastrar o registro.

### 11.3. Consultar ocorrências

Utilize a listagem e os filtros para localizar registros.

A aplicação permite pesquisar informações textuais e restringir os resultados de acordo com os critérios implementados, como tipo e situação da ocorrência.

### 11.4. Visualizar os detalhes

Abra uma ocorrência para consultar suas informações completas e os recursos disponíveis para aquele registro.

### 11.5. Editar ou excluir registros

Acesse os detalhes ou a opção correspondente para editar ou excluir uma ocorrência.

A exclusão remove o registro do sistema, portanto deve ser realizada com cuidado.

### 11.6. Registrar a devolução ou encerrar uma ocorrência

Quando um objeto for devolvido, utilize a funcionalidade correspondente para atualizar sua situação.

Também é possível encerrar uma ocorrência, de acordo com as opções disponíveis na interface.

### 11.7. Consultar possíveis correspondências

A aplicação compara informações de objetos perdidos e encontrados para calcular possíveis correspondências.

A comparação utiliza critérios implementados no projeto, como categoria e palavras em comum nos campos textuais.

Os resultados são sugestões e **não garantem que dois registros correspondam ao mesmo objeto**. As informações devem ser conferidas antes de considerar uma ocorrência resolvida.

### 11.8. Exportar os registros

Utilize a funcionalidade de exportação para obter os registros no formato JSON.

O arquivo exportado pode ser utilizado para consulta ou análise externa.

**A exportação JSON não substitui um backup completo do banco Redis.**

---

## 12. Como os dados são armazenados no Redis

O Redis é o banco de dados principal da aplicação. Os registros são armazenados utilizando estruturas nativas do banco.

### 12.1. Hashes

Cada ocorrência é armazenada em uma chave individual, seguindo um padrão semelhante a:

```text
ocorrencia:<id>
```

Por exemplo:

```text
ocorrencia:1
```

Essa chave representa a ocorrência de identificador `1`.

O Hash armazena os campos associados ao registro, como nome, descrição, categoria, local, data e situação, conforme definidos pela implementação.

### 12.2. Sets

O conjunto:

```text
ocorrencias:ids
```

armazena os identificadores das ocorrências cadastradas.

Essa estrutura facilita a manutenção e a recuperação do conjunto de registros.

### 12.3. Strings

A chave:

```text
ocorrencias:proximo_id
```

armazena o contador utilizado na geração de novos identificadores.

A operação `INCR` do Redis permite incrementar esse contador.

### 12.4. Sorted Sets

A estrutura:

```text
ocorrencias:por_data
```

organiza os identificadores de acordo com os valores de ordenação associados às ocorrências, utilizados para a recuperação ordenada por data.

### 12.5. Operações CRUD

A aplicação implementa as quatro operações fundamentais de manipulação de dados:

| Operação | Significado | Exemplo de uso |
|---|---|---|
| Create | Criar | Cadastrar uma ocorrência. |
| Read | Ler | Consultar os detalhes de um objeto. |
| Update | Atualizar | Editar os dados ou a situação de uma ocorrência. |
| Delete | Excluir | Remover uma ocorrência. |

O acesso aos dados é organizado principalmente no arquivo `repositories/occurrence_repository.py`.

---

## 13. Organização do código-fonte

O projeto foi organizado em arquivos e diretórios com responsabilidades específicas.

| Arquivo ou diretório | Responsabilidade |
|---|---|
| `app.py` | Ponto de entrada da aplicação. |
| `app_factory.py` | Cria e configura a aplicação Flask. |
| `config.py` | Centraliza as configurações. |
| `extensions.py` | Inicializa e disponibiliza o cliente Redis. |
| `repositories/` | Contém a camada de acesso aos dados. |
| `repositories/occurrence_repository.py` | Implementa operações de armazenamento, consulta, atualização e exclusão das ocorrências. |
| `services/` | Contém a lógica de serviços da aplicação. |
| `services/matching_service.py` | Calcula possíveis correspondências entre ocorrências. |
| `routes/` | Contém as rotas da aplicação web. |
| `routes/main.py` | Processa as requisições e conecta a interface às operações do sistema. |
| `templates/` | Contém os templates HTML renderizados pelo Flask. |
| `templates/base.html` | Define a estrutura compartilhada das páginas. |
| `templates/index.html` | Apresenta a página inicial e a listagem das ocorrências. |
| `templates/form.html` | Contém o formulário utilizado para cadastrar e editar ocorrências. |
| `templates/detail.html` | Apresenta os detalhes de uma ocorrência. |
| `static/style.css` | Define os estilos visuais da aplicação. |
| `requirements.txt` | Lista as dependências Python. |
| `README.md` | Documenta o projeto e as instruções de execução. |
| `.gitignore` | Define arquivos e diretórios que devem ser ignorados pelo Git. |

Essa organização separa as responsabilidades e facilita a manutenção, a compreensão e a evolução do projeto.

---

## 14. Comandos úteis para administrar o Redis

Os comandos a seguir são úteis durante o desenvolvimento, os testes e a apresentação acadêmica.

### Verificar o estado do contêiner

```bash
docker ps
```

### Iniciar o contêiner

```bash
docker start redis-achados
```

### Parar o contêiner

```bash
docker stop redis-achados
```

### Abrir o terminal do Redis

```bash
docker exec -it redis-achados redis-cli
```

### Testar a conexão

Dentro do terminal do Redis, execute:

```redis
PING
```

Resultado esperado:

```text
PONG
```

### Consultar uma ocorrência

```redis
HGETALL ocorrencia:1
```

O comando retorna os campos e valores armazenados no Hash correspondente, caso a chave exista.

### Consultar os identificadores cadastrados

```redis
SMEMBERS ocorrencias:ids
```

### Consultar o contador

```redis
GET ocorrencias:proximo_id
```

### Consultar a ordenação por data

```redis
ZREVRANGE ocorrencias:por_data 0 -1 WITHSCORES
```

Esses comandos permitem observar diretamente as estruturas de dados utilizadas pela aplicação.

---

## 15. Persistência e backup

O Redis pode manter dados em memória e oferecer persistência em disco, dependendo de sua configuração.

Entre os mecanismos de persistência disponíveis estão:

- **RDB:** produz snapshots dos dados em determinados momentos.
- **AOF (*Append Only File*):** registra operações de escrita para permitir a reconstrução dos dados.

A configuração efetiva de persistência depende do servidor Redis e da imagem utilizada.

No comando Docker apresentado neste README, não foram definidos volumes persistentes nem configurações personalizadas de backup. Portanto, não se deve presumir que os dados estarão protegidos contra a remoção do contêiner ou a perda de seus arquivos.

### 15.1. Consultar a configuração de persistência

Abra o terminal do Redis:

```bash
docker exec -it redis-achados redis-cli
```

Para consultar o diretório de dados configurado:

```redis
CONFIG GET dir
```

Para consultar o nome do arquivo RDB:

```redis
CONFIG GET dbfilename
```

Também é possível consultar o estado da persistência AOF:

```redis
CONFIG GET appendonly
```

Esses comandos ajudam a identificar a configuração efetiva do servidor.

### 15.2. Gerar um snapshot RDB

Para solicitar a geração de um snapshot em segundo plano:

```bash
docker exec redis-achados redis-cli BGSAVE
```

A operação solicita que o Redis gere um arquivo RDB conforme sua configuração atual.

Depois, verifique o resultado:

```bash
docker exec redis-achados redis-cli INFO persistence
```

Consulte os valores de `CONFIG GET dir` e `CONFIG GET dbfilename` para identificar o caminho e o nome do arquivo gerado.

Se o arquivo estiver em `/data/dump.rdb`, por exemplo, ele poderá ser copiado para o diretório atual com:

```bash
docker cp redis-achados:/data/dump.rdb ./dump.rdb
```

Esse caminho é apenas um exemplo. Caso a configuração retorne outro diretório ou nome de arquivo, adapte o comando.

**Atenção:** gerar um arquivo RDB não configura automaticamente uma política de backup recorrente. Para um ambiente real, é necessário definir onde os backups serão armazenados, com que frequência serão realizados e como serão restaurados e verificados.

### 15.3. Redundância

O Redis oferece mecanismos que podem ser utilizados para replicação dos dados entre servidores.

Entretanto, este projeto não configura replicação automaticamente. A execução com um único contêiner Redis não deve ser considerada uma arquitetura redundante.

A persistência, o backup e a replicação são conceitos diferentes:

- **Persistência:** mantém dados em disco.
- **Backup:** cria uma cópia recuperável dos dados.
- **Replicação:** mantém cópias dos dados em outras instâncias, conforme a configuração.

---

## 16. Solução de problemas comuns

### Problema: `python` não é reconhecido

**Possível causa:** o Python não está instalado corretamente ou não está disponível no PATH.

**Solução:** verifique a instalação e tente:

```bash
python --version
```

No Windows, também é possível tentar:

```bash
py --version
```

### Problema: erro ao instalar as dependências

**Possível causa:** ambiente virtual não ativado, versão incompatível do Python ou problema de conexão com a internet.

**Solução:** ative o ambiente virtual e execute novamente:

```bash
python -m pip install -r requirements.txt
```

### Problema: o Docker não consegue iniciar o contêiner

**Possível causa:** o serviço Docker não está em execução ou já existe um contêiner com o mesmo nome.

**Solução:** confira o estado do Docker:

```bash
docker ps -a
```

Se o contêiner já existir, tente iniciá-lo:

```bash
docker start redis-achados
```

Não crie um segundo contêiner com o mesmo nome.

### Problema: erro de conexão com o Redis

**Possível causa:** o Redis não está em execução, a porta está incorreta ou outro serviço está utilizando a porta 6379.

**Solução:** verifique o contêiner:

```bash
docker ps
```

Teste a conexão:

```bash
docker exec -it redis-achados redis-cli PING
```

Se necessário, confira se o host e a porta configurados em `config.py` correspondem ao ambiente em execução.

### Problema: a página não abre no navegador

**Possível causa:** o servidor Flask não foi iniciado ou a porta 5000 está sendo utilizada por outro programa.

**Solução:** verifique as mensagens do terminal e confirme que o comando abaixo foi executado sem erros:

```bash
python app.py
```

Depois, acesse:

```text
http://127.0.0.1:5000/
```

### Problema: as ocorrências não aparecem

**Possível causa:** o registro não foi criado, o banco consultado é diferente ou o contêiner Redis foi recriado sem persistência dos dados anteriores.

**Solução:** confirme se o Redis está em execução e consulte as chaves:

```bash
docker exec -it redis-achados redis-cli SMEMBERS ocorrencias:ids
```

Se o conjunto estiver vazio, verifique se existem registros no banco e se a aplicação está conectada ao Redis esperado.

### Problema: o erro `Address already in use`

**Possível causa:** outro processo já está utilizando a porta que a aplicação tenta abrir.

**Solução:** encerre o processo que utiliza a porta ou ajuste a porta do serviço responsável, de acordo com a necessidade.

---

## 17. Segurança e limitações

O Reencontra foi desenvolvido com finalidade acadêmica e para execução local.

Algumas limitações importantes:

- A aplicação não implementa um sistema completo de autenticação e autorização.
- O servidor Flask em modo de desenvolvimento não deve ser utilizado como servidor de produção.
- O Redis deste exemplo não está configurado com autenticação ou acesso restrito personalizado.
- Não há replicação automática configurada.
- A persistência em disco e os backups dependem da configuração do Redis.
- A comparação de ocorrências fornece sugestões e não confirma automaticamente a identidade de um objeto.
- A configuração padrão de chave secreta do Flask deve ser substituída por uma chave forte e protegida antes de qualquer implantação real.
- A aplicação deve ser executada em um ambiente controlado, sem expor desnecessariamente o servidor Flask ou o Redis à rede.

Para uso em produção, seria necessário implementar controles adicionais de segurança, proteção dos dados, gerenciamento de credenciais, persistência, backup e monitoramento.

---

## 18. Considerações finais

O Reencontra demonstra como uma aplicação web pode utilizar um banco de dados NoSQL chave-valor para resolver um problema cotidiano.

O projeto integra uma interface desenvolvida com HTML e CSS, uma aplicação Python utilizando Flask e o Redis como mecanismo de armazenamento.

Além das operações CRUD, a aplicação utiliza diferentes estruturas de dados do Redis para organizar os registros, realizar consultas e manter informações auxiliares.

O desenvolvimento permite explorar aspectos importantes de bancos NoSQL, como suas estruturas de armazenamento, suas operações, suas vantagens e limitações, bem como os cuidados necessários com persistência, backup e redundância.

---

**Projeto acadêmico — Reencontra**  
**Tecnologias principais:** Python, Flask, Redis, Docker, HTML, CSS e Jinja.