# Dependencies
from osgeo import gdal
import geopandas as gpd 
import numpy as np
import os

# Belize Geometry
blz_path = "C:/Users/ryanm/Files/base_data/pyramids/countries_iso3.gpkg" 
# Reproject the mask layer to Robinson
blz_mask = "C:/Users/ryanm/Dropbox (Personal)/Files/apec_8601/env8601_project/base_data/aoi_BLZ_reproject.gpkg"
iso_blz = gpd.read_file(blz_path)
iso_blz = iso_blz[iso_blz['iso3']=='BLZ']
iso_blz = iso_blz.to_crs('ESRI:54030')
iso_blz.to_file(blz_mask, driver = 'GPKG')

# Command: Warp and reproject
def wrap_proj(input, output): # Credit to Matt Braaksma (E.g., he showed me how to use the GDAL function)
    # Warp base data to Belize geometry and Reproject to Robinson projection
    gdal.Warp(output, input, dstSRS = 'ESRI:54030',
            cutlineDSName = blz_mask, cropToCutline = True, dstNodata = np.nan)

# Clip and Reproject for Baseline
seals_lulc_path = 'C:/Users/ryanm/Dropbox (Personal)/Files/apec_8601/env8601_project/seals/projects/BLZ_standard/intermediate/stitched_lulc_simplified_scenarios/'
input_raster = seals_lulc_path + f'lulc_esa_seals7_luh2-message_2017.tif'
output_raster= seals_lulc_path + f'reprojected/lulc_esa_seals7_luh2-message_2017_clipped.tif'
gdal.Warp(output_raster, input_raster, dstSRS = 'ESRI:54030')

# Reproject the SEALS LULC base data to Robinson (redefine)
scenario_list = ['ssp1_rcp26', 'ssp5_rcp85']
year_list = [2030, 2035, 2045]

for scenario in scenario_list:
    for year in year_list:
        input_raster = seals_lulc_path + f'lulc_esa_seals7_{scenario}_luh2-message_bau_{year}_clipped.tif'
        output_raster= seals_lulc_path + f'reprojected/lulc_esa_seals7_{scenario}_luh2-message_bau_{year}_clipped.tif'
        gdal.Warp(output_raster, input_raster, dstSRS = 'ESRI:54030')

### Precipitation
input_path = "C:/Users/ryanm/Files/base_data/mesh/worldclim/baseline/5min/baseline_bio12_Annual_Precipitation.tif"
output_path = "C:/Users/ryanm/Dropbox (Personal)/Files/apec_8601/env8601_project/base_data/invest/precipitation.tif"
wrap_proj(input_path, output_path)

### Evapotranspiration
input_path = "C:/Users/ryanm/Files/base_data/mesh/cgiar_csi/pet.tif"
output_path = "C:/Users/ryanm/Dropbox (Personal)/Files/apec_8601/env8601_project/base_data/invest/evapotranspiration.tif"
wrap_proj(input_path, output_path)

### Root Restricting Layer Depth
input_path = "C:/Users/ryanm/Files/base_data/mesh/isric/depth_to_root_restricting_layer.tif"
output_path = "C:/Users/ryanm/Dropbox (Personal)/Files/apec_8601/env8601_project/base_data/invest/root-layer-depth.tif"
wrap_proj(input_path, output_path)

### Plant Avaliable Water Content
input_path = "C:/Users/ryanm/Files/base_data/mesh/soil/pawc_30s.tif"
output_path = "C:/Users/ryanm/Dropbox (Personal)/Files/apec_8601/env8601_project/base_data/invest/plant-water-content.tif"
wrap_proj(input_path, output_path)

### DEM
input_path = "C:/Users/ryanm/Files/base_data/seals/static_regressors/alt_m.tif"
output_path = "C:/Users/ryanm/Dropbox (Personal)/Files/apec_8601/env8601_project/base_data/invest/dem.tif"
wrap_proj(input_path, output_path)

### Erosivity
input_path = "C:/Users/ryanm/Files/base_data/mesh/GlobalR_NoPol.tif"
output_path = "C:/Users/ryanm/Dropbox (Personal)/Files/apec_8601/env8601_project/base_data/invest/erosivity.tif"
wrap_proj(input_path, output_path)

### Soil Erodibilty
input_path = "C:/Users/ryanm/Files/base_data/mesh/RUSLE_KFactor_v1.1_25km.tif"
output_path = "C:/Users/ryanm/Dropbox (Personal)/Files/apec_8601/env8601_project/base_data/invest/soil_erodibilty.tif"
wrap_proj(input_path, output_path)

### Watersheds
input_path = "C:/Users/ryanm/Files/base_data/mesh/hydrosheds/hydrobasins/hybas_na_lev01-06_v1c/hybas_na_lev06_v1c.shp"
output_path = "C:/Users/ryanm/Dropbox (Personal)/Files/apec_8601/env8601_project/base_data/invest/watershed.shp"

watershed_tif = gpd.read_file(input_path)
watershed_tif = watershed_tif.to_crs('ESRI:54030')
watershed_tif.to_file(output_path, driver = 'GPKG')