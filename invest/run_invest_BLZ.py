import logging
import sys

import natcap.invest.carbon
import natcap.invest.pollination
import natcap.invest.sdr.sdr
import natcap.invest.ndr.ndr
import natcap.invest.annual_water_yield
import natcap.invest.utils

LOGGER = logging.getLogger(__name__)
root_logger = logging.getLogger()

handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter(
    fmt=natcap.invest.utils.LOG_FMT,
    datefmt='%m/%d/%Y %H:%M:%S ')
handler.setFormatter(formatter)
logging.basicConfig(level=logging.INFO, handlers=[handler])


#################################################
# Module: Run Carbon Storage

## Run for SSP1 2030
args = {
    'calc_sequestration': False,
    'carbon_pools_path': 'C:\\Users\\ryanm\\Dropbox '
                         '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\carbon_pools.csv',
    'discount_rate': '',
    'do_redd': False,
    'do_valuation': False,
    'lulc_cur_path': 'C:\\Users\\ryanm\\Dropbox '
                     '(Personal)\\Files\\apec_8601\\env8601_project\\seals\\projects\\BLZ_standard\\intermediate\\stitched_lulc_simplified_scenarios\\reprojected\\lulc_esa_seals7_ssp1_rcp26_luh2-message_bau_2030_clipped.tif',
    'lulc_cur_year': '',
    'lulc_fut_path': '',
    'lulc_fut_year': '',
    'lulc_redd_path': '',
    'n_workers': '-1',
    'price_per_metric_ton_of_c': '',
    'rate_change': '',
    'results_suffix': '',
    'workspace_dir': 'C:\\Users\\ryanm\\Dropbox '
                     '(Personal)\\Files\\apec_8601\\env8601_project\\invest\\carbon-ssp1-2030',
}

if __name__ == '__main__':
    natcap.invest.carbon.execute(args)

## Run for SSP1 2035
args = {
    'calc_sequestration': False,
    'carbon_pools_path': 'C:\\Users\\ryanm\\Dropbox '
                         '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\carbon_pools.csv',
    'discount_rate': '',
    'do_redd': False,
    'do_valuation': False,
    'lulc_cur_path': 'C:\\Users\\ryanm\\Dropbox '
                     '(Personal)\\Files\\apec_8601\\env8601_project\\seals\\projects\\BLZ_standard\\intermediate\\stitched_lulc_simplified_scenarios\\reprojected\\lulc_esa_seals7_ssp1_rcp26_luh2-message_bau_2035_clipped.tif',
    'lulc_cur_year': '',
    'lulc_fut_path': '',
    'lulc_fut_year': '',
    'lulc_redd_path': '',
    'n_workers': '-1',
    'price_per_metric_ton_of_c': '',
    'rate_change': '',
    'results_suffix': '',
    'workspace_dir': 'C:\\Users\\ryanm\\Dropbox '
                     '(Personal)\\Files\\apec_8601\\env8601_project\\invest\\carbon-ssp1-2035',
}

if __name__ == '__main__':
    natcap.invest.carbon.execute(args)

## Run for SSP1 2045
args = {
    'calc_sequestration': False,
    'carbon_pools_path': 'C:\\Users\\ryanm\\Dropbox '
                         '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\carbon_pools.csv',
    'discount_rate': '',
    'do_redd': False,
    'do_valuation': False,
    'lulc_cur_path': 'C:\\Users\\ryanm\\Dropbox '
                     '(Personal)\\Files\\apec_8601\\env8601_project\\seals\\projects\\BLZ_standard\\intermediate\\stitched_lulc_simplified_scenarios\\reprojected\\lulc_esa_seals7_ssp1_rcp26_luh2-message_bau_2045_clipped.tif',
    'lulc_cur_year': '',
    'lulc_fut_path': '',
    'lulc_fut_year': '',
    'lulc_redd_path': '',
    'n_workers': '-1',
    'price_per_metric_ton_of_c': '',
    'rate_change': '',
    'results_suffix': '',
    'workspace_dir': 'C:\\Users\\ryanm\\Dropbox '
                     '(Personal)\\Files\\apec_8601\\env8601_project\\invest\\carbon-ssp1-2045',
}

if __name__ == '__main__':
    natcap.invest.carbon.execute(args)

## Run for SSP5 2030
args = {
    'calc_sequestration': False,
    'carbon_pools_path': 'C:\\Users\\ryanm\\Dropbox '
                         '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\carbon_pools.csv',
    'discount_rate': '',
    'do_redd': False,
    'do_valuation': False,
    'lulc_cur_path': 'C:\\Users\\ryanm\\Dropbox '
                     '(Personal)\\Files\\apec_8601\\env8601_project\\seals\\projects\\BLZ_standard\\intermediate\\stitched_lulc_simplified_scenarios\\reprojected\\lulc_esa_seals7_ssp5_rcp85_luh2-message_bau_2030_clipped.tif',
    'lulc_cur_year': '',
    'lulc_fut_path': '',
    'lulc_fut_year': '',
    'lulc_redd_path': '',
    'n_workers': '-1',
    'price_per_metric_ton_of_c': '',
    'rate_change': '',
    'results_suffix': '',
    'workspace_dir': 'C:\\Users\\ryanm\\Dropbox '
                     '(Personal)\\Files\\apec_8601\\env8601_project\\invest\\carbon-ssp5-2030',
}

