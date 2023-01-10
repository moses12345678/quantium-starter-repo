import pandas
def managedata():

        # load the first CSV file
        df1 = pandas.read_csv('data/daily_sales_data_0.csv', index_col='product')
        # load the second CSV file
        df2 = pandas.read_csv('data/daily_sales_data_1.csv', index_col = 'product')
        #load the third CSV file
        df3 =  pandas.read_csv('data/daily_sales_data_2.csv', index_col = 'product')


        # combine them vertically
        df = pandas.concat([df1,df2,df3])
        # select on the product name "pink morsel and calculate the price* quty without $ sign"
        df['Sales'] = df['quantity'].multiply(df['price'].str.replace("$", "").astype(float))
        df = df.loc['pink morsel',['Sales','date','region']]
        #.assign(Sales=df['price'] * df['quantity'],inplace=True).head(5)
        df = df.sort_values(by='region', ascending=True)
        # Save the combined DataFrame to a new CSV file
        df.to_csv('combined_file.csv', index=False)
        print(df)

if __name__ == '__main__':
    managedata()