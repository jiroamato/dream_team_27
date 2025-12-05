import click
import os
import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from sklearn import set_config
from sklearn.metrics import (
    PredictionErrorDisplay,
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

TARGET = "G3"


@click.command()
@click.option('--test-data', type=str, help="Path to test data")
@click.option('--pipeline-from', type=str, help="Path to the fit pipeline pickle file")
@click.option('--tables-to', type=str, help="Path to directory where table results will be written to")
@click.option('--plot-to', type=str, help="Path to directory where plots will be written to")
@click.option('--seed', type=int, help="Random seed", default=123)
def main(test_data, pipeline_from, tables_to, plot_to, seed):
    """
    Evaluate the student grade predictor on test data and save results.

    Parameters
    ----------
    test_data : str
        Path to the test data CSV file.
    pipeline_from : str
        Path to the pickled pipeline object from training.
    tables_to : str
        Path to directory where table results will be written.
    plot_to : str
        Path to directory where plots will be written.
    seed : int
        Random seed for reproducibility. Default is 123.

    Returns
    -------
    None
        Saves test scores, predictions, and prediction error plot.
    """
    ...  # STUB - implement after tests are written


if __name__ == '__main__':
    main()