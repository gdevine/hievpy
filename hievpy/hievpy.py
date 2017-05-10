# coding: utf-8
import urllib2
import requests
import json

# Global variables
BASE_URL = 'https://hiev.uws.edu.au/'


def search_hiev(auth_token,
                base_url=BASE_URL,
                full_records=True,
                from_date=None,
                to_date=None,
                filename=None,
                description=None,
                file_id=None,
                record_id=None,
                stati=None,
                automation_stati=None,
                access_rights_types=None,
                file_formats=None,
                published=None,
                unpublished=None,
                published_date=None,
                tags=None,
                labels=None,
                grant_numbers=None,
                related_websites=None,
                facilities=None,
                experiments=None,
                variables=None,
                uploader_id=None,
                upload_from_date=None,
                upload_to_date=None):
    """
    Returns a list of full file records (or their IDs) matching a set of input search parameters
    (see https://github.com/IntersectAustralia/dc21-doc/blob/2.3/Search_API.md)

    Input
    -----
    Required
    - auth_token - HIEv Authorisation token/key

    Optional
    - base_url - Base URL of the HIEv/Diver instance. Default is 'https://hiev.uws.edu.au'
    - full_records - Boolean value dictating whether to return full records or just IDs - Default is full records
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
    List of matching hiev search results (with file download url included) OR list of matching file IDs 

    Example
    -------
    myfiles = searchHIEv('3uzsPVNajEf762KRQhXV', full_records=False, experiments=['39'], from_date="2016-08-01")

    """

    request_url = base_url + 'data_files/api_search'

    # -- Set up the http search request and handle the returned response
    request_headers = {'Content-Type': 'application/json; charset=UTF-8', 'X-Accept': 'application/json'}
    request_data = json.dumps(
        {'auth_token': auth_token, 'filename': filename, 'from_date': from_date, 'to_date': to_date,
         'description': description, 'file_id': file_id, 'id': record_id, 'stati': stati,
         'automation_stati': automation_stati, 'access_rights_types': access_rights_types, 'file_formats': file_formats,
         'published': published, 'unpublished': unpublished, 'published_date': published_date, 'tags': tags,
         'labels': labels, 'grant_numbers': grant_numbers, 'related_websites': related_websites,
         'facilities': facilities, 'experiments': experiments, 'variables': variables, 'uploader_id': uploader_id,
         'upload_from_date': upload_from_date, 'upload_to_date': upload_to_date})
    requests.packages.urllib3.disable_warnings()  # ignore ssl warnings from python 2.7.5
    request = urllib2.Request(request_url, request_data, request_headers)
    response = urllib2.urlopen(request)

    if full_records:
        return json.load(response)
    else:
        records_list = json.load(response)
        # Create an empty list to hold our IDs
        ids = []
        # Loop over each record and pull out the ID field
        for rec in records_list:
            ids.append(rec['file_id'])

        return ids
