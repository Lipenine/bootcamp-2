# Guia de publicação no GitHub

Siga os passos abaixo no terminal, dentro da pasta `tasktracker-projeto`.

## 1. Configure o Git (se ainda não estiver configurado)
```bash
git config --global user.name "SEU NOME"
git config --global user.email "SEU EMAIL DO GITHUB"
```

## 2. Inicialize o repositório e faça o primeiro commit
```bash
git init
git branch -M main
git add README.md .gitignore docs src
git commit -m "chore: cria estrutura inicial do TaskTracker"
```

## 3. Faça commits separados para demonstrar a evolução
Se ainda não fez o commit inicial, você pode começar com a estrutura e depois adicionar o código.
Para criar novos commits de forma real, faça pequenas alterações, salve e execute:
```bash
git add src/main.py
git commit -m "feat: implementa menu principal"
```
Depois, faça outra alteração real (por exemplo, melhorar uma mensagem ou organização do código), salve e execute:
```bash
git add src/main.py
git commit -m "feat: adiciona validacoes de titulo e prioridade"
```

Não crie commits falsos ou repetidos apenas para aparentar histórico; cada commit deve registrar uma mudança real. Se o código completo já estiver no primeiro commit, altere a sequência conforme as mudanças que você realmente fizer.

## 4. Crie o repositório remoto
1. Entre em https://github.com e crie um repositório chamado `tasktracker-projeto`.
2. Não precisa adicionar README no GitHub, pois ele já existe localmente.
3. Copie a URL HTTPS do seu repositório e execute, substituindo a URL abaixo:
```bash
git remote add origin https://github.com/SEU-USUARIO/tasktracker-projeto.git
git push -u origin main
```

## 5. Confira
Atualize a página do GitHub e confirme que `README.md`, `.gitignore`, `src/main.py` e `docs/` aparecem.
Substitua `docs/LEIA-ME-planejamento.txt` pelo PDF original da Fase 1, renomeado para `planejamento_logico.pdf`, se disponível.
