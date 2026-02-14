# BlenderSpaceshipGenerator

A comprehensive Blender addon for procedurally generating spaceships with modular parts and interiors. Inspired by games like X4 Foundations, Elite Dangerous, and Eve Online.

## Features

- **Multiple Ship Classes**: Generate ships from small shuttles to massive capital ships
  - Shuttle
  - Fighter
  - Corvette
  - Frigate
  - Destroyer
  - Cruiser
  - Battleship
  - Carrier
  - Capital Ship

- **Modular Ship Parts**:
  - Hull with configurable geometry and complexity
  - Cockpit/Bridge appropriate to ship size
  - Multiple engine configurations
  - Wing structures for smaller vessels
  - Weapon hardpoints
  - Progressive module system for ship expansion

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

## Installation

1. Download or clone this repository
2. In Blender, go to Edit → Preferences → Add-ons
3. Click "Install" and select the downloaded folder or ZIP file
4. Enable the "Spaceship Generator" addon

## Usage

1. Open Blender and go to the 3D Viewport
2. Open the sidebar (press N if not visible)
3. Navigate to the "Spaceship" tab
4. Configure your ship:
   - Select ship class (Shuttle to Capital)
   - Choose design style
   - Set random seed for variation
   - Enable/disable interior generation
   - Adjust module slots
   - Set hull complexity
   - Toggle symmetry
5. Click "Generate Spaceship"

## Ship Classes

### Small Vessels
- **Shuttle**: Basic transport, 2 crew, minimal weapons
- **Fighter**: Single-seat combat, agile with wings
- **Corvette**: Small multi-crew, 4 crew, basic modules

### Medium Vessels
- **Frigate**: Multi-role ship, 10 crew, interior corridors
- **Destroyer**: Heavy combat focus, 25 crew, full interior

### Large Vessels
- **Cruiser**: Large multi-role, 50 crew, extensive interior
- **Battleship**: Heavy capital ship, 100 crew, many weapon hardpoints
- **Carrier**: Fleet carrier, 200 crew, hangar capacity
- **Capital**: Largest class, 500 crew, maximum module slots

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

