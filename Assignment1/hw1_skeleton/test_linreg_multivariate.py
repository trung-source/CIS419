'''
    TEST SCRIPT FOR MULTIVARIATE LINEAR REGRESSION
    AUTHOR Eric Eaton, Vishnu Purushothaman Sreenivasan
'''

'''
Numpy is a standard library in python that lets you do matrix and vector operations like Matlab in python.
Check out documentation here: http://wiki.scipy.org/Tentative_NumPy_Tutorial
If you are a Matlab user this page is super useful: http://wiki.scipy.org/NumPy_for_Matlab_Users 
'''
import numpy as np
from numpy.linalg import *

# our linear regression class
from linreg import LinearRegression


from test_linreg_univariate import plotData1D
from test_linreg_univariate import plotRegLine1D,visualizeObjective


if __name__ == "__main__":
    '''
        Main function to test multivariate linear regression
    '''
    
    # load the data
    filePath = "CIS419/Assignment1/hw1_skeleton/data/multivariateData.dat"
    # filePath = "CIS419/Assignment1/hw1_skeleton/data/univariateData.dat"
    
    
    file = open(filePath,'r')
    allData = np.loadtxt(file, delimiter=',')

    X = np.matrix(allData[:,:-1])
    y = np.matrix((allData[:,-1])).T
 

    n,d = X.shape
    
    # Standardize
    mean = X.mean(axis=0)
    std = X.std(axis=0)
    X = (X - mean) / std
    
    # Add a row of ones for the bias term
    X = np.c_[np.ones((n,1)), X]
    
    # initialize the model
    init_theta = np.matrix(np.random.randn((d+1))).T
    n_iter = 2000
    alpha = 0.01

    # Instantiate objects
    lr_model = LinearRegression(init_theta = init_theta, alpha = alpha, n_iter = n_iter)
    plotData1D(X[:,1],y,str = "Multivariate Data")
    lr_model.fit(X,y)
    print("x",X.shape,"y",y.shape)
    print("theta",lr_model.theta.shape)
    
    plotRegLine1D(lr_model,X, y,string = "Multivariate Data")
    
 
    
    
    

    # Compute the closed form solution in one line of code
    # thetaClosedForm = 0  # TODO:  replace "0" with closed form solution
    thetaClosedForm = (X.getT()*X).getI()*X.getT()*y
    print("thetaClosedForm: ", thetaClosedForm)


