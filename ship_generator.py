"""
Main ship generator module
Coordinates the generation of ship parts and assembly
"""

import bpy
import random
from . import ship_parts
from . import interior_generator
from . import module_system


# Maximum number of turret hardpoints any ship may have
MAX_TURRET_HARDPOINTS = 10


# Ship class configurations
SHIP_CONFIGS = {
    'SHUTTLE': {
        'scale': 1.0,
        'hull_segments': 3,
        'engines': 2,
        'weapons': 0,
        'turret_hardpoints': 0,
        'wings': False,
        'crew_capacity': 2,
    },
    'FIGHTER': {
        'scale': 1.5,
        'hull_segments': 4,
        'engines': 2,
        'weapons': 2,
        'turret_hardpoints': 1,
        'wings': True,
        'crew_capacity': 1,
    },
    'CORVETTE': {
        'scale': 3.0,
        'hull_segments': 5,
        'engines': 3,
        'weapons': 4,
        'turret_hardpoints': 2,
        'wings': True,
        'crew_capacity': 4,
    },
    'FRIGATE': {
        'scale': 5.0,
        'hull_segments': 6,
        'engines': 4,
        'weapons': 6,
        'turret_hardpoints': 3,
        'wings': False,
        'crew_capacity': 10,
    },
    'DESTROYER': {
        'scale': 8.0,
        'hull_segments': 7,
        'engines': 4,
        'weapons': 8,
        'turret_hardpoints': 4,
        'wings': False,
        'crew_capacity': 25,
    },
    'CRUISER': {
        'scale': 12.0,
        'hull_segments': 8,
        'engines': 6,
        'weapons': 12,
        'turret_hardpoints': 6,
        'wings': False,
        'crew_capacity': 50,
    },
    'BATTLESHIP': {
        'scale': 18.0,
        'hull_segments': 10,
        'engines': 8,
        'weapons': 16,
        'turret_hardpoints': 8,
        'wings': False,
        'crew_capacity': 100,
    },
    'CARRIER': {
        'scale': 25.0,
        'hull_segments': 12,
        'engines': 10,
        'weapons': 10,
        'turret_hardpoints': 6,
        'wings': False,
        'crew_capacity': 200,
    },
    'CAPITAL': {
        'scale': 35.0,
        'hull_segments': 15,
        'engines': 12,
        'weapons': 20,
        'turret_hardpoints': 10,
        'wings': False,
        'crew_capacity': 500,
    },
    'BATTLECRUISER': {
        'scale': 15.0,
        'hull_segments': 9,
        'engines': 6,
        'weapons': 14,
        'turret_hardpoints': 7,
        'wings': False,
        'crew_capacity': 75,
    },
    'DREADNOUGHT': {
        'scale': 30.0,
        'hull_segments': 14,
        'engines': 5,
        'weapons': 18,
        'turret_hardpoints': 10,
        'wings': False,
        'crew_capacity': 400,
    },
    'TITAN': {
        'scale': 50.0,
        'hull_segments': 18,
        'engines': 10,
        'weapons': 24,
        'turret_hardpoints': 10,
        'wings': False,
        'crew_capacity': 1000,
    },
    'INDUSTRIAL': {
        'scale': 6.0,
        'hull_segments': 5,
        'engines': 3,
        'weapons': 1,
        'turret_hardpoints': 0,
        'wings': False,
        'crew_capacity': 5,
    },
    'MINING_BARGE': {
        'scale': 4.0,
        'hull_segments': 4,
        'engines': 2,
        'weapons': 0,
        'turret_hardpoints': 0,
        'wings': False,
        'crew_capacity': 3,
    },
    'EXHUMER': {
        'scale': 5.0,
        'hull_segments': 5,
        'engines': 3,
        'weapons': 0,
        'turret_hardpoints': 0,
        'wings': False,
        'crew_capacity': 4,
    },
    'EXPLORER': {
        'scale': 2.0,
        'hull_segments': 5,
        'engines': 2,
        'weapons': 1,
        'turret_hardpoints': 1,
        'wings': True,
        'crew_capacity': 1,
    },
    'HAULER': {
        'scale': 5.5,
        'hull_segments': 6,
        'engines': 4,
        'weapons': 0,
        'turret_hardpoints': 0,
        'wings': False,
        'crew_capacity': 2,
    },
    'EXOTIC': {
        'scale': 2.5,
        'hull_segments': 7,
        'engines': 2,
        'weapons': 2,
        'turret_hardpoints': 1,
        'wings': True,
        'crew_capacity': 1,
    },
}


