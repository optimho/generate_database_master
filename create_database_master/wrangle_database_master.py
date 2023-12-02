"""
Compares the master instrument dataframe and creates a database master dataframe
This is used to create an Excel spreadsheet to import into an access database
for contact energys' device database.

"""

import numpy as np
import pandas as pd

def wrangle_database_list(master_list: pd, database_list: pd, version: str):
    #Takes the new instrument lists, checks the exsisting database lists
    #compiles a new lists with data from both lists and presents the data in a format that
    #can easily be used to import into the new instrument database

    master_instrument_list = master_list
    master_database_list = database_list


    for instrument_list_index in range(master_instrument_list.shape[0]):
        device_is_listed=False
        for database_list_index in range(master_database_list.shape[0]):

            #Check the kks numbers in both lists -- check what indexes should be set 0 is default  #####
            ####  TODO _ NOTE {This is an essential part - compares a unique cell in both workbooks }##################
            ####  TODO _ NOTE {The number at the end indictes the column                            }##################
            ####  TODO _ NOTE {of the cells in the Dataframe to compare                             }##################

            kks_number_instrument_list = master_instrument_list.iloc[instrument_list_index,10]
            kks_number_database_list = master_database_list.iloc[database_list_index,0]

            #If you find an instrument that is listed in both lists update the database lists
            #with as much data from the new instrument lists
            if kks_number_instrument_list==kks_number_database_list:
                device_is_listed = True

                # #make a series of the row of data being checked from both dataframes
                # temp_database: np = master_database_list.loc[database_list_index+1]
                # temp_master: np = master_instrument_list.loc[instrument_list_index+1]
                #
                # ###### WRANGLE DATA HERE ###########  TODO      #####################################################
                # temp_database['Station'] = temp_master['PLANT']
                # temp_database['Station'] = temp_master['PLANT']
                # temp_database['Station'] = temp_master['PLANT']
                # temp_database['Station'] = temp_master['PLANT']
                # temp_database['Station'] = temp_master['PLANT']
                # temp_database['Station'] = temp_master['PLANT']
                # temp_database['Station'] = temp_master['PLANT']
                # temp_database['Station'] = temp_master['PLANT']
                # temp_database['Station'] = temp_master['PLANT']
                # temp_database['Station'] = temp_master['PLANT']
                #
                # ######################################################################################################
                # # TODO update the updated record
                # #master_database_list = master_database_list._append(temp_database, ignore_index=True)



            #Chpytesteck if the device was not on the lists of items in the database, then add it
            if (device_is_listed==False) and (master_database_list.shape[0] == database_list_index+1) :

                #copy the last record in the master_database dataframe and append the record to the master database /
                # dataframe
                temp_database: np = master_database_list.loc[master_database_list.shape[0]-1]
                temp_master: np = master_instrument_list.loc[instrument_list_index]

                ###### TODO WRANGLE DATA HERE ##########################################################################
                # a = master_database_list.iat[database_list_index, 0]
                # master_database_list.iat[database_list_index,0] = master_instrument_list.iat[instrument_list_index,1]
                # b = master_database_list.iat[database_list_index, 0]

                master_database_list.iat[database_list_index, 0] = master_instrument_list.iat[instrument_list_index, 1]


                ########################################################################################################
                # append the updated record
                master_database_list = master_database_list._append(temp_database, ignore_index=True)


                #print(f'ADD This to Database List --{instrument_list_index} Updates')
                device_is_listed = True
                ##TODO add master lists item to the the database lists




