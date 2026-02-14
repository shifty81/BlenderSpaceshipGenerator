"""
Ship parts generation module
Generates individual ship components (hull, cockpit, engines, wings, weapons)
"""

import bpy
import bmesh
import random
import math


def create_mesh_object(name, verts, edges, faces):
    """Helper function to create a mesh object from vertices, edges, and faces"""
    mesh = bpy.data.meshes.new(name)
    mesh.from_pydata(verts, edges, faces)
    mesh.update()
    
    obj = bpy.data.objects.new(name, mesh)
    return obj


def generate_hull(segments=5, scale=1.0, complexity=1.0, symmetry=True, style='MIXED'):
    """
    Generate the main hull of the spaceship
    
    Args:
        segments: Number of hull segments
        scale: Overall scale factor
        complexity: Geometry complexity (0.1-3.0)
        symmetry: Use symmetrical design
        style: Design style
    """
    # Create base hull mesh
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, 0))
    hull = bpy.context.active_object
    hull.name = "Hull"
    
    # Scale to ship size
    hull.scale = (scale * 0.5, scale, scale * 0.3)
    bpy.ops.object.transform_apply(scale=True)
    
    # Enter edit mode to modify geometry
    bpy.context.view_layer.objects.active = hull
    bpy.ops.object.mode_set(mode='EDIT')
    
    # Add subdivisions based on complexity
    subdiv_levels = max(1, int(complexity * 2))
    bpy.ops.mesh.subdivide(number_cuts=subdiv_levels)
    
    # Add some variation to vertices
    bpy.ops.object.mode_set(mode='OBJECT')
    
    # Apply style-specific modifications
    if style == 'X4':
        # X4 style: Angular, geometric
        apply_x4_style(hull, scale)
    elif style == 'ELITE':
        # Elite style: Sleek, aerodynamic
        apply_elite_style(hull, scale)
    elif style == 'EVE':
        # Eve style: Organic, flowing
        apply_eve_style(hull, scale)
    elif style == 'SOLARI':
        apply_solari_style(hull, scale)
    elif style == 'VEYREN':
        apply_veyren_style(hull, scale)
    elif style == 'AURELIAN':
        apply_aurelian_style(hull, scale)
    elif style == 'KELDARI':
        apply_keldari_style(hull, scale)
    elif style == 'NMS':
        apply_nms_style(hull, scale)
    else:
        # Mixed style
        apply_mixed_style(hull, scale)
    
    # Add smooth shading
    bpy.ops.object.shade_smooth()
    
    # Add subdivision surface modifier for smoother look
    modifier = hull.modifiers.new(name="Subdivision", type='SUBSURF')
    modifier.levels = 1
    modifier.render_levels = 2
    
    # Add edge split for hard edges
    edge_split = hull.modifiers.new(name="EdgeSplit", type='EDGE_SPLIT')
    edge_split.split_angle = math.radians(30)
    
    return hull


def apply_x4_style(hull, scale):
    """Apply X4 Foundations style - angular and geometric"""
    bpy.context.view_layer.objects.active = hull
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.bevel(offset=0.1 * scale, segments=1)
    bpy.ops.object.mode_set(mode='OBJECT')


def apply_elite_style(hull, scale):
    """Apply Elite Dangerous style - sleek and aerodynamic"""
    bpy.context.view_layer.objects.active = hull
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.transform.taper(value=0.7)
    bpy.ops.object.mode_set(mode='OBJECT')


def apply_eve_style(hull, scale):
    """Apply Eve Online style - organic and flowing"""
    # Add a smooth deformation for organic look
    bpy.context.view_layer.objects.active = hull
    bpy.ops.object.mode_set(mode='EDIT')
    # Add some organic variation with proportional editing concept
    bpy.ops.mesh.subdivide(number_cuts=1)
    bpy.ops.object.mode_set(mode='OBJECT')
    
    # Add a cast modifier for more organic curves
    cast_mod = hull.modifiers.new(name="Cast", type='CAST')
    cast_mod.factor = 0.3
    cast_mod.cast_type = 'SPHERE'


def apply_mixed_style(hull, scale):
    """Apply mixed style from all inspirations"""
    bpy.context.view_layer.objects.active = hull
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.bevel(offset=0.05 * scale, segments=2)
    bpy.ops.object.mode_set(mode='OBJECT')


