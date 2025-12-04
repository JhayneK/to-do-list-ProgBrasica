<h1 align="center"> To-Do List Básico em Python (CLI) </h1>

<p align="center">
  <a href="#-contribuintes">Contribuintes</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-tecnologias">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-projeto">Projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-como-executar">Como executar</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-melhorias-futuras">Melhorias futuras</a>
</p>

---

### 👥 Contribuintes:
- Jhayne Henemam - [perfil](https://github.com/JhayneK)

---

## 🚀 Tecnologias

Esse projeto foi desenvolvido com as seguintes tecnologias:

- Git e GitHub
- Python
- VSCode (ou qualquer editor de texto de sua preferência)
- Terminal / Prompt de Comando

---

## 💻 Projeto

Este repositório apresenta um **To-Do List básico em Python**, rodando diretamente no terminal (linha de comando).

O objetivo do projeto é demonstrar, de forma simples e didática, conceitos fundamentais de programação:

- uso de **listas**
- criação de **funções**
- estruturas de **decisão** (`if`, `elif`, `else`)
- **laços de repetição** (`while`)
- interação com o usuário via `input()` e `print()`

Tudo isso em um exemplo prático: um gerenciador de tarefas simples.

---

### ✅ Funcionalidades

O programa permite:

- ➕ **Adicionar tarefa**  
  O usuário digita uma descrição e ela é armazenada em uma lista.

- 📋 **Listar tarefas**  
  Mostra todas as tarefas com numeração e status:
  - `[ ]` tarefa pendente  
  - `[X]` tarefa concluída

- ✔ **Marcar tarefa como concluída**  
  O usuário informa o **número** da tarefa e ela é marcada como concluída.

- ❌ **Remover tarefa**  
  O usuário informa o **número** da tarefa e ela é removida da lista.

- 🚪 **Sair do programa**  
  Encerra o loop do menu e finaliza a aplicação.

---

## 🧠 Lógica do Programa

As tarefas são armazenadas em uma lista chamada `tarefas`, onde **cada tarefa é um dicionário** com a seguinte estrutura:

```python
{
    "descricao": "Texto da tarefa",
    "concluida": False  # ou True, quando concluída
}

=== TO-DO LIST ===
1 - Adicionar tarefa
2 - Listar tarefas
3 - Marcar tarefa como concluída
4 - Remover tarefa
5 - Sair
Escolha uma opção: 1
Digite a nova tarefa: Estudar Python
Tarefa adicionada: Estudar Python
------------------------------

=== TO-DO LIST ===
1 - Adicionar tarefa
2 - Listar tarefas
3 - Marcar tarefa como concluída
4 - Remover tarefa
5 - Sair
Escolha uma opção: 2

Suas tarefas:
1. [ ] Estudar Python

git clone https://github.com/SEU-USUARIO/seu-repositorio.git

cd seu-repositorio

python to_do_list.py
