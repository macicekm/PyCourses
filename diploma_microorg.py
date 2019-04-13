
# Created by Martin Macíček 13.4.2019
# This script is used for diploma thesis statistical hypothesis evalutation of friend Eliška Rohrerová


import pandas as pd

folder = 'D:\\Users\\mmacicek1695ab\\Desktop\\personal\\Eliška diplomka\\'

def print_mean_std(data):
    """
     SOURCE: https://machinelearningmastery.com/a-gentle-introduction-to-normality-tests-in-python/
     This function prints mean and standard deviation
     :param data: one-dimensional array
     """

    from numpy import mean
    from numpy import std

    # summarize
    print('mean=%.3f stdv=%.3f' % (mean(data), std(data)))


def histogram(data):
    """
    SOURCE: https://machinelearningmastery.com/a-gentle-introduction-to-normality-tests-in-python/
    This function prints histogram plot
    :param data: one-dimensional array
    """
    from matplotlib import pyplot
    pyplot.hist(data)
    pyplot.show()

def qq_plot(data):
    """
    SOURCE: https://machinelearningmastery.com/a-gentle-introduction-to-normality-tests-in-python/
    This function prints qq plot
    :param data: one-dimensional array
    """
    from statsmodels.graphics.gofplots import qqplot
    from matplotlib import pyplot

    qqplot(data, line='s')
    pyplot.show()

def shapiro_wilk_test(data, alpha=0.05):
    """
    SOURCE: https://machinelearningmastery.com/a-gentle-introduction-to-normality-tests-in-python/
    This function executes shapiro_wilk_test
    :param data: one-dimensional array
    :param alpha: level of significance - default=0.05
    """

    from scipy.stats import shapiro

    # normality test
    stat, p = shapiro(data)
    print('shapiro_wilk_test: Statistics=%.3f, p=%.3f' % (stat, p))

    if p > alpha:
        print('Sample looks Gaussian (fail to reject H0)')
    else:
        print('Sample does not look Gaussian (reject H0)')

def d_agostino_test(data, alpha=0.05):
    """
    SOURCE: https://machinelearningmastery.com/a-gentle-introduction-to-normality-tests-in-python/
    This function executes d_agostino_test
    :param data: one-dimensional array
    :param alpha: level of significance - default=0.05
    """

    from scipy.stats import normaltest

    stat, p = normaltest(data)
    print('d_agostino_test: Statistics=%.3f, p=%.3f' % (stat, p))
    if p > alpha:
        print('Sample looks Gaussian (fail to reject H0)')
    else:
        print('Sample does not look Gaussian (reject H0)')

def anderson_darling_test(data):
    """
    SOURCE: https://machinelearningmastery.com/a-gentle-introduction-to-normality-tests-in-python/
    This function executes anderson_darling_test
    :param data: one-dimensional array
    :param alpha: level of significance - default=0.05
    """

    from scipy.stats import anderson

    result = anderson(data)
    print('anderson_darling_test: Statistic: %.3f' % result.statistic)
    p = 0
    for i in range(len(result.critical_values)):
        sl, cv = result.significance_level[i], result.critical_values[i]
        if result.statistic < result.critical_values[i]:
            print('%.3f: %.3f, data looks normal (fail to reject H0)' % (sl, cv))
        else:
            print('%.3f: %.3f, data does not look normal (reject H0)' % (sl, cv))


def independent_ttest(data1, data2, alpha=0.05):
    """
    Function for calculating the t-test for two independent samples

    Student’s t-test: the case where we are comparing the means of two independent samples.

    The result is two samples of the same size where the observations in each sample are related or paired.

    SOURCE: https://machinelearningmastery.com/how-to-code-the-students-t-test-from-scratch-in-python/
    :param data1: first data sample
    :param data2: second data sample
    :param alpha: level of significance - default=0.05
    :return: t statistic, degrees of freedom, critical value, p-value
    """

    # t-test for independent samples
    from math import sqrt
    from numpy import mean
    from scipy.stats import sem
    from scipy.stats import t

    # calculate means
    mean1, mean2 = mean(data1), mean(data2)
    # calculate standard errors
    se1, se2 = sem(data1), sem(data2)
    # standard error on the difference between the samples
    sed = sqrt(se1**2.0 + se2**2.0)
    # calculate the t statistic
    t_stat = (mean1 - mean2) / sed
    # degrees of freedom
    df = len(data1) + len(data2) - 2
    # calculate the critical value
    cv = t.ppf(1.0 - alpha, df)
    # calculate the p-value
    p = (1.0 - t.cdf(abs(t_stat), df)) * 2.0

    print('independent_ttest: t=%.3f, df=%d, cv=%.3f, p=%.3f' % (t_stat, df, cv, p))
    # interpret via critical value
    if abs(t_stat) <= cv:
        print('Accept null hypothesis that the means are equal.')
    else:
        print('Reject the null hypothesis that the means are equal.')
    # interpret via p-value
    if p > alpha:
        print('Accept null hypothesis that the means are equal.')
    else:
        print('Reject the null hypothesis that the means are equal.')

    # return everything
    return t_stat, df, cv, p


