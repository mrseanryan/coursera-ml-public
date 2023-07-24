# multi-class classification with softmax activation function on the output layer

# MNIST:
# The MNIST database (Modified National Institute of Standards and Technology database) is a large database of handwritten digits that is commonly used for training various image processing systems.

import tensorflow as tf
import numpy as np

model = tf.keras.Sequential([
    tf.keras.Input(shape=(25,)),
    tf.keras.layers.Dense(units=25, activation='relu'), # hidden layer
    tf.keras.layers.Dense(units=15, activation='relu'), # hidden layer
    tf.keras.layers.Dense(units=3, activation='linear'), # softmax output layer - softmax via 'linear' and from_logits in the loss function (see below). This reduces numerical roundoff error.
    # output layer has 1 node for each output class (10 digits)
])

model.summary()


[layer1, layer2, layer3] = model.layers
#### Examine Weights shapes
W1,b1 = layer1.get_weights()
W2,b2 = layer2.get_weights()
W3,b3 = layer3.get_weights()
print(f"W1 shape = {W1.shape}, b1 shape = {b1.shape}")
print(f"W2 shape = {W2.shape}, b2 shape = {b2.shape}")
print(f"W3 shape = {W3.shape}, b3 shape = {b3.shape}")

# X: 3 x low res images of digits, rolled up so 1 row for each image.
X = np.array([[0,1,0,1,0,0,1,0,1,0, 0,255,0,255,0,0,255,0,255,0, 0,255,0,255,0],
              [0,20,0,20,0,0,20,0,20,0, 0,255,0,255,0,0,255,0,255,0, 0,255,0,255,0],
              [0,255,0,255,0,0,255,0,255,0, 0,255,0,255,0,0,255,0,255,0, 0,255,0,255,0]
              ])
print(f"X shape: {X.shape}")
# Y has just 1 class per expected output
Y = np.array([[0], # '0'
              [1], # '1'
              [2] # '2'
              ])
# note: if Y hot-encoded, (just one 1 and others 0) then need loss function like categorical_crossentropy
print(f"Y shape: {Y.shape}")


# sparse - Y can only take on 1 of the N values (although we have P for all N!)
model.compile(loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              optimizer=tf.keras.optimizers.Adam(learning_rate=0.001) # override the default Gradient Descent with the 'smarter' Adams which sets an appropriate learning rate for each variable (Wj + B)
              )

history = model.fit(X, Y, epochs=10)

# predict - need convert from linear to softmax
expected_label = 2 # for this model, labels == indexes (0,1,2)
prediction = model.predict(np.array([[0,255,0,255,0,0,255,0,255,0, 0,255,0,255,0,0,255,0,255,0, 0,255,0,255,0]])) # 2
print(f"predicting: {prediction}")
print(f" Largest Prediction index: {np.argmax(prediction)} (expected {expected_label})")

# If we require a Probability as an output -> then need Softmax (convert the logic to a probability)
prediction_p = tf.nn.softmax(prediction)
print(f" predicting a {expected_label}. Probability vector: \n{prediction_p}")
print(f"Total of predictions: [Softmax -> should always be 1!] {np.sum(prediction_p):0.3f}")
