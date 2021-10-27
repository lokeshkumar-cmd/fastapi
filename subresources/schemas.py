from types import ModuleType
from pydantic import BaseModel
from typing import Optional
from enum import Enum

class User(BaseModel):
    user: str
    email: str
    mob: int
    add: Optional[str] = None

class MachineLearningModel(str, Enum):
    randomForest = 'Random Forest'
    linearRegression = 'Linear Regression'
    svd = 'SVD'
    xgBoost = 'XG-Boost'

class Items(BaseModel):
    item_name: str
    quantity: int
    buy: Optional[bool] = False