def dependent_ttest(data1, data2, alpha=0.05):
    """
    Function for calculating the t-test for two dependent samples
    Also known as paired Student’s t-test

    This is the case where we collect some observations on a sample from the population,
    then apply some treatment, and then collect observations from the same sample.

    The result is two samples of the same size where the observations in each sample are related or paired.

    SOURCE: https://machinelearningmastery.com/how-to-code-the-students-t-test-from-scratch-in-python/
    :param data1: first data sample
    :param data2: second data sample
    :param alpha: level of significance - default=0.05
    :return: t statistic, degrees of freedom, critical value, p-value
    """

    from math import sqrt
    from numpy import mean
    from scipy.stats import t

    # calculate means
    mean1, mean2 = mean(data1), mean(data2)
    # number of paired samples
    n = len(data1)
    # sum squared difference between observations
    d1 = sum([(data1[i]-data2[i])**2 for i in range(n)])
    # sum difference between observations
    d2 = sum([data1[i]-data2[i] for i in range(n)])
    # standard deviation of the difference between means
    sd = sqrt((d1 - (d2**2 / n)) / (n - 1))
    # standard error of the difference between the means
    sed = sd / sqrt(n)
    # calculate the t statistic
    t_stat = (mean1 - mean2) / sed
    # degrees of freedom
    df = n - 1
    # calculate the critical value
    cv = t.ppf(1.0 - alpha, df)
    # calculate the p-value
    p = (1.0 - t.cdf(abs(t_stat), df)) * 2.0

    print('dependent_ttest: t=%.3f, df=%d, cv=%.3f, p=%.3f' % (t_stat, df, cv, p))
    # interpret via critical value
    if abs(t_stat) <= cv:
        print('Accept null hypothesis that the means are equal.')
    else:
        print('Reject the null hypothesis that the means are equal.')
    # interpret via p-value
    if p > alpha:
        print('Accept null hypothesis that the means are equal.')
    else:
        print('Reject the null hypothesis that the means are equal.')

    # return everything
    return t_stat, df, cv, p


def mann_whitney_test(data1, data2, alpha=0.05):
    """
    SOURCE: https://machinelearningmastery.com/nonparametric-statistical-significance-tests-in-python/
    This function executes mann_whitney_test

    The Mann-Whitney U test is a nonparametric statistical significance test for determining
    whether two independent samples were drawn from a population with the same distribution.

    :param data1: first data sample
    :param data2: second data sample
    :param alpha: level of significance - default=0.05
    """
    from scipy.stats import mannwhitneyu

    stat, p = mannwhitneyu(data1, data2)
    print('mann_whitney_test: Statistics=%.3f, p=%.3f' % (stat, p))

    if p > alpha:
        print('Same distribution (fail to reject H0)')
    else:
        print('Different distribution (reject H0)')


def wilcoxon_signed_rank_test(data1, data2, alpha=0.05):
    """
    SOURCE: https://machinelearningmastery.com/nonparametric-statistical-significance-tests-in-python/
    This function executes wilcoxon_signed_rank_test

    In some cases, the data samples may be paired.

    There are many reasons why this may be the case, for example, the samples are related or matched
    in some way or represent two measurements of the same technique.
    More specifically, each sample is independent, but comes from the same population.

    :param data1: first data sample
    :param data2: second data sample
    :param alpha: level of significance - default=0.05
    """

    from scipy.stats import wilcoxon
    stat, p = wilcoxon(data1, data2)
    print('wilcoxon_signed_rank_test: Statistics=%.3f, p=%.3f' % (stat, p))

    if p > alpha:
        print('Same distribution (fail to reject H0)')
    else:
        print('Different distribution (reject H0)')


def anova_test(data1, data2, data3, alpha=0.05):
    """
    SOURCE: https://machinelearningmastery.com/parametric-statistical-significance-tests-in-python/
    This function executes anova_test

    We can perform the Student’s t-test pairwise on each combination of the data samples
    to get an idea of which samples have different means.
    This can be onerous if we are only interested in whether all samples have the same distribution or not.


    To answer this question, we can use the analysis of variance test, or ANOVA for short.
    ANOVA is a statistical test that assumes that the mean across 2 or more groups are equal.
    If the evidence suggests that this is not the case, the null hypothesis is rejected
    and at least one data sample has a different distribution.

    :param data1: first data sample
    :param data2: second data sample
    :param data3: third data sample
    :param alpha: level of significance - default=0.05
    """

    from scipy.stats import f_oneway
    stat, p = f_oneway(data1, data2, data3)

    print('anova_test: Statistics=%.3f, p=%.3f' % (stat, p))
    if p > alpha:
        print('Same distributions (fail to reject H0)')
    else:
        print('Different distributions (reject H0)')



