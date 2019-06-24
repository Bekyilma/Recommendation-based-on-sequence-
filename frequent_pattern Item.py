from gensim.models import Word2Vec
import numpy as np
from Cython.Build import cythonize
import logging

logging.basicConfig(level=logging.INFO)

patterns = []


def load_sequence(from_path):
    with open(from_path) as fp:
        [patterns.append(line.strip().split(",")) for line in fp]


def main():
    load_sequence('/your directory/retail_dataset.csv')
    # split patterns to train_patterns and test_patterns

    train_patterns = np.random.choice(patterns, np.floor(len(patterns) * 0.8))
    test_patterns = np.random.choice(patterns, np.floor(len(patterns) * 0.2))

    # Word vector representation learning
    model = Word2Vec(train_patterns, size=15, window=3, min_count=1, workers=1, iter=3, sample=1e-4, negative=20)


    # Test
    test_size = float(len(test_patterns))
    hit = 0.0
    for current_pattern in test_patterns:
        if len(current_pattern) < 2:
            test_size -= 1.0
            continue
        # Reduce the current pattern in the test set by removing the last item
        last_item = current_pattern.pop()

        # Keep those items in the reduced current pattern, which are also in the models vocabulary
        items = [it for it in current_pattern if it in model.vocab]
        if len(items) <= 2:
            test_size -= 1.0
            continue

        # Predict the most similar items to items
        prediction = model.most_similar(positive=items)

        # Check if the item that we have removed from the test, last_item, is among
        # the predicted ones.
        for predicted_item, score in prediction:
            if predicted_item == last_item:
                hit += 1.0
                #print last_item
                #print prediction

    print 'Accuracy like measure: {}'.format(hit / test_size)


if __name__ == '__main__':
    main()
