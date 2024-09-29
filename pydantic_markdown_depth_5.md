<details><summary>`pydantic`</summary>
  <details><summary>`class AfterValidator(object)`</summary>
    <details><summary>`__delattr__ (self, name)`</summary>
    </details>
    <details><summary>`__eq__ (self, other)`</summary>
    </details>
    <details><summary>`__get_pydantic_core_schema__ (self, source_type: 'Any', handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'`</summary>
    </details>
    <details><summary>`__getstate__ (self)`</summary>
    </details>
    <details><summary>`__hash__ (self)`</summary>
    </details>
    <details><summary>`__init__ (self, func: 'core_schema.NoInfoValidatorFunction | core_schema.WithInfoValidatorFunction') -> None`</summary>
    </details>
    <details><summary>`__repr__ (self)`</summary>
    </details>
    <details><summary>`__setattr__ (self, name, value)`</summary>
    </details>
    <details><summary>`__setstate__ (self, state)`</summary>
    </details>
    <details><summary>`_from_decorator (decorator: '_decorators.Decorator[_decorators.FieldValidatorDecoratorInfo]') -> 'Self'`</summary>
    </details>
    - `func = <member 'func' of 'AfterValidator' objects>`
  </details>
  <details><summary>`class AliasChoices(object)`</summary>
    <details><summary>`__eq__ (self, other)`</summary>
    </details>
    <details><summary>`__init__ (self, first_choice: 'str | AliasPath', *choices: 'str | AliasPath') -> 'None'`</summary>
    </details>
    <details><summary>`__repr__ (self)`</summary>
    </details>
    - `choices = <member 'choices' of 'AliasChoices' objects>`
    <details><summary>`convert_to_aliases (self) -> 'list[list[str | int]]'`</summary>
    </details>
  </details>
  <details><summary>`class AliasGenerator(object)`</summary>
    <details><summary>`__eq__ (self, other)`</summary>
    </details>
    <details><summary>`__init__ (self, alias: 'Callable[[str], str] | None' = None, validation_alias: 'Callable[[str], str | AliasPath | AliasChoices] | None' = None, serialization_alias: 'Callable[[str], str] | None' = None) -> None`</summary>
    </details>
    <details><summary>`__repr__ (self)`</summary>
    </details>
    <details><summary>`_generate_alias (self, alias_kind: "Literal['alias', 'validation_alias', 'serialization_alias']", allowed_types: 'tuple[type[str] | type[AliasPath] | type[AliasChoices], ...]', field_name: 'str') -> 'str | AliasPath | AliasChoices | None'`</summary>
    </details>
    - `alias = <member 'alias' of 'AliasGenerator' objects>`
    <details><summary>`generate_aliases (self, field_name: 'str') -> 'tuple[str | None, str | AliasPath | AliasChoices | None, str | None]'`</summary>
    </details>
    - `serialization_alias = <member 'serialization_alias' of 'AliasGenerator' objects>`
    - `validation_alias = <member 'validation_alias' of 'AliasGenerator' objects>`
  </details>
  <details><summary>`class AliasPath(object)`</summary>
    <details><summary>`__eq__ (self, other)`</summary>
    </details>
    <details><summary>`__init__ (self, first_arg: 'str', *args: 'str | int') -> 'None'`</summary>
    </details>
    <details><summary>`__repr__ (self)`</summary>
    </details>
    <details><summary>`convert_to_aliases (self) -> 'list[str | int]'`</summary>
    </details>
    - `path = <member 'path' of 'AliasPath' objects>`
    <details><summary>`search_dict_for_path (self, d: 'dict') -> 'Any'`</summary>
    </details>
  </details>
  <details><summary>`class AllowInfNan(PydanticMetadata)`</summary>
    <details><summary>`__eq__ (self, other)`</summary>
    </details>
    <details><summary>`__hash__ (self) -> 'int'`</summary>
    </details>
    <details><summary>`__init__ (self, allow_inf_nan: 'bool' = True) -> None`</summary>
    </details>
    <details><summary>`__pretty__ (self, fmt: 'typing.Callable[[Any], Any]', **kwargs: 'Any') -> 'typing.Generator[Any, None, None]'`</summary>
    </details>
    <details><summary>`__repr__ (self)`</summary>
    </details>
    <details><summary>`__repr_args__ (self) -> 'ReprArgs'`</summary>
    </details>
    <details><summary>`__repr_name__ (self) -> 'str'`</summary>
    </details>
    <details><summary>`__repr_str__ (self, join_str: 'str') -> 'str'`</summary>
    </details>
    <details><summary>`__rich_repr__ (self) -> 'RichReprResult'`</summary>
    </details>
    <details><summary>`__str__ (self) -> 'str'`</summary>
    </details>
    - `allow_inf_nan = True`
  </details>
  - `AmqpDsn = typing.Annotated[pydantic_core._pydantic_core.Url, UrlConstraints(max_length=None, allowed_schemes=['amqp', 'amqps'], host_required=None, default_host=None, default_port=None, default_path=None)]`
  - `AnyHttpUrl = typing.Annotated[pydantic_core._pydantic_core.Url, UrlConstraints(max_length=None, allowed_schemes=['http', 'https'], host_required=None, default_host=None, default_port=None, default_path=None)]`
  <details><summary>`class Url(object)`</summary>
    - `build = <built-in method build of type object at 0x55fa9ac31d30>`
    - `fragment = <attribute 'fragment' of 'pydantic_core._pydantic_core.Url' objects>`
    - `host = <attribute 'host' of 'pydantic_core._pydantic_core.Url' objects>`
    - `password = <attribute 'password' of 'pydantic_core._pydantic_core.Url' objects>`
    - `path = <attribute 'path' of 'pydantic_core._pydantic_core.Url' objects>`
    - `port = <attribute 'port' of 'pydantic_core._pydantic_core.Url' objects>`
    - `query = <attribute 'query' of 'pydantic_core._pydantic_core.Url' objects>`
    - `query_params = <method 'query_params' of 'pydantic_core._pydantic_core.Url' objects>`
    - `scheme = <attribute 'scheme' of 'pydantic_core._pydantic_core.Url' objects>`
    - `unicode_host = <method 'unicode_host' of 'pydantic_core._pydantic_core.Url' objects>`
    - `unicode_string = <method 'unicode_string' of 'pydantic_core._pydantic_core.Url' objects>`
    - `username = <attribute 'username' of 'pydantic_core._pydantic_core.Url' objects>`
  </details>
  - `AnyWebsocketUrl = typing.Annotated[pydantic_core._pydantic_core.Url, UrlConstraints(max_length=None, allowed_schemes=['ws', 'wss'], host_required=None, default_host=None, default_port=None, default_path=None)]`
  <details><summary>`class AwareDatetime(object)`</summary>
    <details><summary>`__get_pydantic_core_schema__ (source: 'type[Any]', handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'`</summary>
    </details>
    <details><summary>`__repr__ (self) -> 'str'`</summary>
    </details>
  </details>
  - `Base64Bytes = typing.Annotated[bytes, EncodedBytes(encoder=<class 'pydantic.types.Base64Encoder'>)]`
  <details><summary>`class Base64Encoder(EncoderProtocol)`</summary>
    <details><summary>`__class_getitem__ (params)`</summary>
    </details>
    <details><summary>`__init__ (self, *args, **kwargs)`</summary>
    </details>
    <details><summary>`__init_subclass__ (*args, **kwargs)`</summary>
    </details>
    <details><summary>`__subclasshook__ (other)`</summary>
    </details>
    <details><summary>`decode (data: 'bytes') -> 'bytes'`</summary>
    </details>
    <details><summary>`encode (value: 'bytes') -> 'bytes'`</summary>
    </details>
    <details><summary>`get_json_format () -> "Literal['base64']"`</summary>
    </details>
  </details>
  - `Base64Str = typing.Annotated[str, EncodedStr(encoder=<class 'pydantic.types.Base64Encoder'>)]`
  - `Base64UrlBytes = typing.Annotated[bytes, EncodedBytes(encoder=<class 'pydantic.types.Base64UrlEncoder'>)]`
  - `Base64UrlStr = typing.Annotated[str, EncodedStr(encoder=<class 'pydantic.types.Base64UrlEncoder'>)]`
  <details><summary>`class BaseConfig(object)`</summary>
    <details><summary>`__getattr__ (self, item: 'str') -> 'Any'`</summary>
    </details>
    <details><summary>`__init_subclass__ (**kwargs: 'Any') -> 'None'`</summary>
    </details>
    <details><summary>`__new__ (*args, **kwargs)`</summary>
    </details>
  </details>
  <details><summary>`class BaseModel(object)`</summary>
    <details><summary>`__class_getitem__ (typevar_values: 'type[Any] | tuple[type[Any], ...]') -> 'type[BaseModel] | _forward_ref.PydanticRecursiveRef'`</summary>
    </details>
    <details><summary>`__copy__ (self) -> 'Self'`</summary>
    </details>
    <details><summary>`__deepcopy__ (self, memo: 'dict[int, Any] | None' = None) -> 'Self'`</summary>
    </details>
    <details><summary>`__delattr__ (self, item: 'str') -> 'Any'`</summary>
    </details>
    <details><summary>`__eq__ (self, other: 'Any') -> 'bool'`</summary>
    </details>
    <details><summary>`__get_pydantic_core_schema__ (source: 'type[BaseModel]', handler: 'GetCoreSchemaHandler', /) -> 'CoreSchema'`</summary>
    </details>
    <details><summary>`__get_pydantic_json_schema__ (core_schema: 'CoreSchema', handler: 'GetJsonSchemaHandler', /) -> 'JsonSchemaValue'`</summary>
    </details>
    <details><summary>`__getattr__ (self, item: 'str') -> 'Any'`</summary>
    </details>
    <details><summary>`__getstate__ (self) -> 'dict[Any, Any]'`</summary>
    </details>
    <details><summary>`__init__ (self, /, **data: 'Any') -> 'None'`</summary>
    </details>
    <details><summary>`__iter__ (self) -> 'TupleGenerator'`</summary>
    </details>
    <details><summary>`__pretty__ (self, fmt: 'typing.Callable[[Any], Any]', **kwargs: 'Any') -> 'typing.Generator[Any, None, None]'`</summary>
    </details>
    <details><summary>`__pydantic_init_subclass__ (**kwargs: 'Any') -> 'None'`</summary>
    </details>
    <details><summary>`__repr__ (self) -> 'str'`</summary>
    </details>
    <details><summary>`__repr_args__ (self) -> '_repr.ReprArgs'`</summary>
    </details>
    <details><summary>`__repr_name__ (self) -> 'str'`</summary>
    </details>
    <details><summary>`__repr_str__ (self, join_str: 'str') -> 'str'`</summary>
    </details>
    <details><summary>`__rich_repr__ (self) -> 'RichReprResult'`</summary>
    </details>
    <details><summary>`__setattr__ (self, name: 'str', value: 'Any') -> 'None'`</summary>
    </details>
    <details><summary>`__setstate__ (self, state: 'dict[Any, Any]') -> 'None'`</summary>
    </details>
    <details><summary>`__str__ (self) -> 'str'`</summary>
    </details>
    <details><summary>`_calculate_keys (self, *args: 'Any', **kwargs: 'Any') -> 'Any'`</summary>
    </details>
    <details><summary>`_check_frozen (self, name: 'str', value: 'Any') -> 'None'`</summary>
    </details>
    <details><summary>`_copy_and_set_values (self, *args: 'Any', **kwargs: 'Any') -> 'Any'`</summary>
    </details>
    <details><summary>`_get_value (*args: 'Any', **kwargs: 'Any') -> 'Any'`</summary>
    </details>
    <details><summary>`_iter (self, *args: 'Any', **kwargs: 'Any') -> 'Any'`</summary>
    </details>
    <details><summary>`construct (_fields_set: 'set[str] | None' = None, **values: 'Any') -> 'Self'`</summary>
    </details>
    <details><summary>`copy (self, *, include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False) -> 'Self'`</summary>
    </details>
    <details><summary>`dict (self, *, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False) -> 'Dict[str, Any]'`</summary>
    </details>
    <details><summary>`from_orm (obj: 'Any') -> 'Self'`</summary>
    </details>
    <details><summary>`json (self, *, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any') -> 'str'`</summary>
    </details>
    - `model_computed_fields = {}`
    - `model_config = {}`
    <details><summary>`model_construct (_fields_set: 'set[str] | None' = None, **values: 'Any') -> 'Self'`</summary>
    </details>
    <details><summary>`model_copy (self, *, update: 'dict[str, Any] | None' = None, deep: 'bool' = False) -> 'Self'`</summary>
    </details>
    <details><summary>`model_dump (self, *, mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, serialize_as_any: 'bool' = False) -> 'dict[str, Any]'`</summary>
    </details>
    <details><summary>`model_dump_json (self, *, indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, serialize_as_any: 'bool' = False) -> 'str'`</summary>
    </details>
    - `model_extra = <property object at 0x7f13fa443010>`
    - `model_fields = {}`
    - `model_fields_set = <property object at 0x7f13fa443970>`
    <details><summary>`model_json_schema (by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation') -> 'dict[str, Any]'`</summary>
    </details>
    <details><summary>`model_parametrized_name (params: 'tuple[type[Any], ...]') -> 'str'`</summary>
    </details>
    <details><summary>`model_post_init (self, _BaseModel__context: 'Any') -> 'None'`</summary>
    </details>
    <details><summary>`model_rebuild (*, force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'dict[str, Any] | None' = None) -> 'bool | None'`</summary>
    </details>
    <details><summary>`model_validate (obj: 'Any', *, strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None) -> 'Self'`</summary>
    </details>
    <details><summary>`model_validate_json (json_data: 'str | bytes | bytearray', *, strict: 'bool | None' = None, context: 'Any | None' = None) -> 'Self'`</summary>
    </details>
    <details><summary>`model_validate_strings (obj: 'Any', *, strict: 'bool | None' = None, context: 'Any | None' = None) -> 'Self'`</summary>
    </details>
    <details><summary>`parse_file (path: 'str | Path', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'`</summary>
    </details>
    <details><summary>`parse_obj (obj: 'Any') -> 'Self'`</summary>
    </details>
    <details><summary>`parse_raw (b: 'str | bytes', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'`</summary>
    </details>
    <details><summary>`schema (by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}') -> 'Dict[str, Any]'`</summary>
    </details>
    <details><summary>`schema_json (*, by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any') -> 'str'`</summary>
    </details>
    <details><summary>`update_forward_refs (**localns: 'Any') -> 'None'`</summary>
    </details>
    <details><summary>`validate (value: 'Any') -> 'Self'`</summary>
    </details>
  </details>
  <details><summary>`class BeforeValidator(object)`</summary>
    <details><summary>`__delattr__ (self, name)`</summary>
    </details>
    <details><summary>`__eq__ (self, other)`</summary>
    </details>
    <details><summary>`__get_pydantic_core_schema__ (self, source_type: 'Any', handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'`</summary>
    </details>
    <details><summary>`__getstate__ (self)`</summary>
    </details>
    <details><summary>`__hash__ (self)`</summary>
    </details>
    <details><summary>`__init__ (self, func: 'core_schema.NoInfoValidatorFunction | core_schema.WithInfoValidatorFunction', json_schema_input_type: 'Any' = PydanticUndefined) -> None`</summary>
    </details>
    <details><summary>`__repr__ (self)`</summary>
    </details>
    <details><summary>`__setattr__ (self, name, value)`</summary>
    </details>
    <details><summary>`__setstate__ (self, state)`</summary>
    </details>
    <details><summary>`_from_decorator (decorator: '_decorators.Decorator[_decorators.FieldValidatorDecoratorInfo]') -> 'Self'`</summary>
    </details>
    - `func = <member 'func' of 'BeforeValidator' objects>`
    - `json_schema_input_type = <member 'json_schema_input_type' of 'BeforeValidator' objects>`
  </details>
  <details><summary>`class ByteSize(int)`</summary>
    <details><summary>`__get_pydantic_core_schema__ (source: 'type[Any]', handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'`</summary>
    </details>
    <details><summary>`_validate (input_value: 'Any', /, _: 'core_schema.ValidationInfo') -> 'ByteSize'`</summary>
    </details>
    - `as_integer_ratio = <method 'as_integer_ratio' of 'int' objects>`
    - `bit_count = <method 'bit_count' of 'int' objects>`
    - `bit_length = <method 'bit_length' of 'int' objects>`
    - `byte_sizes = {'b': 1, 'kb': 1000, 'mb': 1000000, 'gb': 1000000000, 'tb': 1000000000000, 'pb': 1000000000000000, 'eb': 1000000000000000000, 'kib': 1024, 'mib': 1048576, 'gib': 1073741824, 'tib': 1099511627776, 'pib': 1125899906842624, 'eib': 1152921504606846976, 'bit': 0.125, 'kbit': 125.0, 'mbit': 125000.0, 'gbit': 125000000.0, 'tbit': 125000000000.0, 'pbit': 125000000000000.0, 'ebit': 1.25e+17, 'kibit': 128.0, 'mibit': 131072.0, 'gibit': 134217728.0, 'tibit': 137438953472.0, 'pibit': 140737488355328.0, 'eibit': 1.4411518807585587e+17, 'k': 1000, 'm': 1000000, 'g': 1000000000, 't': 1000000000000, 'p': 1000000000000000, 'e': 1000000000000000000}`
    - `byte_string_pattern = '^\\s*(\\d*\\.?\\d+)\\s*(\\w+)?'`
    - `byte_string_re = re.compile('^\\s*(\\d*\\.?\\d+)\\s*(\\w+)?', re.IGNORECASE)`
    - `conjugate = <method 'conjugate' of 'int' objects>`
    - `denominator = <attribute 'denominator' of 'int' objects>`
    - `from_bytes = <built-in method from_bytes of type object at 0x55fa9ad2e040>`
    <details><summary>`human_readable (self, decimal: 'bool' = False, separator: 'str' = '') -> 'str'`</summary>
    </details>
    - `imag = <attribute 'imag' of 'int' objects>`
    - `numerator = <attribute 'numerator' of 'int' objects>`
    - `real = <attribute 'real' of 'int' objects>`
    <details><summary>`to (self, unit: 'str') -> 'float'`</summary>
    </details>
    - `to_bytes = <method 'to_bytes' of 'int' objects>`
  </details>
  - `ClickHouseDsn = typing.Annotated[pydantic_core._pydantic_core.Url, UrlConstraints(max_length=None, allowed_schemes=['clickhouse+native', 'clickhouse+asynch'], host_required=None, default_host='localhost', default_port=9000, default_path=None)]`
  - `CockroachDsn = typing.Annotated[pydantic_core._pydantic_core.Url, UrlConstraints(max_length=None, allowed_schemes=['cockroachdb', 'cockroachdb+psycopg2', 'cockroachdb+asyncpg'], host_required=True, default_host=None, default_port=None, default_path=None)]`
  <details><summary>`class ConfigDict(dict)`</summary>
    - `clear = <method 'clear' of 'dict' objects>`
    - `copy = <method 'copy' of 'dict' objects>`
    - `fromkeys = <built-in method fromkeys of _TypedDictMeta object at 0x55fa9ad0ccf0>`
    - `get = <method 'get' of 'dict' objects>`
    - `items = <method 'items' of 'dict' objects>`
    - `keys = <method 'keys' of 'dict' objects>`
    - `pop = <method 'pop' of 'dict' objects>`
    - `popitem = <method 'popitem' of 'dict' objects>`
    - `setdefault = <method 'setdefault' of 'dict' objects>`
    - `update = <method 'update' of 'dict' objects>`
    - `values = <method 'values' of 'dict' objects>`
  </details>
  - `DirectoryPath = typing.Annotated[pathlib.Path, PathType(path_type='dir')]`
  <details><summary>`class Discriminator(object)`</summary>
    <details><summary>`__delattr__ (self, name)`</summary>
    </details>
    <details><summary>`__eq__ (self, other)`</summary>
    </details>
    <details><summary>`__get_pydantic_core_schema__ (self, source_type: 'Any', handler: 'GetCoreSchemaHandler') -> 'CoreSchema'`</summary>
    </details>
    <details><summary>`__getstate__ (self)`</summary>
    </details>
    <details><summary>`__hash__ (self)`</summary>
    </details>
    <details><summary>`__init__ (self, discriminator: 'str | Callable[[Any], Hashable]', custom_error_type: 'str | None' = None, custom_error_message: 'str | None' = None, custom_error_context: 'dict[str, int | str | float] | None' = None) -> None`</summary>
    </details>
    <details><summary>`__repr__ (self)`</summary>
    </details>
    <details><summary>`__setattr__ (self, name, value)`</summary>
    </details>
    <details><summary>`__setstate__ (self, state)`</summary>
    </details>
    <details><summary>`_convert_schema (self, original_schema: 'core_schema.CoreSchema') -> 'core_schema.TaggedUnionSchema'`</summary>
    </details>
    - `custom_error_context = <member 'custom_error_context' of 'Discriminator' objects>`
    - `custom_error_message = <member 'custom_error_message' of 'Discriminator' objects>`
    - `custom_error_type = <member 'custom_error_type' of 'Discriminator' objects>`
    - `discriminator = <member 'discriminator' of 'Discriminator' objects>`
  </details>
  <details><summary>`class EmailStr(object)`</summary>
    <details><summary>`__get_pydantic_core_schema__ (_source: 'type[Any]', _handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'`</summary>
    </details>
    <details><summary>`__get_pydantic_json_schema__ (core_schema: 'core_schema.CoreSchema', handler: '_schema_generation_shared.GetJsonSchemaHandler') -> 'JsonSchemaValue'`</summary>
    </details>
    <details><summary>`_validate (input_value: 'str', /) -> 'str'`</summary>
    </details>
  </details>
  <details><summary>`class EncodedBytes(object)`</summary>
    <details><summary>`__eq__ (self, other)`</summary>
    </details>
    <details><summary>`__get_pydantic_core_schema__ (self, source: 'type[Any]', handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'`</summary>
    </details>
    <details><summary>`__get_pydantic_json_schema__ (self, core_schema: 'core_schema.CoreSchema', handler: 'GetJsonSchemaHandler') -> 'JsonSchemaValue'`</summary>
    </details>
    <details><summary>`__hash__ (self) -> 'int'`</summary>
    </details>
    <details><summary>`__init__ (self, encoder: 'type[EncoderProtocol]') -> None`</summary>
    </details>
    <details><summary>`__repr__ (self)`</summary>
    </details>
    <details><summary>`decode (self, data: 'bytes', _: 'core_schema.ValidationInfo') -> 'bytes'`</summary>
    </details>
    <details><summary>`encode (self, value: 'bytes') -> 'bytes'`</summary>
    </details>
    - `encoder = <member 'encoder' of 'EncodedBytes' objects>`
  </details>
  <details><summary>`class EncodedStr(EncodedBytes)`</summary>
    <details><summary>`__eq__ (self, other)`</summary>
    </details>
    <details><summary>`__get_pydantic_core_schema__ (self, source: 'type[Any]', handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'`</summary>
    </details>
    <details><summary>`__get_pydantic_json_schema__ (self, core_schema: 'core_schema.CoreSchema', handler: 'GetJsonSchemaHandler') -> 'JsonSchemaValue'`</summary>
    </details>
    <details><summary>`__hash__ (self) -> 'int'`</summary>
    </details>
    <details><summary>`__init__ (self, encoder: 'type[EncoderProtocol]') -> None`</summary>
    </details>
    <details><summary>`__repr__ (self)`</summary>
    </details>
    <details><summary>`decode (self, data: 'bytes', _: 'core_schema.ValidationInfo') -> 'bytes'`</summary>
    </details>
    <details><summary>`decode_str (self, data: 'bytes', _: 'core_schema.ValidationInfo') -> 'str'`</summary>
    </details>
    <details><summary>`encode (self, value: 'bytes') -> 'bytes'`</summary>
    </details>
    <details><summary>`encode_str (self, value: 'str') -> 'str'`</summary>
    </details>
    - `encoder = <member 'encoder' of 'EncodedBytes' objects>`
  </details>
  <details><summary>`class EncoderProtocol(Protocol)`</summary>
    <details><summary>`__class_getitem__ (params)`</summary>
    </details>
    <details><summary>`__init__ (self, *args, **kwargs)`</summary>
    </details>
    <details><summary>`__init_subclass__ (*args, **kwargs)`</summary>
    </details>
    <details><summary>`__subclasshook__ (other)`</summary>
    </details>
    <details><summary>`decode (data: 'bytes') -> 'bytes'`</summary>
    </details>
    <details><summary>`encode (value: 'bytes') -> 'bytes'`</summary>
    </details>
    <details><summary>`get_json_format () -> 'str'`</summary>
    </details>
  </details>
  <details><summary>`class Extra(object)`</summary>
    - `__init_subclass__ <signature unavailable>`
    <details><summary>`__new__ (*args, **kwargs)`</summary>
    </details>
    - `allow = 'allow'`
    - `forbid = 'forbid'`
    - `ignore = 'ignore'`
  </details>
  <details><summary>`class FailFast(PydanticMetadata, BaseMetadata)`</summary>
    <details><summary>`__eq__ (self, other)`</summary>
    </details>
    <details><summary>`__init__ (self, fail_fast: 'bool' = True) -> None`</summary>
    </details>
    <details><summary>`__pretty__ (self, fmt: 'typing.Callable[[Any], Any]', **kwargs: 'Any') -> 'typing.Generator[Any, None, None]'`</summary>
    </details>
    <details><summary>`__repr__ (self)`</summary>
    </details>
    <details><summary>`__repr_args__ (self) -> 'ReprArgs'`</summary>
    </details>
    <details><summary>`__repr_name__ (self) -> 'str'`</summary>
    </details>
    <details><summary>`__repr_str__ (self, join_str: 'str') -> 'str'`</summary>
    </details>
    <details><summary>`__rich_repr__ (self) -> 'RichReprResult'`</summary>
    </details>
    <details><summary>`__str__ (self) -> 'str'`</summary>
    </details>
    - `fail_fast = True`
  </details>
  <details><summary>`Field (default: 'Any' = PydanticUndefined, *, default_factory: 'typing.Callable[[], Any] | None' = PydanticUndefined, alias: 'str | None' = PydanticUndefined, alias_priority: 'int | None' = PydanticUndefined, validation_alias: 'str | AliasPath | AliasChoices | None' = PydanticUndefined, serialization_alias: 'str | None' = PydanticUndefined, title: 'str | None' = PydanticUndefined, field_title_generator: 'typing_extensions.Callable[[str, FieldInfo], str] | None' = PydanticUndefined, description: 'str | None' = PydanticUndefined, examples: 'list[Any] | None' = PydanticUndefined, exclude: 'bool | None' = PydanticUndefined, discriminator: 'str | types.Discriminator | None' = PydanticUndefined, deprecated: 'Deprecated | str | bool | None' = PydanticUndefined, json_schema_extra: 'JsonDict | typing.Callable[[JsonDict], None] | None' = PydanticUndefined, frozen: 'bool | None' = PydanticUndefined, validate_default: 'bool | None' = PydanticUndefined, repr: 'bool' = PydanticUndefined, init: 'bool | None' = PydanticUndefined, init_var: 'bool | None' = PydanticUndefined, kw_only: 'bool | None' = PydanticUndefined, pattern: 'str | typing.Pattern[str] | None' = PydanticUndefined, strict: 'bool | None' = PydanticUndefined, coerce_numbers_to_str: 'bool | None' = PydanticUndefined, gt: 'annotated_types.SupportsGt | None' = PydanticUndefined, ge: 'annotated_types.SupportsGe | None' = PydanticUndefined, lt: 'annotated_types.SupportsLt | None' = PydanticUndefined, le: 'annotated_types.SupportsLe | None' = PydanticUndefined, multiple_of: 'float | None' = PydanticUndefined, allow_inf_nan: 'bool | None' = PydanticUndefined, max_digits: 'int | None' = PydanticUndefined, decimal_places: 'int | None' = PydanticUndefined, min_length: 'int | None' = PydanticUndefined, max_length: 'int | None' = PydanticUndefined, union_mode: "Literal['smart', 'left_to_right']" = PydanticUndefined, fail_fast: 'bool | None' = PydanticUndefined, **extra: 'Unpack[_EmptyKwargs]') -> 'Any'`</summary>
  </details>
  <details><summary>`class FieldSerializationInfo(SerializationInfo, Protocol)`</summary>
    <details><summary>`__class_getitem__ (params)`</summary>
    </details>
    <details><summary>`__init__ (self, *args, **kwargs)`</summary>
    </details>
    <details><summary>`__init_subclass__ (*args, **kwargs)`</summary>
    </details>
    <details><summary>`__repr__ (self) -> 'str'`</summary>
    </details>
    <details><summary>`__str__ (self) -> 'str'`</summary>
    </details>
    <details><summary>`__subclasshook__ (other)`</summary>
    </details>
    - `by_alias = <property object at 0x7f13faf32d40>`
    - `context = <property object at 0x7f13faf0c680>`
    - `exclude = <property object at 0x7f13faf07e70>`
    - `exclude_defaults = <property object at 0x7f13faf32e30>`
    - `exclude_none = <property object at 0x7f13faf32e80>`
    - `exclude_unset = <property object at 0x7f13faf32de0>`
    - `field_name = <property object at 0x7f13faf32f70>`
    - `include = <property object at 0x7f13fb2918a0>`
    - `mode = <property object at 0x7f13faf32d90>`
    <details><summary>`mode_is_json (self) -> 'bool'`</summary>
    </details>
    <details><summary>`round_trip (self) -> 'bool'`</summary>
    </details>
    - `serialize_as_any = <property object at 0x7f13faf32ed0>`
  </details>
  - `FilePath = typing.Annotated[pathlib.Path, PathType(path_type='file')]`
  - `FileUrl = typing.Annotated[pydantic_core._pydantic_core.Url, UrlConstraints(max_length=None, allowed_schemes=['file'], host_required=None, default_host=None, default_port=None, default_path=None)]`
  - `FiniteFloat = typing.Annotated[float, AllowInfNan(allow_inf_nan=False)]`
  - `FtpUrl = typing.Annotated[pydantic_core._pydantic_core.Url, UrlConstraints(max_length=None, allowed_schemes=['ftp'], host_required=None, default_host=None, default_port=None, default_path=None)]`
  <details><summary>`class FutureDate(object)`</summary>
    <details><summary>`__get_pydantic_core_schema__ (source: 'type[Any]', handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'`</summary>
    </details>
    <details><summary>`__repr__ (self) -> 'str'`</summary>
    </details>
  </details>
  <details><summary>`class FutureDatetime(object)`</summary>
    <details><summary>`__get_pydantic_core_schema__ (source: 'type[Any]', handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'`</summary>
    </details>
    <details><summary>`__repr__ (self) -> 'str'`</summary>
    </details>
  </details>
  <details><summary>`class GenerateSchema(object)`</summary>
    - `CollectedInvalid = <class 'pydantic._internal._generate_schema.GenerateSchema.CollectedInvalid'>`
    <details><summary>`_GenerateSchema__from_parent (config_wrapper_stack: 'ConfigWrapperStack', types_namespace_stack: 'TypesNamespaceStack', model_type_stack: '_ModelTypeStack', typevars_map: 'dict[Any, Any] | None', defs: '_Definitions') -> 'GenerateSchema'`</summary>
    </details>
    <details><summary>`__init__ (self, config_wrapper: 'ConfigWrapper', types_namespace: 'dict[str, Any] | None', typevars_map: 'dict[Any, Any] | None' = None) -> 'None'`</summary>
    </details>
    <details><summary>`_add_js_function (self, metadata_schema: 'CoreSchema', js_function: 'Callable[..., Any]') -> 'None'`</summary>
    </details>
    <details><summary>`_annotated_schema (self, annotated_type: 'Any') -> 'core_schema.CoreSchema'`</summary>
    </details>
    <details><summary>`_apply_alias_generator_to_computed_field_info (alias_generator: 'Callable[[str], str] | AliasGenerator', computed_field_info: 'ComputedFieldInfo', computed_field_name: 'str')`</summary>
    </details>
    <details><summary>`_apply_alias_generator_to_field_info (alias_generator: 'Callable[[str], str] | AliasGenerator', field_info: 'FieldInfo', field_name: 'str') -> 'None'`</summary>
    </details>
    <details><summary>`_apply_annotations (self, source_type: 'Any', annotations: 'list[Any]', transform_inner_schema: 'Callable[[CoreSchema], CoreSchema]' = <function GenerateSchema.<lambda> at 0x7f13fa4b02c0>) -> 'CoreSchema'`</summary>
    </details>
    <details><summary>`_apply_discriminator_to_union (self, schema: 'CoreSchema', discriminator: 'str | Discriminator | None') -> 'CoreSchema'`</summary>
    </details>
    <details><summary>`_apply_field_serializers (self, schema: 'core_schema.CoreSchema', serializers: 'list[Decorator[FieldSerializerDecoratorInfo]]', computed_field: 'bool' = False) -> 'core_schema.CoreSchema'`</summary>
    </details>
    <details><summary>`_apply_field_title_generator_to_field_info (config_wrapper: 'ConfigWrapper', field_info: 'FieldInfo | ComputedFieldInfo', field_name: 'str') -> 'None'`</summary>
    </details>
    <details><summary>`_apply_model_serializers (self, schema: 'core_schema.CoreSchema', serializers: 'Iterable[Decorator[ModelSerializerDecoratorInfo]]') -> 'core_schema.CoreSchema'`</summary>
    </details>
    <details><summary>`_apply_single_annotation (self, schema: 'core_schema.CoreSchema', metadata: 'Any') -> 'core_schema.CoreSchema'`</summary>
    </details>
    <details><summary>`_apply_single_annotation_json_schema (self, schema: 'core_schema.CoreSchema', metadata: 'Any') -> 'core_schema.CoreSchema'`</summary>
    </details>
    <details><summary>`_arbitrary_type_schema (self, tp: 'Any') -> 'CoreSchema'`</summary>
    </details>
    <details><summary>`_callable_schema (self, function: 'Callable[..., Any]') -> 'core_schema.CallSchema'`</summary>
    </details>
    <details><summary>`_common_field_schema (self, name: 'str', field_info: 'FieldInfo', decorators: 'DecoratorInfos') -> '_CommonField'`</summary>
    </details>
    <details><summary>`_computed_field_schema (self, d: 'Decorator[ComputedFieldInfo]', field_serializers: 'dict[str, Decorator[FieldSerializerDecoratorInfo]]') -> 'core_schema.ComputedField'`</summary>
    </details>
    <details><summary>`_dataclass_schema (self, dataclass: 'type[StandardDataclass]', origin: 'type[StandardDataclass] | None') -> 'core_schema.CoreSchema'`</summary>
    </details>
    <details><summary>`_dict_schema (self, keys_type: 'Any', values_type: 'Any') -> 'CoreSchema'`</summary>
    </details>
    <details><summary>`_enum_schema (self, enum_type: 'type[Enum]') -> 'CoreSchema'`</summary>
    </details>
    <details><summary>`_frozenset_schema (self, items_type: 'Any') -> 'CoreSchema'`</summary>
    </details>
    <details><summary>`_generate_dc_field_schema (self, name: 'str', field_info: 'FieldInfo', decorators: 'DecoratorInfos') -> 'core_schema.DataclassField'`</summary>
    </details>
    <details><summary>`_generate_md_field_schema (self, name: 'str', field_info: 'FieldInfo', decorators: 'DecoratorInfos') -> 'core_schema.ModelField'`</summary>
    </details>
    <details><summary>`_generate_parameter_schema (self, name: 'str', annotation: 'type[Any]', default: 'Any', mode: "Literal['positional_only', 'positional_or_keyword', 'keyword_only'] | None" = None) -> 'core_schema.ArgumentsParameter'`</summary>
    </details>
    <details><summary>`_generate_schema_from_property (self, obj: 'Any', source: 'Any') -> 'core_schema.CoreSchema | None'`</summary>
    </details>
    <details><summary>`_generate_schema_inner (self, obj: 'Any') -> 'core_schema.CoreSchema'`</summary>
    </details>
    <details><summary>`_generate_td_field_schema (self, name: 'str', field_info: 'FieldInfo', decorators: 'DecoratorInfos', *, required: 'bool' = True) -> 'core_schema.TypedDictField'`</summary>
    </details>
    <details><summary>`_get_args_resolving_forward_refs (self, obj: 'Any', required: 'bool' = False) -> 'tuple[Any, ...] | None'`</summary>
    </details>
    <details><summary>`_get_first_arg_or_any (self, obj: 'Any') -> 'Any'`</summary>
    </details>
    <details><summary>`_get_first_two_args_or_any (self, obj: 'Any') -> 'tuple[Any, Any]'`</summary>
    </details>
    <details><summary>`_get_model_title_from_config (model: 'type[BaseModel | StandardDataclass]', config_wrapper: 'ConfigWrapper | None' = None) -> 'str | None'`</summary>
    </details>
    <details><summary>`_get_prepare_pydantic_annotations_for_known_type (self, obj: 'Any', annotations: 'tuple[Any, ...]') -> 'tuple[Any, list[Any]] | None'`</summary>
    </details>
    <details><summary>`_get_wrapped_inner_schema (self, get_inner_schema: 'GetCoreSchemaHandler', annotation: 'Any', pydantic_js_annotation_functions: 'list[GetJsonSchemaFunction]') -> 'CallbackGetCoreSchemaHandler'`</summary>
    </details>
    <details><summary>`_hashable_schema (self) -> 'core_schema.CoreSchema'`</summary>
    </details>
    <details><summary>`_ip_schema (self, tp: 'Any') -> 'CoreSchema'`</summary>
    </details>
    <details><summary>`_iterable_schema (self, type_: 'Any') -> 'core_schema.GeneratorSchema'`</summary>
    </details>
    <details><summary>`_list_schema (self, items_type: 'Any') -> 'CoreSchema'`</summary>
    </details>
    <details><summary>`_literal_schema (self, literal_type: 'Any') -> 'CoreSchema'`</summary>
    </details>
    <details><summary>`_match_generic_type (self, obj: 'Any', origin: 'Any') -> 'CoreSchema'`</summary>
    </details>
    <details><summary>`_model_schema (self, cls: 'type[BaseModel]') -> 'core_schema.CoreSchema'`</summary>
    </details>
    <details><summary>`_namedtuple_schema (self, namedtuple_cls: 'Any', origin: 'Any') -> 'core_schema.CoreSchema'`</summary>
    </details>
    <details><summary>`_pattern_schema (self, pattern_type: 'Any') -> 'core_schema.CoreSchema'`</summary>
    </details>
    <details><summary>`_resolve_forward_ref (self, obj: 'Any') -> 'Any'`</summary>
    </details>
    <details><summary>`_sequence_schema (self, items_type: 'Any') -> 'core_schema.CoreSchema'`</summary>
    </details>
    <details><summary>`_set_schema (self, items_type: 'Any') -> 'CoreSchema'`</summary>
    </details>
    <details><summary>`_subclass_schema (self, type_: 'Any') -> 'core_schema.CoreSchema'`</summary>
    </details>
    <details><summary>`_tuple_schema (self, tuple_type: 'Any') -> 'core_schema.CoreSchema'`</summary>
    </details>
    <details><summary>`_type_alias_type_schema (self, obj: 'Any') -> 'CoreSchema'`</summary>
    </details>
    <details><summary>`_type_schema (self) -> 'core_schema.CoreSchema'`</summary>
    </details>
    <details><summary>`_typed_dict_schema (self, typed_dict_cls: 'Any', origin: 'Any') -> 'core_schema.CoreSchema'`</summary>
    </details>
    <details><summary>`_union_is_subclass_schema (self, union_type: 'Any') -> 'core_schema.CoreSchema'`</summary>
    </details>
    <details><summary>`_union_schema (self, union_type: 'Any') -> 'core_schema.CoreSchema'`</summary>
    </details>
    <details><summary>`_unknown_type_schema (self, obj: 'Any') -> 'CoreSchema'`</summary>
    </details>
    <details><summary>`_unpack_refs_defs (self, schema: 'CoreSchema') -> 'CoreSchema'`</summary>
    </details>
    <details><summary>`_unsubstituted_typevar_schema (self, typevar: 'typing.TypeVar') -> 'core_schema.CoreSchema'`</summary>
    </details>
    <details><summary>`_zoneinfo_schema (self) -> 'core_schema.CoreSchema'`</summary>
    </details>
    <details><summary>`clean_schema (self, schema: 'CoreSchema') -> 'CoreSchema'`</summary>
    </details>
    <details><summary>`collect_definitions (self, schema: 'CoreSchema') -> 'CoreSchema'`</summary>
    </details>
    - `defs = <member 'defs' of 'GenerateSchema' objects>`
    - `field_name_stack = <member 'field_name_stack' of 'GenerateSchema' objects>`
    <details><summary>`generate_schema (self, obj: 'Any', from_dunder_get_core_schema: 'bool' = True) -> 'core_schema.CoreSchema'`</summary>
    </details>
    <details><summary>`match_type (self, obj: 'Any') -> 'core_schema.CoreSchema'`</summary>
    </details>
    - `model_type_stack = <member 'model_type_stack' of 'GenerateSchema' objects>`
    <details><summary>`str_schema (self) -> 'CoreSchema'`</summary>
    </details>
  </details>
  <details><summary>`class GetCoreSchemaHandler(object)`</summary>
    <details><summary>`__call__ (self, source_type: 'Any', /) -> 'core_schema.CoreSchema'`</summary>
    </details>
    <details><summary>`_get_types_namespace (self) -> 'dict[str, Any] | None'`</summary>
    </details>
    - `field_name = <property object at 0x7f13faee2340>`
    <details><summary>`generate_schema (self, source_type: 'Any', /) -> 'core_schema.CoreSchema'`</summary>
    </details>
    <details><summary>`resolve_ref_schema (self, maybe_ref_schema: 'core_schema.CoreSchema', /) -> 'core_schema.CoreSchema'`</summary>
    </details>
  </details>
  <details><summary>`class GetJsonSchemaHandler(object)`</summary>
    <details><summary>`__call__ (self, core_schema: 'CoreSchemaOrField', /) -> 'JsonSchemaValue'`</summary>
    </details>
    <details><summary>`resolve_ref_schema (self, maybe_ref_json_schema: 'JsonSchemaValue', /) -> 'JsonSchemaValue'`</summary>
    </details>
  </details>
  <details><summary>`class GetPydanticSchema(object)`</summary>
    <details><summary>`__eq__ (self, other)`</summary>
    </details>
    <details><summary>`__getattr__ (self, item: 'str') -> 'Any'`</summary>
    </details>
    <details><summary>`__init__ (self, get_pydantic_core_schema: 'Callable[[Any, GetCoreSchemaHandler], CoreSchema] | None' = None, get_pydantic_json_schema: 'Callable[[Any, GetJsonSchemaHandler], JsonSchemaValue] | None' = None) -> None`</summary>
    </details>
    <details><summary>`__repr__ (self)`</summary>
    </details>
    - `get_pydantic_core_schema = <member 'get_pydantic_core_schema' of 'GetPydanticSchema' objects>`
    - `get_pydantic_json_schema = <member 'get_pydantic_json_schema' of 'GetPydanticSchema' objects>`
  </details>
  - `HttpUrl = typing.Annotated[pydantic_core._pydantic_core.Url, UrlConstraints(max_length=2083, allowed_schemes=['http', 'https'], host_required=None, default_host=None, default_port=None, default_path=None)]`
  <details><summary>`class IPvAnyAddress(object)`</summary>
    <details><summary>`__get_pydantic_core_schema__ (_source: 'type[Any]', _handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'`</summary>
    </details>
    <details><summary>`__get_pydantic_json_schema__ (core_schema: 'core_schema.CoreSchema', handler: '_schema_generation_shared.GetJsonSchemaHandler') -> 'JsonSchemaValue'`</summary>
    </details>
    <details><summary>`__new__ (cls, value: 'Any') -> 'IPvAnyAddressType'`</summary>
    </details>
    <details><summary>`_validate (input_value: 'Any', /) -> 'IPvAnyAddressType'`</summary>
    </details>
  </details>
  <details><summary>`class IPvAnyInterface(object)`</summary>
    <details><summary>`__get_pydantic_core_schema__ (_source: 'type[Any]', _handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'`</summary>
    </details>
    <details><summary>`__get_pydantic_json_schema__ (core_schema: 'core_schema.CoreSchema', handler: '_schema_generation_shared.GetJsonSchemaHandler') -> 'JsonSchemaValue'`</summary>
    </details>
    <details><summary>`__new__ (cls, value: 'NetworkType') -> 'IPvAnyInterfaceType'`</summary>
    </details>
    <details><summary>`_validate (input_value: 'NetworkType', /) -> 'IPvAnyInterfaceType'`</summary>
    </details>
  </details>
  <details><summary>`class IPvAnyNetwork(object)`</summary>
    <details><summary>`__get_pydantic_core_schema__ (_source: 'type[Any]', _handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'`</summary>
    </details>
    <details><summary>`__get_pydantic_json_schema__ (core_schema: 'core_schema.CoreSchema', handler: '_schema_generation_shared.GetJsonSchemaHandler') -> 'JsonSchemaValue'`</summary>
    </details>
    <details><summary>`__new__ (cls, value: 'NetworkType') -> 'IPvAnyNetworkType'`</summary>
    </details>
    <details><summary>`_validate (input_value: 'NetworkType', /) -> 'IPvAnyNetworkType'`</summary>
    </details>
  </details>
  <details><summary>`class ImportString(object)`</summary>
    <details><summary>`__class_getitem__ (item: 'AnyType') -> 'AnyType'`</summary>
    </details>
    <details><summary>`__get_pydantic_core_schema__ (source: 'type[Any]', handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'`</summary>
    </details>
    <details><summary>`__get_pydantic_json_schema__ (cs: 'CoreSchema', handler: 'GetJsonSchemaHandler') -> 'JsonSchemaValue'`</summary>
    </details>
    <details><summary>`__repr__ (self) -> 'str'`</summary>
    </details>
    <details><summary>`_serialize (v: 'Any') -> 'str'`</summary>
    </details>
  </details>
  <details><summary>`class InstanceOf(object)`</summary>
    <details><summary>`__class_getitem__ (item: 'AnyType') -> 'AnyType'`</summary>
    </details>
    <details><summary>`__eq__ (self, other)`</summary>
    </details>
    <details><summary>`__get_pydantic_core_schema__ (source: 'Any', handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'`</summary>
    </details>
    <details><summary>`__init__ (self) -> None`</summary>
    </details>
    <details><summary>`__repr__ (self)`</summary>
    </details>
  </details>
  <details><summary>`class Json(object)`</summary>
    <details><summary>`__class_getitem__ (item: 'AnyType') -> 'AnyType'`</summary>
    </details>
    <details><summary>`__eq__ (self, other: 'Any') -> 'bool'`</summary>
    </details>
    <details><summary>`__get_pydantic_core_schema__ (source: 'Any', handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'`</summary>
    </details>
    <details><summary>`__hash__ (self) -> 'int'`</summary>
    </details>
    <details><summary>`__repr__ (self) -> 'str'`</summary>
    </details>
  </details>
  - `JsonValue = JsonValue`
  - `KafkaDsn = typing.Annotated[pydantic_core._pydantic_core.Url, UrlConstraints(max_length=None, allowed_schemes=['kafka'], host_required=None, default_host='localhost', default_port=9092, default_path=None)]`
  - `MariaDBDsn = typing.Annotated[pydantic_core._pydantic_core.Url, UrlConstraints(max_length=None, allowed_schemes=['mariadb', 'mariadb+mariadbconnector', 'mariadb+pymysql'], host_required=None, default_host=None, default_port=3306, default_path=None)]`
  - `MongoDsn = typing.Annotated[pydantic_core._pydantic_core.MultiHostUrl, UrlConstraints(max_length=None, allowed_schemes=['mongodb', 'mongodb+srv'], host_required=None, default_host=None, default_port=27017, default_path=None)]`
  - `MySQLDsn = typing.Annotated[pydantic_core._pydantic_core.Url, UrlConstraints(max_length=None, allowed_schemes=['mysql', 'mysql+mysqlconnector', 'mysql+aiomysql', 'mysql+asyncmy', 'mysql+mysqldb', 'mysql+pymysql', 'mysql+cymysql', 'mysql+pyodbc'], host_required=None, default_host=None, default_port=3306, default_path=None)]`
  <details><summary>`class NaiveDatetime(object)`</summary>
    <details><summary>`__get_pydantic_core_schema__ (source: 'type[Any]', handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'`</summary>
    </details>
    <details><summary>`__repr__ (self) -> 'str'`</summary>
    </details>
  </details>
  <details><summary>`class NameEmail(Representation)`</summary>
    <details><summary>`__eq__ (self, other: 'Any') -> 'bool'`</summary>
    </details>
    <details><summary>`__get_pydantic_core_schema__ (_source: 'type[Any]', _handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'`</summary>
    </details>
    <details><summary>`__get_pydantic_json_schema__ (core_schema: 'core_schema.CoreSchema', handler: '_schema_generation_shared.GetJsonSchemaHandler') -> 'JsonSchemaValue'`</summary>
    </details>
    <details><summary>`__init__ (self, name: 'str', email: 'str')`</summary>
    </details>
    <details><summary>`__pretty__ (self, fmt: 'typing.Callable[[Any], Any]', **kwargs: 'Any') -> 'typing.Generator[Any, None, None]'`</summary>
    </details>
    <details><summary>`__repr__ (self) -> 'str'`</summary>
    </details>
    <details><summary>`__repr_args__ (self) -> 'ReprArgs'`</summary>
    </details>
    <details><summary>`__repr_name__ (self) -> 'str'`</summary>
    </details>
    <details><summary>`__repr_str__ (self, join_str: 'str') -> 'str'`</summary>
    </details>
    <details><summary>`__rich_repr__ (self) -> 'RichReprResult'`</summary>
    </details>
    <details><summary>`__str__ (self) -> 'str'`</summary>
    </details>
    <details><summary>`_validate (input_value: 'Self | str', /) -> 'Self'`</summary>
    </details>
    - `email = <member 'email' of 'NameEmail' objects>`
    - `name = <member 'name' of 'NameEmail' objects>`
  </details>
  - `NatsDsn = typing.Annotated[pydantic_core._pydantic_core.MultiHostUrl, UrlConstraints(max_length=None, allowed_schemes=['nats', 'tls', 'ws', 'wss'], host_required=None, default_host='localhost', default_port=4222, default_path=None)]`
  - `NegativeFloat = typing.Annotated[float, Lt(lt=0)]`
  - `NegativeInt = typing.Annotated[int, Lt(lt=0)]`
  - `NewPath = typing.Annotated[pathlib.Path, PathType(path_type='new')]`
  - `NonNegativeFloat = typing.Annotated[float, Ge(ge=0)]`
  - `NonNegativeInt = typing.Annotated[int, Ge(ge=0)]`
  - `NonPositiveFloat = typing.Annotated[float, Le(le=0)]`
  - `NonPositiveInt = typing.Annotated[int, Le(le=0)]`
  - `OnErrorOmit = typing.Annotated[~T, <class 'pydantic.types._OnErrorOmit'>]`
  <details><summary>`class PastDate(object)`</summary>
    <details><summary>`__get_pydantic_core_schema__ (source: 'type[Any]', handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'`</summary>
    </details>
    <details><summary>`__repr__ (self) -> 'str'`</summary>
    </details>
  </details>
  <details><summary>`class PastDatetime(object)`</summary>
    <details><summary>`__get_pydantic_core_schema__ (source: 'type[Any]', handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'`</summary>
    </details>
    <details><summary>`__repr__ (self) -> 'str'`</summary>
    </details>
  </details>
  <details><summary>`class PaymentCardNumber(str)`</summary>
    <details><summary>`__get_pydantic_core_schema__ (source: 'type[Any]', handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'`</summary>
    </details>
    <details><summary>`__init__ (self, card_number: 'str')`</summary>
    </details>
    - `__init_subclass__ <signature unavailable>`
    <details><summary>`__new__ (*args, **kwargs)`</summary>
    </details>
    - `capitalize = <method 'capitalize' of 'str' objects>`
    - `casefold = <method 'casefold' of 'str' objects>`
    - `center = <method 'center' of 'str' objects>`
    - `count = <method 'count' of 'str' objects>`
    - `encode = <method 'encode' of 'str' objects>`
    - `endswith = <method 'endswith' of 'str' objects>`
    - `expandtabs = <method 'expandtabs' of 'str' objects>`
    - `find = <method 'find' of 'str' objects>`
    - `format = <method 'format' of 'str' objects>`
    - `format_map = <method 'format_map' of 'str' objects>`
    - `index = <method 'index' of 'str' objects>`
    - `isalnum = <method 'isalnum' of 'str' objects>`
    - `isalpha = <method 'isalpha' of 'str' objects>`
    - `isascii = <method 'isascii' of 'str' objects>`
    - `isdecimal = <method 'isdecimal' of 'str' objects>`
    - `isdigit = <method 'isdigit' of 'str' objects>`
    - `isidentifier = <method 'isidentifier' of 'str' objects>`
    - `islower = <method 'islower' of 'str' objects>`
    - `isnumeric = <method 'isnumeric' of 'str' objects>`
    - `isprintable = <method 'isprintable' of 'str' objects>`
    - `isspace = <method 'isspace' of 'str' objects>`
    - `istitle = <method 'istitle' of 'str' objects>`
    - `isupper = <method 'isupper' of 'str' objects>`
    - `join = <method 'join' of 'str' objects>`
    - `ljust = <method 'ljust' of 'str' objects>`
    - `lower = <method 'lower' of 'str' objects>`
    - `lstrip = <method 'lstrip' of 'str' objects>`
    - `maketrans = <built-in method maketrans of type object at 0x55fa99f75f60>`
    - `masked = <property object at 0x7f13fa746250>`
    - `max_length = 19`
    - `min_length = 12`
    - `partition = <method 'partition' of 'str' objects>`
    - `removeprefix = <method 'removeprefix' of 'str' objects>`
    - `removesuffix = <method 'removesuffix' of 'str' objects>`
    - `replace = <method 'replace' of 'str' objects>`
    - `rfind = <method 'rfind' of 'str' objects>`
    - `rindex = <method 'rindex' of 'str' objects>`
    - `rjust = <method 'rjust' of 'str' objects>`
    - `rpartition = <method 'rpartition' of 'str' objects>`
    - `rsplit = <method 'rsplit' of 'str' objects>`
    - `rstrip = <method 'rstrip' of 'str' objects>`
    - `split = <method 'split' of 'str' objects>`
    - `splitlines = <method 'splitlines' of 'str' objects>`
    - `startswith = <method 'startswith' of 'str' objects>`
    - `strip = <method 'strip' of 'str' objects>`
    - `strip_whitespace = True`
    - `swapcase = <method 'swapcase' of 'str' objects>`
    - `title = <method 'title' of 'str' objects>`
    - `translate = <method 'translate' of 'str' objects>`
    - `upper = <method 'upper' of 'str' objects>`
    <details><summary>`validate (input_value: 'str', /, _: 'core_schema.ValidationInfo') -> 'PaymentCardNumber'`</summary>
    </details>
    <details><summary>`validate_brand (card_number: 'str') -> 'PaymentCardBrand'`</summary>
    </details>
    <details><summary>`validate_digits (card_number: 'str') -> 'None'`</summary>
    </details>
    <details><summary>`validate_luhn_check_digit (card_number: 'str') -> 'str'`</summary>
    </details>
    - `zfill = <method 'zfill' of 'str' objects>`
  </details>
  <details><summary>`class PlainSerializer(object)`</summary>
    <details><summary>`__delattr__ (self, name)`</summary>
    </details>
    <details><summary>`__eq__ (self, other)`</summary>
    </details>
    <details><summary>`__get_pydantic_core_schema__ (self, source_type: 'Any', handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'`</summary>
    </details>
    <details><summary>`__getstate__ (self)`</summary>
    </details>
    <details><summary>`__hash__ (self)`</summary>
    </details>
    <details><summary>`__init__ (self, func: 'core_schema.SerializerFunction', return_type: 'Any' = PydanticUndefined, when_used: 'WhenUsed' = 'always') -> None`</summary>
    </details>
    <details><summary>`__repr__ (self)`</summary>
    </details>
    <details><summary>`__setattr__ (self, name, value)`</summary>
    </details>
    <details><summary>`__setstate__ (self, state)`</summary>
    </details>
    - `func = <member 'func' of 'PlainSerializer' objects>`
    - `return_type = <member 'return_type' of 'PlainSerializer' objects>`
    - `when_used = <member 'when_used' of 'PlainSerializer' objects>`
  </details>
  <details><summary>`class PlainValidator(object)`</summary>
    <details><summary>`__delattr__ (self, name)`</summary>
    </details>
    <details><summary>`__eq__ (self, other)`</summary>
    </details>
    <details><summary>`__get_pydantic_core_schema__ (self, source_type: 'Any', handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'`</summary>
    </details>
    <details><summary>`__getstate__ (self)`</summary>
    </details>
    <details><summary>`__hash__ (self)`</summary>
    </details>
    <details><summary>`__init__ (self, func: 'core_schema.NoInfoValidatorFunction | core_schema.WithInfoValidatorFunction', json_schema_input_type: 'Any' = typing.Any) -> None`</summary>
    </details>
    <details><summary>`__repr__ (self)`</summary>
    </details>
    <details><summary>`__setattr__ (self, name, value)`</summary>
    </details>
    <details><summary>`__setstate__ (self, state)`</summary>
    </details>
    <details><summary>`_from_decorator (decorator: '_decorators.Decorator[_decorators.FieldValidatorDecoratorInfo]') -> 'Self'`</summary>
    </details>
    - `func = <member 'func' of 'PlainValidator' objects>`
    - `json_schema_input_type = <member 'json_schema_input_type' of 'PlainValidator' objects>`
  </details>
  - `PositiveFloat = typing.Annotated[float, Gt(gt=0)]`
  - `PositiveInt = typing.Annotated[int, Gt(gt=0)]`
  - `PostgresDsn = typing.Annotated[pydantic_core._pydantic_core.MultiHostUrl, UrlConstraints(max_length=None, allowed_schemes=['postgres', 'postgresql', 'postgresql+asyncpg', 'postgresql+pg8000', 'postgresql+psycopg', 'postgresql+psycopg2', 'postgresql+psycopg2cffi', 'postgresql+py-postgresql', 'postgresql+pygresql'], host_required=True, default_host=None, default_port=None, default_path=None)]`
  <details><summary>`PrivateAttr (default: 'Any' = PydanticUndefined, *, default_factory: 'typing.Callable[[], Any] | None' = None, init: 'Literal[False]' = False) -> 'Any'`</summary>
  </details>
  <details><summary>`class PydanticDeprecatedSince20(PydanticDeprecationWarning)`</summary>
    <details><summary>`__init__ (self, message: 'str', *args: 'object') -> 'None'`</summary>
    </details>
    <details><summary>`__str__ (self) -> 'str'`</summary>
    </details>
    - `add_note = <method 'add_note' of 'BaseException' objects>`
    - `args = <attribute 'args' of 'BaseException' objects>`
    - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
  </details>
  <details><summary>`class PydanticDeprecatedSince26(PydanticDeprecationWarning)`</summary>
    <details><summary>`__init__ (self, message: 'str', *args: 'object') -> 'None'`</summary>
    </details>
    <details><summary>`__str__ (self) -> 'str'`</summary>
    </details>
    - `add_note = <method 'add_note' of 'BaseException' objects>`
    - `args = <attribute 'args' of 'BaseException' objects>`
    - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
  </details>
  <details><summary>`class PydanticDeprecatedSince29(PydanticDeprecationWarning)`</summary>
    <details><summary>`__init__ (self, message: 'str', *args: 'object') -> 'None'`</summary>
    </details>
    <details><summary>`__str__ (self) -> 'str'`</summary>
    </details>
    - `add_note = <method 'add_note' of 'BaseException' objects>`
    - `args = <attribute 'args' of 'BaseException' objects>`
    - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
  </details>
  <details><summary>`class PydanticDeprecationWarning(DeprecationWarning)`</summary>
    <details><summary>`__init__ (self, message: 'str', *args: 'object', since: 'tuple[int, int]', expected_removal: 'tuple[int, int] | None' = None) -> 'None'`</summary>
    </details>
    <details><summary>`__str__ (self) -> 'str'`</summary>
    </details>
    - `add_note = <method 'add_note' of 'BaseException' objects>`
    - `args = <attribute 'args' of 'BaseException' objects>`
    - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
  </details>
  - `PydanticErrorCodes = typing.Literal['class-not-fully-defined', 'custom-json-schema', 'decorator-missing-field', 'discriminator-no-field', 'discriminator-alias-type', 'discriminator-needs-literal', 'discriminator-alias', 'discriminator-validator', 'callable-discriminator-no-tag', 'typed-dict-version', 'model-field-overridden', 'model-field-missing-annotation', 'config-both', 'removed-kwargs', 'invalid-for-json-schema', 'json-schema-already-used', 'base-model-instantiated', 'undefined-annotation', 'schema-for-unknown-type', 'import-error', 'create-model-field-definitions', 'create-model-config-base', 'validator-no-fields', 'validator-invalid-fields', 'validator-instance-method', 'validator-input-type', 'root-validator-pre-skip', 'model-serializer-instance-method', 'validator-field-config-info', 'validator-v1-signature', 'validator-signature', 'field-serializer-signature', 'model-serializer-signature', 'multiple-field-serializers', 'invalid-annotated-type', 'type-adapter-config-unused', 'root-model-extra', 'unevaluable-type-annotation', 'dataclass-init-false-extra-allow', 'clashing-init-and-init-var', 'model-config-invalid-field-name', 'with-config-on-model', 'dataclass-on-model']`
  <details><summary>`class PydanticExperimentalWarning(Warning)`</summary>
    - `add_note = <method 'add_note' of 'BaseException' objects>`
    - `args = <attribute 'args' of 'BaseException' objects>`
    - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
  </details>
  <details><summary>`class PydanticImportError(PydanticErrorMixin, ImportError)`</summary>
    <details><summary>`__init__ (self, message: 'str') -> 'None'`</summary>
    </details>
    <details><summary>`__str__ (self) -> 'str'`</summary>
    </details>
    - `add_note = <method 'add_note' of 'BaseException' objects>`
    - `args = <attribute 'args' of 'BaseException' objects>`
    - `msg = <member 'msg' of 'ImportError' objects>`
    - `name = <member 'name' of 'ImportError' objects>`
    - `path = <member 'path' of 'ImportError' objects>`
    - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
  </details>
  <details><summary>`class PydanticInvalidForJsonSchema(PydanticUserError)`</summary>
    <details><summary>`__init__ (self, message: 'str') -> 'None'`</summary>
    </details>
    <details><summary>`__str__ (self) -> 'str'`</summary>
    </details>
    - `add_note = <method 'add_note' of 'BaseException' objects>`
    - `args = <attribute 'args' of 'BaseException' objects>`
    - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
  </details>
  <details><summary>`class PydanticSchemaGenerationError(PydanticUserError)`</summary>
    <details><summary>`__init__ (self, message: 'str') -> 'None'`</summary>
    </details>
    <details><summary>`__str__ (self) -> 'str'`</summary>
    </details>
    - `add_note = <method 'add_note' of 'BaseException' objects>`
    - `args = <attribute 'args' of 'BaseException' objects>`
    - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
  </details>
  <details><summary>`class PydanticUndefinedAnnotation(PydanticErrorMixin, NameError)`</summary>
    <details><summary>`__init__ (self, name: 'str', message: 'str') -> 'None'`</summary>
    </details>
    <details><summary>`__str__ (self) -> 'str'`</summary>
    </details>
    - `add_note = <method 'add_note' of 'BaseException' objects>`
    - `args = <attribute 'args' of 'BaseException' objects>`
    <details><summary>`from_name_error (name_error: 'NameError') -> 'Self'`</summary>
    </details>
    - `name = <member 'name' of 'NameError' objects>`
    - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
  </details>
  <details><summary>`class PydanticUserError(PydanticErrorMixin, TypeError)`</summary>
    <details><summary>`__init__ (self, message: 'str', *, code: 'PydanticErrorCodes | None') -> 'None'`</summary>
    </details>
    <details><summary>`__str__ (self) -> 'str'`</summary>
    </details>
    - `add_note = <method 'add_note' of 'BaseException' objects>`
    - `args = <attribute 'args' of 'BaseException' objects>`
    - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
  </details>
  - `RedisDsn = typing.Annotated[pydantic_core._pydantic_core.Url, UrlConstraints(max_length=None, allowed_schemes=['redis', 'rediss'], host_required=None, default_host='localhost', default_port=6379, default_path='/0')]`
  <details><summary>`class RootModel(BaseModel, Generic)`</summary>
    <details><summary>`__class_getitem__ (typevar_values: 'type[Any] | tuple[type[Any], ...]') -> 'type[BaseModel] | _forward_ref.PydanticRecursiveRef'`</summary>
    </details>
    <details><summary>`__copy__ (self) -> 'Self'`</summary>
    </details>
    <details><summary>`__deepcopy__ (self, memo: 'dict[int, Any] | None' = None) -> 'Self'`</summary>
    </details>
    <details><summary>`__delattr__ (self, item: 'str') -> 'Any'`</summary>
    </details>
    <details><summary>`__eq__ (self, other: 'Any') -> 'bool'`</summary>
    </details>
    <details><summary>`__get_pydantic_core_schema__ (source: 'type[BaseModel]', handler: 'GetCoreSchemaHandler', /) -> 'CoreSchema'`</summary>
    </details>
    <details><summary>`__get_pydantic_json_schema__ (core_schema: 'CoreSchema', handler: 'GetJsonSchemaHandler', /) -> 'JsonSchemaValue'`</summary>
    </details>
    <details><summary>`__getattr__ (self, item: 'str') -> 'Any'`</summary>
    </details>
    <details><summary>`__getstate__ (self) -> 'dict[Any, Any]'`</summary>
    </details>
    <details><summary>`__init__ (self, /, root: 'RootModelRootType' = PydanticUndefined, **data) -> 'None'`</summary>
    </details>
    <details><summary>`__init_subclass__ (**kwargs)`</summary>
    </details>
    <details><summary>`__iter__ (self) -> 'TupleGenerator'`</summary>
    </details>
    <details><summary>`__pretty__ (self, fmt: 'typing.Callable[[Any], Any]', **kwargs: 'Any') -> 'typing.Generator[Any, None, None]'`</summary>
    </details>
    <details><summary>`__pydantic_init_subclass__ (**kwargs: 'Any') -> 'None'`</summary>
    </details>
    <details><summary>`__repr__ (self) -> 'str'`</summary>
    </details>
    <details><summary>`__repr_args__ (self) -> '_repr.ReprArgs'`</summary>
    </details>
    <details><summary>`__repr_name__ (self) -> 'str'`</summary>
    </details>
    <details><summary>`__repr_str__ (self, join_str: 'str') -> 'str'`</summary>
    </details>
    <details><summary>`__rich_repr__ (self) -> 'RichReprResult'`</summary>
    </details>
    <details><summary>`__setattr__ (self, name: 'str', value: 'Any') -> 'None'`</summary>
    </details>
    <details><summary>`__setstate__ (self, state: 'dict[Any, Any]') -> 'None'`</summary>
    </details>
    <details><summary>`__str__ (self) -> 'str'`</summary>
    </details>
    <details><summary>`_calculate_keys (self, *args: 'Any', **kwargs: 'Any') -> 'Any'`</summary>
    </details>
    <details><summary>`_check_frozen (self, name: 'str', value: 'Any') -> 'None'`</summary>
    </details>
    <details><summary>`_copy_and_set_values (self, *args: 'Any', **kwargs: 'Any') -> 'Any'`</summary>
    </details>
    <details><summary>`_get_value (*args: 'Any', **kwargs: 'Any') -> 'Any'`</summary>
    </details>
    <details><summary>`_iter (self, *args: 'Any', **kwargs: 'Any') -> 'Any'`</summary>
    </details>
    <details><summary>`construct (_fields_set: 'set[str] | None' = None, **values: 'Any') -> 'Self'`</summary>
    </details>
    <details><summary>`copy (self, *, include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False) -> 'Self'`</summary>
    </details>
    <details><summary>`dict (self, *, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False) -> 'Dict[str, Any]'`</summary>
    </details>
    <details><summary>`from_orm (obj: 'Any') -> 'Self'`</summary>
    </details>
    <details><summary>`json (self, *, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any') -> 'str'`</summary>
    </details>
    - `model_computed_fields = {}`
    - `model_config = {}`
    <details><summary>`model_construct (root: 'RootModelRootType', _fields_set: 'set[str] | None' = None) -> 'Self'`</summary>
    </details>
    <details><summary>`model_copy (self, *, update: 'dict[str, Any] | None' = None, deep: 'bool' = False) -> 'Self'`</summary>
    </details>
    <details><summary>`model_dump (self, *, mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, serialize_as_any: 'bool' = False) -> 'dict[str, Any]'`</summary>
    </details>
    <details><summary>`model_dump_json (self, *, indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, serialize_as_any: 'bool' = False) -> 'str'`</summary>
    </details>
    - `model_extra = <property object at 0x7f13fa443010>`
    - `model_fields = {'root': FieldInfo(annotation=~RootModelRootType, required=True)}`
    - `model_fields_set = <property object at 0x7f13fa443970>`
    <details><summary>`model_json_schema (by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation') -> 'dict[str, Any]'`</summary>
    </details>
    <details><summary>`model_parametrized_name (params: 'tuple[type[Any], ...]') -> 'str'`</summary>
    </details>
    <details><summary>`model_post_init (self, _BaseModel__context: 'Any') -> 'None'`</summary>
    </details>
    <details><summary>`model_rebuild (*, force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'dict[str, Any] | None' = None) -> 'bool | None'`</summary>
    </details>
    <details><summary>`model_validate (obj: 'Any', *, strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None) -> 'Self'`</summary>
    </details>
    <details><summary>`model_validate_json (json_data: 'str | bytes | bytearray', *, strict: 'bool | None' = None, context: 'Any | None' = None) -> 'Self'`</summary>
    </details>
    <details><summary>`model_validate_strings (obj: 'Any', *, strict: 'bool | None' = None, context: 'Any | None' = None) -> 'Self'`</summary>
    </details>
    <details><summary>`parse_file (path: 'str | Path', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'`</summary>
    </details>
    <details><summary>`parse_obj (obj: 'Any') -> 'Self'`</summary>
    </details>
    <details><summary>`parse_raw (b: 'str | bytes', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'`</summary>
    </details>
    <details><summary>`schema (by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}') -> 'Dict[str, Any]'`</summary>
    </details>
    <details><summary>`schema_json (*, by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any') -> 'str'`</summary>
    </details>
    <details><summary>`update_forward_refs (**localns: 'Any') -> 'None'`</summary>
    </details>
    <details><summary>`validate (value: 'Any') -> 'Self'`</summary>
    </details>
  </details>
  <details><summary>`class Secret(_SecretBase)`</summary>
    <details><summary>`__class_getitem__ (params)`</summary>
    </details>
    <details><summary>`__eq__ (self, other: 'Any') -> 'bool'`</summary>
    </details>
    <details><summary>`__get_pydantic_core_schema__ (source: 'type[Any]', handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'`</summary>
    </details>
    <details><summary>`__hash__ (self) -> 'int'`</summary>
    </details>
    <details><summary>`__init__ (self, secret_value: 'SecretType') -> 'None'`</summary>
    </details>
    <details><summary>`__init_subclass__ (*args, **kwargs)`</summary>
    </details>
    <details><summary>`__repr__ (self) -> 'str'`</summary>
    </details>
    <details><summary>`__str__ (self) -> 'str'`</summary>
    </details>
    <details><summary>`_display (self) -> 'str | bytes'`</summary>
    </details>
    <details><summary>`get_secret_value (self) -> 'SecretType'`</summary>
    </details>
  </details>
  <details><summary>`class SecretBytes(_SecretField)`</summary>
    <details><summary>`__class_getitem__ (params)`</summary>
    </details>
    <details><summary>`__eq__ (self, other: 'Any') -> 'bool'`</summary>
    </details>
    <details><summary>`__get_pydantic_core_schema__ (source: 'type[Any]', handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'`</summary>
    </details>
    <details><summary>`__hash__ (self) -> 'int'`</summary>
    </details>
    <details><summary>`__init__ (self, secret_value: 'SecretType') -> 'None'`</summary>
    </details>
    <details><summary>`__init_subclass__ (*args, **kwargs)`</summary>
    </details>
    <details><summary>`__len__ (self) -> 'int'`</summary>
    </details>
    <details><summary>`__repr__ (self) -> 'str'`</summary>
    </details>
    <details><summary>`__str__ (self) -> 'str'`</summary>
    </details>
    <details><summary>`_display (self) -> 'bytes'`</summary>
    </details>
    <details><summary>`get_secret_value (self) -> 'SecretType'`</summary>
    </details>
  </details>
  <details><summary>`class SecretStr(_SecretField)`</summary>
    <details><summary>`__class_getitem__ (params)`</summary>
    </details>
    <details><summary>`__eq__ (self, other: 'Any') -> 'bool'`</summary>
    </details>
    <details><summary>`__get_pydantic_core_schema__ (source: 'type[Any]', handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'`</summary>
    </details>
    <details><summary>`__hash__ (self) -> 'int'`</summary>
    </details>
    <details><summary>`__init__ (self, secret_value: 'SecretType') -> 'None'`</summary>
    </details>
    <details><summary>`__init_subclass__ (*args, **kwargs)`</summary>
    </details>
    <details><summary>`__len__ (self) -> 'int'`</summary>
    </details>
    <details><summary>`__repr__ (self) -> 'str'`</summary>
    </details>
    <details><summary>`__str__ (self) -> 'str'`</summary>
    </details>
    <details><summary>`_display (self) -> 'str'`</summary>
    </details>
    <details><summary>`get_secret_value (self) -> 'SecretType'`</summary>
    </details>
  </details>
  <details><summary>`class SerializationInfo(Protocol)`</summary>
    <details><summary>`__class_getitem__ (params)`</summary>
    </details>
    <details><summary>`__init__ (self, *args, **kwargs)`</summary>
    </details>
    <details><summary>`__init_subclass__ (*args, **kwargs)`</summary>
    </details>
    <details><summary>`__repr__ (self) -> 'str'`</summary>
    </details>
    <details><summary>`__str__ (self) -> 'str'`</summary>
    </details>
    <details><summary>`__subclasshook__ (other)`</summary>
    </details>
    - `by_alias = <property object at 0x7f13faf32d40>`
    - `context = <property object at 0x7f13faf0c680>`
    - `exclude = <property object at 0x7f13faf07e70>`
    - `exclude_defaults = <property object at 0x7f13faf32e30>`
    - `exclude_none = <property object at 0x7f13faf32e80>`
    - `exclude_unset = <property object at 0x7f13faf32de0>`
    - `include = <property object at 0x7f13fb2918a0>`
    - `mode = <property object at 0x7f13faf32d90>`
    <details><summary>`mode_is_json (self) -> 'bool'`</summary>
    </details>
    <details><summary>`round_trip (self) -> 'bool'`</summary>
    </details>
    - `serialize_as_any = <property object at 0x7f13faf32ed0>`
  </details>
  <details><summary>`class SerializeAsAny(object)`</summary>
    <details><summary>`__class_getitem__ (item: 'Any') -> 'Any'`</summary>
    </details>
    <details><summary>`__eq__ (self, other)`</summary>
    </details>
    <details><summary>`__get_pydantic_core_schema__ (self, source_type: 'Any', handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'`</summary>
    </details>
    <details><summary>`__init__ (self) -> None`</summary>
    </details>
    <details><summary>`__repr__ (self)`</summary>
    </details>
  </details>
  <details><summary>`class SerializerFunctionWrapHandler(Protocol)`</summary>
    <details><summary>`__call__ (self, input_value: 'Any', index_key: 'int | str | None' = None, /) -> 'Any'`</summary>
    </details>
    <details><summary>`__class_getitem__ (params)`</summary>
    </details>
    <details><summary>`__init__ (self, *args, **kwargs)`</summary>
    </details>
    <details><summary>`__init_subclass__ (*args, **kwargs)`</summary>
    </details>
    <details><summary>`__subclasshook__ (other)`</summary>
    </details>
  </details>
  <details><summary>`class SkipValidation(object)`</summary>
    <details><summary>`__class_getitem__ (item: 'Any') -> 'Any'`</summary>
    </details>
    <details><summary>`__eq__ (self, other)`</summary>
    </details>
    <details><summary>`__get_pydantic_core_schema__ (source: 'Any', handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'`</summary>
    </details>
    <details><summary>`__init__ (self) -> None`</summary>
    </details>
    <details><summary>`__repr__ (self)`</summary>
    </details>
  </details>
  - `SnowflakeDsn = typing.Annotated[pydantic_core._pydantic_core.Url, UrlConstraints(max_length=None, allowed_schemes=['snowflake'], host_required=True, default_host=None, default_port=None, default_path=None)]`
  <details><summary>`class Strict(PydanticMetadata, BaseMetadata)`</summary>
    <details><summary>`__eq__ (self, other)`</summary>
    </details>
    <details><summary>`__hash__ (self) -> 'int'`</summary>
    </details>
    <details><summary>`__init__ (self, strict: 'bool' = True) -> None`</summary>
    </details>
    <details><summary>`__pretty__ (self, fmt: 'typing.Callable[[Any], Any]', **kwargs: 'Any') -> 'typing.Generator[Any, None, None]'`</summary>
    </details>
    <details><summary>`__repr__ (self)`</summary>
    </details>
    <details><summary>`__repr_args__ (self) -> 'ReprArgs'`</summary>
    </details>
    <details><summary>`__repr_name__ (self) -> 'str'`</summary>
    </details>
    <details><summary>`__repr_str__ (self, join_str: 'str') -> 'str'`</summary>
    </details>
    <details><summary>`__rich_repr__ (self) -> 'RichReprResult'`</summary>
    </details>
    <details><summary>`__str__ (self) -> 'str'`</summary>
    </details>
    - `strict = True`
  </details>
  - `StrictBool = typing.Annotated[bool, Strict(strict=True)]`
  - `StrictBytes = typing.Annotated[bytes, Strict(strict=True)]`
  - `StrictFloat = typing.Annotated[float, Strict(strict=True)]`
  - `StrictInt = typing.Annotated[int, Strict(strict=True)]`
  - `StrictStr = typing.Annotated[str, Strict(strict=True)]`
  <details><summary>`class StringConstraints(GroupedMetadata)`</summary>
    <details><summary>`__class_getitem__ (params)`</summary>
    </details>
    <details><summary>`__delattr__ (self, name)`</summary>
    </details>
    <details><summary>`__eq__ (self, other)`</summary>
    </details>
    <details><summary>`__hash__ (self)`</summary>
    </details>
    <details><summary>`__init__ (self, strip_whitespace: 'bool | None' = None, to_upper: 'bool | None' = None, to_lower: 'bool | None' = None, strict: 'bool | None' = None, min_length: 'int | None' = None, max_length: 'int | None' = None, pattern: 'str | Pattern[str] | None' = None) -> None`</summary>
    </details>
    <details><summary>`__init_subclass__ (*args: Any, **kwargs: Any) -> None`</summary>
    </details>
    <details><summary>`__iter__ (self) -> 'Iterator[BaseMetadata]'`</summary>
    </details>
    <details><summary>`__repr__ (self)`</summary>
    </details>
    <details><summary>`__setattr__ (self, name, value)`</summary>
    </details>
    <details><summary>`__subclasshook__ (other)`</summary>
    </details>
    - `max_length = None`
    - `min_length = None`
    - `pattern = None`
    - `strict = None`
    - `strip_whitespace = None`
    - `to_lower = None`
    - `to_upper = None`
  </details>
  <details><summary>`class Tag(object)`</summary>
    <details><summary>`__delattr__ (self, name)`</summary>
    </details>
    <details><summary>`__eq__ (self, other)`</summary>
    </details>
    <details><summary>`__get_pydantic_core_schema__ (self, source_type: 'Any', handler: 'GetCoreSchemaHandler') -> 'CoreSchema'`</summary>
    </details>
    <details><summary>`__getstate__ (self)`</summary>
    </details>
    <details><summary>`__hash__ (self)`</summary>
    </details>
    <details><summary>`__init__ (self, tag: 'str') -> None`</summary>
    </details>
    <details><summary>`__repr__ (self)`</summary>
    </details>
    <details><summary>`__setattr__ (self, name, value)`</summary>
    </details>
    <details><summary>`__setstate__ (self, state)`</summary>
    </details>
    - `tag = <member 'tag' of 'Tag' objects>`
  </details>
  <details><summary>`class TypeAdapter(Generic)`</summary>
    <details><summary>`__class_getitem__ (params)`</summary>
    </details>
    <details><summary>`__init__ (self, type: 'Any', *, config: 'ConfigDict | None' = None, _parent_depth: 'int' = 2, module: 'str | None' = None) -> 'None'`</summary>
    </details>
    <details><summary>`__init_subclass__ (*args, **kwargs)`</summary>
    </details>
    <details><summary>`_defer_build (self) -> 'bool'`</summary>
    </details>
    <details><summary>`_init_core_attrs (self, rebuild_mocks: 'bool') -> 'None'`</summary>
    </details>
    <details><summary>`_is_defer_build_config (config: 'ConfigDict') -> 'bool'`</summary>
    </details>
    <details><summary>`_model_config (self) -> 'ConfigDict | None'`</summary>
    </details>
    <details><summary>`_with_frame_depth (self, depth: 'int') -> 'Iterator[None]'`</summary>
    </details>
    - `core_schema = <functools.cached_property object at 0x7f13fa50d2d0>`
    <details><summary>`dump_json (self, instance: 'T', /, *, indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, serialize_as_any: 'bool' = False, context: 'dict[str, Any] | None' = None) -> 'bytes'`</summary>
    </details>
    <details><summary>`dump_python (self, instance: 'T', /, *, mode: "Literal['json', 'python']" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, serialize_as_any: 'bool' = False, context: 'dict[str, Any] | None' = None) -> 'Any'`</summary>
    </details>
    <details><summary>`get_default_value (self, *, strict: 'bool | None' = None, context: 'dict[str, Any] | None' = None) -> 'Some[T] | None'`</summary>
    </details>
    <details><summary>`json_schema (self, *, by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation') -> 'dict[str, Any]'`</summary>
    </details>
    <details><summary>`json_schemas (inputs: 'Iterable[tuple[JsonSchemaKeyT, JsonSchemaMode, TypeAdapter[Any]]]', /, *, by_alias: 'bool' = True, title: 'str | None' = None, description: 'str | None' = None, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>) -> 'tuple[dict[tuple[JsonSchemaKeyT, JsonSchemaMode], JsonSchemaValue], JsonSchemaValue]'`</summary>
    </details>
    - `serializer = <functools.cached_property object at 0x7f13fa50e190>`
    <details><summary>`validate_json (self, data: 'str | bytes', /, *, strict: 'bool | None' = None, context: 'dict[str, Any] | None' = None) -> 'T'`</summary>
    </details>
    <details><summary>`validate_python (self, object: 'Any', /, *, strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'dict[str, Any] | None' = None) -> 'T'`</summary>
    </details>
    <details><summary>`validate_strings (self, obj: 'Any', /, *, strict: 'bool | None' = None, context: 'dict[str, Any] | None' = None) -> 'T'`</summary>
    </details>
    - `validator = <functools.cached_property object at 0x7f13fa50e150>`
  </details>
  - `UUID1 = typing.Annotated[uuid.UUID, UuidVersion(uuid_version=1)]`
  - `UUID3 = typing.Annotated[uuid.UUID, UuidVersion(uuid_version=3)]`
  - `UUID4 = typing.Annotated[uuid.UUID, UuidVersion(uuid_version=4)]`
  - `UUID5 = typing.Annotated[uuid.UUID, UuidVersion(uuid_version=5)]`
  <details><summary>`class UrlConstraints(PydanticMetadata)`</summary>
    <details><summary>`__eq__ (self, other)`</summary>
    </details>
    <details><summary>`__hash__ (self) -> 'int'`</summary>
    </details>
    <details><summary>`__init__ (self, max_length: 'int | None' = None, allowed_schemes: 'list[str] | None' = None, host_required: 'bool | None' = None, default_host: 'str | None' = None, default_port: 'int | None' = None, default_path: 'str | None' = None) -> None`</summary>
    </details>
    <details><summary>`__pretty__ (self, fmt: 'typing.Callable[[Any], Any]', **kwargs: 'Any') -> 'typing.Generator[Any, None, None]'`</summary>
    </details>
    <details><summary>`__repr__ (self)`</summary>
    </details>
    <details><summary>`__repr_args__ (self) -> 'ReprArgs'`</summary>
    </details>
    <details><summary>`__repr_name__ (self) -> 'str'`</summary>
    </details>
    <details><summary>`__repr_str__ (self, join_str: 'str') -> 'str'`</summary>
    </details>
    <details><summary>`__rich_repr__ (self) -> 'RichReprResult'`</summary>
    </details>
    <details><summary>`__str__ (self) -> 'str'`</summary>
    </details>
    - `allowed_schemes = None`
    - `default_host = None`
    - `default_path = None`
    - `default_port = None`
    - `host_required = None`
    - `max_length = None`
  </details>
  - `VERSION = '2.9.2'`
  <details><summary>`class ValidationError(ValueError)`</summary>
    - `add_note = <method 'add_note' of 'BaseException' objects>`
    - `args = <attribute 'args' of 'BaseException' objects>`
    - `error_count = <method 'error_count' of 'pydantic_core._pydantic_core.ValidationError' objects>`
    - `errors = <method 'errors' of 'pydantic_core._pydantic_core.ValidationError' objects>`
    - `from_exception_data = <built-in method from_exception_data of type object at 0x55fa9ac46190>`
    - `json = <method 'json' of 'pydantic_core._pydantic_core.ValidationError' objects>`
    - `title = <attribute 'title' of 'pydantic_core._pydantic_core.ValidationError' objects>`
    - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
  </details>
  <details><summary>`class ValidationInfo(Protocol)`</summary>
    <details><summary>`__class_getitem__ (params)`</summary>
    </details>
    <details><summary>`__init__ (self, *args, **kwargs)`</summary>
    </details>
    <details><summary>`__init_subclass__ (*args, **kwargs)`</summary>
    </details>
    <details><summary>`__subclasshook__ (other)`</summary>
    </details>
    - `config = <property object at 0x7f13faf330b0>`
    - `context = <property object at 0x7f13faf33060>`
    - `data = <property object at 0x7f13faf33150>`
    - `field_name = <property object at 0x7f13faf331a0>`
    - `mode = <property object at 0x7f13faf33100>`
  </details>
  <details><summary>`class ValidatorFunctionWrapHandler(Protocol)`</summary>
    <details><summary>`__call__ (self, input_value: 'Any', outer_location: 'str | int | None' = None, /) -> 'Any'`</summary>
    </details>
    <details><summary>`__class_getitem__ (params)`</summary>
    </details>
    <details><summary>`__init__ (self, *args, **kwargs)`</summary>
    </details>
    <details><summary>`__init_subclass__ (*args, **kwargs)`</summary>
    </details>
    <details><summary>`__subclasshook__ (other)`</summary>
    </details>
  </details>
  - `WebsocketUrl = typing.Annotated[pydantic_core._pydantic_core.Url, UrlConstraints(max_length=2083, allowed_schemes=['ws', 'wss'], host_required=None, default_host=None, default_port=None, default_path=None)]`
  <details><summary>`class WithJsonSchema(object)`</summary>
    <details><summary>`__eq__ (self, other)`</summary>
    </details>
    <details><summary>`__get_pydantic_json_schema__ (self, core_schema: 'core_schema.CoreSchema', handler: 'GetJsonSchemaHandler') -> 'JsonSchemaValue'`</summary>
    </details>
    <details><summary>`__hash__ (self) -> 'int'`</summary>
    </details>
    <details><summary>`__init__ (self, json_schema: 'JsonSchemaValue | None', mode: "Literal['validation', 'serialization'] | None" = None) -> None`</summary>
    </details>
    <details><summary>`__repr__ (self)`</summary>
    </details>
    - `json_schema = <member 'json_schema' of 'WithJsonSchema' objects>`
    - `mode = <member 'mode' of 'WithJsonSchema' objects>`
  </details>
  <details><summary>`class WrapSerializer(object)`</summary>
    <details><summary>`__delattr__ (self, name)`</summary>
    </details>
    <details><summary>`__eq__ (self, other)`</summary>
    </details>
    <details><summary>`__get_pydantic_core_schema__ (self, source_type: 'Any', handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'`</summary>
    </details>
    <details><summary>`__getstate__ (self)`</summary>
    </details>
    <details><summary>`__hash__ (self)`</summary>
    </details>
    <details><summary>`__init__ (self, func: 'core_schema.WrapSerializerFunction', return_type: 'Any' = PydanticUndefined, when_used: 'WhenUsed' = 'always') -> None`</summary>
    </details>
    <details><summary>`__repr__ (self)`</summary>
    </details>
    <details><summary>`__setattr__ (self, name, value)`</summary>
    </details>
    <details><summary>`__setstate__ (self, state)`</summary>
    </details>
    - `func = <member 'func' of 'WrapSerializer' objects>`
    - `return_type = <member 'return_type' of 'WrapSerializer' objects>`
    - `when_used = <member 'when_used' of 'WrapSerializer' objects>`
  </details>
  <details><summary>`class WrapValidator(object)`</summary>
    <details><summary>`__delattr__ (self, name)`</summary>
    </details>
    <details><summary>`__eq__ (self, other)`</summary>
    </details>
    <details><summary>`__get_pydantic_core_schema__ (self, source_type: 'Any', handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'`</summary>
    </details>
    <details><summary>`__getstate__ (self)`</summary>
    </details>
    <details><summary>`__hash__ (self)`</summary>
    </details>
    <details><summary>`__init__ (self, func: 'core_schema.NoInfoWrapValidatorFunction | core_schema.WithInfoWrapValidatorFunction', json_schema_input_type: 'Any' = PydanticUndefined) -> None`</summary>
    </details>
    <details><summary>`__repr__ (self)`</summary>
    </details>
    <details><summary>`__setattr__ (self, name, value)`</summary>
    </details>
    <details><summary>`__setstate__ (self, state)`</summary>
    </details>
    <details><summary>`_from_decorator (decorator: '_decorators.Decorator[_decorators.FieldValidatorDecoratorInfo]') -> 'Self'`</summary>
    </details>
    - `func = <member 'func' of 'WrapValidator' objects>`
    - `json_schema_input_type = <member 'json_schema_input_type' of 'WrapValidator' objects>`
  </details>
  <details><summary>`computed_field (func: 'PropertyT | None' = None, /, *, alias: 'str | None' = None, alias_priority: 'int | None' = None, title: 'str | None' = None, field_title_generator: 'typing.Callable[[str, ComputedFieldInfo], str] | None' = None, description: 'str | None' = None, deprecated: 'Deprecated | str | bool | None' = None, examples: 'list[Any] | None' = None, json_schema_extra: 'JsonDict | typing.Callable[[JsonDict], None] | None' = None, repr: 'bool | None' = None, return_type: 'Any' = PydanticUndefined) -> 'PropertyT | typing.Callable[[PropertyT], PropertyT]'`</summary>
  </details>
  <details><summary>`conbytes (*, min_length: 'int | None' = None, max_length: 'int | None' = None, strict: 'bool | None' = None) -> 'type[bytes]'`</summary>
  </details>
  <details><summary>`condate (*, strict: 'bool | None' = None, gt: 'date | None' = None, ge: 'date | None' = None, lt: 'date | None' = None, le: 'date | None' = None) -> 'type[date]'`</summary>
  </details>
  <details><summary>`condecimal (*, strict: 'bool | None' = None, gt: 'int | Decimal | None' = None, ge: 'int | Decimal | None' = None, lt: 'int | Decimal | None' = None, le: 'int | Decimal | None' = None, multiple_of: 'int | Decimal | None' = None, max_digits: 'int | None' = None, decimal_places: 'int | None' = None, allow_inf_nan: 'bool | None' = None) -> 'type[Decimal]'`</summary>
  </details>
  <details><summary>`confloat (*, strict: 'bool | None' = None, gt: 'float | None' = None, ge: 'float | None' = None, lt: 'float | None' = None, le: 'float | None' = None, multiple_of: 'float | None' = None, allow_inf_nan: 'bool | None' = None) -> 'type[float]'`</summary>
  </details>
  <details><summary>`confrozenset (item_type: 'type[HashableItemType]', *, min_length: 'int | None' = None, max_length: 'int | None' = None) -> 'type[frozenset[HashableItemType]]'`</summary>
  </details>
  <details><summary>`conint (*, strict: 'bool | None' = None, gt: 'int | None' = None, ge: 'int | None' = None, lt: 'int | None' = None, le: 'int | None' = None, multiple_of: 'int | None' = None) -> 'type[int]'`</summary>
  </details>
  <details><summary>`conlist (item_type: 'type[AnyItemType]', *, min_length: 'int | None' = None, max_length: 'int | None' = None, unique_items: 'bool | None' = None) -> 'type[list[AnyItemType]]'`</summary>
  </details>
  <details><summary>`conset (item_type: 'type[HashableItemType]', *, min_length: 'int | None' = None, max_length: 'int | None' = None) -> 'type[set[HashableItemType]]'`</summary>
  </details>
  <details><summary>`constr (*, strip_whitespace: 'bool | None' = None, to_upper: 'bool | None' = None, to_lower: 'bool | None' = None, strict: 'bool | None' = None, min_length: 'int | None' = None, max_length: 'int | None' = None, pattern: 'str | Pattern[str] | None' = None) -> 'type[str]'`</summary>
  </details>
  <details><summary>`create_model (model_name: 'str', /, *, __config__: 'ConfigDict | None' = None, __doc__: 'str | None' = None, __base__: 'type[ModelT] | tuple[type[ModelT], ...] | None' = None, __module__: 'str | None' = None, __validators__: 'dict[str, Callable[..., Any]] | None' = None, __cls_kwargs__: 'dict[str, Any] | None' = None, __slots__: 'tuple[str, ...] | None' = None, **field_definitions: 'Any') -> 'type[ModelT]'`</summary>
  </details>
  <details><summary>`pydantic.dataclasses`</summary>
    <details><summary>`class Any(object)`</summary>
      <details><summary>`__new__ (cls, *args, **kwargs)`</summary>
      </details>
    </details>
    - `Callable = typing.Callable`
    <details><summary>`class ConfigDict(dict)`</summary>
      - `clear = <method 'clear' of 'dict' objects>`
      - `copy = <method 'copy' of 'dict' objects>`
      - `fromkeys = <built-in method fromkeys of _TypedDictMeta object at 0x55fa9ad0ccf0>`
      - `get = <method 'get' of 'dict' objects>`
      - `items = <method 'items' of 'dict' objects>`
      - `keys = <method 'keys' of 'dict' objects>`
      - `pop = <method 'pop' of 'dict' objects>`
      - `popitem = <method 'popitem' of 'dict' objects>`
      - `setdefault = <method 'setdefault' of 'dict' objects>`
      - `update = <method 'update' of 'dict' objects>`
      - `values = <method 'values' of 'dict' objects>`
    </details>
    <details><summary>`Field (default: 'Any' = PydanticUndefined, *, default_factory: 'typing.Callable[[], Any] | None' = PydanticUndefined, alias: 'str | None' = PydanticUndefined, alias_priority: 'int | None' = PydanticUndefined, validation_alias: 'str | AliasPath | AliasChoices | None' = PydanticUndefined, serialization_alias: 'str | None' = PydanticUndefined, title: 'str | None' = PydanticUndefined, field_title_generator: 'typing_extensions.Callable[[str, FieldInfo], str] | None' = PydanticUndefined, description: 'str | None' = PydanticUndefined, examples: 'list[Any] | None' = PydanticUndefined, exclude: 'bool | None' = PydanticUndefined, discriminator: 'str | types.Discriminator | None' = PydanticUndefined, deprecated: 'Deprecated | str | bool | None' = PydanticUndefined, json_schema_extra: 'JsonDict | typing.Callable[[JsonDict], None] | None' = PydanticUndefined, frozen: 'bool | None' = PydanticUndefined, validate_default: 'bool | None' = PydanticUndefined, repr: 'bool' = PydanticUndefined, init: 'bool | None' = PydanticUndefined, init_var: 'bool | None' = PydanticUndefined, kw_only: 'bool | None' = PydanticUndefined, pattern: 'str | typing.Pattern[str] | None' = PydanticUndefined, strict: 'bool | None' = PydanticUndefined, coerce_numbers_to_str: 'bool | None' = PydanticUndefined, gt: 'annotated_types.SupportsGt | None' = PydanticUndefined, ge: 'annotated_types.SupportsGe | None' = PydanticUndefined, lt: 'annotated_types.SupportsLt | None' = PydanticUndefined, le: 'annotated_types.SupportsLe | None' = PydanticUndefined, multiple_of: 'float | None' = PydanticUndefined, allow_inf_nan: 'bool | None' = PydanticUndefined, max_digits: 'int | None' = PydanticUndefined, decimal_places: 'int | None' = PydanticUndefined, min_length: 'int | None' = PydanticUndefined, max_length: 'int | None' = PydanticUndefined, union_mode: "Literal['smart', 'left_to_right']" = PydanticUndefined, fail_fast: 'bool | None' = PydanticUndefined, **extra: 'Unpack[_EmptyKwargs]') -> 'Any'`</summary>
    </details>
    <details><summary>`class FieldInfo(Representation)`</summary>
      <details><summary>`__init__ (self, **kwargs: 'Unpack[_FieldInfoInputs]') -> 'None'`</summary>
      </details>
      <details><summary>`__pretty__ (self, fmt: 'typing.Callable[[Any], Any]', **kwargs: 'Any') -> 'typing.Generator[Any, None, None]'`</summary>
      </details>
      <details><summary>`__repr__ (self) -> 'str'`</summary>
      </details>
      <details><summary>`__repr_args__ (self) -> 'ReprArgs'`</summary>
      </details>
      <details><summary>`__repr_name__ (self) -> 'str'`</summary>
      </details>
      <details><summary>`__repr_str__ (self, join_str: 'str') -> 'str'`</summary>
      </details>
      <details><summary>`__rich_repr__ (self) -> 'RichReprResult'`</summary>
      </details>
      <details><summary>`__str__ (self) -> 'str'`</summary>
      </details>
      <details><summary>`_collect_metadata (kwargs: 'dict[str, Any]') -> 'list[Any]'`</summary>
      </details>
      <details><summary>`_extract_metadata (annotation: 'type[Any] | None') -> 'tuple[type[Any] | None, list[Any]]'`</summary>
      </details>
      <details><summary>`_from_dataclass_field (dc_field: 'DataclassField[Any]') -> 'FieldInfo'`</summary>
      </details>
      - `alias = <member 'alias' of 'FieldInfo' objects>`
      - `alias_priority = <member 'alias_priority' of 'FieldInfo' objects>`
      - `annotation = <member 'annotation' of 'FieldInfo' objects>`
      <details><summary>`apply_typevars_map (self, typevars_map: 'dict[Any, Any] | None', types_namespace: 'dict[str, Any] | None') -> 'None'`</summary>
      </details>
      - `default = <member 'default' of 'FieldInfo' objects>`
      - `default_factory = <member 'default_factory' of 'FieldInfo' objects>`
      - `deprecated = <member 'deprecated' of 'FieldInfo' objects>`
      - `deprecation_message = <property object at 0x7f13fa4d53a0>`
      - `description = <member 'description' of 'FieldInfo' objects>`
      - `discriminator = <member 'discriminator' of 'FieldInfo' objects>`
      - `examples = <member 'examples' of 'FieldInfo' objects>`
      - `exclude = <member 'exclude' of 'FieldInfo' objects>`
      - `field_title_generator = <member 'field_title_generator' of 'FieldInfo' objects>`
      <details><summary>`from_annotated_attribute (annotation: 'type[Any]', default: 'Any') -> 'FieldInfo'`</summary>
      </details>
      <details><summary>`from_annotation (annotation: 'type[Any]') -> 'FieldInfo'`</summary>
      </details>
      <details><summary>`from_field (default: 'Any' = PydanticUndefined, **kwargs: 'Unpack[_FromFieldInfoInputs]') -> 'FieldInfo'`</summary>
      </details>
      - `frozen = <member 'frozen' of 'FieldInfo' objects>`
      <details><summary>`get_default (self, *, call_default_factory: 'bool' = False) -> 'Any'`</summary>
      </details>
      - `init = <member 'init' of 'FieldInfo' objects>`
      - `init_var = <member 'init_var' of 'FieldInfo' objects>`
      <details><summary>`is_required (self) -> 'bool'`</summary>
      </details>
      - `json_schema_extra = <member 'json_schema_extra' of 'FieldInfo' objects>`
      - `kw_only = <member 'kw_only' of 'FieldInfo' objects>`
      <details><summary>`merge_field_infos (*field_infos: 'FieldInfo', **overrides: 'Any') -> 'FieldInfo'`</summary>
      </details>
      - `metadata = <member 'metadata' of 'FieldInfo' objects>`
      - `metadata_lookup = {'strict': <class 'pydantic.types.Strict'>, 'gt': <class 'annotated_types.Gt'>, 'ge': <class 'annotated_types.Ge'>, 'lt': <class 'annotated_types.Lt'>, 'le': <class 'annotated_types.Le'>, 'multiple_of': <class 'annotated_types.MultipleOf'>, 'min_length': <class 'annotated_types.MinLen'>, 'max_length': <class 'annotated_types.MaxLen'>, 'pattern': None, 'allow_inf_nan': None, 'max_digits': None, 'decimal_places': None, 'union_mode': None, 'coerce_numbers_to_str': None, 'fail_fast': <class 'pydantic.types.FailFast'>}`
      <details><summary>`rebuild_annotation (self) -> 'Any'`</summary>
      </details>
      - `repr = <member 'repr' of 'FieldInfo' objects>`
      - `serialization_alias = <member 'serialization_alias' of 'FieldInfo' objects>`
      - `title = <member 'title' of 'FieldInfo' objects>`
      - `validate_default = <member 'validate_default' of 'FieldInfo' objects>`
      - `validation_alias = <member 'validation_alias' of 'FieldInfo' objects>`
    </details>
    <details><summary>`class Generic(object)`</summary>
      <details><summary>`__class_getitem__ (params)`</summary>
      </details>
      <details><summary>`__init_subclass__ (*args, **kwargs)`</summary>
      </details>
    </details>
    - `Literal = typing.Literal`
    - `NoReturn = typing.NoReturn`
    <details><summary>`PrivateAttr (default: 'Any' = PydanticUndefined, *, default_factory: 'typing.Callable[[], Any] | None' = None, init: 'Literal[False]' = False) -> 'Any'`</summary>
    </details>
    <details><summary>`class PydanticUserError(PydanticErrorMixin, TypeError)`</summary>
      <details><summary>`__init__ (self, message: 'str', *, code: 'PydanticErrorCodes | None') -> 'None'`</summary>
      </details>
      <details><summary>`__str__ (self) -> 'str'`</summary>
      </details>
      - `add_note = <method 'add_note' of 'BaseException' objects>`
      - `args = <attribute 'args' of 'BaseException' objects>`
      - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
    </details>
    - `TYPE_CHECKING = False`
    - `TypeGuard = typing.TypeGuard`
    <details><summary>`class TypeVar(_Final, _Immutable, _BoundVarianceMixin, _PickleUsingNameMixin)`</summary>
      <details><summary>`__copy__ (self)`</summary>
      </details>
      <details><summary>`__deepcopy__ (self, memo)`</summary>
      </details>
      <details><summary>`__init__ (self, name, *constraints, bound=None, covariant=False, contravariant=False)`</summary>
      </details>
      <details><summary>`__init_subclass__ (*args, **kwds)`</summary>
      </details>
      <details><summary>`__or__ (self, right)`</summary>
      </details>
      <details><summary>`__reduce__ (self)`</summary>
      </details>
      <details><summary>`__repr__ (self)`</summary>
      </details>
      <details><summary>`__ror__ (self, left)`</summary>
      </details>
      <details><summary>`__typing_subst__ (self, arg)`</summary>
      </details>
    </details>
    <details><summary>`dataclass (_cls: 'type[_T] | None' = None, *, init: 'Literal[False]' = False, repr: 'bool' = True, eq: 'bool' = True, order: 'bool' = False, unsafe_hash: 'bool' = False, frozen: 'bool | None' = None, config: 'ConfigDict | type[object] | None' = None, validate_on_init: 'bool | None' = None, kw_only: 'bool' = False, slots: 'bool' = False) -> 'Callable[[type[_T]], type[PydanticDataclass]] | type[PydanticDataclass]'`</summary>
    </details>
    <details><summary>`dataclass_transform (*, eq_default: bool = True, order_default: bool = False, kw_only_default: bool = False, frozen_default: bool = False, field_specifiers: Tuple[Union[Type[Any], Callable[..., Any]], ...] = (), **kwargs: Any) -> Callable[[~T], ~T]`</summary>
    </details>
    <details><summary>`dataclasses`</summary>
      <details><summary>`class Field(object)`</summary>
        - `__class_getitem__ <signature unavailable>`
        <details><summary>`__init__ (self, default, default_factory, init, repr, hash, compare, metadata, kw_only)`</summary>
        </details>
        <details><summary>`__repr__ (self)`</summary>
        </details>
        <details><summary>`__set_name__ (self, owner, name)`</summary>
        </details>
        - `compare = <member 'compare' of 'Field' objects>`
        - `default = <member 'default' of 'Field' objects>`
        - `default_factory = <member 'default_factory' of 'Field' objects>`
        - `hash = <member 'hash' of 'Field' objects>`
        - `init = <member 'init' of 'Field' objects>`
        - `kw_only = <member 'kw_only' of 'Field' objects>`
        - `metadata = <member 'metadata' of 'Field' objects>`
        - `name = <member 'name' of 'Field' objects>`
        - `repr = <member 'repr' of 'Field' objects>`
        - `type = <member 'type' of 'Field' objects>`
      </details>
      <details><summary>`class FrozenInstanceError(AttributeError)`</summary>
        - `add_note = <method 'add_note' of 'BaseException' objects>`
        - `args = <attribute 'args' of 'BaseException' objects>`
        - `name = <member 'name' of 'AttributeError' objects>`
        - `obj = <member 'obj' of 'AttributeError' objects>`
        - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
      </details>
      <details><summary>`class function(object)`</summary>
      </details>
      <details><summary>`class GenericAlias(object)`</summary>
      </details>
      <details><summary>`class InitVar(object)`</summary>
        <details><summary>`__class_getitem__ (type)`</summary>
        </details>
        <details><summary>`__init__ (self, type)`</summary>
        </details>
        <details><summary>`__repr__ (self)`</summary>
        </details>
        - `type = <member 'type' of 'InitVar' objects>`
      </details>
      - `KW_ONLY = <dataclasses._KW_ONLY_TYPE object at 0x7f13faebaa10>`
      - `MISSING = <dataclasses._MISSING_TYPE object at 0x7f13faeba050>`
      <details><summary>`abc`</summary>
        <details><summary>`class ABC(object)`</summary>
        </details>
        <details><summary>`class ABCMeta(type)`</summary>
          <details><summary>`__instancecheck__ (cls, instance)`</summary>
          </details>
          <details><summary>`__new__ (mcls, name, bases, namespace, /, **kwargs)`</summary>
          </details>
          <details><summary>`__subclasscheck__ (cls, subclass)`</summary>
          </details>
          <details><summary>`_abc_caches_clear (cls)`</summary>
          </details>
          <details><summary>`_abc_registry_clear (cls)`</summary>
          </details>
          <details><summary>`_dump_registry (cls, file=None)`</summary>
          </details>
          - `mro = <method 'mro' of 'type' objects>`
          <details><summary>`register (cls, subclass)`</summary>
          </details>
        </details>
        <details><summary>`class abstractclassmethod(classmethod)`</summary>
          <details><summary>`__init__ (self, callable)`</summary>
          </details>
        </details>
        <details><summary>`abstractmethod (funcobj)`</summary>
        </details>
        <details><summary>`class abstractproperty(property)`</summary>
          - `deleter = <method 'deleter' of 'property' objects>`
          - `fdel = <member 'fdel' of 'property' objects>`
          - `fget = <member 'fget' of 'property' objects>`
          - `fset = <member 'fset' of 'property' objects>`
          - `getter = <method 'getter' of 'property' objects>`
          - `setter = <method 'setter' of 'property' objects>`
        </details>
        <details><summary>`class abstractstaticmethod(staticmethod)`</summary>
          <details><summary>`__init__ (self, callable)`</summary>
          </details>
        </details>
        - `get_cache_token = <built-in function get_cache_token>`
        <details><summary>`update_abstractmethods (cls)`</summary>
        </details>
      </details>
      <details><summary>`asdict (obj, *, dict_factory=<class 'dict'>)`</summary>
      </details>
      <details><summary>`astuple (obj, *, tuple_factory=<class 'tuple'>)`</summary>
      </details>
      <details><summary>`builtins`</summary>
        <details><summary>`class ArithmeticError(Exception)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class AssertionError(Exception)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class AttributeError(Exception)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `name = <member 'name' of 'AttributeError' objects>`
          - `obj = <member 'obj' of 'AttributeError' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class BaseException(object)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class BaseExceptionGroup(BaseException)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `derive = <method 'derive' of 'BaseExceptionGroup' objects>`
          - `exceptions = <member 'exceptions' of 'BaseExceptionGroup' objects>`
          - `message = <member 'message' of 'BaseExceptionGroup' objects>`
          - `split = <method 'split' of 'BaseExceptionGroup' objects>`
          - `subgroup = <method 'subgroup' of 'BaseExceptionGroup' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class BlockingIOError(OSError)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `characters_written = <attribute 'characters_written' of 'OSError' objects>`
          - `errno = <member 'errno' of 'OSError' objects>`
          - `filename = <member 'filename' of 'OSError' objects>`
          - `filename2 = <member 'filename2' of 'OSError' objects>`
          - `strerror = <member 'strerror' of 'OSError' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class BrokenPipeError(ConnectionError)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `characters_written = <attribute 'characters_written' of 'OSError' objects>`
          - `errno = <member 'errno' of 'OSError' objects>`
          - `filename = <member 'filename' of 'OSError' objects>`
          - `filename2 = <member 'filename2' of 'OSError' objects>`
          - `strerror = <member 'strerror' of 'OSError' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class BufferError(Exception)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class BytesWarning(Warning)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class ChildProcessError(OSError)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `characters_written = <attribute 'characters_written' of 'OSError' objects>`
          - `errno = <member 'errno' of 'OSError' objects>`
          - `filename = <member 'filename' of 'OSError' objects>`
          - `filename2 = <member 'filename2' of 'OSError' objects>`
          - `strerror = <member 'strerror' of 'OSError' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class ConnectionAbortedError(ConnectionError)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `characters_written = <attribute 'characters_written' of 'OSError' objects>`
          - `errno = <member 'errno' of 'OSError' objects>`
          - `filename = <member 'filename' of 'OSError' objects>`
          - `filename2 = <member 'filename2' of 'OSError' objects>`
          - `strerror = <member 'strerror' of 'OSError' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class ConnectionError(OSError)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `characters_written = <attribute 'characters_written' of 'OSError' objects>`
          - `errno = <member 'errno' of 'OSError' objects>`
          - `filename = <member 'filename' of 'OSError' objects>`
          - `filename2 = <member 'filename2' of 'OSError' objects>`
          - `strerror = <member 'strerror' of 'OSError' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class ConnectionRefusedError(ConnectionError)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `characters_written = <attribute 'characters_written' of 'OSError' objects>`
          - `errno = <member 'errno' of 'OSError' objects>`
          - `filename = <member 'filename' of 'OSError' objects>`
          - `filename2 = <member 'filename2' of 'OSError' objects>`
          - `strerror = <member 'strerror' of 'OSError' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class ConnectionResetError(ConnectionError)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `characters_written = <attribute 'characters_written' of 'OSError' objects>`
          - `errno = <member 'errno' of 'OSError' objects>`
          - `filename = <member 'filename' of 'OSError' objects>`
          - `filename2 = <member 'filename2' of 'OSError' objects>`
          - `strerror = <member 'strerror' of 'OSError' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class DeprecationWarning(Warning)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class EOFError(Exception)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        - `Ellipsis = Ellipsis`
        <details><summary>`class EncodingWarning(Warning)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class OSError(Exception)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `characters_written = <attribute 'characters_written' of 'OSError' objects>`
          - `errno = <member 'errno' of 'OSError' objects>`
          - `filename = <member 'filename' of 'OSError' objects>`
          - `filename2 = <member 'filename2' of 'OSError' objects>`
          - `strerror = <member 'strerror' of 'OSError' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class Exception(BaseException)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class ExceptionGroup(BaseExceptionGroup, Exception)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `derive = <method 'derive' of 'BaseExceptionGroup' objects>`
          - `exceptions = <member 'exceptions' of 'BaseExceptionGroup' objects>`
          - `message = <member 'message' of 'BaseExceptionGroup' objects>`
          - `split = <method 'split' of 'BaseExceptionGroup' objects>`
          - `subgroup = <method 'subgroup' of 'BaseExceptionGroup' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        - `False = False`
        <details><summary>`class FileExistsError(OSError)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `characters_written = <attribute 'characters_written' of 'OSError' objects>`
          - `errno = <member 'errno' of 'OSError' objects>`
          - `filename = <member 'filename' of 'OSError' objects>`
          - `filename2 = <member 'filename2' of 'OSError' objects>`
          - `strerror = <member 'strerror' of 'OSError' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class FileNotFoundError(OSError)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `characters_written = <attribute 'characters_written' of 'OSError' objects>`
          - `errno = <member 'errno' of 'OSError' objects>`
          - `filename = <member 'filename' of 'OSError' objects>`
          - `filename2 = <member 'filename2' of 'OSError' objects>`
          - `strerror = <member 'strerror' of 'OSError' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class FloatingPointError(ArithmeticError)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class FutureWarning(Warning)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class GeneratorExit(BaseException)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class OSError(Exception)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `characters_written = <attribute 'characters_written' of 'OSError' objects>`
          - `errno = <member 'errno' of 'OSError' objects>`
          - `filename = <member 'filename' of 'OSError' objects>`
          - `filename2 = <member 'filename2' of 'OSError' objects>`
          - `strerror = <member 'strerror' of 'OSError' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class ImportError(Exception)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `msg = <member 'msg' of 'ImportError' objects>`
          - `name = <member 'name' of 'ImportError' objects>`
          - `path = <member 'path' of 'ImportError' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class ImportWarning(Warning)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class IndentationError(SyntaxError)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `end_lineno = <member 'end_lineno' of 'SyntaxError' objects>`
          - `end_offset = <member 'end_offset' of 'SyntaxError' objects>`
          - `filename = <member 'filename' of 'SyntaxError' objects>`
          - `lineno = <member 'lineno' of 'SyntaxError' objects>`
          - `msg = <member 'msg' of 'SyntaxError' objects>`
          - `offset = <member 'offset' of 'SyntaxError' objects>`
          - `print_file_and_line = <member 'print_file_and_line' of 'SyntaxError' objects>`
          - `text = <member 'text' of 'SyntaxError' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class IndexError(LookupError)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class InterruptedError(OSError)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `characters_written = <attribute 'characters_written' of 'OSError' objects>`
          - `errno = <member 'errno' of 'OSError' objects>`
          - `filename = <member 'filename' of 'OSError' objects>`
          - `filename2 = <member 'filename2' of 'OSError' objects>`
          - `strerror = <member 'strerror' of 'OSError' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class IsADirectoryError(OSError)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `characters_written = <attribute 'characters_written' of 'OSError' objects>`
          - `errno = <member 'errno' of 'OSError' objects>`
          - `filename = <member 'filename' of 'OSError' objects>`
          - `filename2 = <member 'filename2' of 'OSError' objects>`
          - `strerror = <member 'strerror' of 'OSError' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class KeyError(LookupError)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class KeyboardInterrupt(BaseException)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class LookupError(Exception)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class MemoryError(Exception)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class ModuleNotFoundError(ImportError)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `msg = <member 'msg' of 'ImportError' objects>`
          - `name = <member 'name' of 'ImportError' objects>`
          - `path = <member 'path' of 'ImportError' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class NameError(Exception)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `name = <member 'name' of 'NameError' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        - `None = None`
        <details><summary>`class NotADirectoryError(OSError)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `characters_written = <attribute 'characters_written' of 'OSError' objects>`
          - `errno = <member 'errno' of 'OSError' objects>`
          - `filename = <member 'filename' of 'OSError' objects>`
          - `filename2 = <member 'filename2' of 'OSError' objects>`
          - `strerror = <member 'strerror' of 'OSError' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        - `NotImplemented = NotImplemented`
        <details><summary>`class NotImplementedError(RuntimeError)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class OSError(Exception)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `characters_written = <attribute 'characters_written' of 'OSError' objects>`
          - `errno = <member 'errno' of 'OSError' objects>`
          - `filename = <member 'filename' of 'OSError' objects>`
          - `filename2 = <member 'filename2' of 'OSError' objects>`
          - `strerror = <member 'strerror' of 'OSError' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class OverflowError(ArithmeticError)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class PendingDeprecationWarning(Warning)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class PermissionError(OSError)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `characters_written = <attribute 'characters_written' of 'OSError' objects>`
          - `errno = <member 'errno' of 'OSError' objects>`
          - `filename = <member 'filename' of 'OSError' objects>`
          - `filename2 = <member 'filename2' of 'OSError' objects>`
          - `strerror = <member 'strerror' of 'OSError' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class ProcessLookupError(OSError)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `characters_written = <attribute 'characters_written' of 'OSError' objects>`
          - `errno = <member 'errno' of 'OSError' objects>`
          - `filename = <member 'filename' of 'OSError' objects>`
          - `filename2 = <member 'filename2' of 'OSError' objects>`
          - `strerror = <member 'strerror' of 'OSError' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class RecursionError(RuntimeError)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class ReferenceError(Exception)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class ResourceWarning(Warning)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class RuntimeError(Exception)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class RuntimeWarning(Warning)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class StopAsyncIteration(Exception)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class StopIteration(Exception)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `value = <member 'value' of 'StopIteration' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class SyntaxError(Exception)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `end_lineno = <member 'end_lineno' of 'SyntaxError' objects>`
          - `end_offset = <member 'end_offset' of 'SyntaxError' objects>`
          - `filename = <member 'filename' of 'SyntaxError' objects>`
          - `lineno = <member 'lineno' of 'SyntaxError' objects>`
          - `msg = <member 'msg' of 'SyntaxError' objects>`
          - `offset = <member 'offset' of 'SyntaxError' objects>`
          - `print_file_and_line = <member 'print_file_and_line' of 'SyntaxError' objects>`
          - `text = <member 'text' of 'SyntaxError' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class SyntaxWarning(Warning)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class SystemError(Exception)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class SystemExit(BaseException)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `code = <member 'code' of 'SystemExit' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class TabError(IndentationError)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `end_lineno = <member 'end_lineno' of 'SyntaxError' objects>`
          - `end_offset = <member 'end_offset' of 'SyntaxError' objects>`
          - `filename = <member 'filename' of 'SyntaxError' objects>`
          - `lineno = <member 'lineno' of 'SyntaxError' objects>`
          - `msg = <member 'msg' of 'SyntaxError' objects>`
          - `offset = <member 'offset' of 'SyntaxError' objects>`
          - `print_file_and_line = <member 'print_file_and_line' of 'SyntaxError' objects>`
          - `text = <member 'text' of 'SyntaxError' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class TimeoutError(OSError)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `characters_written = <attribute 'characters_written' of 'OSError' objects>`
          - `errno = <member 'errno' of 'OSError' objects>`
          - `filename = <member 'filename' of 'OSError' objects>`
          - `filename2 = <member 'filename2' of 'OSError' objects>`
          - `strerror = <member 'strerror' of 'OSError' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        - `True = True`
        <details><summary>`class TypeError(Exception)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class UnboundLocalError(NameError)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `name = <member 'name' of 'NameError' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class UnicodeDecodeError(UnicodeError)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `encoding = <member 'encoding' of 'UnicodeDecodeError' objects>`
          - `end = <member 'end' of 'UnicodeDecodeError' objects>`
          - `object = <member 'object' of 'UnicodeDecodeError' objects>`
          - `reason = <member 'reason' of 'UnicodeDecodeError' objects>`
          - `start = <member 'start' of 'UnicodeDecodeError' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class UnicodeEncodeError(UnicodeError)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `encoding = <member 'encoding' of 'UnicodeEncodeError' objects>`
          - `end = <member 'end' of 'UnicodeEncodeError' objects>`
          - `object = <member 'object' of 'UnicodeEncodeError' objects>`
          - `reason = <member 'reason' of 'UnicodeEncodeError' objects>`
          - `start = <member 'start' of 'UnicodeEncodeError' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class UnicodeError(ValueError)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class UnicodeTranslateError(UnicodeError)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `encoding = <member 'encoding' of 'UnicodeTranslateError' objects>`
          - `end = <member 'end' of 'UnicodeTranslateError' objects>`
          - `object = <member 'object' of 'UnicodeTranslateError' objects>`
          - `reason = <member 'reason' of 'UnicodeTranslateError' objects>`
          - `start = <member 'start' of 'UnicodeTranslateError' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class UnicodeWarning(Warning)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class UserWarning(Warning)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class ValueError(Exception)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class Warning(Exception)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class ZeroDivisionError(ArithmeticError)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        - `abs = <built-in function abs>`
        - `aiter = <built-in function aiter>`
        - `all = <built-in function all>`
        - `anext = <built-in function anext>`
        - `any = <built-in function any>`
        - `ascii = <built-in function ascii>`
        - `bin = <built-in function bin>`
        <details><summary>`class bool(int)`</summary>
          - `as_integer_ratio = <method 'as_integer_ratio' of 'int' objects>`
          - `bit_count = <method 'bit_count' of 'int' objects>`
          - `bit_length = <method 'bit_length' of 'int' objects>`
          - `conjugate = <method 'conjugate' of 'int' objects>`
          - `denominator = <attribute 'denominator' of 'int' objects>`
          - `from_bytes = <built-in method from_bytes of type object at 0x55fa99f8fae0>`
          - `imag = <attribute 'imag' of 'int' objects>`
          - `numerator = <attribute 'numerator' of 'int' objects>`
          - `real = <attribute 'real' of 'int' objects>`
          - `to_bytes = <method 'to_bytes' of 'int' objects>`
        </details>
        - `breakpoint = <built-in function breakpoint>`
        <details><summary>`class bytearray(object)`</summary>
          - `append = <method 'append' of 'bytearray' objects>`
          - `capitalize = <method 'capitalize' of 'bytearray' objects>`
          - `center = <method 'center' of 'bytearray' objects>`
          - `clear = <method 'clear' of 'bytearray' objects>`
          - `copy = <method 'copy' of 'bytearray' objects>`
          - `count = <method 'count' of 'bytearray' objects>`
          - `decode = <method 'decode' of 'bytearray' objects>`
          - `endswith = <method 'endswith' of 'bytearray' objects>`
          - `expandtabs = <method 'expandtabs' of 'bytearray' objects>`
          - `extend = <method 'extend' of 'bytearray' objects>`
          - `find = <method 'find' of 'bytearray' objects>`
          - `fromhex = <built-in method fromhex of type object at 0x55fa99f8f7c0>`
          - `hex = <method 'hex' of 'bytearray' objects>`
          - `index = <method 'index' of 'bytearray' objects>`
          - `insert = <method 'insert' of 'bytearray' objects>`
          - `isalnum = <method 'isalnum' of 'bytearray' objects>`
          - `isalpha = <method 'isalpha' of 'bytearray' objects>`
          - `isascii = <method 'isascii' of 'bytearray' objects>`
          - `isdigit = <method 'isdigit' of 'bytearray' objects>`
          - `islower = <method 'islower' of 'bytearray' objects>`
          - `isspace = <method 'isspace' of 'bytearray' objects>`
          - `istitle = <method 'istitle' of 'bytearray' objects>`
          - `isupper = <method 'isupper' of 'bytearray' objects>`
          - `join = <method 'join' of 'bytearray' objects>`
          - `ljust = <method 'ljust' of 'bytearray' objects>`
          - `lower = <method 'lower' of 'bytearray' objects>`
          - `lstrip = <method 'lstrip' of 'bytearray' objects>`
          - `maketrans = <built-in method maketrans of type object at 0x55fa99f8f7c0>`
          - `partition = <method 'partition' of 'bytearray' objects>`
          - `pop = <method 'pop' of 'bytearray' objects>`
          - `remove = <method 'remove' of 'bytearray' objects>`
          - `removeprefix = <method 'removeprefix' of 'bytearray' objects>`
          - `removesuffix = <method 'removesuffix' of 'bytearray' objects>`
          - `replace = <method 'replace' of 'bytearray' objects>`
          - `reverse = <method 'reverse' of 'bytearray' objects>`
          - `rfind = <method 'rfind' of 'bytearray' objects>`
          - `rindex = <method 'rindex' of 'bytearray' objects>`
          - `rjust = <method 'rjust' of 'bytearray' objects>`
          - `rpartition = <method 'rpartition' of 'bytearray' objects>`
          - `rsplit = <method 'rsplit' of 'bytearray' objects>`
          - `rstrip = <method 'rstrip' of 'bytearray' objects>`
          - `split = <method 'split' of 'bytearray' objects>`
          - `splitlines = <method 'splitlines' of 'bytearray' objects>`
          - `startswith = <method 'startswith' of 'bytearray' objects>`
          - `strip = <method 'strip' of 'bytearray' objects>`
          - `swapcase = <method 'swapcase' of 'bytearray' objects>`
          - `title = <method 'title' of 'bytearray' objects>`
          - `translate = <method 'translate' of 'bytearray' objects>`
          - `upper = <method 'upper' of 'bytearray' objects>`
          - `zfill = <method 'zfill' of 'bytearray' objects>`
        </details>
        <details><summary>`class bytes(object)`</summary>
          - `capitalize = <method 'capitalize' of 'bytes' objects>`
          - `center = <method 'center' of 'bytes' objects>`
          - `count = <method 'count' of 'bytes' objects>`
          - `decode = <method 'decode' of 'bytes' objects>`
          - `endswith = <method 'endswith' of 'bytes' objects>`
          - `expandtabs = <method 'expandtabs' of 'bytes' objects>`
          - `find = <method 'find' of 'bytes' objects>`
          - `fromhex = <built-in method fromhex of type object at 0x55fa99f8e9a0>`
          - `hex = <method 'hex' of 'bytes' objects>`
          - `index = <method 'index' of 'bytes' objects>`
          - `isalnum = <method 'isalnum' of 'bytes' objects>`
          - `isalpha = <method 'isalpha' of 'bytes' objects>`
          - `isascii = <method 'isascii' of 'bytes' objects>`
          - `isdigit = <method 'isdigit' of 'bytes' objects>`
          - `islower = <method 'islower' of 'bytes' objects>`
          - `isspace = <method 'isspace' of 'bytes' objects>`
          - `istitle = <method 'istitle' of 'bytes' objects>`
          - `isupper = <method 'isupper' of 'bytes' objects>`
          - `join = <method 'join' of 'bytes' objects>`
          - `ljust = <method 'ljust' of 'bytes' objects>`
          - `lower = <method 'lower' of 'bytes' objects>`
          - `lstrip = <method 'lstrip' of 'bytes' objects>`
          - `maketrans = <built-in method maketrans of type object at 0x55fa99f8e9a0>`
          - `partition = <method 'partition' of 'bytes' objects>`
          - `removeprefix = <method 'removeprefix' of 'bytes' objects>`
          - `removesuffix = <method 'removesuffix' of 'bytes' objects>`
          - `replace = <method 'replace' of 'bytes' objects>`
          - `rfind = <method 'rfind' of 'bytes' objects>`
          - `rindex = <method 'rindex' of 'bytes' objects>`
          - `rjust = <method 'rjust' of 'bytes' objects>`
          - `rpartition = <method 'rpartition' of 'bytes' objects>`
          - `rsplit = <method 'rsplit' of 'bytes' objects>`
          - `rstrip = <method 'rstrip' of 'bytes' objects>`
          - `split = <method 'split' of 'bytes' objects>`
          - `splitlines = <method 'splitlines' of 'bytes' objects>`
          - `startswith = <method 'startswith' of 'bytes' objects>`
          - `strip = <method 'strip' of 'bytes' objects>`
          - `swapcase = <method 'swapcase' of 'bytes' objects>`
          - `title = <method 'title' of 'bytes' objects>`
          - `translate = <method 'translate' of 'bytes' objects>`
          - `upper = <method 'upper' of 'bytes' objects>`
          - `zfill = <method 'zfill' of 'bytes' objects>`
        </details>
        - `callable = <built-in function callable>`
        - `chr = <built-in function chr>`
        <details><summary>`class classmethod(object)`</summary>
        </details>
        - `compile = <built-in function compile>`
        <details><summary>`class complex(object)`</summary>
          - `conjugate = <method 'conjugate' of 'complex' objects>`
          - `imag = <member 'imag' of 'complex' objects>`
          - `real = <member 'real' of 'complex' objects>`
        </details>
        - `copyright = Copyright (c) 2001-2023 Python Software Foundation.