if __name__ == '__main__':
    natcap.invest.carbon.execute(args)

## Run for SSP5 2035 
args = {
    'calc_sequestration': False,
    'carbon_pools_path': 'C:\\Users\\ryanm\\Dropbox '
                         '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\carbon_pools.csv',
    'discount_rate': '',
    'do_redd': False,
    'do_valuation': False,
    'lulc_cur_path': 'C:\\Users\\ryanm\\Dropbox '
                     '(Personal)\\Files\\apec_8601\\env8601_project\\seals\\projects\\BLZ_standard\\intermediate\\stitched_lulc_simplified_scenarios\\reprojected\\lulc_esa_seals7_ssp5_rcp85_luh2-message_bau_2035_clipped.tif',
    'lulc_cur_year': '',
    'lulc_fut_path': '',
    'lulc_fut_year': '',
    'lulc_redd_path': '',
    'n_workers': '-1',
    'price_per_metric_ton_of_c': '',
    'rate_change': '',
    'results_suffix': '',
    'workspace_dir': 'C:\\Users\\ryanm\\Dropbox '
                     '(Personal)\\Files\\apec_8601\\env8601_project\\invest\\carbon-ssp5-2035',
}

if __name__ == '__main__':
    natcap.invest.carbon.execute(args)

## Run for SSP5 2045 
args = {
    'calc_sequestration': False,
    'carbon_pools_path': 'C:\\Users\\ryanm\\Dropbox '
                         '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\carbon_pools.csv',
    'discount_rate': '',
    'do_redd': False,
    'do_valuation': False,
    'lulc_cur_path': 'C:\\Users\\ryanm\\Dropbox '
                     '(Personal)\\Files\\apec_8601\\env8601_project\\seals\\projects\\BLZ_standard\\intermediate\\stitched_lulc_simplified_scenarios\\reprojected\\lulc_esa_seals7_ssp5_rcp85_luh2-message_bau_2045_clipped.tif',
    'lulc_cur_year': '',
    'lulc_fut_path': '',
    'lulc_fut_year': '',
    'lulc_redd_path': '',
    'n_workers': '-1',
    'price_per_metric_ton_of_c': '',
    'rate_change': '',
    'results_suffix': '',
    'workspace_dir': 'C:\\Users\\ryanm\\Dropbox '
                     '(Personal)\\Files\\apec_8601\\env8601_project\\invest\\carbon-ssp5-2045',
}

if __name__ == '__main__':
    natcap.invest.carbon.execute(args)

#################################################
# Module: Run Pollination

## Run for SSP1 2030
args = {
    'farm_vector_path': '',
    'guild_table_path': 'C:\\Users\\ryanm\\Dropbox '
                        '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\pollination_guild_table.csv',
    'landcover_biophysical_table_path': 'C:\\Users\\ryanm\\Dropbox '
                                        '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\pollination_landcover_biophysical_table.csv',
    'landcover_raster_path': 'C:\\Users\\ryanm\\Dropbox '
                             '(Personal)\\Files\\apec_8601\\env8601_project\\seals\\projects\\BLZ_standard\\intermediate\\stitched_lulc_simplified_scenarios\\reprojected\\lulc_esa_seals7_ssp1_rcp26_luh2-message_bau_2030_clipped.tif',
    'n_workers': '-1',
    'results_suffix': '',
    'workspace_dir': 'C:\\Users\\ryanm\\Dropbox '
                     '(Personal)\\Files\\apec_8601\\env8601_project\\invest\\pollinate-ssp1-2030',
}

if __name__ == '__main__':
    natcap.invest.pollination.execute(args)

## Run for SSP1 2035
args = {
    'farm_vector_path': '',
    'guild_table_path': 'C:\\Users\\ryanm\\Dropbox '
                        '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\pollination_guild_table.csv',
    'landcover_biophysical_table_path': 'C:\\Users\\ryanm\\Dropbox '
                                        '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\pollination_landcover_biophysical_table.csv',
    'landcover_raster_path': 'C:\\Users\\ryanm\\Dropbox '
                             '(Personal)\\Files\\apec_8601\\env8601_project\\seals\\projects\\BLZ_standard\\intermediate\\stitched_lulc_simplified_scenarios\\reprojected\\lulc_esa_seals7_ssp1_rcp26_luh2-message_bau_2035_clipped.tif',
    'n_workers': '-1',
    'results_suffix': '',
    'workspace_dir': 'C:\\Users\\ryanm\\Dropbox '
                     '(Personal)\\Files\\apec_8601\\env8601_project\\invest\\pollinate-ssp1-2035',
}

if __name__ == '__main__':
    natcap.invest.pollination.execute(args)

## Run for SSP1 2045
args = {
    'farm_vector_path': '',
    'guild_table_path': 'C:\\Users\\ryanm\\Dropbox '
                        '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\pollination_guild_table.csv',
    'landcover_biophysical_table_path': 'C:\\Users\\ryanm\\Dropbox '
                                        '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\pollination_landcover_biophysical_table.csv',
    'landcover_raster_path': 'C:\\Users\\ryanm\\Dropbox '
                             '(Personal)\\Files\\apec_8601\\env8601_project\\seals\\projects\\BLZ_standard\\intermediate\\stitched_lulc_simplified_scenarios\\reprojected\\lulc_esa_seals7_ssp1_rcp26_luh2-message_bau_2045_clipped.tif',
    'n_workers': '-1',
    'results_suffix': '',
    'workspace_dir': 'C:\\Users\\ryanm\\Dropbox '
                     '(Personal)\\Files\\apec_8601\\env8601_project\\invest\\pollinate-ssp1-2045',
}

