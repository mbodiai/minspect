<details><summary><h2>requests</h2></summary>
  <details><summary><code type="python"> Requests is an HTTP library, written in Python, for human beings.</code></summary>
    <code type="python">
    Basic GET usage:

      >>> import requests
      >>> r = requests.get('https://www.python.org')
      >>> r.status_code
      200
      >>> b'Python is a programming language' in r.content
      True

    ... or POST:

      >>> payload = dict(key1='value1', key2='value2')
      >>> r = requests.post('https://httpbin.org/post', data=payload)
      >>> print(r.text)
      {
        ...
        "form": {
          "key1": "value1",
          "key2": "value2"
        },
        ...
      }

    The other HTTP methods are supported - see `requests.api`. Full documentation
    is at <https://requests.readthedocs.io>.

    :copyright: (c) 2017 by Kenneth Reitz.
    :license: Apache 2.0, see LICENSE for more details.
  </code>
  </details>



  <details><summary><h3>class ConnectTimeout:</h3></summary>
  <li> The request timed out while trying to connect to the remote server.</li>

  Requests that produced this error are safe to retry.
  </details>

  <details>
    <summary><b>type</b></summary>
    <details>
    
  <summary>class type:</summary>

  <li><code>def type(object) -> type</code></li>

</details>

  <details>
    <summary><b>object</b></summary>
    <details>
      <summary>class object:</summary>
- **Documentation**: The base class of the class hierarchy.

When called, it accepts no arguments and returns a new featureless
instance that has no instance attributes and cannot be given any.
        </details>

      </details>

    </details>

    <details>
      <summary><b>__init__</b></summary>
  - **Signature**: `def __init__(self, *args, **kwargs):`
  - **Documentation**: Initialize RequestException with `request` and `response` objects.

      <details>
        <summary>Source Code</summary>
    ```python
        def __init__(self, *args, **kwargs):
            """Initialize RequestException with `request` and `response` objects."""
            response = kwargs.pop("response", None)
            self.response = response
            self.request = kwargs.pop("request", None)
            if response is not None and not self.request and hasattr(response, "request"):
                self.request = self.response.request
            super().__init__(*args, **kwargs)
    
    ```
      </details>

    </details>

  </details>

  <details>
    <summary><b>ConnectionError</b></summary>
    <details>
      <summary>class ConnectionError:</summary>
    - **Documentation**: A Connection error occurred.
    </details>

    <details>
      <summary><b>__init__</b></summary>
  - **Signature**: `def __init__(self, *args, **kwargs):`
  - **Documentation**: Initialize RequestException with `request` and `response` objects.

      <details>
        <summary>Source Code</summary>
    ```python
        def __init__(self, *args, **kwargs):
            """Initialize RequestException with `request` and `response` objects."""
            response = kwargs.pop("response", None)
            self.response = response
            self.request = kwargs.pop("request", None)
            if response is not None and not self.request and hasattr(response, "request"):
                self.request = self.response.request
            super().__init__(*args, **kwargs)
    
    ```
      </details>

    </details>

  </details>

  <details>
    <summary><b>DependencyWarning</b></summary>
    <details>
      <summary>class DependencyWarning:</summary>
    - **Documentation**: Warned when an attempt is made to import a module with missing optional
dependencies.
    </details>

  </details>

  <details>
    <summary><b>FileModeWarning</b></summary>
    <details>
      <summary>class FileModeWarning:</summary>
    - **Documentation**: A file was opened in text mode, but Requests determined its binary length.
    </details>

  </details>

  <details>
    <summary><b>HTTPError</b></summary>
    <details>
      <summary>class HTTPError:</summary>
    - **Documentation**: An HTTP error occurred.
    </details>

    <details>
      <summary><b>__init__</b></summary>
  - **Signature**: `def __init__(self, *args, **kwargs):`
  - **Documentation**: Initialize RequestException with `request` and `response` objects.

      <details>
        <summary>Source Code</summary>
    ```python
        def __init__(self, *args, **kwargs):
            """Initialize RequestException with `request` and `response` objects."""
            response = kwargs.pop("response", None)
            self.response = response
            self.request = kwargs.pop("request", None)
            if response is not None and not self.request and hasattr(response, "request"):
                self.request = self.response.request
            super().__init__(*args, **kwargs)
    
    ```
      </details>

    </details>

  </details>

  <details>
    <summary><b>JSONDecodeError</b></summary>
    <details>
      <summary>class JSONDecodeError:</summary>
    - **Documentation**: Couldn't decode the text into json
    </details>

    <details>
      <summary><b>__init__</b></summary>
  - **Signature**: `def __init__(self, *args, **kwargs):`
  - **Documentation**: Construct the JSONDecodeError instance first with all
args. Then use it's args to construct the IOError so that
the json specific args aren't used as IOError specific args
and the error message from JSONDecodeError is preserved.

      <details>
        <summary>Source Code</summary>
    ```python
        def __init__(self, *args, **kwargs):
            """
            Construct the JSONDecodeError instance first with all
            args. Then use it's args to construct the IOError so that
            the json specific args aren't used as IOError specific args
            and the error message from JSONDecodeError is preserved.
            """
            CompatJSONDecodeError.__init__(self, *args)
            InvalidJSONError.__init__(self, *self.args, **kwargs)
    
    ```
      </details>

    </details>

    <details>
      <summary><b>__reduce__</b></summary>
  - **Signature**: `def __reduce__(self):`
  - **Documentation**: The __reduce__ method called when pickling the object must
be the one from the JSONDecodeError (be it json/simplejson)
as it expects all the arguments for instantiation, not just
one like the IOError, and the MRO would by default call the
__reduce__ method from the IOError due to the inheritance order.

      <details>
        <summary>Source Code</summary>
    ```python
        def __reduce__(self):
            """
            The __reduce__ method called when pickling the object must
            be the one from the JSONDecodeError (be it json/simplejson)
            as it expects all the arguments for instantiation, not just
            one like the IOError, and the MRO would by default call the
            __reduce__ method from the IOError due to the inheritance order.
            """
            return CompatJSONDecodeError.__reduce__(self)
    
    ```
      </details>

    </details>

  </details>

  <details>
    <summary><b>NullHandler</b></summary>
    <details>
      <summary>class NullHandler:</summary>
    - **Documentation**: This handler does nothing. It's intended to be used to avoid the
"No handlers could be found for logger XXX" one-off warning. This is
important for library code, which may contain code to log events. If a user
of the library does not configure logging, the one-off warning might be
produced; to avoid this, the library developer simply needs to instantiate
a NullHandler and add it to the top-level logger of the library module or
package.
    </details>

    <details>
      <summary><b>__init__</b></summary>
  - **Signature**: `def __init__(self, level=0):`
  - **Documentation**: Initializes the instance - basically setting the formatter to None
and the filter list to empty.

      <details>
        <summary>Source Code</summary>
    ```python
        def __init__(self, level=NOTSET):
            """
            Initializes the instance - basically setting the formatter to None
            and the filter list to empty.
            """
            Filterer.__init__(self)
            self._name = None
            self.level = _checkLevel(level)
            self.formatter = None
            self._closed = False
            # Add the handler to the global _handlerList (for cleanup on shutdown)
            _addHandlerRef(self)
            self.createLock()
    
    ```
      </details>

    </details>

    <details>
      <summary><b>__repr__</b></summary>
  - **Signature**: `def __repr__(self):`
  - **Documentation**: Return repr(self).

      <details>
        <summary>Source Code</summary>
    ```python
        def __repr__(self):
            level = getLevelName(self.level)
            return '<%s (%s)>' % (self.__class__.__name__, level)
    
    ```
      </details>

    </details>

    <details>
      <summary><b>_at_fork_reinit</b></summary>
  - **Signature**: `def _at_fork_reinit(self):`
  - **Documentation**: No documentation provided.

      <details>
        <summary>Source Code</summary>
    ```python
        def _at_fork_reinit(self):
            pass
    
    ```
      </details>

    </details>

    <details>
      <summary><b>acquire</b></summary>
  - **Signature**: `def acquire(self):`
  - **Documentation**: Acquire the I/O thread lock.

      <details>
        <summary>Source Code</summary>
    ```python
        def acquire(self):
            """
            Acquire the I/O thread lock.
            """
            if self.lock:
                self.lock.acquire()
    
    ```
      </details>

    </details>

    <details>
      <summary><b>addFilter</b></summary>
  - **Signature**: `def addFilter(self, filter):`
  - **Documentation**: Add the specified filter to this handler.

      <details>
        <summary>Source Code</summary>
    ```python
        def addFilter(self, filter):
            """
            Add the specified filter to this handler.
            """
            if not (filter in self.filters):
                self.filters.append(filter)
    
    ```
      </details>

    </details>

    <details>
      <summary><b>close</b></summary>
  - **Signature**: `def close(self):`
  - **Documentation**: Tidy up any resources used by the handler.

This version removes the handler from an internal map of handlers,
_handlers, which is used for handler lookup by name. Subclasses
should ensure that this gets called from overridden close()
methods.

      <details>
        <summary>Source Code</summary>
    ```python
        def close(self):
            """
            Tidy up any resources used by the handler.
    
            This version removes the handler from an internal map of handlers,
            _handlers, which is used for handler lookup by name. Subclasses
            should ensure that this gets called from overridden close()
            methods.
            """
            #get the module data lock, as we're updating a shared structure.
            _acquireLock()
            try:    #unlikely to raise an exception, but you never know...
                self._closed = True
                if self._name and self._name in _handlers:
                    del _handlers[self._name]
            finally:
                _releaseLock()
    
    ```
      </details>

    </details>

    <details>
      <summary><b>createLock</b></summary>
  - **Signature**: `def createLock(self):`
  - **Documentation**: Acquire a thread lock for serializing access to the underlying I/O.

      <details>
        <summary>Source Code</summary>
    ```python
        def createLock(self):
            self.lock = None
    
    ```
      </details>

    </details>

    <details>
      <summary><b>emit</b></summary>
  - **Signature**: `def emit(self, record):`
  - **Documentation**: Stub.

      <details>
        <summary>Source Code</summary>
    ```python
        def emit(self, record):
            """Stub."""
    
    ```
      </details>

    </details>

    <details>
      <summary><b>filter</b></summary>
  - **Signature**: `def filter(self, record):`
  - **Documentation**: Determine if a record is loggable by consulting all the filters.

The default is to allow the record to be logged; any filter can veto
this and the record is then dropped. Returns a zero value if a record
is to be dropped, else non-zero.

.. versionchanged:: 3.2

   Allow filters to be just callables.

      <details>
        <summary>Source Code</summary>
    ```python
        def filter(self, record):
            """
            Determine if a record is loggable by consulting all the filters.
    
            The default is to allow the record to be logged; any filter can veto
            this and the record is then dropped. Returns a zero value if a record
            is to be dropped, else non-zero.
    
            .. versionchanged:: 3.2
    
               Allow filters to be just callables.
            """
            rv = True
            for f in self.filters:
                if hasattr(f, 'filter'):
                    result = f.filter(record)
                else:
                    result = f(record) # assume callable - will raise if not
                if not result:
                    rv = False
                    break
            return rv
    
    ```
      </details>

    </details>

    <details>
      <summary><b>flush</b></summary>
  - **Signature**: `def flush(self):`
  - **Documentation**: Ensure all logging output has been flushed.

This version does nothing and is intended to be implemented by
subclasses.

      <details>
        <summary>Source Code</summary>
    ```python
        def flush(self):
            """
            Ensure all logging output has been flushed.
    
            This version does nothing and is intended to be implemented by
            subclasses.
            """
            pass
    
    ```
      </details>

    </details>

    <details>
      <summary><b>format</b></summary>
  - **Signature**: `def format(self, record):`
  - **Documentation**: Format the specified record.

If a formatter is set, use it. Otherwise, use the default formatter
for the module.

      <details>
        <summary>Source Code</summary>
    ```python
        def format(self, record):
            """
            Format the specified record.
    
            If a formatter is set, use it. Otherwise, use the default formatter
            for the module.
            """
            if self.formatter:
                fmt = self.formatter
            else:
                fmt = _defaultFormatter
            return fmt.format(record)
    
    ```
      </details>

    </details>

    <details>
      <summary><b>get_name</b></summary>
  - **Signature**: `def get_name(self):`
  - **Documentation**: No documentation provided.

      <details>
        <summary>Source Code</summary>
    ```python
        def get_name(self):
            return self._name
    
    ```
      </details>

    </details>

    <details>
      <summary><b>handle</b></summary>
  - **Signature**: `def handle(self, record):`
  - **Documentation**: Stub.

      <details>
        <summary>Source Code</summary>
    ```python
        def handle(self, record):
            """Stub."""
    
    ```
      </details>

    </details>

    <details>
      <summary><b>handleError</b></summary>
  - **Signature**: `def handleError(self, record):`
  - **Documentation**: Handle errors which occur during an emit() call.

