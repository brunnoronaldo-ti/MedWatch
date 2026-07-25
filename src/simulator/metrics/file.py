import pandas as pd
from datetime import datetime, timedelta
import random
from collections import defaultdict

class Metrics:
    def __init__(self):
        self.metrics = defaultdict(list)

    def record_metric(self, metric_name, value):
        self.metrics[metric_name].append(value)

    def save_metrics_to_csv(self, filename):
        df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in self.metrics.items()]))
        df.to_csv(filename, index=False)