if __name__ == '__main__':
    natcap.invest.pollination.execute(args)

## Run for SSP5 2030
args = {
    'farm_vector_path': '',
    'guild_table_path': 'C:\\Users\\ryanm\\Dropbox '
                        '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\pollination_guild_table.csv',
    'landcover_biophysical_table_path': 'C:\\Users\\ryanm\\Dropbox '
                                        '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\pollination_landcover_biophysical_table.csv',
    'landcover_raster_path': 'C:\\Users\\ryanm\\Dropbox '
                             '(Personal)\\Files\\apec_8601\\env8601_project\\seals\\projects\\BLZ_standard\\intermediate\\stitched_lulc_simplified_scenarios\\reprojected\\lulc_esa_seals7_ssp5_rcp85_luh2-message_bau_2030_clipped.tif',
    'n_workers': '-1',
    'results_suffix': '',
    'workspace_dir': 'C:\\Users\\ryanm\\Dropbox '
                     '(Personal)\\Files\\apec_8601\\env8601_project\\invest\\pollinate-ssp5-2030',
}

if __name__ == '__main__':
    natcap.invest.pollination.execute(args)

## Run for SSP5 2035
args = {
    'farm_vector_path': '',
    'guild_table_path': 'C:\\Users\\ryanm\\Dropbox '
                        '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\pollination_guild_table.csv',
    'landcover_biophysical_table_path': 'C:\\Users\\ryanm\\Dropbox '
                                        '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\pollination_landcover_biophysical_table.csv',
    'landcover_raster_path': 'C:\\Users\\ryanm\\Dropbox '
                             '(Personal)\\Files\\apec_8601\\env8601_project\\seals\\projects\\BLZ_standard\\intermediate\\stitched_lulc_simplified_scenarios\\reprojected\\lulc_esa_seals7_ssp5_rcp85_luh2-message_bau_2035_clipped.tif',
    'n_workers': '-1',
    'results_suffix': '',
    'workspace_dir': 'C:\\Users\\ryanm\\Dropbox '
                     '(Personal)\\Files\\apec_8601\\env8601_project\\invest\\pollinate-ssp5-2035',
}

if __name__ == '__main__':
    natcap.invest.pollination.execute(args)

## Run for SSP5 2045
args = {
    'farm_vector_path': '',
    'guild_table_path': 'C:\\Users\\ryanm\\Dropbox '
                        '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\pollination_guild_table.csv',
    'landcover_biophysical_table_path': 'C:\\Users\\ryanm\\Dropbox '
                                        '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\pollination_landcover_biophysical_table.csv',
    'landcover_raster_path': 'C:\\Users\\ryanm\\Dropbox '
                             '(Personal)\\Files\\apec_8601\\env8601_project\\seals\\projects\\BLZ_standard\\intermediate\\stitched_lulc_simplified_scenarios\\reprojected\\lulc_esa_seals7_ssp5_rcp85_luh2-message_bau_2045_clipped.tif',
    'n_workers': '-1',
    'results_suffix': '',
    'workspace_dir': 'C:\\Users\\ryanm\\Dropbox '
                     '(Personal)\\Files\\apec_8601\\env8601_project\\invest\\pollinate-ssp5-2045',
}

if __name__ == '__main__':
    natcap.invest.pollination.execute(args)

#################################################
# Module: Run Sediment Retention

## Run for SSP1 2030
args = {
    'biophysical_table_path': 'C:\\Users\\ryanm\\Dropbox '
                              '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\esa_and_modis_biophysical_table.csv',
    'dem_path': 'C:\\Users\\ryanm\\Dropbox '
                '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\dem.tif',
    'drainage_path': '',
    'erodibility_path': 'C:\\Users\\ryanm\\Dropbox '
                        '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\soil_erodibilty.tif',
    'erosivity_path': 'C:\\Users\\ryanm\\Dropbox '
                      '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\erosivity.tif',
    'ic_0_param': '.5',
    'k_param': '2',
    'l_max': '1.22',
    'lulc_path': 'C:\\Users\\ryanm\\Dropbox '
                 '(Personal)\\Files\\apec_8601\\env8601_project\\seals\\projects\\BLZ_standard\\intermediate\\stitched_lulc_simplified_scenarios\\lulc_esa_seals7_ssp1_rcp26_luh2-message_bau_2030_clipped.tif',
    'n_workers': '-1',
    'results_suffix': '',
    'sdr_max': '0.8',
    'threshold_flow_accumulation': '1000',
    'watersheds_path': 'C:\\Users\\ryanm\\Dropbox '
                       '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\watershed.shp',
    'workspace_dir': 'C:\\Users\\ryanm\\Dropbox '
                     '(Personal)\\Files\\apec_8601\\env8601_project\\invest\\sediment-ssp1-2030',
}