def kruskal_wallis_htest(data1, data2, data3, alpha=0.05):
    """
    SOURCE: https://machinelearningmastery.com/nonparametric-statistical-significance-tests-in-python/
    This function executes kruskal_wallis_htest

    The Kruskal-Wallis test is a nonparametric version of the one-way analysis of variance test or ANOVA for short.
    It is named for the developers of the method, William Kruskal and Wilson Wallis.
    This test can be used to determine whether more than two independent samples have a different distribution.
    It can be thought of as the generalization of the Mann-Whitney U test.

    :param data1: first data sample
    :param data2: second data sample
    :param data3: third data sample
    :param alpha: level of significance - default=0.05
    """

    from scipy.stats import kruskal
    # compare samples
    stat, p = kruskal(data1, data2, data3)
    print('kruskal_wallis_htest: Statistics=%.3f, p=%.3f' % (stat, p))
    if p > alpha:
        print('Same distributions (fail to reject H0)')
    else:
        print('Different distributions (reject H0)')

def friedman_test(data1, data2, data3, alpha=0.05):
    """
    SOURCE: https://machinelearningmastery.com/nonparametric-statistical-significance-tests-in-python/
    This function executes friedman_test

    The Friedman test is the nonparametric version of the repeated
    measures analysis of variance test, or repeated measures ANOVA.
    The test can be thought of as a generalization of the Kruskal-Wallis H Test to more than two samples.

    # The assumption is that all samples have the same number of observations

    :param data1: first data sample
    :param data2: second data sample
    :param data3: third data sample
    :param alpha: level of significance - default=0.05
    """

    from scipy.stats import friedmanchisquare
    stat, p = friedmanchisquare(data1, data2, data3)
    print('friedman_test: Statistics=%.3f, p=%.3f' % (stat, p))
    if p > alpha:
        print('Same distributions (fail to reject H0)')
    else:
        print('Different distributions (reject H0)')


if __name__ == '__main__':

    df_raw_data = pd.read_excel(f'{folder}data.xlsx', sheet_name='raw_data')
    df_cpm_data_22_36_joined = pd.read_excel(f'{folder}data.xlsx', sheet_name='cpm_data_22_36_joined')

    data = df_cpm_data_22_36_joined['DIFF_CPM']

    data_cpm_summer = df_cpm_data_22_36_joined['LETO_CPM']
    data_cpm_winter = df_cpm_data_22_36_joined['ZIMA_CPM']

    data_3way_studna = pd.read_excel(f'{folder}data.xlsx', sheet_name='cpm_3waycomparison_studna')
    data_3way_vodovod = pd.read_excel(f'{folder}data.xlsx', sheet_name='cpm_3waycomparison_vodovod')
    data_3way_balena = pd.read_excel(f'{folder}data.xlsx', sheet_name='cpm_3waycomparison_balena')

    data_cpm_studna = data_3way_studna['CPM']
    data_cpm_vodovod = data_3way_vodovod['CPM']
    data_cpm_balena = data_3way_balena['CPM']



    ###################################################################################################
    # Differences between winter and summer

    histogram(data)
    qq_plot(data)
    
    shapiro_wilk_test(data)
    d_agostino_test(data)
    anderson_darling_test(data)
    # data does not seem to be normal


    
    # Test based on assumption of normality
    independent_ttest(data_cpm_summer, data_cpm_winter)  # works for independent samples
    dependent_ttest(data_cpm_summer, data_cpm_winter)  # works for dependent samples
    
    # Non-Parametric tests
    mann_whitney_test(data_cpm_summer, data_cpm_winter)  # works for independent samples
    wilcoxon_signed_rank_test(data_cpm_summer, data_cpm_winter)   # works for dependent samples


    ###################################################################################################
    # Differences between water sources

    # Three way tests
    shapiro_wilk_test(data_cpm_studna)
    shapiro_wilk_test(data_cpm_vodovod)
    shapiro_wilk_test(data_cpm_balena)

    anova_test(data_cpm_studna, data_cpm_vodovod, data_cpm_balena)  # parametric independent samples

    kruskal_wallis_htest(data_cpm_studna, data_cpm_vodovod, data_cpm_balena)  # non-parametric independent samples

    mann_whitney_test(data_cpm_studna, data_cpm_vodovod)
    mann_whitney_test(data_cpm_studna, data_cpm_balena)
    mann_whitney_test(data_cpm_vodovod, data_cpm_balena)

