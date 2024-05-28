from search.config import TrussEnvironmentConfig, UCTSConfig
from search.state import State
from search.truss_search_tree import TreeSearchNode, TrussSearchTree
from search.utils import load_config, read_json


def execute(run_id: str, config_file: str, input_file: str) -> None:
    config = load_config(config_file)
    ucts_config = UCTSConfig(run_id, config)
    truss_env_config = TrussEnvironmentConfig(config)

    nodes = read_json(input_file)

    state = State(config=ucts_config, nodes=nodes, edges=[])

    root = TreeSearchNode(state=state, config=truss_env_config, parent=None)
    mcts = TrussSearchTree(root=root, config=truss_env_config)
    best_node = mcts.best_action(ucts_config.max_iter)

    result = {}
    result["nodes"] = [node.get_json() for node in best_node.state.nodes]
    result["edges"] = [edge.get_json() for edge in best_node.state.edges]
    print(result)
