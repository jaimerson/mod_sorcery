# mod_sorcery
Generate images from given mod.

## Requirements
* python > 2.6
* PIL or Pillow
* anything else in requirements.txt

## Running
Run the script passing the *mod* as the first argument and the *size* of each tile as the 2nd.

```bash
python draw_image.py 5 15
```

This will generate and image with a name following the structure `image_{mod}_{size}.png`.
Example:

#### Mod 31, Size 14
![Mod 31, Size 14](examples/image_31_14.png)

More examples in the `examples` directory.

## License
MIT.
