# Plot the raster for output from InVEST Model 

# Dependencies
import os 
from osgeo import gdal 
import matplotlib.pyplot as plt 

# Reused content
scenario_list = ['ssp1', 'ssp5']
year_list = [2030, 2035, 2045]
output_path = os.path('C:\Users\ryanm\Dropbox (Personal)\Files\apec_8601\env8601_project\invest')

## Model Output: Carbon 
for scenario in scenario_list:
    for year in year_list:
        output_file = os.path(output_path + f'carbon-{scenario}-{year}\tot_c_cur.tif')
        img = np.dstack((b1, b2, b3)) 
        f = plt.figure() 
        plt.imshow(img) 
        plt.savefig(os.path(output_path + f'carbon-{scenario}-{year}\tot_c_cur.png') 


## Model Output: Pollination


## Nurtient Retention 


## Sediment Retention


## Water Yield


