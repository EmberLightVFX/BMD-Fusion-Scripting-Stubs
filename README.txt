A script to generate python stubs from Fusion.
It uses a modified version of Roger Magnusson's Class Browser Extractor script to genenrate the needed json files
Simply run the script and select the json_stubs folder. When the UI opens the files have bin generated.

Now run the stubs_generator script and you'll find all the newly created stubs in the typings folder.

Add the typings folder to your language interpreters extra folder.
In VSCode and Pylance add this string to your settings.json:
```json
"python.analysis.extraPaths": [
    "./typings"
],
```
The script adds all the newly created classes to __builtins__.pyi so your python files will find these classes without the need to import anything in your python script (that would break the script when ran from Fusion as Fusion already have those classes in the global space)