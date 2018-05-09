import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt


class QuantileSmoother:

    def __init__(self, n_samples, q):
        self.n_samples = n_samples
        self.buffer = np.zeros((n_samples,))
        self.q = q
        self.chunk_size = 0

    def apply(self, chunk: np.ndarray):
        chunk_size = chunk.shape[0]
        self.chunk_size = chunk_size
        if chunk_size <= self.n_samples:
            self.buffer[:-chunk_size] = self.buffer[chunk_size:]
            self.buffer[-chunk_size:] = chunk
        else:
            self.buffer = chunk[-self.n_samples:]
        return np.ones(chunk_size) * np.percentile(self.buffer, self.q * 100)