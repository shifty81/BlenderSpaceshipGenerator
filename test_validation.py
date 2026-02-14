"""
Syntax and structure validation tests for the Blender Spaceship Generator addon
These tests run without requiring Blender to be installed
"""

import ast
import os
import sys


def test_python_syntax(filepath):
    """Test if a Python file has valid syntax"""
    try:
        with open(filepath, 'r') as f:
            code = f.read()
        ast.parse(code)
        return True, None
    except SyntaxError as e:
        return False, str(e)


def test_addon_structure():
    """Test that all required files exist"""
    print("Testing addon structure...")
    
    addon_path = os.path.dirname(os.path.abspath(__file__))
    required_files = [
        '__init__.py',
        'ship_generator.py',
        'ship_parts.py',
        'interior_generator.py',
        'module_system.py',
        'atlas_exporter.py',
        'station_generator.py',
        'asteroid_generator.py',
        'texture_generator.py',
    ]
    
    all_exist = True
    for filename in required_files:
        filepath = os.path.join(addon_path, filename)
        if os.path.exists(filepath):
            print(f"✓ {filename} exists")
        else:
            print(f"✗ {filename} is missing")
            all_exist = False
    
    return all_exist


def test_file_syntax():
    """Test Python syntax of all module files"""
    print("\nTesting Python syntax...")
    
    addon_path = os.path.dirname(os.path.abspath(__file__))
    python_files = [
        '__init__.py',
        'ship_generator.py',
        'ship_parts.py',
        'interior_generator.py',
        'module_system.py',
        'atlas_exporter.py',
        'station_generator.py',
        'asteroid_generator.py',
        'texture_generator.py',
    ]
    
    all_valid = True
    for filename in python_files:
        filepath = os.path.join(addon_path, filename)
        if os.path.exists(filepath):
            valid, error = test_python_syntax(filepath)
            if valid:
                print(f"✓ {filename} has valid syntax")
            else:
                print(f"✗ {filename} has syntax error: {error}")
                all_valid = False
    
    return all_valid


def test_bl_info():
    """Test that __init__.py has valid bl_info"""
    print("\nTesting bl_info metadata...")
    
    addon_path = os.path.dirname(os.path.abspath(__file__))
    init_file = os.path.join(addon_path, '__init__.py')
    
    try:
        with open(init_file, 'r') as f:
            content = f.read()
        
        # Check for bl_info
        if 'bl_info' not in content:
            print("✗ bl_info not found in __init__.py")
            return False
        
        # Parse and check bl_info
        tree = ast.parse(content)
        bl_info_found = False
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == 'bl_info':
                        bl_info_found = True
                        
                        # Check if it's a dictionary
                        if isinstance(node.value, ast.Dict):
                            keys = [k.s if isinstance(k, ast.Str) else (k.value if isinstance(k, ast.Constant) else None) 
                                   for k in node.value.keys]
                            
                            required_keys = ['name', 'author', 'version', 'blender', 'category']
                            for key in required_keys:
                                if key in keys:
                                    print(f"✓ bl_info has '{key}' key")
                                else:
                                    print(f"✗ bl_info missing '{key}' key")
                                    return False
                        break
        
        if not bl_info_found:
            print("✗ bl_info assignment not found")
            return False
        
        return True
        
    except Exception as e:
        print(f"✗ Error checking bl_info: {e}")
        return False


def test_register_functions():
    """Test that register/unregister functions exist"""
    print("\nTesting register/unregister functions...")
    
    addon_path = os.path.dirname(os.path.abspath(__file__))
    files_to_check = [
        '__init__.py',
        'ship_generator.py',
        'ship_parts.py',
        'interior_generator.py',
        'module_system.py',
        'atlas_exporter.py',
        'station_generator.py',
        'asteroid_generator.py',
        'texture_generator.py',
    ]
    
    all_valid = True
    for filename in files_to_check:
        filepath = os.path.join(addon_path, filename)
        
        try:
            with open(filepath, 'r') as f:
                content = f.read()
            
            has_register = 'def register()' in content
            has_unregister = 'def unregister()' in content
            
            if has_register and has_unregister:
                print(f"✓ {filename} has register/unregister functions")
            else:
                missing = []
                if not has_register:
                    missing.append('register')
                if not has_unregister:
                    missing.append('unregister')
                print(f"✗ {filename} missing: {', '.join(missing)}")
                all_valid = False
                
        except Exception as e:
            print(f"✗ Error checking {filename}: {e}")
            all_valid = False
    
    return all_valid


def test_documentation():
    """Test that documentation files exist"""
    print("\nTesting documentation...")
    
    addon_path = os.path.dirname(os.path.abspath(__file__))
    doc_files = ['README.md', 'USAGE.md']
    
    all_exist = True
    for filename in doc_files:
        filepath = os.path.join(addon_path, filename)
        if os.path.exists(filepath):
            size = os.path.getsize(filepath)
            print(f"✓ {filename} exists ({size} bytes)")
        else:
            print(f"✗ {filename} is missing")
            all_exist = False
    
    return all_exist


def run_tests():
    """Run all validation tests"""
    print("=" * 60)
    print("Blender Spaceship Generator - Validation Tests")
    print("=" * 60)
    
    tests = [
        ("Addon Structure", test_addon_structure),
        ("Python Syntax", test_file_syntax),
        ("bl_info Metadata", test_bl_info),
        ("Register Functions", test_register_functions),
        ("Documentation", test_documentation),
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"\n✗ {test_name} raised exception: {e}")
            import traceback
            traceback.print_exc()
            results.append((test_name, False))
    
    print("\n" + "=" * 60)
    print("Test Results Summary:")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{status}: {test_name}")
    
    print("=" * 60)
    print(f"Total: {passed}/{total} tests passed")
    
    if passed == total:
        print("✓ All validation tests passed!")
    else:
        print("✗ Some tests failed")
    
    print("=" * 60)
    
    return passed == total


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