This method should be called from handlers when an exception is
encountered during an emit() call. If raiseExceptions is false,
exceptions get silently ignored. This is what is mostly wanted
for a logging system - most users will not care about errors in
the logging system, they are more interested in application errors.
You could, however, replace this with a custom handler if you wish.
The record which was being processed is passed in to this method.

      <details>
        <summary>Source Code</summary>
    ```python
        def handleError(self, record):
            """
            Handle errors which occur during an emit() call.
    
            This method should be called from handlers when an exception is
            encountered during an emit() call. If raiseExceptions is false,
            exceptions get silently ignored. This is what is mostly wanted
            for a logging system - most users will not care about errors in
            the logging system, they are more interested in application errors.
            You could, however, replace this with a custom handler if you wish.
            The record which was being processed is passed in to this method.
            """
            if raiseExceptions and sys.stderr:  # see issue 13807
                t, v, tb = sys.exc_info()
                try:
                    sys.stderr.write('--- Logging error ---\n')
                    traceback.print_exception(t, v, tb, None, sys.stderr)
                    sys.stderr.write('Call stack:\n')
                    # Walk the stack frame up until we're out of logging,
                    # so as to print the calling context.
                    frame = tb.tb_frame
                    while (frame and os.path.dirname(frame.f_code.co_filename) ==
                           __path__[0]):
                        frame = frame.f_back
                    if frame:
                        traceback.print_stack(frame, file=sys.stderr)
                    else:
                        # couldn't find the right stack frame, for some reason
                        sys.stderr.write('Logged from file %s, line %s\n' % (
                                         record.filename, record.lineno))
                    # Issue 18671: output logging message and arguments
                    try:
                        sys.stderr.write('Message: %r\n'
                                         'Arguments: %s\n' % (record.msg,
                                                              record.args))
                    except RecursionError:  # See issue 36272
                        raise
                    except Exception:
                        sys.stderr.write('Unable to print the message and arguments'
                                         ' - possible formatting error.\nUse the'
                                         ' traceback above to help find the error.\n'
                                        )
                except OSError: #pragma: no cover
                    pass    # see issue 5971
                finally:
                    del t, v, tb
    
    ```
      </details>

    </details>

    <details>
      <summary><b>release</b></summary>
  - **Signature**: `def release(self):`
  - **Documentation**: Release the I/O thread lock.

      <details>
        <summary>Source Code</summary>
    ```python
        def release(self):
            """
            Release the I/O thread lock.
            """
            if self.lock:
                self.lock.release()
    
    ```
      </details>

    </details>

    <details>
      <summary><b>removeFilter</b></summary>
  - **Signature**: `def removeFilter(self, filter):`
  - **Documentation**: Remove the specified filter from this handler.

      <details>
        <summary>Source Code</summary>
    ```python
        def removeFilter(self, filter):
            """
            Remove the specified filter from this handler.
            """
            if filter in self.filters:
                self.filters.remove(filter)
    
    ```
      </details>

    </details>

    <details>
      <summary><b>setFormatter</b></summary>
  - **Signature**: `def setFormatter(self, fmt):`
  - **Documentation**: Set the formatter for this handler.

      <details>
        <summary>Source Code</summary>
    ```python
        def setFormatter(self, fmt):
            """
            Set the formatter for this handler.
            """
            self.formatter = fmt
    
    ```
      </details>

    </details>

    <details>
      <summary><b>setLevel</b></summary>
  - **Signature**: `def setLevel(self, level):`
  - **Documentation**: Set the logging level of this handler.  level must be an int or a str.

      <details>
        <summary>Source Code</summary>
    ```python
        def setLevel(self, level):
            """
            Set the logging level of this handler.  level must be an int or a str.
            """
            self.level = _checkLevel(level)
    
    ```
      </details>

    </details>

    <details>
      <summary><b>set_name</b></summary>
  - **Signature**: `def set_name(self, name):`
  - **Documentation**: No documentation provided.

      <details>
        <summary>Source Code</summary>
    ```python
        def set_name(self, name):
            _acquireLock()
            try:
                if self._name in _handlers:
                    del _handlers[self._name]
                self._name = name
                if name:
                    _handlers[name] = self
            finally:
                _releaseLock()
    
    ```
      </details>

    </details>

  </details>

  <details>
    <summary><b>PreparedRequest</b></summary>
    <details>
      <summary>class PreparedRequest:</summary>
    - **Documentation**: The fully mutable :class:`PreparedRequest <PreparedRequest>` object,
containing the exact bytes that will be sent to the server.

Instances are generated from a :class:`Request <Request>` object, and
should not be instantiated manually; doing so may produce undesirable
effects.

Usage::

  >>> import requests
  >>> req = requests.Request('GET', 'https://httpbin.org/get')
  >>> r = req.prepare()
  >>> r
  <PreparedRequest [GET]>

  >>> s = requests.Session()
  >>> s.send(r)
  <Response [200]>
    </details>

    <details>
      <summary><b>__init__</b></summary>
  - **Signature**: `def __init__(self):`
  - **Documentation**: Initialize self.  See help(type(self)) for accurate signature.

      <details>
        <summary>Source Code</summary>
    ```python
        def __init__(self):
            #: HTTP verb to send to the server.
            self.method = None
            #: HTTP URL to send the request to.
            self.url = None
            #: dictionary of HTTP headers.
            self.headers = None
            # The `CookieJar` used to create the Cookie header will be stored here
            # after prepare_cookies is called
            self._cookies = None
            #: request body to send to the server.
            self.body = None
            #: dictionary of callback hooks, for internal usage.
            self.hooks = default_hooks()
            #: integer denoting starting position of a readable file-like body.
            self._body_position = None
    
    ```
      </details>

    </details>

    <details>
      <summary><b>__repr__</b></summary>
  - **Signature**: `def __repr__(self):`
  - **Documentation**: Return repr(self).

      <details>
        <summary>Source Code</summary>
    ```python
        def __repr__(self):
            return f"<PreparedRequest [{self.method}]>"
    
    ```
      </details>

    </details>

    <details>
      <summary><b>_encode_files</b></summary>
  - **Signature**: `def _encode_files(files, data):`
  - **Documentation**: Build the body for a multipart/form-data request.

Will successfully encode files when passed as a dict or a list of
tuples. Order is retained if data is a list of tuples but arbitrary
if parameters are supplied as a dict.
The tuples may be 2-tuples (filename, fileobj), 3-tuples (filename, fileobj, contentype)
or 4-tuples (filename, fileobj, contentype, custom_headers).

      <details>
        <summary>Source Code</summary>
    ```python
        @staticmethod
        def _encode_files(files, data):
            """Build the body for a multipart/form-data request.
    
            Will successfully encode files when passed as a dict or a list of
            tuples. Order is retained if data is a list of tuples but arbitrary
            if parameters are supplied as a dict.
            The tuples may be 2-tuples (filename, fileobj), 3-tuples (filename, fileobj, contentype)
            or 4-tuples (filename, fileobj, contentype, custom_headers).
            """
            if not files:
                raise ValueError("Files must be provided.")
            elif isinstance(data, basestring):
                raise ValueError("Data must not be a string.")
    
            new_fields = []
            fields = to_key_val_list(data or {})
            files = to_key_val_list(files or {})
    
            for field, val in fields:
                if isinstance(val, basestring) or not hasattr(val, "__iter__"):
                    val = [val]
                for v in val:
                    if v is not None:
                        # Don't call str() on bytestrings: in Py3 it all goes wrong.
                        if not isinstance(v, bytes):
                            v = str(v)
    
                        new_fields.append(
                            (
                                field.decode("utf-8")
                                if isinstance(field, bytes)
                                else field,
                                v.encode("utf-8") if isinstance(v, str) else v,
                            )
                        )
    
            for k, v in files:
                # support for explicit filename
                ft = None
                fh = None
                if isinstance(v, (tuple, list)):
                    if len(v) == 2:
                        fn, fp = v
                    elif len(v) == 3:
                        fn, fp, ft = v
                    else:
                        fn, fp, ft, fh = v
                else:
                    fn = guess_filename(v) or k
                    fp = v
    
                if isinstance(fp, (str, bytes, bytearray)):
                    fdata = fp
                elif hasattr(fp, "read"):
                    fdata = fp.read()
                elif fp is None:
                    continue
                else:
                    fdata = fp
    
                rf = RequestField(name=k, data=fdata, filename=fn, headers=fh)
                rf.make_multipart(content_type=ft)
                new_fields.append(rf)
    
            body, content_type = encode_multipart_formdata(new_fields)
    
            return body, content_type
    
    ```
      </details>

    </details>

    <details>
      <summary><b>_encode_params</b></summary>
  - **Signature**: `def _encode_params(data):`
  - **Documentation**: Encode parameters in a piece of data.

Will successfully encode parameters when passed as a dict or a list of
2-tuples. Order is retained if data is a list of 2-tuples but arbitrary
if parameters are supplied as a dict.

      <details>
        <summary>Source Code</summary>
    ```python
        @staticmethod
        def _encode_params(data):
            """Encode parameters in a piece of data.
    
            Will successfully encode parameters when passed as a dict or a list of
            2-tuples. Order is retained if data is a list of 2-tuples but arbitrary
            if parameters are supplied as a dict.
            """
    
            if isinstance(data, (str, bytes)):
                return data
            elif hasattr(data, "read"):
                return data
            elif hasattr(data, "__iter__"):
                result = []
                for k, vs in to_key_val_list(data):
                    if isinstance(vs, basestring) or not hasattr(vs, "__iter__"):
                        vs = [vs]
                    for v in vs:
                        if v is not None:
                            result.append(
                                (
                                    k.encode("utf-8") if isinstance(k, str) else k,
                                    v.encode("utf-8") if isinstance(v, str) else v,
                                )
                            )
                return urlencode(result, doseq=True)
            else:
                return data
    
    ```
      </details>

    </details>

    <details>
      <summary><b>_get_idna_encoded_host</b></summary>
  - **Signature**: `def _get_idna_encoded_host(host):`
  - **Documentation**: No documentation provided.

      <details>
        <summary>Source Code</summary>
    ```python
        @staticmethod
        def _get_idna_encoded_host(host):
            import idna
    
            try:
                host = idna.encode(host, uts46=True).decode("utf-8")
            except idna.IDNAError:
                raise UnicodeError
            return host
    
    ```
      </details>

    </details>

    <details>
      <summary><b>copy</b></summary>
  - **Signature**: `def copy(self):`
  - **Documentation**: No documentation provided.

      <details>
        <summary>Source Code</summary>
    ```python
        def copy(self):
            p = PreparedRequest()
            p.method = self.method
            p.url = self.url
            p.headers = self.headers.copy() if self.headers is not None else None
            p._cookies = _copy_cookie_jar(self._cookies)
            p.body = self.body
            p.hooks = self.hooks
            p._body_position = self._body_position
            return p
    
    ```
      </details>

    </details>

    <details>
      <summary><b>deregister_hook</b></summary>
  - **Signature**: `def deregister_hook(self, event, hook):`
  - **Documentation**: Deregister a previously registered hook.
