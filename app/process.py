import pandas as pd
import os
import dotenv as env
import googlemaps

# =================== Main =====================
DEBUG_MODE=True

# ============ Enviroment Variables ============
env.load_dotenv()
GMAPS_API_KEY = str(os.getenv('GOOGLE_MAPS_API_KEY'))

# =================== Main =====================
class Process:
    def __init__(self):
        self.home_address = '4643 29 Ave N.W, Calgary, AB'
        self.gmaps_client = googlemaps.Client(key=GMAPS_API_KEY)

    def df_set_data(self, data_path):
        self.df = pd.read_csv(data_path)
        
        # Add column for distance
        self.df['distance'] = 0
        # Add a column for date
        self.df['date'] = '0000-00-00'
        DEBUG_MODE and print(self.df)

    def df_calculate_distances(self):
        for index, row in self.df.iterrows():
            # Modify address value
            self.df.at[index,'address'] = row['address']+', Calgary, AB '+row['postal_code']+', Canada'

            try:
                result = self.gmaps_client.distance_matrix([self.home_address], [row['address']], mode='driving', units='metric')
            except Exception as e:
                print(f'df_calculate_distances [{index}] | {e}')

            # Get distance in km 
            self.df.at[index,'distance'] = self.process_dist_matrix_km(result)

            # Extrapolate dates 
            self.df_extrapolate_date(index, row)

        # Check output
        DEBUG_MODE and print(self.df.head())
        DEBUG_MODE and print(self.df.info())

    def process_dist_matrix_km(self, data):
        # Validate that there is no USA address in the destination address string
        if "USA" in data['destination_addresses'][0]:
            km = None
            print('==> process_dist_matrix_km | error: Distance calculated USA address')
            return km

        km = int(round(data['rows'][0]['elements'][0]['distance']['value']/1000))
        return km

    def _df_extrapolate_date(self):
        # val = pd.date_range(start='2021-01-01', end='2021-01-08')
        # # new_df = pd.DataFrame(index=val, columns=['date','address','distance'])
        # new_df = pd.DataFrame(columns=['date'])
        # new_df['date'] = val
        # print(val)
        # print(new_df)

        # new_val = pd.date_range(start='2021-01-17', end='2021-01-23')
        # new_df2 = pd.DataFrame(columns=['date'])
        # new_df2['date'] = new_val
        
        # new_df = pd.concat([new_df, new_df2])
        # print(new_df)

        val = pd.date_range(start='2021-02-01', end='2021-02-08')
        # new_df = pd.DataFrame(index=val, columns=['date','address','distance'])
        new_df = pd.DataFrame(index=val, columns=['date'])
        new_df['date'] = val
        print(val)
        print(new_df)

        new_val = pd.date_range(start='2021-01-17', end='2021-01-23')
        new_df2 = pd.DataFrame(index=new_val, columns=['date'])
        new_df2['date'] = new_val
        
        new_df = pd.concat([new_df, new_df2])
        print(new_df)

        new_df['date']=pd.to_datetime(new_df['date'])
        new_df.sort_values(by=['date'], inplace=True, ascending=True) # This now sorts in date order
        new_df.reset_index(inplace=True)
        print(new_df)

    def df_extrapolate_date(self, idx, row):
        print(idx, ' | ', row['start_date'])

        dates = pd.date_range(start=row['start_date'], end=row['end_date'])
        

    def test_distance_matrix(self):
        origins = ['Vancouver, BC', 'Seattle, WA']
        destinations = ['San Francisco, CA', 'Victoria, BC']
        mode = 'driving'
        try:
            result = self.gmaps_client.distance_matrix(origins, destinations, mode=mode, units='metric')
            self.dist_matrix = result 
            print(result)
        except Exception as e:
            print(e)