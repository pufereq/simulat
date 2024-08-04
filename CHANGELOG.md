# Changelog

All notable changes to this project will be documented in this file.

## [0.18.0] - 2024-08-04

### Features

- [`4f353b9`](https://github.com/pufereq/simulat/commit/4f353b9a574a4d09c96b594bf0d6c738e76089af) **surface.py**: rewrite `Surface.blit_text()` method
- [`de1ebf6`](https://github.com/pufereq/simulat/commit/de1ebf6c85aa861cb956aa0c7b79119bbeeb7f91) **colors.py**: add `hex_to_rgba()` function

### Miscellaneous Tasks

- [`08619e3`](https://github.com/pufereq/simulat/commit/08619e3af9e7f114f88223f841848b4d85c4ad2a) **game.py**: add `__str__` and `__repr__` methods to `Simulat`
- [`20ae4d4`](https://github.com/pufereq/simulat/commit/20ae4d4d458d77754c006f2d3e2500d6677ae251) **surface.py**: change default value for `antialias` argument of `Surface.blit_text()` to False
- [`e06b292`](https://github.com/pufereq/simulat/commit/e06b292df66ded9c8be089cfdb730b38152ac40f) **game.py**: migrate from `pygame.ftfont.Font` to `pygame.Font` for font handling
- [`869b485`](https://github.com/pufereq/simulat/commit/869b485c543b48343cc860c9ff400c799f5c56eb) [**breaking**] move `src/simulat/` -> `simulat/`

### Refactor

- [`59cd0ae`](https://github.com/pufereq/simulat/commit/59cd0aec6585911c2e6bce31f049ad47f00d83c7) **button.py**: adjust `blit_text()` arguments after rewrite
- [`58ac5c6`](https://github.com/pufereq/simulat/commit/58ac5c6b280a7394d70425e1091a239aa78f5e1d) **sidebar.py**: adjust `blit_text()` arguments after rewrite
- [`57a71c9`](https://github.com/pufereq/simulat/commit/57a71c95e59ead149c8e93b936209c24a21a80d2) **debug_screen.py**: adjust `blit_text()` arguments after rewrite
- [`685b772`](https://github.com/pufereq/simulat/commit/685b772cbccd5093c68eb3b6a189b211186f409e) **topbar.py**: modify arguments to `blit_text()` after rewrite

### Build

- [`d19f63c`](https://github.com/pufereq/simulat/commit/d19f63c098bab9d1b201e0f3f5e7d62b45d82fd1) **requirements.txt**: [**breaking**] migrate to pygame-ce

## [0.18.0-dev.1] - 2024-06-23

### Bug Fixes

- [`93152ee`](https://github.com/pufereq/simulat/commit/93152ee8ae7bf4e45cce19effe82364f6c8469e4) **entity.py**: fix error on `Entity.current_tile()` call if entity is out of bounds

### Documentation

- [`b1a624d`](https://github.com/pufereq/simulat/commit/b1a624d279d56a4c324877e8a2a1a65b6ed44e2d) **FEAT.yaml**: remove contact information input
- [`c6077d4`](https://github.com/pufereq/simulat/commit/c6077d4db832ac20cfd7858c33c9ac9d757ed993) **BUG.yaml**: remove contact information input

### Features

- [`a08e724`](https://github.com/pufereq/simulat/commit/a08e72499869b0d6d81063aca367f40bc4c6fb1f) **debug_screen.py**: add a debug screen
- [`62777af`](https://github.com/pufereq/simulat/commit/62777afb05c45c81030e716469200249c9f2e0bf) **surface.py**: add `antialias` argument

### Miscellaneous Tasks

- [`477fdde`](https://github.com/pufereq/simulat/commit/477fdde311b9c02d6c0c3facdb8bd812ad3a6d54) **release**: 0.18.0-dev.1
- [`959e3af`](https://github.com/pufereq/simulat/commit/959e3af5aa3985b47d91dea5ab5af644d8f992fd) **game_map.py**: use the `DebugScreen`, toggled using `F9`
- [`17143ac`](https://github.com/pufereq/simulat/commit/17143ac18a4af86e7d63a6350951539c1993040a) **game.py**: add a `Simulat.version` constant
- [`0298b12`](https://github.com/pufereq/simulat/commit/0298b124f8826fa332309d0e48192c295143a700) **main_menu_scene.py**: remove unused loading screen

### Refactor

- [`8cf721c`](https://github.com/pufereq/simulat/commit/8cf721cc2a6c6a206f9963dc7901f754bea35cd9) **game_map.py**: change `GameMap.update()` method to adapt to changes in `Entity.current_tile`
- [`eebf61c`](https://github.com/pufereq/simulat/commit/eebf61c1d53397cf6913ab24dcac06d1dc199aa4) **sidebar.py**: change `Surface.add_text()` call to `blit_text()`
- [`4cf554b`](https://github.com/pufereq/simulat/commit/4cf554bd884abb9ab78eca3662e52096650a7080) **surface.py**: rename `Surface.add_text()` to `blit_text()`

### Styling

- [`6ca841c`](https://github.com/pufereq/simulat/commit/6ca841c9199a3aa9db982d4d178fbe710e189223) **main_menu_scene.py**: format module using black
- [`0350157`](https://github.com/pufereq/simulat/commit/0350157919a9979f86ef83429d92594585aec771) **scene.py**: format module using black

## [0.17.2] - 2024-06-21

### Documentation

- [`a4c17e9`](https://github.com/pufereq/simulat/commit/a4c17e9061b0f1b8d378be532474498aea65bfa4) add issue templates

### Miscellaneous Tasks

- [`53cb1fd`](https://github.com/pufereq/simulat/commit/53cb1fd09251cfae832268d3d874fd138ff45517) **release**: 0.17.2

## [0.17.1] - 2024-06-18

### Bug Fixes

- [`a166680`](https://github.com/pufereq/simulat/commit/a166680f182ed56eb0df729dcf335dd484b6fc73) **game.py**: fix error on outdated config

### Miscellaneous Tasks

- [`f47c323`](https://github.com/pufereq/simulat/commit/f47c3230013afd7d123d0fefbb56eafb3eb2c1d2) **release**: 0.17.1

## [0.17.0] - 2024-06-18

### Features

- [`a0f3492`](https://github.com/pufereq/simulat/commit/a0f34926b57a64dd4fb72879f5104fb442740e07) **game.py**: use `ConfigHandler`
- [`13090a9`](https://github.com/pufereq/simulat/commit/13090a9710f97502100aa04362622f146748c257) **config_handler.py**: add `ConfigHandler`

### Miscellaneous Tasks

- [`c076567`](https://github.com/pufereq/simulat/commit/c076567c874d1ead84dc4897ab81d9a0fa28d3b9) **release**: 0.17.0
- [`5b14c9b`](https://github.com/pufereq/simulat/commit/5b14c9b54e14f90d74096d59f1e9e7a5479d31dc) add `data/user/` folder for storing user data
- [`dcd211d`](https://github.com/pufereq/simulat/commit/dcd211ddbaad985e9f188d07b46c98445d081c22) rename `src/simulat/core/characters` to `src/simulat/core/entities`

### Refactor

- [`c37eb27`](https://github.com/pufereq/simulat/commit/c37eb27a76a5067239a3fb0a0a33960ea707fff3) **game.py**: rename `Simulat._init_next()` method to `init_next()`
- [`5c03e67`](https://github.com/pufereq/simulat/commit/5c03e67078d5d83a486051c2a42cb16e7128281e) **tiles.yaml**: rename `tiles.yml` to `tiles.yaml`
- [`19f3a07`](https://github.com/pufereq/simulat/commit/19f3a07d2aec7fcbd70a0a194bb80331825f26fb) **world.py**: change the `Character` imports to point to `Entity`

### Build

- [`4d5d91a`](https://github.com/pufereq/simulat/commit/4d5d91abebb741951468dff1559eda7d6542cca5) **.gitignore**: add `data/user/` folder to gitignore
- [`332f72e`](https://github.com/pufereq/simulat/commit/332f72e8977984f66915e0c7db912ac7f2ec7bff) **requirements.txt**: add a dependency on `cerberus`

## [0.16.1] - 2024-06-17

### Miscellaneous Tasks

- [`6efef1a`](https://github.com/pufereq/simulat/commit/6efef1aaa10ee5a95d5cc0fa6a1fa3c89c6b1be8) **release**: 0.16.1
- [`a5d1ae6`](https://github.com/pufereq/simulat/commit/a5d1ae6730eed6459c65958c1306df68322f573d) **release.yml**: fix typo
- [`9885fa0`](https://github.com/pufereq/simulat/commit/9885fa0574e97787c3a191c640501d3099d837ff) **release.yml**: add pre-release input and disable version drafting

## [0.16.0] - 2024-06-17

### Features

- [`026288f`](https://github.com/pufereq/simulat/commit/026288fa410ba7bf1e0a604f7623b95c42ec220b) **map_tile.py**: add multiple texture randomization
- [`4e38bfc`](https://github.com/pufereq/simulat/commit/4e38bfcb86d5b5e592cd69e2c0fd00ed3821c479) **tile_manager.py**: add support for multiple textures for one tile

### Miscellaneous Tasks

- [`6cf2924`](https://github.com/pufereq/simulat/commit/6cf292428b4d12fc897254dcfc020980c459f85d) **release**: 0.16.0
- [`884acd7`](https://github.com/pufereq/simulat/commit/884acd741940ab8f3a17a5f1a360b705e4bb0be6) **tiles.yml**: use new textures
- [`53116e6`](https://github.com/pufereq/simulat/commit/53116e6217f2b9fff7ea889c80b5d67794a388c5) **grass.png**: remove old grass texture
- [`6a03942`](https://github.com/pufereq/simulat/commit/6a03942edc56193ac5dca34a58cf9c79b8c34613) add more grass textures
- [`d92043d`](https://github.com/pufereq/simulat/commit/d92043d012dd7c1f44b5f92c9b6d07c21ac480be) **map_tile.py**: add `MapTile.instances` counter and `MapTile.instance_num` for randomization purposes
- [`b617cd0`](https://github.com/pufereq/simulat/commit/b617cd053033c0145e413363eb372b974337a3f9) **tile_type.py**: remove `TileType.draw()` method as drawing is handled by `MapTile`
- [`7c2d410`](https://github.com/pufereq/simulat/commit/7c2d41098144dc5af6ac4c49cf9d36f9c6bf6116) **map_tile.py**: add `pos` argument to `MapTile.draw()` and call `blit`

### Refactor

- [`96fd57b`](https://github.com/pufereq/simulat/commit/96fd57b4d2b5196cef5e32732e2b6f4d3f074258) **game_map.py**: use `tile.draw` method instead of manually blitting a tile
- [`6b48904`](https://github.com/pufereq/simulat/commit/6b48904278459f4a711c6a6a4bcacb4dc0c746d0) **tile_type.py**: rename `TileType.texture` to `TileType.textures`
- [`afe7d6f`](https://github.com/pufereq/simulat/commit/afe7d6fd9e1d163ab95bc8b55a52e37894ee8d0c) **map_tile.py**: set `MapTile.rect` based on `TILE_SIZE` rather then texture size

## [0.15.0] - 2024-06-13

### Bug Fixes

- [`a754dc2`](https://github.com/pufereq/simulat/commit/a754dc2568b45d495fe9c48912a12424a7e57eae) **grass.png**: fix rotation of grass texture
- [`8229799`](https://github.com/pufereq/simulat/commit/8229799aa04ce2d9a8a29e65795222ddf8a205d9) **tile_manager.py**: handle empty `tiles.yml` parsing gracefully

### Features

- [`b5e51ac`](https://github.com/pufereq/simulat/commit/b5e51acf1b2f91919360fe7b08f0b7773acaedc1) **tile_manager.py**: add fallback for missing tiles in `id_to_tile()` function
- [`b048e7d`](https://github.com/pufereq/simulat/commit/b048e7d1d5d3895c958e48ece4a174f3aeca0bdb) **tile_manager.py**: add `missing` tile (as a fallback)
- [`f3be33c`](https://github.com/pufereq/simulat/commit/f3be33c15a0365c66bc5706315b7437f8f9cc4dc) **world.py**: add `World.set_tile()` method
- [`6ace62c`](https://github.com/pufereq/simulat/commit/6ace62c8474273786fedf9d2e671b1e876e8cf58) **world.py**: add `World.get_tile()` method
- [`bc190c7`](https://github.com/pufereq/simulat/commit/bc190c74031f3b15663fd8e8b619d83ac9200958) **world_manager.py**: add world_manager.py for world management
- [`06a76ad`](https://github.com/pufereq/simulat/commit/06a76ad5f2a489b03d9f08f35c5470e070a1a797) **debug_world.py**: add a debug world
- [`d371169`](https://github.com/pufereq/simulat/commit/d371169df86941c2ac99a8b7fe3cc50f6e438ac3) **world.py**: add `World` class
- [`dc66f87`](https://github.com/pufereq/simulat/commit/dc66f876d51e5450b36439eb3c27e1089523877f) **map_tile.py**: add MapTile class
- [`c4f2892`](https://github.com/pufereq/simulat/commit/c4f28921380caa5bf5d803d12d2014f9e9506551) **tile_manager.py**: add tile_manager.py
- [`54dbed2`](https://github.com/pufereq/simulat/commit/54dbed2716b40a9a49c5982eeb4bf03ead8e5d70) **textures.py**: add textures module
- [`7b98d86`](https://github.com/pufereq/simulat/commit/7b98d86f40dbacdebe2432f12c66cbf3768feb6b) **tile_type.py**: add TileType class to define the different types of tiles

### Miscellaneous Tasks

- [`366379d`](https://github.com/pufereq/simulat/commit/366379d6791c99c72de4314b64fcad7c3afde87f) **release**: 0.15.0
- [`0d43cdc`](https://github.com/pufereq/simulat/commit/0d43cdca966613ea78637bd73f82c2daf8c49200) **world.py**: make `World.generate_chunk()`'s argument a tuple of ints
- [`03d5903`](https://github.com/pufereq/simulat/commit/03d5903091b4ead85f18586ff18218b1d4b6666a) **character.py**: refactor Character class to support the new GameMap
- [`499b10d`](https://github.com/pufereq/simulat/commit/499b10d641cbe60eb6677c22cedcef79a46606e3) **player.py**: refactor player class for support of the new GameMap
- [`1a0e574`](https://github.com/pufereq/simulat/commit/1a0e57478b9f2b6dc82c2006046b1ae792c4e25a) **bricks.png**: add bricks tile texture
- [`065666a`](https://github.com/pufereq/simulat/commit/065666ae830220d6b6925a5a5ddd8a36e747132d) **grass.png**: add grass tile texture
- [`3d51b9f`](https://github.com/pufereq/simulat/commit/3d51b9f1a3466a380287ed3aa5a4f7c5208ef10a) **tiles.yml**: add tiles configuration file
- [`b2c9712`](https://github.com/pufereq/simulat/commit/b2c9712bb14c4bde28c6ef3bca6c45668176bd2c) **tile.py**: remove tile.py for splitting
- [`7ae2c38`](https://github.com/pufereq/simulat/commit/7ae2c3845990299f21c6733deee47181008d5d39) **game_scene.py**: remove rounded corner overlay
- [`d775ce7`](https://github.com/pufereq/simulat/commit/d775ce7cf88b49f942ea505331461fa20c907570) **camera.py**: untie camera size from `GameMap.display_size` variable
- [`de943aa`](https://github.com/pufereq/simulat/commit/de943aa1f5004e6720e87a517c7950d364020ee8) **character.py**: rename `unit` attribute to `size_unit` for clarity
- [`261a4f2`](https://github.com/pufereq/simulat/commit/261a4f27ac864c7bb0d46c6492fc7a51f7775018) **map_layout.py**: remove map_layout.py
- [`9331d43`](https://github.com/pufereq/simulat/commit/9331d4344290b60cfd2f2cbde3dd730415528cb2) remove `ColliderTile` and `DecorativeTile` classes
- [`a2d1e04`](https://github.com/pufereq/simulat/commit/a2d1e04d59b6ce115dca1c2054faddbd7ee89e45) [**breaking**] move `src/simulat/core/surfaces/game_map` to `src/simulat/core/scenes/game_scene/game_map`
- [`3620c4d`](https://github.com/pufereq/simulat/commit/3620c4d77df9a1736d2676f64d18c7e255040cba) **simulat.ttf**: size changes (9px → 12px)
- [`569eae0`](https://github.com/pufereq/simulat/commit/569eae010741e6149152b05cf37f7fe67f234ab3) move `src/simulat/core/surfaces/scenes` to `src/simulat/core/scenes`
- [`4ed0cc1`](https://github.com/pufereq/simulat/commit/4ed0cc18e857ef5da6453f9f636288e04215e2bf) **colors.py**: move colors.py to `src/simulat/core/`

### Refactor

- [`ae9b640`](https://github.com/pufereq/simulat/commit/ae9b64037f8b95c64f92a6b0ec9f764f05e5437c) **game_map.py**: adjust `world.generate_chunk()` arguments
- [`4b89eef`](https://github.com/pufereq/simulat/commit/4b89eeff94d526b575d856fc4a9026fd9c6e1b4e) **camera.py**: refactor Camera class to support the new GameMap
- [`fb6755e`](https://github.com/pufereq/simulat/commit/fb6755e23c858c6713210bf7ca10c1caee1acfc8) **game_map.py**: rewrite the `GameMap` class

### Styling

- [`dbd9802`](https://github.com/pufereq/simulat/commit/dbd9802f9ba0e9d060a7e024597022cc1bb8f0f2) **button_container.py**: change import order
- [`61b1cf4`](https://github.com/pufereq/simulat/commit/61b1cf47d6ee169be43c5d2659cfadbeaa004bf4) **button.py**: change import order
- [`188bce6`](https://github.com/pufereq/simulat/commit/188bce6f6828f19aea3478e0f652851988cb574d) use black formatter

### Build

- [`b308ad1`](https://github.com/pufereq/simulat/commit/b308ad1e41dec51d843d2895bb904fad42c43578) **requirements.txt**: add PyYAML dependency
- [`d08bb65`](https://github.com/pufereq/simulat/commit/d08bb65454cd0800e561e4774c1d35d0d659367a) **.vscode/settings.json**: set type checking mode to strict

## [0.14.0] - 2024-05-08

### Features

- [`93d4014`](https://github.com/pufereq/simulat/commit/93d401432e76f09c848a3e7ad3d56c570f22aca5) **simulat.ttf**: add the simulat font
- [`ae58007`](https://github.com/pufereq/simulat/commit/ae58007a3ef5715fde9abf8952e298e53b55833f) **button_container.py**: add calculations to ensure correct mouse interaction independetly from resolution
- [`5c574e6`](https://github.com/pufereq/simulat/commit/5c574e6c16cf819efb929f4688ba256608faf6dc) **game.py**: add `Simulat.internal_screen` and `Simulat.display` surfaces

### Miscellaneous Tasks

- [`388af08`](https://github.com/pufereq/simulat/commit/388af08992865cd143736bc7963fc560b24817b8) **release**: 0.14.0
- [`5220601`](https://github.com/pufereq/simulat/commit/5220601e2b70c1cadbc607e66ca70d5ba86111e6) **game.py**: use the simulat font
- [`6be9dcd`](https://github.com/pufereq/simulat/commit/6be9dcd8f32eda3635dd062e3e89ced12eb37423) **game.py**: decrease font sizes
- [`61af88b`](https://github.com/pufereq/simulat/commit/61af88b840e2b8fe0df8981076eee81a47f4a4d2) **main_menu_scene.py**: change position and scaling of logo on main menu
- [`e79bed3`](https://github.com/pufereq/simulat/commit/e79bed33bc13a93ac7839f3f893cfe76a08dfbc0) **main_menu_scene.py**: correct wrong button size and position on main menu
- [`37097d2`](https://github.com/pufereq/simulat/commit/37097d2189969f09e3603d8fcd16d7c0320a4883) **tile.py**: lower the `TILE_SIZE` to 32px for consistent scale
- [`f0f2b22`](https://github.com/pufereq/simulat/commit/f0f2b222e356e787c02839eb9a001ac47d22e784) **sidebar.py**: adjust button rounded corner radius for consistency with pre-scaling style
- [`2019fa4`](https://github.com/pufereq/simulat/commit/2019fa4e066bf179bcbf50980d13f7dbf70a5851) **sidebar.py**: adjust sidebar width for consistency with pre-scaled size
- [`a8232e8`](https://github.com/pufereq/simulat/commit/a8232e8d05faafb35d1422cc34de401cb758022d) **game.py**: draw scaled to `DISPLAY_SIZE``internal_screen` onto the `display`

### Refactor

- [`6d08e33`](https://github.com/pufereq/simulat/commit/6d08e337b346871b72c17f33ddddf40b4654ae73) **scene.py**: replace `simulat.SIZE` with `simulat.INTERNAL_SCREEN_SIZE` for consistency
- [`93e4c9c`](https://github.com/pufereq/simulat/commit/93e4c9c391a85a7c8ee84b4a86f282722c4d3f2e) **topbar.py**: replace `simulat.SIZE` with `simulat.INTERNAL_SCREEN_SIZE` for consistency
- [`d6d97fe`](https://github.com/pufereq/simulat/commit/d6d97fe8a27ccbf1a01cd583c82f06cc98847ab8) **game.py**: replace `Simulat.screen` surface calls with `internal_screen`
- [`75b690c`](https://github.com/pufereq/simulat/commit/75b690c6cfaded38de5f360cb5669d481aae3db6) **game.py**: rename variable `Simulat.SIZE` -> `Simulat.INTERNAL_SCREEN_SIZE`
- [`afc6b8e`](https://github.com/pufereq/simulat/commit/afc6b8e3b957a85ce149de667fdd4eb16e62a49a) move `src/simulat/assets/` to `assets/`

## [0.13.0] - 2024-05-06

### Features

- [`fe76834`](https://github.com/pufereq/simulat/commit/fe768340d69e4d6c091ed5a2d909a817efb3613e) **game_map.py**: show camera position on topbar when detached
- [`b30de9e`](https://github.com/pufereq/simulat/commit/b30de9e140242ac3f960a97fa505def2b8d9371d) **camera.py**: cap camera position within player's distance

### Miscellaneous Tasks

- [`ec8d20e`](https://github.com/pufereq/simulat/commit/ec8d20e5035abd3f7e06f78427ef73b340197b49) **release**: 0.13.0

### Refactor

- [`f0667c2`](https://github.com/pufereq/simulat/commit/f0667c29f2f055b2d3475d53e53d6a71829e302f) **game_map.py**: move `update_title` call from Player's `render()` method to `GameMap.update()`

## [0.12.2] - 2024-05-05

### Bug Fixes

- [`0832fdb`](https://github.com/pufereq/simulat/commit/0832fdb62569d823d52d117efd9c1657bc723ae7) **character.py**: fix clunky collision handling

### Miscellaneous Tasks

- [`b9a984e`](https://github.com/pufereq/simulat/commit/b9a984e3e845fa4059a2d39fadfe0fcb90038cac) **release**: 0.12.2
- [`946a90e`](https://github.com/pufereq/simulat/commit/946a90e3516bca4936c90ba88f6cb5d83f5646a2) **character.py**: add `Character.move_to()` method
- [`3b6ac20`](https://github.com/pufereq/simulat/commit/3b6ac20e569aa81ad3e88f1ee9d9a88cc9c050c9) **character.py**: make `Character._check_collision()` return Tile or None

## [0.12.1] - 2024-05-04

### Miscellaneous Tasks

- [`b1971f8`](https://github.com/pufereq/simulat/commit/b1971f8aa152ba06c5bf45c540de0ca8479541c0) **release**: 0.12.1
- [`8c71fc3`](https://github.com/pufereq/simulat/commit/8c71fc3712ed863eeb5c59dbc05684ee9053c053) **release.yml**: after release, merge into develop

## [0.12.0] - 2024-05-04

### Documentation

- [`be6c716`](https://github.com/pufereq/simulat/commit/be6c7161843d0f08281987a7e9167e26f39a6c3e) **button_container.py**: add Usage section to class docstring
- [`815dd8d`](https://github.com/pufereq/simulat/commit/815dd8d4f4771e6deba2521e83a8b190c849bde5) **README.md**: modify the commit since latest release badge to show data from develop

### Features

- [`db70519`](https://github.com/pufereq/simulat/commit/db70519fb77a745bcbae30454f4782f314a22302) **main_menu_scene.py**: use button container
- [`bb021d7`](https://github.com/pufereq/simulat/commit/bb021d7f856decec3f2b652639f0aef77e3e8fd9) **button_container.py**: add a button container class

### Miscellaneous Tasks

- [`e1ecf09`](https://github.com/pufereq/simulat/commit/e1ecf09c3dfc5fae7d5fe4c2416a7f0538f36840) **release**: 0.12.0
- [`c07ada0`](https://github.com/pufereq/simulat/commit/c07ada0463abcbe8ffe48c421d019cd16bb23fcf) **button.py**: add `Button.pos` attribute and make `rect` independent
- [`5053faa`](https://github.com/pufereq/simulat/commit/5053faae71dbc7a91f88d13109818987236414fc) **sidebar.py**: change attribute naming for clarity
- [`341668b`](https://github.com/pufereq/simulat/commit/341668bde0e3ac3cd0d386a15e842d762dc5483a) **scene.py**: add `Scene.pos` attribute

## [0.11.1] - 2024-04-07

### Documentation

- [`ec5a5f6`](https://github.com/pufereq/simulat/commit/ec5a5f6ab2b30fb2245d9ea7eb2916ee18395fa2) **README.md**: use the SVG logo

### Miscellaneous Tasks

- [`7cbb467`](https://github.com/pufereq/simulat/commit/7cbb4672aef59fcfc0908f40d9ff82bbcd2ff905) **release**: 0.11.1
- [`fdaac38`](https://github.com/pufereq/simulat/commit/fdaac38b1eb35ca874d1d2dee026473b81175b38) **main_menu_scene.py**: change the displayed logo
- [`3ce3cad`](https://github.com/pufereq/simulat/commit/3ce3cad56dae68c620ff790db0460af75ff2abe2) remove `logo_transparent.png` in favor of new SVG render `logo.png`
- [`c15e59b`](https://github.com/pufereq/simulat/commit/c15e59b105e290522bc96c72ba88df21a31b7107) **logo.svg**: make logo a SVG
- [`2e1a0ee`](https://github.com/pufereq/simulat/commit/2e1a0eeed22b74bc5a60ae05becb83262edfd5fb) **banner_big.png**: add a bigger version of the banner
- [`98981e5`](https://github.com/pufereq/simulat/commit/98981e579face3a36fd32741f0e574c3a53afc8b) **banner.png**: move `banner.png` to `banner/banner.png`
- [`e5c7c1e`](https://github.com/pufereq/simulat/commit/e5c7c1e43c3574db04c82bddfa43167975815a4a) **logo_menu.png**: include scaled version of logo for main menu
- [`f6b5ed7`](https://github.com/pufereq/simulat/commit/f6b5ed7301c38e0765e8696fe870f956296ab50d) **logo_bloom.png**: remove the bloom version of logo
- [`e13398e`](https://github.com/pufereq/simulat/commit/e13398e3e89a2336e2942cb6137ea29e85a9726c) **logo_transparent_bloom.png**: remove the transparent bloom version of logo

## [0.11.0] - 2024-04-06

### Bug Fixes

- [`37607ce`](https://github.com/pufereq/simulat/commit/37607ce55ea74f47b0ba899bf008db48e053ad59) **game.py**: fix `focus_surface` making duplicates of focused surfaces
- [`b3d3034`](https://github.com/pufereq/simulat/commit/b3d3034f5c764ff3ff332f68f7ef21f196d74492) **game.py**: fix no events being passed to `surface.input()`

### Documentation

- [`4b07904`](https://github.com/pufereq/simulat/commit/4b079045b8b49822b96802c2d603ad8c0be33251) **README.md**: add logo
- [`e55b996`](https://github.com/pufereq/simulat/commit/e55b996816b5b08aa46fef6f43a42a5325bf10a6) **game_map.py**: add a logger call at beginning of `GameMap.__init__`

### Features

- [`20db862`](https://github.com/pufereq/simulat/commit/20db862eab96d5d68373265dec61dd507e49a9c2) **main_menu_scene.py**: display logo
- [`3802193`](https://github.com/pufereq/simulat/commit/3802193c8cf389e2542e3a456b78628f423de173) **main_menu_scene.py**: add buttons to main menu
- [`2a3a6a9`](https://github.com/pufereq/simulat/commit/2a3a6a9469b26c646225fa80640a6d8be8803c48) **button.py**: add `Button`s
- [`ecd235b`](https://github.com/pufereq/simulat/commit/ecd235bba31225545184be8d64050c29de9f9448) **game.py**: add helper methods `Simulat.focus_surface()` and `Simulat.unfocus_surface()`
- [`e13cf20`](https://github.com/pufereq/simulat/commit/e13cf206f12cc090667696a6e69eb2bb5e0a2ea6) **game.py**: add `Simulat.quit()` method
- [`89ec98d`](https://github.com/pufereq/simulat/commit/89ec98d23b8059eb04b91ebca7b93a82e55a3ebb) **main_menu_scene.py**: add main menu scene
- [`631dd20`](https://github.com/pufereq/simulat/commit/631dd202b5e7e85b3cad2fc17cf1d133717fb467) **game.py**: add `Simulat.change_scene()` method

### Miscellaneous Tasks

- [`40498a9`](https://github.com/pufereq/simulat/commit/40498a9c324e4bc920c8282f4633c5e53221822f) **release**: 0.11.0
- [`f5a507f`](https://github.com/pufereq/simulat/commit/f5a507fdaccf04dc7b0fd459be560732b13e2f08) add simulat logos
- [`95f71da`](https://github.com/pufereq/simulat/commit/95f71daa42dabe2e7fad89521379b943259ea090) **main_menu_scene.py**: move separate imports to one module-wide
- [`6c8896e`](https://github.com/pufereq/simulat/commit/6c8896e9c282f0d9e4ada57eab5da39657e4d523) **main_menu_scene.py**: add `_start_load_thread()` helper method
- [`0ad4825`](https://github.com/pufereq/simulat/commit/0ad4825159851f06f723f063c320e41d6b811287) **game_map.py**: provide more detailed loading progress to main menu
- [`352e42b`](https://github.com/pufereq/simulat/commit/352e42b076b0600393c2249e2e86917f36f210ea) **main_menu_scene.py**: add support for more detailed loading progress
- [`1bc4ed4`](https://github.com/pufereq/simulat/commit/1bc4ed4a6e466a0ab9197bd1b7fc483b673927e6) **button.py**: change default font to `button`
- [`3d778e3`](https://github.com/pufereq/simulat/commit/3d778e3fd666b1100aabc2bf3b37c8243db1c1e7) **game.py**: add `button` font
- [`5fc223e`](https://github.com/pufereq/simulat/commit/5fc223ed347f3efe2610986c20471f993118f0f4) **colors.py**: add `ACCENT_BLUISH_DISABLED` color
- [`57dc429`](https://github.com/pufereq/simulat/commit/57dc429c5b901e48544e0d4891b3ef96f74037b6) **colors.py**: [**breaking**] rename `ACCENT` -> `ACCENT_PURPLE`
- [`f8c2e92`](https://github.com/pufereq/simulat/commit/f8c2e9253c4e7f00d9a0a720e3571291a5f5321b) **colors.py**: [**breaking**] rename `ACCENT1` -> `ACCENT_BLUISH`
- [`62dfb45`](https://github.com/pufereq/simulat/commit/62dfb45fc37802856a49feb78af37ae80a8f05c4) **game.py**: provide `mouse_pos` and `mouse_buttons` to focused surfaces' `input()` methods
- [`5dd46af`](https://github.com/pufereq/simulat/commit/5dd46af3af313b581d02e0ed7b929c9630be20b8) **surface.py**: add `Surface.input()` method
- [`a11a67b`](https://github.com/pufereq/simulat/commit/a11a67b126e2a6bde74ddf8d99ff8662a5ddf74f) **scene.py**: add `Scene.input()` method
- [`bdf12ca`](https://github.com/pufereq/simulat/commit/bdf12cad5cae64a11ed476df740d4ac24e7adec9) **main_menu_scene.py**: add `mouse_pos` and `mouse_buttons` arguments to `input()`
- [`c0985d3`](https://github.com/pufereq/simulat/commit/c0985d3aae9fb37df9121266280c9e0ad097c3de) **game_scene.py**: add `mouse_pos` and `mouse_buttons` arguments to `input()`
- [`d466b93`](https://github.com/pufereq/simulat/commit/d466b93457feb6fe30652fdc7a02ac07ba1e6a3e) **game.py**: make `Simulat.focused_surfaces` a list for clarity
- [`3be14a7`](https://github.com/pufereq/simulat/commit/3be14a715b09e3fe6cb4f47655862148103453ef) **game_map.py**: supply the `MainMenuScene.game_map_loading_progress` variable
- [`27cd468`](https://github.com/pufereq/simulat/commit/27cd468948ff76a8609cb3501b5110b239e89e2c) **main_menu_scene.py**: add progress to game map loading screen
- [`0261464`](https://github.com/pufereq/simulat/commit/026146411c324bad57639fdaf502d141f8fd5e34) **main_menu_scene.py**: add welcome text
- [`22f3634`](https://github.com/pufereq/simulat/commit/22f363441b5f747d3335a3d6bacd14c42afd7b4e) **game.py**: remove duplicate init of `GameMap`
- [`f615b82`](https://github.com/pufereq/simulat/commit/f615b8266ccb7179262d3c2aa94cd105fcbcc847) **game_scene.py**: remove `GameMap` from `simulat.focused_surfaces`
- [`29d385f`](https://github.com/pufereq/simulat/commit/29d385fcb6d8844ed3f05aa8e0cb5e3024df08bc) **game_scene.py**: add `GameScene.input()` to redirect input to `GameScene.game_map.input`
- [`862461d`](https://github.com/pufereq/simulat/commit/862461d0b7833a3ed56470906209e5aa9d1204a1) **game_map.py**: remove unnecesarry import
- [`4eaa017`](https://github.com/pufereq/simulat/commit/4eaa017b09172a593574d326ae7072383c2c2ee6) **game_map.py**: remove `time_it()` decorator from `GameMao._init_tiles()`
- [`e502834`](https://github.com/pufereq/simulat/commit/e502834c754b6ecb0fccb153597d104e410d34bb) **game.py**: add a thread name field to loggers
- [`0c2d516`](https://github.com/pufereq/simulat/commit/0c2d516eb0370dcf65aca9993e50335041011107) **game.py**: add call to `change_scene()` in `run()` instead of setting `active_scene`
- [`488cb4e`](https://github.com/pufereq/simulat/commit/488cb4ef4375a75ef7f73346248cdeb053b5dc8d) **game.py**: init `MainMenuScene` in `Simulat._init_scenes()`
- [`9dbe0f6`](https://github.com/pufereq/simulat/commit/9dbe0f64bdcb9ab2d06733dc25c9e494faa4fdf9) **game.py**: provide `events` argument in call to `surface.input()` in `run()`
- [`f45572b`](https://github.com/pufereq/simulat/commit/f45572bf538d159ae31cdfa2c5bebcad6a535768) **game_map.py**: add `events` argument to `GameMap.input()`
- [`5bc3c47`](https://github.com/pufereq/simulat/commit/5bc3c47af95b3a6b1d33ae0088bf600d5bfdbbb4) **release**: 0.10.0

### Styling

- [`b1ce976`](https://github.com/pufereq/simulat/commit/b1ce976788c3a547d6f59d259dba0d0c6e5ae482) **game.py**: make font definitions cleaner
- [`5fab889`](https://github.com/pufereq/simulat/commit/5fab889d4428a90bb8f0f5b91b6bcbed335f923b) **main_menu_scene.py**: correct placement of `MainMenuScene._load_game()` in code
- [`fcc4987`](https://github.com/pufereq/simulat/commit/fcc498783a7cb9ef1dd995e89fc83c203ee8460c) **main_menu_scene.py**: fix whitespace

## [0.10.0] - 2024-03-29

### Features

- [`692fbc3`](https://github.com/pufereq/simulat/commit/692fbc3c27fb9b15b09682cac4aa68422b3e8166) **character.py**: add ability to set whether the character has collision
- [`2b7bf72`](https://github.com/pufereq/simulat/commit/2b7bf72b3f1340c11817000490ec8bdd12ecadcd) **character.py**: add ability to specify the sprite size in px/tiles

### Miscellaneous Tasks

- [`87b259c`](https://github.com/pufereq/simulat/commit/87b259ce01ec4f256ffe9c1872c295d9834ff8ed) **release**: 0.10.0
- [`f4351b5`](https://github.com/pufereq/simulat/commit/f4351b5e9bc6913339739f0250a5ee76a4d3448f) **game_map.py**: use the new `Camera` class and remap keys
- [`4906185`](https://github.com/pufereq/simulat/commit/4906185e3c1a7ce7cd43acf7f79f762ef4a69ff8) **player.py**: add the `size` and `unit` argument to init
- [`bc08e85`](https://github.com/pufereq/simulat/commit/bc08e85ea74a5194efc100a28b16d9c3268d2e2b) **.../game_map/camera.py**: [**breaking**] remove the ye olde camera system

### Refactor

- [`fee99e3`](https://github.com/pufereq/simulat/commit/fee99e3e80938f8d7366b68a85ee75f8405ebace) **character.py**: refactor `Character._cap_position()` to use tiles (unit)

### Rewrite

- [`dc4a0f1`](https://github.com/pufereq/simulat/commit/dc4a0f18f3d70d3409444a9f216a669c553b137c) **camera.py**: [**breaking**] rewrite the camera system as a character

## [0.9.1] - 2024-03-29

### Miscellaneous Tasks

- [`909b554`](https://github.com/pufereq/simulat/commit/909b554528fa9121313b91f3f289d8c3a24fc4d8) **release**: 0.9.1
- [`5f156c1`](https://github.com/pufereq/simulat/commit/5f156c1145bb3a4c65f422466b795a46fe501d66) **character.py**: make `Character.current_speed` a property
- [`42afc89`](https://github.com/pufereq/simulat/commit/42afc89462a5fec5d89f004a1e33911aea85ed8f) **character.py**: make `Character.name` a property

### Performance

- [`94c1938`](https://github.com/pufereq/simulat/commit/94c19388d06281f7552bb540f6b1dcfada7a021f) **character.py**: make `Character.px_pos` a property

### Styling

- [`bfe7c8e`](https://github.com/pufereq/simulat/commit/bfe7c8e4cd04009b59d005c0452c6225cc2aab0a) **character.py**: add typing suggestions to `Character.first_name` and `Character.last_name`

## [0.9.0] - 2024-03-28

### Features

- [`67f8def`](https://github.com/pufereq/simulat/commit/67f8def5e0cc107747ac6dfaa3ed1f2e194f3dbd) **surface.py**: add support for hex colors in `Surface.add_text` method
- [`850552c`](https://github.com/pufereq/simulat/commit/850552c04f75b3c5192cb5d525e2edcdac5b8066) **topbar.py**: use the simulat color palette
- [`135c421`](https://github.com/pufereq/simulat/commit/135c421d60faf1349a41cb231e4a13423c04a7dc) **colors.py**: add color palettes

### Miscellaneous Tasks

- [`0addbf6`](https://github.com/pufereq/simulat/commit/0addbf685cddc043e93859e3685c28917fb217d8) **release**: 0.9.0
- [`5543259`](https://github.com/pufereq/simulat/commit/55432591e72500730226bbe16a60e08e7dfbfda9) **game_scene.py**: change the game map view to be rounded only on top right
- [`1e4dfe7`](https://github.com/pufereq/simulat/commit/1e4dfe7c154ea5472929922bc15d5d69168e2268) **game_scene.py**: use the simulat color palette
- [`df4b051`](https://github.com/pufereq/simulat/commit/df4b051f5bd01eb26bf18af3c90202b9731b1b9e) **scene.py**: modify the color argument of the fallback scene text call
- [`21d6d1b`](https://github.com/pufereq/simulat/commit/21d6d1b7a6f46ab9fa98eb345b8841af67ffe498) **sidebar.py**: use the simulat color palette
- [`8e9b3b3`](https://github.com/pufereq/simulat/commit/8e9b3b3f4e42a3ff6a316dbb33e4e5e33ccb74e9) **surface.py**: add hex color support to `Surface.fill` method
- [`b748de9`](https://github.com/pufereq/simulat/commit/b748de9e2553708398637afff643ba5dcfff8444) **topbar.py**: add color lists

## [0.8.0] - 2024-02-25

### Bug Fixes

- [`5411b13`](https://github.com/pufereq/simulat/commit/5411b1356f108df2e860d13b4d0f4e763e3c9ae3) **game_scene.py**: fix double blit of `GameMap.surface` in `GameScene.render()`

### Features

- [`866a581`](https://github.com/pufereq/simulat/commit/866a58119a31803d343f0ed4a406dbcaeb8c9ea1) **game_scene.py**: add rounded corners around game map
- [`52e8f17`](https://github.com/pufereq/simulat/commit/52e8f17755e2286cfad235b37cef2f8e4257c9c1) **sidebar.py**: add a sidebar to game scene

### Miscellaneous Tasks

- [`1bba274`](https://github.com/pufereq/simulat/commit/1bba274ef15ce6523a6d46846bd0072095a016da) **release**: 0.8.0
- [`2384633`](https://github.com/pufereq/simulat/commit/2384633bc033b9ec5315157281fdff040a1ef163) **decorative_tile.py**: change the tile color to a more pleasant shade
- [`0605729`](https://github.com/pufereq/simulat/commit/0605729910ca8d834a91ced1ac26e4390b4485d7) **game_scene.py**: add `self` as an argument to `GameMap()` constructor
- [`4425995`](https://github.com/pufereq/simulat/commit/44259955b6563b1709a74ebaa018715ac29af6c5) **game_scene.py**: add `GameScene.sidebar` and render it
- [`0cd3315`](https://github.com/pufereq/simulat/commit/0cd3315b82bac172ecadfdedd62e7c612dd2336b) **game_map.py**: blit the `GameMap.surface` onto the scene surface in `render()`
- [`e10f8e3`](https://github.com/pufereq/simulat/commit/e10f8e350ba588d264278148198b9e32a687ab1f) **camera.py**: use game map's `display_size` as size of the camera rect
- [`73a7b47`](https://github.com/pufereq/simulat/commit/73a7b47274aaba7207082bc78802939969ea3a3c) **game_map.py**: add `GameMap.display_size` attribute
- [`6850b94`](https://github.com/pufereq/simulat/commit/6850b94b8645a088a674b23e32aa889d370460fb) **map_layout.py**: remove `g` character and assign `DecorativeTile` to `" "`
- [`677c76c`](https://github.com/pufereq/simulat/commit/677c76ca5d56880d6e06bb17b75f652c1ac686b5) **character.py**: normalize diagonal movement of characters
- [`8399e8c`](https://github.com/pufereq/simulat/commit/8399e8cc2ca2519dfacbde868eeb5a04d4116615) **character.py**: add `Character.current_speed` variable and speed calculation

### Performance

- [`2b07718`](https://github.com/pufereq/simulat/commit/2b07718282a19bb69512c736ddaf050b47d48531) **decorative_tile.py**: fill surface only once instead every `draw()` call
- [`7a3953e`](https://github.com/pufereq/simulat/commit/7a3953ee5d2a0df931d65858371d8c93e17123dd) **collider_tile.py**: fill surface only once instead every `draw()` call

## [0.7.0] - 2024-02-19

### Features

- [`a1fdaf9`](https://github.com/pufereq/simulat/commit/a1fdaf9a7d6eed4db1a05152b29ce4d55000a5ce) **time_it.py**: add `Timer()` class
- [`9b4d6a1`](https://github.com/pufereq/simulat/commit/9b4d6a1c6f7a94b8a2313a770717fcdac3bec8b9) **decorative_tile.py**: add `DecorativeTile` class
- [`3b1b879`](https://github.com/pufereq/simulat/commit/3b1b8792162eac7c6f9aeb71d5b7b417480e94b9) **player.py**: display tile name by player position on topbar

### Miscellaneous Tasks

- [`a83bf06`](https://github.com/pufereq/simulat/commit/a83bf06f085db11e94e55fa14825ba47b6eb4a7a) **release**: 0.7.0
- [`0375a94`](https://github.com/pufereq/simulat/commit/0375a949863aa14e7ab4a78143a9fe40deb3c882) **game.py**: set window title to game name, version and FPS
- [`f42a27d`](https://github.com/pufereq/simulat/commit/f42a27df453396f9169b93bd54a75826d4674741) **game_scene.py**: remove the blit area from `GameScene.render()`
- [`40e42bd`](https://github.com/pufereq/simulat/commit/40e42bdf78365919048dc2a53862a8597a2fd82b) **character.py**: modify `Character.render()` to blit on `GameMap.character_surface`
- [`2287abe`](https://github.com/pufereq/simulat/commit/2287abe81cd513507d98939dd3a921bdacf8b069) **game_map.py**: change render order
- [`350c159`](https://github.com/pufereq/simulat/commit/350c1592d7b367cf78f45e0c724edba5011fe309) **game_map.py**: add `GameMap.character_surface`
- [`98279f9`](https://github.com/pufereq/simulat/commit/98279f995bfe524feebaba8a3f25156b9bd677ad) **map_layout.py**: add decorative tiles to the map
- [`1cd5d49`](https://github.com/pufereq/simulat/commit/1cd5d49f80e70443549a429576d870e7f3f88148) **map_layout.py**: assign char `g` to `DecorativeTile` in map layout
- [`8e66974`](https://github.com/pufereq/simulat/commit/8e66974e9cb2c60d26d1fda21b3fe912efae323f) **collider_tile.py**: add `ColliderTile.name` attribute
- [`72cb540`](https://github.com/pufereq/simulat/commit/72cb540dd0b398c5162e3516f23d940814c3590c) **tile.py**: add `Tile.name` attribute

### Performance

- [`dca5111`](https://github.com/pufereq/simulat/commit/dca511125ba26b3e73c43fb1b5340b7ff1c15bcc) **game_map.py**: optimize game map rendering process

## [0.6.0] - 2024-02-18

### Bug Fixes

- [`a5d68f5`](https://github.com/pufereq/simulat/commit/a5d68f5099acdc666f00241c1a7968c4596839b0) **character.py**: fix wrong initial position of character

### Features

- [`c95d15f`](https://github.com/pufereq/simulat/commit/c95d15f49b3e7475442ce3c63b2bed7e2f479f64) **character.py**: add collision checks in `Character.move()`
- [`0e37f19`](https://github.com/pufereq/simulat/commit/0e37f198554a7053f02f6dafac040c884cab9943) **game_map.py**: init the game map based on `MapLayout`
- [`285077d`](https://github.com/pufereq/simulat/commit/285077d47c06c7a566d8fae11596e71d8b063ed5) **map_layout.py**: add `MapLayout` class
- [`be6325c`](https://github.com/pufereq/simulat/commit/be6325c24e3e1f0d993981f96a2fdf95d4c7d6a7) **collider_tile.py**: add `ColliderTile` class
- [`0647f6f`](https://github.com/pufereq/simulat/commit/0647f6f96074c9815c5acf88d7f64be83c441f23) **character.py**: add `delta` argument to `Character.update()` and modify call to `move()`
- [`527790b`](https://github.com/pufereq/simulat/commit/527790bcdd0a919f1131b58b668346d888ef19e3) **tile.py**: add `Tile.id` attribute

### Miscellaneous Tasks

- [`7978c57`](https://github.com/pufereq/simulat/commit/7978c57821c26169f9b3e81c1d7984c0ccf2aebf) **release**: 0.6.0
- [`5347e6b`](https://github.com/pufereq/simulat/commit/5347e6b252751627b3a109c22d196ff65a0bd562) **game.py**: display the game version in topbar
- [`882a17b`](https://github.com/pufereq/simulat/commit/882a17ba78af029903ba49f3a11d9b1ee7c5ae91) **version.py**: add `VERSION` constant determined by reading the `VERSION` file
- [`cc2f870`](https://github.com/pufereq/simulat/commit/cc2f87010ab1ebb727f5a7af4aefdb0afd8eb592) **character.py**: add velocity cap
- [`9fd0686`](https://github.com/pufereq/simulat/commit/9fd0686069747378ea30fdb730d5f4cbcddad2c0) **character.py**: add `_check_collision()` method
- [`00ad8f0`](https://github.com/pufereq/simulat/commit/00ad8f006a22c669f7bb9ade7e4ddedb9769df58) **character.py**: remove unnecesarry imports
- [`d2759cc`](https://github.com/pufereq/simulat/commit/d2759cc27e54e03f8b854ce3ee61d0356372620a) **tile.py**: add `Tile.is_collider` and `Tile.rect` attributes
- [`b1b9162`](https://github.com/pufereq/simulat/commit/b1b9162439579fb9dc06ce57f1eea9f8beeede9d) **game.py**: remove unnecesarry redefinition of logging level
- [`3a76ba4`](https://github.com/pufereq/simulat/commit/3a76ba44d1ce86da29bfc5dc1cab4239ae655ba5) **game.py**: provide `self.frame_delta` as an argument to active scene's `update()` method
- [`4dc2b60`](https://github.com/pufereq/simulat/commit/4dc2b605a348b10631df9a51457e458b5145643e) **game_scene.py**: add `delta` argument to `GameScene.update()` and provide it to `GameScene.game_map.update()`
- [`52ed3e0`](https://github.com/pufereq/simulat/commit/52ed3e08b0483a40b07768dacc9cd4f1fe7d9169) **game_map.py**: add `delta` argument to `GameMap.update()` and provide it to `GameMap.player.update()`
- [`937e0c6`](https://github.com/pufereq/simulat/commit/937e0c6973741c7b033acc2acafc187599b249d9) **scene.py**: add `delta` argument to `Scene.update()`
- [`02ee0bf`](https://github.com/pufereq/simulat/commit/02ee0bf76721fcb919f6b4bceed852b0bc953583) **player.py**: add `Player.render()` method to display player position on topbar
- [`3b667e9`](https://github.com/pufereq/simulat/commit/3b667e902edae0bb9b42d719501b35cbd4efacd4) **character.py**: remove the position (topbar) info for move to `Player.render()` method
- [`98747e7`](https://github.com/pufereq/simulat/commit/98747e78e5a8b793d27955a780e9c7b2e9d9f140) **character.py**: modify `Character.move()` method to alter position (in tiles) instead of pixel
- [`8f39d8d`](https://github.com/pufereq/simulat/commit/8f39d8d22e7ea5b933a0e0bed86f9875279a3495) **character.py**: change `Character.pos`, `max_speed` to tile scale
- [`1e45142`](https://github.com/pufereq/simulat/commit/1e451423c47a5e7dde782c3fbf96004512c78315) **game.py**: add `Simulat.frame_delta` attribute
- [`35800a7`](https://github.com/pufereq/simulat/commit/35800a79b615215e247207e74f22c0a28157b990) **player.py**: remove duplicate `Player.move()` method
- [`c4faa39`](https://github.com/pufereq/simulat/commit/c4faa3960d36e30491c92a9699779f74a5e81f47) move `Player._cap_position()` to parent class `Character._cap_position()`

### Build

- [`5ed6c37`](https://github.com/pufereq/simulat/commit/5ed6c3731cbdf7f15e2f996e9dcdd6cbd1d15822) **.release-it.toml**: write the new version to `VERSION` file
- [`df4ddd3`](https://github.com/pufereq/simulat/commit/df4ddd30c19014d332a62f6d2c94ee57bc8c4680) **VERSION**: add `VERSION` file

## [0.5.0] - 2024-02-12

### Bug Fixes

- [`89d5130`](https://github.com/pufereq/simulat/commit/89d513018fc0f722e8f41ddfb758c4e6b5b54deb) **game_map.py**: fix camera lagging behind the player

### Documentation

- [`0d35cc8`](https://github.com/pufereq/simulat/commit/0d35cc8d62d3b3fcdb9d4f323d574437850c629b) **game_map.py**: improve docstrings
- [`3f6671d`](https://github.com/pufereq/simulat/commit/3f6671d2ff9ea4bc65bcb6e166ef10a5baea0514) **README.md**: add README

### Features

- [`e4be2fa`](https://github.com/pufereq/simulat/commit/e4be2fabca4e960538da131253220c663a8fd52b) **game_map.py**: implement `Player` class as `GameMap.player`
- [`5bf06aa`](https://github.com/pufereq/simulat/commit/5bf06aaa46e1f8fb1f54bc98ff0b640ff11c6ec3) **player.py**: add `Player` class
- [`7fc1702`](https://github.com/pufereq/simulat/commit/7fc1702d8a5907cadc9f3b3bd66928654f3fbf94) **character.py**: add `Character` class

### Miscellaneous Tasks

- [`9c4ecec`](https://github.com/pufereq/simulat/commit/9c4ecec1279e6de4c911a683b07ddb8b8a422313) **release**: 0.5.0
- [`df23a8a`](https://github.com/pufereq/simulat/commit/df23a8a1b938ca20dbf6598a2477616369751b0c) **player.py**: fix typing issues
- [`2a0fe14`](https://github.com/pufereq/simulat/commit/2a0fe1414347954f5ad78df86129adb826abc96d) **game_map.py**: modify `GameMap.input()` to move the player instead of camera
- [`3961217`](https://github.com/pufereq/simulat/commit/39612174e6c1b0fc463c2e15eeb17ca75c71c90a) **tile.py**: remove the exception if `px` not a multiple of `TILE_SIZE` and return a float
- [`ce45417`](https://github.com/pufereq/simulat/commit/ce45417ddb5c1b7a0df252877271420d644c738c) **character.py**: fix typing issues
- [`37d8b8b`](https://github.com/pufereq/simulat/commit/37d8b8b58d6a32aa4b7f7af7301b1166ca6d516a) **character.py**: modify `pos` argument to be specified in tiles
- [`672b82f`](https://github.com/pufereq/simulat/commit/672b82f2ee69ef58118be843ddba77926aa4efe1) **character.py**: add `Character.pos` measured in tiles
- [`b6769ea`](https://github.com/pufereq/simulat/commit/b6769ea0aa89e8183209ba54d559d218aba382ef) **game_scene.py**: add call to `game_map.render()` in `GameScene`
- [`2e7eed7`](https://github.com/pufereq/simulat/commit/2e7eed709eb2eb1ff41d4eb40b6e0043d379750d) **camera.py**: modify `Camera.update()` method to center to player
- [`4e76017`](https://github.com/pufereq/simulat/commit/4e76017fdd18edaa8a0307348fb94cab9a168b14) **character.py**: rename `Character.pos` -> `Character.px_pos`
- [`6bdcd54`](https://github.com/pufereq/simulat/commit/6bdcd543b8cd8a5f2ea21f50bbb74d1d9a46a549) **game_map.py**: add `GameMap.tile_surface` for tiles to be drawn on instead of main surface
- [`d922c4d`](https://github.com/pufereq/simulat/commit/d922c4dd076020cf233f870abff55a03b15440c2) **tile.py**: rewrite `px_to_tiles` function to add support for tuples and rounding
- [`20cb653`](https://github.com/pufereq/simulat/commit/20cb65326ae545dbe675296ffca79b6b84795596) **tile.py**: add `Tile._id` attribute
- [`12a1195`](https://github.com/pufereq/simulat/commit/12a1195d3a447e7697df64eada3ecd6296b0bc21) **tile.py**: increase `TILE_SIZE` to 64px

### Performance

- [`d755475`](https://github.com/pufereq/simulat/commit/d7554750db66779f9a893819e7fb0d89b9ad98d2) **tile.py**: make tiles surfaces instead of subsurfaces of `GameMap.game_map`

### Refactor

- [`ef2205a`](https://github.com/pufereq/simulat/commit/ef2205ad96b620b5aff134456e4c902efbdc9290) **character.py**: modify `Character.update` method after revert of `px_to_tiles` signature change

### Revert

- [`f1286ae`](https://github.com/pufereq/simulat/commit/f1286aec165f6bf402d7b8c55c4cfb357cbba8d0) **tile.py**: revert the `px_to_tiles` method to only use integers

## [0.4.0] - 2024-01-27

### Features

- [`5a39afa`](https://github.com/pufereq/simulat/commit/5a39afacf2e41e6a051bba5fd01121bc474ad295) **camera.py**: add `Camera` class

### Miscellaneous Tasks

- [`dc4e9a7`](https://github.com/pufereq/simulat/commit/dc4e9a7153866e60fbb2dc018da9f714fe656495) **release**: 0.4.0
- [`3de7bbd`](https://github.com/pufereq/simulat/commit/3de7bbd5ab4d43b9737d48c8cd61a7255f5e3e14) **camera.py**: remove debug call to `simulat.topbar.update_title()`
- [`b085c50`](https://github.com/pufereq/simulat/commit/b085c5078a5acd10d574e0845f5fed5ec18cf062) **camera.py**: convert `dx` and `dy` to `int`s
- [`6e72ac9`](https://github.com/pufereq/simulat/commit/6e72ac9987e4ebfe9b43469a915e32b34857526e) **scene.py**: add `Scene.size` variable
- [`f4080a9`](https://github.com/pufereq/simulat/commit/f4080a971bf78b35d1cbd496b81cc2068695a1da) **game_map.py**: replace the old camera with the `Camera` class
- [`8c886a9`](https://github.com/pufereq/simulat/commit/8c886a9cfc3cdadcacf5a734d14f60111dbe58c1) **game_scene.py**: adjust call to `blit` to new `Camera`
- [`5d8ea95`](https://github.com/pufereq/simulat/commit/5d8ea9586336f54273fbe4ba4b3fe3d55343b79e) **surface.py**: replace the ValueError when text is too wide with a logging call
- [`6eb18cd`](https://github.com/pufereq/simulat/commit/6eb18cd525d83882a2a144ef71e3833fa9a3bf1f) **surface.py**: add `Surface.logger` & `SubSurface.logger`
- [`01472a3`](https://github.com/pufereq/simulat/commit/01472a3b2397833acf7abcc1ded29babafebb009) **tile.py**: move `tile.py` -> `.../surfaces/game_map/tiles/`
- [`b714915`](https://github.com/pufereq/simulat/commit/b714915bbdd38fc2f10ecf082c8e16b092480f7b) **game_map.py**: move `game_map.py` -> `.../surfaces/game_map/`
- [`5e41a98`](https://github.com/pufereq/simulat/commit/5e41a98ee956d013c131bb8bb1f11a6854e90ee2) add `__init__.py` to `simulat/`
- [`03241db`](https://github.com/pufereq/simulat/commit/03241db8fa42267335abc8d349de16cf458a6dbd) [**breaking**] move `src/core/` to `src/simulat/core/`
- [`99ebf45`](https://github.com/pufereq/simulat/commit/99ebf450c919bda009ee6dedd013d40617b45694) **game_scene.py**: modify `GameMap` import after move
- [`09d3ffa`](https://github.com/pufereq/simulat/commit/09d3ffa3c72a59bc8687d20faf80979427450a24) **tile.py**: [**breaking**] move `tile.py` to `src/core/surfaces/`
- [`a680060`](https://github.com/pufereq/simulat/commit/a6800605766f4e4644610f836251e73fafc218ae) **game_map.py**: [**breaking**] move `game_map.py` to `src/core/surfaces/`

## [0.3.0] - 2024-01-25

### Bug Fixes

- [`35818bb`](https://github.com/pufereq/simulat/commit/35818bb061ca6799987c19ca5f72ee5a50db891c) **topbar.py**: fix floats being provided to `Surface.subsurface`, int required
- [`232dbe9`](https://github.com/pufereq/simulat/commit/232dbe90cf79db0b2f3cee4e3bc043ac76713c4c) **tile.py**: fix `tiles_to_px()` output being a float

### Documentation

- [`a560b9c`](https://github.com/pufereq/simulat/commit/a560b9c3426cd506f90fea6dfc750f948664c091) **tile.py**: add a disclaimer to unused `Tile.draw()` method

### Features

- [`8c76e7d`](https://github.com/pufereq/simulat/commit/8c76e7d1275806e7cdfd523908e606f311e2505b) **game_map.py**: add moveable camera
- [`f8010c0`](https://github.com/pufereq/simulat/commit/f8010c02b46b85e68139531ffac5f7627a93a229) **game.py**: add `Simulat.focused_surfaces` dict to direct input to
- [`5d522ca`](https://github.com/pufereq/simulat/commit/5d522ca061e0f13a5056c85b5cde8a2f6d20e3ab) **scene.py**: add `Scene.update()` and `Scene.render()` methods
- [`783c447`](https://github.com/pufereq/simulat/commit/783c4479793d996adcc8d83a0f786067c419fd70) **tile.py**: add conversion functions (tiles <-> px)

### Miscellaneous Tasks

- [`1dfbfb8`](https://github.com/pufereq/simulat/commit/1dfbfb8e1ca0c2c2762645ec3522abf8526b2a7f) **release**: 0.3.0
- [`699445f`](https://github.com/pufereq/simulat/commit/699445fc8f38c2122e2a93e24b7f77c3d086dd94) **surface.py**: fix typing errors
- [`b0d5d70`](https://github.com/pufereq/simulat/commit/b0d5d70a7f178123080c537ab248e398080a5d62) **game_map.py**: fix typing errors
- [`7f0f1ea`](https://github.com/pufereq/simulat/commit/7f0f1ea429e6bad4d0771b8fd55413ace951ff7f) **game.py**: fix typing errors
- [`e4d967d`](https://github.com/pufereq/simulat/commit/e4d967dcdbded2c4e94019f9179ff2e81fea9fef) **surface.py**: remove unused import
- [`9cba445`](https://github.com/pufereq/simulat/commit/9cba445faba109949372e3e170e87c2e0761b238) **game_map.py**: enlarge map
- [`f2d30ff`](https://github.com/pufereq/simulat/commit/f2d30ff3cfd5253b1180e27b548232705378199d) **game_scene.py**: enable camera
- [`cafc41e`](https://github.com/pufereq/simulat/commit/cafc41e8e66b51146b7cdb35a465f3cba7be7acd) **game_scene.py**: move the `blit` call into `GameScene.render()` method and add `GameScene.update()`
- [`af16b0f`](https://github.com/pufereq/simulat/commit/af16b0ff8d8719550390887d7d99586b7695d979) **game.py**: use the new `update` and `render` methods in loop
- [`d0f4293`](https://github.com/pufereq/simulat/commit/d0f42938bf8f5c4c25bef2a1b50c84308ce5e122) **game_map.py**: use `tiles_to_px()` function in `GameMap.surface_size` variable
- [`7ee9de8`](https://github.com/pufereq/simulat/commit/7ee9de822161951d08dcd58bae1f7cef7cd43a5a) **tile.py**: move `TILE_SIZE` constant to `tile.py`
- [`f82c144`](https://github.com/pufereq/simulat/commit/f82c1448f6536f747ae255c9e5b4861d90353271) **game.py**: move constants `FPS` and `SIZE` into `simulat` class
- [`ca56f83`](https://github.com/pufereq/simulat/commit/ca56f839f73df522ea72a8bc6b3c4f4b79eaf1c1) **tile.py**: add `__str__` and `__repr__` methods to `Tile`
- [`8e538ba`](https://github.com/pufereq/simulat/commit/8e538bab8afc56102231a4732218ac82fcec7562) **game_scene.py**: remove unnecesarry import
- [`3dcc56e`](https://github.com/pufereq/simulat/commit/3dcc56ea5c41474809122625265d4f9fa6777843) **game_map.py**: remove not needed argument to `GameMap` class

### Refactor

- [`aaefd78`](https://github.com/pufereq/simulat/commit/aaefd78dbd337fe52139f817a60478485c7160cf) **game_map.py**: make imports absolute
- [`9e742b2`](https://github.com/pufereq/simulat/commit/9e742b26b6599d98af1bcf0c07a2bfdd4831e2bf) **game_scene.py**: make imports absolute
- [`de303a3`](https://github.com/pufereq/simulat/commit/de303a3d95f377dd5f7777076afadde3dbabcee5) **scene.py**: make imports absolute
- [`1c406a9`](https://github.com/pufereq/simulat/commit/1c406a98dda1052bb88f6aa748a079f8215593e9) **surface.py**: make imports absolute
- [`751c7ba`](https://github.com/pufereq/simulat/commit/751c7bac55e8f4aa48b77dce2c68a59ae335fd0a) **topbar.py**: make imports absolute
- [`4b7f4ff`](https://github.com/pufereq/simulat/commit/4b7f4ff09ce1ae0df084c0e5dc84db0373605301) **game.py**: make imports absolute

### Styling

- [`3732879`](https://github.com/pufereq/simulat/commit/3732879e9eab7cda6cc0875b472aad673d635e0e) organize imports

### Build

- [`014a0eb`](https://github.com/pufereq/simulat/commit/014a0eb48f4d4cdde2e89fe7ddd3475a5b7d3e8b) **setting.json**: add `settings.json`

## [0.3.0-dev.1] - 2024-01-22

### Bug Fixes

- [`c3a75a5`](https://github.com/pufereq/simulat/commit/c3a75a5bc052dcd5d652736974d843dc063422f9) **surface.py**: fix wrong order of arguments to `Surface().subsurface()` method

### Documentation

- [`022bf50`](https://github.com/pufereq/simulat/commit/022bf5076348f4c7aecfb66a8ba164686e93256b) **scene.py**: modify `Scene()`'s docstring to reflect topbar exclusion

### Features

- [`5715999`](https://github.com/pufereq/simulat/commit/57159999ba14470384fa0b93a184899d8543111d) **game_scene.py**: add `GameScene()` scene class
- [`4d26b28`](https://github.com/pufereq/simulat/commit/4d26b2824b8ebb770f961e9924d1d82d48bb07d5) **game_map.py**: add `GameMap()` class
- [`0bbfd3c`](https://github.com/pufereq/simulat/commit/0bbfd3c69bb2668e00b230e74fafa4ab783aa61d) **tile.py**: add `Tile()` class
- [`a5679f4`](https://github.com/pufereq/simulat/commit/a5679f4827da375d4d278e85c3b4ef40c6d39035) **time_it.py**: add `time_it` decorator

### Miscellaneous Tasks

- [`f57a130`](https://github.com/pufereq/simulat/commit/f57a1303ffe64a472088d11a07bf507b8a2b3e8e) **release**: 0.3.0-dev.1
- [`b8e107f`](https://github.com/pufereq/simulat/commit/b8e107f17a697f5bffae3cd41fc14a67a86ecaae) **game.py**: add `GameScene()` to `_init_scenes`
- [`3f044a5`](https://github.com/pufereq/simulat/commit/3f044a503c07acc2df21b527689be1d04bf4d623) **time_it.py**: modify logging to use wrapped function's logger instead of root
- [`6ee66a7`](https://github.com/pufereq/simulat/commit/6ee66a79ce1536b23fc919e673d0ef24bd84bcfe) **game.py**: replace absolute import of `Scene()` with a relative one

### Refactor

- [`a5f8907`](https://github.com/pufereq/simulat/commit/a5f8907269a9c50797cb64b00d85fb3a46190cd9) **game.py**: rename variable `self.scene` -> `self.active_scene` for clarity

### Build

- [`9775e2c`](https://github.com/pufereq/simulat/commit/9775e2c8bf2691f15d9ac4e33daf61b01ad5dabf) **launch.json**: add ability to run the game via VSCode's internal console

## [0.2.0] - 2024-01-04

### Documentation

- [`ce7385c`](https://github.com/pufereq/simulat/commit/ce7385c2b887587a8ec9006a2a7650cdfb419038) **surface.py**: add docstrings to `Surface` and its methods

### Features

- [`c1bf466`](https://github.com/pufereq/simulat/commit/c1bf466b949086c65a1bf2e134a56d69ec876075) **topbar.py**: add ability to add text to topbar
- [`7ac9e02`](https://github.com/pufereq/simulat/commit/7ac9e02bde3ff5313eb3b70ea14ae839ca949f07) **log_exception.py**: add `log_exception()` function
- [`fcd44fe`](https://github.com/pufereq/simulat/commit/fcd44fed67603251828747aa7e0fa7f82c0e813a) **surface.py**: add ability to align text vertically and horizontally in `add_text()`
- [`5eb2d85`](https://github.com/pufereq/simulat/commit/5eb2d85702d7ceb4367ccee48901eea877648574) **surface.py**: add `SubSurface` class
- [`fc296b3`](https://github.com/pufereq/simulat/commit/fc296b37591a60380a1fa90003f8b9839e6da361) **surface.py**: add `add_text()` method to `Surface`
- [`7671f86`](https://github.com/pufereq/simulat/commit/7671f86e6d93f518f7c15681e4ec1ef4401069d0) **topbar.py**: add `Topbar` class
- [`b2a2fff`](https://github.com/pufereq/simulat/commit/b2a2fffea740259a88a3956a73607579dac1e52d) **surface.py**: add `Surface` class for surface management

### Miscellaneous Tasks

- [`df21439`](https://github.com/pufereq/simulat/commit/df214399b720956e92d9956925862d5be062d451) **release**: 0.2.0
- [`891606d`](https://github.com/pufereq/simulat/commit/891606dc642152ebb71ced6e50b0e9231fac7588) **surface.py**: raise exception if the rendered text is too wide
- [`baa0e5f`](https://github.com/pufereq/simulat/commit/baa0e5fde8485454bd922a018c5232ec66d9b78f) **game.py**: add 'topbar' font
- [`063be7a`](https://github.com/pufereq/simulat/commit/063be7af8f8413cdf8dfdfa5067d70ecc0aea649) **surface.py**: change color depth to 24bits
- [`84895c5`](https://github.com/pufereq/simulat/commit/84895c53ec7b725491f56cc25a5a279710074707) **game.py**: implement `log_exception()`
- [`ac9c855`](https://github.com/pufereq/simulat/commit/ac9c8550374f31411a30116c3ad36a00df53fc0a) **game.py**: modify logging format for readability
- [`57eb65a`](https://github.com/pufereq/simulat/commit/57eb65a555d896b42e56d55cbb0acc92afa11c75) **topbar.py**: modify subsurfaces to use `SubSurface` class
- [`cc78baf`](https://github.com/pufereq/simulat/commit/cc78baf87429cb137d6bd734eaa242e8ac84918f) **surface.py**: modify `add_text()` method to use only font name
- [`5ae301e`](https://github.com/pufereq/simulat/commit/5ae301e04f5b02c5d215708d6c0a1a0f889b56b3) **scene.py**: add a warning when `Scene` is called directly (fallback)
- [`4f7f99a`](https://github.com/pufereq/simulat/commit/4f7f99a98a710ca3cb5491802a85d1d1ebf0fcdf) **game.py**: add `_init_topbar()` method and draw the topbar
- [`ac779a7`](https://github.com/pufereq/simulat/commit/ac779a7610d08f74d0ea3a92a4fdbf82ec4be995) **scene.py**: adjust the size and position of scenes to make space for topbar
- [`0e5b0a4`](https://github.com/pufereq/simulat/commit/0e5b0a4fc2a9815381dfe02560c9759aa92debf6) **game.py**: add `SIZE` global variable (window size)
- [`039cc5d`](https://github.com/pufereq/simulat/commit/039cc5dd1bd91c2ffeca3e7ae43df53f7e0f65d1) **scene.py**: move `scenes/scene.py` -> `surfaces/scenes/scene.py`
- [`4b0c59d`](https://github.com/pufereq/simulat/commit/4b0c59d15cf25ffaaa7470b031c892bcb1aad56c) **game.py**: remove `pg.RESIZABLE` flag from `self.screen`

### Refactor

- [`776dbdc`](https://github.com/pufereq/simulat/commit/776dbdc10a7f28e3a3178facf9bac762d71cfe49) **scene.py**: use `add_text()` method instead of manually adding fallback text
- [`16a6312`](https://github.com/pufereq/simulat/commit/16a631289820b98919ad1691dae049fcfeb1cb3c) **game.py**: move declarations of `self.scenes` and `self.scene` to `_init_scenes()`
- [`f322560`](https://github.com/pufereq/simulat/commit/f3225601c8225fb854df964e2e88cd14e7d6488d) **scene.py**: use `Surface` class

## [0.1.0] - 2024-01-01

### Features

- [`21c2f2b`](https://github.com/pufereq/simulat/commit/21c2f2b0d477ac647e706306943735b58a306acf) **scene.py**: add `Scene` class
- [`49f9f69`](https://github.com/pufereq/simulat/commit/49f9f6952307afbef24c462b0c2350823c61d0f0) **simulat.py**: add game launcher
- [`7dacf29`](https://github.com/pufereq/simulat/commit/7dacf29625de5d62f7523857bb4debc2433a270b) **game.py**: add `Simulat` class and set up logging

### Miscellaneous Tasks

- [`83add70`](https://github.com/pufereq/simulat/commit/83add70cad146fb2d9e06219ecc03e633a8da81e) **release**: 0.1.0
- [`3c8e115`](https://github.com/pufereq/simulat/commit/3c8e11597a62ab938834c0a50ca59b0819fb303f) **game.py**: add `_init_next` and `_init_scenes` method meant to init scenes

### Build

- [`ca55c2c`](https://github.com/pufereq/simulat/commit/ca55c2cd5c18f21b588ac02e3e128b46119d6197) **Makefile**: add `Makefile`

<!-- generated by git-cliff -->
