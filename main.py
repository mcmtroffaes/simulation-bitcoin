import csv
import math

import numpy as np
from matplotlib import pyplot as plt

with open("BTC-USD.csv") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # skip header
    data = [float(row[1]) for row in reader]
log_data = [math.log(x) for x in data]
sigma2 = np.mean([(x2 - x1) ** 2 for x1, x2 in zip(log_data[1:], log_data[:-1])])
num_segments = 20


def make_segments(xs):
    size = len(log_data) // num_segments
    idx = [slice(i * size, (i + 1) * size) for i in range(num_segments)]
    return [range(len(xs))[i] for i in idx], [xs[i] for i in idx]


indices, segments = make_segments(data)
_, log_segments = make_segments(log_data)


def plot1():
    plt.figure(figsize=(10, 6))
    for index, segment in zip(indices, segments):
        plt.plot(index, segment, linestyle="-")
    plt.title("Bitcoin Value")
    plt.xlabel("$t$")
    plt.ylabel("$x_t$")
    plt.grid(True)
    plt.savefig("btc1.png")


def plot2():
    plt.figure(figsize=(10, 6))
    for index, segment in zip(indices, log_segments):
        plt.plot(index, segment, linestyle="-")
    plt.title("Bitcoin Value")
    plt.xlabel("$t$")
    plt.ylabel("$\\log x_t$")
    plt.grid(True)
    plt.savefig("btc2.png")


def plot3():
    plt.figure(figsize=(10, 6))
    for segment in log_segments:
        plt.plot(segment, linestyle="-")
    plt.title("Bitcoin Value")
    plt.xlabel("$t$")
    plt.ylabel("$\\log x_t$")
    plt.grid(True)
    plt.savefig("btc3.png")


def plot4():
    plt.figure(figsize=(10, 6))
    for segment in log_segments:
        segment2 = [x - segment[0] for x in segment]
        plt.plot(segment2, linestyle="-")
    plt.plot(
        [1.96 * np.sqrt(sigma2 * i) for i in range(len(log_segments[0]))],
        color="black",
        linestyle="dashed",
        label="$\\pm 1.96\\sigma\\sqrt{t}$",
    )
    plt.plot(
        [-1.96 * np.sqrt(sigma2 * i) for i in range(len(log_segments[0]))],
        color="black",
        linestyle="dashed",
        label="$\\pm 1.96\\sigma\\sqrt{t}$",
    )
    plt.title("Bitcoin Value")
    plt.xlabel("$t$")
    plt.ylabel("$\\log x_t - \\log x_0$")
    plt.legend()
    plt.grid(True)
    plt.savefig("btc4.png")


plot1()
plot2()
plot3()
plot4()
