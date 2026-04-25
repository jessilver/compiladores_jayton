# visualizer.py
import graphviz
from ast_nodes import Number, Identifier, BinOp, Assign

# visualizer.py atualizado

def draw_ast(node, filename="ast_output"):
    dot = graphviz.Digraph(comment='Abstract Syntax Tree')
    dot.attr('node', shape='box', style='rounded,filled', fontname='Helvetica')

    def traverse(curr_node):
        if curr_node is None: return None
        node_id = str(id(curr_node))

        # Pegamos o tipo anotado (se existir) para exibir na etiqueta
        # Exemplo: "Número (2.0) [FLOAT]"
        tipo_anotado = f"\n[{curr_node.eval_type}]" if hasattr(curr_node, 'eval_type') else ""

        if isinstance(curr_node, Assign):
            label = f"Atribuição (=)\n{curr_node.name}{tipo_anotado}"
            dot.node(node_id, label, fillcolor='lightgreen')
            child_id = traverse(curr_node.expr)
            if child_id: dot.edge(node_id, child_id)

        elif isinstance(curr_node, BinOp):
            label = f"Operação ({curr_node.op}){tipo_anotado}"
            dot.node(node_id, label, fillcolor='lightyellow')
            left_id = traverse(curr_node.left)
            right_id = traverse(curr_node.right)
            dot.edge(node_id, left_id)
            dot.edge(node_id, right_id)

        elif isinstance(curr_node, Number):
            label = f"Número\n{curr_node.value}{tipo_anotado}"
            dot.node(node_id, label, fillcolor='lightpink')

        elif isinstance(curr_node, Identifier):
            label = f"Variável\n{curr_node.name}{tipo_anotado}"
            dot.node(node_id, label, fillcolor='lightcyan')

        return node_id

    traverse(node)
    dot.render(filename, format='png', view=True, cleanup=True)

def print_ast(node, prefix="", is_last=True):
    if node is None: return

    # Adicionamos a exibição do tipo no terminal também
    tipo = f" [{node.eval_type}]" if hasattr(node, 'eval_type') else ""

    if isinstance(node, Assign):
        node_name = f"Atribuição (=) -> '{node.name}'{tipo}"
    elif isinstance(node, BinOp):
        node_name = f"Operação ({node.op}){tipo}"
    elif isinstance(node, Number):
        node_name = f"Número ({node.value}){tipo}"
    elif isinstance(node, Identifier):
        node_name = f"Variável ({node.name}){tipo}"
    else:
        node_name = "Nó Desconhecido"

    marker = "└── " if is_last else "├── "
    print(f"{prefix}{marker}{node_name}")
    new_prefix = prefix + ("    " if is_last else "│   ")

    if isinstance(node, Assign):
        print_ast(node.expr, new_prefix, True)
    elif isinstance(node, BinOp):
        print_ast(node.left, new_prefix, False)
        print_ast(node.right, new_prefix, True)