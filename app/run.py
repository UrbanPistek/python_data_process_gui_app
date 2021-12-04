import process
import os
import dotenv as env

# =============== Custom Modules ===============
# Import custom processing module
p = process.Process()

# ================== Constants =================
# Path to the data file 
DATA_FILE = str(os.path.dirname(os.path.dirname(__file__))) + 'data.csv'

# ============ Enviroment Variables ============
env.load_dotenv()
GMAPS_API_KEY = str(os.getenv('GOOGLE_MAPS_API_KEY'))

# =================== Main =====================
print("Data File: ",DATA_FILE)
p.df_set_data(DATA_FILE)

# p.test_distance_matrix()
# print('Dist Matrix: ', p.dist_matrix)

# determine all distances per address
p.df_calculate_distances()

print('==== Test ====')
# p.df_extrapolate_date()