from experiments import Experiments
from meta_layer_experiment import MetaLayerExperiment

def main():
    content_experiment = Experiments.load_from_file('Ghostwriter Experiment 1')
    experiment = MetaLayerExperiment(content_experiment, 3, 3)
    experiment.run()

if __name__ == '__main__': main()