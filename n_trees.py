import argparse

parser = argparse.ArgumentParser(description="Nombre d'arbre?")
parser.add_argument(
    "--n_trees", type=int, default=1500, help="Un nombre d'arbre"
)
args = parser.parse_args()
N_TREES = args.n_trees
print(args.n_trees)