if __name__ == '__main__':
    natcap.invest.sdr.sdr.execute(args)

## Run for SSP1 2035
args = {
    'biophysical_table_path': 'C:\\Users\\ryanm\\Dropbox '
                              '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\esa_and_modis_biophysical_table.csv',
    'dem_path': 'C:\\Users\\ryanm\\Dropbox '
                '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\dem.tif',
    'drainage_path': '',
    'erodibility_path': 'C:\\Users\\ryanm\\Dropbox '
                        '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\soil_erodibilty.tif',
    'erosivity_path': 'C:\\Users\\ryanm\\Dropbox '
                      '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\erosivity.tif',
    'ic_0_param': '.5',
    'k_param': '2',
    'l_max': '1.22',
    'lulc_path': 'C:\\Users\\ryanm\\Dropbox '
                 '(Personal)\\Files\\apec_8601\\env8601_project\\seals\\projects\\BLZ_standard\\intermediate\\stitched_lulc_simplified_scenarios\\lulc_esa_seals7_ssp1_rcp26_luh2-message_bau_2035_clipped.tif',
    'n_workers': '-1',
    'results_suffix': '',
    'sdr_max': '0.8',
    'threshold_flow_accumulation': '1000',
    'watersheds_path': 'C:\\Users\\ryanm\\Dropbox '
                       '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\watershed.shp',
    'workspace_dir': 'C:\\Users\\ryanm\\Dropbox '
                     '(Personal)\\Files\\apec_8601\\env8601_project\\invest\\sediment-ssp1-2035',
}

if __name__ == '__main__':
    natcap.invest.sdr.sdr.execute(args)

## Run for SSP1 2045
args = {
    'biophysical_table_path': 'C:\\Users\\ryanm\\Dropbox '
                              '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\esa_and_modis_biophysical_table.csv',
    'dem_path': 'C:\\Users\\ryanm\\Dropbox '
                '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\dem.tif',
    'drainage_path': '',
    'erodibility_path': 'C:\\Users\\ryanm\\Dropbox '
                        '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\soil_erodibilty.tif',
    'erosivity_path': 'C:\\Users\\ryanm\\Dropbox '
                      '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\erosivity.tif',
    'ic_0_param': '.5',
    'k_param': '2',
    'l_max': '1.22',
    'lulc_path': 'C:\\Users\\ryanm\\Dropbox '
                 '(Personal)\\Files\\apec_8601\\env8601_project\\seals\\projects\\BLZ_standard\\intermediate\\stitched_lulc_simplified_scenarios\\lulc_esa_seals7_ssp1_rcp26_luh2-message_bau_2045_clipped.tif',
    'n_workers': '-1',
    'results_suffix': '',
    'sdr_max': '0.8',
    'threshold_flow_accumulation': '1000',
    'watersheds_path': 'C:\\Users\\ryanm\\Dropbox '
                       '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\watershed.shp',
    'workspace_dir': 'C:\\Users\\ryanm\\Dropbox '
                     '(Personal)\\Files\\apec_8601\\env8601_project\\invest\\sediment-ssp1-2045',
}

if __name__ == '__main__':
    natcap.invest.sdr.sdr.execute(args)

## Run for SSP5 2030
args = {
    'biophysical_table_path': 'C:\\Users\\ryanm\\Dropbox '
                              '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\esa_and_modis_biophysical_table.csv',
    'dem_path': 'C:\\Users\\ryanm\\Dropbox '
                '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\dem.tif',
    'drainage_path': '',
    'erodibility_path': 'C:\\Users\\ryanm\\Dropbox '
                        '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\soil_erodibilty.tif',
    'erosivity_path': 'C:\\Users\\ryanm\\Dropbox '
                      '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\erosivity.tif',
    'ic_0_param': '.5',
    'k_param': '2',
    'l_max': '1.22',
    'lulc_path': 'C:\\Users\\ryanm\\Dropbox '
                 '(Personal)\\Files\\apec_8601\\env8601_project\\seals\\projects\\BLZ_standard\\intermediate\\stitched_lulc_simplified_scenarios\\lulc_esa_seals7_ssp5_rcp85_luh2-message_bau_2030_clipped.tif',
    'n_workers': '-1',
    'results_suffix': '',
    'sdr_max': '0.8',
    'threshold_flow_accumulation': '1000',
    'watersheds_path': 'C:\\Users\\ryanm\\Dropbox '
                       '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\watershed.shp',
    'workspace_dir': 'C:\\Users\\ryanm\\Dropbox '
                     '(Personal)\\Files\\apec_8601\\env8601_project\\invest\\sediment-ssp5-2030',
}

if __name__ == '__main__':
    natcap.invest.sdr.sdr.execute(args)

