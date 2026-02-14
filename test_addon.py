"""
Basic tests for the Blender Spaceship Generator addon
Tests the module structure and basic functionality
"""

import sys
import os

# Add the addon directory to path for testing
addon_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, addon_path)


def test_imports():
    """Test that all modules can be imported"""
    print("Testing module imports...")
    
    try:
        import ship_generator
        print("✓ ship_generator imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import ship_generator: {e}")
        return False
    
    try:
        import ship_parts
        print("✓ ship_parts imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import ship_parts: {e}")
        return False
    
    try:
        import interior_generator
        print("✓ interior_generator imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import interior_generator: {e}")
        return False
    
    try:
        import module_system
        print("✓ module_system imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import module_system: {e}")
        return False
    
    return True


def test_ship_configs():
    """Test that ship configurations are properly defined"""
    print("\nTesting ship configurations...")
    
    import ship_generator
    
    expected_classes = [
        'SHUTTLE', 'FIGHTER', 'CORVETTE', 'FRIGATE', 
        'DESTROYER', 'CRUISER', 'BATTLESHIP', 'CARRIER', 'CAPITAL'
    ]
    
    for ship_class in expected_classes:
        if ship_class in ship_generator.SHIP_CONFIGS:
            config = ship_generator.SHIP_CONFIGS[ship_class]
            required_keys = ['scale', 'hull_segments', 'engines', 'weapons', 'wings', 'crew_capacity']
            
            missing_keys = [key for key in required_keys if key not in config]
            if missing_keys:
                print(f"✗ {ship_class} config missing keys: {missing_keys}")
                return False
            
            print(f"✓ {ship_class} configuration is valid")
        else:
            print(f"✗ {ship_class} not found in SHIP_CONFIGS")
            return False
    
    return True


def test_module_types():
    """Test that module types are properly defined"""
    print("\nTesting module types...")
    
    import module_system
    
    expected_types = ['CARGO', 'WEAPON', 'SHIELD', 'HANGAR', 'SENSOR', 'POWER']
    
    for module_type in expected_types:
        if module_type in module_system.MODULE_TYPES:
            config = module_system.MODULE_TYPES[module_type]
            required_keys = ['name', 'scale_factor', 'shape']
            
            missing_keys = [key for key in required_keys if key not in config]
            if missing_keys:
                print(f"✗ {module_type} config missing keys: {missing_keys}")
                return False
            
            print(f"✓ {module_type} module type is valid")
        else:
            print(f"✗ {module_type} not found in MODULE_TYPES")
            return False
    
    return True


def test_interior_constants():
    """Test that interior constants are properly defined"""
    print("\nTesting interior constants...")
    
    import interior_generator
    
    constants = {
        'HUMAN_HEIGHT': interior_generator.HUMAN_HEIGHT,
        'DOOR_HEIGHT': interior_generator.DOOR_HEIGHT,
        'DOOR_WIDTH': interior_generator.DOOR_WIDTH,
        'CORRIDOR_WIDTH': interior_generator.CORRIDOR_WIDTH,
        'CORRIDOR_HEIGHT': interior_generator.CORRIDOR_HEIGHT,
        'ROOM_HEIGHT': interior_generator.ROOM_HEIGHT,
    }
    
    for name, value in constants.items():
        if isinstance(value, (int, float)) and value > 0:
            print(f"✓ {name} = {value}")
        else:
            print(f"✗ {name} has invalid value: {value}")
            return False
    
    return True


def run_tests():
    """Run all tests"""
    print("=" * 50)
    print("Blender Spaceship Generator - Structure Tests")
    print("=" * 50)
    
    tests = [
        ("Module Imports", test_imports),
        ("Ship Configurations", test_ship_configs),
        ("Module Types", test_module_types),
        ("Interior Constants", test_interior_constants),
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"\n✗ {test_name} raised exception: {e}")
            results.append((test_name, False))
    
    print("\n" + "=" * 50)
    print("Test Results:")
    print("=" * 50)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{status}: {test_name}")
    
    print("=" * 50)
    print(f"Total: {passed}/{total} tests passed")
    print("=" * 50)
    
    return passed == total


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