Returns True if the hook existed, False if not.

      <details>
        <summary>Source Code</summary>
    ```python
        def deregister_hook(self, event, hook):
            """Deregister a previously registered hook.
            Returns True if the hook existed, False if not.
            """
    
            try:
                self.hooks[event].remove(hook)
                return True
            except ValueError:
                return False
    
    ```
      </details>

    </details>

    <details>
      <summary><b>prepare</b></summary>
  - **Signature**: `def prepare(self, method=None, url=None, headers=None, files=None, data=None, params=None, auth=None, cookies=None, hooks=None, json=None):`
  - **Documentation**: Prepares the entire request with the given parameters.

      <details>
        <summary>Source Code</summary>
    ```python
        def prepare(
            self,
            method=None,
            url=None,
            headers=None,
            files=None,
            data=None,
            params=None,
            auth=None,
            cookies=None,
            hooks=None,
            json=None,
        ):
            """Prepares the entire request with the given parameters."""
    
            self.prepare_method(method)
            self.prepare_url(url, params)
            self.prepare_headers(headers)
            self.prepare_cookies(cookies)
            self.prepare_body(data, files, json)
            self.prepare_auth(auth, url)
    
            # Note that prepare_auth must be last to enable authentication schemes
            # such as OAuth to work on a fully prepared request.
    
            # This MUST go after prepare_auth. Authenticators could add a hook
            self.prepare_hooks(hooks)
    
    ```
      </details>

    </details>

    <details>
      <summary><b>prepare_auth</b></summary>
  - **Signature**: `def prepare_auth(self, auth, url=''):`
  - **Documentation**: Prepares the given HTTP auth data.

      <details>
        <summary>Source Code</summary>
    ```python
        def prepare_auth(self, auth, url=""):
            """Prepares the given HTTP auth data."""
    
            # If no Auth is explicitly provided, extract it from the URL first.
            if auth is None:
                url_auth = get_auth_from_url(self.url)
                auth = url_auth if any(url_auth) else None
    
            if auth:
                if isinstance(auth, tuple) and len(auth) == 2:
                    # special-case basic HTTP auth
                    auth = HTTPBasicAuth(*auth)
    
                # Allow auth to make its changes.
                r = auth(self)
    
                # Update self to reflect the auth changes.
                self.__dict__.update(r.__dict__)
    
                # Recompute Content-Length
                self.prepare_content_length(self.body)
    
    ```
      </details>

    </details>

    <details>
      <summary><b>prepare_body</b></summary>
  - **Signature**: `def prepare_body(self, data, files, json=None):`
  - **Documentation**: Prepares the given HTTP body data.

      <details>
        <summary>Source Code</summary>
    ```python
        def prepare_body(self, data, files, json=None):
            """Prepares the given HTTP body data."""
    
            # Check if file, fo, generator, iterator.
            # If not, run through normal process.
    
            # Nottin' on you.
            body = None
            content_type = None
    
            if not data and json is not None:
                # urllib3 requires a bytes-like body. Python 2's json.dumps
                # provides this natively, but Python 3 gives a Unicode string.
                content_type = "application/json"
    
                try:
                    body = complexjson.dumps(json, allow_nan=False)
                except ValueError as ve:
                    raise InvalidJSONError(ve, request=self)
    
                if not isinstance(body, bytes):
                    body = body.encode("utf-8")
    
            is_stream = all(
                [
                    hasattr(data, "__iter__"),
                    not isinstance(data, (basestring, list, tuple, Mapping)),
                ]
            )
    
            if is_stream:
                try:
                    length = super_len(data)
                except (TypeError, AttributeError, UnsupportedOperation):
                    length = None
    
                body = data
    
                if getattr(body, "tell", None) is not None:
                    # Record the current file position before reading.
                    # This will allow us to rewind a file in the event
                    # of a redirect.
                    try:
                        self._body_position = body.tell()
                    except OSError:
                        # This differentiates from None, allowing us to catch
                        # a failed `tell()` later when trying to rewind the body
                        self._body_position = object()
    
                if files:
                    raise NotImplementedError(
                        "Streamed bodies and files are mutually exclusive."
                    )
    
                if length:
                    self.headers["Content-Length"] = builtin_str(length)
                else:
                    self.headers["Transfer-Encoding"] = "chunked"
            else:
                # Multi-part file uploads.
                if files:
                    (body, content_type) = self._encode_files(files, data)
                else:
                    if data:
                        body = self._encode_params(data)
                        if isinstance(data, basestring) or hasattr(data, "read"):
                            content_type = None
                        else:
                            content_type = "application/x-www-form-urlencoded"
    
                self.prepare_content_length(body)
    
                # Add content-type if it wasn't explicitly provided.
                if content_type and ("content-type" not in self.headers):
                    self.headers["Content-Type"] = content_type
    
            self.body = body
    
    ```
      </details>

    </details>

    <details>
      <summary><b>prepare_content_length</b></summary>
  - **Signature**: `def prepare_content_length(self, body):`
  - **Documentation**: Prepare Content-Length header based on request method and body

      <details>
        <summary>Source Code</summary>
    ```python
        def prepare_content_length(self, body):
            """Prepare Content-Length header based on request method and body"""
            if body is not None:
                length = super_len(body)
                if length:
                    # If length exists, set it. Otherwise, we fallback
                    # to Transfer-Encoding: chunked.
                    self.headers["Content-Length"] = builtin_str(length)
            elif (
                self.method not in ("GET", "HEAD")
                and self.headers.get("Content-Length") is None
            ):
                # Set Content-Length to 0 for methods that can have a body
                # but don't provide one. (i.e. not GET or HEAD)
                self.headers["Content-Length"] = "0"
    
    ```
      </details>

    </details>

    <details>
      <summary><b>prepare_cookies</b></summary>
  - **Signature**: `def prepare_cookies(self, cookies):`
  - **Documentation**: Prepares the given HTTP cookie data.

This function eventually generates a ``Cookie`` header from the
given cookies using cookielib. Due to cookielib's design, the header
will not be regenerated if it already exists, meaning this function
can only be called once for the life of the
:class:`PreparedRequest <PreparedRequest>` object. Any subsequent calls
to ``prepare_cookies`` will have no actual effect, unless the "Cookie"
header is removed beforehand.

      <details>
        <summary>Source Code</summary>
    ```python
        def prepare_cookies(self, cookies):
            """Prepares the given HTTP cookie data.
    
            This function eventually generates a ``Cookie`` header from the
            given cookies using cookielib. Due to cookielib's design, the header
            will not be regenerated if it already exists, meaning this function
            can only be called once for the life of the
            :class:`PreparedRequest <PreparedRequest>` object. Any subsequent calls
            to ``prepare_cookies`` will have no actual effect, unless the "Cookie"
            header is removed beforehand.
            """
            if isinstance(cookies, cookielib.CookieJar):
                self._cookies = cookies
            else:
                self._cookies = cookiejar_from_dict(cookies)
    
            cookie_header = get_cookie_header(self._cookies, self)
            if cookie_header is not None:
                self.headers["Cookie"] = cookie_header
    
    ```
      </details>

    </details>

    <details>
      <summary><b>prepare_headers</b></summary>
  - **Signature**: `def prepare_headers(self, headers):`
  - **Documentation**: Prepares the given HTTP headers.

      <details>
        <summary>Source Code</summary>
    ```python
        def prepare_headers(self, headers):
            """Prepares the given HTTP headers."""
    
            self.headers = CaseInsensitiveDict()
            if headers:
                for header in headers.items():
                    # Raise exception on invalid header value.
                    check_header_validity(header)
                    name, value = header
                    self.headers[to_native_string(name)] = value
    
    ```
      </details>

    </details>

    <details>
      <summary><b>prepare_hooks</b></summary>
  - **Signature**: `def prepare_hooks(self, hooks):`
  - **Documentation**: Prepares the given hooks.

      <details>
        <summary>Source Code</summary>
    ```python
        def prepare_hooks(self, hooks):
            """Prepares the given hooks."""
            # hooks can be passed as None to the prepare method and to this
            # method. To prevent iterating over None, simply use an empty list
            # if hooks is False-y
            hooks = hooks or []
            for event in hooks:
                self.register_hook(event, hooks[event])
    
    ```
      </details>

    </details>

    <details>
      <summary><b>prepare_method</b></summary>
  - **Signature**: `def prepare_method(self, method):`
  - **Documentation**: Prepares the given HTTP method.

      <details>
        <summary>Source Code</summary>
    ```python
        def prepare_method(self, method):
            """Prepares the given HTTP method."""
            self.method = method
            if self.method is not None:
                self.method = to_native_string(self.method.upper())
    
    ```
      </details>

    </details>

    <details>
      <summary><b>prepare_url</b></summary>
  - **Signature**: `def prepare_url(self, url, params):`
  - **Documentation**: Prepares the given HTTP URL.

      <details>
        <summary>Source Code</summary>
    ```python
        def prepare_url(self, url, params):
            """Prepares the given HTTP URL."""
            #: Accept objects that have string representations.
            #: We're unable to blindly call unicode/str functions
            #: as this will include the bytestring indicator (b'')
            #: on python 3.x.
            #: https://github.com/psf/requests/pull/2238
            if isinstance(url, bytes):
                url = url.decode("utf8")
            else:
                url = str(url)
    
            # Remove leading whitespaces from url
            url = url.lstrip()
    
            # Don't do any URL preparation for non-HTTP schemes like `mailto`,
            # `data` etc to work around exceptions from `url_parse`, which
            # handles RFC 3986 only.
            if ":" in url and not url.lower().startswith("http"):
                self.url = url
                return
    
            # Support for unicode domain names and paths.
            try:
                scheme, auth, host, port, path, query, fragment = parse_url(url)
            except LocationParseError as e:
                raise InvalidURL(*e.args)
    
            if not scheme:
                raise MissingSchema(
                    f"Invalid URL {url!r}: No scheme supplied. "
                    f"Perhaps you meant https://{url}?"
                )
    
            if not host:
                raise InvalidURL(f"Invalid URL {url!r}: No host supplied")
    
            # In general, we want to try IDNA encoding the hostname if the string contains
            # non-ASCII characters. This allows users to automatically get the correct IDNA
            # behaviour. For strings containing only ASCII characters, we need to also verify
            # it doesn't start with a wildcard (*), before allowing the unencoded hostname.
            if not unicode_is_ascii(host):
                try:
                    host = self._get_idna_encoded_host(host)
                except UnicodeError:
                    raise InvalidURL("URL has an invalid label.")
            elif host.startswith(("*", ".")):
                raise InvalidURL("URL has an invalid label.")
    
            # Carefully reconstruct the network location
            netloc = auth or ""
            if netloc:
                netloc += "@"
            netloc += host
            if port:
                netloc += f":{port}"
    
            # Bare domains aren't valid URLs.
            if not path:
                path = "/"
    
            if isinstance(params, (str, bytes)):
                params = to_native_string(params)
    
            enc_params = self._encode_params(params)
            if enc_params:
                if query:
                    query = f"{query}&{enc_params}"
                else:
                    query = enc_params
    
            url = requote_uri(urlunparse([scheme, netloc, path, None, query, fragment]))
            self.url = url
    
    ```
      </details>

    </details>

    <details>
      <summary><b>register_hook</b></summary>
  - **Signature**: `def register_hook(self, event, hook):`
  - **Documentation**: Properly register a hook.

      <details>
        <summary>Source Code</summary>
    ```python
        def register_hook(self, event, hook):
            """Properly register a hook."""
    
            if event not in self.hooks:
                raise ValueError(f'Unsupported event specified, with event name "{event}"')
    
            if isinstance(hook, Callable):
                self.hooks[event].append(hook)
            elif hasattr(hook, "__iter__"):
                self.hooks[event].extend(h for h in hook if isinstance(h, Callable))
    
    ```
      </details>

    </details>

  </details>

  <details>
    <summary><b>ReadTimeout</b></summary>
    <details>
      <summary>class ReadTimeout:</summary>
    - **Documentation**: The server did not send any data in the allotted amount of time.
    </details>

    <details>
      <summary><b>__init__</b></summary>
  - **Signature**: `def __init__(self, *args, **kwargs):`
  - **Documentation**: Initialize RequestException with `request` and `response` objects.

      <details>
        <summary>Source Code</summary>
    ```python
        def __init__(self, *args, **kwargs):
            """Initialize RequestException with `request` and `response` objects."""
            response = kwargs.pop("response", None)
            self.response = response
            self.request = kwargs.pop("request", None)
            if response is not None and not self.request and hasattr(response, "request"):
                self.request = self.response.request
            super().__init__(*args, **kwargs)
    
    ```
      </details>

    </details>

  </details>

  <details>
    <summary><b>Request</b></summary>
    <details>
      <summary>class Request:</summary>
    - **Documentation**: A user-created :class:`Request <Request>` object.

Used to prepare a :class:`PreparedRequest <PreparedRequest>`, which is sent to the server.

:param method: HTTP method to use.
:param url: URL to send.
:param headers: dictionary of headers to send.
:param files: dictionary of {filename: fileobject} files to multipart upload.
:param data: the body to attach to the request. If a dictionary or
    list of tuples ``[(key, value)]`` is provided, form-encoding will
    take place.
:param json: json for the body to attach to the request (if files or data is not specified).
:param params: URL parameters to append to the URL. If a dictionary or
    list of tuples ``[(key, value)]`` is provided, form-encoding will
    take place.
:param auth: Auth handler or (user, pass) tuple.
:param cookies: dictionary or CookieJar of cookies to attach to this request.
:param hooks: dictionary of callback hooks, for internal usage.

Usage::

  >>> import requests
  >>> req = requests.Request('GET', 'https://httpbin.org/get')
  >>> req.prepare()
  <PreparedRequest [GET]>
    </details>

    <details>
      <summary><b>__init__</b></summary>
  - **Signature**: `def __init__(self, method=None, url=None, headers=None, files=None, data=None, params=None, auth=None, cookies=None, hooks=None, json=None):`
  - **Documentation**: Initialize self.  See help(type(self)) for accurate signature.

      <details>
        <summary>Source Code</summary>
    ```python
        def __init__(
            self,
            method=None,
            url=None,
            headers=None,
            files=None,
            data=None,
            params=None,
            auth=None,
            cookies=None,
            hooks=None,
            json=None,
        ):
            # Default empty dicts for dict params.
            data = [] if data is None else data
            files = [] if files is None else files
            headers = {} if headers is None else headers
            params = {} if params is None else params
            hooks = {} if hooks is None else hooks
    
            self.hooks = default_hooks()
            for k, v in list(hooks.items()):
                self.register_hook(event=k, hook=v)
    
            self.method = method
            self.url = url
            self.headers = headers
            self.files = files
            self.data = data
            self.json = json
            self.params = params
            self.auth = auth
            self.cookies = cookies
    
    ```
      </details>

    </details>

    <details>
      <summary><b>__repr__</b></summary>
  - **Signature**: `def __repr__(self):`
  - **Documentation**: Return repr(self).

      <details>
        <summary>Source Code</summary>
    ```python
        def __repr__(self):
            return f"<Request [{self.method}]>"
    
    ```
      </details>

    </details>

    <details>
      <summary><b>deregister_hook</b></summary>
  - **Signature**: `def deregister_hook(self, event, hook):`
  - **Documentation**: Deregister a previously registered hook.