## Run for SSP5 2035
args = {
    'biophysical_table_path': 'C:\\Users\\ryanm\\Dropbox '
                              '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\esa_and_modis_biophysical_table.csv',
    'dem_path': 'C:\\Users\\ryanm\\Dropbox '
                '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\dem.tif',
    'drainage_path': '',
    'erodibility_path': 'C:\\Users\\ryanm\\Dropbox '
                        '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\soil_erodibilty.tif',
    'erosivity_path': 'C:\\Users\\ryanm\\Dropbox '
                      '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\erosivity.tif',
    'ic_0_param': '.5',
    'k_param': '2',
    'l_max': '1.22',
    'lulc_path': 'C:\\Users\\ryanm\\Dropbox '
                 '(Personal)\\Files\\apec_8601\\env8601_project\\seals\\projects\\BLZ_standard\\intermediate\\stitched_lulc_simplified_scenarios\\lulc_esa_seals7_ssp5_rcp85_luh2-message_bau_2035_clipped.tif',
    'n_workers': '-1',
    'results_suffix': '',
    'sdr_max': '0.8',
    'threshold_flow_accumulation': '1000',
    'watersheds_path': 'C:\\Users\\ryanm\\Dropbox '
                       '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\watershed.shp',
    'workspace_dir': 'C:\\Users\\ryanm\\Dropbox '
                     '(Personal)\\Files\\apec_8601\\env8601_project\\invest\\sediment-ssp5-2035',
}

if __name__ == '__main__':
    natcap.invest.sdr.sdr.execute(args)

## Run for SSP5 2045
args = {
    'biophysical_table_path': 'C:\\Users\\ryanm\\Dropbox '
                              '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\esa_and_modis_biophysical_table.csv',
    'dem_path': 'C:\\Users\\ryanm\\Dropbox '
                '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\dem.tif',
    'drainage_path': '',
    'erodibility_path': 'C:\\Users\\ryanm\\Dropbox '
                        '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\soil_erodibilty.tif',
    'erosivity_path': 'C:\\Users\\ryanm\\Dropbox '
                      '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\erosivity.tif',
    'ic_0_param': '.5',
    'k_param': '2',
    'l_max': '1.22',
    'lulc_path': 'C:\\Users\\ryanm\\Dropbox '
                 '(Personal)\\Files\\apec_8601\\env8601_project\\seals\\projects\\BLZ_standard\\intermediate\\stitched_lulc_simplified_scenarios\\lulc_esa_seals7_ssp5_rcp85_luh2-message_bau_2045_clipped.tif',
    'n_workers': '-1',
    'results_suffix': '',
    'sdr_max': '0.8',
    'threshold_flow_accumulation': '1000',
    'watersheds_path': 'C:\\Users\\ryanm\\Dropbox '
                       '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\watershed.shp',
    'workspace_dir': 'C:\\Users\\ryanm\\Dropbox '
                     '(Personal)\\Files\\apec_8601\\env8601_project\\invest\\sediment-ssp5-2045',
}

if __name__ == '__main__':
    natcap.invest.sdr.sdr.execute(args)

#################################################
# Module: Run Nutrient Retention

## Run for SSP1 2030
args = {
    'biophysical_table_path': 'C:\\Users\\ryanm\\Dropbox '
                              '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\esa_and_modis_biophysical_table.csv',
    'calc_n': False,
    'calc_p': True,
    'dem_path': 'C:\\Users\\ryanm\\Dropbox '
                '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\dem.tif',
    'k_param': '2',
    'lulc_path': 'C:\\Users\\ryanm\\Dropbox '
                 '(Personal)\\Files\\apec_8601\\env8601_project\\seals\\projects\\BLZ_standard\\intermediate\\stitched_lulc_simplified_scenarios\\reprojected\\lulc_esa_seals7_ssp1_rcp26_luh2-message_bau_2030_clipped.tif',
    'n_workers': '-1',
    'results_suffix': '',
    'runoff_proxy_path': 'C:\\Users\\ryanm\\Dropbox '
                         '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\precipitation.tif',
    'subsurface_critical_length_n': '',
    'subsurface_eff_n': '',
    'threshold_flow_accumulation': '1000',
    'watersheds_path': 'C:\\Users\\ryanm\\Dropbox '
                       '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\watershed.shp',
    'workspace_dir': 'C:\\Users\\ryanm\\Dropbox '
                     '(Personal)\\Files\\apec_8601\\env8601_project\\invest\\nutrient-ssp1-2030',
}

if __name__ == '__main__':
    natcap.invest.ndr.ndr.execute(args)

## Run for SSP1 2035
args = {
    'biophysical_table_path': 'C:\\Users\\ryanm\\Dropbox '
                              '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\esa_and_modis_biophysical_table.csv',
    'calc_n': False,
    'calc_p': True,
    'dem_path': 'C:\\Users\\ryanm\\Dropbox '
                '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\dem.tif',
    'k_param': '2',
    'lulc_path': 'C:\\Users\\ryanm\\Dropbox '
                 '(Personal)\\Files\\apec_8601\\env8601_project\\seals\\projects\\BLZ_standard\\intermediate\\stitched_lulc_simplified_scenarios\\reprojected\\lulc_esa_seals7_ssp1_rcp26_luh2-message_bau_2035_clipped.tif',
    'n_workers': '-1',
    'results_suffix': '',
    'runoff_proxy_path': 'C:\\Users\\ryanm\\Dropbox '
                         '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\precipitation.tif',
    'subsurface_critical_length_n': '',
    'subsurface_eff_n': '',
    'threshold_flow_accumulation': '1000',
    'watersheds_path': 'C:\\Users\\ryanm\\Dropbox '
                       '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\watershed.shp',
    'workspace_dir': 'C:\\Users\\ryanm\\Dropbox '
                     '(Personal)\\Files\\apec_8601\\env8601_project\\invest\\nutrient-ssp1-2035',
}

