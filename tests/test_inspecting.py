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

def test_load_all_modules():
    # This test might need to be adjusted based on your actual module structure
    import minspect
    modules = load_all_modules(minspect)
    assert len(modules) > 0
    assert any(name == "inspecting" for name, _ in modules)

def test_is_standard_lib():
    import os
    assert is_standard_lib(os) == True
    import minspect
    assert is_standard_lib(minspect) == False

def test_get_root_module():
    import os.path
    assert get_root_module(os.path) == "os"
    import minspect.inspecting
    assert get_root_module(minspect.inspecting) == "minspect"

def test_is_imported():
    import os
    import minspect
    assert is_imported(minspect, os) == True
    from minspect import inspecting
    assert is_imported(minspect, inspecting) == False

def test_get_full_name():
    def test_function():
        pass
    assert get_full_name(test_function) == "test_inspecting.test_get_full_name.<locals>.test_function"
    assert get_full_name(pytest) == "pytest"

def test_collect_info():
    import minspect
    info = collect_info(minspect, depth=1)
    assert isinstance(info, dict)
    assert "inspecting" in info

def test_inspect_library():
    result = inspect_library("minspect", depth=1)
    assert isinstance(result, dict)
    assert "inspecting" in result
