# Solution is available in the other "solution.py" tab
import numpy as np


def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    # TODO: Compute and return softmax(x)
    exp = np.exp(x)
    return exp / np.sum(exp, axis=0)


logits = [3.0, 1.0, 0.2]
print(softmax(logits))
