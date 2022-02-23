# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 21:49:51 2020

@author: John Paudraig Doherty 17346006
X Y Z = 0 0 6 
"""
import numpy as np
import pandas as pd
#------------------------------------------------------------------------------
def createDataFrame():
    """Creates dataframe of subset of data 1986: 1993 from text file 
    EP305Formal2.txt provided
        
            Returns:
                (DataFrame): Dataframe containing the data being analysed.
            
    """
    #reads in the data from the textfile EP305Formal2.txt, skipping the header
    data = np.loadtxt('EP305Formal2.txt', skiprows= 1)
    
    #slices the years from the array of data and converts to a list
    years = list(data[:,0])
    
    #creates a data frame with years as index and months as columns
    df = pd.DataFrame({'January': data[:,1],
                       'February': data[:,2],
                       'March': data[:,3],
                       'April': data[:,4],
                       'May': data[:,5],
                       'June': data[:,6],
                       'July': data[:,7],
                       'August': data[:,8],
                       'September': data[:,9],
                       'October': data[:,10],
                       'November': data[:,11],
                       'December': data[:,12]
                      }, index = years)
    print(df)
    #creates a dataframe for specified range 1986 - 1993
    return df.loc[1986: 1993]
#------------------------------------------------------------------------------
def dataStat(stat, data):
    """Gets the statistics of data based on selection.
        
            Args:
                stat (str): String deciding which stat is to be calculated.
                data (DataFrame): Dataframe containing the data being analysed.
                
            Returns:
                (float): Float value for specified statistic.
                
    """
    if(stat.lower() == 'mean'):
        mean = (data.mean()).mean()
        return mean
    
    elif(stat.lower() == 'median'):
        median = (data.median()).median()
        print(np.median(data.values))
        return median
    
    elif(stat.lower() == 'mode'):
        #finds the mode value of the data
        mode = (((data.mode()).loc[0]).mode()).loc[0]
        return mode
    
    elif(stat.lower() == 'standard deviation'):
        #finds the standard deviation of data
        stdv = (data.std()).mean()
        return stdv
    else:
        print('Invalid Input')
#------------------------------------------------------------------------------
def searchDataFrame(data, searchValue):
    """Gets the statistics of data based on selection.
    
            Args:
                data (DataFrame): Dataframe containing the data being analysed.
                searchValue (set): Set of value/s being searched for. 
                
    """
    #creates list of dataframe values
    values = data.values
    
    #finds position/s of value/s being searched for
    index = np.where(np.isin(values, [e for e in searchValue]))
    
    #returns list of tuples of position and value for value/s being 
    #searched for
    return [(row, col, values[row][col]) for row, 
            col in zip(index[0], index[1])]
#------------------------------------------------------------------------------
def printPercentileCount(data):
    """Creates sorted array of all values from dataframe.
        
            Args:
                data (DataFrame): Dataframe containing the data being analysed.
            
    """
    #creates an empty array for storage
    values = np.array([])
    
    #loops through array of arrays
    for i in range(8):
        values = np.concatenate((values, data.values[i]))
    
    #sorts values
    values = np.sort(values)
    
    #creates index for percentiles
    percentiles = []
    for i in range (0,100, 4):
        percentiles.append('{0:}-{1:}%'.format(i,i+4))
    
    #cuts values into 25 bins
    percentileValues = pd.cut(values, 25)
    
    #creates list of the counts for percentile values
    listValues = pd.Series(percentileValues).value_counts(sort = False).tolist()
    
    #creates proper dataframe with columns and percentile index
    #dfValues = pd.DataFrame({'Count': listValues}, index = percentiles)
    
    #prints the dataframe containing percentiles and their values
    print('\nCalculated number of readings in 4% bins')
    print('\n{0:>25} : {1:}'.format('Percentile Bin','Count'))
    print('\n'.join(map(lambda x: '{0:>25} : {1:}'.format(percentiles[x], 
                                  listValues[x]), range(0, len(percentiles)))))
#------------------------------------------------------------------------------
def plotting(data, mean, median, mode, stdv):
    """Plots data provided.
        
            Args:
                data (DataFrame): Dataframe containing the data being analysed.
                mean (float): Mean of the data provided.
                median (float): Median of the data provided.
                mode (float): Mode of the data provided.
                stdv (float): Standard Deviation of the data provided.
            
    """
    
    #creates axes object for plot of months for values against years
    ax = data.plot(figsize = (13,10), colormap='Spectral')
    
    #adds gridlines to the plot
    ax.grid(c = 'k', ls = '--', lw = 0.5)
    
    #sets axes labels
    ax.set(xlabel = 'Year', ylabel = 'Month Values', )
    
    #changes the background colour of the plot to make lines clearer
    ax.set_facecolor('#aFaFaF')
    
    #changes legend colour to make lines clearer
    ax.legend(title='Month Line Colours', fancybox=True, facecolor='#ffd1e7')
    
    #adds mean value to the plot
    ax.text(1986.6, -1, 'Mean:{0:.2f}'.format(mean), fontsize = 18,
            fontweight='heavy', fontfamily='monospace', c='#1b1b1b')
    #plots line for mean
    ax.plot([1986,1993],[mean,mean], c='#1b1b1b', ls='--', lw=2)
    
    #adds median value to the plot
    ax.text(1986.7, -4, 'Median:{0:.2f}'.format(median), fontsize = 18,
            color='#944700', fontweight='heavy', fontfamily='monospace')
    #plots line for median
    ax.plot([1986,1993],[median,median], c='#944700', ls='--', lw=2)
    
    #adds mode value to the plot
    ax.text(1987.4, -16, 'Mode:{0:.2f}'.format(mode), fontsize = 18,
            color='b', fontweight='heavy', fontfamily='monospace')
    #plots line for mode
    ax.plot([1986,1993],[mode,mode], c='b', ls='--', lw=2)
    
    #adds standard deviation value to the plot
    ax.text(1986, 13, 'Standard Deviation:{0:.2f}'.format(stdv), 
            fontsize = 18, color='#6f00ff', fontweight='heavy', 
            fontfamily='monospace')
#------------------------------------------------------------------------------
def printStats(labels, stats):
    """Prints the statistic to the screen.
        
            Args:
                label (list): List containing labels for statistical labels.
                stats (list): List containing statiscal values.
            
    """
    #prints title for table
    print('\n{:>35}'.format('Statistical Information'))
    
    #prints labelled statistical information in table format
    print('\n'.join(map(lambda x: '{0:>25} :{1:^10.2f}'
                        .format(labels[x], stats[x]), range(0, len(stats)))))
#------------------------------------------------------------------------------
def checkMonth(monthPos):
    """Gets the month from corresponding position in dataframe.#
    
            Args:
                monthPos (int): Integer from posiiton corresponding to a month.
                
            Returns:
                (str): The month as a String from position.
                
    """
    #switch statement for months
    switch = {
        0: "January",
        1: "February",
        2: "March",
        3: "April",
        4: "May",
        5: "June",
        6: "July",
        7: "August",
        8: "September",
        9: "October",
        10: "November",
        11: "December"
    }    
    return switch.get(monthPos, 'Invalid Month')
#------------------------------------------------------------------------------
def checkYear(yearPos):
    """Gets the year from corresponding position in dataframe.
    
            Args:
                monthPos (int): Integer from posiiton corresponding to a year.
                
            Returns:
                (int): The year as an int from position.
                
    """
    #switch statment for my subset of years
    switch = {
        0: 1986,
        1: 1987,
        2: 1988,
        3: 1989,
        4: 1990,
        5: 1991,
        6: 1992,
        7: 1993,
    }    
    return switch.get(yearPos, 'Invalid Year')
#------------------------------------------------------------------------------
def printPosition(label, result):
    """Prints value along with it's position.
        
            Args:
                label (str): String denoting what is being printed
                result (tuple): Tuple containing value and its position.
            
    """
    print('{0:>20} value: {1:.3f}. {2:>}: {3:} {4:}'.format(label,
        result[2], 'Occurence',checkMonth(result[1]), checkYear(result[0])))
#------------------------------------------------------------------------------
def main():
    
    #calls function to get dataframe of my subset of the data
    data = createDataFrame()
    
    #creates list for stat value labels
    statsLabels=['Mean', 'Median', 'Mode', 'Standard Deviation']
    
    #finds the mean value of the data
    mean = dataStat(statsLabels[0], data)

    #finds the median value of the data
    median = dataStat(statsLabels[1], data)
    
    #finds the mode value of the data
    mode = dataStat(statsLabels[2], data)
    
    #finds the standard deviation of data
    stdv = dataStat(statsLabels[3], data)
    
    #finds the minimum and maximum value and their positions
    minmax = searchDataFrame(data, {(data.min()).min(),(data.max()).max()})
    
    #prints percentile data
    printPercentileCount(data)
    
    #plots subset data
    plotting(data, mean, median, mode, stdv)
    
    #prints stats in table output
    printStats(statsLabels, [mean, median, mode, stdv])
    
    #prints minimum value and its position
    printPosition('Minimum',minmax[0])
    #prints maximum value and its position
    printPosition('Maximum',minmax[1])
#------------------------------------------------------------------------------
#calls the main method
if __name__ == '__main__' : main()