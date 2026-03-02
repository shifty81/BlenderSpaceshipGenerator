# BlenderSpaceshipGenerator

A comprehensive Blender addon for procedurally generating spaceships, textures, and catalog renders. This is the **asset pipeline tool** for the [NovaForge](https://github.com/shifty81/NovaForge) PVE space simulator, built on the Atlas Engine.

## NovaForge Asset Pipeline

This addon is the primary tool for generating and refining all 3D assets used by NovaForge:

- **Import ships from NovaForge JSON** — reads `data/ships/*.json` and generates matching geometry using each ship's faction, class, seed, `model_data` (turret_hardpoints, launcher_hardpoints, drone_bays, engine_count, generation_seed).
- **Batch generate** — process an entire `data/ships/` directory in one click to regenerate all ship meshes.
- **Faction-specific details** — Solari spires, Veyren armor panels, Aurelian organic pods, Keldari exposed framework struts match NovaForge's four races.
- **PBR material pipeline** — procedural diffuse, normal (panel lines + rivets), glow/emissive, and dirt/grime materials for full texture baking.
- **Catalog render setup** — one-click 3/4-view camera, three-point lighting, and transparent PNG output for ship catalog images.
- **Export OBJ for Atlas Engine** — correct +Z-forward coordinate system, NovaForge scale (1 game unit ≈ 50 m), companion material JSON.
- **All ship classes** — Frigates through Titans, plus Industrials, Mining Barges, and Exhumers.
- **Station generation** — procedural space stations matching NovaForge station types (Industrial, Military, Commercial, Research, Mining) and Upwell structures (Astrahus, Fortizar, Keepstar).
- **Asteroid belt generation** — procedural asteroid belts with all 16 NovaForge ore types and 4 belt layouts (Semicircle, Sphere, Cluster, Ring).

**→ [Feature Specification](features.md)** — complete feature list, design rules, and implementation status.

**→ [NovaForge Implementation Plan](NOVAFORGE_PLAN.md)** — phased roadmap for evolving this addon into a full PCG pipeline (galaxy, systems, planets, stations, ships, characters) with C++ integration, ECS architecture, multiplayer sync, and environmental simulation.

## Features

- **Multiple Ship Classes**: Generate ships from small shuttles to massive titans
  - Shuttle
  - Fighter
  - Corvette
  - Frigate
  - Destroyer
  - Cruiser
  - Battlecruiser
  - Battleship
  - Carrier
  - Dreadnought
  - Capital Ship
  - Titan
  - Industrial
  - Mining Barge
  - Exhumer

- **Modular Ship Parts**:
  - Hull with configurable geometry and complexity
  - Cockpit/Bridge appropriate to ship size
  - Multiple engine configurations
  - Wing structures for smaller vessels
  - Turret hardpoints (from NovaForge `model_data`)
  - Launcher hardpoints (missile/torpedo bays)
  - Drone bays (ventral recesses)
  - Progressive module system for ship expansion

- **Brick Taxonomy & LEGO Logic**:
  - 18 brick types across 5 categories (Core, Hull, Function, Utility, Detail)
  - Hardpoint declarations on every brick for snap-attach rules
  - Scale hierarchy bands (primary, structural, detail)
  - Grid snapping per ship class (0.5 m for shuttles up to 8 m for titans)
  - Ship DNA JSON export for reproducible/saveable ships

- **Spine-First Assembly Pipeline**:
  1. Core hull (spine)
  2. Cockpit / bridge
  3. Major structures (wings)
  4. Engines (archetype-varied)
  5. Weapons & turrets
  6. Detail modules
  7. Interior (optional)
  8. Hull taper / deform pass
  9. Bevel + auto-smooth cleanup pass

- **Engine Archetypes**:
  - Main Thrust — big, recessed, with nozzle flare
  - Maneuvering Thrusters — small, angled
  - Utility Exhaust — flat vents
  - Each archetype varies depth, radius, glow strength

- **Hull Shaping**:
  - Configurable hull taper for silhouette shaping
  - Automatic bevel + auto-smooth cleanup pass
  - Style-specific hull deformations (X4, Elite, EVE, NMS, factions)

- **Interior Generation**:
  - FPV-ready interiors scaled for human exploration
  - Corridor networks connecting ship areas
  - Bridge/cockpit interiors
  - Crew quarters with bunks
  - Cargo bays with containers
  - Engine rooms with reactor cores
  - Doorways and access points

- **Module System**:
  - Cargo modules
  - Weapon modules
  - Shield generators
  - Hangar bays
  - Sensor arrays
  - Power modules

- **Design Styles**:
  - X4 Foundations (Angular, geometric)
  - Elite Dangerous (Sleek, aerodynamic)
  - Eve Online (Organic, flowing)
  - Mixed (Combination of all styles)
  - **NovaForge Factions**:
    - Solari (Golden cathedral spires — armor tanking)
    - Veyren (Steel-blue blocky panels — shield tanking)
    - Aurelian (Green organic curves — drones)
    - Keldari (Rust-brown asymmetric framework — projectiles)

- **Station Generation**:
  - NPC station types: Industrial, Military, Commercial, Research, Mining
  - Upwell structures: Astrahus, Fortizar, Keepstar
  - Faction-specific architecture (spires, domes, blocks, scaffolding)
  - Docking bays and hangars

- **Asteroid Belt Generation**:
  - 16 ore types from NovaForge (Dustite through Nexorite)
  - 4 belt layouts: Semicircle, Sphere, Cluster, Ring
  - Procedural deformation for natural rocky shapes
  - PBR materials matching ore visual data

- **PBR Material Pipeline**:
  - Procedural hull materials with metallic/roughness workflow
  - Normal map generation via Voronoi panel lines and noise rivets
  - Glow/emissive materials for engines and running lights
  - Dirt/grime overlay materials with adjustable intensity
  - Faction-specific color palettes (Solari gold, Veyren steel, Aurelian green, Keldari rust)

- **Catalog Render Pipeline**:
  - One-click 3/4-view camera setup
  - Three-point lighting (key, fill, rim)
  - Transparent background PNG output
  - Thumbnail render mode (512×512)

- **NovaForge Export**:
  - OBJ export with +Z-forward, +Y-up coordinate system
  - Scale conversion (1 game unit = 50 m)
  - Companion material JSON with PBR properties

## Installation

1. Download or clone this repository
2. In Blender, go to Edit → Preferences → Add-ons
3. Click "Install" and select the downloaded folder or ZIP file
4. Enable the "Spaceship Generator" addon

## Usage

### Quick Generate

1. Open Blender and go to the 3D Viewport
2. Open the sidebar (press N if not visible)
3. Navigate to the "Spaceship" tab
4. Configure your ship:
   - Select ship class (Shuttle to Titan)
   - Choose design style (or a NovaForge faction)
   - Set random seed for variation
   - Set turret, launcher, and drone bay counts
   - Enable/disable interior generation
   - Adjust module slots
   - Set hull complexity
   - Toggle symmetry
5. Click "Generate Spaceship"

### NovaForge Pipeline

1. In the **NovaForge Integration** section, set the data directory to your NovaForge `data/ships/` folder
2. Click **"Generate from NovaForge JSON"** to import a single JSON file, or **"Batch Generate All Ships"** to process the entire directory
3. Each ship is generated using its `model_data` (seed, turrets, launchers, drones, engines) and race-to-faction style mapping
4. Click **"Setup Catalog Render"** to position the camera and lights for a catalog image
5. Use **File → Export → Export for NovaForge (.obj)** to export with the correct coordinate system and scale

## Ship Classes

### Small Vessels
- **Shuttle**: Basic transport, 2 crew, minimal weapons
- **Fighter**: Single-seat combat, agile with wings
- **Corvette**: Small multi-crew, 4 crew, basic modules

### Medium Vessels
- **Frigate**: Multi-role ship, 10 crew, interior corridors
- **Destroyer**: Heavy combat focus, 25 crew, full interior
- **Industrial**: Cargo hauler, 5 crew, large hold
- **Mining Barge**: Mining vessel, 3 crew
- **Exhumer**: Advanced mining vessel, 4 crew

### Large Vessels
- **Cruiser**: Large multi-role, 50 crew, extensive interior
- **Battlecruiser**: Heavy attack cruiser, 75 crew
- **Battleship**: Heavy capital ship, 100 crew, many weapon hardpoints
- **Carrier**: Fleet carrier, 200 crew, hangar capacity
- **Capital**: Large capital ship, 500 crew, maximum module slots

### Supercapital Vessels
- **Dreadnought**: Siege capital, 400 crew, devastating firepower
- **Titan**: Supercapital flagship, 1000 crew, doomsday weapons

## Progressive Module System

Ships can be expanded with additional modules based on their class:
- Small ships: Weapon, Shield, Sensor modules
- Medium ships: Also Cargo and Power modules
- Large ships: All module types including Hangar modules

Each module is automatically placed and connected to the ship with appropriate details.

## Interior Standards

All ship interiors are built to human scale for FPV exploration:
- Standard door height: 2.0m
- Corridor width: 1.5m
- Room height: 3.0m
- All dimensions support first-person navigation

## Customization

The addon supports extensive customization:
- **Random Seed**: Change to generate different ship variations
- **Hull Complexity**: Adjust geometry detail (0.1 - 3.0)
- **Module Slots**: Add 0-10 additional modules
- **Symmetry**: Toggle symmetrical design
- **Style**: Choose specific design inspiration or mixed

## Requirements

- Blender 2.80 or higher
- No additional dependencies required

## License

This project is open source and available for modification and distribution.

## Contributing

Contributions are welcome! Feel free to submit pull requests with improvements, new features, or bug fixes.

## Credits

Inspired by the spaceship designs from:
- X4 Foundations by Egosoft
- Elite Dangerous by Frontier Developments
- Eve Online by CCP Games

