## Search
To search for records within HIEv database, you can use the hievpy _search_ function:

```sh
import hievpy as hp
hp.search(api_token, base_url, search_params)
```

A list of HIEv record objects matching the search parameters will be returned. The optional arguments that can be 
passed to the search call are outlined below:


>- from_date - This is "Date->From Date" in search box of WEB UI: "from_date"=>"2013-01-01"
>- to_date - This is "Date->To Date" in search box of WEB UI: "to_date"=>"2013-01-02"
>- filename - This is "Filename" in search box of WEB UI: "filename"=>"test"
>- description - This is "Description" in search box of WEB UI: "description"=>"test"
>- file_id - This is "File ID" in search box of WEB UI: "file_id"=>"test"
>- id (here replaced as record_id)- This is "ID" in search box of WEB UI: "id"=>"26"
>- stati - This is "Type" in search box of WEB UI: "stati"=>["RAW", "CLEANSED"]
>- automation_stati - This is "Automation Status" in search box of WEB UI, "automation_stati"=>["COMPLETE",
>  "WORKING"]
>- access_rights_types - This is the "Access Rights Type" in the search box of the WEB UI: "access_rights_types"=>
>  ["Open", "Conditional", "Restricted"]
>- file_formats - This is "File Formats" in search box of WEB UI, "file_formats"=>["TOA5", "Unknown", "audio/mpeg"]
>- published - This is "Type->PACKAGE->Published" in search box of WEB UI: "stati"=>["PACKAGE"], "published"=>
>  ["true"]
>- unpublished - This is "Type->PACKAGE->Published" in search box of WEB UI: "stati"=>["PACKAGE"], "unpublished"=>
>  ["true"].
>- published_date - This is "Type->PACKAGE->Published Date" in search box of WEB UI: "stati"=>["PACKAGE"],
>  "published_date"=>"2013-01-01"
>- tags - This is "Tags" in search box of WEB UI: "tags"=>["4", "5"]
>- labels - This is "Labels" in search box of WEB UI, "labels"=>["label_name_1", "label_name_2"]
>- grant_numbers - This is the "Grant Numbers" in search box of WEB UI, "grant_numbers"=>["grant_number_1",
>  "grant_number_2"]
>- related_websites - This is the "Related Websites" in the search box of WEB UI, "related_websites"=>
>  ["http://www.intersect.org.au"]
>- facilities - This is "Facility" in search box of WEB UI, ask system administrator to get facility ids :
>  "facilities"=>["27"]
>- experiments - This is "Facility" in search box of WEB UI, when one facility is clicked, experiments of this
>  facility are selectable, ask system administrator to get experiment ids: "experiments"=>["58", "54"]
>- variables - This is "Columns" in search box of WEB UI, when one group is clicked, columns of this group are
>  selectable: "variables"=>["SoilTempProbe_Avg(1)", "SoilTempProbe_Avg(3)"]
>- uploader_id - This is "Added By" in search box of WEB UI, ask system administrator to get uploader ids:
>  "uploader_id"=>"83"
>- upload_from_date - This is "Date Added->From Date" in search box of WEB UI, "upload_from_date"=>"2013-01-01"
>- upload_to_date - This is "Date Added->To Date" in search box of WEB UI, "upload_to_date"=>"2013-01-02"


**It is highly recommended that you supply at least one search query to your search to limit returning the full 
database in one call**


## Example

As an example, to search for all records with data for February 2017 from the DriGrass facility (id=10) and save to 
a variable called *my_files* use:
```sh
my_files = hievpy.search(api_token, from_date="2017-02-01", to_date="2017-02-28", facilities=['10'])
```

Note that by default the Search function calls out to https://hiev.westernsydney.edu.au (i.e. 
the HIEv at HIE). You can override this by providing a _base_url_ parameter to the search function, e.g.:

```sh
my_files = hievpy.search(api_token, base_url='https://myhiev.com.au', from_date="2017-02-01")
```


Or, alternatively, download a Jupyter notebook version of this example from the __/examples__ folder :