"""
Main ship generator module
Coordinates the generation of ship parts and assembly
"""

import bpy
import random
from . import ship_parts
from . import interior_generator
from . import module_system


# Ship class configurations
SHIP_CONFIGS = {
    'SHUTTLE': {
        'scale': 1.0,
        'hull_segments': 3,
        'engines': 2,
        'weapons': 0,
        'wings': False,
        'crew_capacity': 2,
    },
    'FIGHTER': {
        'scale': 1.5,
        'hull_segments': 4,
        'engines': 2,
        'weapons': 2,
        'wings': True,
        'crew_capacity': 1,
    },
    'CORVETTE': {
        'scale': 3.0,
        'hull_segments': 5,
        'engines': 3,
        'weapons': 4,
        'wings': True,
        'crew_capacity': 4,
    },
    'FRIGATE': {
        'scale': 5.0,
        'hull_segments': 6,
        'engines': 4,
        'weapons': 6,
        'wings': False,
        'crew_capacity': 10,
    },
    'DESTROYER': {
        'scale': 8.0,
        'hull_segments': 7,
        'engines': 4,
        'weapons': 8,
        'wings': False,
        'crew_capacity': 25,
    },
    'CRUISER': {
        'scale': 12.0,
        'hull_segments': 8,
        'engines': 6,
        'weapons': 12,
        'wings': False,
        'crew_capacity': 50,
    },
    'BATTLESHIP': {
        'scale': 18.0,
        'hull_segments': 10,
        'engines': 8,
        'weapons': 16,
        'wings': False,
        'crew_capacity': 100,
    },
    'CARRIER': {
        'scale': 25.0,
        'hull_segments': 12,
        'engines': 10,
        'weapons': 10,
        'wings': False,
        'crew_capacity': 200,
    },
    'CAPITAL': {
        'scale': 35.0,
        'hull_segments': 15,
        'engines': 12,
        'weapons': 20,
        'wings': False,
        'crew_capacity': 500,
    },
}


def generate_spaceship(ship_class='FIGHTER', seed=1, generate_interior=True,
                       module_slots=2, hull_complexity=1.0, symmetry=True,
                       style='MIXED'):
    """
    Generate a complete spaceship with all parts
    
    Args:
        ship_class: Type of ship to generate
        seed: Random seed for generation
        generate_interior: Whether to generate interior
        module_slots: Number of module slots to add
        hull_complexity: Complexity factor for hull geometry
        symmetry: Whether to use symmetrical design
        style: Design style (MIXED, X4, ELITE, EVE)
    """
    random.seed(seed)
    
    # Get ship configuration
    config = SHIP_CONFIGS.get(ship_class, SHIP_CONFIGS['FIGHTER'])
    scale = config['scale']
    
    # Create main collection for the ship
    collection_name = f"Spaceship_{ship_class}_{seed}"
    collection = bpy.data.collections.new(collection_name)
    bpy.context.scene.collection.children.link(collection)
    
    # Generate hull
    hull = ship_parts.generate_hull(
        segments=config['hull_segments'],
        scale=scale,
        complexity=hull_complexity,
        symmetry=symmetry,
        style=style
    )
    collection.objects.link(hull)
    
    # Generate cockpit/bridge
    cockpit = ship_parts.generate_cockpit(
        scale=scale,
        position=(0, scale * 0.8, 0),
        ship_class=ship_class,
        style=style
    )
    collection.objects.link(cockpit)
    
    # Generate engines
    engines = ship_parts.generate_engines(
        count=config['engines'],
        scale=scale,
        symmetry=symmetry,
        style=style
    )
    for engine in engines:
        collection.objects.link(engine)
    
    # Generate wings if applicable
    if config['wings']:
        wings = ship_parts.generate_wings(
            scale=scale,
            symmetry=symmetry,
            style=style
        )
        for wing in wings:
            collection.objects.link(wing)
    
    # Generate weapon hardpoints
    if config['weapons'] > 0:
        weapons = ship_parts.generate_weapon_hardpoints(
            count=config['weapons'],
            scale=scale,
            symmetry=symmetry
        )
        for weapon in weapons:
            collection.objects.link(weapon)
    
    # Generate modules
    if module_slots > 0:
        modules = module_system.generate_modules(
            count=module_slots,
            scale=scale,
            ship_class=ship_class
        )
        for module in modules:
            collection.objects.link(module)
    
    # Generate interior if requested
    if generate_interior:
        interior_objects = interior_generator.generate_interior(
            ship_class=ship_class,
            scale=scale,
            crew_capacity=config['crew_capacity']
        )
        for obj in interior_objects:
            collection.objects.link(obj)
    
    # Parent all objects to the hull
    for obj in collection.objects:
        if obj != hull:
            obj.parent = hull
    
    # Center the ship at the 3D cursor
    hull.location = bpy.context.scene.cursor.location
    
    return hull


def register():
    """Register this module"""
    pass


def unregister():
    """Unregister this module"""
    pass
