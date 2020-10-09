
# coding: utf-8

# In[1]:


class CompareModels:
    def __init__(self):
        import pandas as pd
        self._models = pd.DataFrame(
            data=['r', 'R^2', 'RMSE', 'RMSRE', 'MAPE'],
            columns=['Model']
        ).set_index(keys='Model')
        
    def add(self, model_name, y_test, y_pred):
        import numpy as np
        from sklearn.metrics import r2_score, mean_squared_error
        self._models[model_name] = np.array(
            object=[
                np.corrcoef(y_test, y_pred)[0, 1], # r
                r2_score(y_true=y_test, y_pred=y_pred), # R^2
                np.sqrt(mean_squared_error(y_true=y_test, y_pred=y_pred)), # RMSE
                np.sqrt(np.mean(((y_test-y_pred)/y_test)**2)), # RMSRE
                np.mean(np.abs((y_test-y_pred) / y_test)) * 100 # MAPE
            ]
        )
        
    def R2AndRMSE(y_test, y_pred):
        import numpy as np
        from sklearn.metrics import r2_score, mean_squared_error
        return r2_score(y_true=y_test, y_pred=y_pred), np.sqrt(mean_squared_error(y_true=y_test, y_pred=y_pred))
    
    @property
    def models(self):
        return self._models
    
    @models.setter
    def models(self, _):
        print('Cannot perform such task.')
    
    def show(self, **kwargs):
        import matplotlib.pyplot as plt
        kwargs['marker'] = kwargs.get('marker', 'X')
        self._models.plot(**kwargs)
        plt.xticks(range(len(self._models)), self._models.index)
        plt.xlabel('')
        plt.axis('auto')
        plt.show()

