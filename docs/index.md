### Pre-requisites
To use HIEvPY you must have an active account (and subsequently a HIEv API token) on the 
[**HIEv**](https://hiev.westernsydney.edu.au) application. To discuss registration please contact HIE's data manager, 
[Gerry Devine](mailto:g.devine@westernsydney.edu.au)


### Installation
HIEvPy can be installed via *pip*:

``` bash
$ pip install --index-url https://test.pypi.org/simple/ hievpy
```

> Note: HIEvPy is currently hosted on Test PyPi. This will soon be moved to the official PyPi repository

Once HIEvPy has been installed, you can import it into a python console or script using:

``` python
import hievpy
```


### HIEv API key 
The majority of HIEvPy functions will require passing in your HIEv API key/token for authentication purposes. 
It is highly recommended that you keep your API key outside of your actual code (particularly if you intend on sharing 
code). Instead, store your API token in a private file or in a local environment variable and externally load it into 
your code, e.g:

```python
api_token = os.environ['HIEV_API_KEY']
```


### HIEvPy Functions

#### Search
To search for records within HIEv database, you can use the hievpy _search_ function:
```sh
hievpy.search(api_token, <optional search parameters>)
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

A more thorough walk-through of the HIEvPy search function can be found here:

[HIEvPy Search Example](notebooks/hievpy-search.md)

Or, alternatively, download a working Jupyter notebook of this example:

[HIEvPy Search Jupyter Notebook](notebooks/hievpy-search.ipynb)

 
#### Download
The HIEvPy.download function can be used in conjunction with the search function to download a file from HIEv (with option to specify download location)
```sh
hievpy.download(api_token, search_record, <optional path>)
```

As an example, the following code snippet is used to search for all files with data for March 15th 2017 from the 
Mini-ROS/DriGrass facility and to download the results to a directory called My_HIEv_DATA (directory must exist)
```python
my_files = hievpy.search(api_token, from_date="2017-03-15", to_date="2017-03-16", facilities=['10'])
for my_file in my_files:
    hievpy.download(api_token, my_file, path='/Users/Me/My_HIEv_DATA/')
```