def apply_solari_style(hull, scale):
    """Apply Solari faction style - golden, elegant, armor-focused"""
    bpy.context.view_layer.objects.active = hull
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.bevel(offset=0.08 * scale, segments=3)
    bpy.ops.object.mode_set(mode='OBJECT')

    # Add smooth curves for elegant look
    cast_mod = hull.modifiers.new(name="Cast", type='CAST')
    cast_mod.factor = 0.15
    cast_mod.cast_type = 'SPHERE'


def apply_veyren_style(hull, scale):
    """Apply Veyren faction style - angular, utilitarian, shield-focused"""
    bpy.context.view_layer.objects.active = hull
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.bevel(offset=0.12 * scale, segments=1)
    bpy.ops.object.mode_set(mode='OBJECT')


def apply_aurelian_style(hull, scale):
    """Apply Aurelian faction style - sleek, organic, drone-focused"""
    bpy.context.view_layer.objects.active = hull
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.subdivide(number_cuts=1)
    bpy.ops.object.mode_set(mode='OBJECT')

    cast_mod = hull.modifiers.new(name="Cast", type='CAST')
    cast_mod.factor = 0.25
    cast_mod.cast_type = 'SPHERE'


def apply_keldari_style(hull, scale):
    """Apply Keldari faction style - rugged, industrial, missile-focused"""
    bpy.context.view_layer.objects.active = hull
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.bevel(offset=0.15 * scale, segments=1)
    bpy.ops.object.mode_set(mode='OBJECT')


def apply_nms_style(hull, scale):
    """Apply No Man's Sky style - colorful, varied, mix of smooth and angular.

    NMS ships combine rounded organic surfaces with sharp mechanical details.
    The hull gets a moderate cast towards a sphere for that rounded look plus a
    light bevel to keep panel edges visible.
    """
    bpy.context.view_layer.objects.active = hull
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.subdivide(number_cuts=1)
    bpy.ops.mesh.bevel(offset=0.06 * scale, segments=2)
    bpy.ops.object.mode_set(mode='OBJECT')

    # Rounded cast for organic NMS silhouette
    cast_mod = hull.modifiers.new(name="NMS_Cast", type='CAST')
    cast_mod.factor = 0.2
    cast_mod.cast_type = 'SPHERE'


def generate_cockpit(scale=1.0, position=(0, 0, 0), ship_class='FIGHTER', style='MIXED'):
    """
    Generate cockpit/bridge for the ship
    
    Args:
        scale: Ship scale factor
        position: Position relative to hull
        ship_class: Type of ship
        style: Design style
    """
    # Create cockpit as a modified cube
    bpy.ops.mesh.primitive_cube_add(size=scale * 0.3, location=position)
    cockpit = bpy.context.active_object
    cockpit.name = "Cockpit"
    
    # Scale to appropriate proportions
    cockpit.scale = (0.8, 1.2, 0.6)
    bpy.ops.object.transform_apply(scale=True)
    
    # Taper the front for viewing angle
    bpy.context.view_layer.objects.active = cockpit
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.subdivide(number_cuts=2)
    bpy.ops.object.mode_set(mode='OBJECT')
    
    # Add smooth shading
    bpy.ops.object.shade_smooth()
    
    return cockpit


