from sklearn.cluster import FeatureAgglomeration
from fastsklearnfeature.declarative_automl.optuna_package.optuna_utils import categorical
import numpy as np
from fastsklearnfeature.declarative_automl.optuna_package.optuna_utils import id_name

class FeatureAgglomerationOptuna(FeatureAgglomeration):
    def init_hyperparameters(self, trial, X, y):
        self.name = id_name('FeatureAgglomeration_')

        self.n_clusters = trial.suggest_int(self.name + "n_clusters", 2, len(X), log=False)
        self.linkage = trial.suggest_categorical(self.name + "linkage", ["ward", "complete", "average"])

        if self.linkage == 'ward':
            self.affinity = "euclidean"
        else:
            self.affinity = trial.suggest_categorical(self.name + "affinity", ["euclidean", "manhattan", "cosine"])

        self.pooling_func = categorical(trial, self.name + "pooling_func", [np.mean, np.median, np.max])
