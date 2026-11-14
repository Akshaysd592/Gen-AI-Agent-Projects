# here we are going to calculate cosine similarity

import numpy as np

def cosine_similarity(vector1, vector2): #function to return cosine values
    v1 = np.array(vector1)
    v2 = np.array(vector2)
    return np.dot(v1,v2)/(
        np.linalg.norm(v1)*
        np.linalg.norm(v2)
    )

