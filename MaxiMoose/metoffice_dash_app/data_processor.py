import os
import pandas as pd
import numpy as np


def main():
    processor_obj = dataProcessor()
    df_averages = processor_obj.build_df()
    print(df_averages)
    df_averages.to_csv('output_csv.csv')


class dataProcessor():

    def build_df(self):

        df = pd.read_csv('output.txt', sep='\s+')
        df.loc[df['sun'] == '---' 'sun'] = np.nan #TODO Replace all missing sun hours values with null, not working
        df_averages = pd.DataFrame(columns=['Month','T Max', 'T Min', 'Rain'])
        dict_months = {'1':'Jan', '2':'Feb', '3':'Mar', '4':'Apr', '5':'May', '6':'Jun',\
             '7':'Jul','8':'Aug', '9':'Sep','10':'Oct','11':'Nov','12':'Dec'}

        #Get weather data for all years, for specified calendar month, allows you to calculate average pattern for month/season
        for month in range(1,13):
            df_per_month = self.df_monthly(df,str(month))
            #print(df_per_month.dtypes)
            df_per_month = df_per_month.astype({'rain': float,'tmax': float, 'tmin': float, 'sun': float},errors='ignore')
            row = {'Month':dict_months[str(month)], 'T Max':df_per_month['tmax'].mean(),\
                 'T Min':df_per_month['tmin'].mean(), 'Rain':df_per_month['rain'].mean()}
            #print(row)
            df_averages = df_averages.append(row, ignore_index=True)#Each loop builds up the seasonal picture through Jan-Dec
        
        if os.path.exists('output.txt'):
            os.remove('output.txt')
  
        return df_averages

    def df_monthly(self, df, month):
        df_result = df[df['mm'] == month]
        return df_result
    

if __name__ == '__main__': main()