# Como Contribuir
## Configurando o Ambiente de Desenvolvimento
### 1. Instale o Nodejs, npm e npx
1. Baixe o Node.js em [nodejs.org](https://nodejs.org) (versão LTS recomendada)
2. Execute o instalador e siga os passos padrão
3. O npm e npx são instalados automaticamente com o Node.js

### 2. Clone o repositório
Navegue para uma pasta vazia e execute o seguinte comando:
```console
git clone https://github.com/syntax-terror-256/new-amorim.git .
```

### 3. Instale a ferramenta uv
#### winget
Execute o seguinte comando para instalar a ferramenta uv usando winget:
```console
winget install --id=astral-sh.uv  -e
```

#### pip
Execute o seguinte comando para instalar a ferramenta uv usando pip:
```console
pip install uv
```

#### Outros métodos
Escolha alguma das várias opções de instalação disponíveis no [site da ferramenta](https://docs.astral.sh/uv/getting-started/installation/#installation-methods).

### 4. Instale as dependências do projeto
Abra um terminal no diretório raiz do projeto e execute os seguintes comandos:
```console
uv sync
```
```console
npm install
```

### 5. Instale as extensões usadas no desenvolvimento
- [**Black Formater**](https://marketplace.visualstudio.com/items/?itemName=ms-python.black-formatter) - Linter utilizado na formatação do código *Python*.
- [**Django**](https://marketplace.visualstudio.com/items/?itemName=batisteo.vscode-django) - Extensão que adiciona suporte ao framework *Django* e *Django Templates*.
- [**Tailwind CSS IntelliSense**](https://marketplace.visualstudio.com/items/?itemName=bradlc.vscode-tailwindcss) - Extensão que adiciona suporte ao framework *Tailwind CSS*.


## Testando o Projeto
Abra um novo terminal e execute o seguinte comando para iniciar o servidor e Tailwind CSS em modo debug:
```console
uv run scripts.py dev
```
