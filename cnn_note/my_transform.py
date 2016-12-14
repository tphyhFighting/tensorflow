from sklearn.base import TransformerMixin
from sklearn.utils import as_float_array
class MeanDiscrete(TransformerMixin):
	#计算数据的均值，用内部变量保存该值
	def fit(self,X,y=None):
		X = as_float_array(X)
		self.mean = np.mean(X, axis = 0)
		#返回self,确保早转换器中能够进行链式调用(例如调用transformer.fit(X).transform(X))
		return self
	def transform(self, X):
		X = as_float_array(X)
		assert X.shape[1] == self.mean.shape[0]
		return X > self.mean
