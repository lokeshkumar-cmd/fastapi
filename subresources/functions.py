from . import schemas


def model_info(models):
    if models == schemas.MachineLearningModel.randomForest:
        return {"model_name": models, "message": "branching method!"}

    if models.value == 'SVD':
        return {"model_name": models, "message": "SVD all the images"}

    if models  == models.xgBoost.value:
        return {"model_name": models, "message": "Multiple Regression"}

    return {"model_name": models, "message": "Have some left"}