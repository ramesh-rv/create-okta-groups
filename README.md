# Create Okta Groups

Create groups in Okta through a script

* The script will read the list of group names in the csv and create groups in the Okta tenant specified
* The script will use [Okta Python SDK](https://github.com/okta/okta-sdk-python) under the hood.
* The script will generate a log file with the output.



*****


How to run
--------------


1. Install the Okta python SDK using the below command

	`pip install okta`



2. Create a .env file and provide the values for OKTA_HOST and API_KEY as shown below

```
OKTA_HOST="https://oie-12345.oktapreview.com"
API_KEY="<enter-api-key-here"


```


3. Create an input file with the group names. The column header should be provided as ``GROUP_NAME``and ``GROUP_DESCRIPTION``



4. A sample input file is shown below
```
cat groups.csv 
GROUP_NAME,GROUP_DESCRIPTION
Group1,Description for Group1
Group2,Description for Group2
"OU=Users,DC=Example,DC=com",AD Group
"A,B,C",No Description
Group 5,Description for Group 5

```

5. The files should be available in the directory as shown below

```
$ tree .
.
├── create_groups.py
└── groups.csv

0 directories, 2 files

```

6. Execute the script using the command

`python create_groups.py`

7. When the script has completed execution, validate the `group_create.log` for the result

----



# create-okta-groups