def _prefixed_name(prefix, name):
    """Return name with project prefix applied if prefix is non-empty."""
    if prefix:
        return f"{prefix}_{name}"
    return name


def generate_spaceship(ship_class='FIGHTER', seed=1, generate_interior=True,
                       module_slots=2, hull_complexity=1.0, symmetry=True,
                       style='MIXED', naming_prefix='', turret_hardpoints=0):
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
        naming_prefix: Project naming prefix applied to all generated elements
        turret_hardpoints: Number of turret hardpoints to generate (0-10)
    """
    random.seed(seed)
    
    # Get ship configuration
    config = SHIP_CONFIGS.get(ship_class, SHIP_CONFIGS['FIGHTER'])
    scale = config['scale']
    
    # Create main collection for the ship
    collection_name = _prefixed_name(naming_prefix, f"Spaceship_{ship_class}_{seed}")
    collection = bpy.data.collections.new(collection_name)
    bpy.context.scene.collection.children.link(collection)
    
    # Generate hull
    hull = ship_parts.generate_hull(
        segments=config['hull_segments'],
        scale=scale,
        complexity=hull_complexity,
        symmetry=symmetry,
        style=style,
        naming_prefix=naming_prefix
    )
    collection.objects.link(hull)
    
    # Generate cockpit/bridge
    cockpit = ship_parts.generate_cockpit(
        scale=scale,
        position=(0, scale * 0.8, 0),
        ship_class=ship_class,
        style=style,
        naming_prefix=naming_prefix
    )
    collection.objects.link(cockpit)
    
    # Generate engines
    engines = ship_parts.generate_engines(
        count=config['engines'],
        scale=scale,
        symmetry=symmetry,
        style=style,
        naming_prefix=naming_prefix
    )
    for engine in engines:
        collection.objects.link(engine)
    
    # Generate wings if applicable
    if config['wings']:
        wings = ship_parts.generate_wings(
            scale=scale,
            symmetry=symmetry,
            style=style,
            naming_prefix=naming_prefix
        )
        for wing in wings:
            collection.objects.link(wing)
    
    # Generate weapon hardpoints
    if config['weapons'] > 0:
        weapons = ship_parts.generate_weapon_hardpoints(
            count=config['weapons'],
            scale=scale,
            symmetry=symmetry,
            naming_prefix=naming_prefix
        )
        for weapon in weapons:
            collection.objects.link(weapon)
    
    # Generate turret hardpoints
    turret_count = turret_hardpoints if turret_hardpoints > 0 else config.get('turret_hardpoints', 0)
    turret_count = min(turret_count, MAX_TURRET_HARDPOINTS)
    if turret_count > 0:
        turrets = ship_parts.generate_turret_hardpoints(
            count=turret_count,
            scale=scale,
            symmetry=symmetry,
            naming_prefix=naming_prefix
        )
        for turret in turrets:
            collection.objects.link(turret)
    
    # Generate modules
    if module_slots > 0:
        modules = module_system.generate_modules(
            count=module_slots,
            scale=scale,
            ship_class=ship_class,
            naming_prefix=naming_prefix
        )
        for module in modules:
            collection.objects.link(module)
    
    # Generate interior if requested
    if generate_interior:
        interior_objects = interior_generator.generate_interior(
            ship_class=ship_class,
            scale=scale,
            crew_capacity=config['crew_capacity'],
            naming_prefix=naming_prefix
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
