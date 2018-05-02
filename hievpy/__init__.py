# coding: utf-8
import os
import urllib.request
import urllib.parse
import json
import pandas as pd
import requests
import io


# Global Defaults
BASE_URL = 'https://hiev.westernsydney.edu.au/'


def search(api_token, base_url=BASE_URL, **kwargs):
    """ Returns a list of HIEv records (or their IDs) matching a set of input search parameters.
    
    (see https://github.com/IntersectAustralia/dc21-doc/blob/2.3/Search_API.md)

    Input
    -----
    Required
    - api_token: HIEv API token/key

    Optional keyword arguments
    - base_url - Base URL of the HIEv/Diver instance. Default is 'https://hiev.uws.edu.au'
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

    Returns
    -------
    List of matching hiev search results (with file download url included)

    Example
    -------
    my_files = hievpy.search('MY_API_TOKEN', experiments=['90'], from_date="2016-02-12")

    """

    request_url = base_url + 'data_files/api_search'

    request_data = kwargs
    # Add Auth/API token to request_data
    request_data['auth_token'] = api_token

    # -- Set up the http request and handle the returned response
    data = urllib.parse.urlencode(request_data, True)
    data = data.encode('ascii')
    req = urllib.request.Request(request_url, data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()

    encoding = response.info().get_content_charset('utf-8')
    results = json.loads(the_page.decode(encoding))

    return results


def download(api_token, record, path=None):
    """ Downloads a file from HIEv to local computer given the file record (as returned by search)
    
    Input
    -----
    Required
    - api_token: HIEv API token/key
    - record: record object returned by the search function
    
    Optional
    - path: Full path of download directory (if path not provided, file will be downloaded to current directory)
    """

    download_url = record['url'] + '?' + 'auth_token=%s' % api_token

    if path:
        download_path = os.path.join(path, record['filename'])
        urllib.request.urlretrieve(download_url, download_path)
    else:
        urllib.request.urlretrieve(download_url, record['filename'])


def toa5_to_df(api_token, record):
    """ Loads a TOA5 file from HIEv into a pandas dataframe given the file record (returned by search function).

    Input
    -----
    Required
    - api_token: HIEv API token/key
    - record: record object returned by the search function

    Returns
    -------
    Pandas dataframe of TOA5 data

    NOTE:
    The top row of the original TOA5 file (logger info etc) is discarded during dataframe creation
    """

    download_url = record['url'] + '?' + 'auth_token=%s' % api_token
    url_data = requests.get(download_url).content
    # TODO Check that file is actually a TOA5 file before proceeding....
    df = pd.read_csv(io.StringIO(url_data.decode('utf-8')), skiprows=1)

    # Disregard the units and measurement type rows (whose info can alternatively returned via the toa5_info function)
    df = df.iloc[2:, :]
    df = df.set_index('TIMESTAMP')
    df.index = pd.to_datetime(df.index)
    df = df.apply(pd.to_numeric)

    return df


def toa5_info(api_token, record):
    """ Returns variable information (name, units and measurement type) from a HIEv TOA5 file given the file
    record (returned by search function).
    """

    download_url = record['url'] + '?' + 'auth_token=%s' % api_token
    url_data = requests.get(download_url).content
    # TODO Check that file is actually a TOA5 file before proceeding....
    df = pd.read_csv(io.StringIO(url_data.decode('utf-8')), skiprows=1)

    # TO BE COMPLETED
