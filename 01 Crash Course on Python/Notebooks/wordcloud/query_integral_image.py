# cython: boundscheck=False
# cython: wraparound=False
import array
import numpy as np


def query_integral_image(integral_image, size_x, size_y, random_state):
    x = integral_image.shape[0]
    y = integral_image.shape[1]
    hits = 0
    # count how many possible locations
    for i in range(x - size_x):
        for j in range(y - size_y):
            area = integral_image[i, j] + integral_image[i + size_x, j + size_y]
            area -= integral_image[i + size_x, j] + integral_image[i, j + size_y]
            if not area:
                hits += 1
    if not hits:
        # no room left
        return None
    # pick a location at random
    goal = random_state.randint(0, hits)
    hits = 0
    for i in range(x - size_x):
        for j in range(y - size_y):
            area = integral_image[i, j] + integral_image[i + size_x, j + size_y]
            area -= integral_image[i + size_x, j] + integral_image[i, j + size_y]
            if not area:
                hits += 1
                if hits == goal:
                    return i, j
