"""
10 - TensorFlow Basics

Learn:
- TensorFlow tensors
- Tensor operations
- Variables
- Basic mathematical operations
"""

import tensorflow as tf


# Create a Tensor
numbers = tf.constant([10, 20, 30, 40])

print("Tensor:")
print(numbers)

print("\nTensor Shape:")
print(numbers.shape)

print("\nTensor Data Type:")
print(numbers.dtype)


# Tensor operations
a = tf.constant([1, 2, 3])
b = tf.constant([4, 5, 6])

print("\nAddition:")
print(tf.add(a, b))

print("\nMultiplication:")
print(tf.multiply(a, b))


# TensorFlow Variable
weight = tf.Variable(2.0)

print("\nInitial Weight:")
print(weight.numpy())

weight.assign(5.0)

print("Updated Weight:")
print(weight.numpy())


# Matrix multiplication
matrix_a = tf.constant([
    [1, 2],
    [3, 4]
])

matrix_b = tf.constant([
    [5, 6],
    [7, 8]
])

result = tf.matmul(matrix_a, matrix_b)

print("\nMatrix Multiplication:")
print(result)
