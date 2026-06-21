def classify_cell(features):

    if features is None:
        return "Unknown"

    if features["circularity"] < 0.65:
        return "Possible Sickle RBC"

    return "Normal RBC"