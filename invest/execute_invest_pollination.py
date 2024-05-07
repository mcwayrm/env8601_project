# coding=UTF-8
# -----------------------------------------------
# Generated by InVEST 3.13.0 on Tue May  7 13:06:31 2024
# Model: Crop Pollination

import logging
import sys

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