if __name__ == '__main__':
    natcap.invest.ndr.ndr.execute(args)

## Run for SSP1 2045
args = {
    'biophysical_table_path': 'C:\\Users\\ryanm\\Dropbox '
                              '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\esa_and_modis_biophysical_table.csv',
    'calc_n': False,
    'calc_p': True,
    'dem_path': 'C:\\Users\\ryanm\\Dropbox '
                '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\dem.tif',
    'k_param': '2',
    'lulc_path': 'C:\\Users\\ryanm\\Dropbox '
                 '(Personal)\\Files\\apec_8601\\env8601_project\\seals\\projects\\BLZ_standard\\intermediate\\stitched_lulc_simplified_scenarios\\reprojected\\lulc_esa_seals7_ssp1_rcp26_luh2-message_bau_2045_clipped.tif',
    'n_workers': '-1',
    'results_suffix': '',
    'runoff_proxy_path': 'C:\\Users\\ryanm\\Dropbox '
                         '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\precipitation.tif',
    'subsurface_critical_length_n': '',
    'subsurface_eff_n': '',
    'threshold_flow_accumulation': '1000',
    'watersheds_path': 'C:\\Users\\ryanm\\Dropbox '
                       '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\watershed.shp',
    'workspace_dir': 'C:\\Users\\ryanm\\Dropbox '
                     '(Personal)\\Files\\apec_8601\\env8601_project\\invest\\nutrient-ssp1-2045',
}

if __name__ == '__main__':
    natcap.invest.ndr.ndr.execute(args)

## Run for SSP5 2030
args = {
    'biophysical_table_path': 'C:\\Users\\ryanm\\Dropbox '
                              '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\esa_and_modis_biophysical_table.csv',
    'calc_n': False,
    'calc_p': True,
    'dem_path': 'C:\\Users\\ryanm\\Dropbox '
                '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\dem.tif',
    'k_param': '2',
    'lulc_path': 'C:\\Users\\ryanm\\Dropbox '
                 '(Personal)\\Files\\apec_8601\\env8601_project\\seals\\projects\\BLZ_standard\\intermediate\\stitched_lulc_simplified_scenarios\\reprojected\\lulc_esa_seals7_ssp5_rcp85_luh2-message_bau_2030_clipped.tif',
    'n_workers': '-1',
    'results_suffix': '',
    'runoff_proxy_path': 'C:\\Users\\ryanm\\Dropbox '
                         '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\precipitation.tif',
    'subsurface_critical_length_n': '',
    'subsurface_eff_n': '',
    'threshold_flow_accumulation': '1000',
    'watersheds_path': 'C:\\Users\\ryanm\\Dropbox '
                       '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\watershed.shp',
    'workspace_dir': 'C:\\Users\\ryanm\\Dropbox '
                     '(Personal)\\Files\\apec_8601\\env8601_project\\invest\\nutrient-ssp5-2030',
}

if __name__ == '__main__':
    natcap.invest.ndr.ndr.execute(args)

## Run for SSP5 2035
args = {
    'biophysical_table_path': 'C:\\Users\\ryanm\\Dropbox '
                              '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\esa_and_modis_biophysical_table.csv',
    'calc_n': False,
    'calc_p': True,
    'dem_path': 'C:\\Users\\ryanm\\Dropbox '
                '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\dem.tif',
    'k_param': '2',
    'lulc_path': 'C:\\Users\\ryanm\\Dropbox '
                 '(Personal)\\Files\\apec_8601\\env8601_project\\seals\\projects\\BLZ_standard\\intermediate\\stitched_lulc_simplified_scenarios\\reprojected\\lulc_esa_seals7_ssp5_rcp85_luh2-message_bau_2035_clipped.tif',
    'n_workers': '-1',
    'results_suffix': '',
    'runoff_proxy_path': 'C:\\Users\\ryanm\\Dropbox '
                         '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\precipitation.tif',
    'subsurface_critical_length_n': '',
    'subsurface_eff_n': '',
    'threshold_flow_accumulation': '1000',
    'watersheds_path': 'C:\\Users\\ryanm\\Dropbox '
                       '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\watershed.shp',
    'workspace_dir': 'C:\\Users\\ryanm\\Dropbox '
                     '(Personal)\\Files\\apec_8601\\env8601_project\\invest\\nutrient-ssp5-2035',
}

if __name__ == '__main__':
    natcap.invest.ndr.ndr.execute(args)

## Run for SSP5 2045
args = {
    'biophysical_table_path': 'C:\\Users\\ryanm\\Dropbox '
                              '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\esa_and_modis_biophysical_table.csv',
    'calc_n': False,
    'calc_p': True,
    'dem_path': 'C:\\Users\\ryanm\\Dropbox '
                '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\dem.tif',
    'k_param': '2',
    'lulc_path': 'C:\\Users\\ryanm\\Dropbox '
                 '(Personal)\\Files\\apec_8601\\env8601_project\\seals\\projects\\BLZ_standard\\intermediate\\stitched_lulc_simplified_scenarios\\reprojected\\lulc_esa_seals7_ssp5_rcp85_luh2-message_bau_2045_clipped.tif',
    'n_workers': '-1',
    'results_suffix': '',
    'runoff_proxy_path': 'C:\\Users\\ryanm\\Dropbox '
                         '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\precipitation.tif',
    'subsurface_critical_length_n': '',
    'subsurface_eff_n': '',
    'threshold_flow_accumulation': '1000',
    'watersheds_path': 'C:\\Users\\ryanm\\Dropbox '
                       '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\watershed.shp',
    'workspace_dir': 'C:\\Users\\ryanm\\Dropbox '
                     '(Personal)\\Files\\apec_8601\\env8601_project\\invest\\nutrient-ssp5-2045',
}

