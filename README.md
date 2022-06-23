# Create Okta Groups

Create groups in Okta through a script

* The script will read the list of group names in the csv and create groups in the Okta tenant specified
* The script will use Okta Python SDK under the hood.
* The script will generate a log file with the output.



*****


Implementation
--------------



1. Install the Okta python SDK using the below command

	`pip install okta`



2. Open the script `create_groups.py` in a text editor or IDE.
3. Update the config with the Okta org URL and the API token

	'orgUrl' : 'https://dev-12345.okta.com'
    
	'token' : 'xxxxxxxxxxxxxxxxxxx'

    ```
	    config = {'orgUrl': 'okta-org-name-here',
	              'token': 'api-token-here',
	              'raiseException': True}
    ```

4. Create an input file with the group names. The column header should be provided as ``GROUP_NAME``




5. A sample input file is shown below
```
cat groups.csv 
GROUP_NAME
Group1,
Group2,
"OU=Users,DC=Example,DC=com"
"A,B,C"

```

6. The files should be available in the directory as shown below

```
$ tree .
.
├── create_groups.py
└── groups.csv

0 directories, 2 files

```

7. Execute the script using the command

`python create_groups.py`

8. When the script has completed execution, validate the group_create.log for the result



