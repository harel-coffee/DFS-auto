from sklearn.decomposition import TruncatedSVD
from fastsklearnfeature.declarative_automl.optuna_package.optuna_utils import id_name

class TruncatedSVDOptuna(TruncatedSVD):
    def init_hyperparameters(self, trial, X, y):
        self.name = id_name('TruncatedSVD_')

        self.target_dim = trial.suggest_int(self.name + "target_dim", 10, 256)