if __name__ == '__main__':
    natcap.invest.ndr.ndr.execute(args)

#################################################
# Module: Run Water Yield (Supply)

## Run for SSP1 2030
args = {
    'biophysical_table_path': 'C:\\Users\\ryanm\\Dropbox '
                              '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\esa_and_modis_biophysical_table.csv',
    'demand_table_path': '',
    'depth_to_root_rest_layer_path': 'C:\\Users\\ryanm\\Dropbox '
                                     '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\root-layer-depth.tif',
    'eto_path': 'C:\\Users\\ryanm\\Dropbox '
                '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\evapotranspiration.tif',
    'lulc_path': 'C:\\Users\\ryanm\\Dropbox '
                 '(Personal)\\Files\\apec_8601\\env8601_project\\seals\\projects\\BLZ_standard\\intermediate\\stitched_lulc_simplified_scenarios\\reprojected\\lulc_esa_seals7_ssp1_rcp26_luh2-message_bau_2030_clipped.tif',
    'n_workers': '-1',
    'pawc_path': 'C:\\Users\\ryanm\\Dropbox '
                 '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\plant-water-content.tif',
    'precipitation_path': 'C:\\Users\\ryanm\\Dropbox '
                          '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\precipitation.tif',
    'results_suffix': '',
    'seasonality_constant': '20',
    'sub_watersheds_path': '',
    'valuation_table_path': '',
    'watersheds_path': 'C:\\Users\\ryanm\\Dropbox '
                       '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\watershed2.shp',
    'workspace_dir': 'C:\\Users\\ryanm\\Dropbox '
                     '(Personal)\\Files\\apec_8601\\env8601_project\\invest\\water-ssp1-2030',
}

if __name__ == '__main__':
    natcap.invest.annual_water_yield.execute(args)

## Run for SSP1 2035
args = {
    'biophysical_table_path': 'C:\\Users\\ryanm\\Dropbox '
                              '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\esa_and_modis_biophysical_table.csv',
    'demand_table_path': '',
    'depth_to_root_rest_layer_path': 'C:\\Users\\ryanm\\Dropbox '
                                     '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\root-layer-depth.tif',
    'eto_path': 'C:\\Users\\ryanm\\Dropbox '
                '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\evapotranspiration.tif',
    'lulc_path': 'C:\\Users\\ryanm\\Dropbox '
                 '(Personal)\\Files\\apec_8601\\env8601_project\\seals\\projects\\BLZ_standard\\intermediate\\stitched_lulc_simplified_scenarios\\reprojected\\lulc_esa_seals7_ssp1_rcp26_luh2-message_bau_2035_clipped.tif',
    'n_workers': '-1',
    'pawc_path': 'C:\\Users\\ryanm\\Dropbox '
                 '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\plant-water-content.tif',
    'precipitation_path': 'C:\\Users\\ryanm\\Dropbox '
                          '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\precipitation.tif',
    'results_suffix': '',
    'seasonality_constant': '20',
    'sub_watersheds_path': '',
    'valuation_table_path': '',
    'watersheds_path': 'C:\\Users\\ryanm\\Dropbox '
                       '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\watershed2.shp',
    'workspace_dir': 'C:\\Users\\ryanm\\Dropbox '
                     '(Personal)\\Files\\apec_8601\\env8601_project\\invest\\water-ssp1-2035',
}

if __name__ == '__main__':
    natcap.invest.annual_water_yield.execute(args)

## Run for SSP1 2045
args = {
    'biophysical_table_path': 'C:\\Users\\ryanm\\Dropbox '
                              '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\esa_and_modis_biophysical_table.csv',
    'demand_table_path': '',
    'depth_to_root_rest_layer_path': 'C:\\Users\\ryanm\\Dropbox '
                                     '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\root-layer-depth.tif',
    'eto_path': 'C:\\Users\\ryanm\\Dropbox '
                '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\evapotranspiration.tif',
    'lulc_path': 'C:\\Users\\ryanm\\Dropbox '
                 '(Personal)\\Files\\apec_8601\\env8601_project\\seals\\projects\\BLZ_standard\\intermediate\\stitched_lulc_simplified_scenarios\\reprojected\\lulc_esa_seals7_ssp1_rcp26_luh2-message_bau_2045_clipped.tif',
    'n_workers': '-1',
    'pawc_path': 'C:\\Users\\ryanm\\Dropbox '
                 '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\plant-water-content.tif',
    'precipitation_path': 'C:\\Users\\ryanm\\Dropbox '
                          '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\precipitation.tif',
    'results_suffix': '',
    'seasonality_constant': '20',
    'sub_watersheds_path': '',
    'valuation_table_path': '',
    'watersheds_path': 'C:\\Users\\ryanm\\Dropbox '
                       '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\watershed2.shp',
    'workspace_dir': 'C:\\Users\\ryanm\\Dropbox '
                     '(Personal)\\Files\\apec_8601\\env8601_project\\invest\\water-ssp1-2045',
}

