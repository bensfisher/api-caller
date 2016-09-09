This program should work with any API that requires an api key, an arbitrary set
of search arguments, and returns the results in a json format. This has been 
successfully tested on the New York Times API and the regulations.gov API.  

Example

Begin by initializing the api_call with your API key and the url for the API.

```python
from api_caller import api_call

key = 'yourapikey'
url = 'apiurl'

call = api_call(key=key, url=url)
```

To submit the call, provide the name for the API key argument used by the API
being queried. For example, the argument name for the NYT is 'api-key', as opposed to
'api_key' for regulations.gov.

```python
keyvar = 'nameofkeyargument'

call(keyvar=keyvar, arg1=arg1, arg2=arg2...)
```

The call function returns the results as a dictionary object.
