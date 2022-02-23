# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 10:39:50 2020

@author: John Paudraig Doherty 17346006

This is a programme which will calculate the range of frequencies in Terrahertz
and energies in electronvolts of a photon over a default range of 
wavelengths(120-900nm) or an extended user defined range(min,max) where 
min < 120nm and max > 900nm in steps of 100nm
"""
#imported numpy for use in ranges for steps
import numpy as np
#imported scipy for constants used in calculations
import scipy.constants as const
#imported colorama for colour in error messages and headers of table
from colorama import Fore, Style

#classes for errors
class Error(Exception):
   """Base class for other exceptions."""
   pass
class ValueNegative(Error):
   """Raised when the input value is negative."""
   pass
class ValueZero(Error):
   """Raised when the input value is zero."""
   pass
#------------------------------------------------------------------------------
def valueMin(a):
    """Checks if a is above 120 and if so changes it to 120.
            Parameter:
                a (float): A positive float
                
            Returns:
                a (float): A positive float
    """
    if(a>120):
        a = 120
        #tells user their minimum value wasn't accepted
        print('\nUser entered a minimum >120, default value of 120 set for',
              'minimum')
        
    return a
#------------------------------------------------------------------------------
def valueMax(b):
    """Checks if b is less 900 and if so changes it to 900.
            Parameter:
                b (float): A positive float
                
            Returns:
                b (float): A positive float
    """
    if(b<900):
        b = 900
        #tells user their maximum value wasn't accepted
        print('\nUser entered a maximum <900, default value of 900 set for',
              'maximum')
        
    return b
#------------------------------------------------------------------------------
def frequency(waveLength):
    """Returns the frequency of a photon of given wavelength.
            Parameter:
                wavelength (float): A positive float
                
            Returns:
                frequency (float): A positive float
    """
    #calculation for frequency f = c/lambda
    return const.c / (waveLength * 1e-9)
#------------------------------------------------------------------------------
def energyConv(waveLength):
    """Returns the energy in electron volts of photon of given wavlength.
            Parameter:
                energy (float): A positive float
                
            Returns:
                energyeV (float): A positive float
    """
    #enrgy in joules calculation E = hf = hc/lambda
    energyJ = const.h * (const.c / (waveLength * 1e-9))
    
    #converts from joules to eV using relationship stored in scipy constants as
    #it is a more accurate value than 6.241e18
    return (energyJ * 
            const.physical_constants['joule-electron volt relationship'][0])
#------------------------------------------------------------------------------
def main():
    
    print('This is a programme which will calculate the range of frequencies',
          'in Terrahertz and energies in electronvolts of a photon over a',
          'default range of wavelengths(120-900nm) or an extended user',
          'defined range(min,max) where min < 120nm and max > 900nm in steps',
          'of 100nm')
    
    #takes in input a and checks if it is a positive float
    while True:
        try:
            a = float(input('Enter a posiitve float value for a in nanometers'+
                    '(e.g 105.6) a = '))
            
            if(a<0):
                #if a is negative it raises an error 
                raise ValueNegative    
            elif(a==0):
                #if a is equal to zero it raises an error
                raise ValueZero
            else:
                break
        
        #exception messages if raised
        except ValueError:
            print(Fore.RED + Style.BRIGHT + 'Invalid input. Incorrect', 
                      'value type. PLease try again', '\a', Style.RESET_ALL)
        except ValueNegative:
            print(Fore.RED + Style.BRIGHT + 'Invalid input. Wavelength can\'t',
                  'be negative. PLease try again', '\a', Style.RESET_ALL)
        except ValueZero:
            print(Fore.RED + Style.BRIGHT + 'Invalid input. Wavelength can\'t',
                  'be zero in length. PLease try again', '\a', Style.RESET_ALL)
    
    #takes in input b and checks if it is a positive float
    while True:
        try:
            b = float(input('Enter a positive float value for b in nanometers'+
                    '(e.g 937.2) b = '))
            
            if(b<0):
                #if b is negative it raises an error 
                raise ValueNegative    
            elif(b==0):
                #if b is equal to zero it raises an error
                raise ValueZero
            else:
                break
        
        #exception messages if raised
        except ValueError:
            print(Fore.RED + Style.BRIGHT + 'Invalid input. Incorrect', 
                      'value type. PLease try again', '\a', Style.RESET_ALL)
        except ValueNegative:
            print(Fore.RED + Style.BRIGHT + 'Invalid input. Wavelength can\'t',
                  'be negative. PLease try again', '\a', Style.RESET_ALL)
        except ValueZero:
            print(Fore.RED + Style.BRIGHT + 'Invalid input. Wavelength can\'t',
                  'be zero in length. PLease try again', '\a', Style.RESET_ALL)
   
    #makes a the minimum value if neccessary
    if(b<a): 
        a,b = b,a
        
    #checks if inputs are inside the default range
    a = valueMin(a)
    b = valueMax(b)
    
    #prints out formatted headers
    print(Fore.GREEN + "\n{0:m<20} ] {1:m<20} ] {2:m<20}".format(
        'Wavelength(nm)', 'Frequency(THz)', 'Energy(eV)') + Style.RESET_ALL)
    
    #calculates the steps required and stores in an array steps. It maps values 
    #a to above b, filters out values greater than b and then adds b to the end
    steps = [a] + list(filter(lambda x: (x <= b), map(lambda x: x+100, 
                    np.arange(a,b,100)))) + [b]
    
    #converts frequencies to Terrahertz
    terra = lambda x: x*1e-12
    
    #prints outputs, wavelength in nanometers, frequency in terrahertz and 
    #energy in electron volts in desired format over required steps
    #(didnt use loop as map function is more efficient)
    print('\n'.join(map(lambda x: "{0:m<20.5f} ] {1:m<20.5f} ] {2:m<20.5f}"
              .format(x, terra(frequency(x)), energyConv(x)), steps)))
#------------------------------------------------------------------------------   
#calls the main method
if __name__ == '__main__' : main()