from hate.pipeline.train_pipeline import TrainPipeline
import sys
from hate.logger import logging
from hate.exception import CustomException


train_pipeline = TrainPipeline()
train_pipeline.run_pipeline()