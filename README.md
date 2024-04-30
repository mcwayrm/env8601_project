# Earth Economy Modeling for APEC ENV 8601 -- Natural Resources
### Country: Belize

# Description: 
This project is an application of the GTAP-InVEST earth economy modeling approach to estimate global-local-global estimates of the influence of ecosystem services on a computable general equilibrium of a national economy. Below are the main steps performed in this analysis as well as a discussion of the results. 


## Step 1

### Use SEALS to generate a LULC map for 2030, 2035, and 2040. Estimate this for SSP2 and SSP5.

To change the input definitions for the SEALS standard run, I need to modify the `scenario_definitions.csv` file called on line 62 of the `run_test_standard.py`: `p.scenario_definitions_path = os.path.join(p.input_dir, 'scenario_defininitions.csv')`. Under `aoi`, I changed the country alpha-3 code to BLZ for Belize. The scenerios are already set to baseline and SSP2 under `exogenous_label`. Here I duplicate a line from SSP2 to create SSP1 and SSP5 while removing SSP2. To modify the years that SEALS generates the LULC maps, I insert `2030 2035 2040` under `years` for the SSP1 and SSP5 scenerios while keeping the baseline year at 2017 (this is the baseline year of data that SEALS is pulling from -- so don't change). Note that the labels in the scenerio definitions are important. So be sure to relabel them consistently as shown in the `scenario_definitions.csv` file in this repo. 

Finally, to run the new SSP scenerios you will need to download the correct `coarse_projections_input_path` from [Land Use Harmonization data](https://luh.umd.edu/data.shtml). You will need to approriately save this in the `base_data` using a consistent directory structure from the baseline input data. 



For `hazelbean` to run parallel processing, it creates separate project folders given the name given in line 24. If you don't change the name, `run_test_standard.py` will throw an error. So, instead create a new file for the Belize run called `run_BLZ_standard.py` and change `project_name = 'BLZ_standard'`

Once completed I now I have a new set of scenerio definitions which I an use in the [run_BLZ_standard.py](./seals/run_BLZ_standard.py). You can examine this file as [scenario_defininitions1a.csv](./seals/projects/BLZ_standard/input/scenario_defininitions1a.csv). To examine the results, you can now look in the `seals` folder under `projects` and you should find the LULC maps (and other output) in a folder called `BLZ_standard` alongside the initial folder for the initial test run called `test_standard`.

You will want to put the `scenario_definitions.csv` file into a new project folder labeled `BLZ_standard\input` before running the `run_BLZ_standard.py`. If you do not, then it will populate the standard test run with Rwanda instead of the new country (Belize). When you go to run this script, run it within the Debug function with VSCode using the internalConsole. Make sure to working within the `earth_economy_devstack (Workspace)` and to run with your `teem_devstack` python kernel so you have all the correct modules. 


### Plot these seven LULC maps and scenerios.



#### LULC 2017 with Baseline (SSP2)

![](./seals/projects/BLZ_standard/intermediate/visualization1a/lulc_pngs/lulc_esa_seals7_luh2-message_2017.png)

#### LULC 2030 with SSP1

![](./seals/projects/BLZ_standard/intermediate/visualization1a/lulc_pngs/lulc_esa_seals7_ssp1_rcp26_luh2-message_bau_2030.png)

#### LULC 2030 with SSP5

![](./seals/projects/BLZ_standard/intermediate/visualization1a/lulc_pngs/lulc_esa_seals7_ssp5_rcp85_luh2-message_bau_2030.png)

#### LULC 2035 with SSP1

![](./seals/projects/BLZ_standard/intermediate/visualization1a/lulc_pngs/lulc_esa_seals7_ssp1_rcp26_luh2-message_bau_2035.png)

#### LULC 2035 with SSP5

![](./seals/projects/BLZ_standard/intermediate/visualization1a/lulc_pngs/lulc_esa_seals7_ssp5_rcp85_luh2-message_bau_2035.png)

#### LULC 2045 with SSP1

![](./seals/projects/BLZ_standard/intermediate/visualization1a/lulc_pngs/lulc_esa_seals7_ssp1_rcp26_luh2-message_bau_2045.png)

#### LULC 2045 with SSP5

![](./seals/projects/BLZ_standard/intermediate/visualization1a/lulc_pngs/lulc_esa_seals7_ssp5_rcp85_luh2-message_bau_2045.png)

### Add a new policy layer preventing or encouraging a type of land-use change. 

The policy I apply is ... To implement this, I change ...

Code for this can be found here.

Here are the results from that...

#### LULC 2030 with SSP1

#### LULC 2030 with SSP5

#### LULC 2035 with SSP1

#### LULC 2035 with SSP5

#### LULC 2040 with SSP1

#### LULC 2040 with SSP5

### Provide a narrative of how the different scenerios changed when this land use class was expanded or contracted. 

Here is a description visually comparing the two sets of graphs. 

## Step 2

### Using the first set of LULC maps from SEALS, assess ecosystem service provision for carbon storage, water yield, pollination, sediment retention, and nutrient retention using the InVEST ecosystem service modeling. 

I completed this run. Any problems that I needed to resolve for a successful run. The code for this can be found here.

### Show the plots for these ecosystem services

plot the images here...
![]()

#### Ecosystem Service: Carbon Storage

#### Ecosystem Service: Water Yield (Supply)

#### Ecosystem Service: Pollination

#### Ecosystem Service: Sediment Retention

#### Ecosystem Service: Nutrient Retention


### Describe how the various scenerios differ with respect to the different ecosystem services. 

Here I discuss what visually increases and decreases. Are there hotstops in the country?

### Write an executive summary for what the policy maker interested in "green economic development" should know. 

Here is my executive summary. Avoid SSP5 as a counterfactual. value in ...

## Step 3 

### Post and organize code from this semester. Add a README.md 

This README file so far has described the final project analysis and the results. In addition, for the APEC 8601 natural resource course, we produced some empirical results using python code. I elaborate on this below. 

- In [problem set 02](./problem_sets/problem_set_2_mcway.pdf) I work with the DICE model for optimal production considering the damages from global warming. Additionally, I work with the MAGICC model to show the projected global temperature under different RCP scenerios through 2100.
- In [problem set 04](./problem_sets/problem_set_4.pdf) I run the InVEST ecosystem services model to estimate the ecosystem service benefits from crop pollination. 

### Make the repository public. Submit Repo to Canvas.

This repository has been made public and can be found [here](https://github.com/mcwayrm/env8601_project).
... completed ... eventually...


