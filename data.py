from scipy import stats
import numpy

numbers = [23,45,23,56,74,34,6,7,8,]

#finds the middle numeber
median = numpy.median(numbers)
#the average number
mean = numpy.mean(numbers)
#the most common numeber
mode = stats.mode(numbers)
#finds the diffrence between each value 
standard = numpy.std(numbers)
#the spread between each of the numbers
var = numpy.var(numbers)
#gives you a percentile of value in the array
percentile = numpy.percentile(numbers, 10)
print(f"this is the median: {median}")
print(f"this is the mean: {mean}")
print(f"this is the mode: {mode}")
print(f"this is the variance: {var}")
print(f"this is the standard: {standard}")
print(f"this is the percentile: {percentile}")