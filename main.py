dataset_raw = []
dataset = []
dataset_file = open("datasettest", 'r')
for line in dataset_file.readlines():
    dataset_raw.append(line)
for i in range(len(dataset_raw)):
    dataset.append([])
    for j in range(len(dataset_raw[i])):
        if dataset_raw[i][j] == ' ':
            dataset[i].append(int(dataset_raw[i][0:j]))
            dataset[i].append(int(dataset_raw[i][j+1:-1]))
            break
dataset_file.close()
print(dataset)


def j_func(theta0, theta1, m, dataset):
    j = 0
    for i in range(m):
        j += ((theta0 + dataset[i][0] * theta1) - dataset[i][1]) ** 2
    j *= 1 / (2 * m)
    return j


def j_derivative_theta1(theta0, theta1, m, dataset):
    j = 0
    for i in range(m):
        j += ((theta0 + dataset[i][0] * theta1) - dataset[i][1]) * dataset[i][0] / m
    return j


def j_derivative_theta0(theta0, theta1, m, dataset):
    j = 0
    for i in range(m):
        j += ((theta0 + dataset[i][0] * theta1) - dataset[i][1]) / m
    return j

counter = 0
theta0 = 0
theta1 = 0
eps = float(1)
alpha = 0.001
while abs(eps) > 0:
    new_theta0 = theta0 - alpha * j_derivative_theta0(theta0, theta1, len(dataset), dataset)
    new_theta1 = theta1 - alpha * j_derivative_theta1(theta0, theta1, len(dataset), dataset)
    eps = theta0 - new_theta0
    theta0, theta1 = new_theta0, new_theta1
    counter += 1
    print('Counter: ', counter)


print(round(theta0, 2), round(theta1, 2))
