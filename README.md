# compiladores_jayton

Guia rapido para gerar parser/visitor da gramatica `Expr.g4`, visualizar a arvore e executar o interpretador.

## Requisitos

- Java 11+ no `PATH`
- Python com `venv`

## Setup

PowerShell (Windows)

```powershell
& .\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Bash / WSL / macOS

```bash
source venv/bin/activate
python3 -m pip install -r requirements.txt
```

## Gerar os arquivos do ANTLR

Use sempre `-visitor` para o `VisitorInterp` funcionar corretamente.

PowerShell (Windows)

```powershell
.\generate_parser.ps1 -ANTLR_VERSION 4.11.1
```

Bash / WSL / macOS

```bash
./generate_parser.sh 4.11.1
```

Alternativa direta:

```powershell
antlr4 -Dlanguage=Python3 -visitor -o generated Expr.g4
```

## Uso real (interpretador)

Coloque expressoes em um arquivo, por exemplo `entrada.txt`:

```txt
1+2*3;
x=10;
y=x+2;
y*3;
```

Execute:

```powershell
python tools\run_visitor.py entrada.txt
```

## Ferramentas de inspeção

```powershell
python tools\dump_tokens.py -s "1+2*3;"
python tools\show_parse_tree.py -s "1+2*3;"
python tools\listener_trace.py -s "1+2*3;"
python test_parser.py
```

## Visualização grafica da arvore (ANTLR)

Com o launcher da venv (Windows):

```powershell
.\venv\Scripts\antlr4-parse.exe Expr.g4 start_ -gui
```

Depois digite a entrada, por exemplo `1+2*3;`, e finalize com `Ctrl+Z` + `Enter`.

Se preferir usar arquivo de entrada:

```powershell
Get-Content .\entrada.txt | .\venv\Scripts\antlr4-parse.exe Expr.g4 start_ -gui
```

## Notas

- Se o wrapper `antlr4` nao achar jar, defina `ANTLR4_TOOLS_ANTLR_VERSION` ou passe versao nos scripts.
- Os artefatos gerados ficam em `generated/`.

## CI

O workflow em `.github/workflows/ci.yml`:

- instala dependencias
- gera parser em `generated/`
- executa `tools/dump_tokens.py`, `tools/show_parse_tree.py`, `tools/listener_trace.py`, `tools/run_visitor.py` e `test_parser.py`
