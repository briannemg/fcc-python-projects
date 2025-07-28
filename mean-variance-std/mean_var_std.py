import numpy as np

def calculate(list):

    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")

    n_array = np.array(list).reshape(3, 3)
    
    calculations = {
        'mean': [np.mean(n_array, axis=0).tolist(), np.mean(n_array, axis=1).tolist(), np.mean(n_array).item()],
        'variance': [np.var(n_array, axis=0).tolist(), np.var(n_array, axis=1).tolist(), np.var(n_array).item()],
        'standard deviation': [np.std(n_array, axis=0).tolist(), np.std(n_array, axis=1).tolist(), np.std(n_array).item()],
        'max': [np.max(n_array, axis=0).tolist(), np.max(n_array, axis=1).tolist(), np.max(n_array).item()],
        'min': [np.min(n_array, axis=0).tolist(), np.min(n_array, axis=1).tolist(), np.min(n_array).item()],
        'sum': [np.sum(n_array, axis=0).tolist(), np.sum(n_array, axis=1).tolist(), np.sum(n_array).item()]
    }

    return calculations