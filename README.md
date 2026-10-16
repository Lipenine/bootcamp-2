# TaskTracker — Fase 2

Aplicação simples de linha de comando (CLI) desenvolvida em Python 3 para cadastrar e visualizar tarefas.

## Funcionalidades
- Cadastro de tarefas com título, descrição, prioridade e data limite.
- Validação de título obrigatório.
- Validação de prioridade: Alta, Média/Media ou Baixa.
- Status inicial definido automaticamente como Pendente.
- Listagem organizada das tarefas.
- Mensagem clara quando ainda não existem tarefas cadastradas.

## Tecnologias
- Python 3
- Git
- GitHub

## Requisitos
Python 3 instalado. Não são necessárias bibliotecas externas.

## Como executar
Na pasta raiz do projeto, execute:

```bash
python src/main.py
```

Em alguns computadores, pode ser necessário usar `python3` no lugar de `python`.

## Menu
1. Cadastrar nova tarefa
2. Visualizar tarefas cadastradas
3. Sair da aplicação

## Observação
Nesta versão, as tarefas ficam na memória durante a execução. Ao encerrar o programa, os registros não são salvos em arquivo.
