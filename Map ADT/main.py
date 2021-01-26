from experiment import experimentRunner
from visualization import visualizer


def main():
    max_n = 10000
    step_size = 50

    config = {}
    config['maps'] = {'Array': 'figures/array_map.png', 'BST': 'figures/BST_map', 'Hash': 'figures/hash_map.png', 'Balanced BST': 'figures/balanced_BST_map'}
    config['operations'] = ['put', 'get', 'contains', 'delete']

    results = experimentRunner.run(config, max_n, step_size)

    for map in results:
        visualizer.plot_results(results[map], map, config['maps'][map])


if __name__ == "__main__":
    main()
