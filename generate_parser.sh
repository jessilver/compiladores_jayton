#!/usr/bin/env bash
ANTLR_VERSION="${1:-}"
GRAMMAR="${2:-Expr.g4}"
OUTDIR="${3:-generated}"

mkdir -p "$OUTDIR"
if [ -n "$ANTLR_VERSION" ]; then
  export ANTLR4_TOOLS_ANTLR_VERSION="$ANTLR_VERSION"
fi

antlr4 -Dlanguage=Python3 -visitor -o "$OUTDIR" "$GRAMMAR"
echo "Generated files are in: $OUTDIR (includes Visitor)"
