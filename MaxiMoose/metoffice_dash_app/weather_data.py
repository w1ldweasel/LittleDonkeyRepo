import os
import requests

def main(): #testing this component with one station data
    city_weather_output = weatherData()
    city_weather_output.build_data('https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/cardiffdata.txt')


class weatherData():

    def build_data(self, path):
        station_response = self.weather_station_call(path)
        if (station_response != False):
            self.clean_data(station_response)


    def weather_station_call(self, path):

        try:
            resp = requests.get(path)
            #print(resp.status_code)
            if (resp.status_code == 200):
                file_name = 'raw_data.txt'
                with open(file_name, 'wb') as writer:
                    writer.write(resp.content)
                    return file_name
            else:
                return False

        except requests.HTTPError as exception:
            print(exception)


    def clean_data(self, file_name):
        line_number = 0
        with open(file_name, 'r+') as readwriter:
            lines = readwriter.readlines()
            readwriter.seek(0)
            for line in lines:
                if line.find('yyyy') == -1:
                    line_number = line_number + 1
                else:
                    break #found the table header now break out of loop
            #print(str(line_number))
            readwriter.writelines(lines[line_number:])
        with open(file_name, 'r') as reader:
            lines = reader.readlines()
            reader.seek(0)
            for line in lines:
                cleaned_line = line.replace('#', ' ')
                cleaned_line = cleaned_line.replace('*', ' ')
                if 'Provisional' not in cleaned_line.strip('\n'):
                    with open('output.txt', 'a') as writer:
                        writer.writelines(cleaned_line)
 
        if os.path.exists(file_name):
            os.remove(file_name)


if __name__ == '__main__': main()