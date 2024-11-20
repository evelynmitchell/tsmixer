from datasets import load_dataset


def load_data(dataset_name="mik3ml/timeseries-finance-ETF"):
    """Load the dataset"""
    ds = load_dataset(dataset_name)
    return ds
