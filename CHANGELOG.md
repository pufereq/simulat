# Changelog

All notable changes to this project will be documented in this file.

## [0.9.0] - 2024-03-28

### Features

- [`67f8def`](https://github.com/pufereq/simulat/commit/67f8def5e0cc107747ac6dfaa3ed1f2e194f3dbd) **surface.py**: add support for hex colors in `Surface.add_text` method
- [`850552c`](https://github.com/pufereq/simulat/commit/850552c04f75b3c5192cb5d525e2edcdac5b8066) **topbar.py**: use the simulat color palette
- [`135c421`](https://github.com/pufereq/simulat/commit/135c421d60faf1349a41cb231e4a13423c04a7dc) **colors.py**: add color palettes

### Miscellaneous Tasks

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