Returns True if the hook existed, False if not.

      <details>
        <summary>Source Code</summary>
    ```python
        def deregister_hook(self, event, hook):
            """Deregister a previously registered hook.
            Returns True if the hook existed, False if not.
            """
    
            try:
                self.hooks[event].remove(hook)
                return True
            except ValueError:
                return False
    
    ```
      </details>

    </details>

    <details>
      <summary><b>prepare</b></summary>
  - **Signature**: `def prepare(self):`
  - **Documentation**: Constructs a :class:`PreparedRequest <PreparedRequest>` for transmission and returns it.

      <details>
        <summary>Source Code</summary>
    ```python
        def prepare(self):
            """Constructs a :class:`PreparedRequest <PreparedRequest>` for transmission and returns it."""
            p = PreparedRequest()
            p.prepare(
                method=self.method,
                url=self.url,
                headers=self.headers,
                files=self.files,
                data=self.data,
                json=self.json,
                params=self.params,
                auth=self.auth,
                cookies=self.cookies,
                hooks=self.hooks,
            )
            return p
    
    ```
      </details>

    </details>

    <details>
      <summary><b>register_hook</b></summary>
  - **Signature**: `def register_hook(self, event, hook):`
  - **Documentation**: Properly register a hook.

      <details>
        <summary>Source Code</summary>
    ```python
        def register_hook(self, event, hook):
            """Properly register a hook."""
    
            if event not in self.hooks:
                raise ValueError(f'Unsupported event specified, with event name "{event}"')
    
            if isinstance(hook, Callable):
                self.hooks[event].append(hook)
            elif hasattr(hook, "__iter__"):
                self.hooks[event].extend(h for h in hook if isinstance(h, Callable))
    
    ```
      </details>

    </details>

  </details>

  <details>
    <summary><b>RequestException</b></summary>
    <details>
      <summary>class RequestException:</summary>
    - **Documentation**: There was an ambiguous exception that occurred while handling your
request.
    </details>

    <details>
      <summary><b>__init__</b></summary>
  - **Signature**: `def __init__(self, *args, **kwargs):`
  - **Documentation**: Initialize RequestException with `request` and `response` objects.

      <details>
        <summary>Source Code</summary>
    ```python
        def __init__(self, *args, **kwargs):
            """Initialize RequestException with `request` and `response` objects."""
            response = kwargs.pop("response", None)
            self.response = response
            self.request = kwargs.pop("request", None)
            if response is not None and not self.request and hasattr(response, "request"):
                self.request = self.response.request
            super().__init__(*args, **kwargs)
    
    ```
      </details>

    </details>

  </details>

  <details>
    <summary><b>RequestsDependencyWarning</b></summary>
    <details>
      <summary>class RequestsDependencyWarning:</summary>
    - **Documentation**: An imported dependency doesn't match the expected version range.
    </details>

  </details>

  <details>
    <summary><b>Response</b></summary>
    <details>
      <summary>class Response:</summary>
    - **Documentation**: The :class:`Response <Response>` object, which contains a
server's response to an HTTP request.
    </details>

    <details>
      <summary><b>__bool__</b></summary>
  - **Signature**: `def __bool__(self):`
  - **Documentation**: Returns True if :attr:`status_code` is less than 400.

This attribute checks if the status code of the response is between
400 and 600 to see if there was a client error or a server error. If
the status code, is between 200 and 400, this will return True. This
is **not** a check to see if the response code is ``200 OK``.

      <details>
        <summary>Source Code</summary>
    ```python
        def __bool__(self):
            """Returns True if :attr:`status_code` is less than 400.
    
            This attribute checks if the status code of the response is between
            400 and 600 to see if there was a client error or a server error. If
            the status code, is between 200 and 400, this will return True. This
            is **not** a check to see if the response code is ``200 OK``.
            """
            return self.ok
    
    ```
      </details>

    </details>

    <details>
      <summary><b>__enter__</b></summary>
  - **Signature**: `def __enter__(self):`
  - **Documentation**: No documentation provided.

      <details>
        <summary>Source Code</summary>
    ```python
        def __enter__(self):
            return self
    
    ```
      </details>

    </details>

    <details>
      <summary><b>__exit__</b></summary>
  - **Signature**: `def __exit__(self, *args):`
  - **Documentation**: No documentation provided.

      <details>
        <summary>Source Code</summary>
    ```python
        def __exit__(self, *args):
            self.close()
    
    ```
      </details>

    </details>

    <details>
      <summary><b>__getstate__</b></summary>
  - **Signature**: `def __getstate__(self):`
  - **Documentation**: Helper for pickle.

      <details>
        <summary>Source Code</summary>
    ```python
        def __getstate__(self):
            # Consume everything; accessing the content attribute makes
            # sure the content has been fully read.
            if not self._content_consumed:
                self.content
    
            return {attr: getattr(self, attr, None) for attr in self.__attrs__}
    
    ```
      </details>

    </details>

    <details>
      <summary><b>__init__</b></summary>
  - **Signature**: `def __init__(self):`
  - **Documentation**: Initialize self.  See help(type(self)) for accurate signature.

      <details>
        <summary>Source Code</summary>
    ```python
        def __init__(self):
            self._content = False
            self._content_consumed = False
            self._next = None
    
            #: Integer Code of responded HTTP Status, e.g. 404 or 200.
            self.status_code = None
    
            #: Case-insensitive Dictionary of Response Headers.
            #: For example, ``headers['content-encoding']`` will return the
            #: value of a ``'Content-Encoding'`` response header.
            self.headers = CaseInsensitiveDict()
    
            #: File-like object representation of response (for advanced usage).
            #: Use of ``raw`` requires that ``stream=True`` be set on the request.
            #: This requirement does not apply for use internally to Requests.
            self.raw = None
    
            #: Final URL location of Response.
            self.url = None
    
            #: Encoding to decode with when accessing r.text.
            self.encoding = None
    
            #: A list of :class:`Response <Response>` objects from
            #: the history of the Request. Any redirect responses will end
            #: up here. The list is sorted from the oldest to the most recent request.
            self.history = []
    
            #: Textual reason of responded HTTP Status, e.g. "Not Found" or "OK".
            self.reason = None
    
            #: A CookieJar of Cookies the server sent back.
            self.cookies = cookiejar_from_dict({})
    
            #: The amount of time elapsed between sending the request
            #: and the arrival of the response (as a timedelta).
            #: This property specifically measures the time taken between sending
            #: the first byte of the request and finishing parsing the headers. It
            #: is therefore unaffected by consuming the response content or the
            #: value of the ``stream`` keyword argument.
            self.elapsed = datetime.timedelta(0)
    
            #: The :class:`PreparedRequest <PreparedRequest>` object to which this
            #: is a response.
            self.request = None
    
    ```
      </details>

    </details>

    <details>
      <summary><b>__iter__</b></summary>
  - **Signature**: `def __iter__(self):`
  - **Documentation**: Allows you to use a response as an iterator.

      <details>
        <summary>Source Code</summary>
    ```python
        def __iter__(self):
            """Allows you to use a response as an iterator."""
            return self.iter_content(128)
    
    ```
      </details>

    </details>

    <details>
      <summary><b>__nonzero__</b></summary>
  - **Signature**: `def __nonzero__(self):`
  - **Documentation**: Returns True if :attr:`status_code` is less than 400.

This attribute checks if the status code of the response is between
400 and 600 to see if there was a client error or a server error. If
the status code, is between 200 and 400, this will return True. This
is **not** a check to see if the response code is ``200 OK``.

      <details>
        <summary>Source Code</summary>
    ```python
        def __nonzero__(self):
            """Returns True if :attr:`status_code` is less than 400.
    
            This attribute checks if the status code of the response is between
            400 and 600 to see if there was a client error or a server error. If
            the status code, is between 200 and 400, this will return True. This
            is **not** a check to see if the response code is ``200 OK``.
            """
            return self.ok
    
    ```
      </details>

    </details>

    <details>
      <summary><b>__repr__</b></summary>
  - **Signature**: `def __repr__(self):`
  - **Documentation**: Return repr(self).

      <details>
        <summary>Source Code</summary>
    ```python
        def __repr__(self):
            return f"<Response [{self.status_code}]>"
    
    ```
      </details>

    </details>

    <details>
      <summary><b>__setstate__</b></summary>
  - **Signature**: `def __setstate__(self, state):`
  - **Documentation**: No documentation provided.

      <details>
        <summary>Source Code</summary>
    ```python
        def __setstate__(self, state):
            for name, value in state.items():
                setattr(self, name, value)
    
            # pickled objects do not have .raw
            setattr(self, "_content_consumed", True)
            setattr(self, "raw", None)
    
    ```
      </details>

    </details>

    <details>
      <summary><b>close</b></summary>
  - **Signature**: `def close(self):`
  - **Documentation**: Releases the connection back to the pool. Once this method has been
called the underlying ``raw`` object must not be accessed again.

*Note: Should not normally need to be called explicitly.*

      <details>
        <summary>Source Code</summary>
    ```python
        def close(self):
            """Releases the connection back to the pool. Once this method has been
            called the underlying ``raw`` object must not be accessed again.
    
            *Note: Should not normally need to be called explicitly.*
            """
            if not self._content_consumed:
                self.raw.close()
    
            release_conn = getattr(self.raw, "release_conn", None)
            if release_conn is not None:
                release_conn()
    
    ```
      </details>

    </details>

    <details>
      <summary><b>iter_content</b></summary>
  - **Signature**: `def iter_content(self, chunk_size=1, decode_unicode=False):`
  - **Documentation**: Iterates over the response data.  When stream=True is set on the
request, this avoids reading the content at once into memory for
large responses.  The chunk size is the number of bytes it should
read into memory.  This is not necessarily the length of each item
returned as decoding can take place.

chunk_size must be of type int or None. A value of None will
function differently depending on the value of `stream`.
stream=True will read data as it arrives in whatever size the
chunks are received. If stream=False, data is returned as
a single chunk.

If decode_unicode is True, content will be decoded using the best
available encoding based on the response.

      <details>
        <summary>Source Code</summary>
    ```python
        def iter_content(self, chunk_size=1, decode_unicode=False):
            """Iterates over the response data.  When stream=True is set on the
            request, this avoids reading the content at once into memory for
            large responses.  The chunk size is the number of bytes it should
            read into memory.  This is not necessarily the length of each item
            returned as decoding can take place.
    
            chunk_size must be of type int or None. A value of None will
            function differently depending on the value of `stream`.
            stream=True will read data as it arrives in whatever size the
            chunks are received. If stream=False, data is returned as
            a single chunk.
    
            If decode_unicode is True, content will be decoded using the best
            available encoding based on the response.
            """
    
            def generate():
                # Special case for urllib3.
                if hasattr(self.raw, "stream"):
                    try:
                        yield from self.raw.stream(chunk_size, decode_content=True)
                    except ProtocolError as e:
                        raise ChunkedEncodingError(e)
                    except DecodeError as e:
                        raise ContentDecodingError(e)
                    except ReadTimeoutError as e:
                        raise ConnectionError(e)
                    except SSLError as e:
                        raise RequestsSSLError(e)
                else:
                    # Standard file-like object.
                    while True:
                        chunk = self.raw.read(chunk_size)
                        if not chunk:
                            break
                        yield chunk
    
                self._content_consumed = True
    
            if self._content_consumed and isinstance(self._content, bool):
                raise StreamConsumedError()
            elif chunk_size is not None and not isinstance(chunk_size, int):
                raise TypeError(
                    f"chunk_size must be an int, it is instead a {type(chunk_size)}."
                )
            # simulate reading small chunks of the content
            reused_chunks = iter_slices(self._content, chunk_size)
    
            stream_chunks = generate()
    
            chunks = reused_chunks if self._content_consumed else stream_chunks
    
            if decode_unicode:
                chunks = stream_decode_response_unicode(chunks, self)
    
            return chunks
    
    ```
      </details>

    </details>

    <details>
      <summary><b>iter_lines</b></summary>
  - **Signature**: `def iter_lines(self, chunk_size=512, decode_unicode=False, delimiter=None):`
  - **Documentation**: Iterates over the response data, one line at a time.  When
stream=True is set on the request, this avoids reading the
content at once into memory for large responses.

.. note:: This method is not reentrant safe.

      <details>
        <summary>Source Code</summary>
    ```python
        def iter_lines(
            self, chunk_size=ITER_CHUNK_SIZE, decode_unicode=False, delimiter=None
        ):
            """Iterates over the response data, one line at a time.  When
            stream=True is set on the request, this avoids reading the
            content at once into memory for large responses.
    
            .. note:: This method is not reentrant safe.
            """
    
            pending = None
    
            for chunk in self.iter_content(
                chunk_size=chunk_size, decode_unicode=decode_unicode
            ):
                if pending is not None:
                    chunk = pending + chunk
    
                if delimiter:
                    lines = chunk.split(delimiter)
                else:
                    lines = chunk.splitlines()
    
                if lines and lines[-1] and chunk and lines[-1][-1] == chunk[-1]:
                    pending = lines.pop()
                else:
                    pending = None
    
                yield from lines
    
            if pending is not None:
                yield pending
    
    ```
      </details>

    </details>

    <details>
      <summary><b>json</b></summary>
  - **Signature**: `def json(self, **kwargs):`
  - **Documentation**: Returns the json-encoded content of a response, if any.

