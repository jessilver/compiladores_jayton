param(
    [string]$ANTLR_VERSION = "4.11.1",
    [string]$GRAMMAR = "Expr.g4",
    [string]$OUTDIR = "generated"
)

# Create output dir
if (-not (Test-Path -Path $OUTDIR)) {
    New-Item -ItemType Directory -Path $OUTDIR | Out-Null
}

# Optionally set version
if ($ANTLR_VERSION -ne "") {
    $env:ANTLR4_TOOLS_ANTLR_VERSION = $ANTLR_VERSION
}

# Run ANTLR (wrapper will download jar if needed). Gera Visitor também.
antlr4 -Dlanguage=Python3 -visitor -o $OUTDIR $GRAMMAR

Write-Host "Generated files are in: $OUTDIR (inclui Visitor)"
