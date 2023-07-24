import numpy as np
import tensorflow as tf

print('TF version:', tf.__version__)

model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=25, activation='relu'),
    tf.keras.layers.Dense(units=15, activation='relu'),
    tf.keras.layers.Dense(units=1, activation='linear') # linear replaces sigmoid, also adding from_logits when compiling (see below). This reduces numerical roundoff errors.
])

# sigmoid is: 1 / (1 + e^-z)

# set the loss function, for training:
model.compile(
    loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
    optimizer = tf.keras.optimizers.Adam(learning_rate=0.01), # Adam is more efficient than Linear Regression, as it adjusts the learning rate up or down as needed, and has a separate learning rate for each parameter (for each weight Wj + the bias B).
    )

# train
X = np.array([[100, 1]])
Y = np.array([[1]])
logit = model.fit(X, Y, epochs=100)

# predict - need convert from linear to sigmoid
f_x = tf.nn.sigmoid(logit)