def generate_engines(count=2, scale=1.0, symmetry=True, style='MIXED'):
    """
    Generate engine units
    
    Args:
        count: Number of engines
        scale: Ship scale factor
        symmetry: Use symmetrical placement
        style: Design style
    """
    engines = []
    engine_size = scale * 0.2
    
    # Position engines at the rear of the ship
    rear_position = -scale * 0.9
    
    if symmetry and count % 2 == 0:
        # Symmetric engine placement
        spacing = scale * 0.3
        for i in range(count // 2):
            offset = spacing * (i + 0.5)
            
            # Left engine
            bpy.ops.mesh.primitive_cylinder_add(
                radius=engine_size,
                depth=engine_size * 2,
                location=(offset, rear_position, 0)
            )
            left_engine = bpy.context.active_object
            left_engine.name = f"Engine_L{i+1}"
            left_engine.rotation_euler = (math.radians(90), 0, 0)
            engines.append(left_engine)
            
            # Right engine
            bpy.ops.mesh.primitive_cylinder_add(
                radius=engine_size,
                depth=engine_size * 2,
                location=(-offset, rear_position, 0)
            )
            right_engine = bpy.context.active_object
            right_engine.name = f"Engine_R{i+1}"
            right_engine.rotation_euler = (math.radians(90), 0, 0)
            engines.append(right_engine)
    else:
        # Non-symmetric or odd count
        for i in range(count):
            x_offset = (i - count / 2) * scale * 0.3
            bpy.ops.mesh.primitive_cylinder_add(
                radius=engine_size,
                depth=engine_size * 2,
                location=(x_offset, rear_position, 0)
            )
            engine = bpy.context.active_object
            engine.name = f"Engine_{i+1}"
            engine.rotation_euler = (math.radians(90), 0, 0)
            engines.append(engine)
    
    # Add glow material to engines
    for engine in engines:
        mat = bpy.data.materials.new(name="Engine_Glow")
        mat.use_nodes = True
        nodes = mat.node_tree.nodes
        
        # Add emission shader
        emission = nodes.new(type='ShaderNodeEmission')
        emission.inputs['Color'].default_value = (0.2, 0.5, 1.0, 1.0)  # Blue glow
        emission.inputs['Strength'].default_value = 5.0
        
        output = nodes.get('Material Output')
        mat.node_tree.links.new(emission.outputs['Emission'], output.inputs['Surface'])
        
        engine.data.materials.append(mat)
    
    return engines


def generate_wings(scale=1.0, symmetry=True, style='MIXED'):
    """
    Generate wing structures
    
    Args:
        scale: Ship scale factor
        symmetry: Use symmetrical design
        style: Design style
    """
    wings = []
    wing_length = scale * 0.8
    wing_width = scale * 0.15
    
    # Left wing
    bpy.ops.mesh.primitive_cube_add(
        size=1,
        location=(wing_length * 0.5, 0, 0)
    )
    left_wing = bpy.context.active_object
    left_wing.name = "Wing_Left"
    left_wing.scale = (wing_length, wing_width, wing_width * 0.3)
    bpy.ops.object.transform_apply(scale=True)
    wings.append(left_wing)
    
    if symmetry:
        # Right wing
        bpy.ops.mesh.primitive_cube_add(
            size=1,
            location=(-wing_length * 0.5, 0, 0)
        )
        right_wing = bpy.context.active_object
        right_wing.name = "Wing_Right"
        right_wing.scale = (wing_length, wing_width, wing_width * 0.3)
        bpy.ops.object.transform_apply(scale=True)
        wings.append(right_wing)
    
    return wings


def generate_weapon_hardpoints(count=2, scale=1.0, symmetry=True):
    """
    Generate weapon hardpoint markers
    
    Args:
        count: Number of weapon hardpoints
        scale: Ship scale factor
        symmetry: Use symmetrical placement
    """
    hardpoints = []
    hardpoint_size = scale * 0.1
    
    positions = []
    if symmetry and count % 2 == 0:
        # Symmetric placement
        for i in range(count // 2):
            y_pos = scale * 0.3 + (i * scale * 0.2)
            x_offset = scale * 0.3 + (i * scale * 0.1)
            positions.append((x_offset, y_pos, -scale * 0.1))
            positions.append((-x_offset, y_pos, -scale * 0.1))
    else:
        # Non-symmetric
        for i in range(count):
            y_pos = scale * 0.3 + (i * scale * 0.2)
            x_pos = (i - count / 2) * scale * 0.2
            positions.append((x_pos, y_pos, -scale * 0.1))
    
    for i, pos in enumerate(positions):
        bpy.ops.mesh.primitive_cylinder_add(
            radius=hardpoint_size,
            depth=hardpoint_size * 2,
            location=pos
        )
        hardpoint = bpy.context.active_object
        hardpoint.name = f"Weapon_Hardpoint_{i+1}"
        hardpoint.rotation_euler = (math.radians(90), 0, 0)
        hardpoints.append(hardpoint)
    
    return hardpoints


def register():
    """Register this module"""
    pass


def unregister():
    """Unregister this module"""
    pass
