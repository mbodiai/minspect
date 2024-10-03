<details><summary><h3>module pydantic</h3></summary>
  <details><summary><h4>class AfterValidator(object)</h4></summary>
  <details><summary><b>def __delattr__(self, name)</b></summary>
  <p>Implement delattr(self, name).</p>
  </details>
  <details><summary><b>def __eq__(self, other)</b></summary>
  <p>Return self==value.</p>
  </details>
  <details><summary><b>def __get_pydantic_core_schema__(self, source_type: 'Any', handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'</b></summary>
  </details>
  <details><summary><b>def _dataclass_getstate(self)</b></summary>
  </details>
  <details><summary><b>def __hash__(self)</b></summary>
  <p>Return hash(self).</p>
  </details>
  <details><summary><b>def __init__(self, func: 'core_schema.NoInfoValidatorFunction | core_schema.WithInfoValidatorFunction') -> None</b></summary>
  <p>Initialize self.  See help(type(self)) for accurate signature.</p>
  </details>
  <details><summary><b>def __repr__(self)</b></summary>
  <p>Return repr(self).</p>
  </details>
  <details><summary><b>def __setattr__(self, name, value)</b></summary>
  <p>Implement setattr(self, name, value).</p>
  </details>
  <details><summary><b>def _dataclass_setstate(self, state)</b></summary>
  </details>
  <details><summary><b>def _from_decorator(decorator: '_decorators.Decorator[_decorators.FieldValidatorDecoratorInfo]') -> 'Self'</b></summary>
  </details>
  <li><b>func:</b> <member 'func' of 'AfterValidator' objects></li>
  </details>
  <details><summary><h4>class AliasChoices(object)</h4></summary>
  <details><summary><b>def __eq__(self, other)</b></summary>
  <p>Return self==value.</p>
  </details>
  <details><summary><b>def __init__(self, first_choice: 'str | AliasPath', *choices: 'str | AliasPath') -> 'None'</b></summary>
  <p>Initialize self.  See help(type(self)) for accurate signature.</p>
  </details>
  <details><summary><b>def __repr__(self)</b></summary>
  <p>Return repr(self).</p>
  </details>
  <li><b>choices:</b> <member 'choices' of 'AliasChoices' objects></li>
  <details><summary><b>def convert_to_aliases(self) -> 'list[list[str | int]]'</b></summary>
  <p>Converts arguments to a list of lists containing string or integer aliases.

Returns:
    The list of aliases.</p>
  </details>
  </details>
  <details><summary><h4>class AliasGenerator(object)</h4></summary>
  <details><summary><b>def __eq__(self, other)</b></summary>
  <p>Return self==value.</p>
  </details>
  <details><summary><b>def __init__(self, alias: 'Callable[[str], str] | None' = None, validation_alias: 'Callable[[str], str | AliasPath | AliasChoices] | None' = None, serialization_alias: 'Callable[[str], str] | None' = None) -> None</b></summary>
  <p>Initialize self.  See help(type(self)) for accurate signature.</p>
  </details>
  <details><summary><b>def __repr__(self)</b></summary>
  <p>Return repr(self).</p>
  </details>
  <details><summary><b>def _generate_alias(self, alias_kind: "Literal['alias', 'validation_alias', 'serialization_alias']", allowed_types: 'tuple[type[str] | type[AliasPath] | type[AliasChoices], ...]', field_name: 'str') -> 'str | AliasPath | AliasChoices | None'</b></summary>
  <p>Generate an alias of the specified kind. Returns None if the alias generator is None.

Raises:
    TypeError: If the alias generator produces an invalid type.</p>
  </details>
  <li><b>alias:</b> <member 'alias' of 'AliasGenerator' objects></li>
  <details><summary><b>def generate_aliases(self, field_name: 'str') -> 'tuple[str | None, str | AliasPath | AliasChoices | None, str | None]'</b></summary>
  <p>Generate `alias`, `validation_alias`, and `serialization_alias` for a field.

Returns:
    A tuple of three aliases - validation, alias, and serialization.</p>
  </details>
  <li><b>serialization_alias:</b> <member 'serialization_alias' of 'AliasGenerator' objects></li>
  <li><b>validation_alias:</b> <member 'validation_alias' of 'AliasGenerator' objects></li>
  </details>
  <details><summary><h4>class AliasPath(object)</h4></summary>
  <details><summary><b>def __eq__(self, other)</b></summary>
  <p>Return self==value.</p>
  </details>
  <details><summary><b>def __init__(self, first_arg: 'str', *args: 'str | int') -> 'None'</b></summary>
  <p>Initialize self.  See help(type(self)) for accurate signature.</p>
  </details>
  <details><summary><b>def __repr__(self)</b></summary>
  <p>Return repr(self).</p>
  </details>
  <details><summary><b>def convert_to_aliases(self) -> 'list[str | int]'</b></summary>
  <p>Converts arguments to a list of string or integer aliases.

Returns:
    The list of aliases.</p>
  </details>
  <li><b>path:</b> <member 'path' of 'AliasPath' objects></li>
  <details><summary><b>def search_dict_for_path(self, d: 'dict') -> 'Any'</b></summary>
  <p>Searches a dictionary for the path specified by the alias.

Returns:
    The value at the specified path, or `PydanticUndefined` if the path is not found.</p>
  </details>
  </details>
  <details><summary><h4>class AllowInfNan(PydanticMetadata)</h4></summary>
  <details><summary><b>def __eq__(self, other)</b></summary>
  <p>Return self==value.</p>
  </details>
  <details><summary><b>def __hash__(self) -> 'int'</b></summary>
  <p>Return hash(self).</p>
  </details>
  <details><summary><b>def __init__(self, allow_inf_nan: 'bool' = True) -> None</b></summary>
  <p>Initialize self.  See help(type(self)) for accurate signature.</p>
  </details>
  <details><summary><b>def __pretty__(self, fmt: 'typing.Callable[[Any], Any]', **kwargs: 'Any') -> 'typing.Generator[Any, None, None]'</b></summary>
  <p>Used by devtools (https://python-devtools.helpmanual.io/) to pretty print objects.</p>
  </details>
  <details><summary><b>def __repr__(self)</b></summary>
  <p>Return repr(self).</p>
  </details>
  <details><summary><b>def __repr_args__(self) -> 'ReprArgs'</b></summary>
  <p>Returns the attributes to show in __str__, __repr__, and __pretty__ this is generally overridden.

Can either return:
* name - value pairs, e.g.: `[('foo_name', 'foo'), ('bar_name', ['b', 'a', 'r'])]`
* or, just values, e.g.: `[(None, 'foo'), (None, ['b', 'a', 'r'])]`</p>
  </details>
  <details><summary><b>def __repr_name__(self) -> 'str'</b></summary>
  <p>Name of the instance's class, used in __repr__.</p>
  </details>
  <details><summary><b>def __repr_str__(self, join_str: 'str') -> 'str'</b></summary>
  </details>
  <details><summary><b>def __rich_repr__(self) -> 'RichReprResult'</b></summary>
  <p>Used by Rich (https://rich.readthedocs.io/en/stable/pretty.html) to pretty print objects.</p>
  </details>
  <details><summary><b>def __str__(self) -> 'str'</b></summary>
  <p>Return str(self).</p>
  </details>
  <li><b>allow_inf_nan:</b> True</li>
  </details>
  <li><b>AmqpDsn:</b> typing.Annotated[pydantic_core._pydantic_core.Url, UrlConstraints(max_length=None, allowed_schemes=['amqp', 'amqps'], host_required=None, default_host=None, default_port=None, default_path=None)]</li>
  <li><b>AnyHttpUrl:</b> typing.Annotated[pydantic_core._pydantic_core.Url, UrlConstraints(max_length=None, allowed_schemes=['http', 'https'], host_required=None, default_host=None, default_port=None, default_path=None)]</li>
  <details><summary><h4>class Url(object)</h4></summary>
  <li><b>build:</b> <built-in method build of type object at 0x5644ae59f590></li>
  <li><b>fragment:</b> <attribute 'fragment' of 'pydantic_core._pydantic_core.Url' objects></li>
  <li><b>host:</b> <attribute 'host' of 'pydantic_core._pydantic_core.Url' objects></li>
  <li><b>password:</b> <attribute 'password' of 'pydantic_core._pydantic_core.Url' objects></li>
  <li><b>path:</b> <attribute 'path' of 'pydantic_core._pydantic_core.Url' objects></li>
  <li><b>port:</b> <attribute 'port' of 'pydantic_core._pydantic_core.Url' objects></li>
  <li><b>query:</b> <attribute 'query' of 'pydantic_core._pydantic_core.Url' objects></li>
  <li><b>query_params:</b> <method 'query_params' of 'pydantic_core._pydantic_core.Url' objects></li>
  <li><b>scheme:</b> <attribute 'scheme' of 'pydantic_core._pydantic_core.Url' objects></li>
  <li><b>unicode_host:</b> <method 'unicode_host' of 'pydantic_core._pydantic_core.Url' objects></li>
  <li><b>unicode_string:</b> <method 'unicode_string' of 'pydantic_core._pydantic_core.Url' objects></li>
  <li><b>username:</b> <attribute 'username' of 'pydantic_core._pydantic_core.Url' objects></li>
  </details>
  <li><b>AnyWebsocketUrl:</b> typing.Annotated[pydantic_core._pydantic_core.Url, UrlConstraints(max_length=None, allowed_schemes=['ws', 'wss'], host_required=None, default_host=None, default_port=None, default_path=None)]</li>
  <details><summary><h4>class AwareDatetime(object)</h4></summary>
  <details><summary><b>def __get_pydantic_core_schema__(source: 'type[Any]', handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'</b></summary>
  </details>
  <details><summary><b>def __repr__(self) -> 'str'</b></summary>
  <p>Return repr(self).</p>
  </details>
  </details>
  <li><b>Base64Bytes:</b> typing.Annotated[bytes, EncodedBytes(encoder=<class 'pydantic.types.Base64Encoder'>)]</li>
  <details><summary><h4>class Base64Encoder(EncoderProtocol)</h4></summary>
  <details><summary><b>def __class_getitem__(params)</b></summary>
  <p>Parameterizes a generic class.

At least, parameterizing a generic class is the *main* thing this method
does. For example, for some generic class `Foo`, this is called when we
do `Foo[int]` - there, with `cls=Foo` and `params=int`.

However, note that this method is also called when defining generic
classes in the first place with `class Foo(Generic[T]): ...`.</p>
  </details>
  <details><summary><b>def _no_init(self, *args, **kwargs)</b></summary>
  </details>
  <details><summary><b>def __init_subclass__(*args, **kwargs)</b></summary>
  <p>This method is called when a class is subclassed.

The default implementation does nothing. It may be
overridden to extend subclasses.</p>
  </details>
  <details><summary><b>def _proto_hook(other)</b></summary>
  </details>
  <details><summary><b>def decode(data: 'bytes') -> 'bytes'</b></summary>
  <p>Decode the data from base64 encoded bytes to original bytes data.

Args:
    data: The data to decode.

Returns:
    The decoded data.</p>
  </details>
  <details><summary><b>def encode(value: 'bytes') -> 'bytes'</b></summary>
  <p>Encode the data from bytes to a base64 encoded bytes.

Args:
    value: The data to encode.

Returns:
    The encoded data.</p>
  </details>
  <details><summary><b>def get_json_format() -> "Literal['base64']"</b></summary>
  <p>Get the JSON format for the encoded data.

Returns:
    The JSON format for the encoded data.</p>
  </details>
  </details>
  <li><b>Base64Str:</b> typing.Annotated[str, EncodedStr(encoder=<class 'pydantic.types.Base64Encoder'>)]</li>
  <li><b>Base64UrlBytes:</b> typing.Annotated[bytes, EncodedBytes(encoder=<class 'pydantic.types.Base64UrlEncoder'>)]</li>
  <li><b>Base64UrlStr:</b> typing.Annotated[str, EncodedStr(encoder=<class 'pydantic.types.Base64UrlEncoder'>)]</li>
  <details><summary><h4>class BaseConfig(object)</h4></summary>
  <details><summary><b>def __getattr__(self, item: 'str') -> 'Any'</b></summary>
  </details>
  <details><summary><b>def __init_subclass__(**kwargs: 'Any') -> 'None'</b></summary>
  <p>This method is called when a class is subclassed.

The default implementation does nothing. It may be
overridden to extend subclasses.</p>
  </details>
  <details><summary><b>def __new__(*args, **kwargs)</b></summary>
  <p>Create and return a new object.  See help(type) for accurate signature.</p>
  </details>
  </details>
  <details><summary><h4>class BaseModel(object)</h4></summary>
  <details><summary><b>def __class_getitem__(typevar_values: 'type[Any] | tuple[type[Any], ...]') -> 'type[BaseModel] | _forward_ref.PydanticRecursiveRef'</b></summary>
  </details>
  <details><summary><b>def __copy__(self) -> 'Self'</b></summary>
  <p>Returns a shallow copy of the model.</p>
  </details>
  <details><summary><b>def __deepcopy__(self, memo: 'dict[int, Any] | None' = None) -> 'Self'</b></summary>
  <p>Returns a deep copy of the model.</p>
  </details>
  <details><summary><b>def __delattr__(self, item: 'str') -> 'Any'</b></summary>
  <p>Implement delattr(self, name).</p>
  </details>
  <details><summary><b>def __eq__(self, other: 'Any') -> 'bool'</b></summary>
  <p>Return self==value.</p>
  </details>
  <details><summary><b>def __get_pydantic_core_schema__(source: 'type[BaseModel]', handler: 'GetCoreSchemaHandler', /) -> 'CoreSchema'</b></summary>
  <p>Hook into generating the model's CoreSchema.

Args:
    source: The class we are generating a schema for.
        This will generally be the same as the `cls` argument if this is a classmethod.
    handler: A callable that calls into Pydantic's internal CoreSchema generation logic.

Returns:
    A `pydantic-core` `CoreSchema`.</p>
  </details>
  <details><summary><b>def __get_pydantic_json_schema__(core_schema: 'CoreSchema', handler: 'GetJsonSchemaHandler', /) -> 'JsonSchemaValue'</b></summary>
  <p>Hook into generating the model's JSON schema.

Args:
    core_schema: A `pydantic-core` CoreSchema.
        You can ignore this argument and call the handler with a new CoreSchema,
        wrap this CoreSchema (`{'type': 'nullable', 'schema': current_schema}`),
        or just call the handler with the original schema.
    handler: Call into Pydantic's internal JSON schema generation.
        This will raise a `pydantic.errors.PydanticInvalidForJsonSchema` if JSON schema
        generation fails.
        Since this gets called by `BaseModel.model_json_schema` you can override the
        `schema_generator` argument to that function to change JSON schema generation globally
        for a type.

Returns:
    A JSON schema, as a Python object.</p>
  </details>
  <details><summary><b>def __getattr__(self, item: 'str') -> 'Any'</b></summary>
  </details>
  <details><summary><b>def __getstate__(self) -> 'dict[Any, Any]'</b></summary>
  <p>Helper for pickle.</p>
  </details>
  <details><summary><b>def __init__(self, /, **data: 'Any') -> 'None'</b></summary>
  <p>Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.</p>
  </details>
  <details><summary><b>def __iter__(self) -> 'TupleGenerator'</b></summary>
  <p>So `dict(model)` works.</p>
  </details>
  <details><summary><b>def __pretty__(self, fmt: 'typing.Callable[[Any], Any]', **kwargs: 'Any') -> 'typing.Generator[Any, None, None]'</b></summary>
  <p>Used by devtools (https://python-devtools.helpmanual.io/) to pretty print objects.</p>
  </details>
  <details><summary><b>def __pydantic_init_subclass__(**kwargs: 'Any') -> 'None'</b></summary>
  <p>This is intended to behave just like `__init_subclass__`, but is called by `ModelMetaclass`
only after the class is actually fully initialized. In particular, attributes like `model_fields` will
be present when this is called.

This is necessary because `__init_subclass__` will always be called by `type.__new__`,
and it would require a prohibitively large refactor to the `ModelMetaclass` to ensure that
`type.__new__` was called in such a manner that the class would already be sufficiently initialized.

This will receive the same `kwargs` that would be passed to the standard `__init_subclass__`, namely,
any kwargs passed to the class definition that aren't used internally by pydantic.

Args:
    **kwargs: Any keyword arguments passed to the class definition that aren't used internally
        by pydantic.</p>
  </details>
  <details><summary><b>def __repr__(self) -> 'str'</b></summary>
  <p>Return repr(self).</p>
  </details>
  <details><summary><b>def __repr_args__(self) -> '_repr.ReprArgs'</b></summary>
  </details>
  <details><summary><b>def __repr_name__(self) -> 'str'</b></summary>
  <p>Name of the instance's class, used in __repr__.</p>
  </details>
  <details><summary><b>def __repr_str__(self, join_str: 'str') -> 'str'</b></summary>
  </details>
  <details><summary><b>def __rich_repr__(self) -> 'RichReprResult'</b></summary>
  <p>Used by Rich (https://rich.readthedocs.io/en/stable/pretty.html) to pretty print objects.</p>
  </details>
  <details><summary><b>def __setattr__(self, name: 'str', value: 'Any') -> 'None'</b></summary>
  <p>Implement setattr(self, name, value).</p>
  </details>
  <details><summary><b>def __setstate__(self, state: 'dict[Any, Any]') -> 'None'</b></summary>
  </details>
  <details><summary><b>def __str__(self) -> 'str'</b></summary>
  <p>Return str(self).</p>
  </details>
  <details><summary><b>def _calculate_keys(self, *args: 'Any', **kwargs: 'Any') -> 'Any'</b></summary>
  </details>
  <details><summary><b>def _check_frozen(self, name: 'str', value: 'Any') -> 'None'</b></summary>
  </details>
  <details><summary><b>def _copy_and_set_values(self, *args: 'Any', **kwargs: 'Any') -> 'Any'</b></summary>
  </details>
  <details><summary><b>def _get_value(*args: 'Any', **kwargs: 'Any') -> 'Any'</b></summary>
  </details>
  <details><summary><b>def _iter(self, *args: 'Any', **kwargs: 'Any') -> 'Any'</b></summary>
  </details>
  <details><summary><b>def construct(_fields_set: 'set[str] | None' = None, **values: 'Any') -> 'Self'</b></summary>
  </details>
  <details><summary><b>def copy(self, *, include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False) -> 'Self'</b></summary>
  <p>Returns a copy of the model.

!!! warning "Deprecated"
    This method is now deprecated; use `model_copy` instead.

If you need `include` or `exclude`, use:

```py
data = self.model_dump(include=include, exclude=exclude, round_trip=True)
data = {**data, **(update or {})}
copied = self.model_validate(data)
```

Args:
    include: Optional set or mapping specifying which fields to include in the copied model.
    exclude: Optional set or mapping specifying which fields to exclude in the copied model.
    update: Optional dictionary of field-value pairs to override field values in the copied model.
    deep: If True, the values of fields that are Pydantic models will be deep-copied.

Returns:
    A copy of the model with included, excluded and updated fields as specified.</p>
  </details>
  <details><summary><b>def dict(self, *, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False) -> 'Dict[str, Any]'</b></summary>
  </details>
  <details><summary><b>def from_orm(obj: 'Any') -> 'Self'</b></summary>
  </details>
  <details><summary><b>def json(self, *, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any') -> 'str'</b></summary>
  </details>
  <li><b>model_computed_fields:</b> {}</li>
  <li><b>model_config:</b> {}</li>
  <details><summary><b>def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any') -> 'Self'</b></summary>
  <p>Creates a new instance of the `Model` class with validated data.

Creates a new model setting `__dict__` and `__pydantic_fields_set__` from trusted or pre-validated data.
Default values are respected, but no other validation is performed.

!!! note
    `model_construct()` generally respects the `model_config.extra` setting on the provided model.
    That is, if `model_config.extra == 'allow'`, then all extra passed values are added to the model instance's `__dict__`
    and `__pydantic_extra__` fields. If `model_config.extra == 'ignore'` (the default), then all extra passed values are ignored.
    Because no validation is performed with a call to `model_construct()`, having `model_config.extra == 'forbid'` does not result in
    an error if extra values are passed, but they will be ignored.

Args:
    _fields_set: A set of field names that were originally explicitly set during instantiation. If provided,
        this is directly used for the [`model_fields_set`][pydantic.BaseModel.model_fields_set] attribute.
        Otherwise, the field names from the `values` argument will be used.
    values: Trusted or pre-validated data dictionary.

Returns:
    A new instance of the `Model` class with validated data.</p>
  </details>
  <details><summary><b>def model_copy(self, *, update: 'dict[str, Any] | None' = None, deep: 'bool' = False) -> 'Self'</b></summary>
  <p>Usage docs: https://docs.pydantic.dev/2.9/concepts/serialization/#model_copy

Returns a copy of the model.

Args:
    update: Values to change/add in the new model. Note: the data is not validated
        before creating the new model. You should trust this data.
    deep: Set to `True` to make a deep copy of the model.

Returns:
    New model instance.</p>
  </details>
  <details><summary><b>def model_dump(self, *, mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, serialize_as_any: 'bool' = False) -> 'dict[str, Any]'</b></summary>
  <p>Usage docs: https://docs.pydantic.dev/2.9/concepts/serialization/#modelmodel_dump

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

Args:
    mode: The mode in which `to_python` should run.
        If mode is 'json', the output will only contain JSON serializable types.
        If mode is 'python', the output may contain non-JSON-serializable Python objects.
    include: A set of fields to include in the output.
    exclude: A set of fields to exclude from the output.
    context: Additional context to pass to the serializer.
    by_alias: Whether to use the field's alias in the dictionary key if defined.
    exclude_unset: Whether to exclude fields that have not been explicitly set.
    exclude_defaults: Whether to exclude fields that are set to their default value.
    exclude_none: Whether to exclude fields that have a value of `None`.
    round_trip: If True, dumped values should be valid as input for non-idempotent types such as Json[T].
    warnings: How to handle serialization errors. False/"none" ignores them, True/"warn" logs errors,
        "error" raises a [`PydanticSerializationError`][pydantic_core.PydanticSerializationError].
    serialize_as_any: Whether to serialize fields with duck-typing serialization behavior.

Returns:
    A dictionary representation of the model.</p>
  </details>
  <details><summary><b>def model_dump_json(self, *, indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, serialize_as_any: 'bool' = False) -> 'str'</b></summary>
  <p>Usage docs: https://docs.pydantic.dev/2.9/concepts/serialization/#modelmodel_dump_json

Generates a JSON representation of the model using Pydantic's `to_json` method.

Args:
    indent: Indentation to use in the JSON output. If None is passed, the output will be compact.
    include: Field(s) to include in the JSON output.
    exclude: Field(s) to exclude from the JSON output.
    context: Additional context to pass to the serializer.
    by_alias: Whether to serialize using field aliases.
    exclude_unset: Whether to exclude fields that have not been explicitly set.
    exclude_defaults: Whether to exclude fields that are set to their default value.
    exclude_none: Whether to exclude fields that have a value of `None`.
    round_trip: If True, dumped values should be valid as input for non-idempotent types such as Json[T].
    warnings: How to handle serialization errors. False/"none" ignores them, True/"warn" logs errors,
        "error" raises a [`PydanticSerializationError`][pydantic_core.PydanticSerializationError].
    serialize_as_any: Whether to serialize fields with duck-typing serialization behavior.

Returns:
    A JSON string representation of the model.</p>
  </details>
  <li><b>model_extra:</b> <property object at 0x7fb1730d98a0></li>
  <li><b>model_fields:</b> {}</li>
  <li><b>model_fields_set:</b> <property object at 0x7fb1730da200></li>
  <details><summary><b>def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation') -> 'dict[str, Any]'</b></summary>
  <p>Generates a JSON schema for a model class.

Args:
    by_alias: Whether to use attribute aliases or not.
    ref_template: The reference template.
    schema_generator: To override the logic used to generate the JSON schema, as a subclass of
        `GenerateJsonSchema` with your desired modifications
    mode: The mode in which to generate the schema.

Returns:
    The JSON schema for the given model class.</p>
  </details>
  <details><summary><b>def model_parametrized_name(params: 'tuple[type[Any], ...]') -> 'str'</b></summary>
  <p>Compute the class name for parametrizations of generic classes.

This method can be overridden to achieve a custom naming scheme for generic BaseModels.

Args:
    params: Tuple of types of the class. Given a generic class
        `Model` with 2 type variables and a concrete model `Model[str, int]`,
        the value `(str, int)` would be passed to `params`.

Returns:
    String representing the new class where `params` are passed to `cls` as type variables.

Raises:
    TypeError: Raised when trying to generate concrete names for non-generic models.</p>
  </details>
  <details><summary><b>def model_post_init(self, _BaseModel__context: 'Any') -> 'None'</b></summary>
  <p>Override this method to perform additional initialization after `__init__` and `model_construct`.
This is useful if you want to do some validation that requires the entire model to be initialized.</p>
  </details>
  <details><summary><b>def model_rebuild(*, force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'dict[str, Any] | None' = None) -> 'bool | None'</b></summary>
  <p>Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annotations is a ForwardRef which could not be resolved during
the initial attempt to build the schema, and automatic rebuilding fails.

Args:
    force: Whether to force the rebuilding of the model schema, defaults to `False`.
    raise_errors: Whether to raise errors, defaults to `True`.
    _parent_namespace_depth: The depth level of the parent namespace, defaults to 2.
    _types_namespace: The types namespace, defaults to `None`.

Returns:
    Returns `None` if the schema is already "complete" and rebuilding was not required.
    If rebuilding _was_ required, returns `True` if rebuilding was successful, otherwise `False`.</p>
  </details>
  <details><summary><b>def model_validate(obj: 'Any', *, strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None) -> 'Self'</b></summary>
  <p>Validate a pydantic model instance.

Args:
    obj: The object to validate.
    strict: Whether to enforce types strictly.
    from_attributes: Whether to extract data from object attributes.
    context: Additional context to pass to the validator.

Raises:
    ValidationError: If the object could not be validated.

Returns:
    The validated model instance.</p>
  </details>
  <details><summary><b>def model_validate_json(json_data: 'str | bytes | bytearray', *, strict: 'bool | None' = None, context: 'Any | None' = None) -> 'Self'</b></summary>
  <p>Usage docs: https://docs.pydantic.dev/2.9/concepts/json/#json-parsing

Validate the given JSON data against the Pydantic model.

Args:
    json_data: The JSON data to validate.
    strict: Whether to enforce types strictly.
    context: Extra variables to pass to the validator.

Returns:
    The validated Pydantic model.

Raises:
    ValidationError: If `json_data` is not a JSON string or the object could not be validated.</p>
  </details>
  <details><summary><b>def model_validate_strings(obj: 'Any', *, strict: 'bool | None' = None, context: 'Any | None' = None) -> 'Self'</b></summary>
  <p>Validate the given object with string data against the Pydantic model.

Args:
    obj: The object containing string data to validate.
    strict: Whether to enforce types strictly.
    context: Extra variables to pass to the validator.

Returns:
    The validated Pydantic model.</p>
  </details>
  <details><summary><b>def parse_file(path: 'str | Path', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'</b></summary>
  </details>
  <details><summary><b>def parse_obj(obj: 'Any') -> 'Self'</b></summary>
  </details>
  <details><summary><b>def parse_raw(b: 'str | bytes', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'</b></summary>
  </details>
  <details><summary><b>def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}') -> 'Dict[str, Any]'</b></summary>
  </details>
  <details><summary><b>def schema_json(*, by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any') -> 'str'</b></summary>
  </details>
  <details><summary><b>def update_forward_refs(**localns: 'Any') -> 'None'</b></summary>
  </details>
  <details><summary><b>def validate(value: 'Any') -> 'Self'</b></summary>
  </details>
  </details>
  <details><summary><h4>class BeforeValidator(object)</h4></summary>
  <details><summary><b>def __delattr__(self, name)</b></summary>
  <p>Implement delattr(self, name).</p>
  </details>
  <details><summary><b>def __eq__(self, other)</b></summary>
  <p>Return self==value.</p>
  </details>
  <details><summary><b>def __get_pydantic_core_schema__(self, source_type: 'Any', handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'</b></summary>
  </details>
  <details><summary><b>def _dataclass_getstate(self)</b></summary>
  </details>
  <details><summary><b>def __hash__(self)</b></summary>
  <p>Return hash(self).</p>
  </details>
  <details><summary><b>def __init__(self, func: 'core_schema.NoInfoValidatorFunction | core_schema.WithInfoValidatorFunction', json_schema_input_type: 'Any' = PydanticUndefined) -> None</b></summary>
  <p>Initialize self.  See help(type(self)) for accurate signature.</p>
  </details>
  <details><summary><b>def __repr__(self)</b></summary>
  <p>Return repr(self).</p>
  </details>
  <details><summary><b>def __setattr__(self, name, value)</b></summary>
  <p>Implement setattr(self, name, value).</p>
  </details>
  <details><summary><b>def _dataclass_setstate(self, state)</b></summary>
  </details>
  <details><summary><b>def _from_decorator(decorator: '_decorators.Decorator[_decorators.FieldValidatorDecoratorInfo]') -> 'Self'</b></summary>
  </details>
  <li><b>func:</b> <member 'func' of 'BeforeValidator' objects></li>
  <li><b>json_schema_input_type:</b> <member 'json_schema_input_type' of 'BeforeValidator' objects></li>
  </details>
  <details><summary><h4>class ByteSize(int)</h4></summary>
  <details><summary><b>def __get_pydantic_core_schema__(source: 'type[Any]', handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'</b></summary>
  </details>
  <details><summary><b>def _validate(input_value: 'Any', /, _: 'core_schema.ValidationInfo') -> 'ByteSize'</b></summary>
  </details>
  <li><b>as_integer_ratio:</b> <method 'as_integer_ratio' of 'int' objects></li>
  <li><b>bit_count:</b> <method 'bit_count' of 'int' objects></li>
  <li><b>bit_length:</b> <method 'bit_length' of 'int' objects></li>
  <li><b>byte_sizes:</b> {'b': 1, 'kb': 1000, 'mb': 1000000, 'gb': 1000000000, 'tb': 1000000000000, 'pb': 1000000000000000, 'eb': 1000000000000000000, 'kib': 1024, 'mib': 1048576, 'gib': 1073741824, 'tib': 1099511627776, 'pib': 1125899906842624, 'eib': 1152921504606846976, 'bit': 0.125, 'kbit': 125.0, 'mbit': 125000.0, 'gbit': 125000000.0, 'tbit': 125000000000.0, 'pbit': 125000000000000.0, 'ebit': 1.25e+17, 'kibit': 128.0, 'mibit': 131072.0, 'gibit': 134217728.0, 'tibit': 137438953472.0, 'pibit': 140737488355328.0, 'eibit': 1.4411518807585587e+17, 'k': 1000, 'm': 1000000, 'g': 1000000000, 't': 1000000000000, 'p': 1000000000000000, 'e': 1000000000000000000}</li>
  <li><b>byte_string_pattern:</b> '^\\s*(\\d*\\.?\\d+)\\s*(\\w+)?'</li>
  <li><b>byte_string_re:</b> re.compile('^\\s*(\\d*\\.?\\d+)\\s*(\\w+)?', re.IGNORECASE)</li>
  <li><b>conjugate:</b> <method 'conjugate' of 'int' objects></li>
  <li><b>denominator:</b> <attribute 'denominator' of 'int' objects></li>
  <li><b>from_bytes:</b> <built-in method from_bytes of type object at 0x5644ae68c190></li>
  <details><summary><b>def human_readable(self, decimal: 'bool' = False, separator: 'str' = '') -> 'str'</b></summary>
  <p>Converts a byte size to a human readable string.

Args:
    decimal: If True, use decimal units (e.g. 1000 bytes per KB). If False, use binary units
        (e.g. 1024 bytes per KiB).
    separator: A string used to split the value and unit. Defaults to an empty string ('').

Returns:
    A human readable string representation of the byte size.</p>
  </details>
  <li><b>imag:</b> <attribute 'imag' of 'int' objects></li>
  <li><b>numerator:</b> <attribute 'numerator' of 'int' objects></li>
  <li><b>real:</b> <attribute 'real' of 'int' objects></li>
  <details><summary><b>def to(self, unit: 'str') -> 'float'</b></summary>
  <p>Converts a byte size to another unit, including both byte and bit units.

Args:
    unit: The unit to convert to. Must be one of the following: B, KB, MB, GB, TB, PB, EB,
        KiB, MiB, GiB, TiB, PiB, EiB (byte units) and
        bit, kbit, mbit, gbit, tbit, pbit, ebit,
        kibit, mibit, gibit, tibit, pibit, eibit (bit units).

Returns:
    The byte size in the new unit.</p>
  </details>
  <li><b>to_bytes:</b> <method 'to_bytes' of 'int' objects></li>
  </details>
  <li><b>ClickHouseDsn:</b> typing.Annotated[pydantic_core._pydantic_core.Url, UrlConstraints(max_length=None, allowed_schemes=['clickhouse+native', 'clickhouse+asynch'], host_required=None, default_host='localhost', default_port=9000, default_path=None)]</li>
  <li><b>CockroachDsn:</b> typing.Annotated[pydantic_core._pydantic_core.Url, UrlConstraints(max_length=None, allowed_schemes=['cockroachdb', 'cockroachdb+psycopg2', 'cockroachdb+asyncpg'], host_required=True, default_host=None, default_port=None, default_path=None)]</li>
  <details><summary><h4>class ConfigDict(dict)</h4></summary>
  <li><b>clear:</b> <method 'clear' of 'dict' objects></li>
  <li><b>copy:</b> <method 'copy' of 'dict' objects></li>
  <li><b>fromkeys:</b> <built-in method fromkeys of _TypedDictMeta object at 0x5644ae66c310></li>
  <li><b>get:</b> <method 'get' of 'dict' objects></li>
  <li><b>items:</b> <method 'items' of 'dict' objects></li>
  <li><b>keys:</b> <method 'keys' of 'dict' objects></li>
  <li><b>pop:</b> <method 'pop' of 'dict' objects></li>
  <li><b>popitem:</b> <method 'popitem' of 'dict' objects></li>
  <li><b>setdefault:</b> <method 'setdefault' of 'dict' objects></li>
  <li><b>update:</b> <method 'update' of 'dict' objects></li>
  <li><b>values:</b> <method 'values' of 'dict' objects></li>
  </details>
  <li><b>DirectoryPath:</b> typing.Annotated[pathlib.Path, PathType(path_type='dir')]</li>
  <details><summary><h4>class Discriminator(object)</h4></summary>
  <details><summary><b>def __delattr__(self, name)</b></summary>
  <p>Implement delattr(self, name).</p>
  </details>
  <details><summary><b>def __eq__(self, other)</b></summary>
  <p>Return self==value.</p>
  </details>
  <details><summary><b>def __get_pydantic_core_schema__(self, source_type: 'Any', handler: 'GetCoreSchemaHandler') -> 'CoreSchema'</b></summary>
  </details>
  <details><summary><b>def _dataclass_getstate(self)</b></summary>
  </details>
  <details><summary><b>def __hash__(self)</b></summary>
  <p>Return hash(self).</p>
  </details>
  <details><summary><b>def __init__(self, discriminator: 'str | Callable[[Any], Hashable]', custom_error_type: 'str | None' = None, custom_error_message: 'str | None' = None, custom_error_context: 'dict[str, int | str | float] | None' = None) -> None</b></summary>
  <p>Initialize self.  See help(type(self)) for accurate signature.</p>
  </details>
  <details><summary><b>def __repr__(self)</b></summary>
  <p>Return repr(self).</p>
  </details>
  <details><summary><b>def __setattr__(self, name, value)</b></summary>
  <p>Implement setattr(self, name, value).</p>
  </details>
  <details><summary><b>def _dataclass_setstate(self, state)</b></summary>
  </details>
  <details><summary><b>def _convert_schema(self, original_schema: 'core_schema.CoreSchema') -> 'core_schema.TaggedUnionSchema'</b></summary>
  </details>
  <li><b>custom_error_context:</b> <member 'custom_error_context' of 'Discriminator' objects></li>
  <li><b>custom_error_message:</b> <member 'custom_error_message' of 'Discriminator' objects></li>
  <li><b>custom_error_type:</b> <member 'custom_error_type' of 'Discriminator' objects></li>
  <li><b>discriminator:</b> <member 'discriminator' of 'Discriminator' objects></li>
  </details>
  <details><summary><h4>class EmailStr(object)</h4></summary>
  <details><summary><b>def __get_pydantic_core_schema__(_source: 'type[Any]', _handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'</b></summary>
  </details>
  <details><summary><b>def __get_pydantic_json_schema__(core_schema: 'core_schema.CoreSchema', handler: '_schema_generation_shared.GetJsonSchemaHandler') -> 'JsonSchemaValue'</b></summary>
  </details>
  <details><summary><b>def _validate(input_value: 'str', /) -> 'str'</b></summary>
  </details>
  </details>
  <details><summary><h4>class EncodedBytes(object)</h4></summary>
  <details><summary><b>def __eq__(self, other)</b></summary>
  <p>Return self==value.</p>
  </details>
  <details><summary><b>def __get_pydantic_core_schema__(self, source: 'type[Any]', handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'</b></summary>
  </details>
  <details><summary><b>def __get_pydantic_json_schema__(self, core_schema: 'core_schema.CoreSchema', handler: 'GetJsonSchemaHandler') -> 'JsonSchemaValue'</b></summary>
  </details>
  <details><summary><b>def __hash__(self) -> 'int'</b></summary>
  <p>Return hash(self).</p>
  </details>
  <details><summary><b>def __init__(self, encoder: 'type[EncoderProtocol]') -> None</b></summary>
  <p>Initialize self.  See help(type(self)) for accurate signature.</p>
  </details>
  <details><summary><b>def __repr__(self)</b></summary>
  <p>Return repr(self).</p>
  </details>
  <details><summary><b>def decode(self, data: 'bytes', _: 'core_schema.ValidationInfo') -> 'bytes'</b></summary>
  <p>Decode the data using the specified encoder.

Args:
    data: The data to decode.

Returns:
    The decoded data.</p>
  </details>
  <details><summary><b>def encode(self, value: 'bytes') -> 'bytes'</b></summary>
  <p>Encode the data using the specified encoder.

Args:
    value: The data to encode.

Returns:
    The encoded data.</p>
  </details>
  <li><b>encoder:</b> <member 'encoder' of 'EncodedBytes' objects></li>
  </details>
  <details><summary><h4>class EncodedStr(EncodedBytes)</h4></summary>
  <details><summary><b>def __eq__(self, other)</b></summary>
  <p>Return self==value.</p>
  </details>
  <details><summary><b>def __get_pydantic_core_schema__(self, source: 'type[Any]', handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'</b></summary>
  </details>
  <details><summary><b>def __get_pydantic_json_schema__(self, core_schema: 'core_schema.CoreSchema', handler: 'GetJsonSchemaHandler') -> 'JsonSchemaValue'</b></summary>
  </details>
  <details><summary><b>def __hash__(self) -> 'int'</b></summary>
  <p>Return hash(self).</p>
  </details>
  <details><summary><b>def __init__(self, encoder: 'type[EncoderProtocol]') -> None</b></summary>
  <p>Initialize self.  See help(type(self)) for accurate signature.</p>
  </details>
  <details><summary><b>def __repr__(self)</b></summary>
  <p>Return repr(self).</p>
  </details>
  <details><summary><b>def decode(self, data: 'bytes', _: 'core_schema.ValidationInfo') -> 'bytes'</b></summary>
  <p>Decode the data using the specified encoder.

Args:
    data: The data to decode.

Returns:
    The decoded data.</p>
  </details>
  <details><summary><b>def decode_str(self, data: 'bytes', _: 'core_schema.ValidationInfo') -> 'str'</b></summary>
  <p>Decode the data using the specified encoder.

Args:
    data: The data to decode.

Returns:
    The decoded data.</p>
  </details>
  <details><summary><b>def encode(self, value: 'bytes') -> 'bytes'</b></summary>
  <p>Encode the data using the specified encoder.

Args:
    value: The data to encode.

Returns:
    The encoded data.</p>
  </details>
  <details><summary><b>def encode_str(self, value: 'str') -> 'str'</b></summary>
  <p>Encode the data using the specified encoder.

Args:
    value: The data to encode.

Returns:
    The encoded data.</p>
  </details>
  <li><b>encoder:</b> <member 'encoder' of 'EncodedBytes' objects></li>
  </details>
  <details><summary><h4>class EncoderProtocol(Protocol)</h4></summary>
  <details><summary><b>def __class_getitem__(params)</b></summary>
  <p>Parameterizes a generic class.

At least, parameterizing a generic class is the *main* thing this method
does. For example, for some generic class `Foo`, this is called when we
do `Foo[int]` - there, with `cls=Foo` and `params=int`.

However, note that this method is also called when defining generic
classes in the first place with `class Foo(Generic[T]): ...`.</p>
  </details>
  <details><summary><b>def _no_init(self, *args, **kwargs)</b></summary>
  </details>
  <details><summary><b>def __init_subclass__(*args, **kwargs)</b></summary>
  <p>This method is called when a class is subclassed.

The default implementation does nothing. It may be
overridden to extend subclasses.</p>
  </details>
  <details><summary><b>def _proto_hook(other)</b></summary>
  </details>
  <details><summary><b>def decode(data: 'bytes') -> 'bytes'</b></summary>
  <p>Decode the data using the encoder.

Args:
    data: The data to decode.

Returns:
    The decoded data.</p>
  </details>
  <details><summary><b>def encode(value: 'bytes') -> 'bytes'</b></summary>
  <p>Encode the data using the encoder.

Args:
    value: The data to encode.

Returns:
    The encoded data.</p>
  </details>
  <details><summary><b>def get_json_format() -> 'str'</b></summary>
  <p>Get the JSON format for the encoded data.

Returns:
    The JSON format for the encoded data.</p>
  </details>
  </details>
  <details><summary><h4>class Extra(object)</h4></summary>
  <!-- Error processing item: no signature found for builtin <built-in method __init_subclass__ of _ExtraMeta object at 0x5644ae745350> -->
  <details><summary><h4>class FailFast(PydanticMetadata, BaseMetadata)</h4></summary>
  <details><summary><b>def __eq__(self, other)</b></summary>
  <p>Return self==value.</p>
  </details>
  <details><summary><b>def __init__(self, fail_fast: 'bool' = True) -> None</b></summary>
  <p>Initialize self.  See help(type(self)) for accurate signature.</p>
  </details>
  <details><summary><b>def __pretty__(self, fmt: 'typing.Callable[[Any], Any]', **kwargs: 'Any') -> 'typing.Generator[Any, None, None]'</b></summary>
  <p>Used by devtools (https://python-devtools.helpmanual.io/) to pretty print objects.</p>
  </details>
  <details><summary><b>def __repr__(self)</b></summary>
  <p>Return repr(self).</p>
  </details>
  <details><summary><b>def __repr_args__(self) -> 'ReprArgs'</b></summary>
  <p>Returns the attributes to show in __str__, __repr__, and __pretty__ this is generally overridden.

Can either return:
* name - value pairs, e.g.: `[('foo_name', 'foo'), ('bar_name', ['b', 'a', 'r'])]`
* or, just values, e.g.: `[(None, 'foo'), (None, ['b', 'a', 'r'])]`</p>
  </details>
  <details><summary><b>def __repr_name__(self) -> 'str'</b></summary>
  <p>Name of the instance's class, used in __repr__.</p>
  </details>
  <details><summary><b>def __repr_str__(self, join_str: 'str') -> 'str'</b></summary>
  </details>
  <details><summary><b>def __rich_repr__(self) -> 'RichReprResult'</b></summary>
  <p>Used by Rich (https://rich.readthedocs.io/en/stable/pretty.html) to pretty print objects.</p>
  </details>
  <details><summary><b>def __str__(self) -> 'str'</b></summary>
  <p>Return str(self).</p>
  </details>
  <li><b>fail_fast:</b> True</li>
  </details>
  <details><summary><b>def Field(default: 'Any' = PydanticUndefined, *, default_factory: 'typing.Callable[[], Any] | None' = PydanticUndefined, alias: 'str | None' = PydanticUndefined, alias_priority: 'int | None' = PydanticUndefined, validation_alias: 'str | AliasPath | AliasChoices | None' = PydanticUndefined, serialization_alias: 'str | None' = PydanticUndefined, title: 'str | None' = PydanticUndefined, field_title_generator: 'typing_extensions.Callable[[str, FieldInfo], str] | None' = PydanticUndefined, description: 'str | None' = PydanticUndefined, examples: 'list[Any] | None' = PydanticUndefined, exclude: 'bool | None' = PydanticUndefined, discriminator: 'str | types.Discriminator | None' = PydanticUndefined, deprecated: 'Deprecated | str | bool | None' = PydanticUndefined, json_schema_extra: 'JsonDict | typing.Callable[[JsonDict], None] | None' = PydanticUndefined, frozen: 'bool | None' = PydanticUndefined, validate_default: 'bool | None' = PydanticUndefined, repr: 'bool' = PydanticUndefined, init: 'bool | None' = PydanticUndefined, init_var: 'bool | None' = PydanticUndefined, kw_only: 'bool | None' = PydanticUndefined, pattern: 'str | typing.Pattern[str] | None' = PydanticUndefined, strict: 'bool | None' = PydanticUndefined, coerce_numbers_to_str: 'bool | None' = PydanticUndefined, gt: 'annotated_types.SupportsGt | None' = PydanticUndefined, ge: 'annotated_types.SupportsGe | None' = PydanticUndefined, lt: 'annotated_types.SupportsLt | None' = PydanticUndefined, le: 'annotated_types.SupportsLe | None' = PydanticUndefined, multiple_of: 'float | None' = PydanticUndefined, allow_inf_nan: 'bool | None' = PydanticUndefined, max_digits: 'int | None' = PydanticUndefined, decimal_places: 'int | None' = PydanticUndefined, min_length: 'int | None' = PydanticUndefined, max_length: 'int | None' = PydanticUndefined, union_mode: "Literal['smart', 'left_to_right']" = PydanticUndefined, fail_fast: 'bool | None' = PydanticUndefined, **extra: 'Unpack[_EmptyKwargs]') -> 'Any'</b></summary>
  <p>Usage docs: https://docs.pydantic.dev/2.9/concepts/fields

Create a field for objects that can be configured.

Used to provide extra information about a field, either for the model schema or complex validation. Some arguments
apply only to number fields (`int`, `float`, `Decimal`) and some apply only to `str`.

Note:
    - Any `_Unset` objects will be replaced by the corresponding value defined in the `_DefaultValues` dictionary. If a key for the `_Unset` object is not found in the `_DefaultValues` dictionary, it will default to `None`

Args:
    default: Default value if the field is not set.
    default_factory: A callable to generate the default value, such as :func:`~datetime.utcnow`.
    alias: The name to use for the attribute when validating or serializing by alias.
        This is often used for things like converting between snake and camel case.
    alias_priority: Priority of the alias. This affects whether an alias generator is used.
    validation_alias: Like `alias`, but only affects validation, not serialization.
    serialization_alias: Like `alias`, but only affects serialization, not validation.
    title: Human-readable title.
    field_title_generator: A callable that takes a field name and returns title for it.
    description: Human-readable description.
    examples: Example values for this field.
    exclude: Whether to exclude the field from the model serialization.
    discriminator: Field name or Discriminator for discriminating the type in a tagged union.
    deprecated: A deprecation message, an instance of `warnings.deprecated` or the `typing_extensions.deprecated` backport,
        or a boolean. If `True`, a default deprecation message will be emitted when accessing the field.
    json_schema_extra: A dict or callable to provide extra JSON schema properties.
    frozen: Whether the field is frozen. If true, attempts to change the value on an instance will raise an error.
    validate_default: If `True`, apply validation to the default value every time you create an instance.
        Otherwise, for performance reasons, the default value of the field is trusted and not validated.
    repr: A boolean indicating whether to include the field in the `__repr__` output.
    init: Whether the field should be included in the constructor of the dataclass.
        (Only applies to dataclasses.)
    init_var: Whether the field should _only_ be included in the constructor of the dataclass.
        (Only applies to dataclasses.)
    kw_only: Whether the field should be a keyword-only argument in the constructor of the dataclass.
        (Only applies to dataclasses.)
    coerce_numbers_to_str: Whether to enable coercion of any `Number` type to `str` (not applicable in `strict` mode).
    strict: If `True`, strict validation is applied to the field.
        See [Strict Mode](../concepts/strict_mode.md) for details.
    gt: Greater than. If set, value must be greater than this. Only applicable to numbers.
    ge: Greater than or equal. If set, value must be greater than or equal to this. Only applicable to numbers.
    lt: Less than. If set, value must be less than this. Only applicable to numbers.
    le: Less than or equal. If set, value must be less than or equal to this. Only applicable to numbers.
    multiple_of: Value must be a multiple of this. Only applicable to numbers.
    min_length: Minimum length for iterables.
    max_length: Maximum length for iterables.
    pattern: Pattern for strings (a regular expression).
    allow_inf_nan: Allow `inf`, `-inf`, `nan`. Only applicable to numbers.
    max_digits: Maximum number of allow digits for strings.
    decimal_places: Maximum number of decimal places allowed for numbers.
    union_mode: The strategy to apply when validating a union. Can be `smart` (the default), or `left_to_right`.
        See [Union Mode](../concepts/unions.md#union-modes) for details.
    fail_fast: If `True`, validation will stop on the first error. If `False`, all validation errors will be collected.
        This option can be applied only to iterable types (list, tuple, set, and frozenset).
    extra: (Deprecated) Extra fields that will be included in the JSON schema.

        !!! warning Deprecated
            The `extra` kwargs is deprecated. Use `json_schema_extra` instead.

Returns:
    A new [`FieldInfo`][pydantic.fields.FieldInfo]. The return annotation is `Any` so `Field` can be used on
        type-annotated fields without causing a type error.</p>
  </details>
  <details><summary><h4>class FieldSerializationInfo(SerializationInfo, Protocol)</h4></summary>
  <details><summary><b>def __class_getitem__(params)</b></summary>
  <p>Parameterizes a generic class.

At least, parameterizing a generic class is the *main* thing this method
does. For example, for some generic class `Foo`, this is called when we
do `Foo[int]` - there, with `cls=Foo` and `params=int`.

However, note that this method is also called when defining generic
classes in the first place with `class Foo(Generic[T]): ...`.</p>
  </details>
  <details><summary><b>def _no_init_or_replace_init(self, *args, **kwargs)</b></summary>
  </details>
  <details><summary><b>def __init_subclass__(*args, **kwargs)</b></summary>
  <p>This method is called when a class is subclassed.

The default implementation does nothing. It may be
overridden to extend subclasses.</p>
  </details>
  <details><summary><b>def __repr__(self) -> 'str'</b></summary>
  <p>Return repr(self).</p>
  </details>
  <details><summary><b>def __str__(self) -> 'str'</b></summary>
  <p>Return str(self).</p>
  </details>
  <details><summary><b>def _proto_hook(other)</b></summary>
  </details>
  <li><b>by_alias:</b> <property object at 0x7fb1736ba480></li>
  <li><b>context:</b> <property object at 0x7fb1736ba430></li>
  <li><b>exclude:</b> <property object at 0x7fb17368b830></li>
  <li><b>exclude_defaults:</b> <property object at 0x7fb1736ba520></li>
  <li><b>exclude_none:</b> <property object at 0x7fb1736ba570></li>
  <li><b>exclude_unset:</b> <property object at 0x7fb1736ba4d0></li>
  <li><b>field_name:</b> <property object at 0x7fb1736ba660></li>
  <li><b>include:</b> <property object at 0x7fb17368ae30></li>
  <li><b>mode:</b> <property object at 0x7fb1736ba3e0></li>
  <details><summary><b>def mode_is_json(self) -> 'bool'</b></summary>
  </details>
  <details><summary><b>def round_trip(self) -> 'bool'</b></summary>
  </details>
  <li><b>serialize_as_any:</b> <property object at 0x7fb1736ba5c0></li>
  </details>
  <li><b>FilePath:</b> typing.Annotated[pathlib.Path, PathType(path_type='file')]</li>
  <li><b>FileUrl:</b> typing.Annotated[pydantic_core._pydantic_core.Url, UrlConstraints(max_length=None, allowed_schemes=['file'], host_required=None, default_host=None, default_port=None, default_path=None)]</li>
  <li><b>FiniteFloat:</b> typing.Annotated[float, AllowInfNan(allow_inf_nan=False)]</li>
  <li><b>FtpUrl:</b> typing.Annotated[pydantic_core._pydantic_core.Url, UrlConstraints(max_length=None, allowed_schemes=['ftp'], host_required=None, default_host=None, default_port=None, default_path=None)]</li>
  <details><summary><h4>class FutureDate(object)</h4></summary>
  <details><summary><b>def __get_pydantic_core_schema__(source: 'type[Any]', handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'</b></summary>
  </details>
  <details><summary><b>def __repr__(self) -> 'str'</b></summary>
  <p>Return repr(self).</p>
  </details>
  </details>
  <details><summary><h4>class FutureDatetime(object)</h4></summary>
  <details><summary><b>def __get_pydantic_core_schema__(source: 'type[Any]', handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'</b></summary>
  </details>
  <details><summary><b>def __repr__(self) -> 'str'</b></summary>
  <p>Return repr(self).</p>
  </details>
  </details>
  <details><summary><h4>class GenerateSchema(object)</h4></summary>
  <li><b>CollectedInvalid:</b> <class 'pydantic._internal._generate_schema.GenerateSchema.CollectedInvalid'></li>
  <details><summary><b>def __from_parent(config_wrapper_stack: 'ConfigWrapperStack', types_namespace_stack: 'TypesNamespaceStack', model_type_stack: '_ModelTypeStack', typevars_map: 'dict[Any, Any] | None', defs: '_Definitions') -> 'GenerateSchema'</b></summary>
  </details>
  <details><summary><b>def __init__(self, config_wrapper: 'ConfigWrapper', types_namespace: 'dict[str, Any] | None', typevars_map: 'dict[Any, Any] | None' = None) -> 'None'</b></summary>
  <p>Initialize self.  See help(type(self)) for accurate signature.</p>
  </details>
  <details><summary><b>def _add_js_function(self, metadata_schema: 'CoreSchema', js_function: 'Callable[..., Any]') -> 'None'</b></summary>
  </details>
  <details><summary><b>def _annotated_schema(self, annotated_type: 'Any') -> 'core_schema.CoreSchema'</b></summary>
  <p>Generate schema for an Annotated type, e.g. `Annotated[int, Field(...)]` or `Annotated[int, Gt(0)]`.</p>
  </details>
  <details><summary><b>def _apply_alias_generator_to_computed_field_info(alias_generator: 'Callable[[str], str] | AliasGenerator', computed_field_info: 'ComputedFieldInfo', computed_field_name: 'str')</b></summary>
  <p>Apply an alias_generator to alias on a ComputedFieldInfo instance if appropriate.

Args:
    alias_generator: A callable that takes a string and returns a string, or an AliasGenerator instance.
    computed_field_info: The ComputedFieldInfo instance to which the alias_generator is (maybe) applied.
    computed_field_name: The name of the computed field from which to generate the alias.</p>
  </details>
  <details><summary><b>def _apply_alias_generator_to_field_info(alias_generator: 'Callable[[str], str] | AliasGenerator', field_info: 'FieldInfo', field_name: 'str') -> 'None'</b></summary>
  <p>Apply an alias_generator to aliases on a FieldInfo instance if appropriate.

Args:
    alias_generator: A callable that takes a string and returns a string, or an AliasGenerator instance.
    field_info: The FieldInfo instance to which the alias_generator is (maybe) applied.
    field_name: The name of the field from which to generate the alias.</p>
  </details>
  <details><summary><b>def _apply_annotations(self, source_type: 'Any', annotations: 'list[Any]', transform_inner_schema: 'Callable[[CoreSchema], CoreSchema]' = <function GenerateSchema.<lambda> at 0x7fb17313ea20>) -> 'CoreSchema'</b></summary>
  <p>Apply arguments from `Annotated` or from `FieldInfo` to a schema.

This gets called by `GenerateSchema._annotated_schema` but differs from it in that it does
not expect `source_type` to be an `Annotated` object, it expects it to be  the first argument of that
(in other words, `GenerateSchema._annotated_schema` just unpacks `Annotated`, this process it).</p>
  </details>
  <details><summary><b>def _apply_discriminator_to_union(self, schema: 'CoreSchema', discriminator: 'str | Discriminator | None') -> 'CoreSchema'</b></summary>
  </details>
  <details><summary><b>def _apply_field_serializers(self, schema: 'core_schema.CoreSchema', serializers: 'list[Decorator[FieldSerializerDecoratorInfo]]', computed_field: 'bool' = False) -> 'core_schema.CoreSchema'</b></summary>
  <p>Apply field serializers to a schema.</p>
  </details>
  <details><summary><b>def _apply_field_title_generator_to_field_info(config_wrapper: 'ConfigWrapper', field_info: 'FieldInfo | ComputedFieldInfo', field_name: 'str') -> 'None'</b></summary>
  <p>Apply a field_title_generator on a FieldInfo or ComputedFieldInfo instance if appropriate
Args:
    config_wrapper: The config of the model
    field_info: The FieldInfo or ComputedField instance to which the title_generator is (maybe) applied.
    field_name: The name of the field from which to generate the title.</p>
  </details>
  <details><summary><b>def _apply_model_serializers(self, schema: 'core_schema.CoreSchema', serializers: 'Iterable[Decorator[ModelSerializerDecoratorInfo]]') -> 'core_schema.CoreSchema'</b></summary>
  <p>Apply model serializers to a schema.</p>
  </details>
  <details><summary><b>def _apply_single_annotation(self, schema: 'core_schema.CoreSchema', metadata: 'Any') -> 'core_schema.CoreSchema'</b></summary>
  </details>
  <details><summary><b>def _apply_single_annotation_json_schema(self, schema: 'core_schema.CoreSchema', metadata: 'Any') -> 'core_schema.CoreSchema'</b></summary>
  </details>
  <details><summary><b>def _arbitrary_type_schema(self, tp: 'Any') -> 'CoreSchema'</b></summary>
  </details>
  <details><summary><b>def _callable_schema(self, function: 'Callable[..., Any]') -> 'core_schema.CallSchema'</b></summary>
  <p>Generate schema for a Callable.

TODO support functional validators once we support them in Config</p>
  </details>
  <details><summary><b>def _common_field_schema(self, name: 'str', field_info: 'FieldInfo', decorators: 'DecoratorInfos') -> '_CommonField'</b></summary>
  </details>
  <details><summary><b>def _computed_field_schema(self, d: 'Decorator[ComputedFieldInfo]', field_serializers: 'dict[str, Decorator[FieldSerializerDecoratorInfo]]') -> 'core_schema.ComputedField'</b></summary>
  </details>
  <details><summary><b>def _dataclass_schema(self, dataclass: 'type[StandardDataclass]', origin: 'type[StandardDataclass] | None') -> 'core_schema.CoreSchema'</b></summary>
  <p>Generate schema for a dataclass.</p>
  </details>
  <details><summary><b>def _dict_schema(self, keys_type: 'Any', values_type: 'Any') -> 'CoreSchema'</b></summary>
  </details>
  <details><summary><b>def _enum_schema(self, enum_type: 'type[Enum]') -> 'CoreSchema'</b></summary>
  </details>
  <details><summary><b>def _frozenset_schema(self, items_type: 'Any') -> 'CoreSchema'</b></summary>
  </details>
  <details><summary><b>def _generate_dc_field_schema(self, name: 'str', field_info: 'FieldInfo', decorators: 'DecoratorInfos') -> 'core_schema.DataclassField'</b></summary>
  <p>Prepare a DataclassField to represent the parameter/field, of a dataclass.</p>
  </details>
  <details><summary><b>def _generate_md_field_schema(self, name: 'str', field_info: 'FieldInfo', decorators: 'DecoratorInfos') -> 'core_schema.ModelField'</b></summary>
  <p>Prepare a ModelField to represent a model field.</p>
  </details>
  <details><summary><b>def _generate_parameter_schema(self, name: 'str', annotation: 'type[Any]', default: 'Any', mode: "Literal['positional_only', 'positional_or_keyword', 'keyword_only'] | None" = None) -> 'core_schema.ArgumentsParameter'</b></summary>
  <p>Prepare a ArgumentsParameter to represent a field in a namedtuple or function signature.</p>
  </details>
  <details><summary><b>def _generate_schema_from_property(self, obj: 'Any', source: 'Any') -> 'core_schema.CoreSchema | None'</b></summary>
  <p>Try to generate schema from either the `__get_pydantic_core_schema__` function or
`__pydantic_core_schema__` property.

Note: `__get_pydantic_core_schema__` takes priority so it can
decide whether to use a `__pydantic_core_schema__` attribute, or generate a fresh schema.</p>
  </details>
  <details><summary><b>def _generate_schema_inner(self, obj: 'Any') -> 'core_schema.CoreSchema'</b></summary>
  </details>
  <details><summary><b>def _generate_td_field_schema(self, name: 'str', field_info: 'FieldInfo', decorators: 'DecoratorInfos', *, required: 'bool' = True) -> 'core_schema.TypedDictField'</b></summary>
  <p>Prepare a TypedDictField to represent a model or typeddict field.</p>
  </details>
  <details><summary><b>def _get_args_resolving_forward_refs(self, obj: 'Any', required: 'bool' = False) -> 'tuple[Any, ...] | None'</b></summary>
  </details>
  <details><summary><b>def _get_first_arg_or_any(self, obj: 'Any') -> 'Any'</b></summary>
  </details>
  <details><summary><b>def _get_first_two_args_or_any(self, obj: 'Any') -> 'tuple[Any, Any]'</b></summary>
  </details>
  <details><summary><b>def _get_model_title_from_config(model: 'type[BaseModel | StandardDataclass]', config_wrapper: 'ConfigWrapper | None' = None) -> 'str | None'</b></summary>
  <p>Get the title of a model if `model_title_generator` or `title` are set in the config, else return None</p>
  </details>
  <details><summary><b>def _get_prepare_pydantic_annotations_for_known_type(self, obj: 'Any', annotations: 'tuple[Any, ...]') -> 'tuple[Any, list[Any]] | None'</b></summary>
  </details>
  <details><summary><b>def _get_wrapped_inner_schema(self, get_inner_schema: 'GetCoreSchemaHandler', annotation: 'Any', pydantic_js_annotation_functions: 'list[GetJsonSchemaFunction]') -> 'CallbackGetCoreSchemaHandler'</b></summary>
  </details>
  <details><summary><b>def _hashable_schema(self) -> 'core_schema.CoreSchema'</b></summary>
  </details>
  <details><summary><b>def _ip_schema(self, tp: 'Any') -> 'CoreSchema'</b></summary>
  </details>
  <details><summary><b>def _iterable_schema(self, type_: 'Any') -> 'core_schema.GeneratorSchema'</b></summary>
  <p>Generate a schema for an `Iterable`.</p>
  </details>
  <details><summary><b>def _list_schema(self, items_type: 'Any') -> 'CoreSchema'</b></summary>
  </details>
  <details><summary><b>def _literal_schema(self, literal_type: 'Any') -> 'CoreSchema'</b></summary>
  <p>Generate schema for a Literal.</p>
  </details>
  <details><summary><b>def _match_generic_type(self, obj: 'Any', origin: 'Any') -> 'CoreSchema'</b></summary>
  </details>
  <details><summary><b>def _model_schema(self, cls: 'type[BaseModel]') -> 'core_schema.CoreSchema'</b></summary>
  <p>Generate schema for a Pydantic model.</p>
  </details>
  <details><summary><b>def _namedtuple_schema(self, namedtuple_cls: 'Any', origin: 'Any') -> 'core_schema.CoreSchema'</b></summary>
  <p>Generate schema for a NamedTuple.</p>
  </details>
  <details><summary><b>def _pattern_schema(self, pattern_type: 'Any') -> 'core_schema.CoreSchema'</b></summary>
  </details>
  <details><summary><b>def _resolve_forward_ref(self, obj: 'Any') -> 'Any'</b></summary>
  </details>
  <details><summary><b>def _sequence_schema(self, items_type: 'Any') -> 'core_schema.CoreSchema'</b></summary>
  <p>Generate schema for a Sequence, e.g. `Sequence[int]`.</p>
  </details>
  <details><summary><b>def _set_schema(self, items_type: 'Any') -> 'CoreSchema'</b></summary>
  </details>
  <details><summary><b>def _subclass_schema(self, type_: 'Any') -> 'core_schema.CoreSchema'</b></summary>
  <p>Generate schema for a Type, e.g. `Type[int]`.</p>
  </details>
  <details><summary><b>def _tuple_schema(self, tuple_type: 'Any') -> 'core_schema.CoreSchema'</b></summary>
  <p>Generate schema for a Tuple, e.g. `tuple[int, str]` or `tuple[int, ...]`.</p>
  </details>
  <details><summary><b>def _type_alias_type_schema(self, obj: 'Any') -> 'CoreSchema'</b></summary>
  </details>
  <details><summary><b>def _type_schema(self) -> 'core_schema.CoreSchema'</b></summary>
  </details>
  <details><summary><b>def _typed_dict_schema(self, typed_dict_cls: 'Any', origin: 'Any') -> 'core_schema.CoreSchema'</b></summary>
  <p>Generate schema for a TypedDict.

It is not possible to track required/optional keys in TypedDict without __required_keys__
since TypedDict.__new__ erases the base classes (it replaces them with just `dict`)
and thus we can track usage of total=True/False
__required_keys__ was added in Python 3.9
(https://github.com/miss-islington/cpython/blob/1e9939657dd1f8eb9f596f77c1084d2d351172fc/Doc/library/typing.rst?plain=1#L1546-L1548)
however it is buggy
(https://github.com/python/typing_extensions/blob/ac52ac5f2cb0e00e7988bae1e2a1b8257ac88d6d/src/typing_extensions.py#L657-L666).

On 3.11 but < 3.12 TypedDict does not preserve inheritance information.

Hence to avoid creating validators that do not do what users expect we only
support typing.TypedDict on Python >= 3.12 or typing_extension.TypedDict on all versions</p>
  </details>
  <details><summary><b>def _union_is_subclass_schema(self, union_type: 'Any') -> 'core_schema.CoreSchema'</b></summary>
  <p>Generate schema for `Type[Union[X, ...]]`.</p>
  </details>
  <details><summary><b>def _union_schema(self, union_type: 'Any') -> 'core_schema.CoreSchema'</b></summary>
  <p>Generate schema for a Union.</p>
  </details>
  <details><summary><b>def _unknown_type_schema(self, obj: 'Any') -> 'CoreSchema'</b></summary>
  </details>
  <details><summary><b>def _unpack_refs_defs(self, schema: 'CoreSchema') -> 'CoreSchema'</b></summary>
  <p>Unpack all 'definitions' schemas into `GenerateSchema.defs.definitions`
and return the inner schema.</p>
  </details>
  <details><summary><b>def _unsubstituted_typevar_schema(self, typevar: 'typing.TypeVar') -> 'core_schema.CoreSchema'</b></summary>
  </details>
  <details><summary><b>def _zoneinfo_schema(self) -> 'core_schema.CoreSchema'</b></summary>
  <p>Generate schema for a zone_info.ZoneInfo object</p>
  </details>
  <details><summary><b>def clean_schema(self, schema: 'CoreSchema') -> 'CoreSchema'</b></summary>
  </details>
  <details><summary><b>def collect_definitions(self, schema: 'CoreSchema') -> 'CoreSchema'</b></summary>
  </details>
  <li><b>defs:</b> <member 'defs' of 'GenerateSchema' objects></li>
  <li><b>field_name_stack:</b> <member 'field_name_stack' of 'GenerateSchema' objects></li>
  <details><summary><b>def generate_schema(self, obj: 'Any', from_dunder_get_core_schema: 'bool' = True) -> 'core_schema.CoreSchema'</b></summary>
  <p>Generate core schema.

Args:
    obj: The object to generate core schema for.
    from_dunder_get_core_schema: Whether to generate schema from either the
        `__get_pydantic_core_schema__` function or `__pydantic_core_schema__` property.

Returns:
    The generated core schema.

Raises:
    PydanticUndefinedAnnotation:
        If it is not possible to evaluate forward reference.
    PydanticSchemaGenerationError:
        If it is not possible to generate pydantic-core schema.
    TypeError:
        - If `alias_generator` returns a disallowed type (must be str, AliasPath or AliasChoices).
        - If V1 style validator with `each_item=True` applied on a wrong field.
    PydanticUserError:
        - If `typing.TypedDict` is used instead of `typing_extensions.TypedDict` on Python < 3.12.
        - If `__modify_schema__` method is used instead of `__get_pydantic_json_schema__`.</p>
  </details>
  <details><summary><b>def match_type(self, obj: 'Any') -> 'core_schema.CoreSchema'</b></summary>
  <p>Main mapping of types to schemas.

The general structure is a series of if statements starting with the simple cases
(non-generic primitive types) and then handling generics and other more complex cases.

Each case either generates a schema directly, calls into a public user-overridable method
(like `GenerateSchema.tuple_variable_schema`) or calls into a private method that handles some
boilerplate before calling into the user-facing method (e.g. `GenerateSchema._tuple_schema`).

The idea is that we'll evolve this into adding more and more user facing methods over time
as they get requested and we figure out what the right API for them is.</p>
  </details>
  <li><b>model_type_stack:</b> <member 'model_type_stack' of 'GenerateSchema' objects></li>
  <details><summary><b>def str_schema(self) -> 'CoreSchema'</b></summary>
  <p>Generate a CoreSchema for `str`</p>
  </details>
  </details>
  <details><summary><h4>class GetCoreSchemaHandler(object)</h4></summary>
  <details><summary><b>def __call__(self, source_type: 'Any', /) -> 'core_schema.CoreSchema'</b></summary>
  <p>Call the inner handler and get the CoreSchema it returns.
This will call the next CoreSchema modifying function up until it calls
into Pydantic's internal schema generation machinery, which will raise a
`pydantic.errors.PydanticSchemaGenerationError` error if it cannot generate
a CoreSchema for the given source type.

Args:
    source_type: The input type.

Returns:
    CoreSchema: The `pydantic-core` CoreSchema generated.</p>
  </details>
  <details><summary><b>def _get_types_namespace(self) -> 'dict[str, Any] | None'</b></summary>
  <p>Internal method used during type resolution for serializer annotations.</p>
  </details>
  <li><b>field_name:</b> <property object at 0x7fb17350d030></li>
  <details><summary><b>def generate_schema(self, source_type: 'Any', /) -> 'core_schema.CoreSchema'</b></summary>
  <p>Generate a schema unrelated to the current context.
Use this function if e.g. you are handling schema generation for a sequence
and want to generate a schema for its items.
Otherwise, you may end up doing something like applying a `min_length` constraint
that was intended for the sequence itself to its items!

Args:
    source_type: The input type.

Returns:
    CoreSchema: The `pydantic-core` CoreSchema generated.</p>
  </details>
  <details><summary><b>def resolve_ref_schema(self, maybe_ref_schema: 'core_schema.CoreSchema', /) -> 'core_schema.CoreSchema'</b></summary>
  <p>Get the real schema for a `definition-ref` schema.
If the schema given is not a `definition-ref` schema, it will be returned as is.
This means you don't have to check before calling this function.

Args:
    maybe_ref_schema: A `CoreSchema`, `ref`-based or not.

Raises:
    LookupError: If the `ref` is not found.

Returns:
    A concrete `CoreSchema`.</p>
  </details>
  </details>
  <details><summary><h4>class GetJsonSchemaHandler(object)</h4></summary>
  <details><summary><b>def __call__(self, core_schema: 'CoreSchemaOrField', /) -> 'JsonSchemaValue'</b></summary>
  <p>Call the inner handler and get the JsonSchemaValue it returns.
This will call the next JSON schema modifying function up until it calls
into `pydantic.json_schema.GenerateJsonSchema`, which will raise a
`pydantic.errors.PydanticInvalidForJsonSchema` error if it cannot generate
a JSON schema.

Args:
    core_schema: A `pydantic_core.core_schema.CoreSchema`.

Returns:
    JsonSchemaValue: The JSON schema generated by the inner JSON schema modify
    functions.</p>
  </details>
  <details><summary><b>def resolve_ref_schema(self, maybe_ref_json_schema: 'JsonSchemaValue', /) -> 'JsonSchemaValue'</b></summary>
  <p>Get the real schema for a `{"$ref": ...}` schema.
If the schema given is not a `$ref` schema, it will be returned as is.
This means you don't have to check before calling this function.

Args:
    maybe_ref_json_schema: A JsonSchemaValue which may be a `$ref` schema.

Raises:
    LookupError: If the ref is not found.

Returns:
    JsonSchemaValue: A JsonSchemaValue that has no `$ref`.</p>
  </details>
  </details>
  <details><summary><h4>class GetPydanticSchema(object)</h4></summary>
  <details><summary><b>def __eq__(self, other)</b></summary>
  <p>Return self==value.</p>
  </details>
  <details><summary><b>def __getattr__(self, item: 'str') -> 'Any'</b></summary>
  <p>Use this rather than defining `__get_pydantic_core_schema__` etc. to reduce the number of nested calls.</p>
  </details>
  <details><summary><b>def __init__(self, get_pydantic_core_schema: 'Callable[[Any, GetCoreSchemaHandler], CoreSchema] | None' = None, get_pydantic_json_schema: 'Callable[[Any, GetJsonSchemaHandler], JsonSchemaValue] | None' = None) -> None</b></summary>
  <p>Initialize self.  See help(type(self)) for accurate signature.</p>
  </details>
  <details><summary><b>def __repr__(self)</b></summary>
  <p>Return repr(self).</p>
  </details>
  <li><b>get_pydantic_core_schema:</b> <member 'get_pydantic_core_schema' of 'GetPydanticSchema' objects></li>
  <li><b>get_pydantic_json_schema:</b> <member 'get_pydantic_json_schema' of 'GetPydanticSchema' objects></li>
  </details>
  <li><b>HttpUrl:</b> typing.Annotated[pydantic_core._pydantic_core.Url, UrlConstraints(max_length=2083, allowed_schemes=['http', 'https'], host_required=None, default_host=None, default_port=None, default_path=None)]</li>
  <details><summary><h4>class IPvAnyAddress(object)</h4></summary>
  <details><summary><b>def __get_pydantic_core_schema__(_source: 'type[Any]', _handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'</b></summary>
  </details>
  <details><summary><b>def __get_pydantic_json_schema__(core_schema: 'core_schema.CoreSchema', handler: '_schema_generation_shared.GetJsonSchemaHandler') -> 'JsonSchemaValue'</b></summary>
  </details>
  <details><summary><b>def __new__(cls, value: 'Any') -> 'IPvAnyAddressType'</b></summary>
  <p>Validate an IPv4 or IPv6 address.</p>
  </details>
  <details><summary><b>def _validate(input_value: 'Any', /) -> 'IPvAnyAddressType'</b></summary>
  </details>
  </details>
  <details><summary><h4>class IPvAnyInterface(object)</h4></summary>
  <details><summary><b>def __get_pydantic_core_schema__(_source: 'type[Any]', _handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'</b></summary>
  </details>
  <details><summary><b>def __get_pydantic_json_schema__(core_schema: 'core_schema.CoreSchema', handler: '_schema_generation_shared.GetJsonSchemaHandler') -> 'JsonSchemaValue'</b></summary>
  </details>
  <details><summary><b>def __new__(cls, value: 'NetworkType') -> 'IPvAnyInterfaceType'</b></summary>
  <p>Validate an IPv4 or IPv6 interface.</p>
  </details>
  <details><summary><b>def _validate(input_value: 'NetworkType', /) -> 'IPvAnyInterfaceType'</b></summary>
  </details>
  </details>
  <details><summary><h4>class IPvAnyNetwork(object)</h4></summary>
  <details><summary><b>def __get_pydantic_core_schema__(_source: 'type[Any]', _handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'</b></summary>
  </details>
  <details><summary><b>def __get_pydantic_json_schema__(core_schema: 'core_schema.CoreSchema', handler: '_schema_generation_shared.GetJsonSchemaHandler') -> 'JsonSchemaValue'</b></summary>
  </details>
  <details><summary><b>def __new__(cls, value: 'NetworkType') -> 'IPvAnyNetworkType'</b></summary>
  <p>Validate an IPv4 or IPv6 network.</p>
  </details>
  <details><summary><b>def _validate(input_value: 'NetworkType', /) -> 'IPvAnyNetworkType'</b></summary>
  </details>
  </details>
  <details><summary><h4>class ImportString(object)</h4></summary>
  <details><summary><b>def __class_getitem__(item: 'AnyType') -> 'AnyType'</b></summary>
  </details>
  <details><summary><b>def __get_pydantic_core_schema__(source: 'type[Any]', handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'</b></summary>
  </details>
  <details><summary><b>def __get_pydantic_json_schema__(cs: 'CoreSchema', handler: 'GetJsonSchemaHandler') -> 'JsonSchemaValue'</b></summary>
  </details>
  <details><summary><b>def __repr__(self) -> 'str'</b></summary>
  <p>Return repr(self).</p>
  </details>
  <details><summary><b>def _serialize(v: 'Any') -> 'str'</b></summary>
  </details>
  </details>
  <details><summary><h4>class InstanceOf(object)</h4></summary>
  <details><summary><b>def __class_getitem__(item: 'AnyType') -> 'AnyType'</b></summary>
  </details>
  <details><summary><b>def __eq__(self, other)</b></summary>
  <p>Return self==value.</p>
  </details>
  <details><summary><b>def __get_pydantic_core_schema__(source: 'Any', handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'</b></summary>
  </details>
  <details><summary><b>def __init__(self) -> None</b></summary>
  <p>Initialize self.  See help(type(self)) for accurate signature.</p>
  </details>
  <details><summary><b>def __repr__(self)</b></summary>
  <p>Return repr(self).</p>
  </details>
  </details>
  <details><summary><h4>class Json(object)</h4></summary>
  <details><summary><b>def __class_getitem__(item: 'AnyType') -> 'AnyType'</b></summary>
  </details>
  <details><summary><b>def __eq__(self, other: 'Any') -> 'bool'</b></summary>
  <p>Return self==value.</p>
  </details>
  <details><summary><b>def __get_pydantic_core_schema__(source: 'Any', handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'</b></summary>
  </details>
  <details><summary><b>def __hash__(self) -> 'int'</b></summary>
  <p>Return hash(self).</p>
  </details>
  <details><summary><b>def __repr__(self) -> 'str'</b></summary>
  <p>Return repr(self).</p>
  </details>
  </details>
  <li><b>JsonValue:</b> JsonValue</li>
  <li><b>KafkaDsn:</b> typing.Annotated[pydantic_core._pydantic_core.Url, UrlConstraints(max_length=None, allowed_schemes=['kafka'], host_required=None, default_host='localhost', default_port=9092, default_path=None)]</li>
  <li><b>MariaDBDsn:</b> typing.Annotated[pydantic_core._pydantic_core.Url, UrlConstraints(max_length=None, allowed_schemes=['mariadb', 'mariadb+mariadbconnector', 'mariadb+pymysql'], host_required=None, default_host=None, default_port=3306, default_path=None)]</li>
  <li><b>MongoDsn:</b> typing.Annotated[pydantic_core._pydantic_core.MultiHostUrl, UrlConstraints(max_length=None, allowed_schemes=['mongodb', 'mongodb+srv'], host_required=None, default_host=None, default_port=27017, default_path=None)]</li>
  <li><b>MySQLDsn:</b> typing.Annotated[pydantic_core._pydantic_core.Url, UrlConstraints(max_length=None, allowed_schemes=['mysql', 'mysql+mysqlconnector', 'mysql+aiomysql', 'mysql+asyncmy', 'mysql+mysqldb', 'mysql+pymysql', 'mysql+cymysql', 'mysql+pyodbc'], host_required=None, default_host=None, default_port=3306, default_path=None)]</li>
  <details><summary><h4>class NaiveDatetime(object)</h4></summary>
  <details><summary><b>def __get_pydantic_core_schema__(source: 'type[Any]', handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'</b></summary>
  </details>
  <details><summary><b>def __repr__(self) -> 'str'</b></summary>
  <p>Return repr(self).</p>
  </details>
  </details>
  <details><summary><h4>class NameEmail(Representation)</h4></summary>
  <details><summary><b>def __eq__(self, other: 'Any') -> 'bool'</b></summary>
  <p>Return self==value.</p>
  </details>
  <details><summary><b>def __get_pydantic_core_schema__(_source: 'type[Any]', _handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'</b></summary>
  </details>
  <details><summary><b>def __get_pydantic_json_schema__(core_schema: 'core_schema.CoreSchema', handler: '_schema_generation_shared.GetJsonSchemaHandler') -> 'JsonSchemaValue'</b></summary>
  </details>
  <details><summary><b>def __init__(self, name: 'str', email: 'str')</b></summary>
  <p>Initialize self.  See help(type(self)) for accurate signature.</p>
  </details>
  <details><summary><b>def __pretty__(self, fmt: 'typing.Callable[[Any], Any]', **kwargs: 'Any') -> 'typing.Generator[Any, None, None]'</b></summary>
  <p>Used by devtools (https://python-devtools.helpmanual.io/) to pretty print objects.</p>
  </details>
  <details><summary><b>def __repr__(self) -> 'str'</b></summary>
  <p>Return repr(self).</p>
  </details>
  <details><summary><b>def __repr_args__(self) -> 'ReprArgs'</b></summary>
  <p>Returns the attributes to show in __str__, __repr__, and __pretty__ this is generally overridden.

Can either return:
* name - value pairs, e.g.: `[('foo_name', 'foo'), ('bar_name', ['b', 'a', 'r'])]`
* or, just values, e.g.: `[(None, 'foo'), (None, ['b', 'a', 'r'])]`</p>
  </details>
  <details><summary><b>def __repr_name__(self) -> 'str'</b></summary>
  <p>Name of the instance's class, used in __repr__.</p>
  </details>
  <details><summary><b>def __repr_str__(self, join_str: 'str') -> 'str'</b></summary>
  </details>
  <details><summary><b>def __rich_repr__(self) -> 'RichReprResult'</b></summary>
  <p>Used by Rich (https://rich.readthedocs.io/en/stable/pretty.html) to pretty print objects.</p>
  </details>
  <details><summary><b>def __str__(self) -> 'str'</b></summary>
  <p>Return str(self).</p>
  </details>
  <details><summary><b>def _validate(input_value: 'Self | str', /) -> 'Self'</b></summary>
  </details>
  <li><b>email:</b> <member 'email' of 'NameEmail' objects></li>
  <li><b>name:</b> <member 'name' of 'NameEmail' objects></li>
  </details>
  <li><b>NatsDsn:</b> typing.Annotated[pydantic_core._pydantic_core.MultiHostUrl, UrlConstraints(max_length=None, allowed_schemes=['nats', 'tls', 'ws', 'wss'], host_required=None, default_host='localhost', default_port=4222, default_path=None)]</li>
  <li><b>NegativeFloat:</b> typing.Annotated[float, Lt(lt=0)]</li>
  <li><b>NegativeInt:</b> typing.Annotated[int, Lt(lt=0)]</li>
  <li><b>NewPath:</b> typing.Annotated[pathlib.Path, PathType(path_type='new')]</li>
  <li><b>NonNegativeFloat:</b> typing.Annotated[float, Ge(ge=0)]</li>
  <li><b>NonNegativeInt:</b> typing.Annotated[int, Ge(ge=0)]</li>
  <li><b>NonPositiveFloat:</b> typing.Annotated[float, Le(le=0)]</li>
  <li><b>NonPositiveInt:</b> typing.Annotated[int, Le(le=0)]</li>
  <li><b>OnErrorOmit:</b> typing.Annotated[~T, <class 'pydantic.types._OnErrorOmit'>]</li>
  <details><summary><h4>class PastDate(object)</h4></summary>
  <details><summary><b>def __get_pydantic_core_schema__(source: 'type[Any]', handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'</b></summary>
  </details>
  <details><summary><b>def __repr__(self) -> 'str'</b></summary>
  <p>Return repr(self).</p>
  </details>
  </details>
  <details><summary><h4>class PastDatetime(object)</h4></summary>
  <details><summary><b>def __get_pydantic_core_schema__(source: 'type[Any]', handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'</b></summary>
  </details>
  <details><summary><b>def __repr__(self) -> 'str'</b></summary>
  <p>Return repr(self).</p>
  </details>
  </details>
  <details><summary><h4>class PaymentCardNumber(str)</h4></summary>
  <details><summary><b>def __get_pydantic_core_schema__(source: 'type[Any]', handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'</b></summary>
  </details>
  <details><summary><b>def __init__(self, card_number: 'str')</b></summary>
  <p>Initialize self.  See help(type(self)) for accurate signature.</p>
  </details>
  <!-- Error processing item: no signature found for builtin <built-in method __init_subclass__ of type object at 0x5644ae68bab0> -->
  <details><summary><h4>class PlainSerializer(object)</h4></summary>
  <details><summary><b>def __delattr__(self, name)</b></summary>
  <p>Implement delattr(self, name).</p>
  </details>
  <details><summary><b>def __eq__(self, other)</b></summary>
  <p>Return self==value.</p>
  </details>
  <details><summary><b>def __get_pydantic_core_schema__(self, source_type: 'Any', handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'</b></summary>
  <p>Gets the Pydantic core schema.

Args:
    source_type: The source type.
    handler: The `GetCoreSchemaHandler` instance.

Returns:
    The Pydantic core schema.</p>
  </details>
  <details><summary><b>def _dataclass_getstate(self)</b></summary>
  </details>
  <details><summary><b>def __hash__(self)</b></summary>
  <p>Return hash(self).</p>
  </details>
  <details><summary><b>def __init__(self, func: 'core_schema.SerializerFunction', return_type: 'Any' = PydanticUndefined, when_used: 'WhenUsed' = 'always') -> None</b></summary>
  <p>Initialize self.  See help(type(self)) for accurate signature.</p>
  </details>
  <details><summary><b>def __repr__(self)</b></summary>
  <p>Return repr(self).</p>
  </details>
  <details><summary><b>def __setattr__(self, name, value)</b></summary>
  <p>Implement setattr(self, name, value).</p>
  </details>
  <details><summary><b>def _dataclass_setstate(self, state)</b></summary>
  </details>
  <li><b>func:</b> <member 'func' of 'PlainSerializer' objects></li>
  <li><b>return_type:</b> <member 'return_type' of 'PlainSerializer' objects></li>
  <li><b>when_used:</b> <member 'when_used' of 'PlainSerializer' objects></li>
  </details>
  <details><summary><h4>class PlainValidator(object)</h4></summary>
  <details><summary><b>def __delattr__(self, name)</b></summary>
  <p>Implement delattr(self, name).</p>
  </details>
  <details><summary><b>def __eq__(self, other)</b></summary>
  <p>Return self==value.</p>
  </details>
  <details><summary><b>def __get_pydantic_core_schema__(self, source_type: 'Any', handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'</b></summary>
  </details>
  <details><summary><b>def _dataclass_getstate(self)</b></summary>
  </details>
  <details><summary><b>def __hash__(self)</b></summary>
  <p>Return hash(self).</p>
  </details>
  <details><summary><b>def __init__(self, func: 'core_schema.NoInfoValidatorFunction | core_schema.WithInfoValidatorFunction', json_schema_input_type: 'Any' = typing.Any) -> None</b></summary>
  <p>Initialize self.  See help(type(self)) for accurate signature.</p>
  </details>
  <details><summary><b>def __repr__(self)</b></summary>
  <p>Return repr(self).</p>
  </details>
  <details><summary><b>def __setattr__(self, name, value)</b></summary>
  <p>Implement setattr(self, name, value).</p>
  </details>
  <details><summary><b>def _dataclass_setstate(self, state)</b></summary>
  </details>
  <details><summary><b>def _from_decorator(decorator: '_decorators.Decorator[_decorators.FieldValidatorDecoratorInfo]') -> 'Self'</b></summary>
  </details>
  <li><b>func:</b> <member 'func' of 'PlainValidator' objects></li>
  <li><b>json_schema_input_type:</b> <member 'json_schema_input_type' of 'PlainValidator' objects></li>
  </details>
  <li><b>PositiveFloat:</b> typing.Annotated[float, Gt(gt=0)]</li>
  <li><b>PositiveInt:</b> typing.Annotated[int, Gt(gt=0)]</li>
  <li><b>PostgresDsn:</b> typing.Annotated[pydantic_core._pydantic_core.MultiHostUrl, UrlConstraints(max_length=None, allowed_schemes=['postgres', 'postgresql', 'postgresql+asyncpg', 'postgresql+pg8000', 'postgresql+psycopg', 'postgresql+psycopg2', 'postgresql+psycopg2cffi', 'postgresql+py-postgresql', 'postgresql+pygresql'], host_required=True, default_host=None, default_port=None, default_path=None)]</li>
  <details><summary><b>def PrivateAttr(default: 'Any' = PydanticUndefined, *, default_factory: 'typing.Callable[[], Any] | None' = None, init: 'Literal[False]' = False) -> 'Any'</b></summary>
  <p>Usage docs: https://docs.pydantic.dev/2.9/concepts/models/#private-model-attributes

Indicates that an attribute is intended for private use and not handled during normal validation/serialization.

Private attributes are not validated by Pydantic, so it's up to you to ensure they are used in a type-safe manner.

Private attributes are stored in `__private_attributes__` on the model.

Args:
    default: The attribute's default value. Defaults to Undefined.
    default_factory: Callable that will be
        called when a default value is needed for this attribute.
        If both `default` and `default_factory` are set, an error will be raised.
    init: Whether the attribute should be included in the constructor of the dataclass. Always `False`.

Returns:
    An instance of [`ModelPrivateAttr`][pydantic.fields.ModelPrivateAttr] class.

Raises:
    ValueError: If both `default` and `default_factory` are set.</p>
  </details>
  <details><summary><h4>class PydanticDeprecatedSince20(PydanticDeprecationWarning)</h4></summary>
  <details><summary><b>def __init__(self, message: 'str', *args: 'object') -> 'None'</b></summary>
  <p>Initialize self.  See help(type(self)) for accurate signature.</p>
  </details>
  <details><summary><b>def __str__(self) -> 'str'</b></summary>
  <p>Return str(self).</p>
  </details>
  <li><b>add_note:</b> <method 'add_note' of 'BaseException' objects></li>
  <li><b>args:</b> <attribute 'args' of 'BaseException' objects></li>
  <li><b>with_traceback:</b> <method 'with_traceback' of 'BaseException' objects></li>
  </details>
  <details><summary><h4>class PydanticDeprecatedSince26(PydanticDeprecationWarning)</h4></summary>
  <details><summary><b>def __init__(self, message: 'str', *args: 'object') -> 'None'</b></summary>
  <p>Initialize self.  See help(type(self)) for accurate signature.</p>
  </details>
  <details><summary><b>def __str__(self) -> 'str'</b></summary>
  <p>Return str(self).</p>
  </details>
  <li><b>add_note:</b> <method 'add_note' of 'BaseException' objects></li>
  <li><b>args:</b> <attribute 'args' of 'BaseException' objects></li>
  <li><b>with_traceback:</b> <method 'with_traceback' of 'BaseException' objects></li>
  </details>
  <details><summary><h4>class PydanticDeprecatedSince29(PydanticDeprecationWarning)</h4></summary>
  <details><summary><b>def __init__(self, message: 'str', *args: 'object') -> 'None'</b></summary>
  <p>Initialize self.  See help(type(self)) for accurate signature.</p>
  </details>
  <details><summary><b>def __str__(self) -> 'str'</b></summary>
  <p>Return str(self).</p>
  </details>
  <li><b>add_note:</b> <method 'add_note' of 'BaseException' objects></li>
  <li><b>args:</b> <attribute 'args' of 'BaseException' objects></li>
  <li><b>with_traceback:</b> <method 'with_traceback' of 'BaseException' objects></li>
  </details>
  <details><summary><h4>class PydanticDeprecationWarning(DeprecationWarning)</h4></summary>
  <details><summary><b>def __init__(self, message: 'str', *args: 'object', since: 'tuple[int, int]', expected_removal: 'tuple[int, int] | None' = None) -> 'None'</b></summary>
  <p>Initialize self.  See help(type(self)) for accurate signature.</p>
  </details>
  <details><summary><b>def __str__(self) -> 'str'</b></summary>
  <p>Return str(self).</p>
  </details>
  <li><b>add_note:</b> <method 'add_note' of 'BaseException' objects></li>
  <li><b>args:</b> <attribute 'args' of 'BaseException' objects></li>
  <li><b>with_traceback:</b> <method 'with_traceback' of 'BaseException' objects></li>
  </details>
  <li><b>PydanticErrorCodes:</b> typing.Literal['class-not-fully-defined', 'custom-json-schema', 'decorator-missing-field', 'discriminator-no-field', 'discriminator-alias-type', 'discriminator-needs-literal', 'discriminator-alias', 'discriminator-validator', 'callable-discriminator-no-tag', 'typed-dict-version', 'model-field-overridden', 'model-field-missing-annotation', 'config-both', 'removed-kwargs', 'invalid-for-json-schema', 'json-schema-already-used', 'base-model-instantiated', 'undefined-annotation', 'schema-for-unknown-type', 'import-error', 'create-model-field-definitions', 'create-model-config-base', 'validator-no-fields', 'validator-invalid-fields', 'validator-instance-method', 'validator-input-type', 'root-validator-pre-skip', 'model-serializer-instance-method', 'validator-field-config-info', 'validator-v1-signature', 'validator-signature', 'field-serializer-signature', 'model-serializer-signature', 'multiple-field-serializers', 'invalid-annotated-type', 'type-adapter-config-unused', 'root-model-extra', 'unevaluable-type-annotation', 'dataclass-init-false-extra-allow', 'clashing-init-and-init-var', 'model-config-invalid-field-name', 'with-config-on-model', 'dataclass-on-model']</li>
  <details><summary><h4>class PydanticExperimentalWarning(Warning)</h4></summary>
  <li><b>add_note:</b> <method 'add_note' of 'BaseException' objects></li>
  <li><b>args:</b> <attribute 'args' of 'BaseException' objects></li>
  <li><b>with_traceback:</b> <method 'with_traceback' of 'BaseException' objects></li>
  </details>
  <details><summary><h4>class PydanticImportError(PydanticErrorMixin, ImportError)</h4></summary>
  <details><summary><b>def __init__(self, message: 'str') -> 'None'</b></summary>
  <p>Initialize self.  See help(type(self)) for accurate signature.</p>
  </details>
  <details><summary><b>def __str__(self) -> 'str'</b></summary>
  <p>Return str(self).</p>
  </details>
  <li><b>add_note:</b> <method 'add_note' of 'BaseException' objects></li>
  <li><b>args:</b> <attribute 'args' of 'BaseException' objects></li>
  <li><b>msg:</b> <member 'msg' of 'ImportError' objects></li>
  <li><b>name:</b> <member 'name' of 'ImportError' objects></li>
  <li><b>path:</b> <member 'path' of 'ImportError' objects></li>
  <li><b>with_traceback:</b> <method 'with_traceback' of 'BaseException' objects></li>
  </details>
  <details><summary><h4>class PydanticInvalidForJsonSchema(PydanticUserError)</h4></summary>
  <details><summary><b>def __init__(self, message: 'str') -> 'None'</b></summary>
  <p>Initialize self.  See help(type(self)) for accurate signature.</p>
  </details>
  <details><summary><b>def __str__(self) -> 'str'</b></summary>
  <p>Return str(self).</p>
  </details>
  <li><b>add_note:</b> <method 'add_note' of 'BaseException' objects></li>
  <li><b>args:</b> <attribute 'args' of 'BaseException' objects></li>
  <li><b>with_traceback:</b> <method 'with_traceback' of 'BaseException' objects></li>
  </details>
  <details><summary><h4>class PydanticSchemaGenerationError(PydanticUserError)</h4></summary>
  <details><summary><b>def __init__(self, message: 'str') -> 'None'</b></summary>
  <p>Initialize self.  See help(type(self)) for accurate signature.</p>
  </details>
  <details><summary><b>def __str__(self) -> 'str'</b></summary>
  <p>Return str(self).</p>
  </details>
  <li><b>add_note:</b> <method 'add_note' of 'BaseException' objects></li>
  <li><b>args:</b> <attribute 'args' of 'BaseException' objects></li>
  <li><b>with_traceback:</b> <method 'with_traceback' of 'BaseException' objects></li>
  </details>
  <details><summary><h4>class PydanticUndefinedAnnotation(PydanticErrorMixin, NameError)</h4></summary>
  <details><summary><b>def __init__(self, name: 'str', message: 'str') -> 'None'</b></summary>
  <p>Initialize self.  See help(type(self)) for accurate signature.</p>
  </details>
  <details><summary><b>def __str__(self) -> 'str'</b></summary>
  <p>Return str(self).</p>
  </details>
  <li><b>add_note:</b> <method 'add_note' of 'BaseException' objects></li>
  <li><b>args:</b> <attribute 'args' of 'BaseException' objects></li>
  <details><summary><b>def from_name_error(name_error: 'NameError') -> 'Self'</b></summary>
  <p>Convert a `NameError` to a `PydanticUndefinedAnnotation` error.

Args:
    name_error: `NameError` to be converted.

Returns:
    Converted `PydanticUndefinedAnnotation` error.</p>
  </details>
  <li><b>name:</b> <member 'name' of 'NameError' objects></li>
  <li><b>with_traceback:</b> <method 'with_traceback' of 'BaseException' objects></li>
  </details>
  <details><summary><h4>class PydanticUserError(PydanticErrorMixin, TypeError)</h4></summary>
  <details><summary><b>def __init__(self, message: 'str', *, code: 'PydanticErrorCodes | None') -> 'None'</b></summary>
  <p>Initialize self.  See help(type(self)) for accurate signature.</p>
  </details>
  <details><summary><b>def __str__(self) -> 'str'</b></summary>
  <p>Return str(self).</p>
  </details>
  <li><b>add_note:</b> <method 'add_note' of 'BaseException' objects></li>
  <li><b>args:</b> <attribute 'args' of 'BaseException' objects></li>
  <li><b>with_traceback:</b> <method 'with_traceback' of 'BaseException' objects></li>
  </details>
  <li><b>RedisDsn:</b> typing.Annotated[pydantic_core._pydantic_core.Url, UrlConstraints(max_length=None, allowed_schemes=['redis', 'rediss'], host_required=None, default_host='localhost', default_port=6379, default_path='/0')]</li>
  <details><summary><h4>class RootModel(BaseModel, Generic)</h4></summary>
  <details><summary><b>def __class_getitem__(typevar_values: 'type[Any] | tuple[type[Any], ...]') -> 'type[BaseModel] | _forward_ref.PydanticRecursiveRef'</b></summary>
  <p>Parameterizes a generic class.

At least, parameterizing a generic class is the *main* thing this method
does. For example, for some generic class `Foo`, this is called when we
do `Foo[int]` - there, with `cls=Foo` and `params=int`.

However, note that this method is also called when defining generic
classes in the first place with `class Foo(Generic[T]): ...`.</p>
  </details>
  <details><summary><b>def __copy__(self) -> 'Self'</b></summary>
  <p>Returns a shallow copy of the model.</p>
  </details>
  <details><summary><b>def __deepcopy__(self, memo: 'dict[int, Any] | None' = None) -> 'Self'</b></summary>
  <p>Returns a deep copy of the model.</p>
  </details>
  <details><summary><b>def __delattr__(self, item: 'str') -> 'Any'</b></summary>
  <p>Implement delattr(self, name).</p>
  </details>
  <details><summary><b>def __eq__(self, other: 'Any') -> 'bool'</b></summary>
  <p>Return self==value.</p>
  </details>
  <details><summary><b>def __get_pydantic_core_schema__(source: 'type[BaseModel]', handler: 'GetCoreSchemaHandler', /) -> 'CoreSchema'</b></summary>
  <p>Hook into generating the model's CoreSchema.

Args:
    source: The class we are generating a schema for.
        This will generally be the same as the `cls` argument if this is a classmethod.
    handler: A callable that calls into Pydantic's internal CoreSchema generation logic.

Returns:
    A `pydantic-core` `CoreSchema`.</p>
  </details>
  <details><summary><b>def __get_pydantic_json_schema__(core_schema: 'CoreSchema', handler: 'GetJsonSchemaHandler', /) -> 'JsonSchemaValue'</b></summary>
  <p>Hook into generating the model's JSON schema.

Args:
    core_schema: A `pydantic-core` CoreSchema.
        You can ignore this argument and call the handler with a new CoreSchema,
        wrap this CoreSchema (`{'type': 'nullable', 'schema': current_schema}`),
        or just call the handler with the original schema.
    handler: Call into Pydantic's internal JSON schema generation.
        This will raise a `pydantic.errors.PydanticInvalidForJsonSchema` if JSON schema
        generation fails.
        Since this gets called by `BaseModel.model_json_schema` you can override the
        `schema_generator` argument to that function to change JSON schema generation globally
        for a type.

Returns:
    A JSON schema, as a Python object.</p>
  </details>
  <details><summary><b>def __getattr__(self, item: 'str') -> 'Any'</b></summary>
  </details>
  <details><summary><b>def __getstate__(self) -> 'dict[Any, Any]'</b></summary>
  <p>Helper for pickle.</p>
  </details>
  <details><summary><b>def __init__(self, /, root: 'RootModelRootType' = PydanticUndefined, **data) -> 'None'</b></summary>
  <p>Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.</p>
  </details>
  <details><summary><b>def __init_subclass__(**kwargs)</b></summary>
  <p>This method is called when a class is subclassed.

The default implementation does nothing. It may be
overridden to extend subclasses.</p>
  </details>
  <details><summary><b>def __iter__(self) -> 'TupleGenerator'</b></summary>
  <p>So `dict(model)` works.</p>
  </details>
  <details><summary><b>def __pretty__(self, fmt: 'typing.Callable[[Any], Any]', **kwargs: 'Any') -> 'typing.Generator[Any, None, None]'</b></summary>
  <p>Used by devtools (https://python-devtools.helpmanual.io/) to pretty print objects.</p>
  </details>
  <details><summary><b>def __pydantic_init_subclass__(**kwargs: 'Any') -> 'None'</b></summary>
  <p>This is intended to behave just like `__init_subclass__`, but is called by `ModelMetaclass`
only after the class is actually fully initialized. In particular, attributes like `model_fields` will
be present when this is called.

This is necessary because `__init_subclass__` will always be called by `type.__new__`,
and it would require a prohibitively large refactor to the `ModelMetaclass` to ensure that
`type.__new__` was called in such a manner that the class would already be sufficiently initialized.

This will receive the same `kwargs` that would be passed to the standard `__init_subclass__`, namely,
any kwargs passed to the class definition that aren't used internally by pydantic.

Args:
    **kwargs: Any keyword arguments passed to the class definition that aren't used internally
        by pydantic.</p>
  </details>
  <details><summary><b>def __repr__(self) -> 'str'</b></summary>
  <p>Return repr(self).</p>
  </details>
  <details><summary><b>def __repr_args__(self) -> '_repr.ReprArgs'</b></summary>
  </details>
  <details><summary><b>def __repr_name__(self) -> 'str'</b></summary>
  <p>Name of the instance's class, used in __repr__.</p>
  </details>
  <details><summary><b>def __repr_str__(self, join_str: 'str') -> 'str'</b></summary>
  </details>
  <details><summary><b>def __rich_repr__(self) -> 'RichReprResult'</b></summary>
  <p>Used by Rich (https://rich.readthedocs.io/en/stable/pretty.html) to pretty print objects.</p>
  </details>
  <details><summary><b>def __setattr__(self, name: 'str', value: 'Any') -> 'None'</b></summary>
  <p>Implement setattr(self, name, value).</p>
  </details>
  <details><summary><b>def __setstate__(self, state: 'dict[Any, Any]') -> 'None'</b></summary>
  </details>
  <details><summary><b>def __str__(self) -> 'str'</b></summary>
  <p>Return str(self).</p>
  </details>
  <details><summary><b>def _calculate_keys(self, *args: 'Any', **kwargs: 'Any') -> 'Any'</b></summary>
  </details>
  <details><summary><b>def _check_frozen(self, name: 'str', value: 'Any') -> 'None'</b></summary>
  </details>
  <details><summary><b>def _copy_and_set_values(self, *args: 'Any', **kwargs: 'Any') -> 'Any'</b></summary>
  </details>
  <details><summary><b>def _get_value(*args: 'Any', **kwargs: 'Any') -> 'Any'</b></summary>
  </details>
  <details><summary><b>def _iter(self, *args: 'Any', **kwargs: 'Any') -> 'Any'</b></summary>
  </details>
  <details><summary><b>def construct(_fields_set: 'set[str] | None' = None, **values: 'Any') -> 'Self'</b></summary>
  </details>
  <details><summary><b>def copy(self, *, include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False) -> 'Self'</b></summary>
  <p>Returns a copy of the model.

!!! warning "Deprecated"
    This method is now deprecated; use `model_copy` instead.

If you need `include` or `exclude`, use:

```py
data = self.model_dump(include=include, exclude=exclude, round_trip=True)
data = {**data, **(update or {})}
copied = self.model_validate(data)
```

Args:
    include: Optional set or mapping specifying which fields to include in the copied model.
    exclude: Optional set or mapping specifying which fields to exclude in the copied model.
    update: Optional dictionary of field-value pairs to override field values in the copied model.
    deep: If True, the values of fields that are Pydantic models will be deep-copied.

Returns:
    A copy of the model with included, excluded and updated fields as specified.</p>
  </details>
  <details><summary><b>def dict(self, *, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False) -> 'Dict[str, Any]'</b></summary>
  </details>
  <details><summary><b>def from_orm(obj: 'Any') -> 'Self'</b></summary>
  </details>
  <details><summary><b>def json(self, *, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any') -> 'str'</b></summary>
  </details>
  <li><b>model_computed_fields:</b> {}</li>
  <li><b>model_config:</b> {}</li>
  <details><summary><b>def model_construct(root: 'RootModelRootType', _fields_set: 'set[str] | None' = None) -> 'Self'</b></summary>
  <p>Create a new model using the provided root object and update fields set.

Args:
    root: The root object of the model.
    _fields_set: The set of fields to be updated.

Returns:
    The new model.

Raises:
    NotImplemented: If the model is not a subclass of `RootModel`.</p>
  </details>
  <details><summary><b>def model_copy(self, *, update: 'dict[str, Any] | None' = None, deep: 'bool' = False) -> 'Self'</b></summary>
  <p>Usage docs: https://docs.pydantic.dev/2.9/concepts/serialization/#model_copy

Returns a copy of the model.

Args:
    update: Values to change/add in the new model. Note: the data is not validated
        before creating the new model. You should trust this data.
    deep: Set to `True` to make a deep copy of the model.

Returns:
    New model instance.</p>
  </details>
  <details><summary><b>def model_dump(self, *, mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, serialize_as_any: 'bool' = False) -> 'dict[str, Any]'</b></summary>
  <p>Usage docs: https://docs.pydantic.dev/2.9/concepts/serialization/#modelmodel_dump

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

Args:
    mode: The mode in which `to_python` should run.
        If mode is 'json', the output will only contain JSON serializable types.
        If mode is 'python', the output may contain non-JSON-serializable Python objects.
    include: A set of fields to include in the output.
    exclude: A set of fields to exclude from the output.
    context: Additional context to pass to the serializer.
    by_alias: Whether to use the field's alias in the dictionary key if defined.
    exclude_unset: Whether to exclude fields that have not been explicitly set.
    exclude_defaults: Whether to exclude fields that are set to their default value.
    exclude_none: Whether to exclude fields that have a value of `None`.
    round_trip: If True, dumped values should be valid as input for non-idempotent types such as Json[T].
    warnings: How to handle serialization errors. False/"none" ignores them, True/"warn" logs errors,
        "error" raises a [`PydanticSerializationError`][pydantic_core.PydanticSerializationError].
    serialize_as_any: Whether to serialize fields with duck-typing serialization behavior.

Returns:
    A dictionary representation of the model.</p>
  </details>
  <details><summary><b>def model_dump_json(self, *, indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, serialize_as_any: 'bool' = False) -> 'str'</b></summary>
  <p>Usage docs: https://docs.pydantic.dev/2.9/concepts/serialization/#modelmodel_dump_json

Generates a JSON representation of the model using Pydantic's `to_json` method.

Args:
    indent: Indentation to use in the JSON output. If None is passed, the output will be compact.
    include: Field(s) to include in the JSON output.
    exclude: Field(s) to exclude from the JSON output.
    context: Additional context to pass to the serializer.
    by_alias: Whether to serialize using field aliases.
    exclude_unset: Whether to exclude fields that have not been explicitly set.
    exclude_defaults: Whether to exclude fields that are set to their default value.
    exclude_none: Whether to exclude fields that have a value of `None`.
    round_trip: If True, dumped values should be valid as input for non-idempotent types such as Json[T].
    warnings: How to handle serialization errors. False/"none" ignores them, True/"warn" logs errors,
        "error" raises a [`PydanticSerializationError`][pydantic_core.PydanticSerializationError].
    serialize_as_any: Whether to serialize fields with duck-typing serialization behavior.

Returns:
    A JSON string representation of the model.</p>
  </details>
  <li><b>model_extra:</b> <property object at 0x7fb1730d98a0></li>
  <li><b>model_fields:</b> {'root': FieldInfo(annotation=~RootModelRootType, required=True)}</li>
  <li><b>model_fields_set:</b> <property object at 0x7fb1730da200></li>
  <details><summary><b>def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation') -> 'dict[str, Any]'</b></summary>
  <p>Generates a JSON schema for a model class.

Args:
    by_alias: Whether to use attribute aliases or not.
    ref_template: The reference template.
    schema_generator: To override the logic used to generate the JSON schema, as a subclass of
        `GenerateJsonSchema` with your desired modifications
    mode: The mode in which to generate the schema.

Returns:
    The JSON schema for the given model class.</p>
  </details>
  <details><summary><b>def model_parametrized_name(params: 'tuple[type[Any], ...]') -> 'str'</b></summary>
  <p>Compute the class name for parametrizations of generic classes.

This method can be overridden to achieve a custom naming scheme for generic BaseModels.

Args:
    params: Tuple of types of the class. Given a generic class
        `Model` with 2 type variables and a concrete model `Model[str, int]`,
        the value `(str, int)` would be passed to `params`.

Returns:
    String representing the new class where `params` are passed to `cls` as type variables.

Raises:
    TypeError: Raised when trying to generate concrete names for non-generic models.</p>
  </details>
  <details><summary><b>def model_post_init(self, _BaseModel__context: 'Any') -> 'None'</b></summary>
  <p>Override this method to perform additional initialization after `__init__` and `model_construct`.
This is useful if you want to do some validation that requires the entire model to be initialized.</p>
  </details>
  <details><summary><b>def model_rebuild(*, force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'dict[str, Any] | None' = None) -> 'bool | None'</b></summary>
  <p>Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annotations is a ForwardRef which could not be resolved during
the initial attempt to build the schema, and automatic rebuilding fails.

Args:
    force: Whether to force the rebuilding of the model schema, defaults to `False`.
    raise_errors: Whether to raise errors, defaults to `True`.
    _parent_namespace_depth: The depth level of the parent namespace, defaults to 2.
    _types_namespace: The types namespace, defaults to `None`.

Returns:
    Returns `None` if the schema is already "complete" and rebuilding was not required.
    If rebuilding _was_ required, returns `True` if rebuilding was successful, otherwise `False`.</p>
  </details>
  <details><summary><b>def model_validate(obj: 'Any', *, strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None) -> 'Self'</b></summary>
  <p>Validate a pydantic model instance.

Args:
    obj: The object to validate.
    strict: Whether to enforce types strictly.
    from_attributes: Whether to extract data from object attributes.
    context: Additional context to pass to the validator.

Raises:
    ValidationError: If the object could not be validated.

Returns:
    The validated model instance.</p>
  </details>
  <details><summary><b>def model_validate_json(json_data: 'str | bytes | bytearray', *, strict: 'bool | None' = None, context: 'Any | None' = None) -> 'Self'</b></summary>
  <p>Usage docs: https://docs.pydantic.dev/2.9/concepts/json/#json-parsing

Validate the given JSON data against the Pydantic model.

Args:
    json_data: The JSON data to validate.
    strict: Whether to enforce types strictly.
    context: Extra variables to pass to the validator.

Returns:
    The validated Pydantic model.

Raises:
    ValidationError: If `json_data` is not a JSON string or the object could not be validated.</p>
  </details>
  <details><summary><b>def model_validate_strings(obj: 'Any', *, strict: 'bool | None' = None, context: 'Any | None' = None) -> 'Self'</b></summary>
  <p>Validate the given object with string data against the Pydantic model.

Args:
    obj: The object containing string data to validate.
    strict: Whether to enforce types strictly.
    context: Extra variables to pass to the validator.

Returns:
    The validated Pydantic model.</p>
  </details>
  <details><summary><b>def parse_file(path: 'str | Path', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'</b></summary>
  </details>
  <details><summary><b>def parse_obj(obj: 'Any') -> 'Self'</b></summary>
  </details>
  <details><summary><b>def parse_raw(b: 'str | bytes', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'</b></summary>
  </details>
  <details><summary><b>def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}') -> 'Dict[str, Any]'</b></summary>
  </details>
  <details><summary><b>def schema_json(*, by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any') -> 'str'</b></summary>
  </details>
  <details><summary><b>def update_forward_refs(**localns: 'Any') -> 'None'</b></summary>
  </details>
  <details><summary><b>def validate(value: 'Any') -> 'Self'</b></summary>
  </details>
  </details>
  <details><summary><h4>class Secret(_SecretBase)</h4></summary>
  <details><summary><b>def __class_getitem__(params)</b></summary>
  <p>Parameterizes a generic class.

At least, parameterizing a generic class is the *main* thing this method
does. For example, for some generic class `Foo`, this is called when we
do `Foo[int]` - there, with `cls=Foo` and `params=int`.

However, note that this method is also called when defining generic
classes in the first place with `class Foo(Generic[T]): ...`.</p>
  </details>
  <details><summary><b>def __eq__(self, other: 'Any') -> 'bool'</b></summary>
  <p>Return self==value.</p>
  </details>
  <details><summary><b>def __get_pydantic_core_schema__(source: 'type[Any]', handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'</b></summary>
  </details>
  <details><summary><b>def __hash__(self) -> 'int'</b></summary>
  <p>Return hash(self).</p>
  </details>
  <details><summary><b>def __init__(self, secret_value: 'SecretType') -> 'None'</b></summary>
  <p>Initialize self.  See help(type(self)) for accurate signature.</p>
  </details>
  <details><summary><b>def __init_subclass__(*args, **kwargs)</b></summary>
  <p>This method is called when a class is subclassed.

The default implementation does nothing. It may be
overridden to extend subclasses.</p>
  </details>
  <details><summary><b>def __repr__(self) -> 'str'</b></summary>
  <p>Return repr(self).</p>
  </details>
  <details><summary><b>def __str__(self) -> 'str'</b></summary>
  <p>Return str(self).</p>
  </details>
  <details><summary><b>def _display(self) -> 'str | bytes'</b></summary>
  </details>
  <details><summary><b>def get_secret_value(self) -> 'SecretType'</b></summary>
  <p>Get the secret value.

Returns:
    The secret value.</p>
  </details>
  </details>
  <details><summary><h4>class SecretBytes(_SecretField)</h4></summary>
  <details><summary><b>def __class_getitem__(params)</b></summary>
  <p>Parameterizes a generic class.

At least, parameterizing a generic class is the *main* thing this method
does. For example, for some generic class `Foo`, this is called when we
do `Foo[int]` - there, with `cls=Foo` and `params=int`.

However, note that this method is also called when defining generic
classes in the first place with `class Foo(Generic[T]): ...`.</p>
  </details>
  <details><summary><b>def __eq__(self, other: 'Any') -> 'bool'</b></summary>
  <p>Return self==value.</p>
  </details>
  <details><summary><b>def __get_pydantic_core_schema__(source: 'type[Any]', handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'</b></summary>
  </details>
  <details><summary><b>def __hash__(self) -> 'int'</b></summary>
  <p>Return hash(self).</p>
  </details>
  <details><summary><b>def __init__(self, secret_value: 'SecretType') -> 'None'</b></summary>
  <p>Initialize self.  See help(type(self)) for accurate signature.</p>
  </details>
  <details><summary><b>def __init_subclass__(*args, **kwargs)</b></summary>
  <p>This method is called when a class is subclassed.

The default implementation does nothing. It may be
overridden to extend subclasses.</p>
  </details>
  <details><summary><b>def __len__(self) -> 'int'</b></summary>
  </details>
  <details><summary><b>def __repr__(self) -> 'str'</b></summary>
  <p>Return repr(self).</p>
  </details>
  <details><summary><b>def __str__(self) -> 'str'</b></summary>
  <p>Return str(self).</p>
  </details>
  <details><summary><b>def _display(self) -> 'bytes'</b></summary>
  </details>
  <details><summary><b>def get_secret_value(self) -> 'SecretType'</b></summary>
  <p>Get the secret value.

Returns:
    The secret value.</p>
  </details>
  </details>
  <details><summary><h4>class SecretStr(_SecretField)</h4></summary>
  <details><summary><b>def __class_getitem__(params)</b></summary>
  <p>Parameterizes a generic class.

At least, parameterizing a generic class is the *main* thing this method
does. For example, for some generic class `Foo`, this is called when we
do `Foo[int]` - there, with `cls=Foo` and `params=int`.

However, note that this method is also called when defining generic
classes in the first place with `class Foo(Generic[T]): ...`.</p>
  </details>
  <details><summary><b>def __eq__(self, other: 'Any') -> 'bool'</b></summary>
  <p>Return self==value.</p>
  </details>
  <details><summary><b>def __get_pydantic_core_schema__(source: 'type[Any]', handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'</b></summary>
  </details>
  <details><summary><b>def __hash__(self) -> 'int'</b></summary>
  <p>Return hash(self).</p>
  </details>
  <details><summary><b>def __init__(self, secret_value: 'SecretType') -> 'None'</b></summary>
  <p>Initialize self.  See help(type(self)) for accurate signature.</p>
  </details>
  <details><summary><b>def __init_subclass__(*args, **kwargs)</b></summary>
  <p>This method is called when a class is subclassed.

The default implementation does nothing. It may be
overridden to extend subclasses.</p>
  </details>
  <details><summary><b>def __len__(self) -> 'int'</b></summary>
  </details>
  <details><summary><b>def __repr__(self) -> 'str'</b></summary>
  <p>Return repr(self).</p>
  </details>
  <details><summary><b>def __str__(self) -> 'str'</b></summary>
  <p>Return str(self).</p>
  </details>
  <details><summary><b>def _display(self) -> 'str'</b></summary>
  </details>
  <details><summary><b>def get_secret_value(self) -> 'SecretType'</b></summary>
  <p>Get the secret value.

Returns:
    The secret value.</p>
  </details>
  </details>
  <details><summary><h4>class SerializationInfo(Protocol)</h4></summary>
  <details><summary><b>def __class_getitem__(params)</b></summary>
  <p>Parameterizes a generic class.

At least, parameterizing a generic class is the *main* thing this method
does. For example, for some generic class `Foo`, this is called when we
do `Foo[int]` - there, with `cls=Foo` and `params=int`.

However, note that this method is also called when defining generic
classes in the first place with `class Foo(Generic[T]): ...`.</p>
  </details>
  <details><summary><b>def _no_init_or_replace_init(self, *args, **kwargs)</b></summary>
  </details>
  <details><summary><b>def __init_subclass__(*args, **kwargs)</b></summary>
  <p>This method is called when a class is subclassed.

The default implementation does nothing. It may be
overridden to extend subclasses.</p>
  </details>
  <details><summary><b>def __repr__(self) -> 'str'</b></summary>
  <p>Return repr(self).</p>
  </details>
  <details><summary><b>def __str__(self) -> 'str'</b></summary>
  <p>Return str(self).</p>
  </details>
  <details><summary><b>def _proto_hook(other)</b></summary>
  </details>
  <li><b>by_alias:</b> <property object at 0x7fb1736ba480></li>
  <li><b>context:</b> <property object at 0x7fb1736ba430></li>
  <li><b>exclude:</b> <property object at 0x7fb17368b830></li>
  <li><b>exclude_defaults:</b> <property object at 0x7fb1736ba520></li>
  <li><b>exclude_none:</b> <property object at 0x7fb1736ba570></li>
  <li><b>exclude_unset:</b> <property object at 0x7fb1736ba4d0></li>
  <li><b>include:</b> <property object at 0x7fb17368ae30></li>
  <li><b>mode:</b> <property object at 0x7fb1736ba3e0></li>
  <details><summary><b>def mode_is_json(self) -> 'bool'</b></summary>
  </details>
  <details><summary><b>def round_trip(self) -> 'bool'</b></summary>
  </details>
  <li><b>serialize_as_any:</b> <property object at 0x7fb1736ba5c0></li>
  </details>
  <details><summary><h4>class SerializeAsAny(object)</h4></summary>
  <details><summary><b>def __class_getitem__(item: 'Any') -> 'Any'</b></summary>
  </details>
  <details><summary><b>def __eq__(self, other)</b></summary>
  <p>Return self==value.</p>
  </details>
  <details><summary><b>def __get_pydantic_core_schema__(self, source_type: 'Any', handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'</b></summary>
  </details>
  <details><summary><b>def __init__(self) -> None</b></summary>
  <p>Initialize self.  See help(type(self)) for accurate signature.</p>
  </details>
  <details><summary><b>def __repr__(self)</b></summary>
  <p>Return repr(self).</p>
  </details>
  </details>
  <details><summary><h4>class SerializerFunctionWrapHandler(Protocol)</h4></summary>
  <details><summary><b>def __call__(self, input_value: 'Any', index_key: 'int | str | None' = None, /) -> 'Any'</b></summary>
  <p>Call self as a function.</p>
  </details>
  <details><summary><b>def __class_getitem__(params)</b></summary>
  <p>Parameterizes a generic class.

At least, parameterizing a generic class is the *main* thing this method
does. For example, for some generic class `Foo`, this is called when we
do `Foo[int]` - there, with `cls=Foo` and `params=int`.

However, note that this method is also called when defining generic
classes in the first place with `class Foo(Generic[T]): ...`.</p>
  </details>
  <details><summary><b>def _no_init_or_replace_init(self, *args, **kwargs)</b></summary>
  </details>
  <details><summary><b>def __init_subclass__(*args, **kwargs)</b></summary>
  <p>This method is called when a class is subclassed.

The default implementation does nothing. It may be
overridden to extend subclasses.</p>
  </details>
  <details><summary><b>def _proto_hook(other)</b></summary>
  </details>
  </details>
  <details><summary><h4>class SkipValidation(object)</h4></summary>
  <details><summary><b>def __class_getitem__(item: 'Any') -> 'Any'</b></summary>
  </details>
  <details><summary><b>def __eq__(self, other)</b></summary>
  <p>Return self==value.</p>
  </details>
  <details><summary><b>def __get_pydantic_core_schema__(source: 'Any', handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'</b></summary>
  </details>
  <details><summary><b>def __init__(self) -> None</b></summary>
  <p>Initialize self.  See help(type(self)) for accurate signature.</p>
  </details>
  <details><summary><b>def __repr__(self)</b></summary>
  <p>Return repr(self).</p>
  </details>
  </details>
  <li><b>SnowflakeDsn:</b> typing.Annotated[pydantic_core._pydantic_core.Url, UrlConstraints(max_length=None, allowed_schemes=['snowflake'], host_required=True, default_host=None, default_port=None, default_path=None)]</li>
  <details><summary><h4>class Strict(PydanticMetadata, BaseMetadata)</h4></summary>
  <details><summary><b>def __eq__(self, other)</b></summary>
  <p>Return self==value.</p>
  </details>
  <details><summary><b>def __hash__(self) -> 'int'</b></summary>
  <p>Return hash(self).</p>
  </details>
  <details><summary><b>def __init__(self, strict: 'bool' = True) -> None</b></summary>
  <p>Initialize self.  See help(type(self)) for accurate signature.</p>
  </details>
  <details><summary><b>def __pretty__(self, fmt: 'typing.Callable[[Any], Any]', **kwargs: 'Any') -> 'typing.Generator[Any, None, None]'</b></summary>
  <p>Used by devtools (https://python-devtools.helpmanual.io/) to pretty print objects.</p>
  </details>
  <details><summary><b>def __repr__(self)</b></summary>
  <p>Return repr(self).</p>
  </details>
  <details><summary><b>def __repr_args__(self) -> 'ReprArgs'</b></summary>
  <p>Returns the attributes to show in __str__, __repr__, and __pretty__ this is generally overridden.

Can either return:
* name - value pairs, e.g.: `[('foo_name', 'foo'), ('bar_name', ['b', 'a', 'r'])]`
* or, just values, e.g.: `[(None, 'foo'), (None, ['b', 'a', 'r'])]`</p>
  </details>
  <details><summary><b>def __repr_name__(self) -> 'str'</b></summary>
  <p>Name of the instance's class, used in __repr__.</p>
  </details>
  <details><summary><b>def __repr_str__(self, join_str: 'str') -> 'str'</b></summary>
  </details>
  <details><summary><b>def __rich_repr__(self) -> 'RichReprResult'</b></summary>
  <p>Used by Rich (https://rich.readthedocs.io/en/stable/pretty.html) to pretty print objects.</p>
  </details>
  <details><summary><b>def __str__(self) -> 'str'</b></summary>
  <p>Return str(self).</p>
  </details>
  <li><b>strict:</b> True</li>
  </details>
  <li><b>StrictBool:</b> typing.Annotated[bool, Strict(strict=True)]</li>
  <li><b>StrictBytes:</b> typing.Annotated[bytes, Strict(strict=True)]</li>
  <li><b>StrictFloat:</b> typing.Annotated[float, Strict(strict=True)]</li>
  <li><b>StrictInt:</b> typing.Annotated[int, Strict(strict=True)]</li>
  <li><b>StrictStr:</b> typing.Annotated[str, Strict(strict=True)]</li>
  <details><summary><h4>class StringConstraints(GroupedMetadata)</h4></summary>
  <details><summary><b>def __class_getitem__(params)</b></summary>
  <p>Parameterizes a generic class.

At least, parameterizing a generic class is the *main* thing this method
does. For example, for some generic class `Foo`, this is called when we
do `Foo[int]` - there, with `cls=Foo` and `params=int`.

However, note that this method is also called when defining generic
classes in the first place with `class Foo(Generic[T]): ...`.</p>
  </details>
  <details><summary><b>def __delattr__(self, name)</b></summary>
  <p>Implement delattr(self, name).</p>
  </details>
  <details><summary><b>def __eq__(self, other)</b></summary>
  <p>Return self==value.</p>
  </details>
  <details><summary><b>def __hash__(self)</b></summary>
  <p>Return hash(self).</p>
  </details>
  <details><summary><b>def __init__(self, strip_whitespace: 'bool | None' = None, to_upper: 'bool | None' = None, to_lower: 'bool | None' = None, strict: 'bool | None' = None, min_length: 'int | None' = None, max_length: 'int | None' = None, pattern: 'str | Pattern[str] | None' = None) -> None</b></summary>
  <p>Initialize self.  See help(type(self)) for accurate signature.</p>
  </details>
  <details><summary><b>def __init_subclass__(*args: Any, **kwargs: Any) -> None</b></summary>
  <p>This method is called when a class is subclassed.

The default implementation does nothing. It may be
overridden to extend subclasses.</p>
  </details>
  <details><summary><b>def __iter__(self) -> 'Iterator[BaseMetadata]'</b></summary>
  </details>
  <details><summary><b>def __repr__(self)</b></summary>
  <p>Return repr(self).</p>
  </details>
  <details><summary><b>def __setattr__(self, name, value)</b></summary>
  <p>Implement setattr(self, name, value).</p>
  </details>
  <details><summary><b>def _proto_hook(other)</b></summary>
  </details>
  <li><b>max_length:</b> None</li>
  <li><b>min_length:</b> None</li>
  <li><b>pattern:</b> None</li>
  <li><b>strict:</b> None</li>
  <li><b>strip_whitespace:</b> None</li>
  <li><b>to_lower:</b> None</li>
  <li><b>to_upper:</b> None</li>
  </details>
  <details><summary><h4>class Tag(object)</h4></summary>
  <details><summary><b>def __delattr__(self, name)</b></summary>
  <p>Implement delattr(self, name).</p>
  </details>
  <details><summary><b>def __eq__(self, other)</b></summary>
  <p>Return self==value.</p>
  </details>
  <details><summary><b>def __get_pydantic_core_schema__(self, source_type: 'Any', handler: 'GetCoreSchemaHandler') -> 'CoreSchema'</b></summary>
  </details>
  <details><summary><b>def _dataclass_getstate(self)</b></summary>
  </details>
  <details><summary><b>def __hash__(self)</b></summary>
  <p>Return hash(self).</p>
  </details>
  <details><summary><b>def __init__(self, tag: 'str') -> None</b></summary>
  <p>Initialize self.  See help(type(self)) for accurate signature.</p>
  </details>
  <details><summary><b>def __repr__(self)</b></summary>
  <p>Return repr(self).</p>
  </details>
  <details><summary><b>def __setattr__(self, name, value)</b></summary>
  <p>Implement setattr(self, name, value).</p>
  </details>
  <details><summary><b>def _dataclass_setstate(self, state)</b></summary>
  </details>
  <li><b>tag:</b> <member 'tag' of 'Tag' objects></li>
  </details>
  <details><summary><h4>class TypeAdapter(Generic)</h4></summary>
  <details><summary><b>def __class_getitem__(params)</b></summary>
  <p>Parameterizes a generic class.

At least, parameterizing a generic class is the *main* thing this method
does. For example, for some generic class `Foo`, this is called when we
do `Foo[int]` - there, with `cls=Foo` and `params=int`.

However, note that this method is also called when defining generic
classes in the first place with `class Foo(Generic[T]): ...`.</p>
  </details>
  <details><summary><b>def __init__(self, type: 'Any', *, config: 'ConfigDict | None' = None, _parent_depth: 'int' = 2, module: 'str | None' = None) -> 'None'</b></summary>
  <p>Initializes the TypeAdapter object.

Args:
    type: The type associated with the `TypeAdapter`.
    config: Configuration for the `TypeAdapter`, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].
    _parent_depth: depth at which to search the parent namespace to construct the local namespace.
    module: The module that passes to plugin if provided.

!!! note
    You cannot use the `config` argument when instantiating a `TypeAdapter` if the type you're using has its own
    config that cannot be overridden (ex: `BaseModel`, `TypedDict`, and `dataclass`). A
    [`type-adapter-config-unused`](../errors/usage_errors.md#type-adapter-config-unused) error will be raised in this case.

!!! note
    The `_parent_depth` argument is named with an underscore to suggest its private nature and discourage use.
    It may be deprecated in a minor version, so we only recommend using it if you're
    comfortable with potential change in behavior / support.

??? tip "Compatibility with `mypy`"
    Depending on the type used, `mypy` might raise an error when instantiating a `TypeAdapter`. As a workaround, you can explicitly
    annotate your variable:

    ```py
    from typing import Union

    from pydantic import TypeAdapter

    ta: TypeAdapter[Union[str, int]] = TypeAdapter(Union[str, int])  # type: ignore[arg-type]
    ```

Returns:
    A type adapter configured for the specified `type`.</p>
  </details>
  <details><summary><b>def __init_subclass__(*args, **kwargs)</b></summary>
  <p>This method is called when a class is subclassed.

The default implementation does nothing. It may be
overridden to extend subclasses.</p>
  </details>
  <details><summary><b>def _defer_build(self) -> 'bool'</b></summary>
  </details>
  <details><summary><b>def _init_core_attrs(self, rebuild_mocks: 'bool') -> 'None'</b></summary>
  </details>
  <details><summary><b>def _is_defer_build_config(config: 'ConfigDict') -> 'bool'</b></summary>
  </details>
  <details><summary><b>def _model_config(self) -> 'ConfigDict | None'</b></summary>
  </details>
  <details><summary><b>def _with_frame_depth(self, depth: 'int') -> 'Iterator[None]'</b></summary>
  </details>
  <li><b>core_schema:</b> <functools.cached_property object at 0x7fb1731c7950></li>
  <details><summary><b>def dump_json(self, instance: 'T', /, *, indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, serialize_as_any: 'bool' = False, context: 'dict[str, Any] | None' = None) -> 'bytes'</b></summary>
  <p>Usage docs: https://docs.pydantic.dev/2.9/concepts/json/#json-serialization

Serialize an instance of the adapted type to JSON.

Args:
    instance: The instance to be serialized.
    indent: Number of spaces for JSON indentation.
    include: Fields to include.
    exclude: Fields to exclude.
    by_alias: Whether to use alias names for field names.
    exclude_unset: Whether to exclude unset fields.
    exclude_defaults: Whether to exclude fields with default values.
    exclude_none: Whether to exclude fields with a value of `None`.
    round_trip: Whether to serialize and deserialize the instance to ensure round-tripping.
    warnings: How to handle serialization errors. False/"none" ignores them, True/"warn" logs errors,
        "error" raises a [`PydanticSerializationError`][pydantic_core.PydanticSerializationError].
    serialize_as_any: Whether to serialize fields with duck-typing serialization behavior.
    context: Additional context to pass to the serializer.

Returns:
    The JSON representation of the given instance as bytes.</p>
  </details>
  <details><summary><b>def dump_python(self, instance: 'T', /, *, mode: "Literal['json', 'python']" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, serialize_as_any: 'bool' = False, context: 'dict[str, Any] | None' = None) -> 'Any'</b></summary>
  <p>Dump an instance of the adapted type to a Python object.

Args:
    instance: The Python object to serialize.
    mode: The output format.
    include: Fields to include in the output.
    exclude: Fields to exclude from the output.
    by_alias: Whether to use alias names for field names.
    exclude_unset: Whether to exclude unset fields.
    exclude_defaults: Whether to exclude fields with default values.
    exclude_none: Whether to exclude fields with None values.
    round_trip: Whether to output the serialized data in a way that is compatible with deserialization.
    warnings: How to handle serialization errors. False/"none" ignores them, True/"warn" logs errors,
        "error" raises a [`PydanticSerializationError`][pydantic_core.PydanticSerializationError].
    serialize_as_any: Whether to serialize fields with duck-typing serialization behavior.
    context: Additional context to pass to the serializer.

Returns:
    The serialized object.</p>
  </details>
  <details><summary><b>def get_default_value(self, *, strict: 'bool | None' = None, context: 'dict[str, Any] | None' = None) -> 'Some[T] | None'</b></summary>
  <p>Get the default value for the wrapped type.

Args:
    strict: Whether to strictly check types.
    context: Additional context to pass to the validator.

Returns:
    The default value wrapped in a `Some` if there is one or None if not.</p>
  </details>
  <details><summary><b>def json_schema(self, *, by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation') -> 'dict[str, Any]'</b></summary>
  <p>Generate a JSON schema for the adapted type.

Args:
    by_alias: Whether to use alias names for field names.
    ref_template: The format string used for generating $ref strings.
    schema_generator: The generator class used for creating the schema.
    mode: The mode to use for schema generation.

Returns:
    The JSON schema for the model as a dictionary.</p>
  </details>
  <details><summary><b>def json_schemas(inputs: 'Iterable[tuple[JsonSchemaKeyT, JsonSchemaMode, TypeAdapter[Any]]]', /, *, by_alias: 'bool' = True, title: 'str | None' = None, description: 'str | None' = None, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>) -> 'tuple[dict[tuple[JsonSchemaKeyT, JsonSchemaMode], JsonSchemaValue], JsonSchemaValue]'</b></summary>
  <p>Generate a JSON schema including definitions from multiple type adapters.

Args:
    inputs: Inputs to schema generation. The first two items will form the keys of the (first)
        output mapping; the type adapters will provide the core schemas that get converted into
        definitions in the output JSON schema.
    by_alias: Whether to use alias names.
    title: The title for the schema.
    description: The description for the schema.
    ref_template: The format string used for generating $ref strings.
    schema_generator: The generator class used for creating the schema.

Returns:
    A tuple where:

        - The first element is a dictionary whose keys are tuples of JSON schema key type and JSON mode, and
            whose values are the JSON schema corresponding to that pair of inputs. (These schemas may have
            JsonRef references to definitions that are defined in the second returned element.)
        - The second element is a JSON schema containing all definitions referenced in the first returned
            element, along with the optional title and description keys.</p>
  </details>
  <li><b>serializer:</b> <functools.cached_property object at 0x7fb1731c77d0></li>
  <details><summary><b>def validate_json(self, data: 'str | bytes', /, *, strict: 'bool | None' = None, context: 'dict[str, Any] | None' = None) -> 'T'</b></summary>
  <p>Usage docs: https://docs.pydantic.dev/2.9/concepts/json/#json-parsing

Validate a JSON string or bytes against the model.

Args:
    data: The JSON data to validate against the model.
    strict: Whether to strictly check types.
    context: Additional context to use during validation.

Returns:
    The validated object.</p>
  </details>
  <details><summary><b>def validate_python(self, object: 'Any', /, *, strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'dict[str, Any] | None' = None) -> 'T'</b></summary>
  <p>Validate a Python object against the model.

Args:
    object: The Python object to validate against the model.
    strict: Whether to strictly check types.
    from_attributes: Whether to extract data from object attributes.
    context: Additional context to pass to the validator.

!!! note
    When using `TypeAdapter` with a Pydantic `dataclass`, the use of the `from_attributes`
    argument is not supported.

Returns:
    The validated object.</p>
  </details>
  <details><summary><b>def validate_strings(self, obj: 'Any', /, *, strict: 'bool | None' = None, context: 'dict[str, Any] | None' = None) -> 'T'</b></summary>
  <p>Validate object contains string data against the model.

Args:
    obj: The object contains string data to validate.
    strict: Whether to strictly check types.
    context: Additional context to use during validation.

Returns:
    The validated object.</p>
  </details>
  <li><b>validator:</b> <functools.cached_property object at 0x7fb1731c7850></li>
  </details>
  <li><b>UUID1:</b> typing.Annotated[uuid.UUID, UuidVersion(uuid_version=1)]</li>
  <li><b>UUID3:</b> typing.Annotated[uuid.UUID, UuidVersion(uuid_version=3)]</li>
  <li><b>UUID4:</b> typing.Annotated[uuid.UUID, UuidVersion(uuid_version=4)]</li>
  <li><b>UUID5:</b> typing.Annotated[uuid.UUID, UuidVersion(uuid_version=5)]</li>
  <details><summary><h4>class UrlConstraints(PydanticMetadata)</h4></summary>
  <details><summary><b>def __eq__(self, other)</b></summary>
  <p>Return self==value.</p>
  </details>
  <details><summary><b>def __hash__(self) -> 'int'</b></summary>
  <p>Return hash(self).</p>
  </details>
  <details><summary><b>def __init__(self, max_length: 'int | None' = None, allowed_schemes: 'list[str] | None' = None, host_required: 'bool | None' = None, default_host: 'str | None' = None, default_port: 'int | None' = None, default_path: 'str | None' = None) -> None</b></summary>
  <p>Initialize self.  See help(type(self)) for accurate signature.</p>
  </details>
  <details><summary><b>def __pretty__(self, fmt: 'typing.Callable[[Any], Any]', **kwargs: 'Any') -> 'typing.Generator[Any, None, None]'</b></summary>
  <p>Used by devtools (https://python-devtools.helpmanual.io/) to pretty print objects.</p>
  </details>
  <details><summary><b>def __repr__(self)</b></summary>
  <p>Return repr(self).</p>
  </details>
  <details><summary><b>def __repr_args__(self) -> 'ReprArgs'</b></summary>
  <p>Returns the attributes to show in __str__, __repr__, and __pretty__ this is generally overridden.

Can either return:
* name - value pairs, e.g.: `[('foo_name', 'foo'), ('bar_name', ['b', 'a', 'r'])]`
* or, just values, e.g.: `[(None, 'foo'), (None, ['b', 'a', 'r'])]`</p>
  </details>
  <details><summary><b>def __repr_name__(self) -> 'str'</b></summary>
  <p>Name of the instance's class, used in __repr__.</p>
  </details>
  <details><summary><b>def __repr_str__(self, join_str: 'str') -> 'str'</b></summary>
  </details>
  <details><summary><b>def __rich_repr__(self) -> 'RichReprResult'</b></summary>
  <p>Used by Rich (https://rich.readthedocs.io/en/stable/pretty.html) to pretty print objects.</p>
  </details>
  <details><summary><b>def __str__(self) -> 'str'</b></summary>
  <p>Return str(self).</p>
  </details>
  <li><b>allowed_schemes:</b> None</li>
  <li><b>default_host:</b> None</li>
  <li><b>default_path:</b> None</li>
  <li><b>default_port:</b> None</li>
  <li><b>host_required:</b> None</li>
  <li><b>max_length:</b> None</li>
  </details>
  <li><b>VERSION:</b> '2.9.2'</li>
  <details><summary><h4>class ValidationError(ValueError)</h4></summary>
  <li><b>add_note:</b> <method 'add_note' of 'BaseException' objects></li>
  <li><b>args:</b> <attribute 'args' of 'BaseException' objects></li>
  <li><b>error_count:</b> <method 'error_count' of 'pydantic_core._pydantic_core.ValidationError' objects></li>
  <li><b>errors:</b> <method 'errors' of 'pydantic_core._pydantic_core.ValidationError' objects></li>
  <li><b>from_exception_data:</b> <built-in method from_exception_data of type object at 0x5644ae5c11f0></li>
  <li><b>json:</b> <method 'json' of 'pydantic_core._pydantic_core.ValidationError' objects></li>
  <li><b>title:</b> <attribute 'title' of 'pydantic_core._pydantic_core.ValidationError' objects></li>
  <li><b>with_traceback:</b> <method 'with_traceback' of 'BaseException' objects></li>
  </details>
  <details><summary><h4>class ValidationInfo(Protocol)</h4></summary>
  <details><summary><b>def __class_getitem__(params)</b></summary>
  <p>Parameterizes a generic class.

At least, parameterizing a generic class is the *main* thing this method
does. For example, for some generic class `Foo`, this is called when we
do `Foo[int]` - there, with `cls=Foo` and `params=int`.

However, note that this method is also called when defining generic
classes in the first place with `class Foo(Generic[T]): ...`.</p>
  </details>
  <details><summary><b>def _no_init_or_replace_init(self, *args, **kwargs)</b></summary>
  </details>
  <details><summary><b>def __init_subclass__(*args, **kwargs)</b></summary>
  <p>This method is called when a class is subclassed.

The default implementation does nothing. It may be
overridden to extend subclasses.</p>
  </details>
  <details><summary><b>def _proto_hook(other)</b></summary>
  </details>
  <li><b>config:</b> <property object at 0x7fb1736ba7a0></li>
  <li><b>context:</b> <property object at 0x7fb1736ba750></li>
  <li><b>data:</b> <property object at 0x7fb1736ba840></li>
  <li><b>field_name:</b> <property object at 0x7fb1736ba890></li>
  <li><b>mode:</b> <property object at 0x7fb1736ba7f0></li>
  </details>
  <details><summary><h4>class ValidatorFunctionWrapHandler(Protocol)</h4></summary>
  <details><summary><b>def __call__(self, input_value: 'Any', outer_location: 'str | int | None' = None, /) -> 'Any'</b></summary>
  <p>Call self as a function.</p>
  </details>
  <details><summary><b>def __class_getitem__(params)</b></summary>
  <p>Parameterizes a generic class.

At least, parameterizing a generic class is the *main* thing this method
does. For example, for some generic class `Foo`, this is called when we
do `Foo[int]` - there, with `cls=Foo` and `params=int`.

However, note that this method is also called when defining generic
classes in the first place with `class Foo(Generic[T]): ...`.</p>
  </details>
  <details><summary><b>def _no_init_or_replace_init(self, *args, **kwargs)</b></summary>
  </details>
  <details><summary><b>def __init_subclass__(*args, **kwargs)</b></summary>
  <p>This method is called when a class is subclassed.

The default implementation does nothing. It may be
overridden to extend subclasses.</p>
  </details>
  <details><summary><b>def _proto_hook(other)</b></summary>
  </details>
  </details>
  <li><b>WebsocketUrl:</b> typing.Annotated[pydantic_core._pydantic_core.Url, UrlConstraints(max_length=2083, allowed_schemes=['ws', 'wss'], host_required=None, default_host=None, default_port=None, default_path=None)]</li>
  <details><summary><h4>class WithJsonSchema(object)</h4></summary>
  <details><summary><b>def __eq__(self, other)</b></summary>
  <p>Return self==value.</p>
  </details>
  <details><summary><b>def __get_pydantic_json_schema__(self, core_schema: 'core_schema.CoreSchema', handler: 'GetJsonSchemaHandler') -> 'JsonSchemaValue'</b></summary>
  </details>
  <details><summary><b>def __hash__(self) -> 'int'</b></summary>
  <p>Return hash(self).</p>
  </details>
  <details><summary><b>def __init__(self, json_schema: 'JsonSchemaValue | None', mode: "Literal['validation', 'serialization'] | None" = None) -> None</b></summary>
  <p>Initialize self.  See help(type(self)) for accurate signature.</p>
  </details>
  <details><summary><b>def __repr__(self)</b></summary>
  <p>Return repr(self).</p>
  </details>
  <li><b>json_schema:</b> <member 'json_schema' of 'WithJsonSchema' objects></li>
  <li><b>mode:</b> <member 'mode' of 'WithJsonSchema' objects></li>
  </details>
  <details><summary><h4>class WrapSerializer(object)</h4></summary>
  <details><summary><b>def __delattr__(self, name)</b></summary>
  <p>Implement delattr(self, name).</p>
  </details>
  <details><summary><b>def __eq__(self, other)</b></summary>
  <p>Return self==value.</p>
  </details>
  <details><summary><b>def __get_pydantic_core_schema__(self, source_type: 'Any', handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'</b></summary>
  <p>This method is used to get the Pydantic core schema of the class.

Args:
    source_type: Source type.
    handler: Core schema handler.

Returns:
    The generated core schema of the class.</p>
  </details>
  <details><summary><b>def _dataclass_getstate(self)</b></summary>
  </details>
  <details><summary><b>def __hash__(self)</b></summary>
  <p>Return hash(self).</p>
  </details>
  <details><summary><b>def __init__(self, func: 'core_schema.WrapSerializerFunction', return_type: 'Any' = PydanticUndefined, when_used: 'WhenUsed' = 'always') -> None</b></summary>
  <p>Initialize self.  See help(type(self)) for accurate signature.</p>
  </details>
  <details><summary><b>def __repr__(self)</b></summary>
  <p>Return repr(self).</p>
  </details>
  <details><summary><b>def __setattr__(self, name, value)</b></summary>
  <p>Implement setattr(self, name, value).</p>
  </details>
  <details><summary><b>def _dataclass_setstate(self, state)</b></summary>
  </details>
  <li><b>func:</b> <member 'func' of 'WrapSerializer' objects></li>
  <li><b>return_type:</b> <member 'return_type' of 'WrapSerializer' objects></li>
  <li><b>when_used:</b> <member 'when_used' of 'WrapSerializer' objects></li>
  </details>
  <details><summary><h4>class WrapValidator(object)</h4></summary>
  <details><summary><b>def __delattr__(self, name)</b></summary>
  <p>Implement delattr(self, name).</p>
  </details>
  <details><summary><b>def __eq__(self, other)</b></summary>
  <p>Return self==value.</p>
  </details>
  <details><summary><b>def __get_pydantic_core_schema__(self, source_type: 'Any', handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'</b></summary>
  </details>
  <details><summary><b>def _dataclass_getstate(self)</b></summary>
  </details>
  <details><summary><b>def __hash__(self)</b></summary>
  <p>Return hash(self).</p>
  </details>
  <details><summary><b>def __init__(self, func: 'core_schema.NoInfoWrapValidatorFunction | core_schema.WithInfoWrapValidatorFunction', json_schema_input_type: 'Any' = PydanticUndefined) -> None</b></summary>
  <p>Initialize self.  See help(type(self)) for accurate signature.</p>
  </details>
  <details><summary><b>def __repr__(self)</b></summary>
  <p>Return repr(self).</p>
  </details>
  <details><summary><b>def __setattr__(self, name, value)</b></summary>
  <p>Implement setattr(self, name, value).</p>
  </details>
  <details><summary><b>def _dataclass_setstate(self, state)</b></summary>
  </details>
  <details><summary><b>def _from_decorator(decorator: '_decorators.Decorator[_decorators.FieldValidatorDecoratorInfo]') -> 'Self'</b></summary>
  </details>
  <li><b>func:</b> <member 'func' of 'WrapValidator' objects></li>
  <li><b>json_schema_input_type:</b> <member 'json_schema_input_type' of 'WrapValidator' objects></li>
  </details>
  <details><summary><b>def computed_field(func: 'PropertyT | None' = None, /, *, alias: 'str | None' = None, alias_priority: 'int | None' = None, title: 'str | None' = None, field_title_generator: 'typing.Callable[[str, ComputedFieldInfo], str] | None' = None, description: 'str | None' = None, deprecated: 'Deprecated | str | bool | None' = None, examples: 'list[Any] | None' = None, json_schema_extra: 'JsonDict | typing.Callable[[JsonDict], None] | None' = None, repr: 'bool | None' = None, return_type: 'Any' = PydanticUndefined) -> 'PropertyT | typing.Callable[[PropertyT], PropertyT]'</b></summary>
  <p>Usage docs: https://docs.pydantic.dev/2.9/concepts/fields#the-computed_field-decorator

Decorator to include `property` and `cached_property` when serializing models or dataclasses.

This is useful for fields that are computed from other fields, or for fields that are expensive to compute and should be cached.

```py
from pydantic import BaseModel, computed_field

class Rectangle(BaseModel):
    width: int
    length: int

    @computed_field
    @property
    def area(self) -> int:
        return self.width * self.length

print(Rectangle(width=3, length=2).model_dump())
#> {'width': 3, 'length': 2, 'area': 6}
```

If applied to functions not yet decorated with `@property` or `@cached_property`, the function is
automatically wrapped with `property`. Although this is more concise, you will lose IntelliSense in your IDE,
and confuse static type checkers, thus explicit use of `@property` is recommended.

!!! warning "Mypy Warning"
    Even with the `@property` or `@cached_property` applied to your function before `@computed_field`,
    mypy may throw a `Decorated property not supported` error.
    See [mypy issue #1362](https://github.com/python/mypy/issues/1362), for more information.
    To avoid this error message, add `# type: ignore[misc]` to the `@computed_field` line.

    [pyright](https://github.com/microsoft/pyright) supports `@computed_field` without error.

```py
import random

from pydantic import BaseModel, computed_field

class Square(BaseModel):
    width: float

    @computed_field
    def area(self) -> float:  # converted to a `property` by `computed_field`
        return round(self.width**2, 2)

    @area.setter
    def area(self, new_area: float) -> None:
        self.width = new_area**0.5

    @computed_field(alias='the magic number', repr=False)
    def random_number(self) -> int:
        return random.randint(0, 1_000)

square = Square(width=1.3)

# `random_number` does not appear in representation
print(repr(square))
#> Square(width=1.3, area=1.69)

print(square.random_number)
#> 3

square.area = 4

print(square.model_dump_json(by_alias=True))
#> {"width":2.0,"area":4.0,"the magic number":3}
```

!!! warning "Overriding with `computed_field`"
    You can't override a field from a parent class with a `computed_field` in the child class.
    `mypy` complains about this behavior if allowed, and `dataclasses` doesn't allow this pattern either.
    See the example below:

```py
from pydantic import BaseModel, computed_field

class Parent(BaseModel):
    a: str

try:

    class Child(Parent):
        @computed_field
        @property
        def a(self) -> str:
            return 'new a'

except ValueError as e:
    print(repr(e))
    #> ValueError("you can't override a field with a computed field")
```

Private properties decorated with `@computed_field` have `repr=False` by default.

```py
from functools import cached_property

from pydantic import BaseModel, computed_field

class Model(BaseModel):
    foo: int

    @computed_field
    @cached_property
    def _private_cached_property(self) -> int:
        return -self.foo

    @computed_field
    @property
    def _private_property(self) -> int:
        return -self.foo

m = Model(foo=1)
print(repr(m))
#> M(foo=1)
```

Args:
    func: the function to wrap.
    alias: alias to use when serializing this computed field, only used when `by_alias=True`
    alias_priority: priority of the alias. This affects whether an alias generator is used
    title: Title to use when including this computed field in JSON Schema
    field_title_generator: A callable that takes a field name and returns title for it.
    description: Description to use when including this computed field in JSON Schema, defaults to the function's
        docstring
    deprecated: A deprecation message (or an instance of `warnings.deprecated` or the `typing_extensions.deprecated` backport).
        to be emitted when accessing the field. Or a boolean. This will automatically be set if the property is decorated with the
        `deprecated` decorator.
    examples: Example values to use when including this computed field in JSON Schema
    json_schema_extra: A dict or callable to provide extra JSON schema properties.
    repr: whether to include this computed field in model repr.
        Default is `False` for private properties and `True` for public properties.
    return_type: optional return for serialization logic to expect when serializing to JSON, if included
        this must be correct, otherwise a `TypeError` is raised.
        If you don't include a return type Any is used, which does runtime introspection to handle arbitrary
        objects.

Returns:
    A proxy wrapper for the property.</p>
  </details>
  <details><summary><b>def conbytes(*, min_length: 'int | None' = None, max_length: 'int | None' = None, strict: 'bool | None' = None) -> 'type[bytes]'</b></summary>
  <p>A wrapper around `bytes` that allows for additional constraints.

Args:
    min_length: The minimum length of the bytes.
    max_length: The maximum length of the bytes.
    strict: Whether to validate the bytes in strict mode.

Returns:
    The wrapped bytes type.</p>
  </details>
  <details><summary><b>def condate(*, strict: 'bool | None' = None, gt: 'date | None' = None, ge: 'date | None' = None, lt: 'date | None' = None, le: 'date | None' = None) -> 'type[date]'</b></summary>
  <p>A wrapper for date that adds constraints.

Args:
    strict: Whether to validate the date value in strict mode. Defaults to `None`.
    gt: The value must be greater than this. Defaults to `None`.
    ge: The value must be greater than or equal to this. Defaults to `None`.
    lt: The value must be less than this. Defaults to `None`.
    le: The value must be less than or equal to this. Defaults to `None`.

Returns:
    A date type with the specified constraints.</p>
  </details>
  <details><summary><b>def condecimal(*, strict: 'bool | None' = None, gt: 'int | Decimal | None' = None, ge: 'int | Decimal | None' = None, lt: 'int | Decimal | None' = None, le: 'int | Decimal | None' = None, multiple_of: 'int | Decimal | None' = None, max_digits: 'int | None' = None, decimal_places: 'int | None' = None, allow_inf_nan: 'bool | None' = None) -> 'type[Decimal]'</b></summary>
  <p>!!! warning "Discouraged"
    This function is **discouraged** in favor of using
    [`Annotated`](https://docs.python.org/3/library/typing.html#typing.Annotated) with
    [`Field`][pydantic.fields.Field] instead.

    This function will be **deprecated** in Pydantic 3.0.

    The reason is that `condecimal` returns a type, which doesn't play well with static analysis tools.

    === ":x: Don't do this"
        ```py
        from pydantic import BaseModel, condecimal

        class Foo(BaseModel):
            bar: condecimal(strict=True, allow_inf_nan=True)
        ```

    === ":white_check_mark: Do this"
        ```py
        from decimal import Decimal

        from typing_extensions import Annotated

        from pydantic import BaseModel, Field

        class Foo(BaseModel):
            bar: Annotated[Decimal, Field(strict=True, allow_inf_nan=True)]
        ```

A wrapper around Decimal that adds validation.

Args:
    strict: Whether to validate the value in strict mode. Defaults to `None`.
    gt: The value must be greater than this. Defaults to `None`.
    ge: The value must be greater than or equal to this. Defaults to `None`.
    lt: The value must be less than this. Defaults to `None`.
    le: The value must be less than or equal to this. Defaults to `None`.
    multiple_of: The value must be a multiple of this. Defaults to `None`.
    max_digits: The maximum number of digits. Defaults to `None`.
    decimal_places: The number of decimal places. Defaults to `None`.
    allow_inf_nan: Whether to allow infinity and NaN. Defaults to `None`.

```py
from decimal import Decimal

from pydantic import BaseModel, ValidationError, condecimal

class ConstrainedExample(BaseModel):
    constrained_decimal: condecimal(gt=Decimal('1.0'))

m = ConstrainedExample(constrained_decimal=Decimal('1.1'))
print(repr(m))
#> ConstrainedExample(constrained_decimal=Decimal('1.1'))

try:
    ConstrainedExample(constrained_decimal=Decimal('0.9'))
except ValidationError as e:
    print(e.errors())
    '''
    [
        {
            'type': 'greater_than',
            'loc': ('constrained_decimal',),
            'msg': 'Input should be greater than 1.0',
            'input': Decimal('0.9'),
            'ctx': {'gt': Decimal('1.0')},
            'url': 'https://errors.pydantic.dev/2/v/greater_than',
        }
    ]
    '''
```</p>
  </details>
  <details><summary><b>def confloat(*, strict: 'bool | None' = None, gt: 'float | None' = None, ge: 'float | None' = None, lt: 'float | None' = None, le: 'float | None' = None, multiple_of: 'float | None' = None, allow_inf_nan: 'bool | None' = None) -> 'type[float]'</b></summary>
  <p>!!! warning "Discouraged"
    This function is **discouraged** in favor of using
    [`Annotated`](https://docs.python.org/3/library/typing.html#typing.Annotated) with
    [`Field`][pydantic.fields.Field] instead.

    This function will be **deprecated** in Pydantic 3.0.

    The reason is that `confloat` returns a type, which doesn't play well with static analysis tools.

    === ":x: Don't do this"
        ```py
        from pydantic import BaseModel, confloat

        class Foo(BaseModel):
            bar: confloat(strict=True, gt=0)
        ```

    === ":white_check_mark: Do this"
        ```py
        from typing_extensions import Annotated

        from pydantic import BaseModel, Field

        class Foo(BaseModel):
            bar: Annotated[float, Field(strict=True, gt=0)]
        ```

A wrapper around `float` that allows for additional constraints.

Args:
    strict: Whether to validate the float in strict mode.
    gt: The value must be greater than this.
    ge: The value must be greater than or equal to this.
    lt: The value must be less than this.
    le: The value must be less than or equal to this.
    multiple_of: The value must be a multiple of this.
    allow_inf_nan: Whether to allow `-inf`, `inf`, and `nan`.

Returns:
    The wrapped float type.

```py
from pydantic import BaseModel, ValidationError, confloat

class ConstrainedExample(BaseModel):
    constrained_float: confloat(gt=1.0)

m = ConstrainedExample(constrained_float=1.1)
print(repr(m))
#> ConstrainedExample(constrained_float=1.1)

try:
    ConstrainedExample(constrained_float=0.9)
except ValidationError as e:
    print(e.errors())
    '''
    [
        {
            'type': 'greater_than',
            'loc': ('constrained_float',),
            'msg': 'Input should be greater than 1',
            'input': 0.9,
            'ctx': {'gt': 1.0},
            'url': 'https://errors.pydantic.dev/2/v/greater_than',
        }
    ]
    '''
```</p>
  </details>
  <details><summary><b>def confrozenset(item_type: 'type[HashableItemType]', *, min_length: 'int | None' = None, max_length: 'int | None' = None) -> 'type[frozenset[HashableItemType]]'</b></summary>
  <p>A wrapper around `typing.FrozenSet` that allows for additional constraints.

Args:
    item_type: The type of the items in the frozenset.
    min_length: The minimum length of the frozenset.
    max_length: The maximum length of the frozenset.

Returns:
    The wrapped frozenset type.</p>
  </details>
  <details><summary><b>def conint(*, strict: 'bool | None' = None, gt: 'int | None' = None, ge: 'int | None' = None, lt: 'int | None' = None, le: 'int | None' = None, multiple_of: 'int | None' = None) -> 'type[int]'</b></summary>
  <p>!!! warning "Discouraged"
    This function is **discouraged** in favor of using
    [`Annotated`](https://docs.python.org/3/library/typing.html#typing.Annotated) with
    [`Field`][pydantic.fields.Field] instead.

    This function will be **deprecated** in Pydantic 3.0.

    The reason is that `conint` returns a type, which doesn't play well with static analysis tools.

    === ":x: Don't do this"
        ```py
        from pydantic import BaseModel, conint

        class Foo(BaseModel):
            bar: conint(strict=True, gt=0)
        ```

    === ":white_check_mark: Do this"
        ```py
        from typing_extensions import Annotated

        from pydantic import BaseModel, Field

        class Foo(BaseModel):
            bar: Annotated[int, Field(strict=True, gt=0)]
        ```

A wrapper around `int` that allows for additional constraints.

Args:
    strict: Whether to validate the integer in strict mode. Defaults to `None`.
    gt: The value must be greater than this.
    ge: The value must be greater than or equal to this.
    lt: The value must be less than this.
    le: The value must be less than or equal to this.
    multiple_of: The value must be a multiple of this.

Returns:
    The wrapped integer type.

```py
from pydantic import BaseModel, ValidationError, conint

class ConstrainedExample(BaseModel):
    constrained_int: conint(gt=1)

m = ConstrainedExample(constrained_int=2)
print(repr(m))
#> ConstrainedExample(constrained_int=2)

try:
    ConstrainedExample(constrained_int=0)
except ValidationError as e:
    print(e.errors())
    '''
    [
        {
            'type': 'greater_than',
            'loc': ('constrained_int',),
            'msg': 'Input should be greater than 1',
            'input': 0,
            'ctx': {'gt': 1},
            'url': 'https://errors.pydantic.dev/2/v/greater_than',
        }
    ]
    '''
```</p>
  </details>
  <details><summary><b>def conlist(item_type: 'type[AnyItemType]', *, min_length: 'int | None' = None, max_length: 'int | None' = None, unique_items: 'bool | None' = None) -> 'type[list[AnyItemType]]'</b></summary>
  <p>A wrapper around typing.List that adds validation.

Args:
    item_type: The type of the items in the list.
    min_length: The minimum length of the list. Defaults to None.
    max_length: The maximum length of the list. Defaults to None.
    unique_items: Whether the items in the list must be unique. Defaults to None.
        !!! warning Deprecated
            The `unique_items` parameter is deprecated, use `Set` instead.
            See [this issue](https://github.com/pydantic/pydantic-core/issues/296) for more details.

Returns:
    The wrapped list type.</p>
  </details>
  <details><summary><b>def conset(item_type: 'type[HashableItemType]', *, min_length: 'int | None' = None, max_length: 'int | None' = None) -> 'type[set[HashableItemType]]'</b></summary>
  <p>A wrapper around `typing.Set` that allows for additional constraints.

Args:
    item_type: The type of the items in the set.
    min_length: The minimum length of the set.
    max_length: The maximum length of the set.

Returns:
    The wrapped set type.</p>
  </details>
  <details><summary><b>def constr(*, strip_whitespace: 'bool | None' = None, to_upper: 'bool | None' = None, to_lower: 'bool | None' = None, strict: 'bool | None' = None, min_length: 'int | None' = None, max_length: 'int | None' = None, pattern: 'str | Pattern[str] | None' = None) -> 'type[str]'</b></summary>
  <p>!!! warning "Discouraged"
    This function is **discouraged** in favor of using
    [`Annotated`](https://docs.python.org/3/library/typing.html#typing.Annotated) with
    [`StringConstraints`][pydantic.types.StringConstraints] instead.

    This function will be **deprecated** in Pydantic 3.0.

    The reason is that `constr` returns a type, which doesn't play well with static analysis tools.

    === ":x: Don't do this"
        ```py
        from pydantic import BaseModel, constr

        class Foo(BaseModel):
            bar: constr(strip_whitespace=True, to_upper=True, pattern=r'^[A-Z]+$')
        ```

    === ":white_check_mark: Do this"
        ```py
        from typing_extensions import Annotated

        from pydantic import BaseModel, StringConstraints

        class Foo(BaseModel):
            bar: Annotated[
                str,
                StringConstraints(
                    strip_whitespace=True, to_upper=True, pattern=r'^[A-Z]+$'
                ),
            ]
        ```

A wrapper around `str` that allows for additional constraints.

```py
from pydantic import BaseModel, constr

class Foo(BaseModel):
    bar: constr(strip_whitespace=True, to_upper=True)

foo = Foo(bar='  hello  ')
print(foo)
#> bar='HELLO'
```

Args:
    strip_whitespace: Whether to remove leading and trailing whitespace.
    to_upper: Whether to turn all characters to uppercase.
    to_lower: Whether to turn all characters to lowercase.
    strict: Whether to validate the string in strict mode.
    min_length: The minimum length of the string.
    max_length: The maximum length of the string.
    pattern: A regex pattern to validate the string against.

Returns:
    The wrapped string type.</p>
  </details>
  <details><summary><b>def create_model(model_name: 'str', /, *, __config__: 'ConfigDict | None' = None, __doc__: 'str | None' = None, __base__: 'type[ModelT] | tuple[type[ModelT], ...] | None' = None, __module__: 'str | None' = None, __validators__: 'dict[str, Callable[..., Any]] | None' = None, __cls_kwargs__: 'dict[str, Any] | None' = None, __slots__: 'tuple[str, ...] | None' = None, **field_definitions: 'Any') -> 'type[ModelT]'</b></summary>
  <p>Usage docs: https://docs.pydantic.dev/2.9/concepts/models/#dynamic-model-creation

Dynamically creates and returns a new Pydantic model, in other words, `create_model` dynamically creates a
subclass of [`BaseModel`][pydantic.BaseModel].

Args:
    model_name: The name of the newly created model.
    __config__: The configuration of the new model.
    __doc__: The docstring of the new model.
    __base__: The base class or classes for the new model.
    __module__: The name of the module that the model belongs to;
        if `None`, the value is taken from `sys._getframe(1)`
    __validators__: A dictionary of methods that validate fields. The keys are the names of the validation methods to
        be added to the model, and the values are the validation methods themselves. You can read more about functional
        validators [here](https://docs.pydantic.dev/2.9/concepts/validators/#field-validators).
    __cls_kwargs__: A dictionary of keyword arguments for class creation, such as `metaclass`.
    __slots__: Deprecated. Should not be passed to `create_model`.
    **field_definitions: Attributes of the new model. They should be passed in the format:
        `<name>=(<type>, <default value>)`, `<name>=(<type>, <FieldInfo>)`, or `typing.Annotated[<type>, <FieldInfo>]`.
        Any additional metadata in `typing.Annotated[<type>, <FieldInfo>, ...]` will be ignored.

Returns:
    The new [model][pydantic.BaseModel].

Raises:
    PydanticUserError: If `__base__` and `__config__` are both passed.</p>
  </details>
  <details><summary><h4>module pydantic.dataclasses</h4></summary>
  </details>
  <details><summary><b>def field_serializer(*fields: 'str', mode: "Literal['plain', 'wrap']" = 'plain', return_type: 'Any' = PydanticUndefined, when_used: 'WhenUsed' = 'always', check_fields: 'bool | None' = None) -> 'Callable[[_FieldWrapSerializerT], _FieldWrapSerializerT] | Callable[[_FieldPlainSerializerT], _FieldPlainSerializerT]'</b></summary>
  <p>Decorator that enables custom field serialization.

In the below example, a field of type `set` is used to mitigate duplication. A `field_serializer` is used to serialize the data as a sorted list.

```python
from typing import Set

from pydantic import BaseModel, field_serializer

class StudentModel(BaseModel):
    name: str = 'Jane'
    courses: Set[str]

    @field_serializer('courses', when_used='json')
    def serialize_courses_in_order(self, courses: Set[str]):
        return sorted(courses)

student = StudentModel(courses={'Math', 'Chemistry', 'English'})
print(student.model_dump_json())
#> {"name":"Jane","courses":["Chemistry","English","Math"]}
```

See [Custom serializers](../concepts/serialization.md#custom-serializers) for more information.

Four signatures are supported:

- `(self, value: Any, info: FieldSerializationInfo)`
- `(self, value: Any, nxt: SerializerFunctionWrapHandler, info: FieldSerializationInfo)`
- `(value: Any, info: SerializationInfo)`
- `(value: Any, nxt: SerializerFunctionWrapHandler, info: SerializationInfo)`

Args:
    fields: Which field(s) the method should be called on.
    mode: The serialization mode.

        - `plain` means the function will be called instead of the default serialization logic,
        - `wrap` means the function will be called with an argument to optionally call the
           default serialization logic.
    return_type: Optional return type for the function, if omitted it will be inferred from the type annotation.
    when_used: Determines the serializer will be used for serialization.
    check_fields: Whether to check that the fields actually exist on the model.

Returns:
    The decorator function.</p>
  </details>
  <details><summary><b>def field_validator(field: 'str', /, *fields: 'str', mode: 'FieldValidatorModes' = 'after', check_fields: 'bool | None' = None, json_schema_input_type: 'Any' = PydanticUndefined) -> 'Callable[[Any], Any]'</b></summary>
  <p>Usage docs: https://docs.pydantic.dev/2.9/concepts/validators/#field-validators

Decorate methods on the class indicating that they should be used to validate fields.

Example usage:
```py
from typing import Any

from pydantic import (
    BaseModel,
    ValidationError,
    field_validator,
)

class Model(BaseModel):
    a: str

    @field_validator('a')
    @classmethod
    def ensure_foobar(cls, v: Any):
        if 'foobar' not in v:
            raise ValueError('"foobar" not found in a')
        return v

print(repr(Model(a='this is foobar good')))
#> Model(a='this is foobar good')

try:
    Model(a='snap')
except ValidationError as exc_info:
    print(exc_info)
    '''
    1 validation error for Model
    a
      Value error, "foobar" not found in a [type=value_error, input_value='snap', input_type=str]
    '''
```

For more in depth examples, see [Field Validators](../concepts/validators.md#field-validators).

Args:
    field: The first field the `field_validator` should be called on; this is separate
        from `fields` to ensure an error is raised if you don't pass at least one.
    *fields: Additional field(s) the `field_validator` should be called on.
    mode: Specifies whether to validate the fields before or after validation.
    check_fields: Whether to check that the fields actually exist on the model.
    json_schema_input_type: The input type of the function. This is only used to generate
        the appropriate JSON Schema (in validation mode) and can only specified
        when `mode` is either `'before'`, `'plain'` or `'wrap'`.

Returns:
    A decorator that can be used to decorate a function to be used as a field_validator.

Raises:
    PydanticUserError:
        - If `@field_validator` is used bare (with no fields).
        - If the args passed to `@field_validator` as fields are not strings.
        - If `@field_validator` applied to instance methods.</p>
  </details>
  <details><summary><b>def model_serializer(f: '_ModelPlainSerializerT | _ModelWrapSerializerT | None' = None, /, *, mode: "Literal['plain', 'wrap']" = 'plain', when_used: 'WhenUsed' = 'always', return_type: 'Any' = PydanticUndefined) -> '_ModelPlainSerializerT | Callable[[_ModelWrapSerializerT], _ModelWrapSerializerT] | Callable[[_ModelPlainSerializerT], _ModelPlainSerializerT]'</b></summary>
  <p>Decorator that enables custom model serialization.

This is useful when a model need to be serialized in a customized manner, allowing for flexibility beyond just specific fields.

An example would be to serialize temperature to the same temperature scale, such as degrees Celsius.

```python
from typing import Literal

from pydantic import BaseModel, model_serializer

class TemperatureModel(BaseModel):
    unit: Literal['C', 'F']
    value: int

    @model_serializer()
    def serialize_model(self):
        if self.unit == 'F':
            return {'unit': 'C', 'value': int((self.value - 32) / 1.8)}
        return {'unit': self.unit, 'value': self.value}

temperature = TemperatureModel(unit='F', value=212)
print(temperature.model_dump())
#> {'unit': 'C', 'value': 100}
```

Two signatures are supported for `mode='plain'`, which is the default:

- `(self)`
- `(self, info: SerializationInfo)`

And two other signatures for `mode='wrap'`:

- `(self, nxt: SerializerFunctionWrapHandler)`
- `(self, nxt: SerializerFunctionWrapHandler, info: SerializationInfo)`

    See [Custom serializers](../concepts/serialization.md#custom-serializers) for more information.

Args:
    f: The function to be decorated.
    mode: The serialization mode.

        - `'plain'` means the function will be called instead of the default serialization logic
        - `'wrap'` means the function will be called with an argument to optionally call the default
            serialization logic.
    when_used: Determines when this serializer should be used.
    return_type: The return type for the function. If omitted it will be inferred from the type annotation.

Returns:
    The decorator function.</p>
  </details>
  <details><summary><b>def model_validator(*, mode: "Literal['wrap', 'before', 'after']") -> 'Any'</b></summary>
  <p>Usage docs: https://docs.pydantic.dev/2.9/concepts/validators/#model-validators

Decorate model methods for validation purposes.

Example usage:
```py
from typing_extensions import Self

from pydantic import BaseModel, ValidationError, model_validator

class Square(BaseModel):
    width: float
    height: float

    @model_validator(mode='after')
    def verify_square(self) -> Self:
        if self.width != self.height:
            raise ValueError('width and height do not match')
        return self

s = Square(width=1, height=1)
print(repr(s))
#> Square(width=1.0, height=1.0)

try:
    Square(width=1, height=2)
except ValidationError as e:
    print(e)
    '''
    1 validation error for Square
      Value error, width and height do not match [type=value_error, input_value={'width': 1, 'height': 2}, input_type=dict]
    '''
```

For more in depth examples, see [Model Validators](../concepts/validators.md#model-validators).

Args:
    mode: A required string literal that specifies the validation mode.
        It can be one of the following: 'wrap', 'before', or 'after'.

Returns:
    A decorator that can be used to decorate a function to be used as a model validator.</p>
  </details>
  <details><summary><b>def parse_obj_as(type_: 'type[T]', obj: 'Any', type_name: 'NameFactory | None' = None) -> 'T'</b></summary>
  </details>
  <details><summary><b>def root_validator(*__args, pre: 'bool' = False, skip_on_failure: 'bool' = False, allow_reuse: 'bool' = False) -> 'Any'</b></summary>
  <p>Decorate methods on a model indicating that they should be used to validate (and perhaps
modify) data either before or after standard model parsing/validation is performed.

Args:
    pre (bool, optional): Whether this validator should be called before the standard
        validators (else after). Defaults to False.
    skip_on_failure (bool, optional): Whether to stop validation and return as soon as a
        failure is encountered. Defaults to False.
    allow_reuse (bool, optional): Whether to track and raise an error if another validator
        refers to the decorated function. Defaults to False.

Returns:
    Any: A decorator that can be used to decorate a function to be used as a root_validator.</p>
  </details>
  <details><summary><b>def schema_json_of(type_: 'Any', *, title: 'NameFactory | None' = None, by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, **dumps_kwargs: 'Any') -> 'str'</b></summary>
  <p>Generate a JSON schema (as JSON) for the passed model or dynamically generated one.</p>
  </details>
  <details><summary><b>def schema_of(type_: 'Any', *, title: 'NameFactory | None' = None, by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>) -> 'dict[str, Any]'</b></summary>
  <p>Generate a JSON schema (as dict) for the passed model or dynamically generated one.</p>
  </details>
  <details><summary><b>def validate_call(func: 'AnyCallableT | None' = None, /, *, config: 'ConfigDict | None' = None, validate_return: 'bool' = False) -> 'AnyCallableT | Callable[[AnyCallableT], AnyCallableT]'</b></summary>
  <p>Usage docs: https://docs.pydantic.dev/2.9/concepts/validation_decorator/

Returns a decorated wrapper around the function that validates the arguments and, optionally, the return value.

Usage may be either as a plain decorator `@validate_call` or with arguments `@validate_call(...)`.

Args:
    func: The function to be decorated.
    config: The configuration dictionary.
    validate_return: Whether to validate the return value.

Returns:
    The decorated function.</p>
  </details>
  <details><summary><b>def validate_email(value: 'str') -> 'tuple[str, str]'</b></summary>
  <p>Email address validation using [email-validator](https://pypi.org/project/email-validator/).

Note:
    Note that:

    * Raw IP address (literal) domain parts are not allowed.
    * `"John Doe <local_part@domain.com>"` style "pretty" email addresses are processed.
    * Spaces are striped from the beginning and end of addresses, but no error is raised.</p>
  </details>
  <details><summary><b>def validator(__field: 'str', *fields: 'str', pre: 'bool' = False, each_item: 'bool' = False, always: 'bool' = False, check_fields: 'bool | None' = None, allow_reuse: 'bool' = False) -> 'Callable[[_V1ValidatorType], _V1ValidatorType]'</b></summary>
  <p>Decorate methods on the class indicating that they should be used to validate fields.

Args:
    __field (str): The first field the validator should be called on; this is separate
        from `fields` to ensure an error is raised if you don't pass at least one.
    *fields (str): Additional field(s) the validator should be called on.
    pre (bool, optional): Whether this validator should be called before the standard
        validators (else after). Defaults to False.
    each_item (bool, optional): For complex objects (sets, lists etc.) whether to validate
        individual elements rather than the whole object. Defaults to False.
    always (bool, optional): Whether this method and other validators should be called even if
        the value is missing. Defaults to False.
    check_fields (bool | None, optional): Whether to check that the fields actually exist on the model.
        Defaults to None.
    allow_reuse (bool, optional): Whether to track and raise an error if another validator refers to
        the decorated function. Defaults to False.

Returns:
    Callable: A decorator that can be used to decorate a
        function to be used as a validator.</p>
  </details>
  <details><summary><b>def with_config(config: 'ConfigDict') -> 'Callable[[_TypeT], _TypeT]'</b></summary>
  <p>Usage docs: https://docs.pydantic.dev/2.9/concepts/config/#configuration-with-dataclass-from-the-standard-library-or-typeddict

A convenience decorator to set a [Pydantic configuration](config.md) on a `TypedDict` or a `dataclass` from the standard library.

Although the configuration can be set using the `__pydantic_config__` attribute, it does not play well with type checkers,
especially with `TypedDict`.

!!! example "Usage"

    ```py
    from typing_extensions import TypedDict

    from pydantic import ConfigDict, TypeAdapter, with_config

    @with_config(ConfigDict(str_to_lower=True))
    class Model(TypedDict):
        x: str

    ta = TypeAdapter(Model)

    print(ta.validate_python({'x': 'ABC'}))
    #> {'x': 'abc'}
    ```</p>
  </details>
</details>