if __name__ == '__main__':
    natcap.invest.annual_water_yield.execute(args)

## Run for SSP5 2030
args = {
    'biophysical_table_path': 'C:\\Users\\ryanm\\Dropbox '
                              '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\esa_and_modis_biophysical_table.csv',
    'demand_table_path': '',
    'depth_to_root_rest_layer_path': 'C:\\Users\\ryanm\\Dropbox '
                                     '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\root-layer-depth.tif',
    'eto_path': 'C:\\Users\\ryanm\\Dropbox '
                '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\evapotranspiration.tif',
    'lulc_path': 'C:\\Users\\ryanm\\Dropbox '
                 '(Personal)\\Files\\apec_8601\\env8601_project\\seals\\projects\\BLZ_standard\\intermediate\\stitched_lulc_simplified_scenarios\\reprojected\\lulc_esa_seals7_ssp5_rcp85_luh2-message_bau_2030_clipped.tif',
    'n_workers': '-1',
    'pawc_path': 'C:\\Users\\ryanm\\Dropbox '
                 '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\plant-water-content.tif',
    'precipitation_path': 'C:\\Users\\ryanm\\Dropbox '
                          '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\precipitation.tif',
    'results_suffix': '',
    'seasonality_constant': '20',
    'sub_watersheds_path': '',
    'valuation_table_path': '',
    'watersheds_path': 'C:\\Users\\ryanm\\Dropbox '
                       '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\watershed2.shp',
    'workspace_dir': 'C:\\Users\\ryanm\\Dropbox '
                     '(Personal)\\Files\\apec_8601\\env8601_project\\invest\\water-ssp5-2030',
}

if __name__ == '__main__':
    natcap.invest.annual_water_yield.execute(args)

## Run for SSP5 2035
args = {
    'biophysical_table_path': 'C:\\Users\\ryanm\\Dropbox '
                              '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\esa_and_modis_biophysical_table.csv',
    'demand_table_path': '',
    'depth_to_root_rest_layer_path': 'C:\\Users\\ryanm\\Dropbox '
                                     '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\root-layer-depth.tif',
    'eto_path': 'C:\\Users\\ryanm\\Dropbox '
                '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\evapotranspiration.tif',
    'lulc_path': 'C:\\Users\\ryanm\\Dropbox '
                 '(Personal)\\Files\\apec_8601\\env8601_project\\seals\\projects\\BLZ_standard\\intermediate\\stitched_lulc_simplified_scenarios\\reprojected\\lulc_esa_seals7_ssp5_rcp85_luh2-message_bau_2035_clipped.tif',
    'n_workers': '-1',
    'pawc_path': 'C:\\Users\\ryanm\\Dropbox '
                 '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\plant-water-content.tif',
    'precipitation_path': 'C:\\Users\\ryanm\\Dropbox '
                          '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\precipitation.tif',
    'results_suffix': '',
    'seasonality_constant': '20',
    'sub_watersheds_path': '',
    'valuation_table_path': '',
    'watersheds_path': 'C:\\Users\\ryanm\\Dropbox '
                       '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\watershed2.shp',
    'workspace_dir': 'C:\\Users\\ryanm\\Dropbox '
                     '(Personal)\\Files\\apec_8601\\env8601_project\\invest\\water-ssp5-2035',
}

if __name__ == '__main__':
    natcap.invest.annual_water_yield.execute(args)

## Run for SSP5 2045
args = {
    'biophysical_table_path': 'C:\\Users\\ryanm\\Dropbox '
                              '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\esa_and_modis_biophysical_table.csv',
    'demand_table_path': '',
    'depth_to_root_rest_layer_path': 'C:\\Users\\ryanm\\Dropbox '
                                     '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\root-layer-depth.tif',
    'eto_path': 'C:\\Users\\ryanm\\Dropbox '
                '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\evapotranspiration.tif',
    'lulc_path': 'C:\\Users\\ryanm\\Dropbox '
                 '(Personal)\\Files\\apec_8601\\env8601_project\\seals\\projects\\BLZ_standard\\intermediate\\stitched_lulc_simplified_scenarios\\reprojected\\lulc_esa_seals7_ssp5_rcp85_luh2-message_bau_2045_clipped.tif',
    'n_workers': '-1',
    'pawc_path': 'C:\\Users\\ryanm\\Dropbox '
                 '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\plant-water-content.tif',
    'precipitation_path': 'C:\\Users\\ryanm\\Dropbox '
                          '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\precipitation.tif',
    'results_suffix': '',
    'seasonality_constant': '20',
    'sub_watersheds_path': '',
    'valuation_table_path': '',
    'watersheds_path': 'C:\\Users\\ryanm\\Dropbox '
                       '(Personal)\\Files\\apec_8601\\env8601_project\\base_data\\invest\\watershed2.shp',
    'workspace_dir': 'C:\\Users\\ryanm\\Dropbox '
                     '(Personal)\\Files\\apec_8601\\env8601_project\\invest\\water-ssp5-2045',
}

if __name__ == '__main__':
    natcap.invest.annual_water_yield.execute(args)
