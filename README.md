# compiladores_jayton

Quick commands to generate and test the `Expr.g4` grammar.

PowerShell (Windows)

```powershell
# Activate virtual environment (if not active)
. .\venv\Scripts\Activate

# Ensure Java 11 is used for this session (adjust path as needed)
$temurinBin='C:\Program Files\Eclipse Adoptium\jdk-11.0.30.7-hotspot\bin'
$env:PATH = "$temurinBin;$env:PATH"
java -version

# Install Python runtime dependencies
python -m pip install -r requirements.txt

# Generate parser into current directory:
antlr4 -Dlanguage=Python3 Expr.g4

# Or generate into dedicated folder `generated/` using the helper script:
.\generate_parser.ps1                # optional: -ANTLR_VERSION 4.11.1

# Test the generated parser
python test_parser.py
```

Bash / WSL / macOS

```bash
# Activate virtual environment
source venv/bin/activate

# Ensure Java 11 is available in PATH (example)
export ANS="/usr/lib/jvm/temurin-11/bin"
export PATH="$ANS:$PATH"
java -version

# Install runtime
python -m pip install -r requirements.txt

# Generate parser into current dir:
antlr4 -Dlanguage=Python3 Expr.g4

# Or generate into `generated/`:
./generate_parser.sh 4.11.1

# Test
python test_parser.py
```

Notes

- If `antlr4` wrapper fails to find a jar, use `-v <version>` or set `ANTLR4_TOOLS_ANTLR_VERSION`.
- Keep generated files in `generated/` (scripts already provided); `.gitignore` ignores that folder.

Ferramentas para aprendizado (ver etapas)

```powershell
# Ver tokens (lexer)
python tools\dump_tokens.py -s "1+2*3"

# Ver árvore de parse (toStringTree)
python tools\show_parse_tree.py -s "1+2*3"

# Ver enter/exit de regras (walker/listener)
python tools\listener_trace.py -s "1+2*3"

# Avaliar com visitor (gera resultados; requer -visitor no gerador)
python VisitorInterp.py example.txt
```

Gere o parser com `-visitor` (os scripts já fazem isso):
`./generate_parser.ps1` ou `./generate_parser.sh`

## Comandos finais (rápido)

Use estes comandos para reproduzir todo o pipeline localmente (Windows PowerShell / Bash). São passos mínimos e diretos.

PowerShell (Windows)

```powershell
# ativar o venv
& .\venv\Scripts\Activate.ps1

# instalar dependências
python -m pip install -r requirements.txt

# gerar parser (gera visitor também)
.\generate_parser.ps1

# garantir que o projeto e generated/ estejam no PYTHONPATH
$env:PYTHONPATH = (Resolve-Path .).Path + ";" + (Resolve-Path generated).Path

# inspeções/checagens (lexer -> parser -> tree -> listener -> visitor)
python .\tools\dump_tokens.py -s "1+2*3"
python .\tools\show_parse_tree.py -s "1+2*3"
python .\tools\listener_trace.py -s "1+2*3"
python .\tools\run_visitor.py example.txt

# teste rápido
python test_parser.py
```

Bash / WSL / macOS

```bash
# ativar venv
source venv/bin/activate

# instalar dependências
python3 -m pip install -r requirements.txt

# gerar parser (gera visitor também)
./generate_parser.sh 4.11.1

# garantir PYTHONPATH
export PYTHONPATH="$(pwd):$(pwd)/generated"

# inspeções
python3 tools/dump_tokens.py -s '1+2*3'
python3 tools/show_parse_tree.py -s '1+2*3'
python3 tools/listener_trace.py -s '1+2*3'
python3 tools/run_visitor.py example.txt

# teste rápido
python3 test_parser.py
```

## CI

O workflow (`.github/workflows/ci.yml`) já faz:

- instalar dependências
- baixar o JAR do ANTLR e gerar o parser em `generated/`
- executar `tools/dump_tokens.py`, `tools/show_parse_tree.py`, `tools/listener_trace.py`, `tools/run_visitor.py` e `test_parser.py`.
