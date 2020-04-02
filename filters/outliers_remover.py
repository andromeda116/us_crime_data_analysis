import pandas as pd
from custom_utilities import agency_categorizer as agncy_cat

fnl_mn = pd.read_csv('/Users/salma/Research/us_crime_data_analysis/data/final_main_gte_10k.csv')
print('fnl_mn: ', fnl_mn.shape[0])

fnl_mn['ori_yr'] = fnl_mn['ORI'] + fnl_mn['YEAR'].astype(str)

fnl_mn_ols = pd.read_csv('/Users/salma/Research/us_crime_data_analysis/data/final_main_rep1_12_clean1_core_counts_low_3z.csv')
print('fnl_mn_ols: ', fnl_mn_ols.shape[0])

fnl_mn_ols['ori_yr'] = fnl_mn_ols['ORI'] +fnl_mn_ols['YEAR'].astype(str)

# https://stackoverflow.com/questions/37313691/how-to-remove-a-pandas-dataframe-from-another-dataframe - piRSquared's ans
# fnl_mn_without_lower_3z = pd.concat([fnl_mn, fnl_mn_ols], sort=False, ignore_index=True).drop_duplicates(subset=['ORI', 'YEAR'], keep=False)

#fnl_mn_without_lower_3z = fnl_mn[~fnl_mn.ori_yr.isin(fnl_mn_ols.ori_yr)]

fnl_mn_without_lower_3z = fnl_mn[~fnl_mn.ori_yr.isin(fnl_mn_ols.ori_yr)]

print('fnl_mn_without_lower_3z: ', fnl_mn_without_lower_3z.shape[0])

## rounding population_mean to have count.
# fnl_mn_without_lower_3z.loc[:, 'population_mean'] = fnl_mn_without_lower_3z['population_mean'].round()


## In cleaned_icpsr_crime_enhancer.py, was using 100000 multiplier for incarceration too.
## But 10000 in initial rates.py. So need to update incarceration rates to be multiplied with only 10000 and not 100000

agncy_cat.categorize_agencies(df=fnl_mn_without_lower_3z, op_path='/Users/salma/Research/us_crime_data_analysis/data/wdt_lower_3z',
                              fl_name='final_main_without_lower_3z')
