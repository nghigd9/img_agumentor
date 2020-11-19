## Image Augmentor

Run the utility from the command-line as follows:

    python main.py <image dir> <transform1> <transform2> ...

The `<image dir>` argument should be the path to a directory containing the image files to be augmented.
The utility will search the directory recursively for files with any of the following extensions:
`jpg, jpeg, bmp, png`.

The `transform` arguments determine what types of augmentation operations will be performed,
using the codes listed in the table below:

|Code|Description|Example Values|
|---|---|------|
|`fliph`|Horizontal Flip|`fliph`|
|`flipv`|Vertical Flip|`flipv`|
|`noise`|Adds random noise to the image|`noise_0.01`,`noise_0.5`|
|`rot`|Rotates the image by the specified amount|`rot_90`,`rot_-45`|
|`trans`|Shifts the pixels of the image by the specified amounts in the x and y directions|`trans_20_10`,`trans_-10_0`|
|`zoom`|Zooms into the specified region of the image, performing stretching/shrinking as necessary|`zoom_0_0_20_20`,`zoom_-10_-20_10_10`|
|`blur`|Blurs the image by the specified amount|`blur_1.5`|

### Examples
Produce 2 output images for each input image, one of which is flipped horizontally, and one of which is flipped vertically:

    python main.py ./my_images fliph flipv

Produce 1 output image for each input image, by first rotating the image by 90&deg; and then flipping it horizontally:

    python main.py ./my_images rot_90,fliph

### Operations

#### Horizontal Flip
Mirrors the image around a vertical line running through its center

    python main.py ./my_images fliph

<img style="border: 1px solid grey" style="border: 1px solid grey" src="http://codebox.net/assets/images/image-augmentation-with-python/macaw.png" alt="Original Image" width="150" height="150"/> &nbsp; &nbsp; &nbsp; <img style="border: 1px solid grey" src="http://codebox.net/assets/images/image-augmentation-with-python/macaw__fliph.png" alt="Flipped Image" width="150" height="150"/>

#### Vertical Flip
Mirrors the image around a horizontal line running through its center

    python main.py ./my_images flipv

<img style="border: 1px solid grey" src="http://codebox.net/assets/images/image-augmentation-with-python/macaw.png" alt="Original Image" width="150" height="150"/> &nbsp; &nbsp; &nbsp; <img style="border: 1px solid grey" src="http://codebox.net/assets/images/image-augmentation-with-python/macaw__flipv.png" alt="Flipped Image" width="150" height="150"/>

#### Noise

    python main.py ./my_images noise_0.01 noise_0.02 noise_0.05

<img style="border: 1px solid grey" src="http://codebox.net/assets/images/image-augmentation-with-python/macaw.png" alt="Original Image" width="150" height="150"/> &nbsp; &nbsp; &nbsp; <img style="border: 1px solid grey" src="http://codebox.net/assets/images/image-augmentation-with-python/macaw__noise0.01.png" alt="Noisy Image" width="150" height="150"/> &nbsp; &nbsp; &nbsp; <img style="border: 1px solid grey" src="http://codebox.net/assets/images/image-augmentation-with-python/macaw__noise0.02.png" alt="Noisy Image" width="150" height="150"/> &nbsp; &nbsp; &nbsp; <img style="border: 1px solid grey" src="http://codebox.net/assets/images/image-augmentation-with-python/macaw__noise0.05.png" alt="Noisy Image" width="150" height="150"/>

#### Rotate

    python main.py ./my_images rot_90 rot_180 rot_-90

<img style="border: 1px solid grey" src="http://codebox.net/assets/images/image-augmentation-with-python/macaw.png" alt="Original Image" width="150" height="150"/> &nbsp; &nbsp; &nbsp; <img style="border: 1px solid grey" src="http://codebox.net/assets/images/image-augmentation-with-python/macaw__rot90.png" alt="Rotated Image" width="150" height="150"/> &nbsp; &nbsp; &nbsp; <img style="border: 1px solid grey" src="http://codebox.net/assets/images/image-augmentation-with-python/macaw__rot180.png" alt="Rotated Image" width="150" height="150"/> &nbsp; &nbsp; &nbsp; <img style="border: 1px solid grey" src="http://codebox.net/assets/images/image-augmentation-with-python/macaw__rot-90.png" alt="Rotated Image" width="150" height="150"/>

#### Translate

    python main.py ./my_images trans_20_20 trans_0_100

<img style="border: 1px solid grey" src="http://codebox.net/assets/images/image-augmentation-with-python/macaw.png" alt="Original Image" width="150" height="150"/> &nbsp; &nbsp; &nbsp; <img style="border: 1px solid grey" src="http://codebox.net/assets/images/image-augmentation-with-python/macaw__trans20_20.png" alt="Translated Image" width="150" height="150"/> &nbsp; &nbsp; &nbsp; <img style="border: 1px solid grey" src="http://codebox.net/assets/images/image-augmentation-with-python/macaw__trans0_100.png" alt="Translated Image" width="150" height="150"/>

#### Zoom/Stretch

    python main.py ./my_images zoom_150_0_300_150 zoom_0_50_300_150 zoom_200_0_300_300

<img style="border: 1px solid grey" src="http://codebox.net/assets/images/image-augmentation-with-python/macaw.png" alt="Original Image" width="150" height="150"/> &nbsp; &nbsp; &nbsp; <img style="border: 1px solid grey" src="http://codebox.net/assets/images/image-augmentation-with-python/macaw__zoom150_0_300_150.png" alt="Zoomed Image" width="150" height="150"/> &nbsp; &nbsp; &nbsp; <img style="border: 1px solid grey" src="http://codebox.net/assets/images/image-augmentation-with-python/macaw__zoom0_50_300_150.png" alt="Stretched Image" width="150" height="150"/> &nbsp; &nbsp; &nbsp; <img style="border: 1px solid grey" src="http://codebox.net/assets/images/image-augmentation-with-python/macaw__zoom200_0_300_300.png" alt="Stretched Image" width="150" height="150"/>

#### Blur

    python main.py ./my_images blur_1.0 blur_2.0 blur_4.0

<img style="border: 1px solid grey" src="http://codebox.net/assets/images/image-augmentation-with-python/macaw.png" alt="Original Image" width="150" height="150"/> &nbsp; &nbsp; &nbsp; <img style="border: 1px solid grey" src="http://codebox.net/assets/images/image-augmentation-with-python/macaw__blur1.0.png" alt="Blurred Image" width="150" height="150"/> &nbsp; &nbsp; &nbsp; <img style="border: 1px solid grey" src="http://codebox.net/assets/images/image-augmentation-with-python/macaw__blur2.0.png" alt="Blurred Image" width="150" height="150"/> &nbsp; &nbsp; &nbsp; <img style="border: 1px solid grey" src="http://codebox.net/assets/images/image-augmentation-with-python/macaw__blur4.0.png" alt="Blurred Image" width="150" height="150"/>
