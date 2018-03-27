from matrices import *
import random
import pylab

def make_matrix(vals):
    '''
    vals: type = list

    This function will take any list and return a matrix object
    '''
    ans = matrix(len(vals), 1)
    ans.add_col_to_matrix(vals, 0)
    return ans


def make_matrix_x(xVals, degree):
    '''
    xVals: type = list
    degree: type = int

    Returns the matrix X housing all training examples and features
    '''

    num_col = degree + 1
    num_row = len(xVals)

    ans = matrix(num_row, num_col)

    for i in range(degree+1):
        if i == 0:
            ans.add_col_to_matrix([1 for i in range(num_row)], 0)
        if i == 1:
            ans.add_col_to_matrix(xVals, 1)
        else:
            ans.add_col_to_matrix([xVals[j]**i for j in range(len(xVals))], i)
    return ans

def init_theta(degree):
    '''
    xVals: type = list
    This function will randomly initialise the values for the theta matrix
    '''
    ans = matrix(degree+1, 1)
    init_values = [random.random() for i in range(degree+1)]
    ans.add_col_to_matrix(init_values, 0)
    return ans

def cost_function(yVals_matrix, estyVals):
    '''
    yVals_matrix: type = matrix
    estyVals: type = matrix

    Returns the value of the least squares error
    '''
    assert yVals_matrix.get_num_rows() == estyVals.get_num_rows(), 'Predicted and actual outcomes have different row lenghts.'
    assert yVals_matrix.get_num_columns() == estyVals.get_num_columns(), 'Predicted and actual outcomes have different column lengths.'

    temp = yVals_matrix - estyVals
    temp = temp**temp
    temp_value = sum(temp.get_column(0))
    ans = (1/(2*yVals_matrix.get_num_rows()))*temp_value
    return ans

def gradient_descent(theta, alpha, x_matrix, yVals_matrix, threshold, max_runs):
    '''
    theta: type = matrix
    alpha: type = float
    threshold: type = float
    max_runs: type = int
    x_matrix: type = matrix
    yVals_matrix: type = matrix
    estyVals: type = matrix

    NOTE:
    alpha is the learning rate, and is a positive float
    threshold is the +- range of the cost function that would be considered a successful run. Reaching the threshold would terminate gradient descent.
    max_runs is the maximum number of times gradient descent will be run. If a result cannot be achived within these runs, the function will return False.
    '''
    estyVals = x_matrix * theta
    ##n is the number of times you want to restart the initialisation of theta, to get out of any plateaus
    n = 100
    break_points = [i*(max_runs//n) for i in range(1,n+1)]
    for run in range(max_runs):
        if run in break_points:
            theta.add_col_to_matrix([random.random() for i in range(len(theta.get_column(0)))],0)
        new_theta = []
        theta_list = theta.get_column(0)
        print(theta_list)
        for row_index in range(len(theta_list)):
            if row_index == 0:
                temp = estyVals-yVals_matrix
                temp = sum(temp.get_column(row_index))
                temp = theta_list[row_index] - (alpha/(yVals_matrix.get_num_rows()))*temp
                new_theta.append(temp)
            else:
                x_matrix_col = matrix(x_matrix.get_num_rows(), 1)
                x_matrix_col.add_col_to_matrix(x_matrix.get_column(row_index),0)
                temp = estyVals-yVals_matrix
                temp = temp**x_matrix_col
                temp = sum(temp.get_column(0))
                temp = theta_list[row_index] - (alpha/(yVals_matrix.get_num_rows()))*temp
                new_theta.append(temp)
        theta.add_col_to_matrix(new_theta, 0)
        original_cost = cost_function(yVals_matrix, estyVals)
        estyVals = x_matrix * theta
        new_cost = cost_function(yVals_matrix, estyVals)
        if abs(new_cost - original_cost) < threshold:
            return theta

    return False

def polyfit(xVals, yVals, degree, alpha = 0.00000000001, threshold = 0.1, max_runs = 100000):
    xVals_matrix = make_matrix_x(xVals, degree)
    yVals_matrix = make_matrix(yVals)
    theta = init_theta(degree)

    theta = gradient_descent(theta, alpha, xVals_matrix, yVals_matrix, threshold, max_runs)

    if not theta:
        return 'Unable to find a good model'
    else:
        pylab.plot(xVals, yVals, 'bo')
        pylab.plot(xVals, (xVals_matrix*theta).get_column(0), 'r-')
        theta.print_matrix()
        pylab.show()

def generate_gaussian_points(x_lower, x_upper, func):
    xVals = []
    yVals = []
    for i in range(x_lower, x_upper + 1):
        yVals.append(func(i) + random.gauss(0, 10))
        xVals.append(i)
    return (xVals, yVals)

xVals, yVals = generate_gaussian_points(1, 100, lambda x: x**3)
# polyfit(xVals, yVals, 2)
x = [1,2,3,4,5,6]
y = [1,2,3,4,5,6]
y2 = [1,4,9,16,25,36]
# polyfit(x,y,1)
# polyfit(x,y,2)
polyfit(xVals, yVals, 3)



###Note: if your coefficients are supposed to have values beyond the 0-1 range, then you must change your code. You cannot use random.random() to generate the initial theta values
