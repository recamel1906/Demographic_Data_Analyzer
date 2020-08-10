import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the
    # index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = (pd.Series(data=df['age'].values, index=df['sex'])[' Male'].values.mean()).round(1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = (100 * (df['education'].value_counts()[' Bachelors']) / df.shape[0]).round(1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[df['education'].isin([' Bachelors', ' Masters', ' Doctorate'])]['salary'].value_counts()
    lower_education = df[~df['education'].isin([' Bachelors', ' Masters', ' Doctorate'])]['salary'].value_counts()

    # percentage with salary >50K
    higher_education_rich = round(
        100 * higher_education[' >50K'] / (higher_education[' >50K'] + higher_education[' <=50K']), 1)
    lower_education_rich = round(
        100 * lower_education[' >50K'] / (lower_education[' >50K'] + lower_education[' <=50K']), 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours].shape[0]
    min_hours_salary = df[df['hours-per-week'] == min_work_hours]['salary'].value_counts()

    rich_percentage = 100 * min_hours_salary[' >50K'] / min_hours_salary.values.sum()

    # What country has the highest percentage of people that earn >50K?
    country_gt50K_counts = df[df['salary'] == ' >50K']['native-country'].value_counts()
    percentages = 100 * country_gt50K_counts / country_gt50K_counts.values.sum()

    highest_earning_country = (percentages[percentages == max(percentages.values)].index[0]).strip()
    highest_earning_country_percentage = max(percentages)

    # Identify the most popular occupation for those who earn >50K in India.
    gt50K_data = df[df['salary'] == ' >50K']
    india_gt50K_occupation_counts = gt50K_data[df['native-country'] == ' India']['occupation'].value_counts()

    top_IN_occupation = (india_gt50K_occupation_counts[india_gt50K_occupation_counts ==
                                                       max(india_gt50K_occupation_counts)].index[0]).strip()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
