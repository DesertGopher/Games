from rich.tree import Tree
from rich import print

tree = Tree("SHA-256 repository")
encode_tree = tree.add("sha-256_encode.py")
modules_tree = tree.add("modules.py")

encode_tree.add("[magenta]def [green]custom_encode[yellow]([white]phrase[yellow])")
encode_tree.add("[magenta]def [green]encode_lib(phrase)")

modules_tree.add("[magenta]def [green]rotate_right[yellow]([white]block, d[yellow])")
modules_tree.add("[magenta]def [green]shift_right[yellow]([white]block, d[yellow])")
modules_tree.add("[magenta]def [green]bin_add[yellow]([white]b1, b2[yellow])")
modules_tree.add("[magenta]def [green]operate_xor[yellow]([white]s01, s02, s03[yellow])")
modules_tree.add("[magenta]def [green]operate_xor_2[yellow]([white]s01, s02[yellow])")
modules_tree.add("[magenta]def [green]operate_and[yellow]([white]s01, s02[yellow])")
modules_tree.add("[magenta]def [green]operate_not[yellow]([white]s01[yellow])")


print(tree)