:param \*\*kwargs: Optional arguments that ``json.loads`` takes.
:raises requests.exceptions.JSONDecodeError: If the response body does not
    contain valid json.

      <details>
        <summary>Source Code</summary>
    ```python
        def json(self, **kwargs):
            r"""Returns the json-encoded content of a response, if any.
    
            :param \*\*kwargs: Optional arguments that ``json.loads`` takes.
            :raises requests.exceptions.JSONDecodeError: If the response body does not
                contain valid json.
            """
    
            if not self.encoding and self.content and len(self.content) > 3:
                # No encoding set. JSON RFC 4627 section 3 states we should expect
                # UTF-8, -16 or -32. Detect which one to use; If the detection or
                # decoding fails, fall back to `self.text` (using charset_normalizer to make
                # a best guess).
                encoding = guess_json_utf(self.content)
                if encoding is not None:
                    try:
                        return complexjson.loads(self.content.decode(encoding), **kwargs)
                    except UnicodeDecodeError:
                        # Wrong UTF codec detected; usually because it's not UTF-8
                        # but some other 8-bit codec.  This is an RFC violation,
                        # and the server didn't bother to tell us what codec *was*
                        # used.
                        pass
                    except JSONDecodeError as e:
                        raise RequestsJSONDecodeError(e.msg, e.doc, e.pos)
    
            try:
                return complexjson.loads(self.text, **kwargs)
            except JSONDecodeError as e:
                # Catch JSON-related errors and raise as requests.JSONDecodeError
                # This aliases json.JSONDecodeError and simplejson.JSONDecodeError
                raise RequestsJSONDecodeError(e.msg, e.doc, e.pos)
    
    ```
      </details>

    </details>

    <details>
      <summary><b>raise_for_status</b></summary>
  - **Signature**: `def raise_for_status(self):`
  - **Documentation**: Raises :class:`HTTPError`, if one occurred.

      <details>
        <summary>Source Code</summary>
    ```python
        def raise_for_status(self):
            """Raises :class:`HTTPError`, if one occurred."""
    
            http_error_msg = ""
            if isinstance(self.reason, bytes):
                # We attempt to decode utf-8 first because some servers
                # choose to localize their reason strings. If the string
                # isn't utf-8, we fall back to iso-8859-1 for all other
                # encodings. (See PR #3538)
                try:
                    reason = self.reason.decode("utf-8")
                except UnicodeDecodeError:
                    reason = self.reason.decode("iso-8859-1")
            else:
                reason = self.reason
    
            if 400 <= self.status_code < 500:
                http_error_msg = (
                    f"{self.status_code} Client Error: {reason} for url: {self.url}"
                )
    
            elif 500 <= self.status_code < 600:
                http_error_msg = (
                    f"{self.status_code} Server Error: {reason} for url: {self.url}"
                )
    
            if http_error_msg:
                raise HTTPError(http_error_msg, response=self)
    
    ```
      </details>

    </details>

  </details>

  <details>
    <summary><b>Session</b></summary>
    <details>
      <summary>class Session:</summary>
    - **Documentation**: A Requests session.

Provides cookie persistence, connection-pooling, and configuration.

Basic Usage::

  >>> import requests
  >>> s = requests.Session()
  >>> s.get('https://httpbin.org/get')
  <Response [200]>

Or as a context manager::

  >>> with requests.Session() as s:
  ...     s.get('https://httpbin.org/get')
  <Response [200]>
    </details>

    <details>
      <summary><b>__enter__</b></summary>
  - **Signature**: `def __enter__(self):`
  - **Documentation**: No documentation provided.

      <details>
        <summary>Source Code</summary>
    ```python
        def __enter__(self):
            return self
    
    ```
      </details>

    </details>

    <details>
      <summary><b>__exit__</b></summary>
  - **Signature**: `def __exit__(self, *args):`
  - **Documentation**: No documentation provided.

      <details>
        <summary>Source Code</summary>
    ```python
        def __exit__(self, *args):
            self.close()
    
    ```
      </details>

    </details>

    <details>
      <summary><b>__getstate__</b></summary>
  - **Signature**: `def __getstate__(self):`
  - **Documentation**: Helper for pickle.

      <details>
        <summary>Source Code</summary>
    ```python
        def __getstate__(self):
            state = {attr: getattr(self, attr, None) for attr in self.__attrs__}
            return state
    
    ```
      </details>

    </details>

    <details>
      <summary><b>__init__</b></summary>
  - **Signature**: `def __init__(self):`
  - **Documentation**: Initialize self.  See help(type(self)) for accurate signature.

      <details>
        <summary>Source Code</summary>
    ```python
        def __init__(self):
            #: A case-insensitive dictionary of headers to be sent on each
            #: :class:`Request <Request>` sent from this
            #: :class:`Session <Session>`.
            self.headers = default_headers()
    
            #: Default Authentication tuple or object to attach to
            #: :class:`Request <Request>`.
            self.auth = None
    
            #: Dictionary mapping protocol or protocol and host to the URL of the proxy
            #: (e.g. {'http': 'foo.bar:3128', 'http://host.name': 'foo.bar:4012'}) to
            #: be used on each :class:`Request <Request>`.
            self.proxies = {}
    
            #: Event-handling hooks.
            self.hooks = default_hooks()
    
            #: Dictionary of querystring data to attach to each
            #: :class:`Request <Request>`. The dictionary values may be lists for
            #: representing multivalued query parameters.
            self.params = {}
    
            #: Stream response content default.
            self.stream = False
    
            #: SSL Verification default.
            #: Defaults to `True`, requiring requests to verify the TLS certificate at the
            #: remote end.
            #: If verify is set to `False`, requests will accept any TLS certificate
            #: presented by the server, and will ignore hostname mismatches and/or
            #: expired certificates, which will make your application vulnerable to
            #: man-in-the-middle (MitM) attacks.
            #: Only set this to `False` for testing.
            self.verify = True
    
            #: SSL client certificate default, if String, path to ssl client
            #: cert file (.pem). If Tuple, ('cert', 'key') pair.
            self.cert = None
    
            #: Maximum number of redirects allowed. If the request exceeds this
            #: limit, a :class:`TooManyRedirects` exception is raised.
            #: This defaults to requests.models.DEFAULT_REDIRECT_LIMIT, which is
            #: 30.
            self.max_redirects = DEFAULT_REDIRECT_LIMIT
    
            #: Trust environment settings for proxy configuration, default
            #: authentication and similar.
            self.trust_env = True
    
            #: A CookieJar containing all currently outstanding cookies set on this
            #: session. By default it is a
            #: :class:`RequestsCookieJar <requests.cookies.RequestsCookieJar>`, but
            #: may be any other ``cookielib.CookieJar`` compatible object.
            self.cookies = cookiejar_from_dict({})
    
            # Default connection adapters.
            self.adapters = OrderedDict()
            self.mount("https://", HTTPAdapter())
            self.mount("http://", HTTPAdapter())
    
    ```
      </details>

    </details>

    <details>
      <summary><b>__setstate__</b></summary>
  - **Signature**: `def __setstate__(self, state):`
  - **Documentation**: No documentation provided.

      <details>
        <summary>Source Code</summary>
    ```python
        def __setstate__(self, state):
            for attr, value in state.items():
                setattr(self, attr, value)
    
    ```
      </details>

    </details>

    <details>
      <summary><b>close</b></summary>
  - **Signature**: `def close(self):`
  - **Documentation**: Closes all adapters and as such the session

      <details>
        <summary>Source Code</summary>
    ```python
        def close(self):
            """Closes all adapters and as such the session"""
            for v in self.adapters.values():
                v.close()
    
    ```
      </details>

    </details>

    <details>
      <summary><b>delete</b></summary>
  - **Signature**: `def delete(self, url, **kwargs):`
  - **Documentation**: Sends a DELETE request. Returns :class:`Response` object.

:param url: URL for the new :class:`Request` object.
:param \*\*kwargs: Optional arguments that ``request`` takes.
:rtype: requests.Response

      <details>
        <summary>Source Code</summary>
    ```python
        def delete(self, url, **kwargs):
            r"""Sends a DELETE request. Returns :class:`Response` object.
    
            :param url: URL for the new :class:`Request` object.
            :param \*\*kwargs: Optional arguments that ``request`` takes.
            :rtype: requests.Response
            """
    
            return self.request("DELETE", url, **kwargs)
    
    ```
      </details>

    </details>

    <details>
      <summary><b>get</b></summary>
  - **Signature**: `def get(self, url, **kwargs):`
  - **Documentation**: Sends a GET request. Returns :class:`Response` object.

:param url: URL for the new :class:`Request` object.
:param \*\*kwargs: Optional arguments that ``request`` takes.
:rtype: requests.Response

      <details>
        <summary>Source Code</summary>
    ```python
        def get(self, url, **kwargs):
            r"""Sends a GET request. Returns :class:`Response` object.
    
            :param url: URL for the new :class:`Request` object.
            :param \*\*kwargs: Optional arguments that ``request`` takes.
            :rtype: requests.Response
            """
    
            kwargs.setdefault("allow_redirects", True)
            return self.request("GET", url, **kwargs)
    
    ```
      </details>

    </details>

    <details>
      <summary><b>get_adapter</b></summary>
  - **Signature**: `def get_adapter(self, url):`
  - **Documentation**: Returns the appropriate connection adapter for the given URL.

:rtype: requests.adapters.BaseAdapter

      <details>
        <summary>Source Code</summary>
    ```python
        def get_adapter(self, url):
            """
            Returns the appropriate connection adapter for the given URL.
    
            :rtype: requests.adapters.BaseAdapter
            """
            for prefix, adapter in self.adapters.items():
                if url.lower().startswith(prefix.lower()):
                    return adapter
    
            # Nothing matches :-/
            raise InvalidSchema(f"No connection adapters were found for {url!r}")
    
    ```
      </details>

    </details>

    <details>
      <summary><b>get_redirect_target</b></summary>
  - **Signature**: `def get_redirect_target(self, resp):`
  - **Documentation**: Receives a Response. Returns a redirect URI or ``None``

      <details>
        <summary>Source Code</summary>
    ```python
        def get_redirect_target(self, resp):
            """Receives a Response. Returns a redirect URI or ``None``"""
            # Due to the nature of how requests processes redirects this method will
            # be called at least once upon the original response and at least twice
            # on each subsequent redirect response (if any).
            # If a custom mixin is used to handle this logic, it may be advantageous
            # to cache the redirect location onto the response object as a private
            # attribute.
            if resp.is_redirect:
                location = resp.headers["location"]
                # Currently the underlying http module on py3 decode headers
                # in latin1, but empirical evidence suggests that latin1 is very
                # rarely used with non-ASCII characters in HTTP headers.
                # It is more likely to get UTF8 header rather than latin1.
                # This causes incorrect handling of UTF8 encoded location headers.
                # To solve this, we re-encode the location in latin1.
                location = location.encode("latin1")
                return to_native_string(location, "utf8")
            return None
    
    ```
      </details>

    </details>

    <details>
      <summary><b>head</b></summary>
  - **Signature**: `def head(self, url, **kwargs):`
  - **Documentation**: Sends a HEAD request. Returns :class:`Response` object.

:param url: URL for the new :class:`Request` object.
:param \*\*kwargs: Optional arguments that ``request`` takes.
:rtype: requests.Response

      <details>
        <summary>Source Code</summary>
    ```python
        def head(self, url, **kwargs):
            r"""Sends a HEAD request. Returns :class:`Response` object.
    
            :param url: URL for the new :class:`Request` object.
            :param \*\*kwargs: Optional arguments that ``request`` takes.
            :rtype: requests.Response
            """
    
            kwargs.setdefault("allow_redirects", False)
            return self.request("HEAD", url, **kwargs)
    
    ```
      </details>

    </details>

    <details>
      <summary><b>merge_environment_settings</b></summary>
  - **Signature**: `def merge_environment_settings(self, url, proxies, stream, verify, cert):`
  - **Documentation**: Check the environment and merge it with some settings.

:rtype: dict

      <details>
        <summary>Source Code</summary>
    ```python
        def merge_environment_settings(self, url, proxies, stream, verify, cert):
            """
            Check the environment and merge it with some settings.
    
            :rtype: dict
            """
            # Gather clues from the surrounding environment.
            if self.trust_env:
                # Set environment's proxies.
                no_proxy = proxies.get("no_proxy") if proxies is not None else None
                env_proxies = get_environ_proxies(url, no_proxy=no_proxy)
                for k, v in env_proxies.items():
                    proxies.setdefault(k, v)
    
                # Look for requests environment configuration
                # and be compatible with cURL.
                if verify is True or verify is None:
                    verify = (
                        os.environ.get("REQUESTS_CA_BUNDLE")
                        or os.environ.get("CURL_CA_BUNDLE")
                        or verify
                    )
    
            # Merge all the kwargs.
            proxies = merge_setting(proxies, self.proxies)
            stream = merge_setting(stream, self.stream)
            verify = merge_setting(verify, self.verify)
            cert = merge_setting(cert, self.cert)
    
            return {"proxies": proxies, "stream": stream, "verify": verify, "cert": cert}
    
    ```
      </details>

    </details>

    <details>
      <summary><b>mount</b></summary>
  - **Signature**: `def mount(self, prefix, adapter):`
  - **Documentation**: Registers a connection adapter to a prefix.

