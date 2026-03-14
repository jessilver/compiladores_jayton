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
