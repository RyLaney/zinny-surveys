
## Usage
The surveys and weights can be accessed using the zinny_surveys package or pkg_resources. The surveys are stored as JSON files and can be loaded as dictionaries. A function list is available in the [Functions.md](README_Functions.md) file.

### Access using zinny_surveys package:
```python
from zinny_surveys import load_survey, load_weight

zinny_surveys.list_file_types()
# ['weights', 'surveys']

zinny_surveys.list_files("surveys", "shared")
# ['vfx_exhaustive.json', 'docs.json', 'vfx_extended.json', 'picture_extended.json', 'directoral.json', 'cinematography.json', 'vfx.json', 'picture.json', 'acting.json']
```

### Acccess using pkg_resources:
```python
import pkg_resources
import json

def load_json_file(package, resource_path):
    resource = pkg_resources.resource_string(package, resource_path)
    return json.loads(resource)

# Example usage
data = load_json_file('zinny_surveys', 'surveys/shared/example.json')
print(data)
```


## Functions

This section provides an overview of available functions and their descriptions:

### zinny_surveys


#### list_file_types():
```
Lists available file types.

Returns:
    list: List of available file types.
```
#### list_scopes(file_type):
```
Lists available scopes for the specified file type.

Args:
    file_type (str): 'surveys' or 'weights'.

Returns:
    list: List of available scopes.
```
#### list_files(file_type, scope):
```
Lists files in the specified scope and file_type.

Args:
    file_type (str): 'surveys' or 'weights'.
    scope (str): 'shared' or 'local'.

Returns:
    list: List of file paths relative to the file_type directory.
```
#### list_surveys(scope):
```
Lists surveys in the specified scope.

Args:
    scope (str): 'shared' or 'local'.

Returns:
    list: List of survey file names.
```
#### load_file(file_type, scope, file_name):
```
Loads a file's content.

Args:
    file_type (str): 'surveys' or 'weights'.
    scope (str): 'shared' or 'local'.
    file_name (str): Name of the file to load.

Returns:
    dict: Parsed JSON content.
```
#### load_survey(file_name):
```
Loads a survey file.

Args:
    file_name (str): Name of the survey file to load.

Returns:
    dict: Parsed JSON content.
```
#### validate_survey_file(content):
```
Validate file content.

Args:
    content (dict): Content to validate.

Returns:
    bool: True if valid, False otherwise.
```
#### save_file(file_type, scope, file_name):
```
Saves content to a file in the local directory.

Args:
    file_type (str): 'surveys' or 'weights'.
    file_name (str): Name of the file to save.
    content (dict): Content to save as JSON.

Returns:
    str: Path to the saved file.
```

#### Note to self
generated using zinny-dev/doc_strings_to_md.py