Adapters are sorted in descending order by prefix length.

      <details>
        <summary>Source Code</summary>
    ```python
        def mount(self, prefix, adapter):
            """Registers a connection adapter to a prefix.
    
            Adapters are sorted in descending order by prefix length.
            """
            self.adapters[prefix] = adapter
            keys_to_move = [k for k in self.adapters if len(k) < len(prefix)]
    
            for key in keys_to_move:
                self.adapters[key] = self.adapters.pop(key)
    
    ```
      </details>

    </details>

    <details>
      <summary><b>options</b></summary>
  - **Signature**: `def options(self, url, **kwargs):`
  - **Documentation**: Sends a OPTIONS request. Returns :class:`Response` object.

:param url: URL for the new :class:`Request` object.
:param \*\*kwargs: Optional arguments that ``request`` takes.
:rtype: requests.Response

      <details>
        <summary>Source Code</summary>
    ```python
        def options(self, url, **kwargs):
            r"""Sends a OPTIONS request. Returns :class:`Response` object.
    
            :param url: URL for the new :class:`Request` object.
            :param \*\*kwargs: Optional arguments that ``request`` takes.
            :rtype: requests.Response
            """
    
            kwargs.setdefault("allow_redirects", True)
            return self.request("OPTIONS", url, **kwargs)
    
    ```
      </details>

    </details>

    <details>
      <summary><b>patch</b></summary>
  - **Signature**: `def patch(self, url, data=None, **kwargs):`
  - **Documentation**: Sends a PATCH request. Returns :class:`Response` object.

:param url: URL for the new :class:`Request` object.
:param data: (optional) Dictionary, list of tuples, bytes, or file-like
    object to send in the body of the :class:`Request`.
:param \*\*kwargs: Optional arguments that ``request`` takes.
:rtype: requests.Response

      <details>
        <summary>Source Code</summary>
    ```python
        def patch(self, url, data=None, **kwargs):
            r"""Sends a PATCH request. Returns :class:`Response` object.
    
            :param url: URL for the new :class:`Request` object.
            :param data: (optional) Dictionary, list of tuples, bytes, or file-like
                object to send in the body of the :class:`Request`.
            :param \*\*kwargs: Optional arguments that ``request`` takes.
            :rtype: requests.Response
            """
    
            return self.request("PATCH", url, data=data, **kwargs)
    
    ```
      </details>

    </details>

    <details>
      <summary><b>post</b></summary>
  - **Signature**: `def post(self, url, data=None, json=None, **kwargs):`
  - **Documentation**: Sends a POST request. Returns :class:`Response` object.

:param url: URL for the new :class:`Request` object.
:param data: (optional) Dictionary, list of tuples, bytes, or file-like
    object to send in the body of the :class:`Request`.
:param json: (optional) json to send in the body of the :class:`Request`.
:param \*\*kwargs: Optional arguments that ``request`` takes.
:rtype: requests.Response

      <details>
        <summary>Source Code</summary>
    ```python
        def post(self, url, data=None, json=None, **kwargs):
            r"""Sends a POST request. Returns :class:`Response` object.
    
            :param url: URL for the new :class:`Request` object.
            :param data: (optional) Dictionary, list of tuples, bytes, or file-like
                object to send in the body of the :class:`Request`.
            :param json: (optional) json to send in the body of the :class:`Request`.
            :param \*\*kwargs: Optional arguments that ``request`` takes.
            :rtype: requests.Response
            """
    
            return self.request("POST", url, data=data, json=json, **kwargs)
    
    ```
      </details>

    </details>

    <details>
      <summary><b>prepare_request</b></summary>
  - **Signature**: `def prepare_request(self, request):`
  - **Documentation**: Constructs a :class:`PreparedRequest <PreparedRequest>` for
transmission and returns it. The :class:`PreparedRequest` has settings
merged from the :class:`Request <Request>` instance and those of the
:class:`Session`.

:param request: :class:`Request` instance to prepare with this
    session's settings.
:rtype: requests.PreparedRequest

      <details>
        <summary>Source Code</summary>
    ```python
        def prepare_request(self, request):
            """Constructs a :class:`PreparedRequest <PreparedRequest>` for
            transmission and returns it. The :class:`PreparedRequest` has settings
            merged from the :class:`Request <Request>` instance and those of the
            :class:`Session`.
    
            :param request: :class:`Request` instance to prepare with this
                session's settings.
            :rtype: requests.PreparedRequest
            """
            cookies = request.cookies or {}
    
            # Bootstrap CookieJar.
            if not isinstance(cookies, cookielib.CookieJar):
                cookies = cookiejar_from_dict(cookies)
    
            # Merge with session cookies
            merged_cookies = merge_cookies(
                merge_cookies(RequestsCookieJar(), self.cookies), cookies
            )
    
            # Set environment's basic authentication if not explicitly set.
            auth = request.auth
            if self.trust_env and not auth and not self.auth:
                auth = get_netrc_auth(request.url)
    
            p = PreparedRequest()
            p.prepare(
                method=request.method.upper(),
                url=request.url,
                files=request.files,
                data=request.data,
                json=request.json,
                headers=merge_setting(
                    request.headers, self.headers, dict_class=CaseInsensitiveDict
                ),
                params=merge_setting(request.params, self.params),
                auth=merge_setting(auth, self.auth),
                cookies=merged_cookies,
                hooks=merge_hooks(request.hooks, self.hooks),
            )
            return p
    
    ```
      </details>

    </details>

    <details>
      <summary><b>put</b></summary>
  - **Signature**: `def put(self, url, data=None, **kwargs):`
  - **Documentation**: Sends a PUT request. Returns :class:`Response` object.

:param url: URL for the new :class:`Request` object.
:param data: (optional) Dictionary, list of tuples, bytes, or file-like
    object to send in the body of the :class:`Request`.
:param \*\*kwargs: Optional arguments that ``request`` takes.
:rtype: requests.Response

      <details>
        <summary>Source Code</summary>
    ```python
        def put(self, url, data=None, **kwargs):
            r"""Sends a PUT request. Returns :class:`Response` object.
    
            :param url: URL for the new :class:`Request` object.
            :param data: (optional) Dictionary, list of tuples, bytes, or file-like
                object to send in the body of the :class:`Request`.
            :param \*\*kwargs: Optional arguments that ``request`` takes.
            :rtype: requests.Response
            """
    
            return self.request("PUT", url, data=data, **kwargs)
    
    ```
      </details>

    </details>

    <details>
      <summary><b>rebuild_auth</b></summary>
  - **Signature**: `def rebuild_auth(self, prepared_request, response):`
  - **Documentation**: When being redirected we may want to strip authentication from the
request to avoid leaking credentials. This method intelligently removes
and reapplies authentication where possible to avoid credential loss.

      <details>
        <summary>Source Code</summary>
    ```python
        def rebuild_auth(self, prepared_request, response):
            """When being redirected we may want to strip authentication from the
            request to avoid leaking credentials. This method intelligently removes
            and reapplies authentication where possible to avoid credential loss.
            """
            headers = prepared_request.headers
            url = prepared_request.url
    
            if "Authorization" in headers and self.should_strip_auth(
                response.request.url, url
            ):
                # If we get redirected to a new host, we should strip out any
                # authentication headers.
                del headers["Authorization"]
    
            # .netrc might have more auth for us on our new host.
            new_auth = get_netrc_auth(url) if self.trust_env else None
            if new_auth is not None:
                prepared_request.prepare_auth(new_auth)
    
    ```
      </details>

    </details>

    <details>
      <summary><b>rebuild_method</b></summary>
  - **Signature**: `def rebuild_method(self, prepared_request, response):`
  - **Documentation**: When being redirected we may want to change the method of the request
based on certain specs or browser behavior.

      <details>
        <summary>Source Code</summary>
    ```python
        def rebuild_method(self, prepared_request, response):
            """When being redirected we may want to change the method of the request
            based on certain specs or browser behavior.
            """
            method = prepared_request.method
    
            # https://tools.ietf.org/html/rfc7231#section-6.4.4
            if response.status_code == codes.see_other and method != "HEAD":
                method = "GET"
    
            # Do what the browsers do, despite standards...
            # First, turn 302s into GETs.
            if response.status_code == codes.found and method != "HEAD":
                method = "GET"
    
            # Second, if a POST is responded to with a 301, turn it into a GET.
            # This bizarre behaviour is explained in Issue 1704.
            if response.status_code == codes.moved and method == "POST":
                method = "GET"
    
            prepared_request.method = method
    
    ```
      </details>

    </details>

    <details>
      <summary><b>rebuild_proxies</b></summary>
  - **Signature**: `def rebuild_proxies(self, prepared_request, proxies):`
  - **Documentation**: This method re-evaluates the proxy configuration by considering the
environment variables. If we are redirected to a URL covered by
NO_PROXY, we strip the proxy configuration. Otherwise, we set missing
proxy keys for this URL (in case they were stripped by a previous
redirect).

This method also replaces the Proxy-Authorization header where
necessary.

:rtype: dict

      <details>
        <summary>Source Code</summary>
    ```python
        def rebuild_proxies(self, prepared_request, proxies):
            """This method re-evaluates the proxy configuration by considering the
            environment variables. If we are redirected to a URL covered by
            NO_PROXY, we strip the proxy configuration. Otherwise, we set missing
            proxy keys for this URL (in case they were stripped by a previous
            redirect).
    
            This method also replaces the Proxy-Authorization header where
            necessary.
    
            :rtype: dict
            """
            headers = prepared_request.headers
            scheme = urlparse(prepared_request.url).scheme
            new_proxies = resolve_proxies(prepared_request, proxies, self.trust_env)
    
            if "Proxy-Authorization" in headers:
                del headers["Proxy-Authorization"]
    
            try:
                username, password = get_auth_from_url(new_proxies[scheme])
            except KeyError:
                username, password = None, None
    
            # urllib3 handles proxy authorization for us in the standard adapter.
            # Avoid appending this to TLS tunneled requests where it may be leaked.
            if not scheme.startswith("https") and username and password:
                headers["Proxy-Authorization"] = _basic_auth_str(username, password)
    
            return new_proxies
    
    ```
      </details>

    </details>

    <details>
      <summary><b>request</b></summary>
  - **Signature**: `def request(self, method, url, params=None, data=None, headers=None, cookies=None, files=None, auth=None, timeout=None, allow_redirects=True, proxies=None, hooks=None, stream=None, verify=None, cert=None, json=None):`
  - **Documentation**: Constructs a :class:`Request <Request>`, prepares it and sends it.
Returns :class:`Response <Response>` object.

:param method: method for the new :class:`Request` object.
:param url: URL for the new :class:`Request` object.
:param params: (optional) Dictionary or bytes to be sent in the query
    string for the :class:`Request`.
:param data: (optional) Dictionary, list of tuples, bytes, or file-like
    object to send in the body of the :class:`Request`.
:param json: (optional) json to send in the body of the
    :class:`Request`.
:param headers: (optional) Dictionary of HTTP Headers to send with the
    :class:`Request`.
:param cookies: (optional) Dict or CookieJar object to send with the
    :class:`Request`.
:param files: (optional) Dictionary of ``'filename': file-like-objects``
    for multipart encoding upload.
:param auth: (optional) Auth tuple or callable to enable
    Basic/Digest/Custom HTTP Auth.
:param timeout: (optional) How long to wait for the server to send
    data before giving up, as a float, or a :ref:`(connect timeout,
    read timeout) <timeouts>` tuple.
:type timeout: float or tuple
:param allow_redirects: (optional) Set to True by default.
:type allow_redirects: bool
:param proxies: (optional) Dictionary mapping protocol or protocol and
    hostname to the URL of the proxy.
:param hooks: (optional) Dictionary mapping hook name to one event or
    list of events, event must be callable.
:param stream: (optional) whether to immediately download the response
    content. Defaults to ``False``.
:param verify: (optional) Either a boolean, in which case it controls whether we verify
    the server's TLS certificate, or a string, in which case it must be a path
    to a CA bundle to use. Defaults to ``True``. When set to
    ``False``, requests will accept any TLS certificate presented by
    the server, and will ignore hostname mismatches and/or expired
    certificates, which will make your application vulnerable to
    man-in-the-middle (MitM) attacks. Setting verify to ``False``
    may be useful during local development or testing.
:param cert: (optional) if String, path to ssl client cert file (.pem).
    If Tuple, ('cert', 'key') pair.
