import tensorflow as tf

import pandas as pd
CSV_COLUMN_NAMES = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species']
SPECIES = ['Setosa', 'Versicolor', 'Virginica']
train_path="D:\Code\GeneralTool\File\iris_training.csv"
test_path="D:\Code\GeneralTool\File\iris_test.csv"

train = pd.read_csv(train_path, names=CSV_COLUMN_NAMES, header=0)
test = pd.read_csv(test_path, names=CSV_COLUMN_NAMES, header=0)

train_label=train.pop('Species')
test_label=test.pop('Species')

def input_fn(feature,label,training=True,batch_size=256):
    dataset=tf.data.Dataset.from_tensor_slices((dict(feature),label))
    if training:
        dataset=dataset.shuffle(1000).repeat()
    return dataset.batch(batch_size)
my_feature_columns = []
for key in train.keys():
    my_feature_columns.append(tf.feature_column.numeric_column(key=key))

classifier=tf.estimator.DNNClassifier(
    feature_columns=my_feature_columns,
    hidden_units=[30,10],
    n_classes=3
)

classifier.train(
    input_fn=lambda: input_fn(train,train_label),
    steps=5000
)
# eval_result = classifier.evaluate(
#     input_fn=lambda: input_fn(test, test_label, training=False))
#
# print('\nTest set accuracy: {accuracy:0.3f}\n'.format(**eval_result))