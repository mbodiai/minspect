import pytest
from minspect.inspecting import (
    load_all_modules,
    is_standard_lib,
    get_root_module,
    is_imported,
    get_full_name,
    collect_info,
    inspect_library
)

# Existing tests...

# New tests for class methods and other objects
class TestClass:
    def instance_method(self):
        pass

    @classmethod
    def class_method(cls):
        pass

    @staticmethod
    def static_method():
        pass

    class NestedClass:
        def nested_method(self):
            pass

def test_get_full_name_class_methods():
    assert get_full_name(TestClass.instance_method) == "test_inspecting.TestClass.instance_method"
    assert get_full_name(TestClass.class_method) == "test_inspecting.TestClass.class_method"
    assert get_full_name(TestClass.static_method) == "test_inspecting.TestClass.static_method"
    assert get_full_name(TestClass.NestedClass.nested_method) == "test_inspecting.TestClass.NestedClass.nested_method"

def test_collect_info_class():
    info = collect_info(TestClass, depth=2)
    assert isinstance(info, dict)
    assert "instance_method" in info
    assert "class_method" in info
    assert "static_method" in info
    assert "NestedClass" in info
    assert isinstance(info["NestedClass"]["members"], dict)
    assert "nested_method" in info["NestedClass"]["members"]

def test_collect_info_builtin():
    info = collect_info(list, depth=1)
    assert isinstance(info, dict)
    assert "append" in info
    assert "extend" in info

def test_collect_info_module():
    import math
    info = collect_info(math, depth=1)
    assert isinstance(info, dict)
    assert "pi" in info
    assert "sin" in info

def test_inspect_library_depth():
    result = inspect_library("minspect", depth=2)
    assert isinstance(result, dict)
    assert "inspecting" in result
    assert isinstance(result["inspecting"]["members"], dict)
    assert "collect_info" in result["inspecting"]["members"]

def test_inspect_library_options():
    result = inspect_library("minspect.inspecting", depth=1, signatures=True, docs=True)
    assert isinstance(result, dict)
    assert "collect_info" in result
    assert "signature" in result["collect_info"]
    assert "docstring" in result["collect_info"]

# You can add more tests here to cover other scenarios and edge cases
