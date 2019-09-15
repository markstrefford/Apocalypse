# import time
# from options.train_options import TrainOptions
# from data import create_dataset
# from models import create_model
# from util.visualizer import Visualizer
import sys
import argparse

print("Usage:\n{0}\n".format(" ".join([x for x in sys.argv])))
print("All settings used:")
print(sys.argv)
for k,v in sorted(sys.argv):
    print("{0}: {1}".format(k,v))
