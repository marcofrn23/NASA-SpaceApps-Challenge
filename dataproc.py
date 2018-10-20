from pandas import *
import requests
import json
#import pandasql


class DataProcessor:
    ''' a class to get data with an HTTP api request and eventually
    to output them into a file'''

    def __init__(self, name='', API_URL=''):
        self.name = name
        if API_URL is '': 
            self.load = False
            self.source =''
        else:
            self.source = API_URL
            self.load = True

    def get_data(self, API_URL=''):
        if self.source == '': self.source = API_URL
        self.fileformat = ".json"

        assert self.source is not '','No valid url provided'

        self.load = True
        self.data_txt = requests.get(self.source).text
        if self.fileformat == ".json":
            self.data = json.loads(self.data_txt)
            self.df = DataFrame(self.data)
            #self.data.describe()

    def show(self):
    	print(self.df)
    	#print(self.df.describe())


    def manage_data(self):
    	## critical part, data manipulation to be defined ##
    	pass

    def write_back(self,filename,fformat=".csv"):

        assert fformat in (".csv", ".json"), "File format invalid or unspecified"

        if filename is '': filename = "new.csv"
        else:
            filename += fformat
            with open(filename, 'w') as out_file:
                if fformat == ".csv":
                    out_file.write(self.df.to_csv())
                elif fformat == ".json":
                    out_file.write(self.df.to_json())
        print("Wrote data in file "+filename)


    def __repr__(self):
    	return f'''DataProcessor('{self.name}','{self.source}', {self.fileformat}')'''


if __name__=="__main__":

    dp = DataProcessor("myData")
    dp.get_data('https://launchlibrary.net/1.4/agency')
    dp.write_back("apollo")
    dp.show()
	