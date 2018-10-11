## Search
To search for records within the HIEv, you can use the hievpy _search_ function:

```sh
import hievpy as hp
hp.search(api_token, base_url, search_params)
```

where
1. api_token: HIEv API token string
2. base_url: the base url string of the HIEv instance
3. search_params: Object containing metadata key-value pairs for searching 

The following search parameters may be used:
(see this [link](https://github.com/IntersectAustralia/dc21-doc/blob/master/Search_API.md) for further information )

- from_date - This is "Date->From Date" in search box of WEB UI: "from_date"=>"2013-01-01"
- to_date - This is "Date->To Date" in search box of WEB UI: "to_date"=>"2013-01-02"
- filename - This is "Filename" in search box of WEB UI: "filename"=>"test"
- description - This is "Description" in search box of WEB UI: "description"=>"test"
- file_id - This is "File ID" in search box of WEB UI: "file_id"=>"test"
- id (here replaced as record_id)- This is "ID" in search box of WEB UI: "id"=>"26"
- stati - This is "Type" in search box of WEB UI: "stati"=>["RAW", "CLEANSED"]
- automation_stati - This is "Automation Status" in search box of WEB UI, "automation_stati"=>["COMPLETE",
  "WORKING"]
- access_rights_types - This is the "Access Rights Type" in the search box of the WEB UI: "access_rights_types"=>
  ["Open", "Conditional", "Restricted"]
- file_formats - This is "File Formats" in search box of WEB UI, "file_formats"=>["TOA5", "Unknown", "audio/mpeg"]
- published - This is "Type->PACKAGE->Published" in search box of WEB UI: "stati"=>["PACKAGE"], "published"=>
  ["true"]
- unpublished - This is "Type->PACKAGE->Published" in search box of WEB UI: "stati"=>["PACKAGE"], "unpublished"=>
  ["true"].
- published_date - This is "Type->PACKAGE->Published Date" in search box of WEB UI: "stati"=>["PACKAGE"],
  "published_date"=>"2013-01-01"
- tags - This is "Tags" in search box of WEB UI: "tags"=>["4", "5"]
- labels - This is "Labels" in search box of WEB UI, "labels"=>["label_name_1", "label_name_2"]
- grant_numbers - This is the "Grant Numbers" in search box of WEB UI, "grant_numbers"=>["grant_number_1",
  "grant_number_2"]
- related_websites - This is the "Related Websites" in the search box of WEB UI, "related_websites"=>
  ["http://www.intersect.org.au"]
- facilities - This is "Facility" in search box of WEB UI, ask system administrator to get facility ids :
  "facilities"=>["27"]
- experiments - This is "Facility" in search box of WEB UI, when one facility is clicked, experiments of this
  facility are selectable, ask system administrator to get experiment ids: "experiments"=>["58", "54"]
- variables - This is "Columns" in search box of WEB UI, when one group is clicked, columns of this group are
  selectable: "variables"=>["SoilTempProbe_Avg(1)", "SoilTempProbe_Avg(3)"]
- uploader_id - This is "Added By" in search box of WEB UI, ask system administrator to get uploader ids:
  "uploader_id"=>"83"
- upload_from_date - This is "Date Added->From Date" in search box of WEB UI, "upload_from_date"=>"2013-01-01"
- upload_to_date - This is "Date Added->To Date" in search box of WEB UI, "upload_to_date"=>"2013-01-02"


**It is highly recommended that you supply at least one search query to your search to limit returning the full 
database in one call**


## Example

> You can download a Jupyter notebook version of this example from the __/examples__ folder on the github 
project page.

As an example, to search for all records matching the filename 'DRL_AUTO_450LO_SOIL_R' between 2nd January 2017 and 
1st Januaruy 2018, and then print the resulting filenames to screen:


##### Import hievpy library

```python
import hievpy as hp
```

##### Import the credentials file (or use your preset environment variable) and set the API token

```python
import credentials as c
api_token = c.hiev_api_key
```

##### Set the base URL of the HIEv instance being called against

```python
base_url = 'https://hiev.westernsydney.edu.au/'
```

##### Set the search parameters

```python
search_params = {"filename": "DRL_AUTO_450LO_SOIL_R",
                 "from_date": "2017-01-02",
                 "to_date": "2018-01-01"}
```

##### Run the hievpy search function using the search parameters

```python
records = hp.search(api_token, base_url, search_params)
```

##### Check the results

```python
for record in records: print(record['filename'])
```

    DRL_AUTO_450LO_SOIL_R_20171130.dat
    DRL_AUTO_450LO_SOIL_R_20170131.dat
    DRL_AUTO_450LO_SOIL_R_20170731.dat
    DRL_AUTO_450LO_SOIL_R_20170430.dat
    DRL_AUTO_450LO_SOIL_R_20171031.dat
    DRL_AUTO_450LO_SOIL_R_20170331.dat
    DRL_AUTO_450LO_SOIL_R_20170228.dat
    DRL_AUTO_450LO_SOIL_R_20170630.dat
    DRL_AUTO_450LO_SOIL_R_20180131.dat
    DRL_AUTO_450LO_SOIL_R_20170531.dat
    DRL_AUTO_450LO_SOIL_R_20170930.dat
    DRL_AUTO_450LO_SOIL_R_20170831.dat
    DRL_AUTO_450LO_SOIL_R_20171231.dat
`

