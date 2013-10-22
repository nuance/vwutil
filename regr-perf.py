import fileinput
import math

if __name__ == '__main__':
    data = [map(float, line.rstrip().split()) for line in fileinput.input()]

    square_error = 0.0
    num = 0

    for truth, prediction in data:
        num += 1
        square_error += (truth - prediction)**2

    print '    RMSE: %f' % math.sqrt(square_error / num)

    total = sum(truth for truth, _ in data)
    avg = total / num
    total_sum_of_squares = sum((truth - avg)**2 for truth, _ in data)

    print '    RSQR: %f' % (1 - (square_error / total_sum_of_squares))
