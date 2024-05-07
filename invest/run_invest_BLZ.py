import logging
import sys

import natcap.invest.carbon
import natcap.invest.pollination
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

## Run for SSP1 2035

## Run for SSP1 2045

## Run for SSP5 2030

## Run for SSP5 2035

## Run for SSP5 2045

#################################################
# Module: Run Nutrient Retention

## Run for SSP1 2030

## Run for SSP1 2035

## Run for SSP1 2045

## Run for SSP5 2030

## Run for SSP5 2035

## Run for SSP5 2045


#################################################
# Module: Run Water Yield (Supply)

## Run for SSP1 2030

## Run for SSP1 2035

## Run for SSP1 2045

## Run for SSP5 2030

## Run for SSP5 2035

## Run for SSP5 2045
