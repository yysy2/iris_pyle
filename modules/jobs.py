''' Module to give back the 
units of variables
information about the timeslice experiments xjmx e,f,g,h 
variable names that are in the individual nc files generated by generate_netcdf.nc
'''
#################################################################### 
#################################################################### 

# JOBID EMISSIONS SENSITIVITY ANALYSIS
def job(jobid):
#    jobid=word
    if jobid=='xjmxe':
        year='1985'	# year of methane emissions
        year2='1985'	# year of other emissions
    elif jobid=='xjmxf' or jobid=='xjmxi':
        year='1995'	# year of methane emissions
        year2='1995'	# year of other emissions
    elif jobid=='xjmxg':
        year='1985'	# year of methane emissions
        year2='1995'	# year of other emissions
    elif jobid=='xjmxh':
        year='1995'	# year of methane emissions
        year2='1985'	# year of other emissions
    else:
        year=''
        year2=''
    return year, year2

# JOBID EMISSIONS SENSITIVITY ANALYSIS
def ems(jobid):
    if   jobid == 'xjmxe':
	ems    =  'Emissions: All 1985'
    elif jobid == 'xjmxf' or jobid=='xjmxi':
	ems    =  'Emissions: All 1995'
    elif jobid == 'xjmxg':
	ems    =  'Emissions: CH4(85), other(95)'
    elif jobid=='xjmxh':
	ems    =  'Emissions: CH4(95), other(85)'
    elif jobid=='xjmxj' or jobid=='xjmxm':
	ems    =  'Emissions: CO(95), other(85)'
    elif jobid=='xjmxk' or jobid=='xjmxn':
	ems    =  'Emissions: NOx(95), other(85)'
    elif jobid=='xjmxl':
	ems    =  'Emissions: Isoprene(95), other(85)'
    else:
	ems    =  ''
    return ems

# VARIABLES IN STASH FILES
def stash_var(stash):
#    stash=word
    if stash=='_ch4+oh_ch4ems':
        var=['ch4_oh_rxn_flux',
             'ch4_ems']
    elif stash=='_o3_ch4_n2o_ageair':
        var=['mass_fraction_of_ozone_in_air',
             'mass_fraction_of_methane_in_air',
             'mass_fraction_of_nitrous_oxide_in_air',
             'age_of_air']
    elif stash=='_t_p_tropopause':
        var=['air_temperature',
             'air_pressure',
             'tropopause_height']
    elif stash=='_oh':
        var=['mass_fraction_of_hydroxyl_radical_in_air']
    else:
        var=[]
    return var

# SPINUP PERIOD
def spinup(jobid):
#    jobid=word
    if jobid=='xjmxe':   # datetime.datetime(2010, 1, 15, 23, 59, 59)
        spinup=[108,-1]	
    elif jobid=='xjmxi': # datetime.datetime(2013, 1, 15, 23, 59, 59)
        spinup=[144,-1]
    elif jobid=='xjmxg': # datetime.datetime(2013, 1, 15, 23, 59, 59)
        spinup=[144,-1]
    elif jobid=='xjmxh':
        spinup=[108,-1]
    else:
        spinup=[108,-1]
    return spinup


# label
def label(jobid):
#    jobid=word
    if jobid=='xjmxe':   # datetime.datetime(2010, 1, 15, 23, 59, 59)
        label='E1'	
    elif jobid=='xjmxi': # datetime.datetime(2013, 1, 15, 23, 59, 59)
        label='E2'
    elif jobid=='xjmxg': # datetime.datetime(2013, 1, 15, 23, 59, 59)
        label='E2a'
    elif jobid=='xjmxh':
        label='E1a'
    else:
        label=''
    return label

