Segue um modelo de `README.md` baseado no seu script e estruturado como documentação de projeto acadêmico:

````md
# Atividade em Python - Agenda 11

## Controle de Níveis de Água utilizando a biblioteca Colorama

### Descrição do Projeto

Este projeto foi desenvolvido com o objetivo de simular um sistema simples de monitoramento de níveis de água em um reservatório, utilizando a linguagem Python e a biblioteca `colorama` para destacar visualmente as situações do reservatório através de cores no terminal.

O sistema recebe um valor numérico entre **0 e 4**, representando diferentes níveis de água, e exibe uma tabela contendo:

- Nível do reservatório
- Situação atual
- Status operacional indicado por cores

O uso das cores auxilia na interpretação rápida das condições do reservatório, simulando um ambiente real de monitoramento.

---

## Tecnologias utilizadas

- Python 3
- Biblioteca Colorama

---

## Biblioteca utilizada

A biblioteca `colorama` permite adicionar cores ao terminal, facilitando a visualização das mensagens de alerta.

Instalação:

```bash
pip install colorama
```

Importação utilizada no projeto:

```python
from colorama import Fore, Style, init
```

---

## Estrutura do sistema

O programa trabalha com:

### Lista de níveis do reservatório

```python
lista_niveis = [
"Nível Crítico",
"Nível Baixo",
"Nível Moderado",
"Nível Bom",
"Nível Máximo"
]
```

### Situações monitoradas

| Entrada | Situação | Status | Cor |
|----------|-----------|---------|------|
| 0 | Nível muito baixo | Crítico | Vermelho |
| 1 | Nível baixo | Atenção 1 | Amarelo |
| 2 | Nível médio | Atenção 2 | Verde |
| 3 | Nível alto | Ideal | Ciano |
| 4 | Nível muito alto | Transbordo | Azul |

---

## Funcionamento

O usuário informa um valor entre **0 e 4**.

Exemplo:

```bash
Insira um número entre 0 e 4: 2
```

Saída:

```
Nivel do reservatório | Situação | STATUS
---------------------------------------------
Nível médio           | Atenção2 | VERDE
```

A cor exibida no terminal será aplicada automaticamente utilizando o recurso da biblioteca `colorama`.

---

## Estruturas utilizadas

O desenvolvimento utiliza conceitos fundamentais estudados anteriormente:

- Listas
- Estruturas condicionais (`if`, `elif`, `else`)
- Entrada de dados (`input`)
- Manipulação de texto (`f-string`)
- Biblioteca externa (`colorama`)
- Formatação visual no terminal

---

## Objetivo acadêmico

Esta atividade tem como finalidade praticar:

- Organização de código em Python
- Uso de bibliotecas externas
- Simulação de sistemas reais
- Exibição de informações formatadas no terminal
- Aplicação de lógica condicional

---

## Autor

Desenvolvido para a atividade **Agenda 11 – Controle de Níveis de Água em Python**.

---

## Exemplo visual esperado

```
Nivel do reservatório | Situação | STATUS
---------------------------------------------
Nível muito baixo     | Crítico  | VERMELHO
```

(Cada status será apresentado com sua respectiva cor no terminal.)

---

### Fim do documento
````
