## requet body

- request.data Contains the incoming request data as string in case it came with a mimetype Flask does not handle.

- request.args: the key/value pairs in the URL query string
- request.form: the key/value pairs in the body, from a HTML post form, or JavaScript request that isn't JSON encoded
- request.files: the files in the body, which Flask keeps separate from form. HTML forms must use enctype=multipart/form-data or files will not be uploaded.
- request.values: combined args and form, preferring args if keys overlap
- request.json: parsed JSON data. The request must have the application/json content type, or use request.get_json(force=True) to ignore the content type.
