# generate_database_master
This code was build for a specific purpuse but could be tweeked for a similar use.

The program opens two xlsx files and matches records in the one file to another file based on a common key.
It then creates a new xlxs file based on data in both of the files.

The program is used to create a file that can be imported into a company database using data from both files.
The company database expects records in a specific format.

with this program cells can be copied from one work book to the other or/and manipulated.

The second workbook is in the format expected by the company database.
The program will create new records in the second workbook if there there is not already a matching record based on a single column/cell specified.

If there is a matching record that record will be altered in the second workbook using
various data manipulation functions, concat, conditional checks and so on.



