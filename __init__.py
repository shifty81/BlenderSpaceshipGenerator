"""
Blender Spaceship Generator Addon
Generates procedural spaceships with modular parts and interiors
Inspired by X4, Elite Dangerous, and Eve Online
"""

bl_info = {
    "name": "Spaceship Generator",
    "author": "BlenderSpaceshipGenerator",
    "version": (1, 0, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Sidebar > Spaceship",
    "description": "Generate procedural spaceships with modular parts and interiors",
    "category": "Add Mesh",
}

import bpy
from bpy.props import (
    EnumProperty,
    BoolProperty,
    IntProperty,
    FloatProperty,
)

from . import ship_generator
from . import ship_parts
from . import interior_generator
from . import module_system


class SpaceshipGeneratorProperties(bpy.types.PropertyGroup):
    """Properties for the spaceship generator"""
    
    ship_class: EnumProperty(
        name="Ship Class",
        description="Type of ship to generate",
        items=[
            ('SHUTTLE', "Shuttle", "Small transport vessel"),
            ('FIGHTER', "Fighter", "Single-seat combat ship"),
            ('CORVETTE', "Corvette", "Small multi-crew combat ship"),
            ('FRIGATE', "Frigate", "Medium combat/utility ship"),
            ('DESTROYER', "Destroyer", "Heavy combat ship"),
            ('CRUISER', "Cruiser", "Large multi-role ship"),
            ('BATTLESHIP', "Battleship", "Heavy capital ship"),
            ('CARRIER', "Carrier", "Fleet carrier ship"),
            ('CAPITAL', "Capital", "Largest class capital ship"),
        ],
        default='FIGHTER'
    )
    
    generate_interior: BoolProperty(
        name="Generate Interior",
        description="Generate ship interior with rooms and corridors",
        default=True
    )
    
    module_slots: IntProperty(
        name="Module Slots",
        description="Number of additional module slots",
        default=2,
        min=0,
        max=10
    )
    
    seed: IntProperty(
        name="Random Seed",
        description="Seed for procedural generation",
        default=1,
        min=1
    )
    
    hull_complexity: FloatProperty(
        name="Hull Complexity",
        description="Complexity of hull geometry",
        default=1.0,
        min=0.1,
        max=3.0
    )
    
    symmetry: BoolProperty(
        name="Symmetry",
        description="Generate symmetric ship design",
        default=True
    )
    
    style: EnumProperty(
        name="Style",
        description="Ship design style",
        items=[
            ('MIXED', "Mixed", "Mixed style from all inspirations"),
            ('X4', "X4", "X4 Foundations style"),
            ('ELITE', "Elite Dangerous", "Elite Dangerous style"),
            ('EVE', "Eve Online", "Eve Online style"),
        ],
        default='MIXED'
    )


class SPACESHIP_OT_generate(bpy.types.Operator):
    """Generate a procedural spaceship"""
    bl_idname = "mesh.generate_spaceship"
    bl_label = "Generate Spaceship"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        props = context.scene.spaceship_props
        
        # Generate the spaceship
        ship_generator.generate_spaceship(
            ship_class=props.ship_class,
            seed=props.seed,
            generate_interior=props.generate_interior,
            module_slots=props.module_slots,
            hull_complexity=props.hull_complexity,
            symmetry=props.symmetry,
            style=props.style
        )
        
        self.report({'INFO'}, f"Generated {props.ship_class} class spaceship")
        return {'FINISHED'}


class SPACESHIP_PT_main_panel(bpy.types.Panel):
    """Main panel for spaceship generator"""
    bl_label = "Spaceship Generator"
    bl_idname = "SPACESHIP_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Spaceship'
    
    def draw(self, context):
        layout = self.layout
        props = context.scene.spaceship_props
        
        layout.label(text="Ship Configuration:")
        layout.prop(props, "ship_class")
        layout.prop(props, "style")
        layout.prop(props, "seed")
        
        layout.separator()
        layout.label(text="Generation Options:")
        layout.prop(props, "generate_interior")
        layout.prop(props, "module_slots")
        layout.prop(props, "hull_complexity")
        layout.prop(props, "symmetry")
        
        layout.separator()
        layout.operator("mesh.generate_spaceship", icon='MESH_CUBE')


# Registration
classes = (
    SpaceshipGeneratorProperties,
    SPACESHIP_OT_generate,
    SPACESHIP_PT_main_panel,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    
    bpy.types.Scene.spaceship_props = bpy.props.PointerProperty(
        type=SpaceshipGeneratorProperties
    )
    
    # Register submodules
    ship_generator.register()
    ship_parts.register()
    interior_generator.register()
    module_system.register()


def unregister():
    # Unregister submodules
    module_system.unregister()
    interior_generator.unregister()
    ship_parts.unregister()
    ship_generator.unregister()
    
    del bpy.types.Scene.spaceship_props
    
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