All Rights Reserved.

Copyright (c) 2000 BeOpen.com.
All Rights Reserved.

Copyright (c) 1995-2001 Corporation for National Research Initiatives.
All Rights Reserved.

Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
All Rights Reserved.`
        - `credits =     Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands
    for supporting Python development.  See www.python.org for more information.`
        - `delattr = <built-in function delattr>`
        <details><summary>`class dict(object)`</summary>
          - `clear = <method 'clear' of 'dict' objects>`
          - `copy = <method 'copy' of 'dict' objects>`
          - `fromkeys = <built-in method fromkeys of type object at 0x55fa99f7ea80>`
          - `get = <method 'get' of 'dict' objects>`
          - `items = <method 'items' of 'dict' objects>`
          - `keys = <method 'keys' of 'dict' objects>`
          - `pop = <method 'pop' of 'dict' objects>`
          - `popitem = <method 'popitem' of 'dict' objects>`
          - `setdefault = <method 'setdefault' of 'dict' objects>`
          - `update = <method 'update' of 'dict' objects>`
          - `values = <method 'values' of 'dict' objects>`
        </details>
        - `dir = <built-in function dir>`
        - `divmod = <built-in function divmod>`
        <details><summary>`class enumerate(object)`</summary>
        </details>
        - `eval = <built-in function eval>`
        - `exec = <built-in function exec>`
        - `exit = Use exit() or Ctrl-D (i.e. EOF) to exit`
        <details><summary>`class filter(object)`</summary>
        </details>
        <details><summary>`class float(object)`</summary>
          - `as_integer_ratio = <method 'as_integer_ratio' of 'float' objects>`
          - `conjugate = <method 'conjugate' of 'float' objects>`
          - `fromhex = <built-in method fromhex of type object at 0x55fa99f81600>`
          - `hex = <method 'hex' of 'float' objects>`
          - `imag = <attribute 'imag' of 'float' objects>`
          - `is_integer = <method 'is_integer' of 'float' objects>`
          - `real = <attribute 'real' of 'float' objects>`
        </details>
        - `format = <built-in function format>`
        <details><summary>`class frozenset(object)`</summary>
          - `copy = <method 'copy' of 'frozenset' objects>`
          - `difference = <method 'difference' of 'frozenset' objects>`
          - `intersection = <method 'intersection' of 'frozenset' objects>`
          - `isdisjoint = <method 'isdisjoint' of 'frozenset' objects>`
          - `issubset = <method 'issubset' of 'frozenset' objects>`
          - `issuperset = <method 'issuperset' of 'frozenset' objects>`
          - `symmetric_difference = <method 'symmetric_difference' of 'frozenset' objects>`
          - `union = <method 'union' of 'frozenset' objects>`
        </details>
        - `getattr = <built-in function getattr>`
        - `globals = <built-in function globals>`
        - `hasattr = <built-in function hasattr>`
        - `hash = <built-in function hash>`
        - `help = Type help() for interactive help, or help(object) for help about object.`
        - `hex = <built-in function hex>`
        - `id = <built-in function id>`
        - `input = <built-in function input>`
        <details><summary>`class int(object)`</summary>
          - `as_integer_ratio = <method 'as_integer_ratio' of 'int' objects>`
          - `bit_count = <method 'bit_count' of 'int' objects>`
          - `bit_length = <method 'bit_length' of 'int' objects>`
          - `conjugate = <method 'conjugate' of 'int' objects>`
          - `denominator = <attribute 'denominator' of 'int' objects>`
          - `from_bytes = <built-in method from_bytes of type object at 0x55fa99f7f120>`
          - `imag = <attribute 'imag' of 'int' objects>`
          - `numerator = <attribute 'numerator' of 'int' objects>`
          - `real = <attribute 'real' of 'int' objects>`
          - `to_bytes = <method 'to_bytes' of 'int' objects>`
        </details>
        - `isinstance = <built-in function isinstance>`
        - `issubclass = <built-in function issubclass>`
        - `iter = <built-in function iter>`
        - `len = <built-in function len>`
        - `license = Type license() to see the full license text`
        <details><summary>`class list(object)`</summary>
          - `append = <method 'append' of 'list' objects>`
          - `clear = <method 'clear' of 'list' objects>`
          - `copy = <method 'copy' of 'list' objects>`
          - `count = <method 'count' of 'list' objects>`
          - `extend = <method 'extend' of 'list' objects>`
          - `index = <method 'index' of 'list' objects>`
          - `insert = <method 'insert' of 'list' objects>`
          - `pop = <method 'pop' of 'list' objects>`
          - `remove = <method 'remove' of 'list' objects>`
          - `reverse = <method 'reverse' of 'list' objects>`
          - `sort = <method 'sort' of 'list' objects>`
        </details>
        - `locals = <built-in function locals>`
        <details><summary>`class map(object)`</summary>
        </details>
        - `max = <built-in function max>`
        <details><summary>`class memoryview(object)`</summary>
          - `c_contiguous = <attribute 'c_contiguous' of 'memoryview' objects>`
          - `cast = <method 'cast' of 'memoryview' objects>`
          - `contiguous = <attribute 'contiguous' of 'memoryview' objects>`
          - `f_contiguous = <attribute 'f_contiguous' of 'memoryview' objects>`
          - `format = <attribute 'format' of 'memoryview' objects>`
          - `hex = <method 'hex' of 'memoryview' objects>`
          - `itemsize = <attribute 'itemsize' of 'memoryview' objects>`
          - `nbytes = <attribute 'nbytes' of 'memoryview' objects>`
          - `ndim = <attribute 'ndim' of 'memoryview' objects>`
          - `obj = <attribute 'obj' of 'memoryview' objects>`
          - `readonly = <attribute 'readonly' of 'memoryview' objects>`
          - `release = <method 'release' of 'memoryview' objects>`
          - `shape = <attribute 'shape' of 'memoryview' objects>`
          - `strides = <attribute 'strides' of 'memoryview' objects>`
          - `suboffsets = <attribute 'suboffsets' of 'memoryview' objects>`
          - `tobytes = <method 'tobytes' of 'memoryview' objects>`
          - `tolist = <method 'tolist' of 'memoryview' objects>`
          - `toreadonly = <method 'toreadonly' of 'memoryview' objects>`
        </details>
        - `min = <built-in function min>`
        - `next = <built-in function next>`
        <details><summary>`class object()`</summary>
        </details>
        - `oct = <built-in function oct>`
        - `open = <built-in function open>`
        - `ord = <built-in function ord>`
        - `pow = <built-in function pow>`
        - `print = <built-in function print>`
        <details><summary>`class property(object)`</summary>
          - `deleter = <method 'deleter' of 'property' objects>`
          - `fdel = <member 'fdel' of 'property' objects>`
          - `fget = <member 'fget' of 'property' objects>`
          - `fset = <member 'fset' of 'property' objects>`
          - `getter = <method 'getter' of 'property' objects>`
          - `setter = <method 'setter' of 'property' objects>`
        </details>
        - `quit = Use quit() or Ctrl-D (i.e. EOF) to exit`
        <details><summary>`class range(object)`</summary>
          - `count = <method 'count' of 'range' objects>`
          - `index = <method 'index' of 'range' objects>`
          - `start = <member 'start' of 'range' objects>`
          - `step = <member 'step' of 'range' objects>`
          - `stop = <member 'stop' of 'range' objects>`
        </details>
        - `repr = <built-in function repr>`
        <details><summary>`class reversed(object)`</summary>
        </details>
        - `round = <built-in function round>`
        <details><summary>`class set(object)`</summary>
          - `add = <method 'add' of 'set' objects>`
          - `clear = <method 'clear' of 'set' objects>`
          - `copy = <method 'copy' of 'set' objects>`
          - `difference = <method 'difference' of 'set' objects>`
          - `difference_update = <method 'difference_update' of 'set' objects>`
          - `discard = <method 'discard' of 'set' objects>`
          - `intersection = <method 'intersection' of 'set' objects>`
          - `intersection_update = <method 'intersection_update' of 'set' objects>`
          - `isdisjoint = <method 'isdisjoint' of 'set' objects>`
          - `issubset = <method 'issubset' of 'set' objects>`
          - `issuperset = <method 'issuperset' of 'set' objects>`
          - `pop = <method 'pop' of 'set' objects>`
          - `remove = <method 'remove' of 'set' objects>`
          - `symmetric_difference = <method 'symmetric_difference' of 'set' objects>`
          - `symmetric_difference_update = <method 'symmetric_difference_update' of 'set' objects>`
          - `union = <method 'union' of 'set' objects>`
          - `update = <method 'update' of 'set' objects>`
        </details>
        - `setattr = <built-in function setattr>`
        <details><summary>`class slice(object)`</summary>
          - `indices = <method 'indices' of 'slice' objects>`
          - `start = <member 'start' of 'slice' objects>`
          - `step = <member 'step' of 'slice' objects>`
          - `stop = <member 'stop' of 'slice' objects>`
        </details>
        - `sorted = <built-in function sorted>`
        <details><summary>`class staticmethod(object)`</summary>
        </details>
        <details><summary>`class str(object)`</summary>
          - `capitalize = <method 'capitalize' of 'str' objects>`
          - `casefold = <method 'casefold' of 'str' objects>`
          - `center = <method 'center' of 'str' objects>`
          - `count = <method 'count' of 'str' objects>`
          - `encode = <method 'encode' of 'str' objects>`
          - `endswith = <method 'endswith' of 'str' objects>`
          - `expandtabs = <method 'expandtabs' of 'str' objects>`
          - `find = <method 'find' of 'str' objects>`
          - `format = <method 'format' of 'str' objects>`
          - `format_map = <method 'format_map' of 'str' objects>`
          - `index = <method 'index' of 'str' objects>`
          - `isalnum = <method 'isalnum' of 'str' objects>`
          - `isalpha = <method 'isalpha' of 'str' objects>`
          - `isascii = <method 'isascii' of 'str' objects>`
          - `isdecimal = <method 'isdecimal' of 'str' objects>`
          - `isdigit = <method 'isdigit' of 'str' objects>`
          - `isidentifier = <method 'isidentifier' of 'str' objects>`
          - `islower = <method 'islower' of 'str' objects>`
          - `isnumeric = <method 'isnumeric' of 'str' objects>`
          - `isprintable = <method 'isprintable' of 'str' objects>`
          - `isspace = <method 'isspace' of 'str' objects>`
          - `istitle = <method 'istitle' of 'str' objects>`
          - `isupper = <method 'isupper' of 'str' objects>`
          - `join = <method 'join' of 'str' objects>`
          - `ljust = <method 'ljust' of 'str' objects>`
          - `lower = <method 'lower' of 'str' objects>`
          - `lstrip = <method 'lstrip' of 'str' objects>`
          - `maketrans = <built-in method maketrans of type object at 0x55fa99f75f60>`
          - `partition = <method 'partition' of 'str' objects>`
          - `removeprefix = <method 'removeprefix' of 'str' objects>`
          - `removesuffix = <method 'removesuffix' of 'str' objects>`
          - `replace = <method 'replace' of 'str' objects>`
          - `rfind = <method 'rfind' of 'str' objects>`
          - `rindex = <method 'rindex' of 'str' objects>`
          - `rjust = <method 'rjust' of 'str' objects>`
          - `rpartition = <method 'rpartition' of 'str' objects>`
          - `rsplit = <method 'rsplit' of 'str' objects>`
          - `rstrip = <method 'rstrip' of 'str' objects>`
          - `split = <method 'split' of 'str' objects>`
          - `splitlines = <method 'splitlines' of 'str' objects>`
          - `startswith = <method 'startswith' of 'str' objects>`
          - `strip = <method 'strip' of 'str' objects>`
          - `swapcase = <method 'swapcase' of 'str' objects>`
          - `title = <method 'title' of 'str' objects>`
          - `translate = <method 'translate' of 'str' objects>`
          - `upper = <method 'upper' of 'str' objects>`
          - `zfill = <method 'zfill' of 'str' objects>`
        </details>
        - `sum = <built-in function sum>`
        <details><summary>`class super(object)`</summary>
        </details>
        <details><summary>`class tuple(object)`</summary>
          - `count = <method 'count' of 'tuple' objects>`
          - `index = <method 'index' of 'tuple' objects>`
        </details>
        <details><summary>`class type(object)`</summary>
          - `mro = <method 'mro' of 'type' objects>`
        </details>
        - `vars = <built-in function vars>`
        <details><summary>`class zip(object)`</summary>
        </details>
      </details>
      <details><summary>`copy`</summary>
        <details><summary>`class Error(Exception)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`copy (x)`</summary>
        </details>
        <details><summary>`deepcopy (x, memo=None, _nil=[])`</summary>
        </details>
        - `dispatch_table = {<class 'complex'>: <function pickle_complex at 0x7f13fb103100>, <class 'types.UnionType'>: <function pickle_union at 0x7f13fb103240>, <class 're.Pattern'>: <function _pickle at 0x7f13fb0e36a0>}`
        <details><summary>`class Error(Exception)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
      </details>
      <details><summary>`dataclass (cls=None, /, *, init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False, match_args=True, kw_only=False, slots=False, weakref_slot=False)`</summary>
      </details>
      <details><summary>`field (*, default=<dataclasses._MISSING_TYPE object at 0x7f13faeba050>, default_factory=<dataclasses._MISSING_TYPE object at 0x7f13faeba050>, init=True, repr=True, hash=None, compare=True, metadata=None, kw_only=<dataclasses._MISSING_TYPE object at 0x7f13faeba050>)`</summary>
      </details>
      <details><summary>`fields (class_or_instance)`</summary>
      </details>
      <details><summary>`functools`</summary>
        <details><summary>`class GenericAlias(object)`</summary>
        </details>
        <details><summary>`class RLock(object)`</summary>
          - `acquire = <method 'acquire' of '_thread.RLock' objects>`
          - `release = <method 'release' of '_thread.RLock' objects>`
        </details>
        - `WRAPPER_ASSIGNMENTS = ('__module__', '__name__', '__qualname__', '__doc__', '__annotations__')`
        - `WRAPPER_UPDATES = ('__dict__',)`
        <details><summary>`cache (user_function, /)`</summary>
        </details>
        <details><summary>`class cached_property(object)`</summary>
          - `__class_getitem__ <signature unavailable>`
          <details><summary>`__get__ (self, instance, owner=None)`</summary>
          </details>
          <details><summary>`__init__ (self, func)`</summary>
          </details>
          <details><summary>`__set_name__ (self, owner, name)`</summary>
          </details>
        </details>
        - `cmp_to_key = <built-in function cmp_to_key>`
        - `get_cache_token = <built-in function get_cache_token>`
        <details><summary>`lru_cache (maxsize=128, typed=False)`</summary>
        </details>
        <details><summary>`namedtuple (typename, field_names, *, rename=False, defaults=None, module=None)`</summary>
        </details>
        <details><summary>`class partial(object)`</summary>
          - `args = <member 'args' of 'functools.partial' objects>`
          - `func = <member 'func' of 'functools.partial' objects>`
          - `keywords = <member 'keywords' of 'functools.partial' objects>`
        </details>
        <details><summary>`class partialmethod(object)`</summary>
          - `__class_getitem__ <signature unavailable>`
          <details><summary>`__get__ (self, obj, cls=None)`</summary>
          </details>
          <details><summary>`__init__ (self, func, /, *args, **keywords)`</summary>
          </details>
          <details><summary>`__repr__ (self)`</summary>
          </details>
          <details><summary>`_make_unbound_method (self)`</summary>
          </details>
        </details>
        <details><summary>`recursive_repr (fillvalue='...')`</summary>
        </details>
        - `reduce = <built-in function reduce>`
        <details><summary>`singledispatch (func)`</summary>
        </details>
        <details><summary>`class singledispatchmethod(object)`</summary>
          <details><summary>`__get__ (self, obj, cls=None)`</summary>
          </details>
          <details><summary>`__init__ (self, func)`</summary>
          </details>
          <details><summary>`register (self, cls, method=None)`</summary>
          </details>
        </details>
        <details><summary>`total_ordering (cls)`</summary>
        </details>
        <details><summary>`update_wrapper (wrapper, wrapped, assigned=('__module__', '__name__', '__qualname__', '__doc__', '__annotations__'), updated=('__dict__',))`</summary>
        </details>
        <details><summary>`wraps (wrapped, assigned=('__module__', '__name__', '__qualname__', '__doc__', '__annotations__'), updated=('__dict__',))`</summary>
        </details>
      </details>
      <details><summary>`inspect`</summary>
        <details><summary>`class ArgInfo(tuple)`</summary>
          <details><summary>`__getnewargs__ (self)`</summary>
          </details>
          <details><summary>`__new__ (_cls, args, varargs, keywords, locals)`</summary>
          </details>
          <details><summary>`__repr__ (self)`</summary>
          </details>
          <details><summary>`_asdict (self)`</summary>
          </details>
          <details><summary>`_make (iterable)`</summary>
          </details>
          <details><summary>`_replace (self, /, **kwds)`</summary>
          </details>
          - `args = _tuplegetter(0, 'Alias for field number 0')`
          - `count = <method 'count' of 'tuple' objects>`
          - `index = <method 'index' of 'tuple' objects>`
          - `keywords = _tuplegetter(2, 'Alias for field number 2')`
          - `locals = _tuplegetter(3, 'Alias for field number 3')`
          - `varargs = _tuplegetter(1, 'Alias for field number 1')`
        </details>
        <details><summary>`class Arguments(tuple)`</summary>
          <details><summary>`__getnewargs__ (self)`</summary>
          </details>
          <details><summary>`__new__ (_cls, args, varargs, varkw)`</summary>
          </details>
          <details><summary>`__repr__ (self)`</summary>
          </details>
          <details><summary>`_asdict (self)`</summary>
          </details>
          <details><summary>`_make (iterable)`</summary>
          </details>
          <details><summary>`_replace (self, /, **kwds)`</summary>
          </details>
          - `args = _tuplegetter(0, 'Alias for field number 0')`
          - `count = <method 'count' of 'tuple' objects>`
          - `index = <method 'index' of 'tuple' objects>`
          - `varargs = _tuplegetter(1, 'Alias for field number 1')`
          - `varkw = _tuplegetter(2, 'Alias for field number 2')`
        </details>
        <details><summary>`class Attribute(tuple)`</summary>
          <details><summary>`__getnewargs__ (self)`</summary>
          </details>
          <details><summary>`__new__ (_cls, name, kind, defining_class, object)`</summary>
          </details>
          <details><summary>`__repr__ (self)`</summary>
          </details>
          <details><summary>`_asdict (self)`</summary>
          </details>
          <details><summary>`_make (iterable)`</summary>
          </details>
          <details><summary>`_replace (self, /, **kwds)`</summary>
          </details>
          - `count = <method 'count' of 'tuple' objects>`
          - `defining_class = _tuplegetter(2, 'Alias for field number 2')`
          - `index = <method 'index' of 'tuple' objects>`
          - `kind = _tuplegetter(1, 'Alias for field number 1')`
          - `name = _tuplegetter(0, 'Alias for field number 0')`
          - `object = _tuplegetter(3, 'Alias for field number 3')`
        </details>
        <details><summary>`class BlockFinder(object)`</summary>
          <details><summary>`__init__ (self)`</summary>
          </details>
          <details><summary>`tokeneater (self, type, token, srowcol, erowcol, line)`</summary>
          </details>
        </details>
        <details><summary>`class BoundArguments(object)`</summary>
          <details><summary>`__eq__ (self, other)`</summary>
          </details>
          <details><summary>`__getstate__ (self)`</summary>
          </details>
          <details><summary>`__init__ (self, signature, arguments)`</summary>
          </details>
          <details><summary>`__repr__ (self)`</summary>
          </details>
          <details><summary>`__setstate__ (self, state)`</summary>
          </details>
          <details><summary>`apply_defaults (self)`</summary>
          </details>
          - `args = <property object at 0x7f13fb042980>`
          - `arguments = <member 'arguments' of 'BoundArguments' objects>`
          - `kwargs = <property object at 0x7f13fb0429d0>`
          - `signature = <property object at 0x7f13fb042930>`
        </details>
        - `CORO_CLOSED = 'CORO_CLOSED'`
        - `CORO_CREATED = 'CORO_CREATED'`
        - `CORO_RUNNING = 'CORO_RUNNING'`
        - `CORO_SUSPENDED = 'CORO_SUSPENDED'`
        - `CO_ASYNC_GENERATOR = 512`
        - `CO_COROUTINE = 128`
        - `CO_GENERATOR = 32`
        - `CO_ITERABLE_COROUTINE = 256`
        - `CO_NESTED = 16`
        - `CO_NEWLOCALS = 2`
        - `CO_NOFREE = 64`
        - `CO_OPTIMIZED = 1`
        - `CO_VARARGS = 4`
        - `CO_VARKEYWORDS = 8`
        <details><summary>`class ClassFoundException(Exception)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class ClosureVars(tuple)`</summary>
          <details><summary>`__getnewargs__ (self)`</summary>
          </details>
          <details><summary>`__new__ (_cls, nonlocals, globals, builtins, unbound)`</summary>
          </details>
          <details><summary>`__repr__ (self)`</summary>
          </details>
          <details><summary>`_asdict (self)`</summary>
          </details>
          <details><summary>`_make (iterable)`</summary>
          </details>
          <details><summary>`_replace (self, /, **kwds)`</summary>
          </details>
          - `builtins = _tuplegetter(2, 'Alias for field number 2')`
          - `count = <method 'count' of 'tuple' objects>`
          - `globals = _tuplegetter(1, 'Alias for field number 1')`
          - `index = <method 'index' of 'tuple' objects>`
          - `nonlocals = _tuplegetter(0, 'Alias for field number 0')`
          - `unbound = _tuplegetter(3, 'Alias for field number 3')`
        </details>
        <details><summary>`class EndOfBlock(Exception)`</summary>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`class FrameInfo(_FrameInfo)`</summary>
          <details><summary>`__getnewargs__ (self)`</summary>
          </details>
          <details><summary>`__new__ (cls, frame, filename, lineno, function, code_context, index, *, positions=None)`</summary>
          </details>
          <details><summary>`__repr__ (self)`</summary>
          </details>
          <details><summary>`_asdict (self)`</summary>
          </details>
          <details><summary>`_make (iterable)`</summary>
          </details>
          <details><summary>`_replace (self, /, **kwds)`</summary>
          </details>
          - `code_context = _tuplegetter(4, 'Alias for field number 4')`
          - `count = <method 'count' of 'tuple' objects>`
          - `filename = _tuplegetter(1, 'Alias for field number 1')`
          - `frame = _tuplegetter(0, 'Alias for field number 0')`
          - `function = _tuplegetter(3, 'Alias for field number 3')`
          - `index = _tuplegetter(5, 'Alias for field number 5')`
          - `lineno = _tuplegetter(2, 'Alias for field number 2')`
        </details>
        <details><summary>`class FullArgSpec(tuple)`</summary>
          <details><summary>`__getnewargs__ (self)`</summary>
          </details>
          <details><summary>`__new__ (_cls, args, varargs, varkw, defaults, kwonlyargs, kwonlydefaults, annotations)`</summary>
          </details>
          <details><summary>`__repr__ (self)`</summary>
          </details>
          <details><summary>`_asdict (self)`</summary>
          </details>
          <details><summary>`_make (iterable)`</summary>
          </details>
          <details><summary>`_replace (self, /, **kwds)`</summary>
          </details>
          - `annotations = _tuplegetter(6, 'Alias for field number 6')`
          - `args = _tuplegetter(0, 'Alias for field number 0')`
          - `count = <method 'count' of 'tuple' objects>`
          - `defaults = _tuplegetter(3, 'Alias for field number 3')`
          - `index = <method 'index' of 'tuple' objects>`
          - `kwonlyargs = _tuplegetter(4, 'Alias for field number 4')`
          - `kwonlydefaults = _tuplegetter(5, 'Alias for field number 5')`
          - `varargs = _tuplegetter(1, 'Alias for field number 1')`
          - `varkw = _tuplegetter(2, 'Alias for field number 2')`
        </details>
        - `GEN_CLOSED = 'GEN_CLOSED'`
        - `GEN_CREATED = 'GEN_CREATED'`
        - `GEN_RUNNING = 'GEN_RUNNING'`
        - `GEN_SUSPENDED = 'GEN_SUSPENDED'`
        <details><summary>`class OrderedDict(dict)`</summary>
          - `clear = <method 'clear' of 'collections.OrderedDict' objects>`
          - `copy = <method 'copy' of 'collections.OrderedDict' objects>`
          - `fromkeys = <built-in method fromkeys of type object at 0x55fa99f7d0a0>`
          - `get = <method 'get' of 'dict' objects>`
          - `items = <method 'items' of 'collections.OrderedDict' objects>`
          - `keys = <method 'keys' of 'collections.OrderedDict' objects>`
          - `move_to_end = <method 'move_to_end' of 'collections.OrderedDict' objects>`
          - `pop = <method 'pop' of 'collections.OrderedDict' objects>`
          - `popitem = <method 'popitem' of 'collections.OrderedDict' objects>`
          - `setdefault = <method 'setdefault' of 'collections.OrderedDict' objects>`
          - `update = <method 'update' of 'collections.OrderedDict' objects>`
          - `values = <method 'values' of 'collections.OrderedDict' objects>`
        </details>
        <details><summary>`class Parameter(object)`</summary>
          - `KEYWORD_ONLY = <_ParameterKind.KEYWORD_ONLY: 3>`
          - `POSITIONAL_ONLY = <_ParameterKind.POSITIONAL_ONLY: 0>`
          - `POSITIONAL_OR_KEYWORD = <_ParameterKind.POSITIONAL_OR_KEYWORD: 1>`
          - `VAR_KEYWORD = <_ParameterKind.VAR_KEYWORD: 4>`
          - `VAR_POSITIONAL = <_ParameterKind.VAR_POSITIONAL: 2>`
          <details><summary>`__eq__ (self, other)`</summary>
          </details>
          <details><summary>`__hash__ (self)`</summary>
          </details>
          <details><summary>`__init__ (self, name, kind, *, default, annotation)`</summary>
          </details>
          <details><summary>`__reduce__ (self)`</summary>
          </details>
          <details><summary>`__repr__ (self)`</summary>
          </details>
          <details><summary>`__setstate__ (self, state)`</summary>
          </details>
          <details><summary>`__str__ (self)`</summary>
          </details>
          - `annotation = <property object at 0x7f13fb042840>`
          - `default = <property object at 0x7f13fb0427f0>`
          - `empty = <class 'inspect._empty'>`
          - `kind = <property object at 0x7f13fb042890>`
          - `name = <property object at 0x7f13fb0427a0>`
          <details><summary>`replace (self, *, name=<class 'inspect._void'>, kind=<class 'inspect._void'>, annotation=<class 'inspect._void'>, default=<class 'inspect._void'>)`</summary>
          </details>
        </details>
        <details><summary>`class Path(PurePath)`</summary>
          <details><summary>`__bytes__ (self)`</summary>
          </details>
          <details><summary>`__enter__ (self)`</summary>
          </details>
          <details><summary>`__eq__ (self, other)`</summary>
          </details>
          <details><summary>`__exit__ (self, t, v, tb)`</summary>
          </details>
          <details><summary>`__fspath__ (self)`</summary>
          </details>
          <details><summary>`__ge__ (self, other)`</summary>
          </details>
          <details><summary>`__gt__ (self, other)`</summary>
          </details>
          <details><summary>`__hash__ (self)`</summary>
          </details>
          <details><summary>`__le__ (self, other)`</summary>
          </details>
          <details><summary>`__lt__ (self, other)`</summary>
          </details>
          <details><summary>`__new__ (cls, *args, **kwargs)`</summary>
          </details>
          <details><summary>`__reduce__ (self)`</summary>
          </details>
          <details><summary>`__repr__ (self)`</summary>
          </details>
          <details><summary>`__rtruediv__ (self, key)`</summary>
          </details>
          <details><summary>`__str__ (self)`</summary>
          </details>
          <details><summary>`__truediv__ (self, key)`</summary>
          </details>
          <details><summary>`_format_parsed_parts (drv, root, parts)`</summary>
          </details>
          <details><summary>`_from_parsed_parts (drv, root, parts)`</summary>
          </details>
          <details><summary>`_from_parts (args)`</summary>
          </details>
          <details><summary>`_make_child (self, args)`</summary>
          </details>
          <details><summary>`_make_child_relpath (self, part)`</summary>
          </details>
          <details><summary>`_parse_args (args)`</summary>
          </details>
          <details><summary>`_scandir (self)`</summary>
          </details>
          <details><summary>`absolute (self)`</summary>
          </details>
          - `anchor = <property object at 0x7f13fb1612b0>`
          <details><summary>`as_posix (self)`</summary>
          </details>
          <details><summary>`as_uri (self)`</summary>
          </details>
          <details><summary>`chmod (self, mode, *, follow_symlinks=True)`</summary>
          </details>
          <details><summary>`cwd ()`</summary>
          </details>
          - `drive = <property object at 0x7f13fb161210>`
          <details><summary>`exists (self)`</summary>
          </details>
          <details><summary>`expanduser (self)`</summary>
          </details>
          <details><summary>`glob (self, pattern)`</summary>
          </details>
          <details><summary>`group (self)`</summary>
          </details>
          <details><summary>`hardlink_to (self, target)`</summary>
          </details>
          <details><summary>`home ()`</summary>
          </details>
          <details><summary>`is_absolute (self)`</summary>
          </details>
          <details><summary>`is_block_device (self)`</summary>
          </details>
          <details><summary>`is_char_device (self)`</summary>
          </details>
          <details><summary>`is_dir (self)`</summary>
          </details>
          <details><summary>`is_fifo (self)`</summary>
          </details>
          <details><summary>`is_file (self)`</summary>
          </details>
          <details><summary>`is_mount (self)`</summary>
          </details>
          <details><summary>`is_relative_to (self, *other)`</summary>
          </details>
          <details><summary>`is_reserved (self)`</summary>
          </details>
          <details><summary>`is_socket (self)`</summary>
          </details>
          <details><summary>`is_symlink (self)`</summary>
          </details>
          <details><summary>`iterdir (self)`</summary>
          </details>
          <details><summary>`joinpath (self, *args)`</summary>
          </details>
          <details><summary>`lchmod (self, mode)`</summary>
          </details>
          <details><summary>`link_to (self, target)`</summary>
          </details>
          <details><summary>`lstat (self)`</summary>
          </details>
          <details><summary>`match (self, path_pattern)`</summary>
          </details>
          <details><summary>`mkdir (self, mode=511, parents=False, exist_ok=False)`</summary>
          </details>
          - `name = <property object at 0x7f13fb161300>`
          <details><summary>`open (self, mode='r', buffering=-1, encoding=None, errors=None, newline=None)`</summary>
          </details>
          <details><summary>`owner (self)`</summary>
          </details>
          - `parent = <property object at 0x7f13fb161490>`
          - `parents = <property object at 0x7f13fb1614e0>`
          - `parts = <property object at 0x7f13fb161440>`
          <details><summary>`read_bytes (self)`</summary>
          </details>
          <details><summary>`read_text (self, encoding=None, errors=None)`</summary>
          </details>
          <details><summary>`readlink (self)`</summary>
          </details>
          <details><summary>`relative_to (self, *other)`</summary>
          </details>
          <details><summary>`rename (self, target)`</summary>
          </details>
          <details><summary>`replace (self, target)`</summary>
          </details>
          <details><summary>`resolve (self, strict=False)`</summary>
          </details>
          <details><summary>`rglob (self, pattern)`</summary>
          </details>
          <details><summary>`rmdir (self)`</summary>
          </details>
          - `root = <property object at 0x7f13fb161260>`
          <details><summary>`samefile (self, other_path)`</summary>
          </details>
          <details><summary>`stat (self, *, follow_symlinks=True)`</summary>
          </details>
          - `stem = <property object at 0x7f13fb1613f0>`
          - `suffix = <property object at 0x7f13fb161350>`
          - `suffixes = <property object at 0x7f13fb1613a0>`
          <details><summary>`symlink_to (self, target, target_is_directory=False)`</summary>
          </details>
          <details><summary>`touch (self, mode=438, exist_ok=True)`</summary>
          </details>
          <details><summary>`unlink (self, missing_ok=False)`</summary>
          </details>
          <details><summary>`with_name (self, name)`</summary>
          </details>
          <details><summary>`with_stem (self, stem)`</summary>
          </details>
          <details><summary>`with_suffix (self, suffix)`</summary>
          </details>
          <details><summary>`write_bytes (self, data)`</summary>
          </details>
          <details><summary>`write_text (self, data, encoding=None, errors=None, newline=None)`</summary>
          </details>
        </details>
        <details><summary>`class Signature(object)`</summary>
          <details><summary>`__eq__ (self, other)`</summary>
          </details>
          <details><summary>`__hash__ (self)`</summary>
          </details>
          <details><summary>`__init__ (self, parameters=None, *, return_annotation, __validate_parameters__=True)`</summary>
          </details>
          <details><summary>`__reduce__ (self)`</summary>
          </details>
          <details><summary>`__repr__ (self)`</summary>
          </details>
          <details><summary>`__setstate__ (self, state)`</summary>
          </details>
          <details><summary>`__str__ (self)`</summary>
          </details>
          <details><summary>`_bind (self, args, kwargs, *, partial=False)`</summary>
          </details>
          <details><summary>`_hash_basis (self)`</summary>
          </details>
          <details><summary>`bind (self, /, *args, **kwargs)`</summary>
          </details>
          <details><summary>`bind_partial (self, /, *args, **kwargs)`</summary>
          </details>
          - `empty = <class 'inspect._empty'>`
          <details><summary>`from_callable (obj, *, follow_wrapped=True, globals=None, locals=None, eval_str=False)`</summary>
          </details>
          - `parameters = <property object at 0x7f13fb042a70>`
          <details><summary>`replace (self, *, parameters=<class 'inspect._void'>, return_annotation=<class 'inspect._void'>)`</summary>
          </details>
          - `return_annotation = <property object at 0x7f13fb042ac0>`
        </details>
        - `TPFLAGS_IS_ABSTRACT = 1048576`
        <details><summary>`class Traceback(_Traceback)`</summary>
          <details><summary>`__getnewargs__ (self)`</summary>
          </details>
          <details><summary>`__new__ (cls, filename, lineno, function, code_context, index, *, positions=None)`</summary>
          </details>
          <details><summary>`__repr__ (self)`</summary>
          </details>
          <details><summary>`_asdict (self)`</summary>
          </details>
          <details><summary>`_make (iterable)`</summary>
          </details>
          <details><summary>`_replace (self, /, **kwds)`</summary>
          </details>
          - `code_context = _tuplegetter(3, 'Alias for field number 3')`
          - `count = <method 'count' of 'tuple' objects>`
          - `filename = _tuplegetter(0, 'Alias for field number 0')`
          - `function = _tuplegetter(2, 'Alias for field number 2')`
          - `index = _tuplegetter(4, 'Alias for field number 4')`
          - `lineno = _tuplegetter(1, 'Alias for field number 1')`
        </details>
        <details><summary>`abc`</summary>
        </details>
        <details><summary>`ast`</summary>
        </details>
        <details><summary>`class attrgetter(object)`</summary>
        </details>
        <details><summary>`builtins`</summary>
        </details>
        <details><summary>`classify_class_attrs (cls)`</summary>
        </details>
        <details><summary>`cleandoc (doc)`</summary>
        </details>
        <details><summary>`collections`</summary>
        </details>
        <details><summary>`currentframe ()`</summary>
        </details>
        <details><summary>`dis`</summary>
        </details>
        <details><summary>`enum`</summary>
        </details>
        <details><summary>`findsource (object)`</summary>
        </details>
        <details><summary>`formatannotation (annotation, base_module=None)`</summary>
        </details>
        <details><summary>`formatannotationrelativeto (object)`</summary>
        </details>
        <details><summary>`formatargvalues (args, varargs, varkw, locals, formatarg=<class 'str'>, formatvarargs=<function <lambda> at 0x7f13fb055a80>, formatvarkw=<function <lambda> at 0x7f13fb055b20>, formatvalue=<function <lambda> at 0x7f13fb055bc0>)`</summary>
        </details>
        <details><summary>`functools`</summary>
        </details>
        <details><summary>`get_annotations (obj, *, globals=None, locals=None, eval_str=False)`</summary>
        </details>
        <details><summary>`getabsfile (object, _filename=None)`</summary>
        </details>
        <details><summary>`getargs (co)`</summary>
        </details>
        <details><summary>`getargvalues (frame)`</summary>
        </details>
        <details><summary>`getattr_static (obj, attr, default=<object object at 0x7f13fb3c4630>)`</summary>
        </details>
        <details><summary>`getblock (lines)`</summary>
        </details>
        <details><summary>`getcallargs (func, /, *positional, **named)`</summary>
        </details>
        <details><summary>`getclasstree (classes, unique=False)`</summary>
        </details>
        <details><summary>`getclosurevars (func)`</summary>
        </details>
        <details><summary>`getcomments (object)`</summary>
        </details>
        <details><summary>`getcoroutinelocals (coroutine)`</summary>
        </details>
        <details><summary>`getcoroutinestate (coroutine)`</summary>
        </details>
        <details><summary>`getdoc (object)`</summary>
        </details>
        <details><summary>`getfile (object)`</summary>
        </details>
        <details><summary>`getframeinfo (frame, context=1)`</summary>
        </details>
        <details><summary>`getfullargspec (func)`</summary>
        </details>
        <details><summary>`getgeneratorlocals (generator)`</summary>
        </details>
        <details><summary>`getgeneratorstate (generator)`</summary>
        </details>
        <details><summary>`getinnerframes (tb, context=1)`</summary>
        </details>
        <details><summary>`getlineno (frame)`</summary>
        </details>
        <details><summary>`getmembers (object, predicate=None)`</summary>
        </details>
        <details><summary>`getmembers_static (object, predicate=None)`</summary>
        </details>
        <details><summary>`getmodule (object, _filename=None)`</summary>
        </details>
        <details><summary>`getmodulename (path)`</summary>
        </details>
        <details><summary>`getmro (cls)`</summary>
        </details>
        <details><summary>`getouterframes (frame, context=1)`</summary>
        </details>
        <details><summary>`getsource (object)`</summary>
        </details>
        <details><summary>`getsourcefile (object)`</summary>
        </details>
        <details><summary>`getsourcelines (object)`</summary>
        </details>
        <details><summary>`importlib`</summary>
        </details>
        <details><summary>`indentsize (line)`</summary>
        </details>
        <details><summary>`isabstract (object)`</summary>
        </details>
        <details><summary>`isasyncgen (object)`</summary>
        </details>
        <details><summary>`isasyncgenfunction (obj)`</summary>
        </details>
        <details><summary>`isawaitable (object)`</summary>
        </details>
        <details><summary>`isbuiltin (object)`</summary>
        </details>
        <details><summary>`isclass (object)`</summary>
        </details>
        <details><summary>`iscode (object)`</summary>
        </details>
        <details><summary>`iscoroutine (object)`</summary>
        </details>
        <details><summary>`iscoroutinefunction (obj)`</summary>
        </details>
        <details><summary>`isdatadescriptor (object)`</summary>
        </details>
        <details><summary>`isframe (object)`</summary>
        </details>
        <details><summary>`isfunction (object)`</summary>
        </details>
        <details><summary>`isgenerator (object)`</summary>
        </details>
        <details><summary>`isgeneratorfunction (obj)`</summary>
        </details>
        <details><summary>`isgetsetdescriptor (object)`</summary>
        </details>
        - `iskeyword = <built-in method __contains__ of frozenset object at 0x7f13fb1ebca0>`
        <details><summary>`ismemberdescriptor (object)`</summary>
        </details>
        <details><summary>`ismethod (object)`</summary>
        </details>
        <details><summary>`ismethoddescriptor (object)`</summary>
        </details>
        <details><summary>`ismethodwrapper (object)`</summary>
        </details>
        <details><summary>`ismodule (object)`</summary>
        </details>
        <details><summary>`isroutine (object)`</summary>
        </details>
        <details><summary>`istraceback (object)`</summary>
        </details>
        <details><summary>`itertools`</summary>
        </details>
        <details><summary>`linecache`</summary>
        </details>
        - `modulesbyfile = {}`
        <details><summary>`namedtuple (typename, field_names, *, rename=False, defaults=None, module=None)`</summary>
        </details>
        <details><summary>`os`</summary>
        </details>
        <details><summary>`re`</summary>
        </details>
        <details><summary>`signature (obj, *, follow_wrapped=True, globals=None, locals=None, eval_str=False)`</summary>
        </details>
        <details><summary>`stack (context=1)`</summary>
        </details>
        <details><summary>`sys`</summary>
        </details>
        <details><summary>`token`</summary>
        </details>
        <details><summary>`tokenize`</summary>
        </details>
        <details><summary>`trace (context=1)`</summary>
        </details>
        <details><summary>`types`</summary>
        </details>
        <details><summary>`unwrap (func, *, stop=None)`</summary>
        </details>
        <details><summary>`walktree (classes, children, parent)`</summary>
        </details>
      </details>
      <details><summary>`is_dataclass (obj)`</summary>
      </details>
      <details><summary>`itertools`</summary>
        <details><summary>`class accumulate(object)`</summary>
        </details>
        <details><summary>`class chain(object)`</summary>
          - `from_iterable = <built-in method from_iterable of type object at 0x55fa99f655e0>`
        </details>
        <details><summary>`class combinations(object)`</summary>
        </details>
        <details><summary>`class combinations_with_replacement(object)`</summary>
        </details>
        <details><summary>`class compress(object)`</summary>
        </details>
        <details><summary>`class count(object)`</summary>
        </details>
        <details><summary>`class cycle(object)`</summary>
        </details>
        <details><summary>`class dropwhile(object)`</summary>
        </details>
        <details><summary>`class filterfalse(object)`</summary>
        </details>
        <details><summary>`class groupby(object)`</summary>
        </details>
        <details><summary>`class islice(object)`</summary>
        </details>
        <details><summary>`class pairwise(object)`</summary>
        </details>
        <details><summary>`class permutations(object)`</summary>
        </details>
        <details><summary>`class product(object)`</summary>
        </details>
        <details><summary>`class repeat(object)`</summary>
        </details>
        <details><summary>`class starmap(object)`</summary>
        </details>
        <details><summary>`class takewhile(object)`</summary>
        </details>
        - `tee = <built-in function tee>`
        <details><summary>`class zip_longest(object)`</summary>
        </details>
      </details>
      <details><summary>`keyword`</summary>
        - `iskeyword = <built-in method __contains__ of frozenset object at 0x7f13fb1ebca0>`
        - `issoftkeyword = <built-in method __contains__ of frozenset object at 0x7f13fb240040>`
        - `kwlist = ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']`
        - `softkwlist = ['_', 'case', 'match']`
      </details>
      <details><summary>`make_dataclass (cls_name, fields, *, bases=(), namespace=None, init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False, match_args=True, kw_only=False, slots=False, weakref_slot=False)`</summary>
      </details>
      <details><summary>`re`</summary>
        - `A = re.ASCII`
        - `ASCII = re.ASCII`
        - `DEBUG = re.DEBUG`
        - `DOTALL = re.DOTALL`
        - `I = re.IGNORECASE`
        - `IGNORECASE = re.IGNORECASE`
        - `L = re.LOCALE`
        - `LOCALE = re.LOCALE`
        - `M = re.MULTILINE`
        - `MULTILINE = re.MULTILINE`
        <details><summary>`class Match(object)`</summary>
          - `end = <method 'end' of 're.Match' objects>`
          - `endpos = <member 'endpos' of 're.Match' objects>`
          - `expand = <method 'expand' of 're.Match' objects>`
          - `group = <method 'group' of 're.Match' objects>`
          - `groupdict = <method 'groupdict' of 're.Match' objects>`
          - `groups = <method 'groups' of 're.Match' objects>`
          - `lastgroup = <attribute 'lastgroup' of 're.Match' objects>`
          - `lastindex = <attribute 'lastindex' of 're.Match' objects>`
          - `pos = <member 'pos' of 're.Match' objects>`
          - `re = <member 're' of 're.Match' objects>`
          - `regs = <attribute 'regs' of 're.Match' objects>`
          - `span = <method 'span' of 're.Match' objects>`
          - `start = <method 'start' of 're.Match' objects>`
          - `string = <member 'string' of 're.Match' objects>`
        </details>
        - `NOFLAG = re.NOFLAG`
        <details><summary>`class Pattern(object)`</summary>
          - `findall = <method 'findall' of 're.Pattern' objects>`
          - `finditer = <method 'finditer' of 're.Pattern' objects>`
          - `flags = <member 'flags' of 're.Pattern' objects>`
          - `fullmatch = <method 'fullmatch' of 're.Pattern' objects>`
          - `groupindex = <attribute 'groupindex' of 're.Pattern' objects>`
          - `groups = <member 'groups' of 're.Pattern' objects>`
          - `match = <method 'match' of 're.Pattern' objects>`
          - `pattern = <member 'pattern' of 're.Pattern' objects>`
          - `scanner = <method 'scanner' of 're.Pattern' objects>`
          - `search = <method 'search' of 're.Pattern' objects>`
          - `split = <method 'split' of 're.Pattern' objects>`
          - `sub = <method 'sub' of 're.Pattern' objects>`
          - `subn = <method 'subn' of 're.Pattern' objects>`
        </details>
        <details><summary>`class RegexFlag(IntFlag)`</summary>
          - `ASCII = re.ASCII`
          - `DEBUG = re.DEBUG`
          - `DOTALL = re.DOTALL`
          - `IGNORECASE = re.IGNORECASE`
          - `LOCALE = re.LOCALE`
          - `MULTILINE = re.MULTILINE`
          - `TEMPLATE = re.TEMPLATE`
          - `UNICODE = re.UNICODE`
          - `VERBOSE = re.VERBOSE`
          <details><summary>`__and__ (self, other)`</summary>
          </details>
          <details><summary>`__contains__ (self, other)`</summary>
          </details>
          <details><summary>`__dir__ (self)`</summary>
          </details>
          <details><summary>`__getitem__ (name)`</summary>
          </details>
          <details><summary>`__init__ (self, *args, **kwds)`</summary>
          </details>
          <details><summary>`__invert__ (self)`</summary>
          </details>
          <details><summary>`__iter__ (self)`</summary>
          </details>
          <details><summary>`__len__ (self)`</summary>
          </details>
          <details><summary>`__new__ (cls, value)`</summary>
          </details>
          <details><summary>`__or__ (self, other)`</summary>
          </details>
          <details><summary>`__rand__ (self, other)`</summary>
          </details>
          <details><summary>`__reduce_ex__ (self, proto)`</summary>
          </details>
          <details><summary>`__repr__ (self)`</summary>
          </details>
          <details><summary>`__ror__ (self, other)`</summary>
          </details>
          <details><summary>`__rxor__ (self, other)`</summary>
          </details>
          <details><summary>`__xor__ (self, other)`</summary>
          </details>
          - `as_integer_ratio = <method 'as_integer_ratio' of 'int' objects>`
          - `bit_count = <method 'bit_count' of 'int' objects>`
          - `bit_length = <method 'bit_length' of 'int' objects>`
          - `conjugate = <method 'conjugate' of 'int' objects>`
          - `denominator = <attribute 'denominator' of 'int' objects>`
          - `from_bytes = <built-in method from_bytes of EnumType object at 0x55fa9ab5be90>`
          - `imag = <attribute 'imag' of 'int' objects>`
          - `numerator = <attribute 'numerator' of 'int' objects>`
          - `real = <attribute 'real' of 'int' objects>`
          - `to_bytes = <method 'to_bytes' of 'int' objects>`
        </details>
        - `S = re.DOTALL`
        <details><summary>`class Scanner(object)`</summary>
          <details><summary>`__init__ (self, lexicon, flags=0)`</summary>
          </details>
          <details><summary>`scan (self, string)`</summary>
          </details>
        </details>
        - `T = re.TEMPLATE`
        - `TEMPLATE = re.TEMPLATE`
        - `U = re.UNICODE`
        - `UNICODE = re.UNICODE`
        - `VERBOSE = re.VERBOSE`
        - `X = re.VERBOSE`
        <details><summary>`compile (pattern, flags=0)`</summary>
        </details>
        <details><summary>`copyreg`</summary>
        </details>
        <details><summary>`enum`</summary>
        </details>
        <details><summary>`class error(Exception)`</summary>
          <details><summary>`__init__ (self, msg, pattern=None, pos=None)`</summary>
          </details>
          - `add_note = <method 'add_note' of 'BaseException' objects>`
          - `args = <attribute 'args' of 'BaseException' objects>`
          - `with_traceback = <method 'with_traceback' of 'BaseException' objects>`
        </details>
        <details><summary>`escape (pattern)`</summary>
        </details>
        <details><summary>`findall (pattern, string, flags=0)`</summary>
        </details>
        <details><summary>`finditer (pattern, string, flags=0)`</summary>
        </details>
        <details><summary>`fullmatch (pattern, string, flags=0)`</summary>
        </details>
        <details><summary>`functools`</summary>
        </details>
        <details><summary>`match (pattern, string, flags=0)`</summary>
        </details>
        <details><summary>`purge ()`</summary>
        </details>
        <details><summary>`search (pattern, string, flags=0)`</summary>
        </details>
        <details><summary>`split (pattern, string, maxsplit=0, flags=0)`</summary>
        </details>
        <details><summary>`sub (pattern, repl, string, count=0, flags=0)`</summary>
        </details>
        <details><summary>`subn (pattern, repl, string, count=0, flags=0)`</summary>
        </details>
        <details><summary>`template (pattern, flags=0)`</summary>
        </details>
      </details>
      <details><summary>`replace (obj, /, **changes)`</summary>
      </details>
      <details><summary>`sys`</summary>
        - `abiflags = ''`
        - `addaudithook = <built-in function addaudithook>`
        - `api_version = 1013`
        - `argv = ['/home/ubuntu/corp/projects/mbodimono/toolbox/minspect/minspect/test2.py']`
        - `audit = <built-in function audit>`
        - `base_exec_prefix = '/opt/conda/envs/py11'`
        - `base_prefix = '/opt/conda/envs/py11'`
        - `breakpointhook = <built-in function breakpointhook>`
        - `builtin_module_names = ('_abc', '_ast', '_codecs', '_collections', '_functools', '_imp', '_io', '_locale', '_operator', '_signal', '_sre', '_stat', '_string', '_symtable', '_thread', '_tokenize', '_tracemalloc', '_warnings', '_weakref', 'atexit', 'builtins', 'errno', 'faulthandler', 'gc', 'itertools', 'marshal', 'posix', 'pwd', 'sys', 'time', 'xxsubtype')`
        - `byteorder = 'little'`
        - `call_tracing = <built-in function call_tracing>`
        - `copyright = 'Copyright (c) 2001-2023 Python Software Foundation.\nAll Rights Reserved.\n\nCopyright (c) 2000 BeOpen.com.\nAll Rights Reserved.\n\nCopyright (c) 1995-2001 Corporation for National Research Initiatives.\nAll Rights Reserved.\n\nCopyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.\nAll Rights Reserved.'`
        - `displayhook = <built-in function displayhook>`
        - `dont_write_bytecode = False`
        - `exc_info = <built-in function exc_info>`
        - `excepthook = <built-in function excepthook>`
        - `exception = <built-in function exception>`
        - `exec_prefix = '/opt/conda/envs/py11'`
        - `executable = '/opt/conda/envs/py11/bin/python'`
        - `exit = <built-in function exit>`
        - `flags = sys.flags(debug=0, inspect=0, interactive=0, optimize=0, dont_write_bytecode=0, no_user_site=0, no_site=0, ignore_environment=0, verbose=0, bytes_warning=0, quiet=0, hash_randomization=1, isolated=0, dev_mode=False, utf8_mode=0, warn_default_encoding=0, safe_path=False, int_max_str_digits=-1)`
        - `float_info = sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)`
        - `float_repr_style = 'short'`
        - `get_asyncgen_hooks = <built-in function get_asyncgen_hooks>`
        - `get_coroutine_origin_tracking_depth = <built-in function get_coroutine_origin_tracking_depth>`
        - `get_int_max_str_digits = <built-in function get_int_max_str_digits>`
        - `getallocatedblocks = <built-in function getallocatedblocks>`
        - `getdefaultencoding = <built-in function getdefaultencoding>`
        - `getdlopenflags = <built-in function getdlopenflags>`
        - `getfilesystemencodeerrors = <built-in function getfilesystemencodeerrors>`
        - `getfilesystemencoding = <built-in function getfilesystemencoding>`
        - `getprofile = <built-in function getprofile>`
        - `getrecursionlimit = <built-in function getrecursionlimit>`
        - `getrefcount = <built-in function getrefcount>`
        - `getsizeof = <built-in function getsizeof>`
        - `getswitchinterval = <built-in function getswitchinterval>`
        - `gettrace = <built-in function gettrace>`
        - `hash_info = sys.hash_info(width=64, modulus=2305843009213693951, inf=314159, nan=0, imag=1000003, algorithm='siphash13', hash_bits=64, seed_bits=128, cutoff=0)`
        - `hexversion = 51055088`
        - `implementation = namespace(name='cpython', cache_tag='cpython-311', version=sys.version_info(major=3, minor=11, micro=9, releaselevel='final', serial=0), hexversion=51055088, _multiarch='x86_64-linux-gnu')`
        - `int_info = sys.int_info(bits_per_digit=30, sizeof_digit=4, default_max_str_digits=4300, str_digits_check_threshold=640)`
        - `intern = <built-in function intern>`
        - `is_finalizing = <built-in function is_finalizing>`
        - `maxsize = 9223372036854775807`
        - `maxunicode = 1114111`
        - `meta_path = [<_distutils_hack.DistutilsMetaFinder object at 0x7f13fb16b050>, <class '_frozen_importlib.BuiltinImporter'>, <class '_frozen_importlib.FrozenImporter'>, <class '_frozen_importlib_external.PathFinder'>, <class '__editable___faster_whisper_server_1_0_0_finder._EditableFinder'>]`
        - `modules = {'sys': <module 'sys' (built-in)>, 'builtins': <module 'builtins' (built-in)>, '_frozen_importlib': <module '_frozen_importlib' (frozen)>, '_imp': <module '_imp' (built-in)>, '_thread': <module '_thread' (built-in)>, '_warnings': <module '_warnings' (built-in)>, '_weakref': <module '_weakref' (built-in)>, '_io': <module '_io' (built-in)>, 'marshal': <module 'marshal' (built-in)>, 'posix': <module 'posix' (built-in)>, '_frozen_importlib_external': <module '_frozen_importlib_external' (frozen)>, 'time': <module 'time' (built-in)>, 'zipimport': <module 'zipimport' (frozen)>, '_codecs': <module '_codecs' (built-in)>, 'codecs': <module 'codecs' (frozen)>, 'encodings.aliases': <module 'encodings.aliases' from '/opt/conda/envs/py11/lib/python3.11/encodings/aliases.py'>, 'encodings': <module 'encodings' from '/opt/conda/envs/py11/lib/python3.11/encodings/__init__.py'>, 'encodings.utf_8': <module 'encodings.utf_8' from '/opt/conda/envs/py11/lib/python3.11/encodings/utf_8.py'>, '_signal': <module '_signal' (built-in)>, '_abc': <module '_abc' (built-in)>, 'abc': <module 'abc' (frozen)>, 'io': <module 'io' (frozen)>, '__main__': <module '__main__' from '/home/ubuntu/corp/projects/mbodimono/toolbox/minspect/minspect/test2.py'>, '_stat': <module '_stat' (built-in)>, 'stat': <module 'stat' (frozen)>, '_collections_abc': <module '_collections_abc' (frozen)>, 'genericpath': <module 'genericpath' (frozen)>, 'posixpath': <module 'posixpath' (frozen)>, 'os.path': <module 'posixpath' (frozen)>, 'os': <module 'os' (frozen)>, '_sitebuiltins': <module '_sitebuiltins' (frozen)>, '__future__': <module '__future__' from '/opt/conda/envs/py11/lib/python3.11/__future__.py'>, 'importlib._bootstrap': <module '_frozen_importlib' (frozen)>, 'importlib._bootstrap_external': <module '_frozen_importlib_external' (frozen)>, 'warnings': <module 'warnings' from '/opt/conda/envs/py11/lib/python3.11/warnings.py'>, 'importlib': <module 'importlib' from '/opt/conda/envs/py11/lib/python3.11/importlib/__init__.py'>, 'importlib.machinery': <module 'importlib.machinery' (frozen)>, 'importlib._abc': <module 'importlib._abc' from '/opt/conda/envs/py11/lib/python3.11/importlib/_abc.py'>, 'itertools': <module 'itertools' (built-in)>, 'keyword': <module 'keyword' from '/opt/conda/envs/py11/lib/python3.11/keyword.py'>, '_operator': <module '_operator' (built-in)>, 'operator': <module 'operator' from '/opt/conda/envs/py11/lib/python3.11/operator.py'>, 'reprlib': <module 'reprlib' from '/opt/conda/envs/py11/lib/python3.11/reprlib.py'>, '_collections': <module '_collections' (built-in)>, 'collections': <module 'collections' from '/opt/conda/envs/py11/lib/python3.11/collections/__init__.py'>, 'types': <module 'types' from '/opt/conda/envs/py11/lib/python3.11/types.py'>, '_functools': <module '_functools' (built-in)>, 'functools': <module 'functools' from '/opt/conda/envs/py11/lib/python3.11/functools.py'>, 'contextlib': <module 'contextlib' from '/opt/conda/envs/py11/lib/python3.11/contextlib.py'>, '_weakrefset': <module '_weakrefset' from '/opt/conda/envs/py11/lib/python3.11/_weakrefset.py'>, 'threading': <module 'threading' from '/opt/conda/envs/py11/lib/python3.11/threading.py'>, 'importlib.util': <module 'importlib.util' (frozen)>, 'enum': <module 'enum' from '/opt/conda/envs/py11/lib/python3.11/enum.py'>, '_sre': <module '_sre' (built-in)>, 're._constants': <module 're._constants' from '/opt/conda/envs/py11/lib/python3.11/re/_constants.py'>, 're._parser': <module 're._parser' from '/opt/conda/envs/py11/lib/python3.11/re/_parser.py'>, 're._casefix': <module 're._casefix' from '/opt/conda/envs/py11/lib/python3.11/re/_casefix.py'>, 're._compiler': <module 're._compiler' from '/opt/conda/envs/py11/lib/python3.11/re/_compiler.py'>, 'copyreg': <module 'copyreg' from '/opt/conda/envs/py11/lib/python3.11/copyreg.py'>, 're': <module 're' from '/opt/conda/envs/py11/lib/python3.11/re/__init__.py'>, 'fnmatch': <module 'fnmatch' from '/opt/conda/envs/py11/lib/python3.11/fnmatch.py'>, 'ntpath': <module 'ntpath' (frozen)>, 'errno': <module 'errno' (built-in)>, 'urllib': <module 'urllib' from '/opt/conda/envs/py11/lib/python3.11/urllib/__init__.py'>, 'ipaddress': <module 'ipaddress' from '/opt/conda/envs/py11/lib/python3.11/ipaddress.py'>, 'urllib.parse': <module 'urllib.parse' from '/opt/conda/envs/py11/lib/python3.11/urllib/parse.py'>, 'pathlib': <module 'pathlib' from '/opt/conda/envs/py11/lib/python3.11/pathlib.py'>, '__editable___faster_whisper_server_1_0_0_finder': <module '__editable___faster_whisper_server_1_0_0_finder' from '/opt/conda/envs/py11/lib/python3.11/site-packages/__editable___faster_whisper_server_1_0_0_finder.py'>, '_distutils_hack': <module '_distutils_hack' from '/opt/conda/envs/py11/lib/python3.11/site-packages/_distutils_hack/__init__.py'>, 'pyannote': <module 'pyannote' (<_frozen_importlib_external.NamespaceLoader object at 0x7f13fb16b3d0>)>, 'sphinxcontrib': <module 'sphinxcontrib' (<_frozen_importlib_external.NamespaceLoader object at 0x7f13fb16b790>)>, 'site': <module 'site' (frozen)>, '_ast': <module '_ast' (built-in)>, 'collections.abc': <module 'collections.abc' from '/opt/conda/envs/py11/lib/python3.11/collections/abc.py'>, '_typing': <module '_typing' from '/opt/conda/envs/py11/lib/python3.11/lib-dynload/_typing.cpython-311-x86_64-linux-gnu.so'>, 'typing.io': <class 'typing.io'>, 'typing.re': <class 'typing.re'>, 'typing': <module 'typing' from '/opt/conda/envs/py11/lib/python3.11/typing.py'>, 'ast': <module 'ast' from '/opt/conda/envs/py11/lib/python3.11/ast.py'>, '_opcode': <module '_opcode' from '/opt/conda/envs/py11/lib/python3.11/lib-dynload/_opcode.cpython-311-x86_64-linux-gnu.so'>, 'opcode': <module 'opcode' from '/opt/conda/envs/py11/lib/python3.11/opcode.py'>, 'dis': <module 'dis' from '/opt/conda/envs/py11/lib/python3.11/dis.py'>, 'token': <module 'token' from '/opt/conda/envs/py11/lib/python3.11/token.py'>, 'tokenize': <module 'tokenize' from '/opt/conda/envs/py11/lib/python3.11/tokenize.py'>, 'linecache': <module 'linecache' from '/opt/conda/envs/py11/lib/python3.11/linecache.py'>, 'inspect': <module 'inspect' from '/opt/conda/envs/py11/lib/python3.11/inspect.py'>, 'pydantic.version': <module 'pydantic.version' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/version.py'>, 'pydantic._migration': <module 'pydantic._migration' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_migration.py'>, '_socket': <module '_socket' from '/opt/conda/envs/py11/lib/python3.11/lib-dynload/_socket.cpython-311-x86_64-linux-gnu.so'>, 'typing_extensions': <module 'typing_extensions' from '/opt/conda/envs/py11/lib/python3.11/site-packages/typing_extensions.py'>, 'pydantic.errors': <module 'pydantic.errors' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/errors.py'>, 'pydantic': <module 'pydantic' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/__init__.py'>, 'weakref': <module 'weakref' from '/opt/conda/envs/py11/lib/python3.11/weakref.py'>, 'copy': <module 'copy' from '/opt/conda/envs/py11/lib/python3.11/copy.py'>, 'dataclasses': <module 'dataclasses' from '/opt/conda/envs/py11/lib/python3.11/dataclasses.py'>, 'math': <module 'math' from '/opt/conda/envs/py11/lib/python3.11/lib-dynload/math.cpython-311-x86_64-linux-gnu.so'>, '_datetime': <module '_datetime' from '/opt/conda/envs/py11/lib/python3.11/lib-dynload/_datetime.cpython-311-x86_64-linux-gnu.so'>, 'datetime': <module 'datetime' from '/opt/conda/envs/py11/lib/python3.11/datetime.py'>, 'pydantic_core._pydantic_core': <module 'pydantic_core._pydantic_core' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic_core/_pydantic_core.cpython-311-x86_64-linux-gnu.so'>, 'numbers': <module 'numbers' from '/opt/conda/envs/py11/lib/python3.11/numbers.py'>, '_decimal': <module '_decimal' from '/opt/conda/envs/py11/lib/python3.11/lib-dynload/_decimal.cpython-311-x86_64-linux-gnu.so'>, 'decimal': <module 'decimal' from '/opt/conda/envs/py11/lib/python3.11/decimal.py'>, 'pydantic_core.core_schema': <module 'pydantic_core.core_schema' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic_core/core_schema.py'>, 'pydantic_core': <module 'pydantic_core' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic_core/__init__.py'>, 'pydantic._internal': <module 'pydantic._internal' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal/__init__.py'>, 'pydantic._internal._core_metadata': <module 'pydantic._internal._core_metadata' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal/_core_metadata.py'>, 'sysconfig': <module 'sysconfig' from '/opt/conda/envs/py11/lib/python3.11/sysconfig.py'>, '_sysconfigdata__linux_x86_64-linux-gnu': <module '_sysconfigdata__linux_x86_64-linux-gnu' from '/opt/conda/envs/py11/lib/python3.11/_sysconfigdata__linux_x86_64-linux-gnu.py'>, 'zoneinfo._tzpath': <module 'zoneinfo._tzpath' from '/opt/conda/envs/py11/lib/python3.11/zoneinfo/_tzpath.py'>, '_struct': <module '_struct' from '/opt/conda/envs/py11/lib/python3.11/lib-dynload/_struct.cpython-311-x86_64-linux-gnu.so'>, 'struct': <module 'struct' from '/opt/conda/envs/py11/lib/python3.11/struct.py'>, 'zoneinfo._common': <module 'zoneinfo._common' from '/opt/conda/envs/py11/lib/python3.11/zoneinfo/_common.py'>, '_zoneinfo': <module '_zoneinfo' from '/opt/conda/envs/py11/lib/python3.11/lib-dynload/_zoneinfo.cpython-311-x86_64-linux-gnu.so'>, 'zoneinfo': <module 'zoneinfo' from '/opt/conda/envs/py11/lib/python3.11/zoneinfo/__init__.py'>, 'pydantic._internal._typing_extra': <module 'pydantic._internal._typing_extra' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal/_typing_extra.py'>, 'pydantic._internal._repr': <module 'pydantic._internal._repr' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal/_repr.py'>, 'pydantic._internal._core_utils': <module 'pydantic._internal._core_utils' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal/_core_utils.py'>, 'pydantic._internal._internal_dataclass': <module 'pydantic._internal._internal_dataclass' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal/_internal_dataclass.py'>, 'pydantic._internal._decorators': <module 'pydantic._internal._decorators' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal/_decorators.py'>, '_contextvars': <module '_contextvars' from '/opt/conda/envs/py11/lib/python3.11/lib-dynload/_contextvars.cpython-311-x86_64-linux-gnu.so'>, 'contextvars': <module 'contextvars' from '/opt/conda/envs/py11/lib/python3.11/contextvars.py'>, 'pydantic._internal._forward_ref': <module 'pydantic._internal._forward_ref' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal/_forward_ref.py'>, 'pydantic._internal._import_utils': <module 'pydantic._internal._import_utils' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal/_import_utils.py'>, 'pydantic._internal._utils': <module 'pydantic._internal._utils' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal/_utils.py'>, 'pydantic._internal._generics': <module 'pydantic._internal._generics' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal/_generics.py'>, 'pydantic.annotated_handlers': <module 'pydantic.annotated_handlers' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/annotated_handlers.py'>, 'pydantic.functional_validators': <module 'pydantic.functional_validators' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/functional_validators.py'>, 'pydantic.aliases': <module 'pydantic.aliases' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/aliases.py'>, 'binascii': <module 'binascii' from '/opt/conda/envs/py11/lib/python3.11/lib-dynload/binascii.cpython-311-x86_64-linux-gnu.so'>, 'base64': <module 'base64' from '/opt/conda/envs/py11/lib/python3.11/base64.py'>, 'platform': <module 'platform' from '/opt/conda/envs/py11/lib/python3.11/platform.py'>, '_uuid': <module '_uuid' from '/opt/conda/envs/py11/lib/python3.11/lib-dynload/_uuid.cpython-311-x86_64-linux-gnu.so'>, 'uuid': <module 'uuid' from '/opt/conda/envs/py11/lib/python3.11/uuid.py'>, 'annotated_types': <module 'annotated_types' from '/opt/conda/envs/py11/lib/python3.11/site-packages/annotated_types/__init__.py'>, 'pydantic.config': <module 'pydantic.config' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/config.py'>, 'pydantic.warnings': <module 'pydantic.warnings' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/warnings.py'>, 'pydantic._internal._config': <module 'pydantic._internal._config' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal/_config.py'>, 'textwrap': <module 'textwrap' from '/opt/conda/envs/py11/lib/python3.11/textwrap.py'>, 'pydantic._internal._docs_extraction': <module 'pydantic._internal._docs_extraction' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal/_docs_extraction.py'>, 'pydantic._internal._fields': <module 'pydantic._internal._fields' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal/_fields.py'>, 'pydantic._internal._validators': <module 'pydantic._internal._validators' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal/_validators.py'>, 'pydantic.plugin': <module 'pydantic.plugin' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/plugin/__init__.py'>, 'pydantic.plugin._schema_validator': <module 'pydantic.plugin._schema_validator' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/plugin/_schema_validator.py'>, 'pydantic._internal._mock_val_ser': <module 'pydantic._internal._mock_val_ser' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal/_mock_val_ser.py'>, 'pydantic._internal._schema_generation_shared': <module 'pydantic._internal._schema_generation_shared' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal/_schema_generation_shared.py'>, 'pydantic.json_schema': <module 'pydantic.json_schema' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/json_schema.py'>, 'pydantic.types': <module 'pydantic.types' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/types.py'>, '_csv': <module '_csv' from '/opt/conda/envs/py11/lib/python3.11/lib-dynload/_csv.cpython-311-x86_64-linux-gnu.so'>, 'csv': <module 'csv' from '/opt/conda/envs/py11/lib/python3.11/csv.py'>, 'email': <module 'email' from '/opt/conda/envs/py11/lib/python3.11/email/__init__.py'>, 'zlib': <module 'zlib' from '/opt/conda/envs/py11/lib/python3.11/lib-dynload/zlib.cpython-311-x86_64-linux-gnu.so'>, '_compression': <module '_compression' from '/opt/conda/envs/py11/lib/python3.11/_compression.py'>, '_bz2': <module '_bz2' from '/opt/conda/envs/py11/lib/python3.11/lib-dynload/_bz2.cpython-311-x86_64-linux-gnu.so'>, 'bz2': <module 'bz2' from '/opt/conda/envs/py11/lib/python3.11/bz2.py'>, '_lzma': <module '_lzma' from '/opt/conda/envs/py11/lib/python3.11/lib-dynload/_lzma.cpython-311-x86_64-linux-gnu.so'>, 'lzma': <module 'lzma' from '/opt/conda/envs/py11/lib/python3.11/lzma.py'>, 'shutil': <module 'shutil' from '/opt/conda/envs/py11/lib/python3.11/shutil.py'>, 'zipfile': <module 'zipfile' from '/opt/conda/envs/py11/lib/python3.11/zipfile.py'>, 'quopri': <module 'quopri' from '/opt/conda/envs/py11/lib/python3.11/quopri.py'>, '_bisect': <module '_bisect' from '/opt/conda/envs/py11/lib/python3.11/lib-dynload/_bisect.cpython-311-x86_64-linux-gnu.so'>, 'bisect': <module 'bisect' from '/opt/conda/envs/py11/lib/python3.11/bisect.py'>, '_random': <module '_random' from '/opt/conda/envs/py11/lib/python3.11/lib-dynload/_random.cpython-311-x86_64-linux-gnu.so'>, '_sha512': <module '_sha512' from '/opt/conda/envs/py11/lib/python3.11/lib-dynload/_sha512.cpython-311-x86_64-linux-gnu.so'>, 'random': <module 'random' from '/opt/conda/envs/py11/lib/python3.11/random.py'>, 'select': <module 'select' from '/opt/conda/envs/py11/lib/python3.11/lib-dynload/select.cpython-311-x86_64-linux-gnu.so'>, 'selectors': <module 'selectors' from '/opt/conda/envs/py11/lib/python3.11/selectors.py'>, 'array': <module 'array' from '/opt/conda/envs/py11/lib/python3.11/lib-dynload/array.cpython-311-x86_64-linux-gnu.so'>, 'socket': <module 'socket' from '/opt/conda/envs/py11/lib/python3.11/socket.py'>, '_locale': <module '_locale' (built-in)>, 'locale': <module 'locale' from '/opt/conda/envs/py11/lib/python3.11/locale.py'>, 'calendar': <module 'calendar' from '/opt/conda/envs/py11/lib/python3.11/calendar.py'>, 'email._parseaddr': <module 'email._parseaddr' from '/opt/conda/envs/py11/lib/python3.11/email/_parseaddr.py'>, 'email.base64mime': <module 'email.base64mime' from '/opt/conda/envs/py11/lib/python3.11/email/base64mime.py'>, '_string': <module '_string' (built-in)>, 'string': <module 'string' from '/opt/conda/envs/py11/lib/python3.11/string.py'>, 'email.quoprimime': <module 'email.quoprimime' from '/opt/conda/envs/py11/lib/python3.11/email/quoprimime.py'>, 'email.errors': <module 'email.errors' from '/opt/conda/envs/py11/lib/python3.11/email/errors.py'>, 'email.encoders': <module 'email.encoders' from '/opt/conda/envs/py11/lib/python3.11/email/encoders.py'>, 'email.charset': <module 'email.charset' from '/opt/conda/envs/py11/lib/python3.11/email/charset.py'>, 'email.utils': <module 'email.utils' from '/opt/conda/envs/py11/lib/python3.11/email/utils.py'>, 'email.header': <module 'email.header' from '/opt/conda/envs/py11/lib/python3.11/email/header.py'>, 'email._policybase': <module 'email._policybase' from '/opt/conda/envs/py11/lib/python3.11/email/_policybase.py'>, 'email._encoded_words': <module 'email._encoded_words' from '/opt/conda/envs/py11/lib/python3.11/email/_encoded_words.py'>, 'email.iterators': <module 'email.iterators' from '/opt/conda/envs/py11/lib/python3.11/email/iterators.py'>, 'email.message': <module 'email.message' from '/opt/conda/envs/py11/lib/python3.11/email/message.py'>, 'importlib.metadata._functools': <module 'importlib.metadata._functools' from '/opt/conda/envs/py11/lib/python3.11/importlib/metadata/_functools.py'>, 'importlib.metadata._text': <module 'importlib.metadata._text' from '/opt/conda/envs/py11/lib/python3.11/importlib/metadata/_text.py'>, 'importlib.metadata._adapters': <module 'importlib.metadata._adapters' from '/opt/conda/envs/py11/lib/python3.11/importlib/metadata/_adapters.py'>, 'importlib.metadata._meta': <module 'importlib.metadata._meta' from '/opt/conda/envs/py11/lib/python3.11/importlib/metadata/_meta.py'>, 'importlib.metadata._collections': <module 'importlib.metadata._collections' from '/opt/conda/envs/py11/lib/python3.11/importlib/metadata/_collections.py'>, 'importlib.metadata._itertools': <module 'importlib.metadata._itertools' from '/opt/conda/envs/py11/lib/python3.11/importlib/metadata/_itertools.py'>, 'tempfile': <module 'tempfile' from '/opt/conda/envs/py11/lib/python3.11/tempfile.py'>, 'importlib.resources.abc': <module 'importlib.resources.abc' from '/opt/conda/envs/py11/lib/python3.11/importlib/resources/abc.py'>, 'importlib.resources._adapters': <module 'importlib.resources._adapters' from '/opt/conda/envs/py11/lib/python3.11/importlib/resources/_adapters.py'>, 'importlib.resources._common': <module 'importlib.resources._common' from '/opt/conda/envs/py11/lib/python3.11/importlib/resources/_common.py'>, 'importlib.resources._legacy': <module 'importlib.resources._legacy' from '/opt/conda/envs/py11/lib/python3.11/importlib/resources/_legacy.py'>, 'importlib.resources': <module 'importlib.resources' from '/opt/conda/envs/py11/lib/python3.11/importlib/resources/__init__.py'>, 'importlib.abc': <module 'importlib.abc' from '/opt/conda/envs/py11/lib/python3.11/importlib/abc.py'>, 'importlib.metadata': <module 'importlib.metadata' from '/opt/conda/envs/py11/lib/python3.11/importlib/metadata/__init__.py'>, 'pydantic.networks': <module 'pydantic.networks' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/networks.py'>, 'pydantic.deprecated': <module 'pydantic.deprecated' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/deprecated/__init__.py'>, 'pydantic.deprecated.config': <module 'pydantic.deprecated.config' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/deprecated/config.py'>, 'pydantic._internal._discriminated_union': <module 'pydantic._internal._discriminated_union' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal/_discriminated_union.py'>, 'pydantic._internal._known_annotated_metadata': <module 'pydantic._internal._known_annotated_metadata' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal/_known_annotated_metadata.py'>, 'pydantic._internal._generate_schema': <module 'pydantic._internal._generate_schema' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal/_generate_schema.py'>, 'pydantic._internal._signature': <module 'pydantic._internal._signature' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal/_signature.py'>, 'pydantic._internal._validate_call': <module 'pydantic._internal._validate_call' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal/_validate_call.py'>, 'pydantic._internal._model_construction': <module 'pydantic._internal._model_construction' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal/_model_construction.py'>, 'pydantic.main': <module 'pydantic.main' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/main.py'>, 'pydantic.fields': <module 'pydantic.fields' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/fields.py'>, 'pydantic.functional_serializers': <module 'pydantic.functional_serializers' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/functional_serializers.py'>, 'pydantic._internal._serializers': <module 'pydantic._internal._serializers' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal/_serializers.py'>, 'pydantic._internal._std_types_schema': <module 'pydantic._internal._std_types_schema' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal/_std_types_schema.py'>, 'pydantic.plugin._loader': <module 'pydantic.plugin._loader' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/plugin/_loader.py'>, 'pydantic.root_model': <module 'pydantic.root_model' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/root_model.py'>, 'pydantic.type_adapter': <module 'pydantic.type_adapter' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/type_adapter.py'>, 'pydantic._internal._dataclasses': <module 'pydantic._internal._dataclasses' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal/_dataclasses.py'>, 'pydantic.dataclasses': <module 'pydantic.dataclasses' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/dataclasses.py'>}`
        - `orig_argv = ['/opt/conda/envs/py11/bin/python', '/home/ubuntu/corp/projects/mbodimono/toolbox/minspect/minspect/test2.py']`
        - `path = ['/home/ubuntu/corp/projects/mbodimono/toolbox/minspect/minspect', '/opt/conda/envs/py11/lib/python311.zip', '/opt/conda/envs/py11/lib/python3.11', '/opt/conda/envs/py11/lib/python3.11/lib-dynload', '/opt/conda/envs/py11/lib/python3.11/site-packages', '__editable__.faster_whisper_server-1.0.0.finder.__path_hook__', '/home/ubuntu/corp/projects/mbodimono/embodied-agents', '/home/ubuntu/corp/projects/mbodimono/toolbox/minspect']`
        - `path_hooks = [<class 'zipimport.zipimporter'>, <function FileFinder.path_hook.<locals>.path_hook_for_FileFinder at 0x7f13fb3d82c0>, <bound method _EditableNamespaceFinder._path_hook of <class '__editable___faster_whisper_server_1_0_0_finder._EditableNamespaceFinder'>>]`
        - `path_importer_cache = {'/opt/conda/envs/py11/lib/python311.zip': None, '/opt/conda/envs/py11/lib/python3.11': FileFinder('/opt/conda/envs/py11/lib/python3.11'), '/opt/conda/envs/py11/lib/python3.11/encodings': FileFinder('/opt/conda/envs/py11/lib/python3.11/encodings'), '/opt/conda/envs/py11/lib/python3.11/lib-dynload': FileFinder('/opt/conda/envs/py11/lib/python3.11/lib-dynload'), '/opt/conda/envs/py11/lib/python3.11/site-packages': FileFinder('/opt/conda/envs/py11/lib/python3.11/site-packages'), '/opt/conda/envs/py11/lib/python3.11/importlib': FileFinder('/opt/conda/envs/py11/lib/python3.11/importlib'), '/opt/conda/envs/py11/lib/python3.11/re': FileFinder('/opt/conda/envs/py11/lib/python3.11/re'), '/opt/conda/envs/py11/lib/python3.11/urllib': FileFinder('/opt/conda/envs/py11/lib/python3.11/urllib'), '__editable__.faster_whisper_server-1.0.0.finder.__path_hook__': <class '__editable___faster_whisper_server_1_0_0_finder._EditableNamespaceFinder'>, '/home/ubuntu/corp/projects/mbodimono/embodied-agents': FileFinder('/home/ubuntu/corp/projects/mbodimono/embodied-agents'), '/home/ubuntu/corp/projects/mbodimono/toolbox/minspect': FileFinder('/home/ubuntu/corp/projects/mbodimono/toolbox/minspect'), '/home/ubuntu/corp/projects/mbodimono/toolbox/minspect/minspect/test2.py': None, '/home/ubuntu/corp/projects/mbodimono/toolbox/minspect/minspect': FileFinder('/home/ubuntu/corp/projects/mbodimono/toolbox/minspect/minspect'), '/opt/conda/envs/py11/lib/python3.11/collections': FileFinder('/opt/conda/envs/py11/lib/python3.11/collections'), '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic': FileFinder('/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic'), '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic_core': FileFinder('/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic_core'), '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal': FileFinder('/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal'), '/opt/conda/envs/py11/lib/python3.11/zoneinfo': FileFinder('/opt/conda/envs/py11/lib/python3.11/zoneinfo'), '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/plugin': FileFinder('/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/plugin'), '/opt/conda/envs/py11/lib/python3.11/importlib/metadata': FileFinder('/opt/conda/envs/py11/lib/python3.11/importlib/metadata'), '/opt/conda/envs/py11/lib/python3.11/email': FileFinder('/opt/conda/envs/py11/lib/python3.11/email'), '/opt/conda/envs/py11/lib/python3.11/importlib/resources': FileFinder('/opt/conda/envs/py11/lib/python3.11/importlib/resources'), '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/deprecated': FileFinder('/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/deprecated')}`
        - `platform = 'linux'`
        - `platlibdir = 'lib'`
        - `prefix = '/opt/conda/envs/py11'`
        - `pycache_prefix = None`
        - `set_asyncgen_hooks = <built-in function set_asyncgen_hooks>`
        - `set_coroutine_origin_tracking_depth = <built-in function set_coroutine_origin_tracking_depth>`
        - `set_int_max_str_digits = <built-in function set_int_max_str_digits>`
        - `setdlopenflags = <built-in function setdlopenflags>`
        - `setprofile = <built-in function setprofile>`
        - `setrecursionlimit = <built-in function setrecursionlimit>`
        - `setswitchinterval = <built-in function setswitchinterval>`
        - `settrace = <built-in function settrace>`
        - `stderr = <_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>`
        - `stdin = <_io.TextIOWrapper name='<stdin>' mode='r' encoding='utf-8'>`
        - `stdlib_module_names = frozenset({'contextlib', 'turtledemo', 'numbers', 'select', 'unittest', 'errno', 'base64', 'fractions', 'plistlib', '_compression', 'wsgiref', '_strptime', 'readline', '_tracemalloc', 'zipfile', '_crypt', '_markupbase', '_string', 'ctypes', 'cProfile', 'chunk', 'platform', 'importlib', 'sched', 'abc', '_datetime', '_uuid', 'datetime', '_zoneinfo', 'shlex', 'symtable', 'trace', 'imaplib', 'mmap', 'bz2', 'typing', 'fnmatch', 'compileall', 'imghdr', 'codeop', '_lzma', '_py_abc', 'resource', 'bisect', '_json', 'sre_parse', 'faulthandler', 'ssl', 'tempfile', 'traceback', 'tracemalloc', 'wave', 'xdrlib', '_codecs_hk', '_posixsubprocess', 'aifc', 'argparse', 'asyncio', 'asyncore', 'zoneinfo', '_io', '_random', 'bdb', 'cmd', 'fileinput', 'heapq', '_aix_support', 'copyreg', 'dbm', 'pydoc', 'tty', 'tomllib', 'filecmp', 'doctest', 'nis', '__future__', 'smtplib', '_csv', 'grp', 'curses', 'signal', '_sre', 'quopri', 'audioop', '_codecs_tw', '_ctypes', 'graphlib', 'math', 'string', '_dbm', 'zlib', 'contextvars', '_frozen_importlib_external', 'ntpath', 'spwd', '_codecs_kr', 'builtins', 'decimal', 'smtpd', 'mimetypes', '_warnings', 'socket', '_gdbm', '_multibytecodec', '_functools', '_weakrefset', '_thread', '_struct', 'code', '_ssl', 'dataclasses', 'collections', 'copy', '_statistics', 'poplib', '_pickle', 'tarfile', 'itertools', '_collections', 'genericpath', 'shutil', 'lzma', '_sitebuiltins', '_compat_pickle', '_curses_panel', 'enum', 'concurrent', 'gettext', '_imp', 'runpy', 'msilib', '_tokenize', 'locale', 'venv', '_collections_abc', '_osx_support', 'binascii', 'gzip', '_sha512', 'ipaddress', 'ossaudiodev', 'getpass', 'configparser', '_stat', 'ensurepip', 'hashlib', 'pkgutil', 'modulefinder', '_overlapped', '_multiprocessing', 'token', '_lsprof', 'msvcrt', 'multiprocessing', '_pyio', 'ast', 'glob', 'posix', 'tabnanny', 'xml', 'posixpath', '_hashlib', 'os', 'pdb', 'keyword', 'linecache', 'pathlib', 'tkinter', 'pprint', 'turtle', 'gc', 'shelve', 'telnetlib', 'winreg', '_md5', 'antigravity', 'subprocess', 'xmlrpc', 'opcode', 'unicodedata', 'pydoc_data', 'nt', 'timeit', '_weakref', 'textwrap', '_sha1', 'mailcap', '_asyncio', 'pickletools', 'zipimport', 'cmath', 'ftplib', '_blake2', 'asynchat', 'logging', 're', 'tokenize', '_symtable', 'uu', 'termios', '_signal', 'nturl2path', 'reprlib', 'json', 'site', 'sqlite3', '_msi', 'uuid', 'cgi', 'urllib', 'winsound', 'csv', 'marshal', 'this', 'zipapp', 'weakref', '_codecs_jp', 'netrc', 'crypt', 'struct', 'operator', 'email', 'io', 'encodings', 'queue', 'inspect', 'http', 'syslog', '_codecs_cn', '_bz2', 'random', 'secrets', 'idlelib', 'profile', 'pty', 'functools', 'sre_compile', 'sre_constants', 'pickle', 'getopt', '_sha3', '_sqlite3', '_heapq', 'sunau', '_winapi', '_threading_local', '_pydecimal', '_scproxy', 'calendar', 'codecs', 'distutils', 'sysconfig', '_elementtree', 'stat', 'nntplib', 'atexit', 'pwd', 'sndhdr', '_bootsubprocess', 'dis', 'fcntl', 'pyclbr', 'pyexpat', '_codecs', 'stringprep', '_frozen_importlib', 'types', 'mailbox', 'optparse', 'time', 'colorsys', 'socketserver', 'webbrowser', '_operator', 'difflib', 'py_compile', '_decimal', '_codecs_iso2022', 'hmac', 'array', 'threading', '_opcode', '_ast', 'selectors', '_curses', '_socket', 'html', 'warnings', '_bisect', '_contextvars', '_locale', 'pipes', 'cgitb', 'pstats', '_tkinter', '_abc', 'lib2to3', '_typing', '_sha256', '_posixshmem', 'rlcompleter', 'sys', 'statistics', 'imp', '_queue'})`
        - `stdout = <_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>`
        - `thread_info = sys.thread_info(name='pthread', lock='semaphore', version='NPTL 2.31')`
        - `unraisablehook = <built-in function unraisablehook>`
        - `version = '3.11.9 | packaged by conda-forge | (main, Apr 19 2024, 18:36:13) [GCC 12.3.0]'`
        - `version_info = sys.version_info(major=3, minor=11, micro=9, releaselevel='final', serial=0)`
        - `warnoptions = []`
      </details>
      <details><summary>`types`</summary>
        <details><summary>`class async_generator(object)`</summary>
          - `aclose = <method 'aclose' of 'async_generator' objects>`
          - `ag_await = <attribute 'ag_await' of 'async_generator' objects>`
          - `ag_code = <member 'ag_code' of 'async_generator' objects>`
          - `ag_frame = <attribute 'ag_frame' of 'async_generator' objects>`
          - `ag_running = <member 'ag_running' of 'async_generator' objects>`
          - `asend = <method 'asend' of 'async_generator' objects>`
          - `athrow = <method 'athrow' of 'async_generator' objects>`
        </details>
        <details><summary>`class builtin_function_or_method(object)`</summary>
        </details>
        <details><summary>`class builtin_function_or_method(object)`</summary>
        </details>
        <details><summary>`class cell(object)`</summary>
          - `cell_contents = <attribute 'cell_contents' of 'cell' objects>`
        </details>
        <details><summary>`class classmethod_descriptor(object)`</summary>
        </details>
        <details><summary>`class code(object)`</summary>
          - `co_argcount = <member 'co_argcount' of 'code' objects>`
          - `co_cellvars = <attribute 'co_cellvars' of 'code' objects>`
          - `co_code = <attribute 'co_code' of 'code' objects>`
          - `co_consts = <member 'co_consts' of 'code' objects>`
          - `co_exceptiontable = <member 'co_exceptiontable' of 'code' objects>`
          - `co_filename = <member 'co_filename' of 'code' objects>`
          - `co_firstlineno = <member 'co_firstlineno' of 'code' objects>`
          - `co_flags = <member 'co_flags' of 'code' objects>`
          - `co_freevars = <attribute 'co_freevars' of 'code' objects>`
          - `co_kwonlyargcount = <member 'co_kwonlyargcount' of 'code' objects>`
          - `co_lines = <method 'co_lines' of 'code' objects>`
          - `co_linetable = <member 'co_linetable' of 'code' objects>`
          - `co_lnotab = <attribute 'co_lnotab' of 'code' objects>`
          - `co_name = <member 'co_name' of 'code' objects>`
          - `co_names = <member 'co_names' of 'code' objects>`
          - `co_nlocals = <member 'co_nlocals' of 'code' objects>`
          - `co_positions = <method 'co_positions' of 'code' objects>`
          - `co_posonlyargcount = <member 'co_posonlyargcount' of 'code' objects>`
          - `co_qualname = <member 'co_qualname' of 'code' objects>`
          - `co_stacksize = <member 'co_stacksize' of 'code' objects>`
          - `co_varnames = <attribute 'co_varnames' of 'code' objects>`
          - `replace = <method 'replace' of 'code' objects>`
        </details>
        <details><summary>`class coroutine(object)`</summary>
          - `close = <method 'close' of 'coroutine' objects>`
          - `cr_await = <attribute 'cr_await' of 'coroutine' objects>`
          - `cr_code = <member 'cr_code' of 'coroutine' objects>`
          - `cr_frame = <attribute 'cr_frame' of 'coroutine' objects>`
          - `cr_origin = <member 'cr_origin' of 'coroutine' objects>`
          - `cr_running = <attribute 'cr_running' of 'coroutine' objects>`
          - `cr_suspended = <attribute 'cr_suspended' of 'coroutine' objects>`
          - `send = <method 'send' of 'coroutine' objects>`
          - `throw = <method 'throw' of 'coroutine' objects>`
        </details>
        <details><summary>`class DynamicClassAttribute(object)`</summary>
          <details><summary>`__delete__ (self, instance)`</summary>
          </details>
          <details><summary>`__get__ (self, instance, ownerclass=None)`</summary>
          </details>
          <details><summary>`__init__ (self, fget=None, fset=None, fdel=None, doc=None)`</summary>
          </details>
          <details><summary>`__set__ (self, instance, value)`</summary>
          </details>
          <details><summary>`deleter (self, fdel)`</summary>
          </details>
          <details><summary>`getter (self, fget)`</summary>
          </details>
          <details><summary>`setter (self, fset)`</summary>
          </details>
        </details>
        <details><summary>`class ellipsis(object)`</summary>
        </details>
        <details><summary>`class frame(object)`</summary>
          - `clear = <method 'clear' of 'frame' objects>`
          - `f_back = <attribute 'f_back' of 'frame' objects>`
          - `f_builtins = <attribute 'f_builtins' of 'frame' objects>`
          - `f_code = <attribute 'f_code' of 'frame' objects>`
          - `f_globals = <attribute 'f_globals' of 'frame' objects>`
          - `f_lasti = <attribute 'f_lasti' of 'frame' objects>`
          - `f_lineno = <attribute 'f_lineno' of 'frame' objects>`
          - `f_locals = <attribute 'f_locals' of 'frame' objects>`
          - `f_trace = <attribute 'f_trace' of 'frame' objects>`
          - `f_trace_lines = <member 'f_trace_lines' of 'frame' objects>`
          - `f_trace_opcodes = <member 'f_trace_opcodes' of 'frame' objects>`
        </details>
        <details><summary>`class function(object)`</summary>
        </details>
        <details><summary>`class generator(object)`</summary>
          - `close = <method 'close' of 'generator' objects>`
          - `gi_code = <member 'gi_code' of 'generator' objects>`
          - `gi_frame = <attribute 'gi_frame' of 'generator' objects>`
          - `gi_running = <attribute 'gi_running' of 'generator' objects>`
          - `gi_suspended = <attribute 'gi_suspended' of 'generator' objects>`
          - `gi_yieldfrom = <attribute 'gi_yieldfrom' of 'generator' objects>`
          - `send = <method 'send' of 'generator' objects>`
          - `throw = <method 'throw' of 'generator' objects>`
        </details>
        <details><summary>`class GenericAlias(object)`</summary>
        </details>
        <details><summary>`class getset_descriptor(object)`</summary>
        </details>
        <details><summary>`class function(object)`</summary>
        </details>
        <details><summary>`class mappingproxy(object)`</summary>
          - `copy = <method 'copy' of 'mappingproxy' objects>`
          - `get = <method 'get' of 'mappingproxy' objects>`
          - `items = <method 'items' of 'mappingproxy' objects>`
          - `keys = <method 'keys' of 'mappingproxy' objects>`
          - `values = <method 'values' of 'mappingproxy' objects>`
        </details>
        <details><summary>`class member_descriptor(object)`</summary>
        </details>
        <details><summary>`class method_descriptor(object)`</summary>
        </details>
        <details><summary>`class method(object)`</summary>
        </details>
        <details><summary>`class method-wrapper(object)`</summary>
        </details>
        <details><summary>`class module(object)`</summary>
        </details>
        <details><summary>`class NoneType(object)`</summary>
        </details>
        <details><summary>`class NotImplementedType(object)`</summary>
        </details>
        <details><summary>`class SimpleNamespace(object)`</summary>
        </details>
        <details><summary>`class traceback(object)`</summary>
          - `tb_frame = <member 'tb_frame' of 'traceback' objects>`
          - `tb_lasti = <member 'tb_lasti' of 'traceback' objects>`
          - `tb_lineno = <attribute 'tb_lineno' of 'traceback' objects>`
          - `tb_next = <attribute 'tb_next' of 'traceback' objects>`
        </details>
        <details><summary>`class UnionType(object)`</summary>
        </details>
        <details><summary>`class wrapper_descriptor(object)`</summary>
        </details>
        <details><summary>`coroutine (func)`</summary>
        </details>
        <details><summary>`new_class (name, bases=(), kwds=None, exec_body=None)`</summary>
        </details>
        <details><summary>`prepare_class (name, bases=(), kwds=None)`</summary>
        </details>
        <details><summary>`resolve_bases (bases)`</summary>
        </details>
      </details>
    </details>
    <details><summary>`getattr_migration (module: str) -> Callable[[str], Any]`</summary>
    </details>
    <details><summary>`is_pydantic_dataclass (class_: 'type[Any]', /) -> 'TypeGuard[type[PydanticDataclass]]'`</summary>
    </details>
    <details><summary>`overload (func)`</summary>
    </details>
    <details><summary>`rebuild_dataclass (cls: 'type[PydanticDataclass]', *, force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'dict[str, Any] | None' = None) -> 'bool | None'`</summary>
    </details>
    <details><summary>`sys`</summary>
      - `abiflags = ''`
      - `addaudithook = <built-in function addaudithook>`
      - `api_version = 1013`
      - `argv = ['/home/ubuntu/corp/projects/mbodimono/toolbox/minspect/minspect/test2.py']`
      - `audit = <built-in function audit>`
      - `base_exec_prefix = '/opt/conda/envs/py11'`
      - `base_prefix = '/opt/conda/envs/py11'`
      - `breakpointhook = <built-in function breakpointhook>`
      - `builtin_module_names = ('_abc', '_ast', '_codecs', '_collections', '_functools', '_imp', '_io', '_locale', '_operator', '_signal', '_sre', '_stat', '_string', '_symtable', '_thread', '_tokenize', '_tracemalloc', '_warnings', '_weakref', 'atexit', 'builtins', 'errno', 'faulthandler', 'gc', 'itertools', 'marshal', 'posix', 'pwd', 'sys', 'time', 'xxsubtype')`
      - `byteorder = 'little'`
      - `call_tracing = <built-in function call_tracing>`
      - `copyright = 'Copyright (c) 2001-2023 Python Software Foundation.\nAll Rights Reserved.\n\nCopyright (c) 2000 BeOpen.com.\nAll Rights Reserved.\n\nCopyright (c) 1995-2001 Corporation for National Research Initiatives.\nAll Rights Reserved.\n\nCopyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.\nAll Rights Reserved.'`
      - `displayhook = <built-in function displayhook>`
      - `dont_write_bytecode = False`
      - `exc_info = <built-in function exc_info>`
      - `excepthook = <built-in function excepthook>`
      - `exception = <built-in function exception>`
      - `exec_prefix = '/opt/conda/envs/py11'`
      - `executable = '/opt/conda/envs/py11/bin/python'`
      - `exit = <built-in function exit>`
      - `flags = sys.flags(debug=0, inspect=0, interactive=0, optimize=0, dont_write_bytecode=0, no_user_site=0, no_site=0, ignore_environment=0, verbose=0, bytes_warning=0, quiet=0, hash_randomization=1, isolated=0, dev_mode=False, utf8_mode=0, warn_default_encoding=0, safe_path=False, int_max_str_digits=-1)`
      - `float_info = sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)`
      - `float_repr_style = 'short'`
      - `get_asyncgen_hooks = <built-in function get_asyncgen_hooks>`
      - `get_coroutine_origin_tracking_depth = <built-in function get_coroutine_origin_tracking_depth>`
      - `get_int_max_str_digits = <built-in function get_int_max_str_digits>`
      - `getallocatedblocks = <built-in function getallocatedblocks>`
      - `getdefaultencoding = <built-in function getdefaultencoding>`
      - `getdlopenflags = <built-in function getdlopenflags>`
      - `getfilesystemencodeerrors = <built-in function getfilesystemencodeerrors>`
      - `getfilesystemencoding = <built-in function getfilesystemencoding>`
      - `getprofile = <built-in function getprofile>`
      - `getrecursionlimit = <built-in function getrecursionlimit>`
      - `getrefcount = <built-in function getrefcount>`
      - `getsizeof = <built-in function getsizeof>`
      - `getswitchinterval = <built-in function getswitchinterval>`
      - `gettrace = <built-in function gettrace>`
      - `hash_info = sys.hash_info(width=64, modulus=2305843009213693951, inf=314159, nan=0, imag=1000003, algorithm='siphash13', hash_bits=64, seed_bits=128, cutoff=0)`
      - `hexversion = 51055088`
      - `implementation = namespace(name='cpython', cache_tag='cpython-311', version=sys.version_info(major=3, minor=11, micro=9, releaselevel='final', serial=0), hexversion=51055088, _multiarch='x86_64-linux-gnu')`
      - `int_info = sys.int_info(bits_per_digit=30, sizeof_digit=4, default_max_str_digits=4300, str_digits_check_threshold=640)`
      - `intern = <built-in function intern>`
      - `is_finalizing = <built-in function is_finalizing>`
      - `maxsize = 9223372036854775807`
      - `maxunicode = 1114111`
      - `meta_path = [<_distutils_hack.DistutilsMetaFinder object at 0x7f13fb16b050>, <class '_frozen_importlib.BuiltinImporter'>, <class '_frozen_importlib.FrozenImporter'>, <class '_frozen_importlib_external.PathFinder'>, <class '__editable___faster_whisper_server_1_0_0_finder._EditableFinder'>]`
      - `modules = {'sys': <module 'sys' (built-in)>, 'builtins': <module 'builtins' (built-in)>, '_frozen_importlib': <module '_frozen_importlib' (frozen)>, '_imp': <module '_imp' (built-in)>, '_thread': <module '_thread' (built-in)>, '_warnings': <module '_warnings' (built-in)>, '_weakref': <module '_weakref' (built-in)>, '_io': <module '_io' (built-in)>, 'marshal': <module 'marshal' (built-in)>, 'posix': <module 'posix' (built-in)>, '_frozen_importlib_external': <module '_frozen_importlib_external' (frozen)>, 'time': <module 'time' (built-in)>, 'zipimport': <module 'zipimport' (frozen)>, '_codecs': <module '_codecs' (built-in)>, 'codecs': <module 'codecs' (frozen)>, 'encodings.aliases': <module 'encodings.aliases' from '/opt/conda/envs/py11/lib/python3.11/encodings/aliases.py'>, 'encodings': <module 'encodings' from '/opt/conda/envs/py11/lib/python3.11/encodings/__init__.py'>, 'encodings.utf_8': <module 'encodings.utf_8' from '/opt/conda/envs/py11/lib/python3.11/encodings/utf_8.py'>, '_signal': <module '_signal' (built-in)>, '_abc': <module '_abc' (built-in)>, 'abc': <module 'abc' (frozen)>, 'io': <module 'io' (frozen)>, '__main__': <module '__main__' from '/home/ubuntu/corp/projects/mbodimono/toolbox/minspect/minspect/test2.py'>, '_stat': <module '_stat' (built-in)>, 'stat': <module 'stat' (frozen)>, '_collections_abc': <module '_collections_abc' (frozen)>, 'genericpath': <module 'genericpath' (frozen)>, 'posixpath': <module 'posixpath' (frozen)>, 'os.path': <module 'posixpath' (frozen)>, 'os': <module 'os' (frozen)>, '_sitebuiltins': <module '_sitebuiltins' (frozen)>, '__future__': <module '__future__' from '/opt/conda/envs/py11/lib/python3.11/__future__.py'>, 'importlib._bootstrap': <module '_frozen_importlib' (frozen)>, 'importlib._bootstrap_external': <module '_frozen_importlib_external' (frozen)>, 'warnings': <module 'warnings' from '/opt/conda/envs/py11/lib/python3.11/warnings.py'>, 'importlib': <module 'importlib' from '/opt/conda/envs/py11/lib/python3.11/importlib/__init__.py'>, 'importlib.machinery': <module 'importlib.machinery' (frozen)>, 'importlib._abc': <module 'importlib._abc' from '/opt/conda/envs/py11/lib/python3.11/importlib/_abc.py'>, 'itertools': <module 'itertools' (built-in)>, 'keyword': <module 'keyword' from '/opt/conda/envs/py11/lib/python3.11/keyword.py'>, '_operator': <module '_operator' (built-in)>, 'operator': <module 'operator' from '/opt/conda/envs/py11/lib/python3.11/operator.py'>, 'reprlib': <module 'reprlib' from '/opt/conda/envs/py11/lib/python3.11/reprlib.py'>, '_collections': <module '_collections' (built-in)>, 'collections': <module 'collections' from '/opt/conda/envs/py11/lib/python3.11/collections/__init__.py'>, 'types': <module 'types' from '/opt/conda/envs/py11/lib/python3.11/types.py'>, '_functools': <module '_functools' (built-in)>, 'functools': <module 'functools' from '/opt/conda/envs/py11/lib/python3.11/functools.py'>, 'contextlib': <module 'contextlib' from '/opt/conda/envs/py11/lib/python3.11/contextlib.py'>, '_weakrefset': <module '_weakrefset' from '/opt/conda/envs/py11/lib/python3.11/_weakrefset.py'>, 'threading': <module 'threading' from '/opt/conda/envs/py11/lib/python3.11/threading.py'>, 'importlib.util': <module 'importlib.util' (frozen)>, 'enum': <module 'enum' from '/opt/conda/envs/py11/lib/python3.11/enum.py'>, '_sre': <module '_sre' (built-in)>, 're._constants': <module 're._constants' from '/opt/conda/envs/py11/lib/python3.11/re/_constants.py'>, 're._parser': <module 're._parser' from '/opt/conda/envs/py11/lib/python3.11/re/_parser.py'>, 're._casefix': <module 're._casefix' from '/opt/conda/envs/py11/lib/python3.11/re/_casefix.py'>, 're._compiler': <module 're._compiler' from '/opt/conda/envs/py11/lib/python3.11/re/_compiler.py'>, 'copyreg': <module 'copyreg' from '/opt/conda/envs/py11/lib/python3.11/copyreg.py'>, 're': <module 're' from '/opt/conda/envs/py11/lib/python3.11/re/__init__.py'>, 'fnmatch': <module 'fnmatch' from '/opt/conda/envs/py11/lib/python3.11/fnmatch.py'>, 'ntpath': <module 'ntpath' (frozen)>, 'errno': <module 'errno' (built-in)>, 'urllib': <module 'urllib' from '/opt/conda/envs/py11/lib/python3.11/urllib/__init__.py'>, 'ipaddress': <module 'ipaddress' from '/opt/conda/envs/py11/lib/python3.11/ipaddress.py'>, 'urllib.parse': <module 'urllib.parse' from '/opt/conda/envs/py11/lib/python3.11/urllib/parse.py'>, 'pathlib': <module 'pathlib' from '/opt/conda/envs/py11/lib/python3.11/pathlib.py'>, '__editable___faster_whisper_server_1_0_0_finder': <module '__editable___faster_whisper_server_1_0_0_finder' from '/opt/conda/envs/py11/lib/python3.11/site-packages/__editable___faster_whisper_server_1_0_0_finder.py'>, '_distutils_hack': <module '_distutils_hack' from '/opt/conda/envs/py11/lib/python3.11/site-packages/_distutils_hack/__init__.py'>, 'pyannote': <module 'pyannote' (<_frozen_importlib_external.NamespaceLoader object at 0x7f13fb16b3d0>)>, 'sphinxcontrib': <module 'sphinxcontrib' (<_frozen_importlib_external.NamespaceLoader object at 0x7f13fb16b790>)>, 'site': <module 'site' (frozen)>, '_ast': <module '_ast' (built-in)>, 'collections.abc': <module 'collections.abc' from '/opt/conda/envs/py11/lib/python3.11/collections/abc.py'>, '_typing': <module '_typing' from '/opt/conda/envs/py11/lib/python3.11/lib-dynload/_typing.cpython-311-x86_64-linux-gnu.so'>, 'typing.io': <class 'typing.io'>, 'typing.re': <class 'typing.re'>, 'typing': <module 'typing' from '/opt/conda/envs/py11/lib/python3.11/typing.py'>, 'ast': <module 'ast' from '/opt/conda/envs/py11/lib/python3.11/ast.py'>, '_opcode': <module '_opcode' from '/opt/conda/envs/py11/lib/python3.11/lib-dynload/_opcode.cpython-311-x86_64-linux-gnu.so'>, 'opcode': <module 'opcode' from '/opt/conda/envs/py11/lib/python3.11/opcode.py'>, 'dis': <module 'dis' from '/opt/conda/envs/py11/lib/python3.11/dis.py'>, 'token': <module 'token' from '/opt/conda/envs/py11/lib/python3.11/token.py'>, 'tokenize': <module 'tokenize' from '/opt/conda/envs/py11/lib/python3.11/tokenize.py'>, 'linecache': <module 'linecache' from '/opt/conda/envs/py11/lib/python3.11/linecache.py'>, 'inspect': <module 'inspect' from '/opt/conda/envs/py11/lib/python3.11/inspect.py'>, 'pydantic.version': <module 'pydantic.version' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/version.py'>, 'pydantic._migration': <module 'pydantic._migration' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_migration.py'>, '_socket': <module '_socket' from '/opt/conda/envs/py11/lib/python3.11/lib-dynload/_socket.cpython-311-x86_64-linux-gnu.so'>, 'typing_extensions': <module 'typing_extensions' from '/opt/conda/envs/py11/lib/python3.11/site-packages/typing_extensions.py'>, 'pydantic.errors': <module 'pydantic.errors' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/errors.py'>, 'pydantic': <module 'pydantic' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/__init__.py'>, 'weakref': <module 'weakref' from '/opt/conda/envs/py11/lib/python3.11/weakref.py'>, 'copy': <module 'copy' from '/opt/conda/envs/py11/lib/python3.11/copy.py'>, 'dataclasses': <module 'dataclasses' from '/opt/conda/envs/py11/lib/python3.11/dataclasses.py'>, 'math': <module 'math' from '/opt/conda/envs/py11/lib/python3.11/lib-dynload/math.cpython-311-x86_64-linux-gnu.so'>, '_datetime': <module '_datetime' from '/opt/conda/envs/py11/lib/python3.11/lib-dynload/_datetime.cpython-311-x86_64-linux-gnu.so'>, 'datetime': <module 'datetime' from '/opt/conda/envs/py11/lib/python3.11/datetime.py'>, 'pydantic_core._pydantic_core': <module 'pydantic_core._pydantic_core' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic_core/_pydantic_core.cpython-311-x86_64-linux-gnu.so'>, 'numbers': <module 'numbers' from '/opt/conda/envs/py11/lib/python3.11/numbers.py'>, '_decimal': <module '_decimal' from '/opt/conda/envs/py11/lib/python3.11/lib-dynload/_decimal.cpython-311-x86_64-linux-gnu.so'>, 'decimal': <module 'decimal' from '/opt/conda/envs/py11/lib/python3.11/decimal.py'>, 'pydantic_core.core_schema': <module 'pydantic_core.core_schema' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic_core/core_schema.py'>, 'pydantic_core': <module 'pydantic_core' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic_core/__init__.py'>, 'pydantic._internal': <module 'pydantic._internal' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal/__init__.py'>, 'pydantic._internal._core_metadata': <module 'pydantic._internal._core_metadata' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal/_core_metadata.py'>, 'sysconfig': <module 'sysconfig' from '/opt/conda/envs/py11/lib/python3.11/sysconfig.py'>, '_sysconfigdata__linux_x86_64-linux-gnu': <module '_sysconfigdata__linux_x86_64-linux-gnu' from '/opt/conda/envs/py11/lib/python3.11/_sysconfigdata__linux_x86_64-linux-gnu.py'>, 'zoneinfo._tzpath': <module 'zoneinfo._tzpath' from '/opt/conda/envs/py11/lib/python3.11/zoneinfo/_tzpath.py'>, '_struct': <module '_struct' from '/opt/conda/envs/py11/lib/python3.11/lib-dynload/_struct.cpython-311-x86_64-linux-gnu.so'>, 'struct': <module 'struct' from '/opt/conda/envs/py11/lib/python3.11/struct.py'>, 'zoneinfo._common': <module 'zoneinfo._common' from '/opt/conda/envs/py11/lib/python3.11/zoneinfo/_common.py'>, '_zoneinfo': <module '_zoneinfo' from '/opt/conda/envs/py11/lib/python3.11/lib-dynload/_zoneinfo.cpython-311-x86_64-linux-gnu.so'>, 'zoneinfo': <module 'zoneinfo' from '/opt/conda/envs/py11/lib/python3.11/zoneinfo/__init__.py'>, 'pydantic._internal._typing_extra': <module 'pydantic._internal._typing_extra' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal/_typing_extra.py'>, 'pydantic._internal._repr': <module 'pydantic._internal._repr' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal/_repr.py'>, 'pydantic._internal._core_utils': <module 'pydantic._internal._core_utils' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal/_core_utils.py'>, 'pydantic._internal._internal_dataclass': <module 'pydantic._internal._internal_dataclass' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal/_internal_dataclass.py'>, 'pydantic._internal._decorators': <module 'pydantic._internal._decorators' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal/_decorators.py'>, '_contextvars': <module '_contextvars' from '/opt/conda/envs/py11/lib/python3.11/lib-dynload/_contextvars.cpython-311-x86_64-linux-gnu.so'>, 'contextvars': <module 'contextvars' from '/opt/conda/envs/py11/lib/python3.11/contextvars.py'>, 'pydantic._internal._forward_ref': <module 'pydantic._internal._forward_ref' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal/_forward_ref.py'>, 'pydantic._internal._import_utils': <module 'pydantic._internal._import_utils' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal/_import_utils.py'>, 'pydantic._internal._utils': <module 'pydantic._internal._utils' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal/_utils.py'>, 'pydantic._internal._generics': <module 'pydantic._internal._generics' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal/_generics.py'>, 'pydantic.annotated_handlers': <module 'pydantic.annotated_handlers' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/annotated_handlers.py'>, 'pydantic.functional_validators': <module 'pydantic.functional_validators' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/functional_validators.py'>, 'pydantic.aliases': <module 'pydantic.aliases' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/aliases.py'>, 'binascii': <module 'binascii' from '/opt/conda/envs/py11/lib/python3.11/lib-dynload/binascii.cpython-311-x86_64-linux-gnu.so'>, 'base64': <module 'base64' from '/opt/conda/envs/py11/lib/python3.11/base64.py'>, 'platform': <module 'platform' from '/opt/conda/envs/py11/lib/python3.11/platform.py'>, '_uuid': <module '_uuid' from '/opt/conda/envs/py11/lib/python3.11/lib-dynload/_uuid.cpython-311-x86_64-linux-gnu.so'>, 'uuid': <module 'uuid' from '/opt/conda/envs/py11/lib/python3.11/uuid.py'>, 'annotated_types': <module 'annotated_types' from '/opt/conda/envs/py11/lib/python3.11/site-packages/annotated_types/__init__.py'>, 'pydantic.config': <module 'pydantic.config' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/config.py'>, 'pydantic.warnings': <module 'pydantic.warnings' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/warnings.py'>, 'pydantic._internal._config': <module 'pydantic._internal._config' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal/_config.py'>, 'textwrap': <module 'textwrap' from '/opt/conda/envs/py11/lib/python3.11/textwrap.py'>, 'pydantic._internal._docs_extraction': <module 'pydantic._internal._docs_extraction' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal/_docs_extraction.py'>, 'pydantic._internal._fields': <module 'pydantic._internal._fields' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal/_fields.py'>, 'pydantic._internal._validators': <module 'pydantic._internal._validators' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal/_validators.py'>, 'pydantic.plugin': <module 'pydantic.plugin' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/plugin/__init__.py'>, 'pydantic.plugin._schema_validator': <module 'pydantic.plugin._schema_validator' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/plugin/_schema_validator.py'>, 'pydantic._internal._mock_val_ser': <module 'pydantic._internal._mock_val_ser' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal/_mock_val_ser.py'>, 'pydantic._internal._schema_generation_shared': <module 'pydantic._internal._schema_generation_shared' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal/_schema_generation_shared.py'>, 'pydantic.json_schema': <module 'pydantic.json_schema' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/json_schema.py'>, 'pydantic.types': <module 'pydantic.types' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/types.py'>, '_csv': <module '_csv' from '/opt/conda/envs/py11/lib/python3.11/lib-dynload/_csv.cpython-311-x86_64-linux-gnu.so'>, 'csv': <module 'csv' from '/opt/conda/envs/py11/lib/python3.11/csv.py'>, 'email': <module 'email' from '/opt/conda/envs/py11/lib/python3.11/email/__init__.py'>, 'zlib': <module 'zlib' from '/opt/conda/envs/py11/lib/python3.11/lib-dynload/zlib.cpython-311-x86_64-linux-gnu.so'>, '_compression': <module '_compression' from '/opt/conda/envs/py11/lib/python3.11/_compression.py'>, '_bz2': <module '_bz2' from '/opt/conda/envs/py11/lib/python3.11/lib-dynload/_bz2.cpython-311-x86_64-linux-gnu.so'>, 'bz2': <module 'bz2' from '/opt/conda/envs/py11/lib/python3.11/bz2.py'>, '_lzma': <module '_lzma' from '/opt/conda/envs/py11/lib/python3.11/lib-dynload/_lzma.cpython-311-x86_64-linux-gnu.so'>, 'lzma': <module 'lzma' from '/opt/conda/envs/py11/lib/python3.11/lzma.py'>, 'shutil': <module 'shutil' from '/opt/conda/envs/py11/lib/python3.11/shutil.py'>, 'zipfile': <module 'zipfile' from '/opt/conda/envs/py11/lib/python3.11/zipfile.py'>, 'quopri': <module 'quopri' from '/opt/conda/envs/py11/lib/python3.11/quopri.py'>, '_bisect': <module '_bisect' from '/opt/conda/envs/py11/lib/python3.11/lib-dynload/_bisect.cpython-311-x86_64-linux-gnu.so'>, 'bisect': <module 'bisect' from '/opt/conda/envs/py11/lib/python3.11/bisect.py'>, '_random': <module '_random' from '/opt/conda/envs/py11/lib/python3.11/lib-dynload/_random.cpython-311-x86_64-linux-gnu.so'>, '_sha512': <module '_sha512' from '/opt/conda/envs/py11/lib/python3.11/lib-dynload/_sha512.cpython-311-x86_64-linux-gnu.so'>, 'random': <module 'random' from '/opt/conda/envs/py11/lib/python3.11/random.py'>, 'select': <module 'select' from '/opt/conda/envs/py11/lib/python3.11/lib-dynload/select.cpython-311-x86_64-linux-gnu.so'>, 'selectors': <module 'selectors' from '/opt/conda/envs/py11/lib/python3.11/selectors.py'>, 'array': <module 'array' from '/opt/conda/envs/py11/lib/python3.11/lib-dynload/array.cpython-311-x86_64-linux-gnu.so'>, 'socket': <module 'socket' from '/opt/conda/envs/py11/lib/python3.11/socket.py'>, '_locale': <module '_locale' (built-in)>, 'locale': <module 'locale' from '/opt/conda/envs/py11/lib/python3.11/locale.py'>, 'calendar': <module 'calendar' from '/opt/conda/envs/py11/lib/python3.11/calendar.py'>, 'email._parseaddr': <module 'email._parseaddr' from '/opt/conda/envs/py11/lib/python3.11/email/_parseaddr.py'>, 'email.base64mime': <module 'email.base64mime' from '/opt/conda/envs/py11/lib/python3.11/email/base64mime.py'>, '_string': <module '_string' (built-in)>, 'string': <module 'string' from '/opt/conda/envs/py11/lib/python3.11/string.py'>, 'email.quoprimime': <module 'email.quoprimime' from '/opt/conda/envs/py11/lib/python3.11/email/quoprimime.py'>, 'email.errors': <module 'email.errors' from '/opt/conda/envs/py11/lib/python3.11/email/errors.py'>, 'email.encoders': <module 'email.encoders' from '/opt/conda/envs/py11/lib/python3.11/email/encoders.py'>, 'email.charset': <module 'email.charset' from '/opt/conda/envs/py11/lib/python3.11/email/charset.py'>, 'email.utils': <module 'email.utils' from '/opt/conda/envs/py11/lib/python3.11/email/utils.py'>, 'email.header': <module 'email.header' from '/opt/conda/envs/py11/lib/python3.11/email/header.py'>, 'email._policybase': <module 'email._policybase' from '/opt/conda/envs/py11/lib/python3.11/email/_policybase.py'>, 'email._encoded_words': <module 'email._encoded_words' from '/opt/conda/envs/py11/lib/python3.11/email/_encoded_words.py'>, 'email.iterators': <module 'email.iterators' from '/opt/conda/envs/py11/lib/python3.11/email/iterators.py'>, 'email.message': <module 'email.message' from '/opt/conda/envs/py11/lib/python3.11/email/message.py'>, 'importlib.metadata._functools': <module 'importlib.metadata._functools' from '/opt/conda/envs/py11/lib/python3.11/importlib/metadata/_functools.py'>, 'importlib.metadata._text': <module 'importlib.metadata._text' from '/opt/conda/envs/py11/lib/python3.11/importlib/metadata/_text.py'>, 'importlib.metadata._adapters': <module 'importlib.metadata._adapters' from '/opt/conda/envs/py11/lib/python3.11/importlib/metadata/_adapters.py'>, 'importlib.metadata._meta': <module 'importlib.metadata._meta' from '/opt/conda/envs/py11/lib/python3.11/importlib/metadata/_meta.py'>, 'importlib.metadata._collections': <module 'importlib.metadata._collections' from '/opt/conda/envs/py11/lib/python3.11/importlib/metadata/_collections.py'>, 'importlib.metadata._itertools': <module 'importlib.metadata._itertools' from '/opt/conda/envs/py11/lib/python3.11/importlib/metadata/_itertools.py'>, 'tempfile': <module 'tempfile' from '/opt/conda/envs/py11/lib/python3.11/tempfile.py'>, 'importlib.resources.abc': <module 'importlib.resources.abc' from '/opt/conda/envs/py11/lib/python3.11/importlib/resources/abc.py'>, 'importlib.resources._adapters': <module 'importlib.resources._adapters' from '/opt/conda/envs/py11/lib/python3.11/importlib/resources/_adapters.py'>, 'importlib.resources._common': <module 'importlib.resources._common' from '/opt/conda/envs/py11/lib/python3.11/importlib/resources/_common.py'>, 'importlib.resources._legacy': <module 'importlib.resources._legacy' from '/opt/conda/envs/py11/lib/python3.11/importlib/resources/_legacy.py'>, 'importlib.resources': <module 'importlib.resources' from '/opt/conda/envs/py11/lib/python3.11/importlib/resources/__init__.py'>, 'importlib.abc': <module 'importlib.abc' from '/opt/conda/envs/py11/lib/python3.11/importlib/abc.py'>, 'importlib.metadata': <module 'importlib.metadata' from '/opt/conda/envs/py11/lib/python3.11/importlib/metadata/__init__.py'>, 'pydantic.networks': <module 'pydantic.networks' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/networks.py'>, 'pydantic.deprecated': <module 'pydantic.deprecated' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/deprecated/__init__.py'>, 'pydantic.deprecated.config': <module 'pydantic.deprecated.config' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/deprecated/config.py'>, 'pydantic._internal._discriminated_union': <module 'pydantic._internal._discriminated_union' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal/_discriminated_union.py'>, 'pydantic._internal._known_annotated_metadata': <module 'pydantic._internal._known_annotated_metadata' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal/_known_annotated_metadata.py'>, 'pydantic._internal._generate_schema': <module 'pydantic._internal._generate_schema' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal/_generate_schema.py'>, 'pydantic._internal._signature': <module 'pydantic._internal._signature' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal/_signature.py'>, 'pydantic._internal._validate_call': <module 'pydantic._internal._validate_call' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal/_validate_call.py'>, 'pydantic._internal._model_construction': <module 'pydantic._internal._model_construction' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal/_model_construction.py'>, 'pydantic.main': <module 'pydantic.main' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/main.py'>, 'pydantic.fields': <module 'pydantic.fields' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/fields.py'>, 'pydantic.functional_serializers': <module 'pydantic.functional_serializers' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/functional_serializers.py'>, 'pydantic._internal._serializers': <module 'pydantic._internal._serializers' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal/_serializers.py'>, 'pydantic._internal._std_types_schema': <module 'pydantic._internal._std_types_schema' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal/_std_types_schema.py'>, 'pydantic.plugin._loader': <module 'pydantic.plugin._loader' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/plugin/_loader.py'>, 'pydantic.root_model': <module 'pydantic.root_model' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/root_model.py'>, 'pydantic.type_adapter': <module 'pydantic.type_adapter' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/type_adapter.py'>, 'pydantic._internal._dataclasses': <module 'pydantic._internal._dataclasses' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal/_dataclasses.py'>, 'pydantic.dataclasses': <module 'pydantic.dataclasses' from '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/dataclasses.py'>}`
      - `orig_argv = ['/opt/conda/envs/py11/bin/python', '/home/ubuntu/corp/projects/mbodimono/toolbox/minspect/minspect/test2.py']`
      - `path = ['/home/ubuntu/corp/projects/mbodimono/toolbox/minspect/minspect', '/opt/conda/envs/py11/lib/python311.zip', '/opt/conda/envs/py11/lib/python3.11', '/opt/conda/envs/py11/lib/python3.11/lib-dynload', '/opt/conda/envs/py11/lib/python3.11/site-packages', '__editable__.faster_whisper_server-1.0.0.finder.__path_hook__', '/home/ubuntu/corp/projects/mbodimono/embodied-agents', '/home/ubuntu/corp/projects/mbodimono/toolbox/minspect']`
      - `path_hooks = [<class 'zipimport.zipimporter'>, <function FileFinder.path_hook.<locals>.path_hook_for_FileFinder at 0x7f13fb3d82c0>, <bound method _EditableNamespaceFinder._path_hook of <class '__editable___faster_whisper_server_1_0_0_finder._EditableNamespaceFinder'>>]`
      - `path_importer_cache = {'/opt/conda/envs/py11/lib/python311.zip': None, '/opt/conda/envs/py11/lib/python3.11': FileFinder('/opt/conda/envs/py11/lib/python3.11'), '/opt/conda/envs/py11/lib/python3.11/encodings': FileFinder('/opt/conda/envs/py11/lib/python3.11/encodings'), '/opt/conda/envs/py11/lib/python3.11/lib-dynload': FileFinder('/opt/conda/envs/py11/lib/python3.11/lib-dynload'), '/opt/conda/envs/py11/lib/python3.11/site-packages': FileFinder('/opt/conda/envs/py11/lib/python3.11/site-packages'), '/opt/conda/envs/py11/lib/python3.11/importlib': FileFinder('/opt/conda/envs/py11/lib/python3.11/importlib'), '/opt/conda/envs/py11/lib/python3.11/re': FileFinder('/opt/conda/envs/py11/lib/python3.11/re'), '/opt/conda/envs/py11/lib/python3.11/urllib': FileFinder('/opt/conda/envs/py11/lib/python3.11/urllib'), '__editable__.faster_whisper_server-1.0.0.finder.__path_hook__': <class '__editable___faster_whisper_server_1_0_0_finder._EditableNamespaceFinder'>, '/home/ubuntu/corp/projects/mbodimono/embodied-agents': FileFinder('/home/ubuntu/corp/projects/mbodimono/embodied-agents'), '/home/ubuntu/corp/projects/mbodimono/toolbox/minspect': FileFinder('/home/ubuntu/corp/projects/mbodimono/toolbox/minspect'), '/home/ubuntu/corp/projects/mbodimono/toolbox/minspect/minspect/test2.py': None, '/home/ubuntu/corp/projects/mbodimono/toolbox/minspect/minspect': FileFinder('/home/ubuntu/corp/projects/mbodimono/toolbox/minspect/minspect'), '/opt/conda/envs/py11/lib/python3.11/collections': FileFinder('/opt/conda/envs/py11/lib/python3.11/collections'), '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic': FileFinder('/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic'), '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic_core': FileFinder('/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic_core'), '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal': FileFinder('/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/_internal'), '/opt/conda/envs/py11/lib/python3.11/zoneinfo': FileFinder('/opt/conda/envs/py11/lib/python3.11/zoneinfo'), '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/plugin': FileFinder('/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/plugin'), '/opt/conda/envs/py11/lib/python3.11/importlib/metadata': FileFinder('/opt/conda/envs/py11/lib/python3.11/importlib/metadata'), '/opt/conda/envs/py11/lib/python3.11/email': FileFinder('/opt/conda/envs/py11/lib/python3.11/email'), '/opt/conda/envs/py11/lib/python3.11/importlib/resources': FileFinder('/opt/conda/envs/py11/lib/python3.11/importlib/resources'), '/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/deprecated': FileFinder('/opt/conda/envs/py11/lib/python3.11/site-packages/pydantic/deprecated')}`
      - `platform = 'linux'`
      - `platlibdir = 'lib'`
      - `prefix = '/opt/conda/envs/py11'`
      - `pycache_prefix = None`
      - `set_asyncgen_hooks = <built-in function set_asyncgen_hooks>`
      - `set_coroutine_origin_tracking_depth = <built-in function set_coroutine_origin_tracking_depth>`
      - `set_int_max_str_digits = <built-in function set_int_max_str_digits>`
      - `setdlopenflags = <built-in function setdlopenflags>`
      - `setprofile = <built-in function setprofile>`
      - `setrecursionlimit = <built-in function setrecursionlimit>`
      - `setswitchinterval = <built-in function setswitchinterval>`
      - `settrace = <built-in function settrace>`
      - `stderr = <_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>`
      - `stdin = <_io.TextIOWrapper name='<stdin>' mode='r' encoding='utf-8'>`
      - `stdlib_module_names = frozenset({'contextlib', 'turtledemo', 'numbers', 'select', 'unittest', 'errno', 'base64', 'fractions', 'plistlib', '_compression', 'wsgiref', '_strptime', 'readline', '_tracemalloc', 'zipfile', '_crypt', '_markupbase', '_string', 'ctypes', 'cProfile', 'chunk', 'platform', 'importlib', 'sched', 'abc', '_datetime', '_uuid', 'datetime', '_zoneinfo', 'shlex', 'symtable', 'trace', 'imaplib', 'mmap', 'bz2', 'typing', 'fnmatch', 'compileall', 'imghdr', 'codeop', '_lzma', '_py_abc', 'resource', 'bisect', '_json', 'sre_parse', 'faulthandler', 'ssl', 'tempfile', 'traceback', 'tracemalloc', 'wave', 'xdrlib', '_codecs_hk', '_posixsubprocess', 'aifc', 'argparse', 'asyncio', 'asyncore', 'zoneinfo', '_io', '_random', 'bdb', 'cmd', 'fileinput', 'heapq', '_aix_support', 'copyreg', 'dbm', 'pydoc', 'tty', 'tomllib', 'filecmp', 'doctest', 'nis', '__future__', 'smtplib', '_csv', 'grp', 'curses', 'signal', '_sre', 'quopri', 'audioop', '_codecs_tw', '_ctypes', 'graphlib', 'math', 'string', '_dbm', 'zlib', 'contextvars', '_frozen_importlib_external', 'ntpath', 'spwd', '_codecs_kr', 'builtins', 'decimal', 'smtpd', 'mimetypes', '_warnings', 'socket', '_gdbm', '_multibytecodec', '_functools', '_weakrefset', '_thread', '_struct', 'code', '_ssl', 'dataclasses', 'collections', 'copy', '_statistics', 'poplib', '_pickle', 'tarfile', 'itertools', '_collections', 'genericpath', 'shutil', 'lzma', '_sitebuiltins', '_compat_pickle', '_curses_panel', 'enum', 'concurrent', 'gettext', '_imp', 'runpy', 'msilib', '_tokenize', 'locale', 'venv', '_collections_abc', '_osx_support', 'binascii', 'gzip', '_sha512', 'ipaddress', 'ossaudiodev', 'getpass', 'configparser', '_stat', 'ensurepip', 'hashlib', 'pkgutil', 'modulefinder', '_overlapped', '_multiprocessing', 'token', '_lsprof', 'msvcrt', 'multiprocessing', '_pyio', 'ast', 'glob', 'posix', 'tabnanny', 'xml', 'posixpath', '_hashlib', 'os', 'pdb', 'keyword', 'linecache', 'pathlib', 'tkinter', 'pprint', 'turtle', 'gc', 'shelve', 'telnetlib', 'winreg', '_md5', 'antigravity', 'subprocess', 'xmlrpc', 'opcode', 'unicodedata', 'pydoc_data', 'nt', 'timeit', '_weakref', 'textwrap', '_sha1', 'mailcap', '_asyncio', 'pickletools', 'zipimport', 'cmath', 'ftplib', '_blake2', 'asynchat', 'logging', 're', 'tokenize', '_symtable', 'uu', 'termios', '_signal', 'nturl2path', 'reprlib', 'json', 'site', 'sqlite3', '_msi', 'uuid', 'cgi', 'urllib', 'winsound', 'csv', 'marshal', 'this', 'zipapp', 'weakref', '_codecs_jp', 'netrc', 'crypt', 'struct', 'operator', 'email', 'io', 'encodings', 'queue', 'inspect', 'http', 'syslog', '_codecs_cn', '_bz2', 'random', 'secrets', 'idlelib', 'profile', 'pty', 'functools', 'sre_compile', 'sre_constants', 'pickle', 'getopt', '_sha3', '_sqlite3', '_heapq', 'sunau', '_winapi', '_threading_local', '_pydecimal', '_scproxy', 'calendar', 'codecs', 'distutils', 'sysconfig', '_elementtree', 'stat', 'nntplib', 'atexit', 'pwd', 'sndhdr', '_bootsubprocess', 'dis', 'fcntl', 'pyclbr', 'pyexpat', '_codecs', 'stringprep', '_frozen_importlib', 'types', 'mailbox', 'optparse', 'time', 'colorsys', 'socketserver', 'webbrowser', '_operator', 'difflib', 'py_compile', '_decimal', '_codecs_iso2022', 'hmac', 'array', 'threading', '_opcode', '_ast', 'selectors', '_curses', '_socket', 'html', 'warnings', '_bisect', '_contextvars', '_locale', 'pipes', 'cgitb', 'pstats', '_tkinter', '_abc', 'lib2to3', '_typing', '_sha256', '_posixshmem', 'rlcompleter', 'sys', 'statistics', 'imp', '_queue'})`
      - `stdout = <_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>`
      - `thread_info = sys.thread_info(name='pthread', lock='semaphore', version='NPTL 2.31')`
      - `unraisablehook = <built-in function unraisablehook>`
      - `version = '3.11.9 | packaged by conda-forge | (main, Apr 19 2024, 18:36:13) [GCC 12.3.0]'`
      - `version_info = sys.version_info(major=3, minor=11, micro=9, releaselevel='final', serial=0)`
      - `warnoptions = []`
    </details>
    <details><summary>`types`</summary>
      <details><summary>`class async_generator(object)`</summary>
        - `aclose = <method 'aclose' of 'async_generator' objects>`
        - `ag_await = <attribute 'ag_await' of 'async_generator' objects>`
        - `ag_code = <member 'ag_code' of 'async_generator' objects>`
        - `ag_frame = <attribute 'ag_frame' of 'async_generator' objects>`
        - `ag_running = <member 'ag_running' of 'async_generator' objects>`
        - `asend = <method 'asend' of 'async_generator' objects>`
        - `athrow = <method 'athrow' of 'async_generator' objects>`
      </details>
      <details><summary>`class builtin_function_or_method(object)`</summary>
      </details>
      <details><summary>`class builtin_function_or_method(object)`</summary>
      </details>
      <details><summary>`class cell(object)`</summary>
        - `cell_contents = <attribute 'cell_contents' of 'cell' objects>`
      </details>
      <details><summary>`class classmethod_descriptor(object)`</summary>
      </details>
      <details><summary>`class code(object)`</summary>
        - `co_argcount = <member 'co_argcount' of 'code' objects>`
        - `co_cellvars = <attribute 'co_cellvars' of 'code' objects>`
        - `co_code = <attribute 'co_code' of 'code' objects>`
        - `co_consts = <member 'co_consts' of 'code' objects>`
        - `co_exceptiontable = <member 'co_exceptiontable' of 'code' objects>`
        - `co_filename = <member 'co_filename' of 'code' objects>`
        - `co_firstlineno = <member 'co_firstlineno' of 'code' objects>`
        - `co_flags = <member 'co_flags' of 'code' objects>`
        - `co_freevars = <attribute 'co_freevars' of 'code' objects>`
        - `co_kwonlyargcount = <member 'co_kwonlyargcount' of 'code' objects>`
        - `co_lines = <method 'co_lines' of 'code' objects>`
        - `co_linetable = <member 'co_linetable' of 'code' objects>`
        - `co_lnotab = <attribute 'co_lnotab' of 'code' objects>`
        - `co_name = <member 'co_name' of 'code' objects>`
        - `co_names = <member 'co_names' of 'code' objects>`
        - `co_nlocals = <member 'co_nlocals' of 'code' objects>`
        - `co_positions = <method 'co_positions' of 'code' objects>`
        - `co_posonlyargcount = <member 'co_posonlyargcount' of 'code' objects>`
        - `co_qualname = <member 'co_qualname' of 'code' objects>`
        - `co_stacksize = <member 'co_stacksize' of 'code' objects>`
        - `co_varnames = <attribute 'co_varnames' of 'code' objects>`
        - `replace = <method 'replace' of 'code' objects>`
      </details>
      <details><summary>`class coroutine(object)`</summary>
        - `close = <method 'close' of 'coroutine' objects>`
        - `cr_await = <attribute 'cr_await' of 'coroutine' objects>`
        - `cr_code = <member 'cr_code' of 'coroutine' objects>`
        - `cr_frame = <attribute 'cr_frame' of 'coroutine' objects>`
        - `cr_origin = <member 'cr_origin' of 'coroutine' objects>`
        - `cr_running = <attribute 'cr_running' of 'coroutine' objects>`
        - `cr_suspended = <attribute 'cr_suspended' of 'coroutine' objects>`
        - `send = <method 'send' of 'coroutine' objects>`
        - `throw = <method 'throw' of 'coroutine' objects>`
      </details>
      <details><summary>`class DynamicClassAttribute(object)`</summary>
        <details><summary>`__delete__ (self, instance)`</summary>
        </details>
        <details><summary>`__get__ (self, instance, ownerclass=None)`</summary>
        </details>
        <details><summary>`__init__ (self, fget=None, fset=None, fdel=None, doc=None)`</summary>
        </details>
        <details><summary>`__set__ (self, instance, value)`</summary>
        </details>
        <details><summary>`deleter (self, fdel)`</summary>
        </details>
        <details><summary>`getter (self, fget)`</summary>
        </details>
        <details><summary>`setter (self, fset)`</summary>
        </details>
      </details>
      <details><summary>`class ellipsis(object)`</summary>
      </details>
      <details><summary>`class frame(object)`</summary>
        - `clear = <method 'clear' of 'frame' objects>`
        - `f_back = <attribute 'f_back' of 'frame' objects>`
        - `f_builtins = <attribute 'f_builtins' of 'frame' objects>`
        - `f_code = <attribute 'f_code' of 'frame' objects>`
        - `f_globals = <attribute 'f_globals' of 'frame' objects>`
        - `f_lasti = <attribute 'f_lasti' of 'frame' objects>`
        - `f_lineno = <attribute 'f_lineno' of 'frame' objects>`
        - `f_locals = <attribute 'f_locals' of 'frame' objects>`
        - `f_trace = <attribute 'f_trace' of 'frame' objects>`
        - `f_trace_lines = <member 'f_trace_lines' of 'frame' objects>`
        - `f_trace_opcodes = <member 'f_trace_opcodes' of 'frame' objects>`
      </details>
      <details><summary>`class function(object)`</summary>
      </details>
      <details><summary>`class generator(object)`</summary>
        - `close = <method 'close' of 'generator' objects>`
        - `gi_code = <member 'gi_code' of 'generator' objects>`
        - `gi_frame = <attribute 'gi_frame' of 'generator' objects>`
        - `gi_running = <attribute 'gi_running' of 'generator' objects>`
        - `gi_suspended = <attribute 'gi_suspended' of 'generator' objects>`
        - `gi_yieldfrom = <attribute 'gi_yieldfrom' of 'generator' objects>`
        - `send = <method 'send' of 'generator' objects>`
        - `throw = <method 'throw' of 'generator' objects>`
      </details>
      <details><summary>`class GenericAlias(object)`</summary>
      </details>
      <details><summary>`class getset_descriptor(object)`</summary>
      </details>
      <details><summary>`class function(object)`</summary>
      </details>
      <details><summary>`class mappingproxy(object)`</summary>
        - `copy = <method 'copy' of 'mappingproxy' objects>`
        - `get = <method 'get' of 'mappingproxy' objects>`
        - `items = <method 'items' of 'mappingproxy' objects>`
        - `keys = <method 'keys' of 'mappingproxy' objects>`
        - `values = <method 'values' of 'mappingproxy' objects>`
      </details>
      <details><summary>`class member_descriptor(object)`</summary>
      </details>
      <details><summary>`class method_descriptor(object)`</summary>
      </details>
      <details><summary>`class method(object)`</summary>
      </details>
      <details><summary>`class method-wrapper(object)`</summary>
      </details>
      <details><summary>`class module(object)`</summary>
      </details>
      <details><summary>`class NoneType(object)`</summary>
      </details>
      <details><summary>`class NotImplementedType(object)`</summary>
      </details>
      <details><summary>`class SimpleNamespace(object)`</summary>
      </details>
      <details><summary>`class traceback(object)`</summary>
        - `tb_frame = <member 'tb_frame' of 'traceback' objects>`
        - `tb_lasti = <member 'tb_lasti' of 'traceback' objects>`
        - `tb_lineno = <attribute 'tb_lineno' of 'traceback' objects>`
        - `tb_next = <attribute 'tb_next' of 'traceback' objects>`
      </details>
      <details><summary>`class UnionType(object)`</summary>
      </details>
      <details><summary>`class wrapper_descriptor(object)`</summary>
      </details>
      <details><summary>`coroutine (func)`</summary>
      </details>
      <details><summary>`new_class (name, bases=(), kwds=None, exec_body=None)`</summary>
      </details>
      <details><summary>`prepare_class (name, bases=(), kwds=None)`</summary>
      </details>
      <details><summary>`resolve_bases (bases)`</summary>
      </details>
    </details>
    - `warn = <built-in function warn>`
  </details>
  <details><summary>`field_serializer (*fields: 'str', mode: "Literal['plain', 'wrap']" = 'plain', return_type: 'Any' = PydanticUndefined, when_used: 'WhenUsed' = 'always', check_fields: 'bool | None' = None) -> 'Callable[[_FieldWrapSerializerT], _FieldWrapSerializerT] | Callable[[_FieldPlainSerializerT], _FieldPlainSerializerT]'`</summary>
  </details>
  <details><summary>`field_validator (field: 'str', /, *fields: 'str', mode: 'FieldValidatorModes' = 'after', check_fields: 'bool | None' = None, json_schema_input_type: 'Any' = PydanticUndefined) -> 'Callable[[Any], Any]'`</summary>
  </details>
  <details><summary>`model_serializer (f: '_ModelPlainSerializerT | _ModelWrapSerializerT | None' = None, /, *, mode: "Literal['plain', 'wrap']" = 'plain', when_used: 'WhenUsed' = 'always', return_type: 'Any' = PydanticUndefined) -> '_ModelPlainSerializerT | Callable[[_ModelWrapSerializerT], _ModelWrapSerializerT] | Callable[[_ModelPlainSerializerT], _ModelPlainSerializerT]'`</summary>
  </details>
  <details><summary>`model_validator (*, mode: "Literal['wrap', 'before', 'after']") -> 'Any'`</summary>
  </details>
  <details><summary>`parse_obj_as (type_: 'type[T]', obj: 'Any', type_name: 'NameFactory | None' = None) -> 'T'`</summary>
  </details>
  <details><summary>`root_validator (*__args, pre: 'bool' = False, skip_on_failure: 'bool' = False, allow_reuse: 'bool' = False) -> 'Any'`</summary>
  </details>
  <details><summary>`schema_json_of (type_: 'Any', *, title: 'NameFactory | None' = None, by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, **dumps_kwargs: 'Any') -> 'str'`</summary>
  </details>
  <details><summary>`schema_of (type_: 'Any', *, title: 'NameFactory | None' = None, by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>) -> 'dict[str, Any]'`</summary>
  </details>
  <details><summary>`validate_call (func: 'AnyCallableT | None' = None, /, *, config: 'ConfigDict | None' = None, validate_return: 'bool' = False) -> 'AnyCallableT | Callable[[AnyCallableT], AnyCallableT]'`</summary>
  </details>
  <details><summary>`validate_email (value: 'str') -> 'tuple[str, str]'`</summary>
  </details>
  <details><summary>`validator (__field: 'str', *fields: 'str', pre: 'bool' = False, each_item: 'bool' = False, always: 'bool' = False, check_fields: 'bool | None' = None, allow_reuse: 'bool' = False) -> 'Callable[[_V1ValidatorType], _V1ValidatorType]'`</summary>
  </details>
  <details><summary>`with_config (config: 'ConfigDict') -> 'Callable[[_TypeT], _TypeT]'`</summary>
  </details>
</details>
