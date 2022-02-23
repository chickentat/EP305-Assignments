# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 13:27:17 2020

@author: John Paudraig Doherty 17346006
X Y Z = 0 0 6 
"""
import numpy as np
import matplotlib.pyplot as plt
#------------------------------------------------------------------------------
def writeToFile(results):
    """Writes results for slope and y-intercept to a file named 
    EP305simdataXYZ.txt.
            
            Parameter:
                results (ndarray): 2D array containing results for file.
    """
    np.savetxt(fname = 'EP305simdataXYZ.txt', X = results, fmt = '%10.7f',
               delimiter = '\t')
#------------------------------------------------------------------------------
def resultStats(results):
    """Gets the mean and standard deviation of a value or set pf values.
            
            Parameter:
                reults (ndarray): Array containing values.
            
            Returns:
                 (tuple): Tuple containing mean and standard deviation.
    """
    return (np.mean(results), np.std(results))
#------------------------------------------------------------------------------
def print_values(label, stats):
    """Prints correct results with appropriate unit.
            
            Parameter:
                label (str): Label for result.
                stats (tuple): Tuple conatinf mean and standard deviation.
    """
    print(label + ' = {0:.5f} ± {1:.5f}'.format(stats[0], stats[1]))
#------------------------------------------------------------------------------
def model(x0, y0):
    """Prints correct results with appropriate unit.
            
            Parameter:
                x0 (ndarray): Array of x values
                y0 (ndarray): Array of y values
            
            Return:
                a (float): The slope of the model for parameters.
                c (float): The y-intercept of the model for parameters.
    """
    #error values for x and y
    sigmaX = 0.002
    sigmaY = 0.03
    
    #normal random sample for x with sigmaX uncertainty
    x = x0 + np.random.normal(0, sigmaX, size = x0.size)
    
    #normal random sample for y with sigmaY uncertainty
    y = y0 + np.random.normal(0, sigmaY, size = y0.size)
    
    #gets the coefficients for the polynomial 
    a, b, c = np.polyfit(x,y,2)
    return a, c
#------------------------------------------------------------------------------
def simulate(N, all_params, x0, y0):
    """Prints correct results with appropriate unit.
            
            Parameter:
                all_params (ndarray): Empty 2D array.
                x0 (ndarray): Array of x values
                y0 (ndarray): Array of y values
            
            Return:
                all_params (ndarray): 2D array containing slopes and 
                y-intercepts.
    """
    for i in range(N):    
        all_params[i,:] = model(x0, y0)
    
    return all_params
#FIXME------------------------------------------------------------------------------
def plotting(N, slopes, intercepts):
    """plots histograms for slope and y-intercept based on number of 
    simulations and 2D array for results.
            
            Parameter:
                N (int): Int of number of simulations.
                slopes (ndarray): Array of slpoes.
                intercepts (ndarray): Array of y-intercepts.
    """
    #number of bins for histograms
    BINS = min(int(np.sqrt(N)), 100)
    
    #style and size of plots
    plt.figure(dpi=100)
    plt.style.use('ggplot')
    
    #plots histogram for slope
    plt.subplot(121)
    plt.xlabel('Slope Value')
    plt.ylabel('Probability of slope')
    plt.hist(slopes, bins=BINS)
    
    #plots histogram for Y-intercept
    plt.subplot(122)
    plt.xlabel('Y-Intercept Value')
    plt.ylabel('Probability of Y-intercept')
    plt.hist(intercepts, bins=BINS)
    plt.tight_layout()
#------------------------------------------------------------------------------
def main():
    # number of samples
    N = 3000
    
    #60 equidistant values for x between 0 and 1.0
    x0 = np.linspace(0.0, 1.0, 60)
    
    #array of values for y0 and model being simulated
    y0 = (5.2 * x0**2) + 1.5
    
    #initiliases empty 2D array to store results
    all_params = np.empty((N,2))
    
    #simulates the model N times
    all_params = simulate(N, all_params, x0, y0)
    
    #saving values for slope and y-intercept to a text file
    writeToFile(all_params)
    
    #prints mean values for slope and intercept and their uncertainties
    print_values('Slope', resultStats(all_params[:,0]))
    print_values('Y-intercept', resultStats(all_params[:,1]))
    
    #plots histograms for slope and y-intercept
    plotting(N, all_params[:,0], all_params[:,1])
#------------------------------------------------------------------------------
#calls the main method
if __name__ == '__main__' : main()