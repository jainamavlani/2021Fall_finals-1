import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import openpyxl


gdp = pd.read_csv("GDP.csv",skiprows = 4)
personal_expenditure = pd.read_csv("PersonalConsumptionExpenditure.csv")
income = pd.read_excel('tableD1.xlsx',skiprows = 3,usecols = ['Year','Current Dollars'])
income = income.iloc[2:]
population = pd.read_excel('Population.xlsx',skiprows = 16)
gdp_doctest = gdp.iloc[[55,77,81,251,119],:5]
#population_doctest = country_population(population,'France')
population_doctest = population.iloc[:6,:]
population_test = population.iloc[[132,276],:]



def country_gdp(gdp,country_name):
    '''
    We have loaded the gdp data as read CSV. We are calling the function to check whether we get the cleaned data
    in correct format. We made a dummy gdp dataframe named gdp_doctest. In the dataframe, we called the dataframe and
    passed the country name. We got the correct data value.

    :param gdp: Testing gdp data
    :param country_name: Using the country_gdp function whether it returns correct data.
    :return:
    >>> country_gdp(gdp_doctest,'France') # doctest: +NORMALIZE_WHITESPACE
                       gdp
    variable
    1960      6.222548e+10
    '''

    gdp_country = gdp[gdp["Country Name"]==country_name]

    gdp_country.drop('Country Name', axis=1, inplace=True)
    gdp_country.drop('Country Code', axis=1, inplace=True)

    gdp_country.drop('Indicator Name', axis=1, inplace=True)

    gdp_country.drop('Indicator Code', axis=1, inplace=True)
    gdp_country = pd.melt(gdp_country)
    gdp_country = gdp_country.set_index('variable')
    gdp_country = gdp_country.rename(columns = {"value": "gdp"})

    return gdp_country

gdp_USA = country_gdp(gdp,'United States')

gdp_USA

def country_population(population,country_name):
    '''
    We have loaded the population data as read CSV. We are calling the function to check whether we get the cleaned data
    in correct format. We made a dummy population dataframe named population_test and loaded data of some countries. In the dataframe, we called the dataframe and
    passed the country name. We got the correct data value.

    :param population: Testing population data
    :param country_name: Checking country_population data to check whether it returns correct data.
    :return:
    >>> country_population(population_test,'France') # doctest: +NORMALIZE_WHITESPACE
       variable population
    0      1960  45673.147
    1      1961  46266.974
    2      1962  46907.043
    3      1963  47560.825
    4      1964  48184.414
    ..      ...        ...
    56     2016   64667.59
    57     2017  64842.513
    58     2018  64990.512
    59     2019  65129.731
    60     2020  65273.512
    <BLANKLINE>
    [61 rows x 2 columns]

    '''
    population_country = population[(population['Region, subregion, country or area *'] == country_name )]
    population_country = population_country.drop(columns=['Index','Variant','Region, subregion, country or area *','Notes','Country code','Type','Parent code','1950','1951','1952','1953','1954','1955','1956','1957','1958','1959'])
    population_country = pd.melt(population_country)
    population_country.set_index('variable')
    population_country = population_country.rename(columns = {"value": "population"})
    return (population_country)

def merging (country_gdp,country_population):
    '''
    Using this function to merge two tables namely the gdp and the population so that we can have a normalized gdp
    :param country_gdp: gdp of the require country
    :param country_population: population the the required country
    :return: returning the merged table

    >>> merging(country_gdp(gdp,'United States'),country_population(population,'United States of America')) # doctest: +NORMALIZE_WHITESPACE
     variable           gdp  population
    0      1960  5.433000e+11   186720.57
    1      1961  5.633000e+11   189569.85
    2      1962  6.051000e+11  192313.747
    3      1963  6.386000e+11    194932.4
    4      1964  6.858000e+11  197408.497
    ..      ...           ...         ...
    56     2016  1.874508e+13  323015.992
    57     2017  1.954298e+13  325084.758
    58     2018  2.061186e+13  327096.263
    59     2019  2.143322e+13  329064.917
    60     2020  2.093660e+13  331002.647
    <BLANKLINE>
    [61 rows x 3 columns]

    >>> merging(country_gdp(gdp,'Denmark'),country_population(population,'Denmark')) # doctest: +NORMALIZE_WHITESPACE
           variable           gdp population
    0      1960           NaN   4581.099
    1      1961           NaN   4614.027
    2      1962           NaN   4649.341
    3      1963           NaN   4686.269
    4      1964           NaN   4723.623
    ..      ...           ...        ...
    56     2016  3.131159e+11   5711.346
    57     2017  3.321211e+11   5732.277
    58     2018  3.568412e+11   5752.131
    59     2019  3.475613e+11   5771.877
    60     2020  3.560849e+11   5792.203
    <BLANKLINE>
    [61 rows x 3 columns]

    '''
    gdp_population_mix = country_gdp
    gdp_population_mix = pd.merge(gdp_population_mix,country_population,how = 'inner',on = 'variable')
    return gdp_population_mix



