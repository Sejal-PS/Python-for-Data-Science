"""
20 - Deep Learning Practice

Practice Tasks

Task 1:
Create a simple neural network for predicting
a numerical target.

Task 2:
Create a binary classification model.

Task 3:
Train a multiclass classification model.

Task 4:
Experiment with different activation functions.

Task 5:
Compare different optimizers.

Task 6:
Add Dropout to a neural network.

Task 7:
Use EarlyStopping.

Task 8:
Build a simple CNN.

Task 9:
Experiment with MNIST.

Task 10:
Create a basic text classification model.
"""


def show_tasks():

    tasks = [
        "Build a regression neural network",
        "Build a binary classification model",
        "Build a multiclass classification model",
        "Compare activation functions",
        "Compare optimizers",
        "Experiment with learning rate",
        "Add Dropout",
        "Use EarlyStopping",
        "Build a CNN for image classification",
        "Build a simple NLP classifier"
    ]

    print("Deep Learning Practice Tasks\n")

    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")


if __name__ == "__main__":
    show_tasks()
