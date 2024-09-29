 - (self, other: 'Any') -> 'bool'

      - **Method**: __get_pydantic_core_schema__ - (source: 'type[Any]', handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'

      - **Method**: __hash__ - (self) -> 'int'

      - **Method**: __init__ - (self, secret_value: 'SecretType') -> 'None'

      - **Method**: __init_subclass__ - (*args, **kwargs)

      - **Method**: __len__ - (self) -> 'int'

      - **Method**: __repr__ - (self) -> 'str'

      - **Method**: __str__ - (self) -> 'str'

      - **Method**: _display - (self) -> 'bytes'

      - **Method**: get_secret_value - (self) -> 'SecretType'

    - **Class**: SecretStr

      - **Method**: __class_getitem__ - (params)

      - **Method**: __eq__ - (self, other: 'Any') -> 'bool'

      - **Method**: __get_pydantic_core_schema__ - (source: 'type[Any]', handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'

      - **Method**: __hash__ - (self) -> 'int'

      - **Method**: __init__ - (self, secret_value: 'SecretType') -> 'None'

      - **Method**: __init_subclass__ - (*args, **kwargs)

      - **Method**: __len__ - (self) -> 'int'

      - **Method**: __repr__ - (self) -> 'str'

      - **Method**: __str__ - (self) -> 'str'

      - **Method**: _display - (self) -> 'str'

      - **Method**: get_secret_value - (self) -> 'SecretType'

    - **Class**: SerializationInfo

      - **Method**: __class_getitem__ - (params)

      - **Method**: __init__ - (self, *args, **kwargs)

      - **Method**: __init_subclass__ - (*args, **kwargs)

      - **Method**: __repr__ - (self) -> 'str'

      - **Method**: __str__ - (self) -> 'str'

      - **Method**: __subclasshook__ - (other)

      - **Attribute**: by_alias = <property object at 0x7eafeb22d860>

      - **Attribute**: context = <property object at 0x7eafeb22d590>

      - **Attribute**: exclude = <property object at 0x7eafeb22d4f0>

      - **Attribute**: exclude_defaults = <property object at 0x7eafeb22dbd0>

      - **Attribute**: exclude_none = <property object at 0x7eafeb22df90>

      - **Attribute**: exclude_unset = <property object at 0x7eafeb22d900>

      - **Attribute**: include = <property object at 0x7eafeb22d180>

      - **Attribute**: mode = <property object at 0x7eafeb22d770>

      - **Method**: mode_is_json - (self) -> 'bool'

      - **Method**: round_trip - (self) -> 'bool'

      - **Attribute**: serialize_as_any = <property object at 0x7eafeb22e260>

    - **Class**: SerializeAsAny

      - **Method**: __class_getitem__ - (item: 'Any') -> 'Any'

      - **Method**: __eq__ - (self, other)

      - **Method**: __get_pydantic_core_schema__ - (self, source_type: 'Any', handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'

      - **Method**: __init__ - (self) -> None

      - **Method**: __repr__ - (self)

    - **Class**: SerializerFunctionWrapHandler

      - **Method**: __call__ - (self, input_value: 'Any', index_key: 'int | str | None' = None, /) -> 'Any'

      - **Method**: __class_getitem__ - (params)

      - **Method**: __init__ - (self, *args, **kwargs)

      - **Method**: __init_subclass__ - (*args, **kwargs)

      - **Method**: __subclasshook__ - (other)

    - **Class**: SkipValidation

      - **Method**: __class_getitem__ - (item: 'Any') -> 'Any'

      - **Method**: __eq__ - (self, other)

      - **Method**: __get_pydantic_core_schema__ - (source: 'Any', handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'

      - **Method**: __init__ - (self) -> None

      - **Method**: __repr__ - (self)

    - **Class**: Strict

      - **Method**: __eq__ - (self, other)

      - **Method**: __hash__ - (self) -> 'int'

      - **Method**: __init__ - (self, strict: 'bool' = True) -> None

      - **Method**: __pretty__ - (self, fmt: 'typing.Callable[[Any], Any]', **kwargs: 'Any') -> 'typing.Generator[Any, None, None]'

      - **Method**: __repr__ - (self)

      - **Method**: __repr_args__ - (self) -> 'ReprArgs'

      - **Method**: __repr_name__ - (self) -> 'str'

      - **Method**: __repr_str__ - (self, join_str: 'str') -> 'str'

      - **Method**: __rich_repr__ - (self) -> 'RichReprResult'

      - **Method**: __str__ - (self) -> 'str'

      - **Attribute**: strict = True

    - **Attribute**: StrictBool = typing.Annotated[bool, Strict(strict=True)]

    - **Attribute**: StrictBytes = typing.Annotated[bytes, Strict(strict=True)]

    - **Attribute**: StrictFloat = typing.Annotated[float, Strict(strict=True)]

    - **Attribute**: StrictInt = typing.Annotated[int, Strict(strict=True)]

    - **Attribute**: StrictStr = typing.Annotated[str, Strict(strict=True)]

    - **Class**: StringConstraints

      - **Method**: __class_getitem__ - (params)

      - **Method**: __delattr__ - (self, name)

      - **Method**: __eq__ - (self, other)

      - **Method**: __hash__ - (self)

      - **Method**: __init__ - (self, strip_whitespace: 'bool | None' = None, to_upper: 'bool | None' = None, to_lower: 'bool | None' = None, strict: 'bool | None' = None, min_length: 'int | None' = None, max_length: 'int | None' = None, pattern: 'str | Pattern[str] | None' = None) -> None

      - **Method**: __init_subclass__ - (*args: Any, **kwargs: Any) -> None

      - **Method**: __iter__ - (self) -> 'Iterator[BaseMetadata]'

      - **Method**: __repr__ - (self)

      - **Method**: __setattr__ - (self, name, value)

      - **Method**: __subclasshook__ - (other)

      - **Attribute**: max_length = None

      - **Attribute**: min_length = None

      - **Attribute**: pattern = None

      - **Attribute**: strict = None

      - **Attribute**: strip_whitespace = None

      - **Attribute**: to_lower = None

      - **Attribute**: to_upper = None

    - **Class**: Tag

      - **Method**: __delattr__ - (self, name)

      - **Method**: __eq__ - (self, other)

      - **Method**: __get_pydantic_core_schema__ - (self, source_type: 'Any', handler: 'GetCoreSchemaHandler') -> 'CoreSchema'

      - **Method**: __getstate__ - (self)

      - **Method**: __hash__ - (self)

      - **Method**: __init__ - (self, tag: 'str') -> None

      - **Method**: __repr__ - (self)

      - **Method**: __setattr__ - (self, name, value)

      - **Method**: __setstate__ - (self, state)

      - **Attribute**: tag = <member 'tag' of 'Tag' objects>

    - **Class**: TypeAdapter

      - **Method**: __class_getitem__ - (params)

      - **Method**: __init__ - (self, type: 'Any', *, config: 'ConfigDict | None' = None, _parent_depth: 'int' = 2, module: 'str | None' = None) -> 'None'

      - **Method**: __init_subclass__ - (*args, **kwargs)

      - **Method**: dump_json - (self, instance: 'T', /, *, indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, serialize_as_any: 'bool' = False) -> 'bytes'

      - **Method**: dump_python - (self, instance: 'T', /, *, mode: "Literal['json', 'python']" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, serialize_as_any: 'bool' = False) -> 'Any'

      - **Method**: get_default_value - (self, *, strict: 'bool | None' = None, context: 'dict[str, Any] | None' = None) -> 'Some[T] | None'

      - **Method**: json_schema - (self, *, by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation') -> 'dict[str, Any]'

      - **Method**: json_schemas - (inputs: 'Iterable[tuple[JsonSchemaKeyT, JsonSchemaMode, TypeAdapter[Any]]]', /, *, by_alias: 'bool' = True, title: 'str | None' = None, description: 'str | None' = None, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>) -> 'tuple[dict[tuple[JsonSchemaKeyT, JsonSchemaMode], JsonSchemaValue], JsonSchemaValue]'

      - **Method**: validate_json - (self, data: 'str | bytes', /, *, strict: 'bool | None' = None, context: 'dict[str, Any] | None' = None) -> 'T'

      - **Method**: validate_python - (self, object: 'Any', /, *, strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'dict[str, Any] | None' = None) -> 'T'

      - **Method**: validate_strings - (self, obj: 'Any', /, *, strict: 'bool | None' = None, context: 'dict[str, Any] | None' = None) -> 'T'

    - **Attribute**: UUID1 = typing.Annotated[uuid.UUID, UuidVersion(uuid_version=1)]

    - **Attribute**: UUID3 = typing.Annotated[uuid.UUID, UuidVersion(uuid_version=3)]

    - **Attribute**: UUID4 = typing.Annotated[uuid.UUID, UuidVersion(uuid_version=4)]

    - **Attribute**: UUID5 = typing.Annotated[uuid.UUID, UuidVersion(uuid_version=5)]

    - **Class**: UrlConstraints

      - **Method**: __eq__ - (self, other)

      - **Method**: __hash__ - (self) -> 'int'

      - **Method**: __init__ - (self, max_length: 'int | None' = None, allowed_schemes: 'list[str] | None' = None, host_required: 'bool | None' = None, default_host: 'str | None' = None, default_port: 'int | None' = None, default_path: 'str | None' = None) -> None

      - **Method**: __pretty__ - (self, fmt: 'typing.Callable[[Any], Any]', **kwargs: 'Any') -> 'typing.Generator[Any, None, None]'

      - **Method**: __repr__ - (self)

      - **Method**: __repr_args__ - (self) -> 'ReprArgs'

      - **Method**: __repr_name__ - (self) -> 'str'

      - **Method**: __repr_str__ - (self, join_str: 'str') -> 'str'

      - **Method**: __rich_repr__ - (self) -> 'RichReprResult'

      - **Method**: __str__ - (self) -> 'str'

      - **Attribute**: allowed_schemes = None

      - **Attribute**: default_host = None

      - **Attribute**: default_path = None

      - **Attribute**: default_port = None

      - **Attribute**: host_required = None

      - **Attribute**: max_length = None

    - **Attribute**: VERSION = '2.7.2'

    - **Class**: ValidationError

      - **Attribute**: add_note = <method 'add_note' of 'BaseException' objects>

      - **Attribute**: args = <attribute 'args' of 'BaseException' objects>

      - **Attribute**: error_count = <method 'error_count' of 'pydantic_core._pydantic_core.ValidationError' objects>

      - **Attribute**: errors = <method 'errors' of 'pydantic_core._pydantic_core.ValidationError' objects>

      - **Attribute**: from_exception_data = <built-in method from_exception_data of type object at 0x7eafeb21d410>

      - **Attribute**: json = <method 'json' of 'pydantic_core._pydantic_core.ValidationError' objects>

      - **Attribute**: title = <attribute 'title' of 'pydantic_core._pydantic_core.ValidationError' objects>

      - **Attribute**: with_traceback = <method 'with_traceback' of 'BaseException' objects>

    - **Class**: ValidationInfo

      - **Method**: __class_getitem__ - (params)

      - **Method**: __init__ - (self, *args, **kwargs)

      - **Method**: __init_subclass__ - (*args, **kwargs)

      - **Method**: __subclasshook__ - (other)

      - **Attribute**: config = <property object at 0x7eafeb22e760>

      - **Attribute**: context = <property object at 0x7eafeb22e6c0>

      - **Attribute**: data = <property object at 0x7eafeb22eda0>

      - **Attribute**: field_name = <property object at 0x7eafeb22ee40>

      - **Attribute**: mode = <property object at 0x7eafeb22e800>

    - **Class**: ValidatorFunctionWrapHandler

      - **Method**: __call__ - (self, input_value: 'Any', outer_location: 'str | int | None' = None) -> 'Any'

      - **Method**: __class_getitem__ - (params)

      - **Method**: __init__ - (self, *args, **kwargs)

      - **Method**: __init_subclass__ - (*args, **kwargs)

      - **Method**: __subclasshook__ - (other)

    - **Attribute**: WebsocketUrl = typing.Annotated[pydantic_core._pydantic_core.Url, UrlConstraints(max_length=2083, allowed_schemes=['ws', 'wss'], host_required=None, default_host=None, default_port=None, default_path=None)]

    - **Class**: WithJsonSchema

      - **Method**: __eq__ - (self, other)

      - **Method**: __get_pydantic_json_schema__ - (self, core_schema: 'core_schema.CoreSchema', handler: 'GetJsonSchemaHandler') -> 'JsonSchemaValue'

      - **Method**: __hash__ - (self) -> 'int'

      - **Method**: __init__ - (self, json_schema: 'JsonSchemaValue | None', mode: "Literal['validation', 'serialization'] | None" = None) -> None

      - **Method**: __repr__ - (self)

      - **Attribute**: json_schema = <member 'json_schema' of 'WithJsonSchema' objects>

      - **Attribute**: mode = <member 'mode' of 'WithJsonSchema' objects>

    - **Class**: WrapSerializer

      - **Method**: __delattr__ - (self, name)

      - **Method**: __eq__ - (self, other)

      - **Method**: __get_pydantic_core_schema__ - (self, source_type: 'Any', handler: 'GetCoreSchemaHandler') -> 'core_schema.CoreSchema'

      - **Method**: __getstate__ - (self)

      - **Method**: __hash__ - (self)

      - **Method**: __init__ - (self, func: 'core_schema.WrapSerializerFunction', return_type: 'Any' = PydanticUndefined, when_used: "Literal['always', 'unless-none', 'json', 'json-unless-none']" = 'always') -> None

      - **Method**: __repr__ - (self)

      - **Method**: __setattr__ - (self, name, value)

      - **Method**: __setstate__ - (self, state)

      - **Attribute**: func = <member 'func' of 'WrapSerializer' objects>

      - **Attribute**: return_type = <member 'return_type' of 'WrapSerializer' objects>

      - **Attribute**: when_used = <member 'when_used' of 'WrapSerializer' objects>

    - **Class**: WrapValidator

      - **Method**: __delattr__ - (self, name)

      - **Method**: __eq__ - (self, other)

      - **Method**: __get_pydantic_core_schema__ - (self, source_type: 'Any', handler: '_GetCoreSchemaHandler') -> 'core_schema.CoreSchema'

      - **Method**: __getstate__ - (self)

      - **Method**: __hash__ - (self)

      - **Method**: __init__ - (self, func: 'core_schema.NoInfoWrapValidatorFunction | core_schema.WithInfoWrapValidatorFunction') -> None

      - **Method**: __repr__ - (self)

      - **Method**: __setattr__ - (self, name, value)

      - **Method**: __setstate__ - (self, state)

      - **Attribute**: func = <member 'func' of 'WrapValidator' objects>

    - **Function/Method**: computed_field - (func: 'PropertyT | None' = None, /, *, alias: 'str | None' = None, alias_priority: 'int | None' = None, title: 'str | None' = None, description: 'str | None' = None, deprecated: 'Deprecated | str | bool | None' = None, examples: 'list[Any] | None' = None, json_schema_extra: 'JsonDict | typing.Callable[[JsonDict], None] | None' = None, repr: 'bool | None' = None, return_type: 'Any' = PydanticUndefined) -> 'PropertyT | typing.Callable[[PropertyT], PropertyT]'

    - **Function/Method**: conbytes - (*, min_length: 'int | None' = None, max_length: 'int | None' = None, strict: 'bool | None' = None) -> 'type[bytes]'

    - **Function/Method**: condate - (*, strict: 'bool | None' = None, gt: 'date | None' = None, ge: 'date | None' = None, lt: 'date | None' = None, le: 'date | None' = None) -> 'type[date]'

    - **Function/Method**: condecimal - (*, strict: 'bool | None' = None, gt: 'int | Decimal | None' = None, ge: 'int | Decimal | None' = None, lt: 'int | Decimal | None' = None, le: 'int | Decimal | None' = None, multiple_of: 'int | Decimal | None' = None, max_digits: 'int | None' = None, decimal_places: 'int | None' = None, allow_inf_nan: 'bool | None' = None) -> 'type[Decimal]'

    - **Function/Method**: confloat - (*, strict: 'bool | None' = None, gt: 'float | None' = None, ge: 'float | None' = None, lt: 'float | None' = None, le: 'float | None' = None, multiple_of: 'float | None' = None, allow_inf_nan: 'bool | None' = None) -> 'type[float]'

    - **Function/Method**: confrozenset - (item_type: 'type[HashableItemType]', *, min_length: 'int | None' = None, max_length: 'int | None' = None) -> 'type[frozenset[HashableItemType]]'

    - **Function/Method**: conint - (*, strict: 'bool | None' = None, gt: 'int | None' = None, ge: 'int | None' = None, lt: 'int | None' = None, le: 'int | None' = None, multiple_of: 'int | None' = None) -> 'type[int]'

    - **Function/Method**: conlist - (item_type: 'type[AnyItemType]', *, min_length: 'int | None' = None, max_length: 'int | None' = None, unique_items: 'bool | None' = None) -> 'type[list[AnyItemType]]'

    - **Function/Method**: conset - (item_type: 'type[HashableItemType]', *, min_length: 'int | None' = None, max_length: 'int | None' = None) -> 'type[set[HashableItemType]]'

    - **Function/Method**: constr - (*, strip_whitespace: 'bool | None' = None, to_upper: 'bool | None' = None, to_lower: 'bool | None' = None, strict: 'bool | None' = None, min_length: 'int | None' = None, max_length: 'int | None' = None, pattern: 'str | Pattern[str] | None' = None) -> 'type[str]'

    - **Function/Method**: create_model - (__model_name: 'str', *, __config__: 'ConfigDict | None' = None, __doc__: 'str | None' = None, __base__: 'type[Model] | tuple[type[Model], ...] | None' = None, __module__: 'str | None' = None, __validators__: 'dict[str, classmethod] | None' = None, __cls_kwargs__: 'dict[str, Any] | None' = None, __slots__: 'tuple[str, ...] | None' = None, **field_definitions: 'Any') -> 'type[Model]'

    - **Module**: pydantic.dataclasses

    - **Function/Method**: field_serializer - (*fields: 'str', mode: "Literal['plain', 'wrap']" = 'plain', return_type: 'Any' = PydanticUndefined, when_used: "Literal['always', 'unless-none', 'json', 'json-unless-none']" = 'always', check_fields: 'bool | None' = None) -> 'Callable[[Any], Any]'

    - **Function/Method**: field_validator - (field: 'str', /, *fields: 'str', mode: 'FieldValidatorModes' = 'after', check_fields: 'bool | None' = None) -> 'Callable[[Any], Any]'

    - **Function/Method**: model_serializer - (f: 'Callable[..., Any] | None' = None, /, *, mode: "Literal['plain', 'wrap']" = 'plain', when_used: "Literal['always', 'unless-none', 'json', 'json-unless-none']" = 'always', return_type: 'Any' = PydanticUndefined) -> 'Callable[[Any], Any]'

    - **Function/Method**: model_validator - (*, mode: "Literal['wrap', 'before', 'after']") -> 'Any'

    - **Function/Method**: parse_obj_as - (type_: 'type[T]', obj: 'Any', type_name: 'NameFactory | None' = None) -> 'T'

    - **Function/Method**: root_validator - (*__args, pre: 'bool' = False, skip_on_failure: 'bool' = False, allow_reuse: 'bool' = False) -> 'Any'

    - **Function/Method**: schema_json_of - (type_: 'Any', *, title: 'NameFactory | None' = None, by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, **dumps_kwargs: 'Any') -> 'str'

    - **Function/Method**: schema_of - (type_: 'Any', *, title: 'NameFactory | None' = None, by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>) -> 'dict[str, Any]'

    - **Function/Method**: validate_call - (func: 'AnyCallableT | None' = None, /, *, config: 'ConfigDict | None' = None, validate_return: 'bool' = False) -> 'AnyCallableT | Callable[[AnyCallableT], AnyCallableT]'

    - **Function/Method**: validate_email - (value: 'str') -> 'tuple[str, str]'

    - **Function/Method**: validator - (__field: 'str', *fields: 'str', pre: 'bool' = False, each_item: 'bool' = False, always: 'bool' = False, check_fields: 'bool | None' = None, allow_reuse: 'bool' = False) -> 'Callable[[_V1ValidatorType], _V1ValidatorType]'

    - **Function/Method**: with_config - (config: 'ConfigDict') -> 'Callable[[_TypeT], _TypeT]'
