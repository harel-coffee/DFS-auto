from fastsklearnfeature.transformations.NumericUnaryTransformation import NumericUnaryTransformation
from sklearn.preprocessing import MinMaxScaler
from sklearn.base import BaseEstimator
from sklearn.feature_selection.base import SelectorMixin
from fastsklearnfeature.candidates.CandidateFeature import CandidateFeature
from typing import List
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import sympy
import numpy as np
from sklearn.model_selection import GridSearchCV
import copy
from hyperopt import fmin, tpe, hp, STATUS_OK, Trials
from hyperopt.pyll.base import scope
import time
import pandas as pd
import inspect
import pickle

import fastsklearnfeature.interactiveAutoML.feature_selection.WrapperBestK as wrap


class RunAllKBestSelection(BaseEstimator, SelectorMixin):
	def __init__(self, selection_strategy, max_complexity=None, min_accuracy=None, model=None, parameters=None, cv=None, scoring=None, fit_time_out=None):
		self.selection_strategy = selection_strategy
		self.my_pipeline = Pipeline([('select', wrap.WrapperBestK(self.selection_strategy)),
									 ('model', model)
									 ])
		wrap.map_fold2ranking[self.selection_strategy.score_func.__name__] = {}
		print(self.selection_strategy.score_func.__name__)

		self.parameters = parameters
		self.cv = cv
		self.max_complexity = max_complexity
		self.min_accuracy = min_accuracy
		self.scoring = scoring
		self.fit_time_out = fit_time_out


	def fit(self, X, y=None):
		self.map_k_to_results = {}

		for k in range(1, self.max_complexity + 1):
			start_time = time.time()
			print(k)
			parameters = copy.deepcopy(self.parameters)
			parameters['select__' + 'k'] = [int(k)]

			cv_eval = GridSearchCV(estimator=self.my_pipeline, param_grid=parameters, cv=self.cv, scoring=self.scoring)
			cv_eval.fit(pd.DataFrame(X), y)

			self.map_k_to_results[k] = (cv_eval.best_score_, time.time() - start_time)

		pfile = open("/tmp/all"+ self.selection_strategy.score_func.__name__ + ".p", "wb")
		pickle.dump(self.map_k_to_results, pfile)
		pfile.flush()
		pfile.close()

		wrap.map_fold2ranking[self.selection_strategy.score_func.__name__] = {}

		return self



	def _get_support_mask(self):
		return self.mask_