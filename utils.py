import numpy as np
PRODUCTOS = ["Manzanas", "Peras"]


def gini(x):

    """ Calculate Gini Coefficient """
    # By Warren Weckesser https://stackoverflow.com/a/39513799

    x = np.array(x)
    mad = np.abs(np.subtract.outer(x, x)).mean()  # Mean absolute difference
    rmad = mad / np.mean(x)  # Relative mean absolute difference
    return 0.5 * rmad

def get_0_agents(x):
    i = 0
    for agent in x:
        if agent.get_0_items():
            i+=1
    return i