:rtype: requests.Response

      <details>
        <summary>Source Code</summary>
    ```python
        def request(
            self,
            method,
            url,
            params=None,
            data=None,
            headers=None,
            cookies=None,
            files=None,
            auth=None,
            timeout=None,
            allow_redirects=True,
            proxies=None,
            hooks=None,
            stream=None,
            verify=None,
            cert=None,
            json=None,
        ):
            """Constructs a :class:`Request <Request>`, prepares it and sends it.
            Returns :class:`Response <Response>` object.
    
            :param method: method for the new :class:`Request` object.
            :param url: URL for the new :class:`Request` object.
            :param params: (optional) Dictionary or bytes to be sent in the query
                string for the :class:`Request`.
            :param data: (optional) Dictionary, list of tuples, bytes, or file-like
                object to send in the body of the :class:`Request`.
            :param json: (optional) json to send in the body of the
                :class:`Request`.
            :param headers: (optional) Dictionary of HTTP Headers to send with the
                :class:`Request`.
            :param cookies: (optional) Dict or CookieJar object to send with the
                :class:`Request`.
            :param files: (optional) Dictionary of ``'filename': file-like-objects``
                for multipart encoding upload.
            :param auth: (optional) Auth tuple or callable to enable
                Basic/Digest/Custom HTTP Auth.
            :param timeout: (optional) How long to wait for the server to send
                data before giving up, as a float, or a :ref:`(connect timeout,
                read timeout) <timeouts>` tuple.
            :type timeout: float or tuple
            :param allow_redirects: (optional) Set to True by default.
            :type allow_redirects: bool
            :param proxies: (optional) Dictionary mapping protocol or protocol and
                hostname to the URL of the proxy.
            :param hooks: (optional) Dictionary mapping hook name to one event or
                list of events, event must be callable.
            :param stream: (optional) whether to immediately download the response
                content. Defaults to ``False``.
            :param verify: (optional) Either a boolean, in which case it controls whether we verify
                the server's TLS certificate, or a string, in which case it must be a path
                to a CA bundle to use. Defaults to ``True``. When set to
                ``False``, requests will accept any TLS certificate presented by
                the server, and will ignore hostname mismatches and/or expired
                certificates, which will make your application vulnerable to
                man-in-the-middle (MitM) attacks. Setting verify to ``False``
                may be useful during local development or testing.
            :param cert: (optional) if String, path to ssl client cert file (.pem).
                If Tuple, ('cert', 'key') pair.
            :rtype: requests.Response
            """
            # Create the Request.
            req = Request(
                method=method.upper(),
                url=url,
                headers=headers,
                files=files,
                data=data or {},
                json=json,
                params=params or {},
                auth=auth,
                cookies=cookies,
                hooks=hooks,
            )
            prep = self.prepare_request(req)
    
            proxies = proxies or {}
    
            settings = self.merge_environment_settings(
                prep.url, proxies, stream, verify, cert
            )
    
            # Send the request.
            send_kwargs = {
                "timeout": timeout,
                "allow_redirects": allow_redirects,
            }
            send_kwargs.update(settings)
            resp = self.send(prep, **send_kwargs)
    
            return resp
    
    ```
      </details>

    </details>

    <details>
      <summary><b>resolve_redirects</b></summary>
  - **Signature**: `def resolve_redirects(self, resp, req, stream=False, timeout=None, verify=True, cert=None, proxies=None, yield_requests=False, **adapter_kwargs):`
  - **Documentation**: Receives a Response. Returns a generator of Responses or Requests.

      <details>
        <summary>Source Code</summary>
    ```python
        def resolve_redirects(
            self,
            resp,
            req,
            stream=False,
            timeout=None,
            verify=True,
            cert=None,
            proxies=None,
            yield_requests=False,
            **adapter_kwargs,
        ):
            """Receives a Response. Returns a generator of Responses or Requests."""
    
            hist = []  # keep track of history
    
            url = self.get_redirect_target(resp)
            previous_fragment = urlparse(req.url).fragment
            while url:
                prepared_request = req.copy()
    
                # Update history and keep track of redirects.
                # resp.history must ignore the original request in this loop
                hist.append(resp)
                resp.history = hist[1:]
    
                try:
                    resp.content  # Consume socket so it can be released
                except (ChunkedEncodingError, ContentDecodingError, RuntimeError):
                    resp.raw.read(decode_content=False)
    
                if len(resp.history) >= self.max_redirects:
                    raise TooManyRedirects(
                        f"Exceeded {self.max_redirects} redirects.", response=resp
                    )
    
                # Release the connection back into the pool.
                resp.close()
    
                # Handle redirection without scheme (see: RFC 1808 Section 4)
                if url.startswith("//"):
                    parsed_rurl = urlparse(resp.url)
                    url = ":".join([to_native_string(parsed_rurl.scheme), url])
    
                # Normalize url case and attach previous fragment if needed (RFC 7231 7.1.2)
                parsed = urlparse(url)
                if parsed.fragment == "" and previous_fragment:
                    parsed = parsed._replace(fragment=previous_fragment)
                elif parsed.fragment:
                    previous_fragment = parsed.fragment
                url = parsed.geturl()
    
                # Facilitate relative 'location' headers, as allowed by RFC 7231.
                # (e.g. '/path/to/resource' instead of 'http://domain.tld/path/to/resource')
                # Compliant with RFC3986, we percent encode the url.
                if not parsed.netloc:
                    url = urljoin(resp.url, requote_uri(url))
                else:
                    url = requote_uri(url)
    
                prepared_request.url = to_native_string(url)
    
                self.rebuild_method(prepared_request, resp)
    
                # https://github.com/psf/requests/issues/1084
                if resp.status_code not in (
                    codes.temporary_redirect,
                    codes.permanent_redirect,
                ):
                    # https://github.com/psf/requests/issues/3490
                    purged_headers = ("Content-Length", "Content-Type", "Transfer-Encoding")
                    for header in purged_headers:
                        prepared_request.headers.pop(header, None)
                    prepared_request.body = None
    
                headers = prepared_request.headers
                headers.pop("Cookie", None)
    
                # Extract any cookies sent on the response to the cookiejar
                # in the new request. Because we've mutated our copied prepared
                # request, use the old one that we haven't yet touched.
                extract_cookies_to_jar(prepared_request._cookies, req, resp.raw)
                merge_cookies(prepared_request._cookies, self.cookies)
                prepared_request.prepare_cookies(prepared_request._cookies)
    
                # Rebuild auth and proxy information.
                proxies = self.rebuild_proxies(prepared_request, proxies)
                self.rebuild_auth(prepared_request, resp)
    
                # A failed tell() sets `_body_position` to `object()`. This non-None
                # value ensures `rewindable` will be True, allowing us to raise an
                # UnrewindableBodyError, instead of hanging the connection.
                rewindable = prepared_request._body_position is not None and (
                    "Content-Length" in headers or "Transfer-Encoding" in headers
                )
    
                # Attempt to rewind consumed file-like object.
                if rewindable:
                    rewind_body(prepared_request)
    
                # Override the original request.
                req = prepared_request
    
                if yield_requests:
                    yield req
                else:
                    resp = self.send(
                        req,
                        stream=stream,
                        timeout=timeout,
                        verify=verify,
                        cert=cert,
                        proxies=proxies,
                        allow_redirects=False,
                        **adapter_kwargs,
                    )
    
                    extract_cookies_to_jar(self.cookies, prepared_request, resp.raw)
    
                    # extract redirect url, if any, for the next loop
                    url = self.get_redirect_target(resp)
                    yield resp
    
    ```
      </details>

    </details>

    <details>
      <summary><b>send</b></summary>
  - **Signature**: `def send(self, request, **kwargs):`
  - **Documentation**: Send a given PreparedRequest.

:rtype: requests.Response

      <details>
        <summary>Source Code</summary>
    ```python
        def send(self, request, **kwargs):
            """Send a given PreparedRequest.
    
            :rtype: requests.Response
            """
            # Set defaults that the hooks can utilize to ensure they always have
            # the correct parameters to reproduce the previous request.
            kwargs.setdefault("stream", self.stream)
            kwargs.setdefault("verify", self.verify)
            kwargs.setdefault("cert", self.cert)
            if "proxies" not in kwargs:
                kwargs["proxies"] = resolve_proxies(request, self.proxies, self.trust_env)
    
            # It's possible that users might accidentally send a Request object.
            # Guard against that specific failure case.
            if isinstance(request, Request):
                raise ValueError("You can only send PreparedRequests.")
    
            # Set up variables needed for resolve_redirects and dispatching of hooks
            allow_redirects = kwargs.pop("allow_redirects", True)
            stream = kwargs.get("stream")
            hooks = request.hooks
    
            # Get the appropriate adapter to use
            adapter = self.get_adapter(url=request.url)
    
            # Start time (approximately) of the request
            start = preferred_clock()
    
            # Send the request
            r = adapter.send(request, **kwargs)
    
            # Total elapsed time of the request (approximately)
            elapsed = preferred_clock() - start
            r.elapsed = timedelta(seconds=elapsed)
    
            # Response manipulation hooks
            r = dispatch_hook("response", hooks, r, **kwargs)
    
            # Persist cookies
            if r.history:
                # If the hooks create history then we want those cookies too
                for resp in r.history:
                    extract_cookies_to_jar(self.cookies, resp.request, resp.raw)
    
            extract_cookies_to_jar(self.cookies, request, r.raw)
    
            # Resolve redirects if allowed.
            if allow_redirects:
                # Redirect resolving generator.
                gen = self.resolve_redirects(r, request, **kwargs)
                history = [resp for resp in gen]
            else:
                history = []
    
            # Shuffle things around if there's history.
            if history:
                # Insert the first (original) request at the start
                history.insert(0, r)
                # Get the last request made
                r = history.pop()
                r.history = history
    
            # If redirects aren't being followed, store the response on the Request for Response.next().
            if not allow_redirects:
                try:
                    r._next = next(
                        self.resolve_redirects(r, request, yield_requests=True, **kwargs)
                    )
                except StopIteration:
                    pass
    
            if not stream:
                r.content
    
            return r
    
    ```
      </details>

    </details>

    <details>
      <summary><b>should_strip_auth</b></summary>
  - **Signature**: `def should_strip_auth(self, old_url, new_url):`
  - **Documentation**: Decide whether Authorization header should be removed when redirecting

      <details>
        <summary>Source Code</summary>
    ```python
        def should_strip_auth(self, old_url, new_url):
            """Decide whether Authorization header should be removed when redirecting"""
            old_parsed = urlparse(old_url)
            new_parsed = urlparse(new_url)
            if old_parsed.hostname != new_parsed.hostname:
                return True
            # Special case: allow http -> https redirect when using the standard
            # ports. This isn't specified by RFC 7235, but is kept to avoid
            # breaking backwards compatibility with older versions of requests
            # that allowed any redirects on the same host.
            if (
                old_parsed.scheme == "http"
                and old_parsed.port in (80, None)
                and new_parsed.scheme == "https"
                and new_parsed.port in (443, None)
            ):
                return False
    
            # Handle default port usage corresponding to scheme.
            changed_port = old_parsed.port != new_parsed.port
            changed_scheme = old_parsed.scheme != new_parsed.scheme
            default_port = (DEFAULT_PORTS.get(old_parsed.scheme, None), None)
            if (
                not changed_scheme
                and old_parsed.port in default_port
                and new_parsed.port in default_port
            ):
                return False
    
            # Standard case: root URI must match
            return changed_port or changed_scheme
    
    ```
      </details>

    </details>

  </details>

  <details>
    <summary><b>Timeout</b></summary>
    <details>
      <summary>class Timeout:</summary>
    - **Documentation**: The request timed out.

Catching this error will catch both
:exc:`~requests.exceptions.ConnectTimeout` and
:exc:`~requests.exceptions.ReadTimeout` errors.
    </details>

    <details>
      <summary><b>__init__</b></summary>
  - **Signature**: `def __init__(self, *args, **kwargs):`
  - **Documentation**: Initialize RequestException with `request` and `response` objects.

      <details>
        <summary>Source Code</summary>
    ```python
        def __init__(self, *args, **kwargs):
            """Initialize RequestException with `request` and `response` objects."""
            response = kwargs.pop("response", None)
            self.response = response
            self.request = kwargs.pop("request", None)
            if response is not None and not self.request and hasattr(response, "request"):
                self.request = self.response.request
            super().__init__(*args, **kwargs)
    
    ```
      </details>

    </details>

  </details>

  <details>
    <summary><b>TooManyRedirects</b></summary>
    <details>
      <summary>class TooManyRedirects:</summary>
    - **Documentation**: Too many redirects.
    </details>

    <details>
      <summary><b>__init__</b></summary>
  - **Signature**: `def __init__(self, *args, **kwargs):`
  - **Documentation**: Initialize RequestException with `request` and `response` objects.

      <details>
        <summary>Source Code</summary>
    ```python
        def __init__(self, *args, **kwargs):
            """Initialize RequestException with `request` and `response` objects."""
            response = kwargs.pop("response", None)
            self.response = response
            self.request = kwargs.pop("request", None)
            if response is not None and not self.request and hasattr(response, "request"):
                self.request = self.response.request
            super().__init__(*args, **kwargs)
    
    ```
      </details>

    </details>

  </details>

  <details>
    <summary><b>URLRequired</b></summary>
    <details>
      <summary>class URLRequired:</summary>
    - **Documentation**: A valid URL is required to make a request.
    </details>

    <details>
      <summary><b>__init__</b></summary>
  - **Signature**: `def __init__(self, *args, **kwargs):`
  - **Documentation**: Initialize RequestException with `request` and `response` objects.

      <details>
        <summary>Source Code</summary>
    ```python
        def __init__(self, *args, **kwargs):
            """Initialize RequestException with `request` and `response` objects."""
            response = kwargs.pop("response", None)
            self.response = response
            self.request = kwargs.pop("request", None)
            if response is not None and not self.request and hasattr(response, "request"):
                self.request = self.response.request
            super().__init__(*args, **kwargs)
    
    ```
      </details>

    </details>

  </details>

  <details>
    <summary><b>_check_cryptography</b></summary>
  - **Signature**: `def _check_cryptography(cryptography_version):`
  - **Documentation**: No documentation provided.

    <details>
      <summary>Source Code</summary>
    ```python
    def _check_cryptography(cryptography_version):
        # cryptography < 1.3.4
        try:
            cryptography_version = list(map(int, cryptography_version.split(".")))
        except ValueError:
            return
    
        if cryptography_version < [1, 3, 4]:
            warning = "Old version of cryptography ({}) may cause slowdown.".format(
                cryptography_version
            )
            warnings.warn(warning, RequestsDependencyWarning)
    
    ```
    </details>

  </details>

  <details>
    <summary><b>check_compatibility</b></summary>
  - **Signature**: `def check_compatibility(urllib3_version, chardet_version, charset_normalizer_version):`
  - **Documentation**: No documentation provided.

    <details>
      <summary>Source Code</summary>
    ```python
    def check_compatibility(urllib3_version, chardet_version, charset_normalizer_version):
        urllib3_version = urllib3_version.split(".")
        assert urllib3_version != ["dev"]  # Verify urllib3 isn't installed from git.
    
        # Sometimes, urllib3 only reports its version as 16.1.
        if len(urllib3_version) == 2:
            urllib3_version.append("0")
    
        # Check urllib3 for compatibility.
        major, minor, patch = urllib3_version  # noqa: F811
        major, minor, patch = int(major), int(minor), int(patch)
        # urllib3 >= 1.21.1
        assert major >= 1
        if major == 1:
            assert minor >= 21
    
        # Check charset_normalizer for compatibility.
        if chardet_version:
            major, minor, patch = chardet_version.split(".")[:3]
            major, minor, patch = int(major), int(minor), int(patch)
            # chardet_version >= 3.0.2, < 6.0.0
            assert (3, 0, 2) <= (major, minor, patch) < (6, 0, 0)
        elif charset_normalizer_version:
            major, minor, patch = charset_normalizer_version.split(".")[:3]
            major, minor, patch = int(major), int(minor), int(patch)
            # charset_normalizer >= 2.0.0 < 4.0.0
            assert (2, 0, 0) <= (major, minor, patch) < (4, 0, 0)
        else:
            warnings.warn(
                "Unable to find acceptable character detection dependency "
                "(chardet or charset_normalizer).",
                RequestsDependencyWarning,
            )
    
    ```
    </details>

  </details>

  <details>
    <summary><b>delete</b></summary>
  - **Signature**: `def delete(url, **kwargs):`
  - **Documentation**: Sends a DELETE request.

:param url: URL for the new :class:`Request` object.
:param \*\*kwargs: Optional arguments that ``request`` takes.
:return: :class:`Response <Response>` object
:rtype: requests.Response

    <details>
      <summary>Source Code</summary>
    ```python
    def delete(url, **kwargs):
        r"""Sends a DELETE request.
    
        :param url: URL for the new :class:`Request` object.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        """
    
        return request("delete", url, **kwargs)
    
    ```
    </details>

  </details>

  <details>
    <summary><b>get</b></summary>
  - **Signature**: `def get(url, params=None, **kwargs):`
  - **Documentation**: Sends a GET request.

:param url: URL for the new :class:`Request` object.
:param params: (optional) Dictionary, list of tuples or bytes to send
    in the query string for the :class:`Request`.
:param \*\*kwargs: Optional arguments that ``request`` takes.
:return: :class:`Response <Response>` object
:rtype: requests.Response

    <details>
      <summary>Source Code</summary>
    ```python
    def get(url, params=None, **kwargs):
        r"""Sends a GET request.
    
        :param url: URL for the new :class:`Request` object.
        :param params: (optional) Dictionary, list of tuples or bytes to send
            in the query string for the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        """
    
        return request("get", url, params=params, **kwargs)
    
    ```
    </details>

  </details>

  <details>
    <summary><b>head</b></summary>
  - **Signature**: `def head(url, **kwargs):`
  - **Documentation**: Sends a HEAD request.

:param url: URL for the new :class:`Request` object.
:param \*\*kwargs: Optional arguments that ``request`` takes. If
    `allow_redirects` is not provided, it will be set to `False` (as
    opposed to the default :meth:`request` behavior).
:return: :class:`Response <Response>` object
:rtype: requests.Response

    <details>
      <summary>Source Code</summary>
    ```python
    def head(url, **kwargs):
        r"""Sends a HEAD request.
    
        :param url: URL for the new :class:`Request` object.
        :param \*\*kwargs: Optional arguments that ``request`` takes. If
            `allow_redirects` is not provided, it will be set to `False` (as
            opposed to the default :meth:`request` behavior).
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        """
    
        kwargs.setdefault("allow_redirects", False)
        return request("head", url, **kwargs)
    
    ```
    </details>

  </details>

  <details>
    <summary><b>options</b></summary>
  - **Signature**: `def options(url, **kwargs):`
  - **Documentation**: Sends an OPTIONS request.

:param url: URL for the new :class:`Request` object.
:param \*\*kwargs: Optional arguments that ``request`` takes.
:return: :class:`Response <Response>` object
:rtype: requests.Response

    <details>
      <summary>Source Code</summary>
    ```python
    def options(url, **kwargs):
        r"""Sends an OPTIONS request.
    
        :param url: URL for the new :class:`Request` object.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        """
    
        return request("options", url, **kwargs)
    
    ```
    </details>

  </details>

  <details>
    <summary><b>patch</b></summary>
  - **Signature**: `def patch(url, data=None, **kwargs):`
  - **Documentation**: Sends a PATCH request.

:param url: URL for the new :class:`Request` object.
:param data: (optional) Dictionary, list of tuples, bytes, or file-like
    object to send in the body of the :class:`Request`.
:param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
:param \*\*kwargs: Optional arguments that ``request`` takes.
:return: :class:`Response <Response>` object
:rtype: requests.Response

    <details>
      <summary>Source Code</summary>
    ```python
    def patch(url, data=None, **kwargs):
        r"""Sends a PATCH request.
    
        :param url: URL for the new :class:`Request` object.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        """
    
        return request("patch", url, data=data, **kwargs)
    
    ```
    </details>

  </details>

  <details>
    <summary><b>post</b></summary>
  - **Signature**: `def post(url, data=None, json=None, **kwargs):`
  - **Documentation**: Sends a POST request.

:param url: URL for the new :class:`Request` object.
:param data: (optional) Dictionary, list of tuples, bytes, or file-like
    object to send in the body of the :class:`Request`.
:param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
:param \*\*kwargs: Optional arguments that ``request`` takes.
:return: :class:`Response <Response>` object
:rtype: requests.Response

    <details>
      <summary>Source Code</summary>
    ```python
    def post(url, data=None, json=None, **kwargs):
        r"""Sends a POST request.
    
        :param url: URL for the new :class:`Request` object.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        """
    
        return request("post", url, data=data, json=json, **kwargs)
    
    ```
    </details>

  </details>

  <details>
    <summary><b>put</b></summary>
  - **Signature**: `def put(url, data=None, **kwargs):`
  - **Documentation**: Sends a PUT request.

:param url: URL for the new :class:`Request` object.
:param data: (optional) Dictionary, list of tuples, bytes, or file-like
    object to send in the body of the :class:`Request`.
:param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
:param \*\*kwargs: Optional arguments that ``request`` takes.
:return: :class:`Response <Response>` object
:rtype: requests.Response

    <details>
      <summary>Source Code</summary>
    ```python
    def put(url, data=None, **kwargs):
        r"""Sends a PUT request.
    
        :param url: URL for the new :class:`Request` object.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        """
    
        return request("put", url, data=data, **kwargs)
    
    ```
    </details>

  </details>

  <details>
    <summary><b>request</b></summary>
  - **Signature**: `def request(method, url, **kwargs):`
  - **Documentation**: Constructs and sends a :class:`Request <Request>`.

:param method: method for the new :class:`Request` object: ``GET``, ``OPTIONS``, ``HEAD``, ``POST``, ``PUT``, ``PATCH``, or ``DELETE``.
:param url: URL for the new :class:`Request` object.
:param params: (optional) Dictionary, list of tuples or bytes to send
    in the query string for the :class:`Request`.
:param data: (optional) Dictionary, list of tuples, bytes, or file-like
    object to send in the body of the :class:`Request`.
:param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
:param headers: (optional) Dictionary of HTTP Headers to send with the :class:`Request`.
:param cookies: (optional) Dict or CookieJar object to send with the :class:`Request`.
:param files: (optional) Dictionary of ``'name': file-like-objects`` (or ``{'name': file-tuple}``) for multipart encoding upload.
    ``file-tuple`` can be a 2-tuple ``('filename', fileobj)``, 3-tuple ``('filename', fileobj, 'content_type')``
    or a 4-tuple ``('filename', fileobj, 'content_type', custom_headers)``, where ``'content_type'`` is a string
    defining the content type of the given file and ``custom_headers`` a dict-like object containing additional headers
    to add for the file.
:param auth: (optional) Auth tuple to enable Basic/Digest/Custom HTTP Auth.
:param timeout: (optional) How many seconds to wait for the server to send data
    before giving up, as a float, or a :ref:`(connect timeout, read
    timeout) <timeouts>` tuple.
:type timeout: float or tuple
:param allow_redirects: (optional) Boolean. Enable/disable GET/OPTIONS/POST/PUT/PATCH/DELETE/HEAD redirection. Defaults to ``True``.
:type allow_redirects: bool
:param proxies: (optional) Dictionary mapping protocol to the URL of the proxy.
:param verify: (optional) Either a boolean, in which case it controls whether we verify
        the server's TLS certificate, or a string, in which case it must be a path
        to a CA bundle to use. Defaults to ``True``.
:param stream: (optional) if ``False``, the response content will be immediately downloaded.
:param cert: (optional) if String, path to ssl client cert file (.pem). If Tuple, ('cert', 'key') pair.
:return: :class:`Response <Response>` object
:rtype: requests.Response

Usage::

  >>> import requests
  >>> req = requests.request('GET', 'https://httpbin.org/get')
  >>> req
  <Response [200]>

    <details>
      <summary>Source Code</summary>
    ```python
    def request(method, url, **kwargs):
        """Constructs and sends a :class:`Request <Request>`.
    
        :param method: method for the new :class:`Request` object: ``GET``, ``OPTIONS``, ``HEAD``, ``POST``, ``PUT``, ``PATCH``, or ``DELETE``.
        :param url: URL for the new :class:`Request` object.
        :param params: (optional) Dictionary, list of tuples or bytes to send
            in the query string for the :class:`Request`.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
        :param headers: (optional) Dictionary of HTTP Headers to send with the :class:`Request`.
        :param cookies: (optional) Dict or CookieJar object to send with the :class:`Request`.
        :param files: (optional) Dictionary of ``'name': file-like-objects`` (or ``{'name': file-tuple}``) for multipart encoding upload.
            ``file-tuple`` can be a 2-tuple ``('filename', fileobj)``, 3-tuple ``('filename', fileobj, 'content_type')``
            or a 4-tuple ``('filename', fileobj, 'content_type', custom_headers)``, where ``'content_type'`` is a string
            defining the content type of the given file and ``custom_headers`` a dict-like object containing additional headers
            to add for the file.
        :param auth: (optional) Auth tuple to enable Basic/Digest/Custom HTTP Auth.
        :param timeout: (optional) How many seconds to wait for the server to send data
            before giving up, as a float, or a :ref:`(connect timeout, read
            timeout) <timeouts>` tuple.
        :type timeout: float or tuple
        :param allow_redirects: (optional) Boolean. Enable/disable GET/OPTIONS/POST/PUT/PATCH/DELETE/HEAD redirection. Defaults to ``True``.
        :type allow_redirects: bool
        :param proxies: (optional) Dictionary mapping protocol to the URL of the proxy.
        :param verify: (optional) Either a boolean, in which case it controls whether we verify
                the server's TLS certificate, or a string, in which case it must be a path
                to a CA bundle to use. Defaults to ``True``.
        :param stream: (optional) if ``False``, the response content will be immediately downloaded.
        :param cert: (optional) if String, path to ssl client cert file (.pem). If Tuple, ('cert', 'key') pair.
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
    
        Usage::
    
          >>> import requests
          >>> req = requests.request('GET', 'https://httpbin.org/get')
          >>> req
          <Response [200]>
        """
    
        # By using the 'with' statement we are sure the session is closed, thus we
        # avoid leaving sockets open which can trigger a ResourceWarning in some
        # cases, and look like a memory leak in others.
        with sessions.Session() as session:
            return session.request(method=method, url=url, **kwargs)
    
    ```
    </details>

  </details>

  <details>
    <summary><b>session</b></summary>
  - **Signature**: `def session():`
  - **Documentation**: Returns a :class:`Session` for context-management.

.. deprecated:: 1.0.0

    This method has been deprecated since version 1.0.0 and is only kept for
    backwards compatibility. New code should use :class:`~requests.sessions.Session`
    to create a session. This may be removed at a future date.

:rtype: Session

    <details>
      <summary>Source Code</summary>
    ```python
    def session():
        """
        Returns a :class:`Session` for context-management.
    
        .. deprecated:: 1.0.0
    
            This method has been deprecated since version 1.0.0 and is only kept for
            backwards compatibility. New code should use :class:`~requests.sessions.Session`
            to create a session. This may be removed at a future date.
    
        :rtype: Session
        """
        return Session()
    
    ```
    </details>

  </details>

</details>
