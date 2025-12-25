# G'MIC Command Reference for AI Photo Editing
This dataset is filtered for commands related to Colors, Filtering, Geometry, and Artistic effects.



---

# Command: apply_curve
**Category:** Values Manipulation
**Source:** https://gmic.eu/reference/apply_curve.html#top

# apply\_curve

## Arguments:

* 0<=smoothness<=1,x0,y0,x1,y1,x2,y2,...,xN,yN

## Description:

Apply curve transformation to image values.  

## Default values:

smoothness=1, x0=0, y0=100.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +apply\_curve 1,0,0,128,255,255,0

  

[![](img/t0_apply_curve.jpg)](img/f0_apply_curve.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +apply\_curve 1,0,0,128,255,255,0**

[![](img/t1_apply_curve.jpg)](img/f1_apply_curve.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +apply\_curve 1,0,0,128,255,255,0**

---

# Command: apply_gamma
**Category:** Values Manipulation
**Source:** https://gmic.eu/reference/apply_gamma.html#top

# apply\_gamma

## Arguments:

* gamma>=0

## Description:

Apply gamma correction to selected images.  

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +apply\_gamma 2

  

[![](img/t0_apply_gamma.jpg)](img/f0_apply_gamma.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +apply\_gamma 2**

[![](img/t1_apply_gamma.jpg)](img/f1_apply_gamma.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +apply\_gamma 2**

---

# Command: apply_mask
**Category:** Values Manipulation
**Source:** https://gmic.eu/reference/apply_mask.html#top

# apply\_mask

## Arguments:

* "command",[opacity\_mask],\_max\_opacity\_mask

## Description:

Apply specified command on selected images but only inside the specified mask.  

## Default values:

max\_opacity\_mask=1.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> 100%,100% noise. 10 blur. 2%,0 ge. 50% blur. 0.5% normalize. 0,1 +apply\_mask.. "sepia whirls",[-1]

  

[![](img/t0_apply_mask.jpg)](img/f0_apply_mask.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> 100%,100% noise. 10 blur. 2%,0 ge. 50% blur. 0.5% normalize. 0,1 +apply\_mask.. "sepia whirls",[-1]**

[![](img/t1_apply_mask.jpg)](img/f1_apply_mask.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> 100%,100% noise. 10 blur. 2%,0 ge. 50% blur. 0.5% normalize. 0,1 +apply\_mask.. "sepia whirls",[-1]**

[![](img/t2_apply_mask.jpg)](img/f2_apply_mask.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> 100%,100% noise. 10 blur. 2%,0 ge. 50% blur. 0.5% normalize. 0,1 +apply\_mask.. "sepia whirls",[-1]**

---

# Command: balance_gamma
**Category:** Values Manipulation
**Source:** https://gmic.eu/reference/balance_gamma.html#top

# balance\_gamma

## Arguments:

* \_ref\_color1,...

## Description:

Compute gamma-corrected color balance of selected image, with respect to specified reference color.  

## Default values:

ref\_color1=128.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +balance\_gamma 128,64,64

  

[![](img/t0_balance_gamma.jpg)](img/f0_balance_gamma.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +balance\_gamma 128,64,64**

[![](img/t1_balance_gamma.jpg)](img/f1_balance_gamma.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +balance\_gamma 128,64,64**

---

# Command: cast
**Category:** Values Manipulation
**Source:** https://gmic.eu/reference/cast.html#top

# cast

## Arguments:

* datatype\_source,datatype\_target

## Description:

Cast datatype of image buffer from specified source type to specified target type.  
  
datatype\_source and datatype\_target can be { uint8 | int8 | uint16 | int16 | uint32 | int32 | uint64 | int64 | float32 | float64 }.

---

# Command: complex2polar
**Category:** Values Manipulation
**Source:** https://gmic.eu/reference/complex2polar.html#top

# complex2polar

### No argumentsDescription:Compute complex to polar transforms of selected images. Example of use: <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +fft complex2polar[-2,-1] log[-2] shift[-2] 50%,50%,0,0,2 remove[-1] Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +fft complex2polar[-2,-1] log[-2] shift[-2] 50%,50%,0,0,2 remove[-1]** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +fft complex2polar[-2,-1] log[-2] shift[-2] 50%,50%,0,0,2 remove[-1]**

---

# Command: compress_clut
**Category:** Values Manipulation
**Source:** https://gmic.eu/reference/compress_clut.html#top

# compress\_clut

### No argumentsDescription:Compress selected color LUTs as sequences of colored keypoints.

---

# Command: compress_huffman
**Category:** Values Manipulation
**Source:** https://gmic.eu/reference/compress_huffman.html#top

# compress\_huffman

## Arguments:

* [huffman\_tree],\_max\_leaf\_value

## Description:

Compress selected images with Huffman coding.  

## See also:

[decompress\_huffman](decompress_huffman.html), [huffman\_tree](huffman_tree.html).

---

# Command: compress_rle
**Category:** Values Manipulation
**Source:** https://gmic.eu/reference/compress_rle.html#top

# compress\_rle

## Arguments:

* \_is\_binary\_data={ 0:No | 1:Yes },\_maximum\_sequence\_length>=0

## Description:

Compress selected images as 2xN data matrices, using RLE algorithm.  
  
Set maximum\_sequence\_length=0 to disable maximum length constraint.  

## Default values:

is\_binary\_data=0 and maximum\_sequence\_length=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rescale2d ,100 quantize 4 round +compress\_rle , +decompress\_rle[-1]

  

[![](img/t0_compress_rle.jpg)](img/f0_compress_rle.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rescale2d ,100 quantize 4 round +compress\_rle , +decompress\_rle[-1]**

[![](img/t1_compress_rle.jpg)](img/f1_compress_rle.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rescale2d ,100 quantize 4 round +compress\_rle , +decompress\_rle[-1]**

[![](img/t2_compress_rle.jpg)](img/f2_compress_rle.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rescale2d ,100 quantize 4 round +compress\_rle , +decompress\_rle[-1]**

---

# Command: cumulate
**Category:** Values Manipulation
**Source:** https://gmic.eu/reference/cumulate.html#top

|  |  |
| --- | --- |
| cumulate | Built-in command |

## Arguments:

* { x | y | z | c }...{ x | y | z | c }    or
* (no arg)

## Description:

Compute the cumulative function of specified image data, optionally along the specified axes.  

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +histogram 256 +cumulate[-1] display\_graph[-2,-1] 400,300,3

  

[![](img/t0_cumulate.jpg)](img/f0_cumulate.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +histogram 256 +cumulate[-1] display\_graph[-2,-1] 400,300,3**

[![](img/t1_cumulate.jpg)](img/f1_cumulate.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +histogram 256 +cumulate[-1] display\_graph[-2,-1] 400,300,3**

[![](img/t2_cumulate.jpg)](img/f2_cumulate.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +histogram 256 +cumulate[-1] display\_graph[-2,-1] 400,300,3**

---

# Command: decompress_clut
**Category:** Values Manipulation
**Source:** https://gmic.eu/reference/decompress_clut.html#top

# decompress\_clut

## Arguments:

* \_width>0,\_height>0,\_depth>0

## Description:

Decompress selected colored keypoints into 3D CLUTs, using a mixed RBF/PDE approach.  

## Default values:

width=height=depth=33 and reconstruction\_colorspace=0.

---

# Command: decompress_from_keypoints
**Category:** Values Manipulation
**Source:** https://gmic.eu/reference/decompress_from_keypoints.html#top

# decompress\_from\_keypoints

## Arguments:

* \_width>0,\_height>0,\_depth>0    or
* (no arg)

## Description:

Decompress selected sets of keypoints as images (opt. of specified size).  
  
A set of keypoints is defined as a vector-valued image, such that:  

The first pixel is a vector which encodes the [ Width,Height,Depth ] of the decompressed image.

The second pixel is a vector which encodes [ Min,Max,Use\_RBF ], where Min and Max defines the value range of the decompressed image, and Use\_RBF tells is the decompression scheme must use RBFs (Use\_RBF=1) or Multiscale Diffusion PDE's (Use\_RBF=0).

The remaining pixels define the keypoint coordinates and values, as:

[ x\_k,y\_k,z\_k, v1\_k,...,vN\_k ] for a 3D target image of N-valued vectors.

[ x\_k,y\_k, v1\_k,...,vN\_k ] for a 2D target image of N-valued vectors.

[ x\_k, v1\_k,...,vN\_k ] for a 1D target image of N-valued vectors.

where the coordinates x\_k, y\_k and z\_k are defined respectively in ranges [0,Width-1], [0,Height-1] and [0,Depth-1].  
If the width, height and depth arguments are provided, they define the size of the decompressed image, : overriding then the original image size [ Width,Height,Depth ] defined in the keypoints header.

---

# Command: decompress_huffman
**Category:** Values Manipulation
**Source:** https://gmic.eu/reference/decompress_huffman.html#top

# decompress\_huffman

## Arguments:

* [huffman\_tree]

## Description:

Decompress selected images with Huffman decoding.  

## See also:

[compress\_huffman](compress_huffman.html), [huffman\_tree](huffman_tree.html).

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> huffman\_tree compress\_huffman.. . +decompress\_huffman.. .

  

[![](img/t0_decompress_huffman.jpg)](img/f0_decompress_huffman.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> huffman\_tree compress\_huffman.. . +decompress\_huffman.. .**

[![](img/t1_decompress_huffman.jpg)](img/f1_decompress_huffman.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> huffman\_tree compress\_huffman.. . +decompress\_huffman.. .**

[![](img/t2_decompress_huffman.jpg)](img/f2_decompress_huffman.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> huffman\_tree compress\_huffman.. . +decompress\_huffman.. .**

---

# Command: decompress_rle
**Category:** Values Manipulation
**Source:** https://gmic.eu/reference/decompress_rle.html#top

# decompress\_rle

### No argumentsDescription:Decompress selected data vectors, using RLE algorithm.

---

# Command: discard
**Category:** Values Manipulation
**Source:** https://gmic.eu/reference/discard.html#top

|  |  |
| --- | --- |
| discard | Built-in command |

## Arguments:

* \_value1,\_value2,...    or
* { x | y | z | c}...{ x | y | z | c},\_value1,\_value2,...    or
* (no arg)

## Description:

Discard specified values in selected images or discard neighboring duplicate values,  
  
optionally only for the values along the first of a specified axis.  
If no arguments are specified, neighboring duplicate values are discarded.  
If all pixels of a selected image are discarded, an empty image is returned.  

## Examples of use:

### • Example #1

(1;2;3;4;3;2;1) +discard 2

  

[![](img/t0_discard.jpg)](img/f0_discard.jpg)

Command: **(1;2;3;4;3;2;1) +discard 2**

[![](img/t1_discard.jpg)](img/f1_discard.jpg)

Command: **(1;2;3;4;3;2;1) +discard 2**

### • Example #2

(1,2,2,3,3,3,4,4,4,4) +discard x

  

[![](img/t0_discard_2.jpg)](img/f0_discard_2.jpg)

Command: **(1,2,2,3,3,3,4,4,4,4) +discard x**

[![](img/t1_discard_2.jpg)](img/f1_discard_2.jpg)

Command: **(1,2,2,3,3,3,4,4,4,4) +discard x**

---

# Command: eigen2tensor
**Category:** Values Manipulation
**Source:** https://gmic.eu/reference/eigen2tensor.html#top

# eigen2tensor

### No argumentsDescription:Recompose selected pairs of eigenvalues/eigenvectors as 2x2 or 3x3 tensor fields. This command has a [tutorial page](https://gmic.eu/tutorial/eigen2tensor).

---

# Command: endian
**Category:** Values Manipulation
**Source:** https://gmic.eu/reference/endian.html#top

|  |  |
| --- | --- |
| endian | Built-in command |

## Arguments:

* \_datatype

## Description:

Reverse data endianness of selected images, eventually considering the pixel being of the specified datatype.  
  
datatype can be { bool | uint8 | int8 | uint16 | int16 | uint32 | int32 | uint64 | int64 | float32 | float64 }.  
This command does nothing for bool, uint8 and int8 datatypes.

---

# Command: equalize
**Category:** Values Manipulation
**Source:** https://gmic.eu/reference/equalize.html#top

|  |  |
| --- | --- |
| equalize | Built-in command |

## Arguments:

* \_nb\_levels[%]>0,\_value\_min[%],\_value\_max[%]    or
* (no arg)

## Description:

Equalize histograms of selected images.  
  
If value range is specified, the equalization is done only for pixels in the specified  
value range.  

## Default values:

nb\_levels=256, value\_min=0% and value\_max=100%.

## Examples of use:

### • Example #1

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +equalize

  

[![](img/t0_equalize.jpg)](img/f0_equalize.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +equalize**

[![](img/t1_equalize.jpg)](img/f1_equalize.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +equalize**

### • Example #2

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +equalize 4,0,128

  

[![](img/t0_equalize_2.jpg)](img/f0_equalize_2.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +equalize 4,0,128**

[![](img/t1_equalize_2.jpg)](img/f1_equalize_2.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +equalize 4,0,128**

---

# Command: fill
**Category:** Values Manipulation
**Source:** https://gmic.eu/reference/fill.html#top

|  |  |
| --- | --- |
| fill | Built-in command |

## Arguments:

* value1,\_value2,...    or
* [image]    or
* 'formula'

## Description:

Fill selected images with values read from the specified value list, existing image  
  
or mathematical expression. Single quotes may be omitted in formula.  

(*equivalent to shortcut command* f).

This command has a [tutorial page](https://gmic.eu/tutorial/fill).

## Examples of use:

### • Example #1

4,4 fill 1,2,3,4,5,6,7

  
[![](img/t_fill.jpg)](img/f_fill.jpg)

Command: **4,4 fill 1,2,3,4,5,6,7**

### • Example #2

4,4 (1,2,3,4,5,6,7) fill[-2] [-1]

  

[![](img/t0_fill_2.jpg)](img/f0_fill_2.jpg)

Command: **4,4 (1,2,3,4,5,6,7) fill[-2] [-1]**

[![](img/t1_fill_2.jpg)](img/f1_fill_2.jpg)

Command: **4,4 (1,2,3,4,5,6,7) fill[-2] [-1]**

### • Example #3

400,400,1,3 fill "X=x-w/2; Y=y-h/2; R=sqrt(X^2+Y^2); a=atan2(Y,X); R<=180?255\*abs(cos(c+200\*(x/w-0.5)\*(y/h-0.5))):850\*(a%(0.1\*(c+1)))"

  
[![](img/t_fill_3.jpg)](img/f_fill_3.jpg)

Command: **400,400,1,3 fill "X=x-w/2; Y=y-h/2; R=sqrt(X^2+Y^2); a=atan2(Y,X); R<=180?255\*abs(cos(c+200\*(x/w-0.5)\*(y/h-0.5))):850\*(a%(0.1\*(c+1)))"**

---

# Command: icp
**Category:** Values Manipulation
**Source:** https://gmic.eu/reference/icp.html#top

# icp

## Arguments:

* [reference],\_affine\_mode,\_precision>0,\_iter\_max>=0

## Description:

Apply affine transformation on vector-valued points of selected images, to match specified set of reference vectors, using the ICP algorithm (Iterative Closest Point).  
  
A description of ICP is available at <https://en.wikipedia.org/wiki/Iterative_closest_point>.  
Argument affine\_mode tells about the type of affine transform applied. It can be: { 0:Free | 1:Rotation+Scaling | 2:Rotation-Only }.  

## Default values:

affine\_mode=0, precision=1e-3 and iter\_max=1000.

---

# Command: map
**Category:** Values Manipulation
**Source:** https://gmic.eu/reference/map.html#top

|  |  |
| --- | --- |
| map | Built-in command |

## Arguments:

* [palette],\_boundary\_conditions    or
* palette\_name,\_boundary\_conditions

## Description:

Map specified vector-valued palette to selected indexed images.  
  
Each output image has M\*N channels, where M and N are the numbers of channels of, respectively, the corresponding input image and the palette image.  
palette\_name can be { default | hsv | lines | hot | cool | jet | flag | cube | rainbow | algae | amp | balance | curl | deep | delta | dense | diff | gray | haline | ice | matter | oxy | phase | rain | solar | speed | tarn | tempo | thermal | topo | turbid | aurora | hocuspocus | srb2 | uzebox }  
boundary\_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.  

## Default values:

boundary\_conditions=0.

This command has a [tutorial page](https://gmic.eu/tutorial/map).

## Examples of use:

### • Example #1

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +luminance map[-1] 3

  

[![](img/t0_map.jpg)](img/f0_map.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +luminance map[-1] 3**

[![](img/t1_map.jpg)](img/f1_map.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +luminance map[-1] 3**

### • Example #2

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +rgb2ycbcr split[-1] c (0,255,0) resize[-1] 256,1,1,1,3 map[-4] [-1] remove[-1] append[-3--1] c ycbcr2rgb[-1]

  

[![](img/t0_map_2.jpg)](img/f0_map_2.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +rgb2ycbcr split[-1] c (0,255,0) resize[-1] 256,1,1,1,3 map[-4] [-1] remove[-1] append[-3--1] c ycbcr2rgb[-1]**

[![](img/t1_map_2.jpg)](img/f1_map_2.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +rgb2ycbcr split[-1] c (0,255,0) resize[-1] 256,1,1,1,3 map[-4] [-1] remove[-1] append[-3--1] c ycbcr2rgb[-1]**

---

# Command: mix_channels
**Category:** Values Manipulation
**Source:** https://gmic.eu/reference/mix_channels.html#top

# mix\_channels

## Arguments:

* (a00,...,aMN)    or
* [matrix]

## Description:

Apply specified matrix to channels of selected images.  

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +mix\_channels (0,1,0;1,0,0;0,0,1)

  

[![](img/t0_mix_channels.jpg)](img/f0_mix_channels.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +mix\_channels (0,1,0;1,0,0;0,0,1)**

[![](img/t1_mix_channels.jpg)](img/f1_mix_channels.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +mix\_channels (0,1,0;1,0,0;0,0,1)**

---

# Command: negate
**Category:** Values Manipulation
**Source:** https://gmic.eu/reference/negate.html#top

# negate

## Arguments:

* base\_value    or
* (no arg)

## Description:

Negate image values.  

## Default values:

base\_value=(undefined).

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +negate

  

[![](img/t0_negate.jpg)](img/f0_negate.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +negate**

[![](img/t1_negate.jpg)](img/f1_negate.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +negate**

---

# Command: noise
**Category:** Values Manipulation
**Source:** https://gmic.eu/reference/noise.html#top

|  |  |
| --- | --- |
| noise | Built-in command |

## Arguments:

* amplitude[%]>=0,\_noise\_type

## Description:

Add random noise to selected images.  
  
noise\_type can be { 0:Gaussian | 1:Uniform | 2:Salt&pepper | 3:Poisson | 4:Rice }.  

## Default values:

noise\_type=0.

## Examples of use:

### • Example #1

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +noise[0] 50,0 +noise[0] 50,1 +noise[0] 10,2 cut 0,255

  

[![](img/t0_noise.jpg)](img/f0_noise.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +noise[0] 50,0 +noise[0] 50,1 +noise[0] 10,2 cut 0,255**

[![](img/t1_noise.jpg)](img/f1_noise.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +noise[0] 50,0 +noise[0] 50,1 +noise[0] 10,2 cut 0,255**

[![](img/t2_noise.jpg)](img/f2_noise.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +noise[0] 50,0 +noise[0] 50,1 +noise[0] 10,2 cut 0,255**

[![](img/t3_noise.jpg)](img/f3_noise.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +noise[0] 50,0 +noise[0] 50,1 +noise[0] 10,2 cut 0,255**

### • Example #2

300,300,1,3 [0] noise[0] 20,0 noise[1] 20,1 +histogram 100 display\_graph[-2,-1] 400,300,3

  

[![](img/t0_noise_2.jpg)](img/f0_noise_2.jpg)

Command: **300,300,1,3 [0] noise[0] 20,0 noise[1] 20,1 +histogram 100 display\_graph[-2,-1] 400,300,3**

[![](img/t1_noise_2.jpg)](img/f1_noise_2.jpg)

Command: **300,300,1,3 [0] noise[0] 20,0 noise[1] 20,1 +histogram 100 display\_graph[-2,-1] 400,300,3**

[![](img/t2_noise_2.jpg)](img/f2_noise_2.jpg)

Command: **300,300,1,3 [0] noise[0] 20,0 noise[1] 20,1 +histogram 100 display\_graph[-2,-1] 400,300,3**

[![](img/t3_noise_2.jpg)](img/f3_noise_2.jpg)

Command: **300,300,1,3 [0] noise[0] 20,0 noise[1] 20,1 +histogram 100 display\_graph[-2,-1] 400,300,3**

---

# Command: noise_hurl
**Category:** Values Manipulation
**Source:** https://gmic.eu/reference/noise_hurl.html#top

# noise\_hurl

## Arguments:

* \_amplitude>=0

## Description:

Add hurl noise to selected images.  

## Default values:

amplitude=10.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +noise\_hurl ,

  

[![](img/t0_noise_hurl.jpg)](img/f0_noise_hurl.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +noise\_hurl ,**

[![](img/t1_noise_hurl.jpg)](img/f1_noise_hurl.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +noise\_hurl ,**

---

# Command: noise_perlin
**Category:** Values Manipulation
**Source:** https://gmic.eu/reference/noise_perlin.html#top

# noise\_perlin

## Arguments:

* \_scale\_x[%]>0,\_scale\_y[%]>0,\_scale\_z[%]>0,\_seed\_x,\_seed\_y,\_seed\_z

## Description:

Render 2D or 3D Perlin noise on selected images, from specified coordinates.  
  
The Perlin noise is a specific type of smooth noise,  
described here : <https://en.wikipedia.org/wiki/Perlin_noise>.  

## Default values:

scale\_x=scale\_y=scale\_z=16 and seed\_x=seed\_y=seed\_z=0.

## Example of use:

500,500,1,3 noise\_perlin ,

  
[![](img/t_noise_perlin.jpg)](img/f_noise_perlin.jpg)

Command: **500,500,1,3 noise\_perlin ,**

---

# Command: noise_poissondisk
**Category:** Values Manipulation
**Source:** https://gmic.eu/reference/noise_poissondisk.html#top

# noise\_poissondisk

## Arguments:

* \_radius[%]>0,\_max\_sample\_attempts>0,\_p\_norm>0

## Description:

Add poisson disk sampling noise to selected images.  
  
Implements the algorithm from the article "Fast Poisson Disk Sampling in Arbitrary Dimensions",  
by Robert Bridson (SIGGRAPH'2007).  

## Default values:

radius=8, max\_sample\_attempts=30 and p\_norm=2.

## Example of use:

300,300 noise\_poissondisk 8

  
[![](img/t_noise_poissondisk.jpg)](img/f_noise_poissondisk.jpg)

Command: **300,300 noise\_poissondisk 8**

---

# Command: normp
**Category:** Values Manipulation
**Source:** https://gmic.eu/reference/normp.html#top

# normp

## Arguments:

* p>=0

## Description:

Compute the pointwise Lp-norm norm of vector-valued pixels in selected images.  

## Default values:

p=2.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +normp[0] 0 +normp[0] 1 +normp[0] 2 +normp[0] inf

  

[![](img/t0_normp.jpg)](img/f0_normp.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +normp[0] 0 +normp[0] 1 +normp[0] 2 +normp[0] inf**

[![](img/t1_normp.jpg)](img/f1_normp.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +normp[0] 0 +normp[0] 1 +normp[0] 2 +normp[0] inf**

[![](img/t2_normp.jpg)](img/f2_normp.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +normp[0] 0 +normp[0] 1 +normp[0] 2 +normp[0] inf**

[![](img/t3_normp.jpg)](img/f3_normp.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +normp[0] 0 +normp[0] 1 +normp[0] 2 +normp[0] inf**

[![](img/t4_normp.jpg)](img/f4_normp.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +normp[0] 0 +normp[0] 1 +normp[0] 2 +normp[0] inf**

---

# Command: norm1
**Category:** Values Manipulation
**Source:** https://gmic.eu/reference/norm1.html#top

# norm1

### No argumentsDescription:Compute the pointwise L1-norm of vector-valued pixels in selected images. This command has a [tutorial page](https://gmic.eu/oldtutorial/_norm1). Example of use: <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +norm1 Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +norm1** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +norm1**

---

# Command: norm2
**Category:** Values Manipulation
**Source:** https://gmic.eu/reference/norm2.html#top

# norm2

### No argumentsDescription:Compute the pointwise L2-norm (euclidean norm) of vector-valued pixels in selected images. This command has a [tutorial page](https://gmic.eu/oldtutorial/_norm2). Example of use: <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +norm Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +norm** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +norm**

---

# Command: normalize
**Category:** Values Manipulation
**Source:** https://gmic.eu/reference/normalize.html#top

|  |  |
| --- | --- |
| normalize | Built-in command |

## Arguments:

* { value0[%] | [image0] },{ value1[%] | [image1] },\_constant\_case\_ratio    or
* [image]

## Description:

Linearly normalize values of selected images in specified range.  

(*equivalent to shortcut command* n).

This command has a [tutorial page](https://gmic.eu/tutorial/normalize).

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> split x,2 normalize[-1] 64,196 append x

  
[![](img/t_normalize.jpg)](img/f_normalize.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> split x,2 normalize[-1] 64,196 append x**

---

# Command: normalize_l2
**Category:** Values Manipulation
**Source:** https://gmic.eu/reference/normalize_l2.html#top

# normalize\_l2

### No argumentsDescription:Normalize selected images such that they have a unit L2 norm.

---

# Command: normalize_sum
**Category:** Values Manipulation
**Source:** https://gmic.eu/reference/normalize_sum.html#top

# normalize\_sum

### No argumentsDescription:Normalize selected images such that they have a unit sum. Example of use: <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +histogram 256 normalize\_sum[-1] display\_graph[-1] 400,300 Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +histogram 256 normalize\_sum[-1] display\_graph[-1] 400,300** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +histogram 256 normalize\_sum[-1] display\_graph[-1] 400,300**

---

# Command: orientation
**Category:** Values Manipulation
**Source:** https://gmic.eu/reference/orientation.html#top

# orientation

### No argumentsDescription:Compute the pointwise orientation of vector-valued pixels in selected images. This command has a [tutorial page](https://gmic.eu/tutorial/orientation). Example of use: <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +orientation +norm[-2] negate[-1] mul[-2] [-1] reverse[-2,-1] Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +orientation +norm[-2] negate[-1] mul[-2] [-1] reverse[-2,-1]** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +orientation +norm[-2] negate[-1] mul[-2] [-1] reverse[-2,-1]** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +orientation +norm[-2] negate[-1] mul[-2] [-1] reverse[-2,-1]**

---

# Command: otsu
**Category:** Values Manipulation
**Source:** https://gmic.eu/reference/otsu.html#top

# otsu

## Arguments:

* \_nb\_levels>0

## Description:

Hard-threshold selected images using Otsu's method.  
  
The computed thresholds are returned as a list of values in the status.  

## Default values:

nb\_levels=256.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> luminance +otsu ,

  

[![](img/t0_otsu.jpg)](img/f0_otsu.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> luminance +otsu ,**

[![](img/t1_otsu.jpg)](img/f1_otsu.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> luminance +otsu ,**

---

# Command: polar2complex
**Category:** Values Manipulation
**Source:** https://gmic.eu/reference/polar2complex.html#top

# polar2complex

### No argumentsDescription:Compute polar to complex transforms of selected images.

---

# Command: quantize
**Category:** Values Manipulation
**Source:** https://gmic.eu/reference/quantize.html#top

# quantize

## Arguments:

* nb\_levels>=1,\_keep\_values={ 0:No | 1:Yes },\_quantization\_type={ -1:Median-cut | 0:K-means | 1:Uniform }

## Description:

Quantize selected images.  

## Default values:

keep\_values=1 and quantization\_type=0.

## Examples of use:

### • Example #1

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> luminance +quantize 3

  

[![](img/t0_quantize.jpg)](img/f0_quantize.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> luminance +quantize 3**

[![](img/t1_quantize.jpg)](img/f1_quantize.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> luminance +quantize 3**

### • Example #2

200,200,1,1,'cos(x/10)\*sin(y/10)' +quantize[0] 6 +quantize[0] 4 +quantize[0] 3 +quantize[0] 2

  

[![](img/t0_quantize_2.jpg)](img/f0_quantize_2.jpg)

Command: **200,200,1,1,'cos(x/10)\*sin(y/10)' +quantize[0] 6 +quantize[0] 4 +quantize[0] 3 +quantize[0] 2**

[![](img/t1_quantize_2.jpg)](img/f1_quantize_2.jpg)

Command: **200,200,1,1,'cos(x/10)\*sin(y/10)' +quantize[0] 6 +quantize[0] 4 +quantize[0] 3 +quantize[0] 2**

[![](img/t2_quantize_2.jpg)](img/f2_quantize_2.jpg)

Command: **200,200,1,1,'cos(x/10)\*sin(y/10)' +quantize[0] 6 +quantize[0] 4 +quantize[0] 3 +quantize[0] 2**

[![](img/t3_quantize_2.jpg)](img/f3_quantize_2.jpg)

Command: **200,200,1,1,'cos(x/10)\*sin(y/10)' +quantize[0] 6 +quantize[0] 4 +quantize[0] 3 +quantize[0] 2**

[![](img/t4_quantize_2.jpg)](img/f4_quantize_2.jpg)

Command: **200,200,1,1,'cos(x/10)\*sin(y/10)' +quantize[0] 6 +quantize[0] 4 +quantize[0] 3 +quantize[0] 2**

---

# Command: quantize_area
**Category:** Values Manipulation
**Source:** https://gmic.eu/reference/quantize_area.html#top

# quantize\_area

## Arguments:

* \_min\_area>0

## Description:

Quantize selected images such that each flat region has an area greater or equal to min\_area.  

## Default values:

min\_area=10.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> quantize 3 +blur 1 round[-1] +quantize\_area[-1] 2

  

[![](img/t0_quantize_area.jpg)](img/f0_quantize_area.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> quantize 3 +blur 1 round[-1] +quantize\_area[-1] 2**

[![](img/t1_quantize_area.jpg)](img/f1_quantize_area.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> quantize 3 +blur 1 round[-1] +quantize\_area[-1] 2**

[![](img/t2_quantize_area.jpg)](img/f2_quantize_area.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> quantize 3 +blur 1 round[-1] +quantize\_area[-1] 2**

---

# Command: rand
**Category:** Values Manipulation
**Source:** https://gmic.eu/reference/rand.html#top

|  |  |
| --- | --- |
| rand | Built-in command |

## Arguments:

* { value0[%] | [image0] },\_{ value1[%] | [image1] },\_[pdf],\_precision[%]    or
* [image]

## Description:

Fill selected images with random values in the specified range.  
  
If no [pdf] (probability density function) is specified, random values follow a uniform distribution.  
Argument precision tells about the number of distinct values that can be generated when a [pdf] is specified.  

## Examples of use:

### • Example #1

400,400,1,3 rand -10,10 +blur 10 sign[-1]

  

[![](img/t0_rand.jpg)](img/f0_rand.jpg)

Command: **400,400,1,3 rand -10,10 +blur 10 sign[-1]**

[![](img/t1_rand.jpg)](img/f1_rand.jpg)

Command: **400,400,1,3 rand -10,10 +blur 10 sign[-1]**

### • Example #2

(8,2,1) 50,50 rand[-1] 0,255,[-2]

  

[![](img/t0_rand_2.jpg)](img/f0_rand_2.jpg)

Command: **(8,2,1) 50,50 rand[-1] 0,255,[-2]**

[![](img/t1_rand_2.jpg)](img/f1_rand_2.jpg)

Command: **(8,2,1) 50,50 rand[-1] 0,255,[-2]**

### • Example #3

256 gaussian[-1] 30 line[-1] 47%,0,53%,0,1,0 500,500 rand[-1] 0,255,[-2] +histogram[-1] 256 display\_graph[0,2] 640,480,3,0

  

[![](img/t0_rand_3.jpg)](img/f0_rand_3.jpg)

Command: **256 gaussian[-1] 30 line[-1] 47%,0,53%,0,1,0 500,500 rand[-1] 0,255,[-2] +histogram[-1] 256 display\_graph[0,2] 640,480,3,0**

[![](img/t1_rand_3.jpg)](img/f1_rand_3.jpg)

Command: **256 gaussian[-1] 30 line[-1] 47%,0,53%,0,1,0 500,500 rand[-1] 0,255,[-2] +histogram[-1] 256 display\_graph[0,2] 640,480,3,0**

[![](img/t2_rand_3.jpg)](img/f2_rand_3.jpg)

Command: **256 gaussian[-1] 30 line[-1] 47%,0,53%,0,1,0 500,500 rand[-1] 0,255,[-2] +histogram[-1] 256 display\_graph[0,2] 640,480,3,0**

---

# Command: rand_sum
**Category:** Values Manipulation
**Source:** https://gmic.eu/reference/rand_sum.html#top

# rand\_sum

## Arguments:

* sum>0,\_random\_function

## Description:

Fill selected images with strictly positive, random, integer values, that sums to sum.  
  
For each image, sum must be greater or equal than width\*height\*depth\*spectrum.  

## Default values:

random\_function=u.

## Example of use:

100 rand\_sum 1000

  
[![](img/t_rand_sum.jpg)](img/f_rand_sum.jpg)

Command: **100 rand\_sum 1000**

---

# Command: replace
**Category:** Values Manipulation
**Source:** https://gmic.eu/reference/replace.html#top

# replace

## Arguments:

* source,target

## Description:

Replace pixel values in selected images.  

## Example of use:

(1;2;3;4) +replace 2,3

  

[![](img/t0_replace.jpg)](img/f0_replace.jpg)

Command: **(1;2;3;4) +replace 2,3**

[![](img/t1_replace.jpg)](img/f1_replace.jpg)

Command: **(1;2;3;4) +replace 2,3**

---

# Command: replace_inf
**Category:** Values Manipulation
**Source:** https://gmic.eu/reference/replace_inf.html#top

# replace\_inf

## Arguments:

* \_expression

## Description:

Replace all infinite values in selected images by specified expression.  

## Example of use:

(0;1;2) log +replace\_inf 2

  

[![](img/t0_replace_inf.jpg)](img/f0_replace_inf.jpg)

Command: **(0;1;2) log +replace\_inf 2**

[![](img/t1_replace_inf.jpg)](img/f1_replace_inf.jpg)

Command: **(0;1;2) log +replace\_inf 2**

---

# Command: replace_infnan
**Category:** Values Manipulation
**Source:** https://gmic.eu/reference/replace_infnan.html#top

# replace\_infnan

## Arguments:

* \_expression

## Description:

Replace all NaN and infinite values in selected images by specified expression.

---

# Command: replace_nan
**Category:** Values Manipulation
**Source:** https://gmic.eu/reference/replace_nan.html#top

# replace\_nan

## Arguments:

* \_expression

## Description:

Replace all NaN values in selected images by specified expression.  

## Example of use:

(-1;0;2) sqrt +replace\_nan 2

  

[![](img/t0_replace_nan.jpg)](img/f0_replace_nan.jpg)

Command: **(-1;0;2) sqrt +replace\_nan 2**

[![](img/t1_replace_nan.jpg)](img/f1_replace_nan.jpg)

Command: **(-1;0;2) sqrt +replace\_nan 2**

---

# Command: replace_seq
**Category:** Values Manipulation
**Source:** https://gmic.eu/reference/replace_seq.html#top

# replace\_seq

## Arguments:

* "search\_seq","replace\_seq"

## Description:

Search and replace a sequence of values in selected images.  

## Example of use:

(1;2;3;4;5) +replace\_seq "2,3,4","7,8"

  

[![](img/t0_replace_seq.jpg)](img/f0_replace_seq.jpg)

Command: **(1;2;3;4;5) +replace\_seq "2,3,4","7,8"**

[![](img/t1_replace_seq.jpg)](img/f1_replace_seq.jpg)

Command: **(1;2;3;4;5) +replace\_seq "2,3,4","7,8"**

---

# Command: replace_str
**Category:** Values Manipulation
**Source:** https://gmic.eu/reference/replace_str.html#top

# replace\_str

## Arguments:

* "search\_str","replace\_str"

## Description:

Search and replace a string in selected images (viewed as strings, i.e. sequences of character codes).  

## Example of use:

('"Hello there, how are you ?"') +replace\_str "Hello there","Hi David"

  

[![](img/t0_replace_str.jpg)](img/f0_replace_str.jpg)

Command: **('"Hello there, how are you ?"') +replace\_str "Hello there","Hi David"**

[![](img/t1_replace_str.jpg)](img/f1_replace_str.jpg)

Command: **('"Hello there, how are you ?"') +replace\_str "Hello there","Hi David"**

---

# Command: round
**Category:** Values Manipulation
**Source:** https://gmic.eu/reference/round.html#top

|  |  |
| --- | --- |
| round | Built-in command |

## Arguments:

* rounding\_value>=0,\_rounding\_type    or
* (no arg)

## Description:

Round values of selected images.  
  
rounding\_type can be { -1:Backward | 0:Nearest | 1:Forward }.  

## Default values:

rounding\_type=0.

## Examples of use:

### • Example #1

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +round 100

  

[![](img/t0_round.jpg)](img/f0_round.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +round 100**

[![](img/t1_round.jpg)](img/f1_round.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +round 100**

### • Example #2

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> mul {pi/180} sin +round

  

[![](img/t0_round_2.jpg)](img/f0_round_2.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> mul {pi/180} sin +round**

[![](img/t1_round_2.jpg)](img/f1_round_2.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> mul {pi/180} sin +round**

---

# Command: roundify
**Category:** Values Manipulation
**Source:** https://gmic.eu/reference/roundify.html#top

# roundify

## Arguments:

* gamma>=0

## Description:

Apply roundify transformation on float-valued data, with specified gamma.  

## Default values:

gamma=0.

## Example of use:

1000 fill '4\*x/w' repeat 5 { +roundify[0] {$>\*0.2} } append c display\_graph 400,300

  
[![](img/t_roundify.jpg)](img/f_roundify.jpg)

Command: **1000 fill '4\*x/w' repeat 5 { +roundify[0] {$>\*0.2} } append c display\_graph 400,300**

---

# Command: set
**Category:** Values Manipulation
**Source:** https://gmic.eu/reference/set.html#top

|  |  |
| --- | --- |
| set | Built-in command |

## Arguments:

* value,\_x[%],\_y[%],\_z[%],\_c[%]

## Description:

Set pixel value in selected images, at specified coordinates.  

(*equivalent to shortcut command* =).

  
If specified coordinates are outside the image bounds, no action is performed.  

## Default values:

x=y=z=c=0.

## Examples of use:

### • Example #1

2,2 set 1,0,0 set 2,1,0 set 3,0,1 set 4,1,1

  
[![](img/t_set.jpg)](img/f_set.jpg)

Command: **2,2 set 1,0,0 set 2,1,0 set 3,0,1 set 4,1,1**

### • Example #2

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> repeat 10000 { set 255,{u(100)}%,{u(100)}%,0,{u(100)}% }

  
[![](img/t_set_2.jpg)](img/f_set_2.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> repeat 10000 { set 255,{u(100)}%,{u(100)}%,0,{u(100)}% }**

---

# Command: threshold
**Category:** Values Manipulation
**Source:** https://gmic.eu/reference/threshold.html#top

# threshold

## Arguments:

* value[%],\_is\_soft\_thresholding={ 0:No | 1:Yes }

## Description:

Threshold values of selected images.  
  
soft can be { 0:Hard-thresholding | 1:Soft-thresholding }.  

## Default values:

is\_soft=0.

This command has a [tutorial page](https://gmic.eu/tutorial/threshold).

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +threshold[0] 50% +threshold[0] 50%,1

  

[![](img/t0_threshold.jpg)](img/f0_threshold.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +threshold[0] 50% +threshold[0] 50%,1**

[![](img/t1_threshold.jpg)](img/f1_threshold.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +threshold[0] 50% +threshold[0] 50%,1**

[![](img/t2_threshold.jpg)](img/f2_threshold.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +threshold[0] 50% +threshold[0] 50%,1**

---

# Command: vector2tensor
**Category:** Values Manipulation
**Source:** https://gmic.eu/reference/vector2tensor.html#top

# vector2tensor

### No argumentsDescription:Convert selected vector fields to corresponding tensor fields.

---

# Command: adjust_colors
**Category:** Colors
**Source:** https://gmic.eu/reference/adjust_colors.html#top

# adjust\_colors

## Arguments:

* -100<=\_brightness<=100,-100<=\_contrast<=100,-100<=\_gamma<=100,-100<=\_hue\_shift<=100,-100<=\_saturation<=100,\_value\_min,\_value\_max

## Description:

Perform a global adjustment of colors on selected images.  
  
Range of correct image values are considered to be in [value\_min,value\_max] (e.g. [0,255]).  
If value\_min==value\_max==0, value range is estimated from min/max values of selected images.  
Processed images have pixel values constrained in [value\_min,value\_max].  

## Default values:

brightness=0, contrast=0, gamma=0, hue\_shift=0, saturation=0, value\_min=value\_max=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +adjust\_colors 0,30,0,0,30

  

[![](img/t0_adjust_colors.jpg)](img/f0_adjust_colors.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +adjust\_colors 0,30,0,0,30**

[![](img/t1_adjust_colors.jpg)](img/f1_adjust_colors.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +adjust\_colors 0,30,0,0,30**

---

# Command: apply_channels
**Category:** Colors
**Source:** https://gmic.eu/reference/apply_channels.html#top

# apply\_channels

## Arguments:

* "command",color\_channels,\_value\_action={ 0:None | 1:Cut | 2:Normalize }

## Description:

Apply specified command on the chosen color channel(s) of each selected images.  

(*equivalent to shortcut command* ac).

  
Argument color\_channels refers to a colorspace, and can be basically one of  
{ all | rgba | [s]rgb | ryb | lrgb | ycbcr | lab | lch | hsv | hsi | hsl | cmy | cmyk | yiq }.  
You can also make the processing focus on a few particular channels of this colorspace,  
by setting color\_channels as colorspace\_channel (e.g. hsv\_h for the hue).  
All channel values are considered to be provided in the [0,255] range.  

## Default values:

value\_action=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +apply\_channels "equalize blur 2",ycbcr\_cbcr

  

[![](img/t0_apply_channels.jpg)](img/f0_apply_channels.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +apply\_channels "equalize blur 2",ycbcr\_cbcr**

[![](img/t1_apply_channels.jpg)](img/f1_apply_channels.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +apply\_channels "equalize blur 2",ycbcr\_cbcr**

---

# Command: bayer2rgb
**Category:** Colors
**Source:** https://gmic.eu/reference/bayer2rgb.html#top

# bayer2rgb

## Arguments:

* \_GM\_smoothness,\_RB\_smoothness1,\_RB\_smoothness2

## Description:

Transform selected RGB-Bayer sampled images to color images.  

## Default values:

GM\_smoothness=RB\_smoothness=1 and RB\_smoothness2=0.5.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2bayer 0 +bayer2rgb 1,1,0.5

  

[![](img/t0_bayer2rgb.jpg)](img/f0_bayer2rgb.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2bayer 0 +bayer2rgb 1,1,0.5**

[![](img/t1_bayer2rgb.jpg)](img/f1_bayer2rgb.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2bayer 0 +bayer2rgb 1,1,0.5**

---

# Command: brightness
**Category:** Colors
**Source:** https://gmic.eu/reference/brightness.html#top

# brightness

## Arguments:

* strength

## Description:

Change contrast of selected images, with specified strength.  

If strength is positive, image brightness is amplified.

If strength is negative, image brightness is reduced.

A typical value range for parameter strength is [-100,100].  

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +brightness 20

  

[![](img/t0_brightness.jpg)](img/f0_brightness.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +brightness 20**

[![](img/t1_brightness.jpg)](img/f1_brightness.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +brightness 20**

---

# Command: clut
**Category:** Colors
**Source:** https://gmic.eu/reference/clut.html#top

# clut

## Arguments:

* "clut\_name",\_resolution>0,\_cut\_and\_round={ 0:No | 1:Yes }

## Description:

Insert one of the 1149 pre-defined CLUTs at the end of the image list.  
  
  
clut\_name can be { 12\_years\_a\_slave | 1917 | 2-strip-process | 60s | 60s\_faded | 60s\_faded\_alt | 7drk\_21 | action\_magenta\_01 | action\_red\_01 | ad\_astra | adventure\_1453 | agfa\_apx\_100 | agfa\_apx\_25 | agfa\_precisa\_100 | agfa\_ultra\_color\_100 | agfa\_vista\_200 | agressive\_highligjtes\_recovery\_5 | aladdin | alberto\_street | alien\_green | ampio | amstragram | amstragram+ | analog\_film\_1 | analogfx\_anno\_1870\_color | analogfx\_old\_style\_i | analogfx\_old\_style\_ii | analogfx\_old\_style\_iii | analogfx\_sepia\_color | analogfx\_soft\_sepia\_i | analogfx\_soft\_sepia\_ii | anime | ant-man | apocalypse\_this\_very\_moment | aqua | aqua\_and\_orange\_dark | aquaman | arabica\_12 | asistas | atomic\_pink | atusa | autumn | autumn\_leaves | ava\_614 | avalanche | avengers\_endgame | azrael\_93 | baby\_driver | bad\_boys\_for\_life | basuco | bboyz\_2 | bc\_darkum | beach\_aqua\_orange | beach\_faded\_analog | beati | beauty\_and\_the\_beast | berlin\_sky | bisogno | black\_and\_white | black\_panther | black\_star | black\_white\_01 | black\_white\_02 | black\_white\_03 | black\_white\_04 | black\_white\_05 | black\_white\_06 | blade\_runner | bleach\_bypass | bleachbypass\_1 | bleachbypass\_2 | bleachbypass\_3 | bleachbypass\_4 | bleech\_bypass\_green | bleech\_bypass\_yellow\_01 | blue\_cold\_fade | blue\_dark | blue\_house | blue\_ice | blue\_love\_39 | blue\_mono | blue\_shadows\_01 | bluearchitecture | bluehour | blues | bob\_ford | bohemian\_rhapsody | bombshell | bourbon\_64 | boyado | bright\_green\_01 | bright\_teal\_orange | bright\_warm | brightgreen | brown\_mobster | brownbm | brownish | bw\_1 | bw\_10 | bw\_2 | bw\_3 | bw\_4 | bw\_5 | bw\_6 | bw\_7 | bw\_8 | bw\_9 | bw\_but\_yellow | byers\_11 | calidum | candlelight | captain\_marvel | caribe | chemical\_168 | chrome\_01 | cineblue | cinebm\_4k | cinema | cinema\_2 | cinema\_3 | cinema\_4 | cinema\_5 | cinema\_noir | cinematic-1 | cinematic-10 | cinematic-2 | cinematic-3 | cinematic-4 | cinematic-5 | cinematic-6 | cinematic-7 | cinematic-8 | cinematic-9 | cinematic\_01 | cinematic\_02 | cinematic\_03 | cinematic\_04 | cinematic\_05 | cinematic\_06 | cinematic\_07 | cinematic\_for\_flog | cinematic\_forest | cinematic\_lady\_bird | cinematic\_mexico | city | city\_7 | city\_dust | city\_of\_god | classic\_films\_01 | classic\_films\_02 | classic\_films\_03 | classic\_films\_04 | classic\_films\_05 | classic\_teal\_and\_orange | clayton\_33 | clear | clear\_teal\_fade | clouseau\_54 | cobi\_3 | coffee\_44 | cold\_clear\_blue | cold\_clear\_blue\_1 | cold\_ice | cold\_simplicity\_2 | coldchrome | color\_rich | colore | colorful\_0209 | colornegative | conflict\_01 | contrail\_35 | contrast\_with\_highlights\_protection | contrasty\_afternoon | contrasty\_green | convold | cosa | creed\_2 | crispautumn | crispromance | crispwarm | crispwinter | cross\_process\_cp\_130 | cross\_process\_cp\_14 | cross\_process\_cp\_15 | cross\_process\_cp\_16 | cross\_process\_cp\_18 | cross\_process\_cp\_3 | cross\_process\_cp\_4 | cross\_process\_cp\_6 | crushin | cubicle\_99 | culor | d\_o\_1 | dark\_blues\_in\_sunlight | dark\_green\_02 | dark\_green\_1 | dark\_man\_x | dark\_orange\_teal | dark\_place\_01 | darkandsomber | darkness | date\_39 | day\_4nite | day\_for\_night | day\_to\_night\_kings\_blue | deep | deep\_blue | deep\_dark\_warm | deep\_high\_contrast | deep\_teal\_fade | deep\_warm\_fade | deepskintones\_2 | deepskintones\_3 | delicatessen | denoiser\_simple\_40 | desert\_gold\_37 | dimension | dimmer | directions\_23 | django\_25 | doctor\_strange | domingo\_145 | dream\_1 | dream\_85 | drop\_green\_tint\_14 | dropblues | dunkirk | duotone\_blue\_red | earth\_tone\_boost | eda\_0\_2 | edgyember | elegance\_38 | enchanted | ensaya | eterna\_for\_flog | expired\_69 | expired\_fade | expired\_polaroid | extreme | fade | fade\_to\_green | faded | faded\_47 | faded\_alt | faded\_analog | faded\_extreme | faded\_green | faded\_pink-ish | faded\_print | faded\_retro\_01 | faded\_retro\_02 | faded\_vivid | fadedlook | fallcolors | falua | farkling | fatos | faux\_infrared | faux\_infrared\_bw\_1 | faux\_infrared\_color\_p\_2 | faux\_infrared\_color\_p\_3 | faux\_infrared\_color\_r\_0a | faux\_infrared\_color\_r\_0b | faux\_infrared\_color\_yp\_1 | fezzle | fg\_cinebasic | fg\_cinebright | fg\_cinecold | fg\_cinedrama | fg\_cinetealorange\_1 | fg\_cinetealorange\_2 | fg\_cinevibrant | fg\_cinewarm | fgcinebasic | fgcinebright | fgcinecold | fgcinedrama | fgcinetealorange\_1 | fgcinetealorange\_2 | fgcinevibrant | fgcinewarm | fight\_club | film\_0987 | film\_9879 | film\_gb-19 | film\_high\_contrast | film\_print\_01 | film\_print\_02 | filmic | filo | flat\_30 | flat\_blue\_moon | flavin | flog\_to\_rec\_709 | foggynight | folger\_50 | ford\_v\_ferrari | foresta | formula\_b | french\_comedy | frosted | frostedbeachpicnic | fuji\_160c | fuji\_160c\_+ | fuji\_160c\_++ | fuji\_160c\_- | fuji\_3510\_constlclip | fuji\_3510\_constlmap | fuji\_3510\_cuspclip | fuji\_3513\_constlclip | fuji\_3513\_constlmap | fuji\_3513\_cuspclip | fuji\_400h | fuji\_400h\_+ | fuji\_400h\_++ | fuji\_400h\_- | fuji\_800z | fuji\_800z\_+ | fuji\_800z\_++ | fuji\_800z\_- | fuji\_astia\_100\_generic | fuji\_astia\_100f | fuji\_fp-100c | fuji\_fp-100c\_+ | fuji\_fp-100c\_++ | fuji\_fp-100c\_+++ | fuji\_fp-100c\_++\_alt | fuji\_fp-100c\_- | fuji\_fp-100c\_-- | fuji\_fp-100c\_alt | fuji\_fp-100c\_cool | fuji\_fp-100c\_cool\_+ | fuji\_fp-100c\_cool\_++ | fuji\_fp-100c\_cool\_- | fuji\_fp-100c\_cool\_-- | fuji\_fp-100c\_negative | fuji\_fp-100c\_negative\_+ | fuji\_fp-100c\_negative\_++ | fuji\_fp-100c\_negative\_+++ | fuji\_fp-100c\_negative\_++\_alt | fuji\_fp-100c\_negative\_- | fuji\_fp-100c\_negative\_-- | fuji\_fp-3000b | fuji\_fp-3000b\_+ | fuji\_fp-3000b\_++ | fuji\_fp-3000b\_+++ | fuji\_fp-3000b\_- | fuji\_fp-3000b\_-- | fuji\_fp-3000b\_hc | fuji\_fp-3000b\_negative | fuji\_fp-3000b\_negative\_+ | fuji\_fp-3000b\_negative\_++ | fuji\_fp-3000b\_negative\_+++ | fuji\_fp-3000b\_negative\_- | fuji\_fp-3000b\_negative\_-- | fuji\_fp-3000b\_negative\_early | fuji\_fp\_100c | fuji\_hdr | fuji\_neopan\_1600 | fuji\_neopan\_1600\_+ | fuji\_neopan\_1600\_++ | fuji\_neopan\_1600\_- | fuji\_neopan\_acros\_100 | fuji\_provia\_100\_generic | fuji\_provia\_100f | fuji\_provia\_400f | fuji\_provia\_400x | fuji\_sensia\_100 | fuji\_superia\_100 | fuji\_superia\_100\_+ | fuji\_superia\_100\_++ | fuji\_superia\_100\_- | fuji\_superia\_1600 | fuji\_superia\_1600\_+ | fuji\_superia\_1600\_++ | fuji\_superia\_1600\_- | fuji\_superia\_200 | fuji\_superia\_200\_xpro | fuji\_superia\_400 | fuji\_superia\_400\_+ | fuji\_superia\_400\_++ | fuji\_superia\_400\_- | fuji\_superia\_800 | fuji\_superia\_800\_+ | fuji\_superia\_800\_++ | fuji\_superia\_800\_- | fuji\_superia\_hg\_1600 | fuji\_superia\_reala\_100 | fuji\_superia\_x-tra\_800 | fuji\_velvia\_100\_generic | fuji\_velvia\_50 | fuji\_xtrans\_iii\_acros | fuji\_xtrans\_iii\_acros+g | fuji\_xtrans\_iii\_acros+r | fuji\_xtrans\_iii\_acros+ye | fuji\_xtrans\_iii\_astia | fuji\_xtrans\_iii\_classic\_chrome | fuji\_xtrans\_iii\_mono | fuji\_xtrans\_iii\_mono+g | fuji\_xtrans\_iii\_mono+r | fuji\_xtrans\_iii\_mono+ye | fuji\_xtrans\_iii\_pro\_neg\_hi | fuji\_xtrans\_iii\_pro\_neg\_std | fuji\_xtrans\_iii\_provia | fuji\_xtrans\_iii\_sepia | fuji\_xtrans\_iii\_velvia | fusion\_88 | futuristicbleak\_1 | futuristicbleak\_2 | futuristicbleak\_3 | futuristicbleak\_4 | going\_for\_a\_walk | golden | golden\_bright | golden\_fade | golden\_mono | golden\_night\_softner\_43 | golden\_sony\_37 | golden\_vibrant | goldengate | goldentime | goldfx\_bright\_spring\_breeze | goldfx\_bright\_summer\_heat | goldfx\_hot\_summer\_heat | goldfx\_perfect\_sunset\_01min | goldfx\_perfect\_sunset\_05min | goldfx\_perfect\_sunset\_10min | goldfx\_spring\_breeze | goldfx\_summer\_heat | good\_morning | green\_15 | green\_2025 | green\_action | green\_afternoon | green\_and\_orange | green\_blues | green\_book | green\_conflict | green\_day\_01 | green\_day\_02 | green\_g\_09 | green\_indoor | green\_light | green\_mono | green\_yellow | greenish\_contrasty | greenish\_fade | greenish\_fade\_1 | gremerta | greyhound | hackmanite | hallowen\_dark | happyness\_133 | hard\_teal\_orange | hardboost | harsh\_day | harsh\_sunset | helios | herderite | heulandite | hiddenite | highlights\_protection | hilutite | hitman | hlg\_1\_1 | honey\_light | hong\_kong | horrorblue | howlite | huesio | husmes | huyan | hydracore | hyla\_68 | hypersthene | hypnosis | hypressen | i\_tonya | ideo | ilford\_delta\_100 | ilford\_delta\_3200 | ilford\_delta\_3200\_+ | ilford\_delta\_3200\_++ | ilford\_delta\_3200\_- | ilford\_delta\_400 | ilford\_fp\_4\_plus\_125 | ilford\_hp\_5 | ilford\_hp\_5\_+ | ilford\_hp\_5\_++ | ilford\_hp\_5\_- | ilford\_hp\_5\_plus\_400 | ilford\_hps\_800 | ilford\_pan\_f\_plus\_50 | ilford\_xp\_2 | inception | indoor\_blue | industrial\_33 | infrared\_-\_dust\_pink | instantc | j | jarklin | jojo\_rabbit | joker | jumanji\_the\_next\_level | jurassic\_world\_fallen\_kingdom | justice\_league | justpeachy | jwick\_21 | k\_tone\_vintage\_kodachrome | kahve\_3 | kh\_1 | kh\_10 | kh\_2 | kh\_3 | kh\_4 | kh\_5 | kh\_6 | kh\_7 | kh\_8 | kh\_9 | killstreak | kingsman\_the\_golden\_circle | knives\_out | kodak\_2383\_constlclip | kodak\_2383\_constlmap | kodak\_2383\_cuspclip | kodak\_2393\_constlclip | kodak\_2393\_constlmap | kodak\_2393\_cuspclip | kodak\_bw\_400\_cn | kodak\_e-100\_gx\_ektachrome\_100 | kodak\_ektachrome\_100\_vs | kodak\_ektachrome\_100\_vs\_generic | kodak\_ektar\_100 | kodak\_elite\_100\_xpro | kodak\_elite\_chrome\_200 | kodak\_elite\_chrome\_400 | kodak\_elite\_color\_200 | kodak\_elite\_color\_400 | kodak\_elite\_extracolor\_100 | kodak\_hie\_hs\_infra | kodak\_kodachrome\_200 | kodak\_kodachrome\_25 | kodak\_kodachrome\_64 | kodak\_kodachrome\_64\_generic | kodak\_portra\_160 | kodak\_portra\_160\_+ | kodak\_portra\_160\_++ | kodak\_portra\_160\_- | kodak\_portra\_160\_nc | kodak\_portra\_160\_nc\_+ | kodak\_portra\_160\_nc\_++ | kodak\_portra\_160\_nc\_- | kodak\_portra\_160\_vc | kodak\_portra\_160\_vc\_+ | kodak\_portra\_160\_vc\_++ | kodak\_portra\_160\_vc\_- | kodak\_portra\_400 | kodak\_portra\_400\_+ | kodak\_portra\_400\_++ | kodak\_portra\_400\_- | kodak\_portra\_400\_nc | kodak\_portra\_400\_nc\_+ | kodak\_portra\_400\_nc\_++ | kodak\_portra\_400\_nc\_- | kodak\_portra\_400\_uc | kodak\_portra\_400\_uc\_+ | kodak\_portra\_400\_uc\_++ | kodak\_portra\_400\_uc\_- | kodak\_portra\_400\_vc | kodak\_portra\_400\_vc\_+ | kodak\_portra\_400\_vc\_++ | kodak\_portra\_400\_vc\_- | kodak\_portra\_800 | kodak\_portra\_800\_+ | kodak\_portra\_800\_++ | kodak\_portra\_800\_- | kodak\_portra\_800\_hc | kodak\_t-max\_100 | kodak\_t-max\_3200 | kodak\_t-max\_400 | kodak\_tmax\_3200 | kodak\_tmax\_3200\_+ | kodak\_tmax\_3200\_++ | kodak\_tmax\_3200\_- | kodak\_tmax\_3200\_alt | kodak\_tri-x\_400 | kodak\_tri-x\_400\_+ | kodak\_tri-x\_400\_++ | kodak\_tri-x\_400\_- | kodak\_tri-x\_400\_alt | korben\_214 | la\_la\_land | landscape | landscape\_01 | landscape\_02 | landscape\_03 | landscape\_04 | landscape\_05 | landscape\_1 | landscape\_10 | landscape\_2 | landscape\_3 | landscape\_4 | landscape\_5 | landscape\_6 | landscape\_7 | landscape\_8 | landscape\_9 | lateafternoonwanderlust | latesunset | lavark | lc\_1 | lc\_10 | lc\_2 | lc\_3 | lc\_4 | lc\_5 | lc\_6 | lc\_7 | lc\_8 | lc\_9 | lenox\_340 | levex | life\_giving\_tree | light | light\_blown | litore | little\_women | logan | lomo | lomography\_redscale\_100 | lomography\_x-pro\_slide\_200 | london\_nights | longbeachmorning | loro | lotta | louetta | low\_contrast\_blue | low\_key\_01 | lucky\_64 | lushgreen | lushgreensummer | mad\_max\_fury\_road | maesky | magenta\_day | magenta\_day\_01 | magenta\_dream | magenta\_yellow | magentacoffee | magichour | marriage\_story | matrix | mckinnon\_75 | memories | mercato | metropolis | milo\_5 | minimalistcaffeination | modern\_film | modern\_films\_01 | modern\_films\_02 | modern\_films\_03 | modern\_films\_04 | modern\_films\_05 | modern\_films\_06 | modern\_films\_07 | molti | mono\_2 | mono\_tinted | monochrome | monochrome\_1 | monochrome\_2 | moody\_1 | moody\_10 | moody\_2 | moody\_3 | moody\_4 | moody\_5 | moody\_6 | moody\_7 | moody\_8 | moody\_9 | moonlight | moonlight\_01 | moonlight\_2 | moonrise | morning\_6 | morroco\_16 | mostly\_blue | mother! | motus | moviz\_1 | moviz\_10 | moviz\_11 | moviz\_12 | moviz\_13 | moviz\_14 | moviz\_15 | moviz\_16 | moviz\_17 | moviz\_18 | moviz\_19 | moviz\_2 | moviz\_20 | moviz\_21 | moviz\_22 | moviz\_23 | moviz\_24 | moviz\_25 | moviz\_26 | moviz\_27 | moviz\_28 | moviz\_29 | moviz\_3 | moviz\_30 | moviz\_31 | moviz\_32 | moviz\_33 | moviz\_34 | moviz\_35 | moviz\_36 | moviz\_37 | moviz\_38 | moviz\_39 | moviz\_4 | moviz\_40 | moviz\_41 | moviz\_42 | moviz\_43 | moviz\_44 | moviz\_45 | moviz\_46 | moviz\_47 | moviz\_48 | moviz\_5 | moviz\_6 | moviz\_7 | moviz\_8 | moviz\_9 | mucca | mute\_shift | muted\_01 | muted\_fade | mysticpurplesunset | nah | natural\_vivid | naturalboost | negative | nemesis | neon\_770 | neutral | neutral\_pump | neutral\_teal\_orange | neutral\_warm\_fade | newspaper | night\_01 | night\_02 | night\_03 | night\_04 | night\_05 | night\_blade\_4 | night\_king\_141 | night\_spy | night\_view | nightfromday | nightlife | nigrum | no\_time\_to\_die | nostalgiahoney | nostalgic | nw-1 | nw-10 | nw-2 | nw-3 | nw-4 | nw-5 | nw-6 | nw-7 | nw-8 | nw-9 | old\_west | once\_upon\_a\_time | once\_upon\_a\_time\_in\_hollywood | onda | only\_red | only\_red\_and\_blue | operation\_yellow | orange\_dark\_4 | orange\_dark\_7 | orange\_dark\_look | orange\_tone | orange\_underexposed | orangeandblue | oranges | padre | paladin | paladin\_1875 | parasite | partia | pasadena\_21 | passing\_by | perso | picola | pink\_fade | pirates\_of\_the\_caribbean | pitaya\_15 | pmcinematic\_01 | pmcinematic\_02 | pmcinematic\_03 | pmcinematic\_04 | pmcinematic\_05 | pmcinematic\_06 | pmcinematic\_07 | pmnight\_01 | pmnight\_02 | pmnight\_03 | pmnight\_04 | pmnight\_05 | polaroid\_664 | polaroid\_665 | polaroid\_665\_+ | polaroid\_665\_++ | polaroid\_665\_- | polaroid\_665\_-- | polaroid\_665\_negative | polaroid\_665\_negative\_+ | polaroid\_665\_negative\_- | polaroid\_665\_negative\_hc | polaroid\_667 | polaroid\_669 | polaroid\_669\_+ | polaroid\_669\_++ | polaroid\_669\_+++ | polaroid\_669\_- | polaroid\_669\_-- | polaroid\_669\_cold | polaroid\_669\_cold\_+ | polaroid\_669\_cold\_- | polaroid\_669\_cold\_-- | polaroid\_672 | polaroid\_690 | polaroid\_690\_+ | polaroid\_690\_++ | polaroid\_690\_- | polaroid\_690\_-- | polaroid\_690\_cold | polaroid\_690\_cold\_+ | polaroid\_690\_cold\_++ | polaroid\_690\_cold\_- | polaroid\_690\_cold\_-- | polaroid\_690\_warm | polaroid\_690\_warm\_+ | polaroid\_690\_warm\_++ | polaroid\_690\_warm\_- | polaroid\_690\_warm\_-- | polaroid\_polachrome | polaroid\_px-100uv+\_cold | polaroid\_px-100uv+\_cold\_+ | polaroid\_px-100uv+\_cold\_++ | polaroid\_px-100uv+\_cold\_+++ | polaroid\_px-100uv+\_cold\_- | polaroid\_px-100uv+\_cold\_-- | polaroid\_px-100uv+\_warm | polaroid\_px-100uv+\_warm\_+ | polaroid\_px-100uv+\_warm\_++ | polaroid\_px-100uv+\_warm\_+++ | polaroid\_px-100uv+\_warm\_- | polaroid\_px-100uv+\_warm\_-- | polaroid\_px-680 | polaroid\_px-680\_+ | polaroid\_px-680\_++ | polaroid\_px-680\_- | polaroid\_px-680\_-- | polaroid\_px-680\_cold | polaroid\_px-680\_cold\_+ | polaroid\_px-680\_cold\_++ | polaroid\_px-680\_cold\_++\_alt | polaroid\_px-680\_cold\_- | polaroid\_px-680\_cold\_-- | polaroid\_px-680\_warm | polaroid\_px-680\_warm\_+ | polaroid\_px-680\_warm\_++ | polaroid\_px-680\_warm\_- | polaroid\_px-680\_warm\_-- | polaroid\_px-70 | polaroid\_px-70\_+ | polaroid\_px-70\_++ | polaroid\_px-70\_+++ | polaroid\_px-70\_- | polaroid\_px-70\_-- | polaroid\_px-70\_cold | polaroid\_px-70\_cold\_+ | polaroid\_px-70\_cold\_++ | polaroid\_px-70\_cold\_- | polaroid\_px-70\_cold\_-- | polaroid\_px-70\_warm | polaroid\_px-70\_warm\_+ | polaroid\_px-70\_warm\_++ | polaroid\_px-70\_warm\_- | polaroid\_px-70\_warm\_-- | polaroid\_time\_zero\_expired | polaroid\_time\_zero\_expired\_+ | polaroid\_time\_zero\_expired\_++ | polaroid\_time\_zero\_expired\_- | polaroid\_time\_zero\_expired\_-- | polaroid\_time\_zero\_expired\_--- | polaroid\_time\_zero\_expired\_cold | polaroid\_time\_zero\_expired\_cold\_- | polaroid\_time\_zero\_expired\_cold\_-- | polaroid\_time\_zero\_expired\_cold\_--- | portrait | portrait\_1 | portrait\_10 | portrait\_2 | portrait\_3 | portrait\_4 | portrait\_5 | portrait\_6 | portrait\_7 | portrait\_8 | portrait\_9 | progressen | protect\_highlights\_01 | prussian\_blue | pseudogrey | purple | purple\_2 | quraqqq\_12 | randas | red\_afternoon\_01 | red\_day\_01 | red\_dream\_01 | redblueyellow | reds | reds\_oranges\_yellows | reeve\_38 | remy\_24 | rest\_33 | retro | retro\_brown\_01 | retro\_magenta\_01 | retro\_summer\_3 | retro\_yellow\_01 | rocketman | rollei\_ir\_400 | rollei\_ortho\_25 | rollei\_retro\_100\_tonal | rollei\_retro\_80s | rotate\_muted | rotate\_vibrant | rotated | rotated\_crush | satid | saturated\_blue | saving\_private\_damon | scala | science\_fiction | scrittle | sea | seges | selor | sensum | separation | serenity | seringe\_4 | serpent | seventies\_magazine | sevsuz | shade\_kings\_ink | shadow\_king\_39 | shine | sicario | sino | skin\_tones | slog\_to\_rec\_709\_basic | slog\_to\_rec\_709\_contrasty | slog\_to\_rec\_709\_crush\_shadows | slog\_to\_rec\_709\_green\_correction | smart\_contrast | smokey | smooth\_clear | smooth\_cromeish | smooth\_fade | smooth\_green\_orange | smooth\_sailing | smooth\_teal\_orange | soft\_fade | softblackandwhite | softwarming | solarized\_color | solarized\_color\_2 | soldi | spider-man\_far\_from\_home | spotlight | springmorning | sprocket\_231 | spy\_29 | standard | star\_wars\_the\_rise\_of\_skywalker | strano | street | stringa | studio\_skin\_tone\_shaper | subtle\_blue | subtle\_green | subtle\_yellow | sully | summer | summer\_alt | sunlight\_love\_11 | sunlightlove | sunny | sunny\_alt | sunny\_rich | sunny\_warm | sunset | sunset\_aqua\_orange | sunset\_intense\_violet\_blue | sunset\_violet\_mood | super\_warm | super\_warm\_rich | sutro\_fx | sweet\_bubblegum | sweet\_gelatto | taşdemirrr\_1 | taiga | tarraco | teal-orange\_for\_flog | teal\_fade | teal\_moonlight | tealmagentagold | tealorange | tealorange\_1 | tealorange\_2 | tealorange\_3 | technicalfx\_backlight\_filter | teigen\_28 | tenet | tensiongreen\_1 | tensiongreen\_2 | tensiongreen\_3 | tensiongreen\_4 | terra\_4 | the\_dark\_knight | the\_darkest\_hour | the\_gentelmen | the\_grand\_budapest\_hotel | the\_hurt\_locker | the\_irishman | the\_lighthouse | the\_lobster | the\_martian | the\_matrices | the\_revenant | the\_shape\_of\_water | the\_social\_network | the\_two\_popes | the\_way\_back | thor\_ragnarok | thriller\_2 | tirare | toastedgarden | top\_gun\_maverick | trent\_18 | true\_colors\_8 | turkiest\_42 | tutto | tweed\_71 | ultra\_water | uncut\_gems | undeniable | undeniable\_2 | underwater | unknown | upglow | urban\_01 | urban\_02 | urban\_03 | urban\_04 | urban\_05 | urban\_cowboy | uzbek\_bukhara | uzbek\_marriage | uzbek\_samarcande | valize | valsky | velvetia | venom | very\_warm\_greenish | vfb\_21 | vibrant | vibrant\_alien | vibrant\_contrast | vibrant\_cromeish | victory | vintage | vintage\_01 | vintage\_02 | vintage\_03 | vintage\_04 | vintage\_05 | vintage\_163 | vintage\_alt | vintage\_brighter | vintage\_chrome | vintage\_mob | vintage\_warmth\_1 | violet\_taste | vireo\_37 | vita | vivid | vubes | war\_for\_the\_planet\_of\_the\_apes | warm | warm\_dark\_contrasty | warm\_fade | warm\_fade\_1 | warm\_highlight | warm\_neutral | warm\_sunset\_red | warm\_teal | warm\_vintage | warm\_yellow | wavefire | waves | well\_see | western | western\_6 | westernlut\_2 | westernlut\_2\_13 | whiter\_whites | winterlighthouse | wipe | wolf\_of\_wall\_street | wonder\_woman | wooden\_gold\_20 | x-men\_dark\_phoenix | yangabuz\_8 | yellow\_55b | yellow\_film\_01 | yellowstone | you\_can\_do\_it | zed\_32 | zeke\_39 | zilverfx\_bw\_solarization | zilverfx\_infrared | zilverfx\_vintage\_bw | zombieland\_double\_tap }  

## Default values:

resolution=33 and cut\_and\_round=1.

## Example of use:

clut summer clut alien\_green,17 clut orange\_dark4,48

  

[![](img/t0_clut.jpg)](img/f0_clut.jpg)

Command: **clut summer clut alien\_green,17 clut orange\_dark4,48**

[![](img/t1_clut.jpg)](img/f1_clut.jpg)

Command: **clut summer clut alien\_green,17 clut orange\_dark4,48**

[![](img/t2_clut.jpg)](img/f2_clut.jpg)

Command: **clut summer clut alien\_green,17 clut orange\_dark4,48**

---

# Command: clut2hald
**Category:** Colors
**Source:** https://gmic.eu/reference/clut2hald.html#top

# clut2hald

### No argumentsDescription:Convert selected 3D CLUTs to 2D HaldCLUTs. Example of use: clut summer +clut2hald Command: **clut summer +clut2hald** Command: **clut summer +clut2hald**

---

# Command: cmy2rgb
**Category:** Colors
**Source:** https://gmic.eu/reference/cmy2rgb.html#top

# cmy2rgb

### No argumentsDescription:Convert color representation of selected images from CMY to RGB.

---

# Command: cmyk2rgb
**Category:** Colors
**Source:** https://gmic.eu/reference/cmyk2rgb.html#top

# cmyk2rgb

### No argumentsDescription:Convert color representation of selected images from CMYK to RGB.

---

# Command: colorblind
**Category:** Colors
**Source:** https://gmic.eu/reference/colorblind.html#top

# colorblind

## Arguments:

* type={ 0:Protanopia | 1:Protanomaly | 2:Deuteranopia | 3:Deuteranomaly | 4:Tritanopia | 5:Tritanomaly | 6:Achromatopsia | 7:Achromatomaly }

## Description:

Simulate color blindness vision.  
  
Simulation method of Vienot, Brettel & Mollon 1999, "Digital video colourmaps for checking the legibility of displays by dichromats".  
The dichromacy matrices of the paper were adapted to sRGB (RGB->XYZ).  
Anomalous trichromacy simulated via linear interpolation with the identity and a factor of 0.6.  

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +colorblind 0

  

[![](img/t0_colorblind.jpg)](img/f0_colorblind.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +colorblind 0**

[![](img/t1_colorblind.jpg)](img/f1_colorblind.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +colorblind 0**

---

# Command: colormap
**Category:** Colors
**Source:** https://gmic.eu/reference/colormap.html#top

# colormap

## Arguments:

* nb\_levels>=0,\_method={ 0:Median-cut | 1:K-means },\_sort\_vectors

## Description:

Estimate best-fitting colormap with nb\_colors entries, to index selected images.  
  
Set nb\_levels==0 to extract all existing colors of an image.  
sort\_vectors can be { 0:Unsorted | 1:By increasing norm | 2:By decreasing occurrence }.  

## Default values:

method=1 and sort\_vectors=1.

This command has a [tutorial page](https://gmic.eu/oldtutorial/_colormap).

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +colormap[0] 4 +colormap[0] 8 +colormap[0] 16

  

[![](img/t0_colormap.jpg)](img/f0_colormap.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +colormap[0] 4 +colormap[0] 8 +colormap[0] 16**

[![](img/t1_colormap.jpg)](img/f1_colormap.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +colormap[0] 4 +colormap[0] 8 +colormap[0] 16**

[![](img/t2_colormap.jpg)](img/f2_colormap.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +colormap[0] 4 +colormap[0] 8 +colormap[0] 16**

[![](img/t3_colormap.jpg)](img/f3_colormap.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +colormap[0] 4 +colormap[0] 8 +colormap[0] 16**

---

# Command: compose_channels
**Category:** Colors
**Source:** https://gmic.eu/reference/compose_channels.html#top

# compose\_channels

## Arguments:

* \_operator

## Description:

Compose all channels of each selected image, using specified arithmetic operator (+,-,or,min,...).  

## Default values:

operator=+.

This command has a [tutorial page](https://gmic.eu/tutorial/compose_channels).

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +compose\_channels and

  

[![](img/t0_compose_channels.jpg)](img/f0_compose_channels.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +compose\_channels and**

[![](img/t1_compose_channels.jpg)](img/f1_compose_channels.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +compose\_channels and**

---

# Command: contrast
**Category:** Colors
**Source:** https://gmic.eu/reference/contrast.html#top

# contrast

## Arguments:

* strength

## Description:

Change contrast of selected images, with specified strength.  

If strength is positive, image contrast is amplified.

If strength is negative, image contrast is reduced.

A typical value range for parameter strength is [-100,100].  

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +contrast 20

  

[![](img/t0_contrast.jpg)](img/f0_contrast.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +contrast 20**

[![](img/t1_contrast.jpg)](img/f1_contrast.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +contrast 20**

---

# Command: count_colors
**Category:** Colors
**Source:** https://gmic.eu/reference/count_colors.html#top

# count\_colors

## Arguments:

* \_count\_until={ 0:None | >0:Max number of counted colors }

## Description:

Count number of distinct colors in selected images until it reaches the specified max number of counted colors.  
  
Set count\_until to 0 to disable limit on counted colors.  
This command returns the number of distinct colors for each image (separated by commas).

---

# Command: deltaE
**Category:** Colors
**Source:** https://gmic.eu/reference/deltaE.html#top

# deltaE

## Arguments:

* [image],\_metric={ 0:DeltaE\_1976 | 1:DeltaE\_2000 },"\_to\_Lab\_command"

## Description:

Compute the CIE DeltaE color difference between selected images and specified [image].  
  
Argument to\_Lab\_command is a command able to convert colors of [image] into a Lab representation.  

## Default values:

metric=1 and to\_Lab\_command="srgb2lab".

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +blur 2 +deltaE[0] [1],1,srgb2lab

  

[![](img/t0_deltaE.jpg)](img/f0_deltaE.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +blur 2 +deltaE[0] [1],1,srgb2lab**

[![](img/t1_deltaE.jpg)](img/f1_deltaE.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +blur 2 +deltaE[0] [1],1,srgb2lab**

[![](img/t2_deltaE.jpg)](img/f2_deltaE.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +blur 2 +deltaE[0] [1],1,srgb2lab**

---

# Command: direction2rgb
**Category:** Colors
**Source:** https://gmic.eu/reference/direction2rgb.html#top

# direction2rgb

### No argumentsDescription:Compute RGB representation of selected 2D direction fields. Example of use: <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> luminance gradient append c blur 2 orientation +direction2rgb Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> luminance gradient append c blur 2 orientation +direction2rgb** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> luminance gradient append c blur 2 orientation +direction2rgb**

---

# Command: ditheredbw
**Category:** Colors
**Source:** https://gmic.eu/reference/ditheredbw.html#top

# ditheredbw

### No argumentsDescription:Create dithered B&W version of selected images. Example of use: <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +equalize ditheredbw[-1] Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +equalize ditheredbw[-1]** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +equalize ditheredbw[-1]**

---

# Command: fill_color
**Category:** Colors
**Source:** https://gmic.eu/reference/fill_color.html#top

# fill\_color

## Arguments:

* col1,...,colN

## Description:

Fill selected images with specified color.  

(*equivalent to shortcut command* fc).

This command has a [tutorial page](https://gmic.eu/oldtutorial/_fill_color).

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +fill\_color 255,0,255

  

[![](img/t0_fill_color.jpg)](img/f0_fill_color.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +fill\_color 255,0,255**

[![](img/t1_fill_color.jpg)](img/f1_fill_color.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +fill\_color 255,0,255**

---

# Command: gradient2rgb
**Category:** Colors
**Source:** https://gmic.eu/reference/gradient2rgb.html#top

# gradient2rgb

## Arguments:

* \_is\_orientation={ 0:No | 1:Yes }

## Description:

Compute RGB representation of 2D gradient of selected images.  

## Default values:

is\_orientation=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +gradient2rgb 0 equalize[-1]

  

[![](img/t0_gradient2rgb.jpg)](img/f0_gradient2rgb.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +gradient2rgb 0 equalize[-1]**

[![](img/t1_gradient2rgb.jpg)](img/f1_gradient2rgb.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +gradient2rgb 0 equalize[-1]**

---

# Command: hald2clut
**Category:** Colors
**Source:** https://gmic.eu/reference/hald2clut.html#top

# hald2clut

### No argumentsDescription:Convert selected 2D HaldCLUTs to 3D CLUTs.

---

# Command: hcy2rgb
**Category:** Colors
**Source:** https://gmic.eu/reference/hcy2rgb.html#top

# hcy2rgb

### No argumentsDescription:Convert color representation of selected images from HCY to RGB.

---

# Command: hsi2rgb
**Category:** Colors
**Source:** https://gmic.eu/reference/hsi2rgb.html#top

# hsi2rgb

### No argumentsDescription:Convert color representation of selected images from HSI to RGB.

---

# Command: hsi82rgb
**Category:** Colors
**Source:** https://gmic.eu/reference/hsi82rgb.html#top

# hsi82rgb

### No argumentsDescription:Convert color representation of selected images from HSI8 to RGB.

---

# Command: hsl2rgb
**Category:** Colors
**Source:** https://gmic.eu/reference/hsl2rgb.html#top

# hsl2rgb

### No argumentsDescription:Convert color representation of selected images from HSL to RGB.

---

# Command: hsl82rgb
**Category:** Colors
**Source:** https://gmic.eu/reference/hsl82rgb.html#top

# hsl82rgb

### No argumentsDescription:Convert color representation of selected images from HSL8 to RGB.

---

# Command: hsv2rgb
**Category:** Colors
**Source:** https://gmic.eu/reference/hsv2rgb.html#top

# hsv2rgb

### No argumentsDescription:Convert color representation of selected images from HSV to RGB. Example of use: (0,360;0,360^0,0;1,1^1,1;1,1) resize 400,400,1,3,3 hsv2rgb Command: **(0,360;0,360^0,0;1,1^1,1;1,1) resize 400,400,1,3,3 hsv2rgb**

---

# Command: hsv82rgb
**Category:** Colors
**Source:** https://gmic.eu/reference/hsv82rgb.html#top

# hsv82rgb

### No argumentsDescription:Convert color representation of selected images from HSV8 to RGB.

---

# Command: int2rgb
**Category:** Colors
**Source:** https://gmic.eu/reference/int2rgb.html#top

# int2rgb

### No argumentsDescription:Convert color representation of selected images from INT24 to RGB.

---

# Command: ipremula
**Category:** Colors
**Source:** https://gmic.eu/reference/ipremula.html#top

# ipremula

### No argumentsDescription:Convert selected images with premultiplied alpha colors to normal colors. See also:[premula](premula.html).

---

# Command: jzazbz2rgb
**Category:** Colors
**Source:** https://gmic.eu/reference/jzazbz2rgb.html#top

# jzazbz2rgb

## Arguments:

* illuminant={ 0:D50 | 1:D65 | 2:E }    or
* (no arg)

## Description:

Convert color representation of selected images from RGB to Jzazbz.  

## Default values:

illuminant=2.

---

# Command: jzazbz2xyz
**Category:** Colors
**Source:** https://gmic.eu/reference/jzazbz2xyz.html#top

# jzazbz2xyz

### No argumentsDescription:Convert color representation of selected images from RGB to XYZ.

---

# Command: lab2lch
**Category:** Colors
**Source:** https://gmic.eu/reference/lab2lch.html#top

# lab2lch

### No argumentsDescription:Convert color representation of selected images from Lab to Lch.

---

# Command: lab2rgb
**Category:** Colors
**Source:** https://gmic.eu/reference/lab2rgb.html#top

# lab2rgb

## Arguments:

* illuminant={ 0:D50 | 1:D65 | 2:E }    or
* (no arg)

## Description:

Convert color representation of selected images from Lab to RGB.  

## Default values:

illuminant=2.

## Example of use:

(50,50;50,50^-3,3;-3,3^-3,-3;3,3) resize 400,400,1,3,3 lab2rgb

  
[![](img/t_lab2rgb.jpg)](img/f_lab2rgb.jpg)

Command: **(50,50;50,50^-3,3;-3,3^-3,-3;3,3) resize 400,400,1,3,3 lab2rgb**

---

# Command: lab2srgb
**Category:** Colors
**Source:** https://gmic.eu/reference/lab2srgb.html#top

# lab2srgb

## Arguments:

* illuminant={ 0:D50 | 1:D65 | 2:E }    or
* (no arg)

## Description:

Convert color representation of selected images from Lab to sRGB.  

## Default values:

illuminant=2.

## Example of use:

(50,50;50,50^-3,3;-3,3^-3,-3;3,3) resize 400,400,1,3,3 lab2rgb

  
[![](img/t_lab2srgb.jpg)](img/f_lab2srgb.jpg)

Command: **(50,50;50,50^-3,3;-3,3^-3,-3;3,3) resize 400,400,1,3,3 lab2rgb**

---

# Command: lab82srgb
**Category:** Colors
**Source:** https://gmic.eu/reference/lab82srgb.html#top

# lab82srgb

## Arguments:

* illuminant={ 0:D50 | 1:D65 | 2:E }    or
* (no arg)

## Description:

Convert color representation of selected images from Lab8 to sRGB.  

## Default values:

illuminant=2.

## Example of use:

(50,50;50,50^-3,3;-3,3^-3,-3;3,3) resize 400,400,1,3,3 lab2rgb

  
[![](img/t_lab82srgb.jpg)](img/f_lab82srgb.jpg)

Command: **(50,50;50,50^-3,3;-3,3^-3,-3;3,3) resize 400,400,1,3,3 lab2rgb**

---

# Command: lab2xyz
**Category:** Colors
**Source:** https://gmic.eu/reference/lab2xyz.html#top

# lab2xyz

## Arguments:

* illuminant={ 0:D50 | 1:D65 | 2:E }    or
* (no arg)

## Description:

Convert color representation of selected images from Lab to XYZ.  

## Default values:

illuminant=2.

---

# Command: lab82rgb
**Category:** Colors
**Source:** https://gmic.eu/reference/lab82rgb.html#top

# lab82rgb

## Arguments:

* illuminant={ 0:D50 | 1:D65 | 2:E }    or
* (no arg)

## Description:

Convert color representation of selected images from Lab8 to RGB.  

## Default values:

illuminant=2.

---

# Command: lch2lab
**Category:** Colors
**Source:** https://gmic.eu/reference/lch2lab.html#top

# lch2lab

### No argumentsDescription:Convert color representation of selected images from Lch to Lab.

---

# Command: lch2rgb
**Category:** Colors
**Source:** https://gmic.eu/reference/lch2rgb.html#top

# lch2rgb

## Arguments:

* illuminant={ 0:D50 | 1:D65 | 2:E }    or
* (no arg)

## Description:

Convert color representation of selected images from Lch to RGB.  

## Default values:

illuminant=2.

---

# Command: lch82rgb
**Category:** Colors
**Source:** https://gmic.eu/reference/lch82rgb.html#top

# lch82rgb

## Arguments:

* illuminant={ 0:D50 | 1:D65 | 2:E }    or
* (no arg)

## Description:

Convert color representation of selected images from Lch8 to RGB.  

## Default values:

illuminant=2.

---

# Command: luminance
**Category:** Colors
**Source:** https://gmic.eu/reference/luminance.html#top

# luminance

### No argumentsDescription:Compute luminance of selected sRGB images. This command has a [tutorial page](https://gmic.eu/tutorial/luminance). Example of use: <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +luminance Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +luminance** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +luminance**

---

# Command: lightness
**Category:** Colors
**Source:** https://gmic.eu/reference/lightness.html#top

# lightness

### No argumentsDescription:Compute lightness of selected sRGB images. Example of use: <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +lightness Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +lightness** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +lightness**

---

# Command: lut_contrast
**Category:** Colors
**Source:** https://gmic.eu/reference/lut_contrast.html#top

# lut\_contrast

## Arguments:

* \_nb\_colors>1,\_min\_rgb\_value

## Description:

Generate a RGB colormap where consecutive colors have high contrast.  
  
This function performs a specific score maximization to generate the result, so  
it may take some time when nb\_colors is high.  

## Default values:

nb\_colors=256 and min\_rgb\_value=64.

---

# Command: map_clut
**Category:** Colors
**Source:** https://gmic.eu/reference/map_clut.html#top

# map\_clut

## Arguments:

* [clut] | "clut\_name"

## Description:

Map specified RGB color LUT to selected images.  

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> uniform\_distribution {2^6},3 mirror[-1] x +map\_clut[0] [1]

  

[![](img/t0_map_clut.jpg)](img/f0_map_clut.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> uniform\_distribution {2^6},3 mirror[-1] x +map\_clut[0] [1]**

[![](img/t1_map_clut.jpg)](img/f1_map_clut.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> uniform\_distribution {2^6},3 mirror[-1] x +map\_clut[0] [1]**

[![](img/t2_map_clut.jpg)](img/f2_map_clut.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> uniform\_distribution {2^6},3 mirror[-1] x +map\_clut[0] [1]**

---

# Command: match_histogram
**Category:** Colors
**Source:** https://gmic.eu/reference/match_histogram.html#top

# match\_histogram

## Arguments:

* [reference\_image],\_nb\_levels>0,\_color\_channels

## Description:

Transfer histogram of the specified reference image to selected images.  
  
Argument color channels is the same as with command apply\_channels.  

## Default values:

nb\_levels=256 and color\_channels=all.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> 100,100,1,3,"u([256,200,100])" +match\_histogram[0] [1]

  

[![](img/t0_match_histogram.jpg)](img/f0_match_histogram.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> 100,100,1,3,"u([256,200,100])" +match\_histogram[0] [1]**

[![](img/t1_match_histogram.jpg)](img/f1_match_histogram.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> 100,100,1,3,"u([256,200,100])" +match\_histogram[0] [1]**

[![](img/t2_match_histogram.jpg)](img/f2_match_histogram.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> 100,100,1,3,"u([256,200,100])" +match\_histogram[0] [1]**

---

# Command: match_pca
**Category:** Colors
**Source:** https://gmic.eu/reference/match_pca.html#top

# match\_pca

## Arguments:

* [reference\_image],\_color\_channels

## Description:

Transfer mean and covariance matrix of specified vector-valued reference image to selected images.  
  
Argument color channels is the same as with command apply\_channels.  

## Default values:

color\_channels=all.

## Example of use:

sample lena,earth +match\_pca[0] [1]

  

[![](img/t0_match_pca.jpg)](img/f0_match_pca.jpg)

Command: **sample lena,earth +match\_pca[0] [1]**

[![](img/t1_match_pca.jpg)](img/f1_match_pca.jpg)

Command: **sample lena,earth +match\_pca[0] [1]**

[![](img/t2_match_pca.jpg)](img/f2_match_pca.jpg)

Command: **sample lena,earth +match\_pca[0] [1]**

---

# Command: match_rgb
**Category:** Colors
**Source:** https://gmic.eu/reference/match_rgb.html#top

# match\_rgb

## Arguments:

* [reference],\_gamma>=0,\_regularization>=0,\_luminosity\_constraints>=0,\_rgb\_resolution>=0,\_is\_constraints={ 0:No | 1:Yes }

## Description:

Transfer colors from specified reference image (given as argument) to selected image.  
  
gamma determines the importance of color occurrences in the matching process (0:None to 1:Huge).  
regularization determines the number of guided filter iterations to remove quantization effects.  
luminosity\_constraints tells if luminosity constraints must be applied on non-confident matched colors.  
is\_constraints tells if additional hard color constraints must be set (opens an interactive window).  

## Default values:

gamma=0.3,regularization=8, luminosity\_constraints=0.1, rgb\_resolution=64 and is\_constraints=0.

## Example of use:

sample pencils,wall +match\_rgb[0] [1],0,0.01

  

[![](img/t0_match_rgb.jpg)](img/f0_match_rgb.jpg)

Command: **sample pencils,wall +match\_rgb[0] [1],0,0.01**

[![](img/t1_match_rgb.jpg)](img/f1_match_rgb.jpg)

Command: **sample pencils,wall +match\_rgb[0] [1],0,0.01**

[![](img/t2_match_rgb.jpg)](img/f2_match_rgb.jpg)

Command: **sample pencils,wall +match\_rgb[0] [1],0,0.01**

---

# Command: mix_rgb
**Category:** Colors
**Source:** https://gmic.eu/reference/mix_rgb.html#top

# mix\_rgb

## Arguments:

* a11,a12,a13,a21,a22,a23,a31,a32,a33

## Description:

Apply 3x3 specified matrix to RGB colors of selected images.  

## Default values:

a11=1, a12=a13=a21=0, a22=1, a23=a31=a32=0 and a33=1.

This command has a [tutorial page](https://gmic.eu/tutorial/mix_rgb).

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +mix\_rgb 0,1,0,1,0,0,0,0,1

  

[![](img/t0_mix_rgb.jpg)](img/f0_mix_rgb.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +mix\_rgb 0,1,0,1,0,0,0,0,1**

[![](img/t1_mix_rgb.jpg)](img/f1_mix_rgb.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +mix\_rgb 0,1,0,1,0,0,0,0,1**

---

# Command: oklab2rgb
**Category:** Colors
**Source:** https://gmic.eu/reference/oklab2rgb.html#top

# oklab2rgb

### No argumentsDescription:Convert color representation of selected images from OKlab to RGB. (see colorspace definition at: <https://bottosson.github.io/posts/oklab/> ). See also:[rgb2oklab](rgb2oklab.html).

---

# Command: palette
**Category:** Colors
**Source:** https://gmic.eu/reference/palette.html#top

# palette

## Arguments:

* palette\_name | palette\_number

## Description:

Input specified color palette at the end of the image list.  
  
palette\_name can be { default | hsv | lines | hot | cool | jet | flag | cube | rainbow | parula | spring | summer | autumn | winter | bone | copper | pink | vga | algae | amp | balance | curl | deep | delta | dense | diff | gray | haline | ice | matter | oxy | phase | rain | solar | speed | tarn | tempo | thermal | topo | turbid | aurora | hocuspocus | srb2 | uzebox | amiga7800 | amiga7800mess | fornaxvoid1 }  

## Example of use:

palette hsv

  
[![](img/t_palette.jpg)](img/f_palette.jpg)

Command: **palette hsv**

---

# Command: premula
**Category:** Colors
**Source:** https://gmic.eu/reference/premula.html#top

# premula

### No argumentsDescription:Convert selected images with normal colors to premultiplied alpha colors. After conversion, alpha channel of resulting images has value in [0,1] range. See also:[ipremula](ipremula.html).

---

# Command: pseudogray
**Category:** Colors
**Source:** https://gmic.eu/reference/pseudogray.html#top

# pseudogray

## Arguments:

* \_max\_increment>=0,\_JND\_threshold>=0,\_bits\_depth>0

## Description:

Generate pseudogray colormap with specified increment and perceptual threshold.  
  
If JND\_threshold is 0, no perceptual constraints are applied.  

## Default values:

max\_increment=5, JND\_threshold=2.3 and bits\_depth=8.

## Example of use:

pseudogray 5

  
[![](img/t_pseudogray.jpg)](img/f_pseudogray.jpg)

Command: **pseudogray 5**

---

# Command: random_clut
**Category:** Colors
**Source:** https://gmic.eu/reference/random_clut.html#top

# random\_clut

## Arguments:

* \_seed = { >=0 | -1 }

## Description:

Generate a 33x33x33 random 3D color LUT.  
  
If specified seed is positive, it is used as a seed for the random number generator @cli : (so that using the same seed will return the same CLUT).  

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> random\_clut +map\_clut.. .

  

[![](img/t0_random_clut.jpg)](img/f0_random_clut.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> random\_clut +map\_clut.. .**

[![](img/t1_random_clut.jpg)](img/f1_random_clut.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> random\_clut +map\_clut.. .**

[![](img/t2_random_clut.jpg)](img/f2_random_clut.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> random\_clut +map\_clut.. .**

---

# Command: random_clut
**Category:** Colors
**Source:** https://gmic.eu/reference/random_clut.html#top

# random\_clut

## Arguments:

* \_seed = { >=0 | -1 }

## Description:

Generate a 33x33x33 random 3D color LUT.  
  
If specified seed is positive, it is used as a seed for the random number generator @cli : (so that using the same seed will return the same CLUT).  

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> random\_clut +map\_clut.. .

  

[![](img/t0_random_clut.jpg)](img/f0_random_clut.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> random\_clut +map\_clut.. .**

[![](img/t1_random_clut.jpg)](img/f1_random_clut.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> random\_clut +map\_clut.. .**

[![](img/t2_random_clut.jpg)](img/f2_random_clut.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> random\_clut +map\_clut.. .**

---

# Command: replace_color
**Category:** Colors
**Source:** https://gmic.eu/reference/replace_color.html#top

# replace\_color

## Arguments:

* tolerance[%]>=0,smoothness[%]>=0,src1,src2,...,dest1,dest2,...

## Description:

Replace pixels from/to specified colors in selected images.  

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +replace\_color 40,3,204,153,110,255,0,0

  

[![](img/t0_replace_color.jpg)](img/f0_replace_color.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +replace\_color 40,3,204,153,110,255,0,0**

[![](img/t1_replace_color.jpg)](img/f1_replace_color.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +replace\_color 40,3,204,153,110,255,0,0**

---

# Command: retinex
**Category:** Colors
**Source:** https://gmic.eu/reference/retinex.html#top

# retinex

## Arguments:

* \_value\_offset>0,\_colorspace={ hsi | hsv | lab | lrgb | rgb | ycbcr },0<=\_min\_cut<=100,0<=\_max\_cut<=100,\_sigma\_low>0,\_sigma\_mid>0,\_sigma\_high>0

## Description:

Apply multi-scale retinex algorithm on selected images to improve color consistency.  
  
(as described in the page <http://www.ipol.im/pub/art/2014/107/>).  

## Default values:

offset=1, colorspace=hsv, min\_cut=1, max\_cut=1, sigma\_low=15,sigma\_mid=80 and sigma\_high=250.

---

# Command: rgb
**Category:** Colors
**Source:** https://gmic.eu/reference/rgb.html#top

# rgb

## Arguments:

* \_min\_RGB\_value,\_max\_RGB\_value    or
* (no arg)

## Description:

Return a random int-valued RGB color.

---

# Command: rgba
**Category:** Colors
**Source:** https://gmic.eu/reference/rgba.html#top

# rgba

## Arguments:

* \_min\_RGB\_value,\_max\_RGB\_value,\_min\_A\_value,\_max\_A\_value    or
* (no\_arg)

## Description:

Return a random int-valued RGBA color.

---

# Command: rgb2bayer
**Category:** Colors
**Source:** https://gmic.eu/reference/rgb2bayer.html#top

# rgb2bayer

## Arguments:

* \_start\_pattern=0,\_color\_grid=0

## Description:

Transform selected color images to RGB-Bayer sampled images.  

## Default values:

start\_pattern=0 and color\_grid=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +rgb2bayer 0

  

[![](img/t0_rgb2bayer.jpg)](img/f0_rgb2bayer.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +rgb2bayer 0**

[![](img/t1_rgb2bayer.jpg)](img/f1_rgb2bayer.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +rgb2bayer 0**

---

# Command: rgb2cmy
**Category:** Colors
**Source:** https://gmic.eu/reference/rgb2cmy.html#top

# rgb2cmy

### No argumentsDescription:Convert color representation of selected images from RGB to CMY. Example of use: <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2cmy split c Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2cmy split c** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2cmy split c** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2cmy split c**

---

# Command: rgb2cmyk
**Category:** Colors
**Source:** https://gmic.eu/reference/rgb2cmyk.html#top

# rgb2cmyk

### No argumentsDescription:Convert color representation of selected images from RGB to CMYK. Examples of use:• Example #1 <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2cmyk split c Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2cmyk split c** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2cmyk split c** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2cmyk split c** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2cmyk split c** • Example #2 <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2cmyk split c fill[3] 0 append c cmyk2rgb Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2cmyk split c fill[3] 0 append c cmyk2rgb**

---

# Command: rgb2hcy
**Category:** Colors
**Source:** https://gmic.eu/reference/rgb2hcy.html#top

# rgb2hcy

### No argumentsDescription:Convert color representation of selected images from RGB to HCY. Example of use: <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2hcy split c Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2hcy split c** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2hcy split c** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2hcy split c**

---

# Command: rgb2hsi
**Category:** Colors
**Source:** https://gmic.eu/reference/rgb2hsi.html#top

# rgb2hsi

### No argumentsDescription:Convert color representation of selected images from RGB to HSI. Example of use: <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2hsi split c Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2hsi split c** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2hsi split c** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2hsi split c**

---

# Command: rgb2hsi8
**Category:** Colors
**Source:** https://gmic.eu/reference/rgb2hsi8.html#top

# rgb2hsi8

### No argumentsDescription:Convert color representation of selected images from RGB to HSI8. Example of use: <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2hsi8 split c Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2hsi8 split c** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2hsi8 split c** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2hsi8 split c**

---

# Command: rgb2hsl
**Category:** Colors
**Source:** https://gmic.eu/reference/rgb2hsl.html#top

# rgb2hsl

### No argumentsDescription:Convert color representation of selected images from RGB to HSL. Examples of use:• Example #1 <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2hsl split c Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2hsl split c** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2hsl split c** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2hsl split c** • Example #2 <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2hsl +split c add[-3] 100 mod[-3] 360 append[-3--1] c hsl2rgb Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2hsl +split c add[-3] 100 mod[-3] 360 append[-3--1] c hsl2rgb** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2hsl +split c add[-3] 100 mod[-3] 360 append[-3--1] c hsl2rgb**

---

# Command: rgb2hsl8
**Category:** Colors
**Source:** https://gmic.eu/reference/rgb2hsl8.html#top

# rgb2hsl8

### No argumentsDescription:Convert color representation of selected images from RGB to HSL8. Example of use: <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2hsl8 split c Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2hsl8 split c** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2hsl8 split c** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2hsl8 split c**

---

# Command: rgb2hsv
**Category:** Colors
**Source:** https://gmic.eu/reference/rgb2hsv.html#top

# rgb2hsv

### No argumentsDescription:Convert color representation of selected images from RGB to HSV. Examples of use:• Example #1 <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2hsv split c Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2hsv split c** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2hsv split c** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2hsv split c** • Example #2 <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2hsv +split c add[-2] 0.3 cut[-2] 0,1 append[-3--1] c hsv2rgb Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2hsv +split c add[-2] 0.3 cut[-2] 0,1 append[-3--1] c hsv2rgb** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2hsv +split c add[-2] 0.3 cut[-2] 0,1 append[-3--1] c hsv2rgb**

---

# Command: rgb2hsv8
**Category:** Colors
**Source:** https://gmic.eu/reference/rgb2hsv8.html#top

# rgb2hsv8

### No argumentsDescription:Convert color representation of selected images from RGB to HSV8. Example of use: <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2hsv8 split c Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2hsv8 split c** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2hsv8 split c** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2hsv8 split c**

---

# Command: rgb2int
**Category:** Colors
**Source:** https://gmic.eu/reference/rgb2int.html#top

# rgb2int

### No argumentsDescription:Convert color representation of selected images from RGB to INT24 scalars. Example of use: <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2int Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2int**

---

# Command: rgb2jzazbz
**Category:** Colors
**Source:** https://gmic.eu/reference/rgb2jzazbz.html#top

# rgb2jzazbz

## Arguments:

* illuminant={ 0:D50 | 1:D65 | 2:E }    or
* (no arg)

## Description:

Convert color representation of selected images from RGB to Jzazbz.  

## Default values:

illuminant=2.

---

# Command: rgb2lab
**Category:** Colors
**Source:** https://gmic.eu/reference/rgb2lab.html#top

# rgb2lab

## Arguments:

* illuminant={ 0:D50 | 1:D65 | 2:E }    or
* (no arg)

## Description:

Convert color representation of selected images from RGB to Lab.  

## Default values:

illuminant=2.

---

# Command: rgb2lab8
**Category:** Colors
**Source:** https://gmic.eu/reference/rgb2lab8.html#top

# rgb2lab8

## Arguments:

* illuminant={ 0:D50 | 1:D65 | 2:E }    or
* (no arg)

## Description:

Convert color representation of selected images from RGB to Lab8.  

## Default values:

illuminant=2.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2lab8 split c

  

[![](img/t0_rgb2lab8.jpg)](img/f0_rgb2lab8.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2lab8 split c**

[![](img/t1_rgb2lab8.jpg)](img/f1_rgb2lab8.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2lab8 split c**

[![](img/t2_rgb2lab8.jpg)](img/f2_rgb2lab8.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2lab8 split c**

---

# Command: rgb2lch
**Category:** Colors
**Source:** https://gmic.eu/reference/rgb2lch.html#top

# rgb2lch

## Arguments:

* illuminant={ 0:D50 | 1:D65 | 2:E }    or
* (no arg)

## Description:

Convert color representation of selected images from RGB to Lch.  

## Default values:

illuminant=2.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2lch split c

  

[![](img/t0_rgb2lch.jpg)](img/f0_rgb2lch.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2lch split c**

[![](img/t1_rgb2lch.jpg)](img/f1_rgb2lch.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2lch split c**

[![](img/t2_rgb2lch.jpg)](img/f2_rgb2lch.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2lch split c**

---

# Command: rgb2lch8
**Category:** Colors
**Source:** https://gmic.eu/reference/rgb2lch8.html#top

# rgb2lch8

## Arguments:

* illuminant={ 0:D50 | 1:D65 | 2:E }    or
* (no arg)

## Description:

Convert color representation of selected images from RGB to Lch8.  

## Default values:

illuminant=2.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2lch8 split c

  

[![](img/t0_rgb2lch8.jpg)](img/f0_rgb2lch8.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2lch8 split c**

[![](img/t1_rgb2lch8.jpg)](img/f1_rgb2lch8.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2lch8 split c**

[![](img/t2_rgb2lch8.jpg)](img/f2_rgb2lch8.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2lch8 split c**

---

# Command: rgb2luv
**Category:** Colors
**Source:** https://gmic.eu/reference/rgb2luv.html#top

# rgb2luv

### No argumentsDescription:Convert color representation of selected images from RGB to LUV. Example of use: <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2luv split c Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2luv split c** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2luv split c** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2luv split c**

---

# Command: rgb2oklab
**Category:** Colors
**Source:** https://gmic.eu/reference/rgb2oklab.html#top

# rgb2oklab

### No argumentsDescription:Convert color representation of selected images from RGB to Oklab. (see colorspace definition at: <https://bottosson.github.io/posts/oklab/> ). See also:[oklab2rgb](oklab2rgb.html).

---

# Command: rgb2ryb
**Category:** Colors
**Source:** https://gmic.eu/reference/rgb2ryb.html#top

# rgb2ryb

### No argumentsDescription:Convert color representation of selected images from RGB to RYB. Example of use: <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2ryb split c Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2ryb split c** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2ryb split c** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2ryb split c**

---

# Command: rgb2srgb
**Category:** Colors
**Source:** https://gmic.eu/reference/rgb2srgb.html#top

# rgb2srgb

### No argumentsDescription:Convert color representation of selected images from linear RGB to sRGB.

---

# Command: rgb2xyz
**Category:** Colors
**Source:** https://gmic.eu/reference/rgb2xyz.html#top

# rgb2xyz

## Arguments:

* illuminant={ 0:D50 | 1:D65 | 2:E }    or
* (no arg)

## Description:

Convert color representation of selected images from RGB to XYZ.  

## Default values:

illuminant=2.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2xyz split c

  

[![](img/t0_rgb2xyz.jpg)](img/f0_rgb2xyz.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2xyz split c**

[![](img/t1_rgb2xyz.jpg)](img/f1_rgb2xyz.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2xyz split c**

[![](img/t2_rgb2xyz.jpg)](img/f2_rgb2xyz.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2xyz split c**

---

# Command: rgb2xyz8
**Category:** Colors
**Source:** https://gmic.eu/reference/rgb2xyz8.html#top

# rgb2xyz8

## Arguments:

* illuminant={ 0:D50 | 1:D65 | 2:E }    or
* (no arg)

## Description:

Convert color representation of selected images from RGB to XYZ8.  

## Default values:

illuminant=2.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2xyz8 split c

  

[![](img/t0_rgb2xyz8.jpg)](img/f0_rgb2xyz8.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2xyz8 split c**

[![](img/t1_rgb2xyz8.jpg)](img/f1_rgb2xyz8.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2xyz8 split c**

[![](img/t2_rgb2xyz8.jpg)](img/f2_rgb2xyz8.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2xyz8 split c**

---

# Command: rgb2yiq
**Category:** Colors
**Source:** https://gmic.eu/reference/rgb2yiq.html#top

# rgb2yiq

### No argumentsDescription:Convert color representation of selected images from RGB to YIQ. Example of use: <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2yiq split c Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2yiq split c** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2yiq split c** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2yiq split c**

---

# Command: rgb2yiq8
**Category:** Colors
**Source:** https://gmic.eu/reference/rgb2yiq8.html#top

# rgb2yiq8

### No argumentsDescription:Convert color representation of selected images from RGB to YIQ8. Example of use: <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2yiq8 split c Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2yiq8 split c** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2yiq8 split c** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2yiq8 split c**

---

# Command: rgb2ycbcr
**Category:** Colors
**Source:** https://gmic.eu/reference/rgb2ycbcr.html#top

# rgb2ycbcr

### No argumentsDescription:Convert color representation of selected images from RGB to YCbCr. Example of use: <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2ycbcr split c Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2ycbcr split c** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2ycbcr split c** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2ycbcr split c**

---

# Command: rgb2yuv
**Category:** Colors
**Source:** https://gmic.eu/reference/rgb2yuv.html#top

# rgb2yuv

### No argumentsDescription:Convert color representation of selected images from RGB to YUV. Example of use: <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2yuv split c Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2yuv split c** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2yuv split c** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2yuv split c**

---

# Command: rgb2yuv8
**Category:** Colors
**Source:** https://gmic.eu/reference/rgb2yuv8.html#top

# rgb2yuv8

### No argumentsDescription:Convert color representation of selected images from RGB to YUV8. Example of use: <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2yuv8 split c Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2yuv8 split c** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2yuv8 split c** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rgb2yuv8 split c**

---

# Command: remove_opacity
**Category:** Colors
**Source:** https://gmic.eu/reference/remove_opacity.html#top

# remove\_opacity

### No argumentsDescription:Remove opacity channel of selected images.

---

# Command: ryb2rgb
**Category:** Colors
**Source:** https://gmic.eu/reference/ryb2rgb.html#top

# ryb2rgb

### No argumentsDescription:Convert color representation of selected images from RYB to RGB.

---

# Command: select_color
**Category:** Colors
**Source:** https://gmic.eu/reference/select_color.html#top

# select\_color

## Arguments:

* tolerance[%]>=0,col1,...,colN

## Description:

Select pixels with specified color in selected images.  

This command has a [tutorial page](https://gmic.eu/oldtutorial/_select_color).

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +select\_color 40,204,153,110

  

[![](img/t0_select_color.jpg)](img/f0_select_color.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +select\_color 40,204,153,110**

[![](img/t1_select_color.jpg)](img/f1_select_color.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +select\_color 40,204,153,110**

---

# Command: sepia
**Category:** Colors
**Source:** https://gmic.eu/reference/sepia.html#top

# sepia

### No argumentsDescription:Apply sepia tones effect on selected images. Example of use: <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> sepia Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> sepia**

---

# Command: solarize
**Category:** Colors
**Source:** https://gmic.eu/reference/solarize.html#top

# solarize

### No argumentsDescription:Solarize selected images. Example of use: <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> solarize Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> solarize**

---

# Command: split_colors
**Category:** Colors
**Source:** https://gmic.eu/reference/split_colors.html#top

# split\_colors

## Arguments:

* \_tolerance>=0,\_max\_nb\_outputs>0,\_min\_area>0

## Description:

Split selected images as several image containing a single color.  
  
One selected image can be split as at most max\_nb\_outputs images.  
Output images are sorted by decreasing area of extracted color regions and have an additional alpha-channel.  

## Default values:

tolerance=0, max\_nb\_outputs=256 and min\_area=8.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> quantize 5 +split\_colors , display\_rgba

  

[![](img/t0_split_colors.jpg)](img/f0_split_colors.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> quantize 5 +split\_colors , display\_rgba**

[![](img/t1_split_colors.jpg)](img/f1_split_colors.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> quantize 5 +split\_colors , display\_rgba**

[![](img/t2_split_colors.jpg)](img/f2_split_colors.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> quantize 5 +split\_colors , display\_rgba**

[![](img/t3_split_colors.jpg)](img/f3_split_colors.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> quantize 5 +split\_colors , display\_rgba**

[![](img/t4_split_colors.jpg)](img/f4_split_colors.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> quantize 5 +split\_colors , display\_rgba**

[![](img/t5_split_colors.jpg)](img/f5_split_colors.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> quantize 5 +split\_colors , display\_rgba**

---

# Command: split_opacity
**Category:** Colors
**Source:** https://gmic.eu/reference/split_opacity.html#top

# split\_opacity

### No argumentsDescription:Split color and opacity parts of selected images. This command returns 1 or 2 images for each selected image, whether it has an opacity channel or not.

---

# Command: split_vector
**Category:** Colors
**Source:** https://gmic.eu/reference/split_vector.html#top

# split\_vector

## Arguments:

* keep\_splitting\_values={ +:Increasing | -:Decreasing },value1,\_value2,...

## Description:

Split selected images into multiple parts, where specified vector [value1,\_value2,...] is the separator.

---

# Command: srgb2lab
**Category:** Colors
**Source:** https://gmic.eu/reference/srgb2lab.html#top

# srgb2lab

## Arguments:

* illuminant={ 0:D50 | 1:D65 | 2:E }    or
* (no arg)

## Description:

Convert color representation of selected images from sRGB to Lab.  

## Default values:

illuminant=2.

## Examples of use:

### • Example #1

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> srgb2lab split c

  

[![](img/t0_srgb2lab.jpg)](img/f0_srgb2lab.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> srgb2lab split c**

[![](img/t1_srgb2lab.jpg)](img/f1_srgb2lab.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> srgb2lab split c**

[![](img/t2_srgb2lab.jpg)](img/f2_srgb2lab.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> srgb2lab split c**

### • Example #2

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> srgb2lab +split c mul[-2,-1] 2.5 append[-3--1] c lab2srgb

  

[![](img/t0_srgb2lab_2.jpg)](img/f0_srgb2lab_2.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> srgb2lab +split c mul[-2,-1] 2.5 append[-3--1] c lab2srgb**

[![](img/t1_srgb2lab_2.jpg)](img/f1_srgb2lab_2.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> srgb2lab +split c mul[-2,-1] 2.5 append[-3--1] c lab2srgb**

---

# Command: srgb2lab8
**Category:** Colors
**Source:** https://gmic.eu/reference/srgb2lab8.html#top

# srgb2lab8

## Arguments:

* illuminant={ 0:D50 | 1:D65 | 2:E }    or
* (no arg)

## Description:

Convert color representation of selected images from sRGB to Lab8.  

## Default values:

illuminant=2.

---

# Command: srgb2rgb
**Category:** Colors
**Source:** https://gmic.eu/reference/srgb2rgb.html#top

# srgb2rgb

### No argumentsDescription:Convert color representation of selected images from sRGB to linear RGB.

---

# Command: to_a
**Category:** Colors
**Source:** https://gmic.eu/reference/to_a.html#top

# to\_a

### No argumentsDescription:Force selected images to have an alpha channel.

---

# Command: to_color
**Category:** Colors
**Source:** https://gmic.eu/reference/to_color.html#top

# to\_color

### No argumentsDescription:Force selected images to be in color mode (RGB or RGBA).

---

# Command: to_colormode
**Category:** Colors
**Source:** https://gmic.eu/reference/to_colormode.html#top

# to\_colormode

## Arguments:

* mode={ 0:Adaptive | 1:G | 2:GA | 3:RGB | 4:RGBA }

## Description:

Force selected images to be in a given color mode.  

## Default values:

mode=0.

---

# Command: to_gray
**Category:** Colors
**Source:** https://gmic.eu/reference/to_gray.html#top

# to\_gray

### No argumentsDescription:Force selected images to be in GRAY mode. Example of use: <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +to\_gray Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +to\_gray** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +to\_gray**

---

# Command: to_graya
**Category:** Colors
**Source:** https://gmic.eu/reference/to_graya.html#top

# to\_graya

### No argumentsDescription:Force selected images to be in GRAYA mode.

---

# Command: to_pseudogray
**Category:** Colors
**Source:** https://gmic.eu/reference/to_pseudogray.html#top

# to\_pseudogray

## Arguments:

* \_max\_step>=0,\_is\_perceptual\_constraint={ 0:No | 1:Yes },\_bits\_depth>0

## Description:

Convert selected scalar images ([0-255]-valued) to pseudo-gray color images.  

## Default values:

max\_step=5, is\_perceptual\_constraint=1 and bits\_depth=8.

  
The original pseudo-gray technique has been introduced by Rich Franzen <http://r0k.us/graphics/pseudoGrey.html>.  
Extension of this technique to arbitrary increments for more tones, has been done by David Tschumperlé.

---

# Command: to_rgb
**Category:** Colors
**Source:** https://gmic.eu/reference/to_rgb.html#top

# to\_rgb

### No argumentsDescription:Force selected images to be in RGB mode.

---

# Command: to_rgba
**Category:** Colors
**Source:** https://gmic.eu/reference/to_rgba.html#top

# to\_rgba

### No argumentsDescription:Force selected images to be in RGBA mode.

---

# Command: to_automode
**Category:** Colors
**Source:** https://gmic.eu/reference/to_automode.html#top

# to\_automode

### No argumentsDescription:Force selected images to be in the most significant color mode. This commands checks for useless alpha channel (all values equal to 255), as well as detects grayscale images encoded as color images.

---

# Command: xyz2jzazbz
**Category:** Colors
**Source:** https://gmic.eu/reference/xyz2jzazbz.html#top

# xyz2jzazbz

### No argumentsDescription:Convert color representation of selected images from XYZ to RGB.

---

# Command: xyz2lab
**Category:** Colors
**Source:** https://gmic.eu/reference/xyz2lab.html#top

# xyz2lab

## Arguments:

* illuminant={ 0:D50 | 1:D65 | 2:E }    or
* (no arg)

## Description:

Convert color representation of selected images from XYZ to Lab.  

## Default values:

illuminant=2.

---

# Command: xyz2rgb
**Category:** Colors
**Source:** https://gmic.eu/reference/xyz2rgb.html#top

# xyz2rgb

## Arguments:

* illuminant={ 0:D50 | 1:D65 | 2:E }    or
* (no arg)

## Description:

Convert color representation of selected images from XYZ to RGB.  

## Default values:

illuminant=2.

---

# Command: xyz82rgb
**Category:** Colors
**Source:** https://gmic.eu/reference/xyz82rgb.html#top

# xyz82rgb

## Arguments:

* illuminant={ 0:D50 | 1:D65 | 2:E }    or
* (no arg)

## Description:

Convert color representation of selected images from XYZ8 to RGB.  

## Default values:

illuminant=2.

---

# Command: ycbcr2rgb
**Category:** Colors
**Source:** https://gmic.eu/reference/ycbcr2rgb.html#top

# ycbcr2rgb

### No argumentsDescription:Convert color representation of selected images from YCbCr to RGB.

---

# Command: yiq2rgb
**Category:** Colors
**Source:** https://gmic.eu/reference/yiq2rgb.html#top

# yiq2rgb

### No argumentsDescription:Convert color representation of selected images from YIQ to RGB.

---

# Command: yiq82rgb
**Category:** Colors
**Source:** https://gmic.eu/reference/yiq82rgb.html#top

# yiq82rgb

### No argumentsDescription:Convert color representation of selected images from YIQ8 to RGB.

---

# Command: yuv2rgb
**Category:** Colors
**Source:** https://gmic.eu/reference/yuv2rgb.html#top

# yuv2rgb

### No argumentsDescription:Convert color representation of selected images from YUV to RGB.

---

# Command: yuv82rgb
**Category:** Colors
**Source:** https://gmic.eu/reference/yuv82rgb.html#top

# yuv82rgb

### No argumentsDescription:Convert selected images from YUV8 to RGB color bases.

---

# Command: append
**Category:** Geometry Manipulation
**Source:** https://gmic.eu/reference/append.html#top

|  |  |
| --- | --- |
| append | Built-in command |

## Arguments:

* [image],axis,\_centering    or
* axis,\_centering

## Description:

Append specified image to selected images, or all selected images together, along specified axis.  

(*equivalent to shortcut command* a).

  
axis can be { x | y | z | c }.  
Usual centering values are { 0:left-justified | 0.5:centered | 1:right-justified }.  

## Default values:

centering=0.

## Examples of use:

### • Example #1

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> split y,10 reverse append y

  
[![](img/t_append.jpg)](img/f_append.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> split y,10 reverse append y**

### • Example #2

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> repeat 5 { +rows[0] 0,{10+18\*$>}% } remove[0] append x,0.5

  
[![](img/t_append_2.jpg)](img/f_append_2.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> repeat 5 { +rows[0] 0,{10+18\*$>}% } remove[0] append x,0.5**

### • Example #3

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> append[0] [0],y

  
[![](img/t_append_3.jpg)](img/f_append_3.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> append[0] [0],y**

---

# Command: append_tiles
**Category:** Geometry Manipulation
**Source:** https://gmic.eu/reference/append_tiles.html#top

# append\_tiles

## Arguments:

* \_M>=0,\_N>=0,0<=\_centering\_x<=1,0<=\_centering\_y<=1

## Description:

Append MxN selected tiles as new images.  
  
If N is set to 0, number of rows is estimated automatically.  
If M is set to 0, number of columns is estimated automatically.  
If M and N are both set to 0, auto-mode is used.  
If M or N is set to 0, only a single image is produced.  
centering\_x and centering\_y tells about the centering of tiles when they have different sizes.  

## Default values:

M=0, N=0, centering\_x=centering\_y=0.5.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> split xy,4 append\_tiles ,

  
[![](img/t_append_tiles.jpg)](img/f_append_tiles.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> split xy,4 append\_tiles ,**

---

# Command: apply_scales
**Category:** Geometry Manipulation
**Source:** https://gmic.eu/reference/apply_scales.html#top

# apply\_scales

## Arguments:

* "command",number\_of\_scales>0,\_min\_scale[%]>=0,\_max\_scale[%]>=0,\_scale\_gamma>0,\_interpolation

## Description:

Apply specified command on different scales of selected images.  
  
interpolation can be { 0:None | 1:Nearest | 2:Average | 3:Linear | 4:Grid | 5:Bicubic | 6:Lanczos }.  

## Default values:

min\_scale=25%, max\_scale=100% and interpolation=3.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> apply\_scales "blur 5 sharpen 1000",4

  

[![](img/t0_apply_scales.jpg)](img/f0_apply_scales.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> apply\_scales "blur 5 sharpen 1000",4**

[![](img/t1_apply_scales.jpg)](img/f1_apply_scales.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> apply\_scales "blur 5 sharpen 1000",4**

[![](img/t2_apply_scales.jpg)](img/f2_apply_scales.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> apply\_scales "blur 5 sharpen 1000",4**

[![](img/t3_apply_scales.jpg)](img/f3_apply_scales.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> apply\_scales "blur 5 sharpen 1000",4**

---

# Command: autocrop
**Category:** Geometry Manipulation
**Source:** https://gmic.eu/reference/autocrop.html#top

# autocrop

## Arguments:

* \_axes,\_value1,\_value2,...

## Description:

Autocrop selected images according to specified axes and values.  
  
axes can be { x | y | z | c | xy | xz | xc | yz | yc | zc | xyz | xyc | xzc | yzc | xyzc }.  
If no axes are provided, autocrop is assumed to be spatial only (e.g. axes=xyz).  
If no value arguments are provided, cropping value is automatically guessed.  

## Default values:

axes=xyz.

## See also:

[autocrop\_coords](autocrop_coords.html).

## Example of use:

400,400,1,3 fill\_color 64,128,255 ellipse 50%,50%,120,120,0,1,255 +autocrop

  

[![](img/t0_autocrop.jpg)](img/f0_autocrop.jpg)

Command: **400,400,1,3 fill\_color 64,128,255 ellipse 50%,50%,120,120,0,1,255 +autocrop**

[![](img/t1_autocrop.jpg)](img/f1_autocrop.jpg)

Command: **400,400,1,3 fill\_color 64,128,255 ellipse 50%,50%,120,120,0,1,255 +autocrop**

---

# Command: autocrop_components
**Category:** Geometry Manipulation
**Source:** https://gmic.eu/reference/autocrop_components.html#top

# autocrop\_components

## Arguments:

* \_threshold[%],\_min\_area[%]>=0,\_is\_high\_connectivity={ 0:No | 1:Yes },\_output\_type={ 0:Crop | 1:Segmentation | 2:Coordinates }

## Description:

Autocrop and extract connected components in selected images, according to a mask given as the last channel of  
  
each of the selected image (e.g. alpha-channel).  

## Default values:

threshold=0%, min\_area=0.1%, is\_high\_connectivity=0 and output\_type=1.

## Example of use:

256,256 noise 0.1,2 eq 1 dilate\_circ 20 label\_fg 0,1 normalize 0,255 +neq 0 \*[-1] 255 append c +autocrop\_components ,

  

[![](img/t0_autocrop_components.jpg)](img/f0_autocrop_components.jpg)

Command: **256,256 noise 0.1,2 eq 1 dilate\_circ 20 label\_fg 0,1 normalize 0,255 +neq 0 \*[-1] 255 append c +autocrop\_components ,**

[![](img/t1_autocrop_components.jpg)](img/f1_autocrop_components.jpg)

Command: **256,256 noise 0.1,2 eq 1 dilate\_circ 20 label\_fg 0,1 normalize 0,255 +neq 0 \*[-1] 255 append c +autocrop\_components ,**

[![](img/t2_autocrop_components.jpg)](img/f2_autocrop_components.jpg)

Command: **256,256 noise 0.1,2 eq 1 dilate\_circ 20 label\_fg 0,1 normalize 0,255 +neq 0 \*[-1] 255 append c +autocrop\_components ,**

[![](img/t3_autocrop_components.jpg)](img/f3_autocrop_components.jpg)

Command: **256,256 noise 0.1,2 eq 1 dilate\_circ 20 label\_fg 0,1 normalize 0,255 +neq 0 \*[-1] 255 append c +autocrop\_components ,**

[![](img/t4_autocrop_components.jpg)](img/f4_autocrop_components.jpg)

Command: **256,256 noise 0.1,2 eq 1 dilate\_circ 20 label\_fg 0,1 normalize 0,255 +neq 0 \*[-1] 255 append c +autocrop\_components ,**

[![](img/t5_autocrop_components.jpg)](img/f5_autocrop_components.jpg)

Command: **256,256 noise 0.1,2 eq 1 dilate\_circ 20 label\_fg 0,1 normalize 0,255 +neq 0 \*[-1] 255 append c +autocrop\_components ,**

[![](img/t6_autocrop_components.jpg)](img/f6_autocrop_components.jpg)

Command: **256,256 noise 0.1,2 eq 1 dilate\_circ 20 label\_fg 0,1 normalize 0,255 +neq 0 \*[-1] 255 append c +autocrop\_components ,**

[![](img/t7_autocrop_components.jpg)](img/f7_autocrop_components.jpg)

Command: **256,256 noise 0.1,2 eq 1 dilate\_circ 20 label\_fg 0,1 normalize 0,255 +neq 0 \*[-1] 255 append c +autocrop\_components ,**

[![](img/t8_autocrop_components.jpg)](img/f8_autocrop_components.jpg)

Command: **256,256 noise 0.1,2 eq 1 dilate\_circ 20 label\_fg 0,1 normalize 0,255 +neq 0 \*[-1] 255 append c +autocrop\_components ,**

[![](img/t9_autocrop_components.jpg)](img/f9_autocrop_components.jpg)

Command: **256,256 noise 0.1,2 eq 1 dilate\_circ 20 label\_fg 0,1 normalize 0,255 +neq 0 \*[-1] 255 append c +autocrop\_components ,**

[![](img/t10_autocrop_components.jpg)](img/f10_autocrop_components.jpg)

Command: **256,256 noise 0.1,2 eq 1 dilate\_circ 20 label\_fg 0,1 normalize 0,255 +neq 0 \*[-1] 255 append c +autocrop\_components ,**

[![](img/t11_autocrop_components.jpg)](img/f11_autocrop_components.jpg)

Command: **256,256 noise 0.1,2 eq 1 dilate\_circ 20 label\_fg 0,1 normalize 0,255 +neq 0 \*[-1] 255 append c +autocrop\_components ,**

[![](img/t12_autocrop_components.jpg)](img/f12_autocrop_components.jpg)

Command: **256,256 noise 0.1,2 eq 1 dilate\_circ 20 label\_fg 0,1 normalize 0,255 +neq 0 \*[-1] 255 append c +autocrop\_components ,**

[![](img/t13_autocrop_components.jpg)](img/f13_autocrop_components.jpg)

Command: **256,256 noise 0.1,2 eq 1 dilate\_circ 20 label\_fg 0,1 normalize 0,255 +neq 0 \*[-1] 255 append c +autocrop\_components ,**

[![](img/t14_autocrop_components.jpg)](img/f14_autocrop_components.jpg)

Command: **256,256 noise 0.1,2 eq 1 dilate\_circ 20 label\_fg 0,1 normalize 0,255 +neq 0 \*[-1] 255 append c +autocrop\_components ,**

[![](img/t15_autocrop_components.jpg)](img/f15_autocrop_components.jpg)

Command: **256,256 noise 0.1,2 eq 1 dilate\_circ 20 label\_fg 0,1 normalize 0,255 +neq 0 \*[-1] 255 append c +autocrop\_components ,**

[![](img/t16_autocrop_components.jpg)](img/f16_autocrop_components.jpg)

Command: **256,256 noise 0.1,2 eq 1 dilate\_circ 20 label\_fg 0,1 normalize 0,255 +neq 0 \*[-1] 255 append c +autocrop\_components ,**

---

# Command: autocrop_coords
**Category:** Geometry Manipulation
**Source:** https://gmic.eu/reference/autocrop_coords.html#top

# autocrop\_coords

## Arguments:

* \_axes,\_value1,\_value2,...

## Description:

Return coordinates of the bounding box that would be used to autocrop selected images, according to specified axes and values.  
  
axes can be { x | y | z | c | xy | xz | xc | yz | yc | zc | xyz | xyc | xzc | yzc | xyzc }.  
If no axes are provided, autocrop is assumed to be spatial only (e.g. axes=xyz).  
If no value arguments are provided, cropping value is automatically guessed.  
If input image is constant and equal to the crop value, -1 is returned for all output coordinates.  

## Default values:

axes=xyz.

## See also:

[autocrop](autocrop.html).

---

# Command: autocrop_seq
**Category:** Geometry Manipulation
**Source:** https://gmic.eu/reference/autocrop_seq.html#top

# autocrop\_seq

## Arguments:

* value1,value2,... | auto

## Description:

Autocrop selected images using the crop geometry of the last one by specified vector-valued intensity,  
  
or by automatic guessing the cropping value.  

## Default values:

auto mode.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +fill[-1] 0 ellipse[-1] 50%,50%,30%,20%,0,1,1 autocrop\_seq 0

  

[![](img/t0_autocrop_seq.jpg)](img/f0_autocrop_seq.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +fill[-1] 0 ellipse[-1] 50%,50%,30%,20%,0,1,1 autocrop\_seq 0**

[![](img/t1_autocrop_seq.jpg)](img/f1_autocrop_seq.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +fill[-1] 0 ellipse[-1] 50%,50%,30%,20%,0,1,1 autocrop\_seq 0**

---

# Command: channels
**Category:** Geometry Manipulation
**Source:** https://gmic.eu/reference/channels.html#top

# channels

## Arguments:

* c0[%],\_c1[%],\_boundary\_conditions

## Description:

Keep only specified channels of selected images.  
  
boundary\_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.  

## Default values:

c1=c0 and boundary\_conditions=0.

## Examples of use:

### • Example #1

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> channels 1

  
[![](img/t_channels.jpg)](img/f_channels.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> channels 1**

### • Example #2

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> luminance channels 0,2

  
[![](img/t_channels_2.jpg)](img/f_channels_2.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> luminance channels 0,2**

---

# Command: columns
**Category:** Geometry Manipulation
**Source:** https://gmic.eu/reference/columns.html#top

# columns

## Arguments:

* x0[%],\_x1[%],\_boundary\_conditions

## Description:

Keep only specified columns of selected images.  
  
boundary\_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.  

## Default values:

x1=x0 and boundary\_conditions=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> columns -25%,50%

  
[![](img/t_columns.jpg)](img/f_columns.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> columns -25%,50%**

---

# Command: crop
**Category:** Geometry Manipulation
**Source:** https://gmic.eu/reference/crop.html#top

|  |  |
| --- | --- |
| crop | Built-in command |

## Arguments:

* x0[%],x1[%],\_boundary\_conditions    or
* x0[%],y0[%],x1[%],y1[%],\_boundary\_conditions    or
* x0[%],y0[%],z0[%],x1[%],y1[%],z1[%],\_boundary\_conditions    or
* x0[%],y0[%],z0[%],c0[%],x1[%],y1[%],z1[%],c1[%],\_boundary\_conditions

## Description:

Crop selected images with specified region coordinates.  

(*equivalent to shortcut command* z).

  
boundary\_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.  

## Default values:

boundary\_conditions=0.

## Examples of use:

### • Example #1

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +crop -230,-230,280,280,1 crop[0] -230,-230,280,280,0

  

[![](img/t0_crop.jpg)](img/f0_crop.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +crop -230,-230,280,280,1 crop[0] -230,-230,280,280,0**

[![](img/t1_crop.jpg)](img/f1_crop.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +crop -230,-230,280,280,1 crop[0] -230,-230,280,280,0**

### • Example #2

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> crop 25%,25%,75%,75%

  
[![](img/t_crop_2.jpg)](img/f_crop_2.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> crop 25%,25%,75%,75%**

---

# Command: elevate
**Category:** Geometry Manipulation
**Source:** https://gmic.eu/reference/elevate.html#top

# elevate

## Arguments:

* \_depth,\_is\_plain={ 0:No | 1:Yes },\_is\_colored={ 0:No | 1:Yes }

## Description:

Elevate selected 2D images into 3D volumes.  

## Default values:

depth=64, is\_plain=1 and is\_colored=1.

## Example of use:

sample colorful,64 +elevate 32

  

[![](img/t0_elevate.jpg)](img/f0_elevate.jpg)

Command: **sample colorful,64 +elevate 32**

[![](img/t1_elevate.jpg)](img/f1_elevate.jpg)

Command: **sample colorful,64 +elevate 32**

---

# Command: expand
**Category:** Geometry Manipulation
**Source:** https://gmic.eu/reference/expand.html#top

# expand

## Arguments:

* axes,size[%],\_boundary\_conditions={ 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }

## Description:

Expand selected images along the specified axes.  
  
axes can be { x | y | z | c | xy | xz | xc | yz | yc | zc | xyz | xyc | xzc | yzc | xyzc }.  

## Default values:

boundary\_conditions=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> expand xy,30

  
[![](img/t_expand.jpg)](img/f_expand.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> expand xy,30**

---

# Command: extract
**Category:** Geometry Manipulation
**Source:** https://gmic.eu/reference/extract.html#top

# extract

## Arguments:

* "condition",\_output\_type={ 0:XYZC-coords | 1:XYZ-coords | 2:Scalar-values | 3:Vector-values | 4:XYZC-coords + scalar value | 5:XYZ-coords + vector-values }

## Description:

Extract a list of coordinates or values from selected image, where  
  
specified mathematical condition holds.  
For N coordinates matching, result is a 1xNx1x4 image.  

## Default values:

output\_type=0.

## Example of use:

sp lena +extract "norm(I)>128",3

  

[![](img/t0_extract.jpg)](img/f0_extract.jpg)

Command: **sp lena +extract "norm(I)>128",3**

[![](img/t1_extract.jpg)](img/f1_extract.jpg)

Command: **sp lena +extract "norm(I)>128",3**

---

# Command: extract_region
**Category:** Geometry Manipulation
**Source:** https://gmic.eu/reference/extract_region.html#top

# extract\_region

## Arguments:

* [label\_image],\_extract\_xyz\_coordinates={ 0:No | 1:Yes },\_label\_1,...,\_label\_M

## Description:

Extract all pixels of selected images whose corresponding label in [label\_image] is equal to label\_m,  
  
and output them as M column images.  

## Default values:

extract\_xyz\_coordinates=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +blur 3 quantize. 4,0 +extract\_region[0] [1],0,1,3

  

[![](img/t0_extract_region.jpg)](img/f0_extract_region.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +blur 3 quantize. 4,0 +extract\_region[0] [1],0,1,3**

[![](img/t1_extract_region.jpg)](img/f1_extract_region.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +blur 3 quantize. 4,0 +extract\_region[0] [1],0,1,3**

[![](img/t2_extract_region.jpg)](img/f2_extract_region.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +blur 3 quantize. 4,0 +extract\_region[0] [1],0,1,3**

[![](img/t3_extract_region.jpg)](img/f3_extract_region.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +blur 3 quantize. 4,0 +extract\_region[0] [1],0,1,3**

---

# Command: montage
**Category:** Geometry Manipulation
**Source:** https://gmic.eu/reference/montage.html#top

# montage

## Arguments:

* "\_layout\_code",\_montage\_mode={ 0<=centering<=1 | 2<=scale+2<=3 },\_output\_mode={ 0:Single layer | 1:Multiple layers },"\_processing\_command"

## Description:

Create a single image montage from selected images, according to specified layout code :  

X to assemble all images using an automatically estimated layout.

H to assemble all images horizontally.

V to assemble all images vertically.

A to assemble all images as an horizontal array.

B to assemble all images as a vertical array.

Ha:b to assemble two blocks a and b horizontally.

Va:b to assemble two blocks a and b vertically.

Ra to rotate a block a by 90 deg. (RRa for 180 deg. and RRRa for 270 deg.).

Ma to mirror a block a along the X-axis (MRRa for the Y-axis).

A block a can be an image index (treated periodically) or a nested layout expression Hb:c,Vb:c,Rb or  
Mb itself.  
For example, layout code H0:V1:2 creates an image where image [0] is on the left, and images [1] and [2]  
vertically packed on the right.  

## Default values:

layout\_code=X, montage\_mode=2, output\_mode='0' and processing\_command="".

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> sample ? +plasma[0] 1 shape\_cupid 256 normalize 0,255 frame xy,3,0 frame xy,10,255 to\_rgb +montage A +montage[^-1] H1:V0:VH2:1H0:3

  

[![](img/t0_montage.jpg)](img/f0_montage.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> sample ? +plasma[0] 1 shape\_cupid 256 normalize 0,255 frame xy,3,0 frame xy,10,255 to\_rgb +montage A +montage[^-1] H1:V0:VH2:1H0:3**

[![](img/t1_montage.jpg)](img/f1_montage.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> sample ? +plasma[0] 1 shape\_cupid 256 normalize 0,255 frame xy,3,0 frame xy,10,255 to\_rgb +montage A +montage[^-1] H1:V0:VH2:1H0:3**

[![](img/t2_montage.jpg)](img/f2_montage.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> sample ? +plasma[0] 1 shape\_cupid 256 normalize 0,255 frame xy,3,0 frame xy,10,255 to\_rgb +montage A +montage[^-1] H1:V0:VH2:1H0:3**

[![](img/t3_montage.jpg)](img/f3_montage.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> sample ? +plasma[0] 1 shape\_cupid 256 normalize 0,255 frame xy,3,0 frame xy,10,255 to\_rgb +montage A +montage[^-1] H1:V0:VH2:1H0:3**

[![](img/t4_montage.jpg)](img/f4_montage.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> sample ? +plasma[0] 1 shape\_cupid 256 normalize 0,255 frame xy,3,0 frame xy,10,255 to\_rgb +montage A +montage[^-1] H1:V0:VH2:1H0:3**

[![](img/t5_montage.jpg)](img/f5_montage.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> sample ? +plasma[0] 1 shape\_cupid 256 normalize 0,255 frame xy,3,0 frame xy,10,255 to\_rgb +montage A +montage[^-1] H1:V0:VH2:1H0:3**

---

# Command: mirror
**Category:** Geometry Manipulation
**Source:** https://gmic.eu/reference/mirror.html#top

|  |  |
| --- | --- |
| mirror | Built-in command |

## Arguments:

* { x | y | z }...{ x | y | z }

## Description:

Mirror selected images along specified axes.  

## Examples of use:

### • Example #1

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +mirror y +mirror[0] c

  

[![](img/t0_mirror.jpg)](img/f0_mirror.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +mirror y +mirror[0] c**

[![](img/t1_mirror.jpg)](img/f1_mirror.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +mirror y +mirror[0] c**

[![](img/t2_mirror.jpg)](img/f2_mirror.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +mirror y +mirror[0] c**

### • Example #2

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +mirror x +mirror y append\_tiles 2,2

  
[![](img/t_mirror_2.jpg)](img/f_mirror_2.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +mirror x +mirror y append\_tiles 2,2**

---

# Command: permute
**Category:** Geometry Manipulation
**Source:** https://gmic.eu/reference/permute.html#top

|  |  |
| --- | --- |
| permute | Built-in command |

## Arguments:

* permutation\_string

## Description:

Permute selected image axes by specified permutation.  
  
permutation is a combination of the character set {x|y|z|c},  
e.g. xycz, cxyz, ...  

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> permute yxzc

  
[![](img/t_permute.jpg)](img/f_permute.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> permute yxzc**

---

# Command: rescale2d
**Category:** Geometry Manipulation
**Source:** https://gmic.eu/reference/rescale2d.html#top

# rescale2d

## Arguments:

* \_width[%]={ 0:Any | >0 },\_height[%]={ 0:Any | >0 },-1=<\_interpolation<=6,\_mode={ 0:Inside | 1:Padded-inside | 2:Outside | 3:Cropped-outside }

## Description:

Resize selected 2D images while preserving aspect ratio.  
  
interpolation can be { -1:Status only | 0:None | 1:Nearest | 2:Average | 3:Linear | 4=Grid | 5=Bicubic | 6=Lanczos }.  
When interpolation==-1, image size is actually not modified, but the size that would have been used for the last selected image is returned in the status value.  
Each resized image size is computed according to the specified mode:  

If mode==0, image size is at most (width,height).

If mode==1 or mode==3, image size is exactly (width,height).

If mode==2, image size is at least (width,height).

(*equivalent to shortcut command* rs).

## Default values:

width=height=0, interpolation=2 and mode=0.

---

# Command: rescale3d
**Category:** Geometry Manipulation
**Source:** https://gmic.eu/reference/rescale3d.html#top

# rescale3d

## Arguments:

* \_width[%]={ 0:Any | >0 },\_height[%]={ 0:Any | >0 },\_depth[%]={ 0:Any | >0 },-1=<\_interpolation<=6,\_mode={ 0:Inside | 1:Padded-inside | 2:Outside | 3    or
* Cropped-outside }

## Description:

Resize selected 3D images while preserving aspect ratio.  
  
interpolation can be { -1:Status only | 0:None | 1:Nearest | 2:Average | 3:Linear | 4=Grid | 5=Bicubic | 6=Lanczos }.  
When interpolation==-1, image size is actually not modified, but the size that would have been used for the last selected image is returned in the status value.  
Each resized image size is computed according to the specified mode:  

If mode==0, image size is at most (width,height).

If mode==1 or mode==3, image size is exactly (width,height).

If mode==2, image size is at least (width,height).

(*equivalent to shortcut command* rs3d).

## Default values:

width=height=depth=0, interpolation=2 and mode=0.

---

# Command: resize
**Category:** Geometry Manipulation
**Source:** https://gmic.eu/reference/resize.html#top

|  |  |
| --- | --- |
| resize | Built-in command |

## Arguments:

* {[image\_w] | width[%]>0},\_{[image\_h] | height[%]>0},\_{[image\_d] | depth[%]>0},\_{[image\_s] | spectrum[%]>0},\_interpolation,\_boundary\_conditions,\_ax,\_ay,\_az,\_ac

## Description:

Resize selected images with specified geometry.  

(*equivalent to shortcut command* r).

  
interpolation can be { -1:None (memory content) | 0:None | 1:Nearest | 2:Average | 3:Linear | 4=Grid | 5=Bicubic | 6=Lanczos }.  
boundary\_conditions has different meanings, according to the chosen interpolation mode :  
. When 'interpolation=={ -1 | 1 | 2 | 4 }', boundary\_conditions is meaningless.  
. When interpolation==0, boundary\_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.  
. When 'interpolation=={ 3 | 5 | 6 }', boundary\_conditions can be { 0:None | 1:Neumann }.  
ax,ay,az,ac set the centering along each axis when interpolation=0 or 4  
(set to 0 by default, must be defined in range [0,1]).  

## Default values:

interpolation=1, boundary\_conditions=0 and ax=ay=az=ac=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +resize[-1] 256,128,1,3,2 +resize[-1] 120%,120%,1,3,0,1,0.5,0.5 +resize[-1] 120%,120%,1,3,0,0,0.2,0.2 +resize[-1] [0],[0],1,3,4

  

[![](img/t0_resize.jpg)](img/f0_resize.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +resize[-1] 256,128,1,3,2 +resize[-1] 120%,120%,1,3,0,1,0.5,0.5 +resize[-1] 120%,120%,1,3,0,0,0.2,0.2 +resize[-1] [0],[0],1,3,4**

[![](img/t1_resize.jpg)](img/f1_resize.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +resize[-1] 256,128,1,3,2 +resize[-1] 120%,120%,1,3,0,1,0.5,0.5 +resize[-1] 120%,120%,1,3,0,0,0.2,0.2 +resize[-1] [0],[0],1,3,4**

[![](img/t2_resize.jpg)](img/f2_resize.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +resize[-1] 256,128,1,3,2 +resize[-1] 120%,120%,1,3,0,1,0.5,0.5 +resize[-1] 120%,120%,1,3,0,0,0.2,0.2 +resize[-1] [0],[0],1,3,4**

[![](img/t3_resize.jpg)](img/f3_resize.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +resize[-1] 256,128,1,3,2 +resize[-1] 120%,120%,1,3,0,1,0.5,0.5 +resize[-1] 120%,120%,1,3,0,0,0.2,0.2 +resize[-1] [0],[0],1,3,4**

[![](img/t4_resize.jpg)](img/f4_resize.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +resize[-1] 256,128,1,3,2 +resize[-1] 120%,120%,1,3,0,1,0.5,0.5 +resize[-1] 120%,120%,1,3,0,0,0.2,0.2 +resize[-1] [0],[0],1,3,4**

---

# Command: resize_as_image
**Category:** Geometry Manipulation
**Source:** https://gmic.eu/reference/resize_as_image.html#top

# resize\_as\_image

## Arguments:

* [reference],\_interpolation,\_boundary\_conditions,\_ax,\_ay,\_az,\_ac

## Description:

Resize selected images to the geometry of specified [reference] image.  

(*equivalent to shortcut command* ri).

## Default values:

interpolation=1, boundary\_conditions=0 and ax=ay=az=ac=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> sample duck +resize\_as\_image[-1] [-2]

  

[![](img/t0_resize_as_image.jpg)](img/f0_resize_as_image.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> sample duck +resize\_as\_image[-1] [-2]**

[![](img/t1_resize_as_image.jpg)](img/f1_resize_as_image.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> sample duck +resize\_as\_image[-1] [-2]**

[![](img/t2_resize_as_image.jpg)](img/f2_resize_as_image.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> sample duck +resize\_as\_image[-1] [-2]**

---

# Command: resize_displacement
**Category:** Geometry Manipulation
**Source:** https://gmic.eu/reference/resize_displacement.html#top

# resize\_displacement

## Arguments:

* width[%]>0,\_height[%]>0,\_depth[%]>0

## Description:

Resize selected displacement fields with specified geometry.  
  
During the process, the displacement vectors are also scaled by the corresponding ratios along each axis.  

## Default values:

height=100% and depth=100%.

---

# Command: resize_mn
**Category:** Geometry Manipulation
**Source:** https://gmic.eu/reference/resize_mn.html#top

# resize\_mn

## Arguments:

* width[%]>=0,\_height[%]>=0,\_depth[%]>=0,\_B\_value,\_C\_value

## Description:

Resize selected images with Mitchell-Netravali filter (cubic).  
  
For details about the method, see: <https://de.wikipedia.org/wiki/Mitchell-Netravali-Filter>.  

## Default values:

height=100%, depth=100%, B=0.3333 and C=0.3333.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rescale2d 32 resize\_mn 800%,800%

  
[![](img/t_resize_mn.jpg)](img/f_resize_mn.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rescale2d 32 resize\_mn 800%,800%**

---

# Command: resize_pow2
**Category:** Geometry Manipulation
**Source:** https://gmic.eu/reference/resize_pow2.html#top

# resize\_pow2

## Arguments:

* \_interpolation,\_boundary\_conditions,\_ax,\_ay,\_az,\_ac

## Description:

Resize selected images so that each dimension is a power of 2.  
  
interpolation can be { -1:None (memory content) | 0:None | 1:Nearest | 2:Average | 3:Linear | 4:Grid | 5:Bicubic | 6:Lanczos }.  
boundary\_conditions has different meanings, according to the chosen interpolation mode :  
. When 'interpolation=={ -1 | 1 | 2 | 4 }', boundary\_conditions is meaningless.  
. When interpolation==0, boundary\_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.  
. When 'interpolation=={ 3 | 5 | 6 }', boundary\_conditions can be { 0:None | 1:Neumann }.  
ax,ay,az,ac set the centering along each axis when interpolation=0  
(set to 0 by default, must be defined in range [0,1]).  

## Default values:

interpolation=0, boundary\_conditions=0 and ax=ay=az=ac=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +resize\_pow2[-1] 0

  

[![](img/t0_resize_pow2.jpg)](img/f0_resize_pow2.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +resize\_pow2[-1] 0**

[![](img/t1_resize_pow2.jpg)](img/f1_resize_pow2.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +resize\_pow2[-1] 0**

---

# Command: rotate
**Category:** Geometry Manipulation
**Source:** https://gmic.eu/reference/rotate.html#top

|  |  |
| --- | --- |
| rotate | Built-in command |

## Arguments:

* angle,\_interpolation,\_boundary\_conditions,\_center\_x[%],\_center\_y[%]    or
* u,v,w,angle,interpolation,boundary\_conditions,\_center\_x[%],\_center\_y[%],\_center\_z[%]

## Description:

Rotate selected images with specified angle (in deg.), and optionally 3D axis (u,v,w).  
  
interpolation can be { 0:None | 1:Linear | 2:Bicubic }.  
boundary\_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.  
When a rotation center (cx,cy,\_cz) is specified, the size of the image is preserved.  

## Default values:

interpolation=1, boundary\_conditions=0 and center\_x=center\_y=(undefined).

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +rotate -25,1,2,50%,50% rotate[0] 25

  

[![](img/t0_rotate.jpg)](img/f0_rotate.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +rotate -25,1,2,50%,50% rotate[0] 25**

[![](img/t1_rotate.jpg)](img/f1_rotate.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +rotate -25,1,2,50%,50% rotate[0] 25**

---

# Command: rotate_tileable
**Category:** Geometry Manipulation
**Source:** https://gmic.eu/reference/rotate_tileable.html#top

# rotate\_tileable

## Arguments:

* angle,\_max\_size\_factor>=0

## Description:

Rotate selected images by specified angle and make them tileable.  
  
If resulting size of an image is too big, the image is replaced by a 1x1 image.  

## Default values:

max\_size\_factor=8.

## Example of use:

sample colorful,128 +rotate\_tileable 16

  

[![](img/t0_rotate_tileable.jpg)](img/f0_rotate_tileable.jpg)

Command: **sample colorful,128 +rotate\_tileable 16**

[![](img/t1_rotate_tileable.jpg)](img/f1_rotate_tileable.jpg)

Command: **sample colorful,128 +rotate\_tileable 16**

---

# Command: rows
**Category:** Geometry Manipulation
**Source:** https://gmic.eu/reference/rows.html#top

# rows

## Arguments:

* y0[%],\_y1[%],\_boundary\_conditions

## Description:

Keep only specified rows of selected images.  
  
boundary\_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.  

## Default values:

y1=y0 and boundary\_conditions=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rows -25%,50%

  
[![](img/t_rows.jpg)](img/f_rows.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rows -25%,50%**

---

# Command: scale2x
**Category:** Geometry Manipulation
**Source:** https://gmic.eu/reference/scale2x.html#top

# scale2x

### No argumentsDescription:Double XY-size of selected images, using the Scale2x algorithm. Example of use: <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> threshold 50% resize 50%,50% +scale2x Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> threshold 50% resize 50%,50% +scale2x** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> threshold 50% resize 50%,50% +scale2x**

---

# Command: scale2x_cnn
**Category:** Geometry Manipulation
**Source:** https://gmic.eu/reference/scale2x_cnn.html#top

# scale2x\_cnn

## Arguments:

* \_sharpness>=0

## Description:

Double XY-size of selected images, using a convolutional neural network.  

## Default values:

sharpness=1.25.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rescale2d 128 +scale2x\_cnn ,

  

[![](img/t0_scale2x_cnn.jpg)](img/f0_scale2x_cnn.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rescale2d 128 +scale2x\_cnn ,**

[![](img/t1_scale2x_cnn.jpg)](img/f1_scale2x_cnn.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rescale2d 128 +scale2x\_cnn ,**

---

# Command: scale3x
**Category:** Geometry Manipulation
**Source:** https://gmic.eu/reference/scale3x.html#top

# scale3x

### No argumentsDescription:Triple XY-size of selected images, using the Scale3x algorithm. Example of use: <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> threshold 50% resize 33%,33% +scale3x Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> threshold 50% resize 33%,33% +scale3x** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> threshold 50% resize 33%,33% +scale3x**

---

# Command: scale_dcci2x
**Category:** Geometry Manipulation
**Source:** https://gmic.eu/reference/scale_dcci2x.html#top

# scale\_dcci2x

## Arguments:

* \_edge\_threshold>=0,\_exponent>0,\_extend\_1px={ 0:No | 1:Yes }

## Description:

Double XY-size of selected images, using a directional cubic convolution interpolation,  
  
as described in <https://en.wikipedia.org/wiki/Directional_Cubic_Convolution_Interpolation>.  

## Default values:

edge\_threshold=1.15, exponent=5 and extend\_1px=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rescale2d 128 +scale\_dcci2x ,

  

[![](img/t0_scale_dcci2x.jpg)](img/f0_scale_dcci2x.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rescale2d 128 +scale\_dcci2x ,**

[![](img/t1_scale_dcci2x.jpg)](img/f1_scale_dcci2x.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rescale2d 128 +scale\_dcci2x ,**

---

# Command: seamcarve
**Category:** Geometry Manipulation
**Source:** https://gmic.eu/reference/seamcarve.html#top

# seamcarve

## Arguments:

* \_width[%]>=0,\_height[%]>=0,\_is\_priority\_channel={ 0:No | 1:Yes },\_is\_antialiasing={ 0:No | 1:Yes },\_maximum\_seams[%]>=0

## Description:

Resize selected images with specified 2D geometry, using the seam-carving algorithm.  

## Default values:

height=100%, is\_priority\_channel=0, is\_antialiasing=1 and maximum\_seams=25%.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> seamcarve 60%

  
[![](img/t_seamcarve.jpg)](img/f_seamcarve.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> seamcarve 60%**

---

# Command: shift
**Category:** Geometry Manipulation
**Source:** https://gmic.eu/reference/shift.html#top

|  |  |
| --- | --- |
| shift | Built-in command |

## Arguments:

* vx[%],\_vy[%],\_vz[%],\_vc[%],\_boundary\_conditions,\_interpolation={ 0:Nearest\_neighbor | 1:Linear }

## Description:

Shift selected images by specified displacement vector.  
  
Displacement vector can be non-integer in which case linear interpolation should be chosen.  
boundary\_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.  

## Default values:

boundary\_conditions=0 and interpolation=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +shift[0] 50%,50%,0,0,0 +shift[0] 50%,50%,0,0,1 +shift[0] 50%,50%,0,0,2

  

[![](img/t0_shift.jpg)](img/f0_shift.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +shift[0] 50%,50%,0,0,0 +shift[0] 50%,50%,0,0,1 +shift[0] 50%,50%,0,0,2**

[![](img/t1_shift.jpg)](img/f1_shift.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +shift[0] 50%,50%,0,0,0 +shift[0] 50%,50%,0,0,1 +shift[0] 50%,50%,0,0,2**

[![](img/t2_shift.jpg)](img/f2_shift.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +shift[0] 50%,50%,0,0,0 +shift[0] 50%,50%,0,0,1 +shift[0] 50%,50%,0,0,2**

[![](img/t3_shift.jpg)](img/f3_shift.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +shift[0] 50%,50%,0,0,0 +shift[0] 50%,50%,0,0,1 +shift[0] 50%,50%,0,0,2**

---

# Command: shrink
**Category:** Geometry Manipulation
**Source:** https://gmic.eu/reference/shrink.html#top

# shrink

## Arguments:

* axes,size[%],\_boundary\_conditions={ 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }

## Description:

Shrink selected images along the specified axes.  
  
axes can be { x | y | z | c | xy | xz | xc | yz | yc | zc | xyz | xyc | xzc | yzc | xyzc }.  

## Default values:

boundary\_conditions=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> shrink xy,100

  
[![](img/t_shrink.jpg)](img/f_shrink.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> shrink xy,100**

---

# Command: slices
**Category:** Geometry Manipulation
**Source:** https://gmic.eu/reference/slices.html#top

# slices

## Arguments:

* z0[%],\_z1[%],\_boundary\_conditions

## Description:

Keep only specified slices of selected images.  
  
boundary\_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.  

## Default values:

z1=z0 and boundary\_conditions=0.

---

# Command: sort
**Category:** Geometry Manipulation
**Source:** https://gmic.eu/reference/sort.html#top

|  |  |
| --- | --- |
| sort | Built-in command |

## Arguments:

* \_ordering={ +:Increasing | -:Decreasing },\_axis={ x | y | z | c }

## Description:

Sort pixel values of selected images.  
  
If axis is specified, the sorting is done according to the data of the first column/row/slice/channel  
of selected images.  

## Default values:

ordering=+ and axis=(undefined).

## Example of use:

64 rand 0,100 +sort display\_graph 400,300,3

  

[![](img/t0_sort.jpg)](img/f0_sort.jpg)

Command: **64 rand 0,100 +sort display\_graph 400,300,3**

[![](img/t1_sort.jpg)](img/f1_sort.jpg)

Command: **64 rand 0,100 +sort display\_graph 400,300,3**

---

# Command: split
**Category:** Geometry Manipulation
**Source:** https://gmic.eu/reference/split.html#top

|  |  |
| --- | --- |
| split | Built-in command |

## Arguments:

* { x | y | z | c }...{ x | y | z | c },\_split\_mode[%],\_max\_parts>0    or
* keep\_splitting\_values={ +:Increasing | -:Decreasing },\_{ x | y | z | c }...{ x | y | z | c },value1,\_value2,...    or
* (no arg)

## Description:

Split selected images along specified axes, or regarding to a sequence of scalar values  
  
(optionally along specified axes).  

(*equivalent to shortcut command* s).

Argument split\_mode determines how the split is done. It can be :  

0: Split image according to consecutive constant values;

N (where N is a positive integer): Split image into N homogeneous parts;

-N[%] (where N is a positive integer): Split image as blocks of size N(opt. specified as a percentage of the image dimension).

When specified, max\_parts defines a limit in the number of resulting images.  

## Default values:

N=-1.

## Examples of use:

### • Example #1

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> split c

  

[![](img/t0_split.jpg)](img/f0_split.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> split c**

[![](img/t1_split.jpg)](img/f1_split.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> split c**

[![](img/t2_split.jpg)](img/f2_split.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> split c**

### • Example #2

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> split y,3

  

[![](img/t0_split_2.jpg)](img/f0_split_2.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> split y,3**

[![](img/t1_split_2.jpg)](img/f1_split_2.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> split y,3**

[![](img/t2_split_2.jpg)](img/f2_split_2.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> split y,3**

### • Example #3

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> split x,-128

  

[![](img/t0_split_3.jpg)](img/f0_split_3.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> split x,-128**

[![](img/t1_split_3.jpg)](img/f1_split_3.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> split x,-128**

[![](img/t2_split_3.jpg)](img/f2_split_3.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> split x,-128**

[![](img/t3_split_3.jpg)](img/f3_split_3.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> split x,-128**

[![](img/t4_split_3.jpg)](img/f4_split_3.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> split x,-128**

### • Example #4

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> split x,-30%,2

  

[![](img/t0_split_4.jpg)](img/f0_split_4.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> split x,-30%,2**

[![](img/t1_split_4.jpg)](img/f1_split_4.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> split x,-30%,2**

### • Example #5

1,20,1,1,"1,2,3,4" +split -,2,3 append[1--1] y

  

[![](img/t0_split_5.jpg)](img/f0_split_5.jpg)

Command: **1,20,1,1,"1,2,3,4" +split -,2,3 append[1--1] y**

[![](img/t1_split_5.jpg)](img/f1_split_5.jpg)

Command: **1,20,1,1,"1,2,3,4" +split -,2,3 append[1--1] y**

### • Example #6

(1,2,2,3,3,3,4,4,4,4) +split x,0 append[1--1] y

  

[![](img/t0_split_6.jpg)](img/f0_split_6.jpg)

Command: **(1,2,2,3,3,3,4,4,4,4) +split x,0 append[1--1] y**

[![](img/t1_split_6.jpg)](img/f1_split_6.jpg)

Command: **(1,2,2,3,3,3,4,4,4,4) +split x,0 append[1--1] y**

---

# Command: split_tiles
**Category:** Geometry Manipulation
**Source:** https://gmic.eu/reference/split_tiles.html#top

# split\_tiles

## Arguments:

* M!=0,\_N!=0,\_is\_homogeneous={ 0:No | 1:Yes }

## Description:

Split selected images as a MxN array of tiles.  
  
If M or N is negative, it stands for the tile size instead.  

## Default values:

N=M and is\_homogeneous=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +local split\_tiles 5,4 blur 3,0 sharpen 700 append\_tiles 4,5 done

  

[![](img/t0_split_tiles.jpg)](img/f0_split_tiles.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +local split\_tiles 5,4 blur 3,0 sharpen 700 append\_tiles 4,5 done**

[![](img/t1_split_tiles.jpg)](img/f1_split_tiles.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +local split\_tiles 5,4 blur 3,0 sharpen 700 append\_tiles 4,5 done**

---

# Command: undistort
**Category:** Geometry Manipulation
**Source:** https://gmic.eu/reference/undistort.html#top

# undistort

## Arguments:

* -1<=\_amplitude<=1,\_aspect\_ratio,\_zoom,\_center\_x[%],\_center\_y[%],\_boundary\_conditions

## Description:

Correct barrel/pincushion distortions occurring with wide-angle lens.  
  
References:  
[1] Zhang Z. (1999). Flexible camera calibration by viewing a plane from unknown orientation.  
[2] Andrew W. Fitzgibbon (2001). Simultaneous linear estimation of multiple view geometry and lens distortion.  
boundary\_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.  

## Default values:

amplitude=0.25, aspect\_ratio=0, zoom=0, center\_x=center\_y=50% and boundary\_conditions=0.

---

# Command: unroll
**Category:** Geometry Manipulation
**Source:** https://gmic.eu/reference/unroll.html#top

|  |  |
| --- | --- |
| unroll | Built-in command |

## Arguments:

* \_axis={ x | y | z | c }

## Description:

Unroll selected images along specified axis.  

(*equivalent to shortcut command* y).

## Default values:

axis=y.

## Example of use:

(1,2,3;4,5,6;7,8,9) +unroll y

  

[![](img/t0_unroll.jpg)](img/f0_unroll.jpg)

Command: **(1,2,3;4,5,6;7,8,9) +unroll y**

[![](img/t1_unroll.jpg)](img/f1_unroll.jpg)

Command: **(1,2,3;4,5,6;7,8,9) +unroll y**

---

# Command: upscale_smart
**Category:** Geometry Manipulation
**Source:** https://gmic.eu/reference/upscale_smart.html#top

# upscale\_smart

## Arguments:

* width[%],\_height[%],\_depth,\_smoothness>=0,\_anisotropy=[0,1],sharpening>=0

## Description:

Upscale selected images with an edge-preserving algorithm.  

## Default values:

height=100%, depth=100%, smoothness=2, anisotropy=0.4 and sharpening=10.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rescale2d ,100 +upscale\_smart 500%,500% append x

  
[![](img/t_upscale_smart.jpg)](img/f_upscale_smart.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rescale2d ,100 +upscale\_smart 500%,500% append x**

---

# Command: volumetric2d
**Category:** Geometry Manipulation
**Source:** https://gmic.eu/reference/volumetric2d.html#top

# volumetric2d

## Arguments:

* \_x[%],\_y[%],\_z[%],\_separator\_size>=0

## Description:

Convert selected 3D volumetric images into a 2D representation.  

## Default values:

x=y=z=50% and separator\_size=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rescale2d 64 animate noise,0,100,50 cut 0,255 append z volumetric2d 50%,50%,50%,1

  
[![](img/t_volumetric2d.jpg)](img/f_volumetric2d.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rescale2d 64 animate noise,0,100,50 cut 0,255 append z volumetric2d 50%,50%,50%,1**

---

# Command: bandpass
**Category:** Filtering
**Source:** https://gmic.eu/reference/bandpass.html#top

# bandpass

## Arguments:

* \_min\_freq[%],\_max\_freq[%]

## Description:

Apply bandpass filter to selected images.  

## Default values:

min\_freq=0 and max\_freq=20%.

This command has a [tutorial page](https://gmic.eu/oldtutorial/_bandpass).

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> bandpass 1%,3%

  
[![](img/t_bandpass.jpg)](img/f_bandpass.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> bandpass 1%,3%**

---

# Command: bilateral
**Category:** Filtering
**Source:** https://gmic.eu/reference/bilateral.html#top

|  |  |
| --- | --- |
| bilateral | Built-in command |

## Arguments:

* [guide],std\_deviation\_s[%]>=0,std\_deviation\_r[%]>=0,\_sampling\_s>=0,\_sampling\_r>=0    or
* std\_deviation\_s[%]>=0,std\_deviation\_r[%]>=0,\_sampling\_s>=0,\_sampling\_r>=0

## Description:

Blur selected images by anisotropic (eventually joint/cross) bilateral filtering.  
  
If a guide image is provided, it is used for drive the smoothing filter.  
A guide image must be of the same xyz-size as the selected images.  
Set sampling arguments to 0 for automatic adjustment.  

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> repeat 5 { bilateral 10,10 }

  
[![](img/t_bilateral.jpg)](img/f_bilateral.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> repeat 5 { bilateral 10,10 }**

---

# Command: blur
**Category:** Filtering
**Source:** https://gmic.eu/reference/blur.html#top

|  |  |
| --- | --- |
| blur | Built-in command |

## Arguments:

* std\_deviation[%]>=0,\_boundary\_conditions,\_kernel    or
* axes,std\_deviation[%]>=0,\_boundary\_conditions,\_kernel

## Description:

Blur selected images by a Deriche or gaussian filter (recursive implementation).  

(*equivalent to shortcut command* b).

  
boundary\_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.  
kernel can be { 0:Deriche | 1:Gaussian }.  
When specified, argument axes is a sequence of { x | y | z | c }.  
Specifying one axis multiple times apply also the blur multiple times.  

## Default values:

boundary\_conditions=1 and kernel=1.

This command has a [tutorial page](https://gmic.eu/oldtutorial/_blur).

## Examples of use:

### • Example #1

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +blur 5,0 +blur[0] 5,1

  

[![](img/t0_blur.jpg)](img/f0_blur.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +blur 5,0 +blur[0] 5,1**

[![](img/t1_blur.jpg)](img/f1_blur.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +blur 5,0 +blur[0] 5,1**

[![](img/t2_blur.jpg)](img/f2_blur.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +blur 5,0 +blur[0] 5,1**

### • Example #2

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +blur y,10%

  

[![](img/t0_blur_2.jpg)](img/f0_blur_2.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +blur y,10%**

[![](img/t1_blur_2.jpg)](img/f1_blur_2.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +blur y,10%**

---

# Command: blur_angular
**Category:** Filtering
**Source:** https://gmic.eu/reference/blur_angular.html#top

# blur\_angular

## Arguments:

* amplitude[%],\_center\_x[%],\_center\_y[%]

## Description:

Apply angular blur on selected images.  

## Default values:

center\_x=center\_y=50%.

This command has a [tutorial page](https://gmic.eu/oldtutorial/_blur_angular).

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> blur\_angular 2%

  
[![](img/t_blur_angular.jpg)](img/f_blur_angular.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> blur\_angular 2%**

---

# Command: blur_bloom
**Category:** Filtering
**Source:** https://gmic.eu/reference/blur_bloom.html#top

# blur\_bloom

## Arguments:

* \_amplitude>=0,\_ratio>=0,\_nb\_iter>=0,\_blend\_operator={ + | max | min },\_kernel={ 0:Deriche | 1:Gaussian | 2:Box | 3:Triangle | 4:Quadratic },\_normalize\_scales={ 0:No | 1:Yes },\_axes

## Description:

Apply a bloom filter that blend multiple blur filters of different radii,  
  
resulting in a larger but sharper glare than a simple blur.  
When specified, argument axes is a sequence of { x | y | z | c }.  
Specifying one axis multiple times apply also the blur multiple times.  
Reference: Masaki Kawase, "Practical Implementation of High Dynamic Range Rendering", GDC 2004.  

## Default values:

amplitude=1, ratio=2, nb\_iter=5, blend\_operator=+, kernel=1, normalize\_scales=0 and axes=(all)

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> blur\_bloom ,

  
[![](img/t_blur_bloom.jpg)](img/f_blur_bloom.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> blur\_bloom ,**

---

# Command: blur_linear
**Category:** Filtering
**Source:** https://gmic.eu/reference/blur_linear.html#top

# blur\_linear

## Arguments:

* amplitude1[%],\_amplitude2[%],\_angle,\_boundary\_conditions={ 0:Dirichlet | 1:Neumann }

## Description:

Apply linear blur on selected images, with specified angle and amplitudes.  

## Default values:

amplitude2=0, angle=0 and boundary\_conditions=1.

This command has a [tutorial page](https://gmic.eu/oldtutorial/_blur_linear).

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> blur\_linear 10,0,45

  
[![](img/t_blur_linear.jpg)](img/f_blur_linear.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> blur\_linear 10,0,45**

---

# Command: blur_radial
**Category:** Filtering
**Source:** https://gmic.eu/reference/blur_radial.html#top

# blur\_radial

## Arguments:

* amplitude[%],\_center\_x[%],\_center\_y[%]

## Description:

Apply radial blur on selected images.  

## Default values:

center\_x=center\_y=50%.

This command has a [tutorial page](https://gmic.eu/oldtutorial/_blur_radial).

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> blur\_radial 2%

  
[![](img/t_blur_radial.jpg)](img/f_blur_radial.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> blur\_radial 2%**

---

# Command: blur_selective
**Category:** Filtering
**Source:** https://gmic.eu/reference/blur_selective.html#top

# blur\_selective

## Arguments:

* sigma>=0,\_edges>0,\_nb\_scales>0

## Description:

Blur selected images using selective gaussian scales.  

## Default values:

sigma=5, edges=0.5 and nb\_scales=5.

This command has a [tutorial page](https://gmic.eu/oldtutorial/_blur_selective).

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> noise 20 cut 0,255 +local[-1] repeat 4 { blur\_selective , } done

  

[![](img/t0_blur_selective.jpg)](img/f0_blur_selective.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> noise 20 cut 0,255 +local[-1] repeat 4 { blur\_selective , } done**

[![](img/t1_blur_selective.jpg)](img/f1_blur_selective.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> noise 20 cut 0,255 +local[-1] repeat 4 { blur\_selective , } done**

---

# Command: boxfilter
**Category:** Filtering
**Source:** https://gmic.eu/reference/boxfilter.html#top

|  |  |
| --- | --- |
| boxfilter | Built-in command |

## Arguments:

* size[%]>=0,\_order,\_boundary\_conditions,\_nb\_iter>=0    or
* axes,size[%]>=0,\_order,\_boundary\_conditions,\_nb\_iter>=0

## Description:

Blur selected images by a box filter of specified size (fast recursive implementation).  
  
order can be { 0:Smooth | 1:1st-derivative | 2:2nd-derivative }.  
boundary\_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.  
When specified, argument axes is a sequence of { x | y | z | c }.  
Specifying one axis multiple times apply also the blur multiple times.  

## Default values:

order=0, boundary\_conditions=1 and nb\_iter=1.

## Examples of use:

### • Example #1

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +boxfilter 5%

  

[![](img/t0_boxfilter.jpg)](img/f0_boxfilter.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +boxfilter 5%**

[![](img/t1_boxfilter.jpg)](img/f1_boxfilter.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +boxfilter 5%**

### • Example #2

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +boxfilter y,3,1

  

[![](img/t0_boxfilter_2.jpg)](img/f0_boxfilter_2.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +boxfilter y,3,1**

[![](img/t1_boxfilter_2.jpg)](img/f1_boxfilter_2.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +boxfilter y,3,1**

---

# Command: bump2normal
**Category:** Filtering
**Source:** https://gmic.eu/reference/bump2normal.html#top

# bump2normal

### No argumentsDescription:Convert selected bumpmaps to normalmaps. Example of use: 300,300 circle 50%,50%,128,1,255 blur 2% +bump2normal Command: **300,300 circle 50%,50%,128,1,255 blur 2% +bump2normal** Command: **300,300 circle 50%,50%,128,1,255 blur 2% +bump2normal**

---

# Command: closing
**Category:** Filtering
**Source:** https://gmic.eu/reference/closing.html#top

# closing

## Arguments:

* size>=0    or
* size\_x>=0,size\_y>=0,\_size\_z>=0    or
* [kernel],\_boundary\_conditions,\_is\_real={ 0:Binary-mode | 1:Real-mode }

## Description:

Apply morphological closing to selected images.  
  
boundary\_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.  

## Default values:

size\_z=1, boundary\_conditions=1 and is\_real=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +closing 10

  

[![](img/t0_closing.jpg)](img/f0_closing.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +closing 10**

[![](img/t1_closing.jpg)](img/f1_closing.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +closing 10**

---

# Command: closing_circ
**Category:** Filtering
**Source:** https://gmic.eu/reference/closing_circ.html#top

# closing\_circ

## Arguments:

* \_size>=0,\_is\_real={ 0:No | 1:Yes }

## Description:

Apply circular dilation of selected images by specified size.  

## Default values:

boundary\_conditions=1 and is\_real=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +closing\_circ 7

  

[![](img/t0_closing_circ.jpg)](img/f0_closing_circ.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +closing\_circ 7**

[![](img/t1_closing_circ.jpg)](img/f1_closing_circ.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +closing\_circ 7**

---

# Command: convolve
**Category:** Filtering
**Source:** https://gmic.eu/reference/convolve.html#top

|  |  |
| --- | --- |
| convolve | Built-in command |

## Arguments:

* [mask],\_boundary\_conditions,\_is\_normalized={ 0:No | 1:Yes },\_channel\_mode,\_xcenter,\_ycenter,\_zcenter,\_xstride>0,\_ystride>0,\_zstride>0,\_xdilation,\_ydilation,\_zdilation,\_xoffset,\_yoffset,\_zoffset,\_xsize>=0,\_ysize>=0,\_zsize>=0

## Description:

Convolve selected images by specified mask.  
  
boundary\_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.  
channel\_mode can be { 0:All | 1:One-for-one | 2:Partial sum | 3:Full sum }.  

## Default values:

boundary\_conditions=1, is\_normalized=0, channel\_mode=1, xcenter=ycenter=zcenter=(undefined), xstride=ystride=zstride=1, xdilation=ydilation=zdilation=1,xoffset=yoffset=zoffset=0 and xsize=ysize=zsize=(input\_size/stride).

This command has a [tutorial page](https://gmic.eu/oldtutorial/_convolve).

## Examples of use:

### • Example #1

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> (0,1,0;1,-4,1;0,1,0) convolve[-2] [-1] keep[-2]

  
[![](img/t_convolve.jpg)](img/f_convolve.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> (0,1,0;1,-4,1;0,1,0) convolve[-2] [-1] keep[-2]**

### • Example #2

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> (0,1,0) resize[-1] 130,1,1,1,3 +convolve[0] [1]

  

[![](img/t0_convolve_2.jpg)](img/f0_convolve_2.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> (0,1,0) resize[-1] 130,1,1,1,3 +convolve[0] [1]**

[![](img/t1_convolve_2.jpg)](img/f1_convolve_2.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> (0,1,0) resize[-1] 130,1,1,1,3 +convolve[0] [1]**

[![](img/t2_convolve_2.jpg)](img/f2_convolve_2.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> (0,1,0) resize[-1] 130,1,1,1,3 +convolve[0] [1]**

---

# Command: convolve_fft
**Category:** Filtering
**Source:** https://gmic.eu/reference/convolve_fft.html#top

# convolve\_fft

## Arguments:

* [mask],\_boundary\_conditions

## Description:

Convolve selected images with specified mask, in the fourier domain.  
  
boundary\_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.  

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> 100%,100% gaussian[-1] 20,1,45 +convolve\_fft[0] [1]

  

[![](img/t0_convolve_fft.jpg)](img/f0_convolve_fft.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> 100%,100% gaussian[-1] 20,1,45 +convolve\_fft[0] [1]**

[![](img/t1_convolve_fft.jpg)](img/f1_convolve_fft.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> 100%,100% gaussian[-1] 20,1,45 +convolve\_fft[0] [1]**

[![](img/t2_convolve_fft.jpg)](img/f2_convolve_fft.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> 100%,100% gaussian[-1] 20,1,45 +convolve\_fft[0] [1]**

---

# Command: correlate
**Category:** Filtering
**Source:** https://gmic.eu/reference/correlate.html#top

|  |  |
| --- | --- |
| correlate | Built-in command |

## Arguments:

* [mask],\_boundary\_conditions,\_is\_normalized={ 0:No | 1:Yes },\_channel\_mode,\_xcenter,\_ycenter,\_zcenter,\_xstride>0,\_ystride>0,\_zstride>0,\_xdilation,\_ydilation,\_zdilation,\_xoffset,\_yoffset,\_zoffset,\_xsize>=0,\_ysize>=0,\_zsize>=0

## Description:

Correlate selected images by specified mask.  
  
boundary\_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.  
channel\_mode can be { 0:All | 1:One-for-one | 2:Partial sum | 3:Full sum }.  

## Default values:

boundary\_conditions=1, is\_normalized=0, channel\_mode=1, xcenter=ycenter=zcenter=-1, xstride=ystride=zstride=1, xdilation=ydilation=zdilation=1,xoffset=yoffset=zoffset=0 and xsize=ysize=zsize=(input\_size/stride).

## Examples of use:

### • Example #1

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> (0,1,0;1,-4,1;0,1,0) correlate[-2] [-1] keep[-2]

  
[![](img/t_correlate.jpg)](img/f_correlate.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> (0,1,0;1,-4,1;0,1,0) correlate[-2] [-1] keep[-2]**

### • Example #2

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +crop 40%,40%,60%,60% +correlate[0] [-1],0,1

  

[![](img/t0_correlate_2.jpg)](img/f0_correlate_2.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +crop 40%,40%,60%,60% +correlate[0] [-1],0,1**

[![](img/t1_correlate_2.jpg)](img/f1_correlate_2.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +crop 40%,40%,60%,60% +correlate[0] [-1],0,1**

[![](img/t2_correlate_2.jpg)](img/f2_correlate_2.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +crop 40%,40%,60%,60% +correlate[0] [-1],0,1**

---

# Command: cross_correlation
**Category:** Filtering
**Source:** https://gmic.eu/reference/cross_correlation.html#top

# cross\_correlation

## Arguments:

* [mask]

## Description:

Compute cross-correlation of selected images with specified mask.  

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +shift -30,-20 +cross\_correlation[0] [1]

  

[![](img/t0_cross_correlation.jpg)](img/f0_cross_correlation.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +shift -30,-20 +cross\_correlation[0] [1]**

[![](img/t1_cross_correlation.jpg)](img/f1_cross_correlation.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +shift -30,-20 +cross\_correlation[0] [1]**

[![](img/t2_cross_correlation.jpg)](img/f2_cross_correlation.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +shift -30,-20 +cross\_correlation[0] [1]**

---

# Command: curvature
**Category:** Filtering
**Source:** https://gmic.eu/reference/curvature.html#top

# curvature

### No argumentsDescription:Compute isophote curvatures on selected images. Example of use: <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> blur 10 curvature Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> blur 10 curvature**

---

# Command: dct
**Category:** Filtering
**Source:** https://gmic.eu/reference/dct.html#top

# dct

## Arguments:

* \_{ x | y | z }...{ x | y | z }    or
* (no arg)

## Description:

Compute the discrete cosine transform of selected images, optionally along the specified axes only.  
  
Output images are always evenly sized, so this command may change the size of the selected images.  

## Default values:

(no arg)

## See also:

[idct](idct.html).

This command has a [tutorial page](https://gmic.eu/oldtutorial/_dct-and-idct).

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +dct +idct[-1] abs[-2] +[-2] 1 log[-2]

  

[![](img/t0_dct.jpg)](img/f0_dct.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +dct +idct[-1] abs[-2] +[-2] 1 log[-2]**

[![](img/t1_dct.jpg)](img/f1_dct.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +dct +idct[-1] abs[-2] +[-2] 1 log[-2]**

[![](img/t2_dct.jpg)](img/f2_dct.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +dct +idct[-1] abs[-2] +[-2] 1 log[-2]**

---

# Command: deblur
**Category:** Filtering
**Source:** https://gmic.eu/reference/deblur.html#top

# deblur

## Arguments:

* amplitude[%]>=0,\_nb\_iter>=0,\_dt>=0,\_regul>=0,\_regul\_type={ 0:Tikhonov | 1:Meancurv. | 2:TV }

## Description:

Deblur image using a regularized Jansson-Van Cittert algorithm.  

## Default values:

nb\_iter=10, dt=20, regul=0.7 and regul\_type=1.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> blur 3 +deblur 3,40,20,0.01

  

[![](img/t0_deblur.jpg)](img/f0_deblur.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> blur 3 +deblur 3,40,20,0.01**

[![](img/t1_deblur.jpg)](img/f1_deblur.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> blur 3 +deblur 3,40,20,0.01**

---

# Command: deblur_goldmeinel
**Category:** Filtering
**Source:** https://gmic.eu/reference/deblur_goldmeinel.html#top

# deblur\_goldmeinel

## Arguments:

* sigma>=0,\_nb\_iter>=0,\_acceleration>=0,\_kernel\_type={ 0:Deriche | 1:Gaussian }.

## Description:

Deblur selected images using Gold-Meinel algorithm  

## Default values:

nb\_iter=8, acceleration=1 and kernel\_type=1.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +blur 1 +deblur\_goldmeinel[-1] 1

  

[![](img/t0_deblur_goldmeinel.jpg)](img/f0_deblur_goldmeinel.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +blur 1 +deblur\_goldmeinel[-1] 1**

[![](img/t1_deblur_goldmeinel.jpg)](img/f1_deblur_goldmeinel.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +blur 1 +deblur\_goldmeinel[-1] 1**

[![](img/t2_deblur_goldmeinel.jpg)](img/f2_deblur_goldmeinel.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +blur 1 +deblur\_goldmeinel[-1] 1**

---

# Command: deblur_richardsonlucy
**Category:** Filtering
**Source:** https://gmic.eu/reference/deblur_richardsonlucy.html#top

# deblur\_richardsonlucy

## Arguments:

* sigma>=0, nb\_iter>=0, \_kernel\_type={ 0:Deriche | 1:Gaussian }.

## Description:

Deblur selected images using Richardson-Lucy algorithm.  

## Default values:

nb\_iter=50 and kernel\_type=1.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +blur 1 +deblur\_richardsonlucy[-1] 1

  

[![](img/t0_deblur_richardsonlucy.jpg)](img/f0_deblur_richardsonlucy.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +blur 1 +deblur\_richardsonlucy[-1] 1**

[![](img/t1_deblur_richardsonlucy.jpg)](img/f1_deblur_richardsonlucy.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +blur 1 +deblur\_richardsonlucy[-1] 1**

[![](img/t2_deblur_richardsonlucy.jpg)](img/f2_deblur_richardsonlucy.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +blur 1 +deblur\_richardsonlucy[-1] 1**

---

# Command: deconvolve_fft
**Category:** Filtering
**Source:** https://gmic.eu/reference/deconvolve_fft.html#top

# deconvolve\_fft

## Arguments:

* [kernel],\_regularization>=0

## Description:

Deconvolve selected images by specified mask in the fourier space.  

## Default values:

regularization>=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +gaussian 5 +convolve\_fft[0] [1] +deconvolve\_fft[-1] [1]

  

[![](img/t0_deconvolve_fft.jpg)](img/f0_deconvolve_fft.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +gaussian 5 +convolve\_fft[0] [1] +deconvolve\_fft[-1] [1]**

[![](img/t1_deconvolve_fft.jpg)](img/f1_deconvolve_fft.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +gaussian 5 +convolve\_fft[0] [1] +deconvolve\_fft[-1] [1]**

[![](img/t2_deconvolve_fft.jpg)](img/f2_deconvolve_fft.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +gaussian 5 +convolve\_fft[0] [1] +deconvolve\_fft[-1] [1]**

[![](img/t3_deconvolve_fft.jpg)](img/f3_deconvolve_fft.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +gaussian 5 +convolve\_fft[0] [1] +deconvolve\_fft[-1] [1]**

---

# Command: deinterlace
**Category:** Filtering
**Source:** https://gmic.eu/reference/deinterlace.html#top

# deinterlace

## Arguments:

* \_method

## Description:

Deinterlace selected images (method can be { 0:Standard | 1:Motion-compensated }).  

## Default values:

method=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +rotate 3,1,1,50%,50% resize 100%,50% resize 100%,200%,1,3,4 shift[-1] 0,1 add +deinterlace 1

  

[![](img/t0_deinterlace.jpg)](img/f0_deinterlace.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +rotate 3,1,1,50%,50% resize 100%,50% resize 100%,200%,1,3,4 shift[-1] 0,1 add +deinterlace 1**

[![](img/t1_deinterlace.jpg)](img/f1_deinterlace.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +rotate 3,1,1,50%,50% resize 100%,50% resize 100%,200%,1,3,4 shift[-1] 0,1 add +deinterlace 1**

---

# Command: denoise
**Category:** Filtering
**Source:** https://gmic.eu/reference/denoise.html#top

|  |  |
| --- | --- |
| denoise | Built-in command |

## Arguments:

* [guide],std\_deviation\_s[%]>=0,std\_deviation\_r[%]>=0,\_patch\_size>0,\_lookup\_size>0,\_smoothness,\_fast\_approx={ 0:No | 1:Yes }    or
* std\_deviation\_s[%]>=0,std\_deviation\_r[%]>=0,\_patch\_size>0,\_lookup\_size>0,\_smoothness,\_fast\_approx={ 0:No | 1:Yes }

## Description:

Denoise selected images by non-local patch averaging.  

## Default values:

patch\_size=5, lookup\_size=6 and smoothness=1.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +denoise 5,5,8

  

[![](img/t0_denoise.jpg)](img/f0_denoise.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +denoise 5,5,8**

[![](img/t1_denoise.jpg)](img/f1_denoise.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +denoise 5,5,8**

---

# Command: denoise_haar
**Category:** Filtering
**Source:** https://gmic.eu/reference/denoise_haar.html#top

# denoise\_haar

## Arguments:

* \_threshold>=0,\_nb\_scales>=0,\_cycle\_spinning>0

## Description:

Denoise selected images using haar-wavelet thresholding with cycle spinning.  
  
Set nb\_scales==0 to automatically determine the optimal number of scales.  

## Default values:

threshold=1.4, nb\_scale=0 and cycle\_spinning=10.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> noise 20 cut 0,255 +denoise\_haar[-1] 0.8

  

[![](img/t0_denoise_haar.jpg)](img/f0_denoise_haar.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> noise 20 cut 0,255 +denoise\_haar[-1] 0.8**

[![](img/t1_denoise_haar.jpg)](img/f1_denoise_haar.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> noise 20 cut 0,255 +denoise\_haar[-1] 0.8**

---

# Command: denoise_cnn
**Category:** Filtering
**Source:** https://gmic.eu/reference/denoise_cnn.html#top

# denoise\_cnn

## Arguments:

* \_noise\_level>=0,\_patch\_size>0

## Description:

Denoise selected images using a convolutional neural network (CNN).  
  
Input value range should be [0,255]. Output value range is [0,255].  
If std\_noise==0, the noise level is automatically estimated for each selected image.  

## Default values:

noise\_level=0 (auto) and patch\_size=64.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> noise 20 cut 0,255 +denoise\_cnn 0

  

[![](img/t0_denoise_cnn.jpg)](img/f0_denoise_cnn.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> noise 20 cut 0,255 +denoise\_cnn 0**

[![](img/t1_denoise_cnn.jpg)](img/f1_denoise_cnn.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> noise 20 cut 0,255 +denoise\_cnn 0**

---

# Command: denoise_patchpca
**Category:** Filtering
**Source:** https://gmic.eu/reference/denoise_patchpca.html#top

# denoise\_patchpca

## Arguments:

* \_strength>=0,\_patch\_size>0,\_lookup\_size>0,\_spatial\_sampling>0

## Description:

Denoise selected images using the patch-pca algorithm.  

## Default values:

patch\_size=7, lookup\_size=11, details=1.8 and spatial\_sampling=5.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +noise 20 cut[-1] 0,255 +denoise\_patchpca[-1] ,

  

[![](img/t0_denoise_patchpca.jpg)](img/f0_denoise_patchpca.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +noise 20 cut[-1] 0,255 +denoise\_patchpca[-1] ,**

[![](img/t1_denoise_patchpca.jpg)](img/f1_denoise_patchpca.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +noise 20 cut[-1] 0,255 +denoise\_patchpca[-1] ,**

[![](img/t2_denoise_patchpca.jpg)](img/f2_denoise_patchpca.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +noise 20 cut[-1] 0,255 +denoise\_patchpca[-1] ,**

---

# Command: deriche
**Category:** Filtering
**Source:** https://gmic.eu/reference/deriche.html#top

|  |  |
| --- | --- |
| deriche | Built-in command |

## Arguments:

* std\_deviation[%]>=0,order={ 0 | 1 | 2 },axis={ x | y | z | c },\_boundary\_conditions

## Description:

Apply Deriche recursive filter on selected images, along specified axis and with  
  
specified standard deviation, order and boundary conditions.  
boundary\_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.  

## Default values:

boundary\_conditions=1.

This command has a [tutorial page](https://gmic.eu/oldtutorial/_deriche).

## Examples of use:

### • Example #1

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> deriche 3,1,x

  
[![](img/t_deriche.jpg)](img/f_deriche.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> deriche 3,1,x**

### • Example #2

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +deriche 30,0,x deriche[-2] 30,0,y add

  
[![](img/t_deriche_2.jpg)](img/f_deriche_2.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +deriche 30,0,x deriche[-2] 30,0,y add**

---

# Command: dilate
**Category:** Filtering
**Source:** https://gmic.eu/reference/dilate.html#top

|  |  |
| --- | --- |
| dilate | Built-in command |

## Arguments:

* size[%]>=0    or
* size\_x[%]>=0,size\_y[%]>=0,size\_z[%]>=0    or
* [kernel],\_boundary\_conditions,\_is\_real={ 0:Binary-mode | 1:Real-mode }

## Description:

Dilate selected images by a rectangular or the specified structuring element.  
  
boundary\_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.  

## Default values:

size\_z=1, boundary\_conditions=1 and is\_real=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +dilate 10

  

[![](img/t0_dilate.jpg)](img/f0_dilate.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +dilate 10**

[![](img/t1_dilate.jpg)](img/f1_dilate.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +dilate 10**

---

# Command: dilate_circ
**Category:** Filtering
**Source:** https://gmic.eu/reference/dilate_circ.html#top

# dilate\_circ

## Arguments:

* \_size[%]>=0,\_boundary\_conditions,\_is\_real={ 0:No | 1:Yes }

## Description:

Apply circular dilation of selected images by specified size.  
  
boundary\_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.  

## Default values:

boundary\_conditions=1 and is\_real=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +dilate\_circ 7

  

[![](img/t0_dilate_circ.jpg)](img/f0_dilate_circ.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +dilate\_circ 7**

[![](img/t1_dilate_circ.jpg)](img/f1_dilate_circ.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +dilate\_circ 7**

---

# Command: dilate_oct
**Category:** Filtering
**Source:** https://gmic.eu/reference/dilate_oct.html#top

# dilate\_oct

## Arguments:

* \_size[%]>=0,\_boundary\_conditions,\_is\_real={ 0:No | 1:Yes }

## Description:

Apply octagonal dilation of selected images by specified size.  

## Default values:

boundary\_conditions=1 and is\_real=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +dilate\_oct 7

  

[![](img/t0_dilate_oct.jpg)](img/f0_dilate_oct.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +dilate\_oct 7**

[![](img/t1_dilate_oct.jpg)](img/f1_dilate_oct.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +dilate\_oct 7**

---

# Command: dilate_threshold
**Category:** Filtering
**Source:** https://gmic.eu/reference/dilate_threshold.html#top

# dilate\_threshold

## Arguments:

* size\_x>=1,size\_y>=1,size\_z>=1,\_threshold>=0,\_boundary\_conditions

## Description:

Dilate selected images in the (X,Y,Z,I) space.  
  
boundary\_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.  

## Default values:

size\_y=size\_x, size\_z=1, threshold=255 and boundary\_conditions=1.

---

# Command: divergence
**Category:** Filtering
**Source:** https://gmic.eu/reference/divergence.html#top

# divergence

### No argumentsDescription:Compute divergence of selected vector fields. Example of use: <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> luminance +gradient append[-2,-1] c divergence[-1] Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> luminance +gradient append[-2,-1] c divergence[-1]** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> luminance +gradient append[-2,-1] c divergence[-1]**

---

# Command: dog
**Category:** Filtering
**Source:** https://gmic.eu/reference/dog.html#top

# dog

## Arguments:

* \_sigma1[%]>=0,\_sigma2[%]>=0

## Description:

Compute difference of gaussian on selected images.  

## Default values:

sigma1=2% and sigma2=3%.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> dog 2,3

  
[![](img/t_dog.jpg)](img/f_dog.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> dog 2,3**

---

# Command: diffusiontensors
**Category:** Filtering
**Source:** https://gmic.eu/reference/diffusiontensors.html#top

# diffusiontensors

## Arguments:

* \_sharpness>=0,0<=\_anisotropy<=1,\_alpha[%],\_sigma[%],is\_sqrt={ 0:No | 1:Yes }

## Description:

Compute the diffusion tensors of selected images for edge-preserving smoothing algorithms.  

## Default values:

sharpness=0.7, anisotropy=0.3, alpha=0.6, sigma=1.1 and is\_sqrt=0.

This command has a [tutorial page](https://gmic.eu/oldtutorial/_diffusiontensors).

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> diffusiontensors 0.8 abs pow 0.2

  
[![](img/t_diffusiontensors.jpg)](img/f_diffusiontensors.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> diffusiontensors 0.8 abs pow 0.2**

---

# Command: erode
**Category:** Filtering
**Source:** https://gmic.eu/reference/erode.html#top

|  |  |
| --- | --- |
| erode | Built-in command |

## Arguments:

* size[%]>=0    or
* size\_x[%]>=0,size\_y[%]>=0,\_size\_z[%]>=0    or
* [kernel],\_boundary\_conditions,\_is\_real={ 0:Binary-mode | 1:Real-mode }

## Description:

Erode selected images by a rectangular or the specified structuring element.  
  
boundary\_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.  

## Default values:

size\_z=1, boundary\_conditions=1 and is\_real=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +erode 10

  

[![](img/t0_erode.jpg)](img/f0_erode.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +erode 10**

[![](img/t1_erode.jpg)](img/f1_erode.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +erode 10**

---

# Command: erode_circ
**Category:** Filtering
**Source:** https://gmic.eu/reference/erode_circ.html#top

# erode\_circ

## Arguments:

* \_size[%]>=0,\_boundary\_conditions,\_is\_real={ 0:No | 1:Yes }

## Description:

Apply circular erosion of selected images by specified size.  
  
boundary\_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.  

## Default values:

boundary\_conditions=1 and is\_real=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +erode\_circ 7

  

[![](img/t0_erode_circ.jpg)](img/f0_erode_circ.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +erode\_circ 7**

[![](img/t1_erode_circ.jpg)](img/f1_erode_circ.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +erode\_circ 7**

---

# Command: erode_oct
**Category:** Filtering
**Source:** https://gmic.eu/reference/erode_oct.html#top

# erode\_oct

## Arguments:

* \_size[%]>=0,\_boundary\_conditions,\_is\_real={ 0:No | 1:Yes }

## Description:

Apply octagonal erosion of selected images by specified size.  

## Default values:

boundary\_conditions=1 and is\_real=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +erode\_oct 7

  

[![](img/t0_erode_oct.jpg)](img/f0_erode_oct.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +erode\_oct 7**

[![](img/t1_erode_oct.jpg)](img/f1_erode_oct.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +erode\_oct 7**

---

# Command: erode_threshold
**Category:** Filtering
**Source:** https://gmic.eu/reference/erode_threshold.html#top

# erode\_threshold

## Arguments:

* size\_x>=1,size\_y>=1,size\_z>=1,\_threshold>=0,\_boundary\_conditions

## Description:

Erode selected images in the (X,Y,Z,I) space.  
  
boundary\_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.  

## Default values:

size\_y=size\_x, size\_z=1, threshold=255 and boundary\_conditions=1.

---

# Command: fft
**Category:** Filtering
**Source:** https://gmic.eu/reference/fft.html#top

|  |  |
| --- | --- |
| fft | Built-in command |

## Arguments:

* \_{ x | y | z }...{ x | y | z }

## Description:

Compute the direct fourier transform (real and imaginary parts) of selected images,  
  
optionally along the specified axes only.  

## See also:

[ifft](ifft.html).

This command has a [tutorial page](https://gmic.eu/oldtutorial/_fft).

## Examples of use:

### • Example #1

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> luminance +fft append[-2,-1] c norm[-1] log[-1] shift[-1] 50%,50%,0,0,2

  

[![](img/t0_fft.jpg)](img/f0_fft.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> luminance +fft append[-2,-1] c norm[-1] log[-1] shift[-1] 50%,50%,0,0,2**

[![](img/t1_fft.jpg)](img/f1_fft.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> luminance +fft append[-2,-1] c norm[-1] log[-1] shift[-1] 50%,50%,0,0,2**

### • Example #2

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> w2:=int(w/2) h2:=int(h/2) fft shift $w2,$h2,0,0,2 ellipse $w2,$h2,30,30,0,1,0 shift -$w2,-$h2,0,0,2 ifft remove[-1]

  
[![](img/t_fft_2.jpg)](img/f_fft_2.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> w2:=int(w/2) h2:=int(h/2) fft shift $w2,$h2,0,0,2 ellipse $w2,$h2,30,30,0,1,0 shift -$w2,-$h2,0,0,2 ifft remove[-1]**

---

# Command: gradient
**Category:** Filtering
**Source:** https://gmic.eu/reference/gradient.html#top

# gradient

## Arguments:

* { x | y | z | c }...{ x | y | z | c },\_scheme,\_boundary\_conditions    or
* (no arg)

## Description:

Compute the gradient components (first derivatives) of selected images, along specified axes.  

(*equivalent to shortcut command* g).

  
scheme can be { -1:Backward | 0:Centered | 1:Forward | 2:Sobel | 3:Rotation-invariant (default) | 4:Deriche | 5:Vanvliet | 6:FB-Maxabs }.  
boundary\_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.  
(no arg) compute all significant components.  

## Default values:

scheme=0 and boundary\_conditions=1.

This command has a [tutorial page](https://gmic.eu/oldtutorial/_gradient).

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> gradient

  

[![](img/t0_gradient.jpg)](img/f0_gradient.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> gradient**

[![](img/t1_gradient.jpg)](img/f1_gradient.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> gradient**

---

# Command: gradient_norm
**Category:** Filtering
**Source:** https://gmic.eu/reference/gradient_norm.html#top

# gradient\_norm

## Arguments:

* \_scheme,\_boundary\_conditions    or
* (no arg)

## Description:

Compute the gradient norm of selected images.  
  
scheme can be { -1:Backward | 0:Centered | 1:Forward | 2:Sobel | 3:Rotation-invariant (default) | 4:Deriche | 5:Vanvliet | 6:FB-Maxabs }.  
boundary\_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.  

## Default values:

scheme=0 and boundary\_conditions=1.

This command has a [tutorial page](https://gmic.eu/oldtutorial/_gradient_norm).

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> gradient\_norm equalize

  
[![](img/t_gradient_norm.jpg)](img/f_gradient_norm.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> gradient\_norm equalize**

---

# Command: gradient_orientation
**Category:** Filtering
**Source:** https://gmic.eu/reference/gradient_orientation.html#top

# gradient\_orientation

## Arguments:

* \_dimension={ 1 | 2 | 3 }

## Description:

Compute N-d gradient orientation of selected images.  

## Default values:

dimension=3.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +gradient\_orientation 2

  

[![](img/t0_gradient_orientation.jpg)](img/f0_gradient_orientation.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +gradient\_orientation 2**

[![](img/t1_gradient_orientation.jpg)](img/f1_gradient_orientation.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +gradient\_orientation 2**

[![](img/t2_gradient_orientation.jpg)](img/f2_gradient_orientation.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +gradient\_orientation 2**

---

# Command: guided
**Category:** Filtering
**Source:** https://gmic.eu/reference/guided.html#top

|  |  |
| --- | --- |
| guided | Built-in command |

## Arguments:

* [guide],radius[%]>=0,regularization[%]>=0    or
* radius[%]>=0,regularization[%]>=0

## Description:

Blur selected images by guided image filtering.  
  
If a guide image is provided, it is used to drive the smoothing process.  
A guide image must be of the same xyz-size as the selected images.  
This command implements the filtering algorithm described in:  
He, Kaiming; Sun, Jian; Tang, Xiaoou, "Guided Image Filtering",  
IEEE Transactions on Pattern Analysis and Machine Intelligence, vol.35, no.6, pp.1397,1409, June 2013  

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +guided 5,400

  

[![](img/t0_guided.jpg)](img/f0_guided.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +guided 5,400**

[![](img/t1_guided.jpg)](img/f1_guided.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +guided 5,400**

---

# Command: haar
**Category:** Filtering
**Source:** https://gmic.eu/reference/haar.html#top

# haar

## Arguments:

* scale>0

## Description:

Compute the direct haar multiscale wavelet transform of selected images.  

## See also:

[ihaar](ihaar.html).

This command has a [tutorial page](https://gmic.eu/oldtutorial/_haar).

---

# Command: heat_flow
**Category:** Filtering
**Source:** https://gmic.eu/reference/heat_flow.html#top

# heat\_flow

## Arguments:

* \_nb\_iter>=0,\_dt,\_keep\_sequence={ 0:No | 1:Yes }

## Description:

Apply iterations of the heat flow on selected images.  

## Default values:

nb\_iter=10, dt=30 and keep\_sequence=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +heat\_flow 20

  

[![](img/t0_heat_flow.jpg)](img/f0_heat_flow.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +heat\_flow 20**

[![](img/t1_heat_flow.jpg)](img/f1_heat_flow.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +heat\_flow 20**

---

# Command: hessian
**Category:** Filtering
**Source:** https://gmic.eu/reference/hessian.html#top

# hessian

## Arguments:

* { xx | xy | xz | yy | yz | zz }...{ xx | xy | xz | yy | yz | zz },\_boundary\_conditions    or
* (no arg) :

## Description:

Compute the hessian components (second derivatives) of selected images along specified axes.  
  
boundary\_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.  
(no arg) compute all significant components.  

## Default values:

boundary\_conditions=1.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> hessian

  

[![](img/t0_hessian.jpg)](img/f0_hessian.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> hessian**

[![](img/t1_hessian.jpg)](img/f1_hessian.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> hessian**

[![](img/t2_hessian.jpg)](img/f2_hessian.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> hessian**

---

# Command: idct
**Category:** Filtering
**Source:** https://gmic.eu/reference/idct.html#top

# idct

## Arguments:

* \_{ x | y | z }...{ x | y | z }    or
* (no arg)

## Description:

Compute the inverse discrete cosine transform of selected images, optionally along the specified axes only.  
  
Output images are always evenly sized, so this command may change the size of the selected images.  
(dct images obtained with the dct command are evenly sized anyway).  

## Default values:

(no arg)

## See also:

[dct](dct.html).

This command has a [tutorial page](https://gmic.eu/oldtutorial/_dct-and-idct).

---

# Command: iee
**Category:** Filtering
**Source:** https://gmic.eu/reference/iee.html#top

# iee

### No argumentsDescription:Compute gradient-orthogonal-directed 2nd derivative of image(s). Example of use: <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> iee Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> iee**

---

# Command: ifft
**Category:** Filtering
**Source:** https://gmic.eu/reference/ifft.html#top

|  |  |
| --- | --- |
| ifft | Built-in command |

## Arguments:

* \_{ x | y | z }...{ x | y | z }

## Description:

Compute the inverse fourier transform (real and imaginary parts) of selected images.  
  
optionally along the specified axes only.  

## See also:

[fft](fft.html).

This command has a [tutorial page](https://gmic.eu/oldtutorial/_fft).

---

# Command: ihaar
**Category:** Filtering
**Source:** https://gmic.eu/reference/ihaar.html#top

# ihaar

## Arguments:

* scale>0

## Description:

Compute the inverse haar multiscale wavelet transform of selected images.  

## See also:

[haar](haar.html).

This command has a [tutorial page](https://gmic.eu/oldtutorial/_haar).

---

# Command: ilaplacian
**Category:** Filtering
**Source:** https://gmic.eu/reference/ilaplacian.html#top

# ilaplacian

## Arguments:

* { nb\_iterations>0 | 0 },\_[initial\_estimate]

## Description:

Invert selected Laplacian images.  
  
If given nb\_iterations is 0, inversion is done in Fourier space (single iteration),  
otherwise, by applying nb\_iterations of a Laplacian-inversion PDE flow.  
Note that the resulting inversions are just estimation of possible/approximated solutions.  

## Default values:

nb\_iterations=0, axes=(undefined) and [initial\_estimated]=(undefined).

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +laplacian +ilaplacian[-1] 0

  

[![](img/t0_ilaplacian.jpg)](img/f0_ilaplacian.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +laplacian +ilaplacian[-1] 0**

[![](img/t1_ilaplacian.jpg)](img/f1_ilaplacian.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +laplacian +ilaplacian[-1] 0**

[![](img/t2_ilaplacian.jpg)](img/f2_ilaplacian.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +laplacian +ilaplacian[-1] 0**

---

# Command: inn
**Category:** Filtering
**Source:** https://gmic.eu/reference/inn.html#top

# inn

### No argumentsDescription:Compute gradient-directed 2nd derivative of image(s). Example of use: <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> inn Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> inn**

---

# Command: inpaint
**Category:** Filtering
**Source:** https://gmic.eu/reference/inpaint.html#top

|  |  |
| --- | --- |
| inpaint | Built-in command |

## Arguments:

* [mask]    or
* [mask],0,\_fast\_method    or
* [mask],\_patch\_size>=1,\_lookup\_size>=1,\_lookup\_factor>=0,\_lookup\_increment!=0,\_blend\_size>=0,0<=\_blend\_threshold<=1,\_blend\_decay>=0,\_blend\_scales>=1,\_is\_blend\_outer={ 0:No | 1:Yes }

## Description:

Inpaint selected images by specified mask.  
  
If no patch size (or 0) is specified, inpainting is done using a fast average or median algorithm.  
Otherwise, it used a patch-based reconstruction method, that can be very time consuming.  
fast\_method can be { 0:Low-connectivity average | 1:High-connectivity average | 2:Low-connectivity median | 3:High-connectivity median }.  

## Default values:

patch\_size=0, fast\_method=1, lookup\_size=22, lookup\_factor=0.5, lookup\_increment=1, blend\_size=0, blend\_threshold=0, blend\_decay=0.05, blend\_scales=10 and is\_blend\_outer=1.

## Examples of use:

### • Example #1

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> 100%,100% ellipse 50%,50%,30,30,0,1,255 ellipse 20%,20%,30,10,0,1,255 +inpaint[-2] [-1] remove[-2]

  

[![](img/t0_inpaint.jpg)](img/f0_inpaint.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> 100%,100% ellipse 50%,50%,30,30,0,1,255 ellipse 20%,20%,30,10,0,1,255 +inpaint[-2] [-1] remove[-2]**

[![](img/t1_inpaint.jpg)](img/f1_inpaint.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> 100%,100% ellipse 50%,50%,30,30,0,1,255 ellipse 20%,20%,30,10,0,1,255 +inpaint[-2] [-1] remove[-2]**

### • Example #2

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> 100%,100% circle 30%,30%,30,1,255,0,255 circle 70%,70%,50,1,255,0,255 +inpaint[0] [1],5,15,0.5,1,9,0 remove[1]

  

[![](img/t0_inpaint_2.jpg)](img/f0_inpaint_2.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> 100%,100% circle 30%,30%,30,1,255,0,255 circle 70%,70%,50,1,255,0,255 +inpaint[0] [1],5,15,0.5,1,9,0 remove[1]**

[![](img/t1_inpaint_2.jpg)](img/f1_inpaint_2.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> 100%,100% circle 30%,30%,30,1,255,0,255 circle 70%,70%,50,1,255,0,255 +inpaint[0] [1],5,15,0.5,1,9,0 remove[1]**

---

# Command: inpaint_pde
**Category:** Filtering
**Source:** https://gmic.eu/reference/inpaint_pde.html#top

# inpaint\_pde

## Arguments:

* [mask],\_nb\_scales[%],\_diffusion\_type={ 0:Isotropic | 1:Delaunay-guided | 2:Edge-guided | 3:Mask-guided },\_diffusion\_iter>=0

## Description:

Inpaint selected images by specified mask using a multiscale transport-diffusion algorithm.  
  
Argument nb\_scales sets the number of scales used in the multi-scale resolution scheme.  

When the % qualifier is used for nb\_scales, the number of used scales is relative to nb\_scales\_max = ceil(log2(max(w,h,d))).

When nb\_scales<0, it determines the minimum image size encountered at the lowest scale.

If diffusion\_type==3, non-zero values of the mask (e.g. a distance function) are used  
to guide the diffusion process.  

## Default values:

nb\_scales=-9, diffusion\_type=1 and diffusion\_iter=20.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> 100%,100% ellipse[-1] 30%,30%,40,30,0,1,255 +inpaint\_pde[0] [1]

  

[![](img/t0_inpaint_pde.jpg)](img/f0_inpaint_pde.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> 100%,100% ellipse[-1] 30%,30%,40,30,0,1,255 +inpaint\_pde[0] [1]**

[![](img/t1_inpaint_pde.jpg)](img/f1_inpaint_pde.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> 100%,100% ellipse[-1] 30%,30%,40,30,0,1,255 +inpaint\_pde[0] [1]**

[![](img/t2_inpaint_pde.jpg)](img/f2_inpaint_pde.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> 100%,100% ellipse[-1] 30%,30%,40,30,0,1,255 +inpaint\_pde[0] [1]**

---

# Command: inpaint_flow
**Category:** Filtering
**Source:** https://gmic.eu/reference/inpaint_flow.html#top

# inpaint\_flow

## Arguments:

* [mask],\_nb\_global\_iter>=0,\_nb\_local\_iter>=0,\_dt>0,\_alpha>=0,\_sigma>=0

## Description:

Apply iteration of the inpainting flow on selected images.  

## Default values:

nb\_global\_iter=10, nb\_local\_iter=100, dt=5, alpha=1 and sigma=3.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> 100%,100% ellipse[-1] 30%,30%,40,30,0,1,255 inpaint\_flow[0] [1]

  

[![](img/t0_inpaint_flow.jpg)](img/f0_inpaint_flow.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> 100%,100% ellipse[-1] 30%,30%,40,30,0,1,255 inpaint\_flow[0] [1]**

[![](img/t1_inpaint_flow.jpg)](img/f1_inpaint_flow.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> 100%,100% ellipse[-1] 30%,30%,40,30,0,1,255 inpaint\_flow[0] [1]**

---

# Command: inpaint_holes
**Category:** Filtering
**Source:** https://gmic.eu/reference/inpaint_holes.html#top

# inpaint\_holes

## Arguments:

* maximal\_area[%]>=0,\_tolerance>=0,\_is\_high\_connectivity={ 0:No | 1:Yes }

## Description:

Inpaint all connected regions having an area less than specified value.  

## Default values:

maximal\_area=4, tolerance=0 and is\_high\_connectivity=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> noise 5%,2 +inpaint\_holes 8,40

  

[![](img/t0_inpaint_holes.jpg)](img/f0_inpaint_holes.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> noise 5%,2 +inpaint\_holes 8,40**

[![](img/t1_inpaint_holes.jpg)](img/f1_inpaint_holes.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> noise 5%,2 +inpaint\_holes 8,40**

---

# Command: inpaint_morpho
**Category:** Filtering
**Source:** https://gmic.eu/reference/inpaint_morpho.html#top

# inpaint\_morpho

## Arguments:

* [mask]

## Description:

Inpaint selected images by specified mask using morphological operators.  

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> 100%,100% ellipse[-1] 30%,30%,40,30,0,1,255 +inpaint\_morpho[0] [1]

  

[![](img/t0_inpaint_morpho.jpg)](img/f0_inpaint_morpho.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> 100%,100% ellipse[-1] 30%,30%,40,30,0,1,255 +inpaint\_morpho[0] [1]**

[![](img/t1_inpaint_morpho.jpg)](img/f1_inpaint_morpho.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> 100%,100% ellipse[-1] 30%,30%,40,30,0,1,255 +inpaint\_morpho[0] [1]**

[![](img/t2_inpaint_morpho.jpg)](img/f2_inpaint_morpho.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> 100%,100% ellipse[-1] 30%,30%,40,30,0,1,255 +inpaint\_morpho[0] [1]**

---

# Command: inpaint_matchpatch
**Category:** Filtering
**Source:** https://gmic.eu/reference/inpaint_matchpatch.html#top

# inpaint\_matchpatch

## Arguments:

* [mask],\_nb\_scales={ 0:Auto | >0 },\_patch\_size>0,\_nb\_iterations\_per\_scale>0,\_blend\_size>=0,\_allow\_outer\_blending={ 0:No | 1:Yes },\_is\_already\_initialized={ 0:No | 1:Yes }

## Description:

Inpaint selected images by specified binary mask, using a multi-scale matchpatch algorithm.  

## Default values:

nb\_scales=0, patch\_size=9, nb\_iterations\_per\_scale=10, blend\_size=5,allow\_outer\_blending=1 and is\_already\_initialized=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> 100%,100% ellipse[-1] 30%,30%,40,30,0,1,255 +inpaint\_matchpatch[0] [1]

  

[![](img/t0_inpaint_matchpatch.jpg)](img/f0_inpaint_matchpatch.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> 100%,100% ellipse[-1] 30%,30%,40,30,0,1,255 +inpaint\_matchpatch[0] [1]**

[![](img/t1_inpaint_matchpatch.jpg)](img/f1_inpaint_matchpatch.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> 100%,100% ellipse[-1] 30%,30%,40,30,0,1,255 +inpaint\_matchpatch[0] [1]**

[![](img/t2_inpaint_matchpatch.jpg)](img/f2_inpaint_matchpatch.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> 100%,100% ellipse[-1] 30%,30%,40,30,0,1,255 +inpaint\_matchpatch[0] [1]**

---

# Command: kuwahara
**Category:** Filtering
**Source:** https://gmic.eu/reference/kuwahara.html#top

# kuwahara

## Arguments:

* size>0

## Description:

Apply Kuwahara filter of specified size on selected images.  

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> kuwahara 9

  
[![](img/t_kuwahara.jpg)](img/f_kuwahara.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> kuwahara 9**

---

# Command: laplacian
**Category:** Filtering
**Source:** https://gmic.eu/reference/laplacian.html#top

# laplacian

### No argumentsDescription:Compute Laplacian of selected images. Example of use: <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> laplacian Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> laplacian**

---

# Command: lic
**Category:** Filtering
**Source:** https://gmic.eu/reference/lic.html#top

# lic

## Arguments:

* \_amplitude>0,\_channels>0

## Description:

Render LIC representation of selected vector fields.  

## Default values:

amplitude=30 and channels=1.

## Example of use:

400,400,1,2,'!c?x-w/2:y-h/2' +lic 200,3 quiver[-2] [-2],10,1,1,1,255

  

[![](img/t0_lic.jpg)](img/f0_lic.jpg)

Command: **400,400,1,2,'!c?x-w/2:y-h/2' +lic 200,3 quiver[-2] [-2],10,1,1,1,255**

[![](img/t1_lic.jpg)](img/f1_lic.jpg)

Command: **400,400,1,2,'!c?x-w/2:y-h/2' +lic 200,3 quiver[-2] [-2],10,1,1,1,255**

---

# Command: map_tones
**Category:** Filtering
**Source:** https://gmic.eu/reference/map_tones.html#top

# map\_tones

## Arguments:

* \_threshold>=0,\_gamma>=0,\_smoothness>=0,nb\_iter>=0

## Description:

Apply tone mapping operator on selected images, based on Poisson equation.  

## Default values:

threshold=0.1, gamma=0.8, smoothness=0.5 and nb\_iter=30.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +map\_tones ,

  

[![](img/t0_map_tones.jpg)](img/f0_map_tones.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +map\_tones ,**

[![](img/t1_map_tones.jpg)](img/f1_map_tones.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +map\_tones ,**

---

# Command: map_tones_fast
**Category:** Filtering
**Source:** https://gmic.eu/reference/map_tones_fast.html#top

# map\_tones\_fast

## Arguments:

* \_radius[%]>=0,\_power>=0

## Description:

Apply fast tone mapping operator on selected images.  

## Default values:

radius=3% and power=0.3.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +map\_tones\_fast ,

  

[![](img/t0_map_tones_fast.jpg)](img/f0_map_tones_fast.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +map\_tones\_fast ,**

[![](img/t1_map_tones_fast.jpg)](img/f1_map_tones_fast.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +map\_tones\_fast ,**

---

# Command: meancurvature_flow
**Category:** Filtering
**Source:** https://gmic.eu/reference/meancurvature_flow.html#top

# meancurvature\_flow

## Arguments:

* \_nb\_iter>=0,\_dt,\_keep\_sequence={ 0:No | 1:Yes }

## Description:

Apply iterations of the mean curvature flow on selected images.  

## Default values:

nb\_iter=10, dt=30 and keep\_sequence=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +meancurvature\_flow 20

  

[![](img/t0_meancurvature_flow.jpg)](img/f0_meancurvature_flow.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +meancurvature\_flow 20**

[![](img/t1_meancurvature_flow.jpg)](img/f1_meancurvature_flow.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +meancurvature\_flow 20**

---

# Command: median
**Category:** Filtering
**Source:** https://gmic.eu/reference/median.html#top

|  |  |
| --- | --- |
| median | Built-in command |

## Arguments:

* size>=0,\_threshold>0

## Description:

Apply (opt. thresholded) median filter on selected images with structuring element size x size.  

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +median 5

  

[![](img/t0_median.jpg)](img/f0_median.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +median 5**

[![](img/t1_median.jpg)](img/f1_median.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +median 5**

---

# Command: merge_alpha
**Category:** Filtering
**Source:** https://gmic.eu/reference/merge_alpha.html#top

# merge\_alpha

### No argumentsDescription:Merge selected alpha detail scales into a single image. Alpha detail scales have been obtained with command [split\_alpha](split_alpha.html).

---

# Command: nlmeans
**Category:** Filtering
**Source:** https://gmic.eu/reference/nlmeans.html#top

# nlmeans

## Arguments:

* [guide],\_patch\_radius>0,\_spatial\_bandwidth>0,\_tonal\_bandwidth>0,\_patch\_measure\_command    or
* \_patch\_radius>0,\_spatial\_bandwidth>0,\_tonal\_bandwidth>0,\_patch\_measure\_command

## Description:

Apply non local means denoising of Buades et al, 2005. on selected images.  
  
The patch is a gaussian function of std\_patch\_radius.  
The spatial kernel is a rectangle of radius spatial\_bandwidth.  
The tonal kernel is exponential (exp(-d^2/\_tonal\_bandwidth^2))  
with d the euclidean distance between image patches.  

## Default values:

patch\_radius=4, spatial\_bandwidth=4, tonal\_bandwidth=10 and patch\_measure\_command=-norm.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +noise 10 nlmeans[-1] 4,4,{0.6\*${-std\_noise}}

  

[![](img/t0_nlmeans.jpg)](img/f0_nlmeans.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +noise 10 nlmeans[-1] 4,4,{0.6\*${-std\_noise}}**

[![](img/t1_nlmeans.jpg)](img/f1_nlmeans.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +noise 10 nlmeans[-1] 4,4,{0.6\*${-std\_noise}}**

---

# Command: nlmeans_core
**Category:** Filtering
**Source:** https://gmic.eu/reference/nlmeans_core.html#top

# nlmeans\_core

## Arguments:

* \_reference\_image,\_scaling\_map,\_patch\_radius>0,\_spatial\_bandwidth>0

## Description:

Apply non local means denoising using a image for weight and a map for scaling

---

# Command: normalize_local
**Category:** Filtering
**Source:** https://gmic.eu/reference/normalize_local.html#top

# normalize\_local

## Arguments:

* \_amplitude>=0,\_radius>0,\_n\_smooth[%]>=0,\_a\_smooth[%]>=0,\_is\_cut={ 0:No | 1:Yes },\_min=0,\_max=255

## Description:

Normalize selected images locally.  

## Default values:

amplitude=3, radius=16, n\_smooth=4%, a\_smooth=2%, is\_cut=1, min=0 and max=255.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> normalize\_local 8,10

  
[![](img/t_normalize_local.jpg)](img/f_normalize_local.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> normalize\_local 8,10**

---

# Command: normalized_cross_correlation
**Category:** Filtering
**Source:** https://gmic.eu/reference/normalized_cross_correlation.html#top

# normalized\_cross\_correlation

## Arguments:

* [mask]

## Description:

Compute normalized cross-correlation of selected images with specified mask.  

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +shift -30,-20 +normalized\_cross\_correlation[0] [1]

  

[![](img/t0_normalized_cross_correlation.jpg)](img/f0_normalized_cross_correlation.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +shift -30,-20 +normalized\_cross\_correlation[0] [1]**

[![](img/t1_normalized_cross_correlation.jpg)](img/f1_normalized_cross_correlation.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +shift -30,-20 +normalized\_cross\_correlation[0] [1]**

[![](img/t2_normalized_cross_correlation.jpg)](img/f2_normalized_cross_correlation.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +shift -30,-20 +normalized\_cross\_correlation[0] [1]**

---

# Command: opening
**Category:** Filtering
**Source:** https://gmic.eu/reference/opening.html#top

# opening

## Arguments:

* size>=0    or
* size\_x>=0,size\_y>=0,\_size\_z>=0    or
* [kernel],\_boundary\_conditions,\_is\_real={ 0:Binary-mode | 1:Real-mode }

## Description:

Apply morphological opening to selected images.  
  
boundary\_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.  

## Default values:

size\_z=1, boundary\_conditions=1 and is\_real=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +opening 10

  

[![](img/t0_opening.jpg)](img/f0_opening.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +opening 10**

[![](img/t1_opening.jpg)](img/f1_opening.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +opening 10**

---

# Command: opening_circ
**Category:** Filtering
**Source:** https://gmic.eu/reference/opening_circ.html#top

# opening\_circ

## Arguments:

* \_size>=0,\_is\_real={ 0:No | 1:Yes }

## Description:

Apply circular opening of selected images by specified size.  

## Default values:

boundary\_conditions=1 and is\_real=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +opening\_circ 7

  

[![](img/t0_opening_circ.jpg)](img/f0_opening_circ.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +opening\_circ 7**

[![](img/t1_opening_circ.jpg)](img/f1_opening_circ.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +opening\_circ 7**

---

# Command: percentile
**Category:** Filtering
**Source:** https://gmic.eu/reference/percentile.html#top

# percentile

## Arguments:

* [mask],0<=\_min\_percentile[%]<=100,0<=\_max\_percentile[%]<=100.

## Description:

Apply percentile averaging filter to selected images.  

## Default values:

min\_percentile=0 and max\_percentile=100.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> shape\_circle 11,11 +percentile[0] [1],25,75

  

[![](img/t0_percentile.jpg)](img/f0_percentile.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> shape\_circle 11,11 +percentile[0] [1],25,75**

[![](img/t1_percentile.jpg)](img/f1_percentile.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> shape\_circle 11,11 +percentile[0] [1],25,75**

[![](img/t2_percentile.jpg)](img/f2_percentile.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> shape\_circle 11,11 +percentile[0] [1],25,75**

---

# Command: peronamalik_flow
**Category:** Filtering
**Source:** https://gmic.eu/reference/peronamalik_flow.html#top

# peronamalik\_flow

## Arguments:

* K\_factor>0,\_nb\_iter>=0,\_dt,\_keep\_sequence={ 0:No | 1:Yes }

## Description:

Apply iterations of the Perona-Malik flow on selected images.  

## Default values:

K\_factor=20, nb\_iter=5, dt=5 and keep\_sequence=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +heat\_flow 20

  

[![](img/t0_peronamalik_flow.jpg)](img/f0_peronamalik_flow.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +heat\_flow 20**

[![](img/t1_peronamalik_flow.jpg)](img/f1_peronamalik_flow.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +heat\_flow 20**

---

# Command: phase_correlation
**Category:** Filtering
**Source:** https://gmic.eu/reference/phase_correlation.html#top

# phase\_correlation

## Arguments:

* [destination]

## Description:

Estimate translation vector between selected source images and specified destination.  

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +shift -30,-20 +phase\_correlation[0] [1] unroll[-1] y

  

[![](img/t0_phase_correlation.jpg)](img/f0_phase_correlation.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +shift -30,-20 +phase\_correlation[0] [1] unroll[-1] y**

[![](img/t1_phase_correlation.jpg)](img/f1_phase_correlation.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +shift -30,-20 +phase\_correlation[0] [1] unroll[-1] y**

[![](img/t2_phase_correlation.jpg)](img/f2_phase_correlation.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +shift -30,-20 +phase\_correlation[0] [1] unroll[-1] y**

---

# Command: pde_flow
**Category:** Filtering
**Source:** https://gmic.eu/reference/pde_flow.html#top

# pde\_flow

## Arguments:

* \_nb\_iter>=0,\_dt,\_velocity\_command,\_keep\_sequence={ 0:No | 1:Yes }

## Description:

Apply iterations of a generic PDE flow on selected images.  

## Default values:

nb\_iter=10, dt=30, velocity\_command=laplacian and keep\_sequence=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +pde\_flow 20

  

[![](img/t0_pde_flow.jpg)](img/f0_pde_flow.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +pde\_flow 20**

[![](img/t1_pde_flow.jpg)](img/f1_pde_flow.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +pde\_flow 20**

---

# Command: periodize_poisson
**Category:** Filtering
**Source:** https://gmic.eu/reference/periodize_poisson.html#top

# periodize\_poisson

### No argumentsDescription:Periodize selected images using a Poisson solver in Fourier space. Example of use: <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +periodize\_poisson array 2,2,2 Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +periodize\_poisson array 2,2,2** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +periodize\_poisson array 2,2,2**

---

# Command: rbf
**Category:** Filtering
**Source:** https://gmic.eu/reference/rbf.html#top

# rbf

## Arguments:

* dx,\_x0,\_x1,\_phi(r)    or
* dx,dy,\_x0,\_y0,\_x1,\_y1,\_phi(r)    or
* dx,dy,dz,x0,y0,z0,x1,y1,z1,phi(r)

## Description:

Reconstruct 1D/2D or 3D image from selected sets of keypoints, by RBF-interpolation.  
  
A set of keypoints is represented by a vector-valued image, where each pixel represents a single keypoint.  
Vector components of a keypoint have the following meaning:  

For 1D reconstruction: [ x\_k, f1(x\_k),...fN(x\_k) ].

For 2D reconstruction: [ x\_k,y\_k, f1(x\_k,y\_k),...,fN(x\_k,y\_k) ].

For 3D reconstruction: [ x\_k,y\_k,z\_k, f1(x\_k,y\_k,z\_k),...,fN(x\_k,y\_k,z\_k) ].

Values x\_k,y\_k and z\_k are the spatial coordinates of keypoint k.  
Values f1(),..,fN() are the N components of the vector value of keypoint k.  
The command reconstructs an image with specified size dx'x'dy'x'dz, with N channels.  

## Default values:

x0=y0=z0=0, x1=dx-1, y1=dy-1, z1=dz-1, phi(r)=r\*log(1+r).

## Examples of use:

### • Example #1

sample colorful,400 100%,100% noise\_poissondisk. 10 1,{is},1,5 eval[-2] "begin(p=0);i?(I[#-1,p++]=[x,y,I(#0)])" to\_rgb[1] mul[0,1] dilate\_circ[0] 5 +rbf[-1] {0,[w,h]} c[-1] 0,255

  

[![](img/t0_rbf.jpg)](img/f0_rbf.jpg)

Command: **sample colorful,400 100%,100% noise\_poissondisk. 10 1,{is},1,5 eval[-2] "begin(p=0);i?(I[#-1,p++]=[x,y,I(#0)])" to\_rgb[1] mul[0,1] dilate\_circ[0] 5 +rbf[-1] {0,[w,h]} c[-1] 0,255**

[![](img/t1_rbf.jpg)](img/f1_rbf.jpg)

Command: **sample colorful,400 100%,100% noise\_poissondisk. 10 1,{is},1,5 eval[-2] "begin(p=0);i?(I[#-1,p++]=[x,y,I(#0)])" to\_rgb[1] mul[0,1] dilate\_circ[0] 5 +rbf[-1] {0,[w,h]} c[-1] 0,255**

[![](img/t2_rbf.jpg)](img/f2_rbf.jpg)

Command: **sample colorful,400 100%,100% noise\_poissondisk. 10 1,{is},1,5 eval[-2] "begin(p=0);i?(I[#-1,p++]=[x,y,I(#0)])" to\_rgb[1] mul[0,1] dilate\_circ[0] 5 +rbf[-1] {0,[w,h]} c[-1] 0,255**

### • Example #2

32,1,1,5,u([400,400,255,255,255]) rbf 400,400 c 0,255

  
[![](img/t_rbf_2.jpg)](img/f_rbf_2.jpg)

Command: **32,1,1,5,u([400,400,255,255,255]) rbf 400,400 c 0,255**

---

# Command: red_eye
**Category:** Filtering
**Source:** https://gmic.eu/reference/red_eye.html#top

# red\_eye

## Arguments:

* 0<=\_threshold<=100,\_smoothness>=0,0<=attenuation<=1

## Description:

Attenuate red-eye effect in selected images.  

## Default values:

threshold=75, smoothness=3.5 and attenuation=0.1.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +red\_eye ,

  

[![](img/t0_red_eye.jpg)](img/f0_red_eye.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +red\_eye ,**

[![](img/t1_red_eye.jpg)](img/f1_red_eye.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +red\_eye ,**

---

# Command: remove_hotpixels
**Category:** Filtering
**Source:** https://gmic.eu/reference/remove_hotpixels.html#top

# remove\_hotpixels

## Arguments:

* \_mask\_size>0, \_threshold[%]>0

## Description:

Remove hot pixels in selected images.  

## Default values:

mask\_size=3 and threshold=10%.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> noise 10,2 +remove\_hotpixels ,

  

[![](img/t0_remove_hotpixels.jpg)](img/f0_remove_hotpixels.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> noise 10,2 +remove\_hotpixels ,**

[![](img/t1_remove_hotpixels.jpg)](img/f1_remove_hotpixels.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> noise 10,2 +remove\_hotpixels ,**

---

# Command: remove_pixels
**Category:** Filtering
**Source:** https://gmic.eu/reference/remove_pixels.html#top

# remove\_pixels

## Arguments:

* number\_of\_pixels[%]>=0

## Description:

Remove specified number of pixels (i.e. set them to 0) from the set of non-zero pixels in selected images.  

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +remove\_pixels 50%

  

[![](img/t0_remove_pixels.jpg)](img/f0_remove_pixels.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +remove\_pixels 50%**

[![](img/t1_remove_pixels.jpg)](img/f1_remove_pixels.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +remove\_pixels 50%**

---

# Command: rolling_guidance
**Category:** Filtering
**Source:** https://gmic.eu/reference/rolling_guidance.html#top

# rolling\_guidance

## Arguments:

* std\_deviation\_s[%]>=0,std\_deviation\_r[%]>=0,\_precision>=0

## Description:

Apply the rolling guidance filter on selected image.  
  
Rolling guidance filter is a fast image abstraction filter, described in:  
"Rolling Guidance Filter", Qi Zhang Xiaoyong, Shen Li, Xu Jiaya Jia, ECCV'2014.  

## Default values:

std\_deviation\_s=4, std\_deviation\_r=10 and precision=0.5.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +rolling\_guidance , +-

  

[![](img/t0_rolling_guidance.jpg)](img/f0_rolling_guidance.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +rolling\_guidance , +-**

[![](img/t1_rolling_guidance.jpg)](img/f1_rolling_guidance.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +rolling\_guidance , +-**

[![](img/t2_rolling_guidance.jpg)](img/f2_rolling_guidance.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +rolling\_guidance , +-**

---

# Command: sharpen
**Category:** Filtering
**Source:** https://gmic.eu/reference/sharpen.html#top

# sharpen

## Arguments:

* amplitude>=0    or
* amplitude>=0,edge>=0,\_alpha[%],\_sigma[%]

## Description:

Sharpen selected images by inverse diffusion or shock filters methods.  
  
edge must be specified to enable shock-filter method.  

## Default values:

edge=0, alpha=0 and sigma=0.

## Examples of use:

### • Example #1

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> sharpen 300

  
[![](img/t_sharpen.jpg)](img/f_sharpen.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> sharpen 300**

### • Example #2

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> blur 5 sharpen 300,1

  
[![](img/t_sharpen_2.jpg)](img/f_sharpen_2.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> blur 5 sharpen 300,1**

---

# Command: sharpen_alpha
**Category:** Filtering
**Source:** https://gmic.eu/reference/sharpen_alpha.html#top

# sharpen\_alpha

## Arguments:

* \_amplitude[%]>=0,\_nb\_scales>0,0<=\_anisotropy<=1,0<=\_minimize\_alpha<=1

## Description:

Sharpen selected images using a multi-scale and alpha boosting algorithm.  

## Default values:

amplitude=1, nb\_scales=5, anisotropy=0 and minimize\_alpha=1.

---

# Command: smooth
**Category:** Filtering
**Source:** https://gmic.eu/reference/smooth.html#top

|  |  |
| --- | --- |
| smooth | Built-in command |

## Arguments:

* amplitude[%]>=0,\_sharpness>=0,0<=\_anisotropy<=1,\_alpha[%],\_sigma[%],\_dl>0,\_da>0,\_precision>0,\_interpolation,\_fast\_approx={ 0:No | 1:Yes }    or
* nb\_iterations>=0,\_sharpness>=0,\_anisotropy,\_alpha,\_sigma,\_dt>0,0    or
* [tensor\_field],\_amplitude>=0,\_dl>0,\_da>0,\_precision>0,\_interpolation,\_fast\_approx={ 0:No | 1:Yes }    or
* [tensor\_field],\_nb\_iters>=0,\_dt>0,0

## Description:

Smooth selected images anisotropically using diffusion PDE's, with specified field of  
  
diffusion tensors.  
interpolation can be { 0:Nearest | 1:Linear | 2:Runge-kutta }.  

## Default values:

sharpness=0.7, anisotropy=0.3, alpha=0.6, sigma=1.1, dl=0.8, da=30, precision=2, interpolation=0 and fast\_approx=1.

This command has a [tutorial page](https://gmic.eu/oldtutorial/_smooth).

## Examples of use:

### • Example #1

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> repeat 3 smooth 40,0,1,1,2 done

  
[![](img/t_smooth.jpg)](img/f_smooth.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> repeat 3 smooth 40,0,1,1,2 done**

### • Example #2

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> 100%,100%,1,2 rand[-1] -100,100 repeat 2 smooth[-1] 100,0.2,1,4,4 done warp[0] [-1],1,1,1

  

[![](img/t0_smooth_2.jpg)](img/f0_smooth_2.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> 100%,100%,1,2 rand[-1] -100,100 repeat 2 smooth[-1] 100,0.2,1,4,4 done warp[0] [-1],1,1,1**

[![](img/t1_smooth_2.jpg)](img/f1_smooth_2.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> 100%,100%,1,2 rand[-1] -100,100 repeat 2 smooth[-1] 100,0.2,1,4,4 done warp[0] [-1],1,1,1**

---

# Command: split_freq
**Category:** Filtering
**Source:** https://gmic.eu/reference/split_freq.html#top

# split\_freq

## Arguments:

* smoothness[%]>0

## Description:

Split selected images into low and high frequency parts.  

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> split\_freq 2%

  

[![](img/t0_split_freq.jpg)](img/f0_split_freq.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> split\_freq 2%**

[![](img/t1_split_freq.jpg)](img/f1_split_freq.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> split\_freq 2%**

---

# Command: solve_poisson
**Category:** Filtering
**Source:** https://gmic.eu/reference/solve_poisson.html#top

# solve\_poisson

## Arguments:

* "laplacian\_command",\_nb\_iterations>=0,\_time\_step>0,\_nb\_scales>=0

## Description:

Solve Poisson equation so that applying laplacian[n] is close to the result of laplacian\_command[n].  
  
Solving is performed using a multi-scale gradient descent algorithm.  
If nb\_scales=0, the number of scales is automatically determined.  

## Default values:

nb\_iterations=60, dt=5 and nb\_scales=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> command "foo : gradient x" +solve\_poisson foo +foo[0] +laplacian[1]

  

[![](img/t0_solve_poisson.jpg)](img/f0_solve_poisson.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> command "foo : gradient x" +solve\_poisson foo +foo[0] +laplacian[1]**

[![](img/t1_solve_poisson.jpg)](img/f1_solve_poisson.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> command "foo : gradient x" +solve\_poisson foo +foo[0] +laplacian[1]**

[![](img/t2_solve_poisson.jpg)](img/f2_solve_poisson.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> command "foo : gradient x" +solve\_poisson foo +foo[0] +laplacian[1]**

[![](img/t3_solve_poisson.jpg)](img/f3_solve_poisson.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> command "foo : gradient x" +solve\_poisson foo +foo[0] +laplacian[1]**

---

# Command: split_alpha
**Category:** Filtering
**Source:** https://gmic.eu/reference/split_alpha.html#top

# split\_alpha

## Arguments:

* \_nb\_scales[%]={ 0:Auto | -S<0 | N>0 },\_subsample={ 0:No | 1:Yes },0<=\_anisotropy<=1,0<=\_minimize\_alpha<=1

## Description:

Split selected images into alpha detail scales.  
  
If nb\_scales==-S, the lowest scale has a size of at least SxS.  
Parameter anisotropy is only considered when subsample=0.  
Image reconstruction is done with command [merge\_alpha](merge_alpha.html).  

## Default values:

nb\_scales=0, subsample=0, anisotropy=0 and minimize\_alpha=1.

---

# Command: split_details
**Category:** Filtering
**Source:** https://gmic.eu/reference/split_details.html#top

# split\_details

## Arguments:

* \_nb\_scales[%]={ 0:Auto | -S<0 | N>0 },\_base\_scale[%]>=0,\_detail\_scale[%]>=0

## Description:

Split selected images into nb\_scales detail scales.  
  
If base\_scale = detail\_scale = 0, the image decomposition is done with a trous wavelets.  
Otherwise, it uses laplacian pyramids with linear standard deviations.  

## Default values:

nb\_scales=0, base\_scale=0 and detail\_scale=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> split\_details ,

  

[![](img/t0_split_details.jpg)](img/f0_split_details.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> split\_details ,**

[![](img/t1_split_details.jpg)](img/f1_split_details.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> split\_details ,**

[![](img/t2_split_details.jpg)](img/f2_split_details.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> split\_details ,**

[![](img/t3_split_details.jpg)](img/f3_split_details.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> split\_details ,**

[![](img/t4_split_details.jpg)](img/f4_split_details.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> split\_details ,**

[![](img/t5_split_details.jpg)](img/f5_split_details.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> split\_details ,**

[![](img/t6_split_details.jpg)](img/f6_split_details.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> split\_details ,**

[![](img/t7_split_details.jpg)](img/f7_split_details.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> split\_details ,**

---

# Command: structuretensors
**Category:** Filtering
**Source:** https://gmic.eu/reference/structuretensors.html#top

# structuretensors

## Arguments:

* \_scheme={ 0:Centered | 1:Forward/backward }

## Description:

Compute the structure tensor field of selected images.  

## Default values:

scheme=0.

This command has a [tutorial page](https://gmic.eu/oldtutorial/_structuretensors).

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> structuretensors abs pow 0.2

  
[![](img/t_structuretensors.jpg)](img/f_structuretensors.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> structuretensors abs pow 0.2**

---

# Command: solidify
**Category:** Filtering
**Source:** https://gmic.eu/reference/solidify.html#top

# solidify

## Arguments:

* \_smoothness[%]>=0,\_diffusion\_type={ 0:Isotropic | 1:Delaunay-guided | 2:Edge-oriented },\_diffusion\_iter>=0

## Description:

Solidify selected transparent images.  

## Default values:

smoothness=75%, diffusion\_type=1 and diffusion\_iter=20.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> 100%,100% circle[-1] 50%,50%,25%,1,255 append c +solidify , display\_rgba

  

[![](img/t0_solidify.jpg)](img/f0_solidify.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> 100%,100% circle[-1] 50%,50%,25%,1,255 append c +solidify , display\_rgba**

[![](img/t1_solidify.jpg)](img/f1_solidify.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> 100%,100% circle[-1] 50%,50%,25%,1,255 append c +solidify , display\_rgba**

---

# Command: syntexturize
**Category:** Filtering
**Source:** https://gmic.eu/reference/syntexturize.html#top

# syntexturize

## Arguments:

* \_width[%]>0,\_height[%]>0

## Description:

Resynthetize width'x'height versions of selected micro-textures by phase randomization.  
  
The texture synthesis algorithm is a straightforward implementation of the method described in :  
<http://www.ipol.im/pub/art/2011/ggm_rpn/>.  

## Default values:

width=height=100%.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> crop 2,282,50,328 +syntexturize 320,320

  

[![](img/t0_syntexturize.jpg)](img/f0_syntexturize.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> crop 2,282,50,328 +syntexturize 320,320**

[![](img/t1_syntexturize.jpg)](img/f1_syntexturize.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> crop 2,282,50,328 +syntexturize 320,320**

---

# Command: syntexturize_matchpatch
**Category:** Filtering
**Source:** https://gmic.eu/reference/syntexturize_matchpatch.html#top

# syntexturize\_matchpatch

## Arguments:

* \_width[%]>0,\_height[%]>0,\_nb\_scales>=0,\_patch\_size>0,\_blending\_size>=0,\_precision>=0

## Description:

Resynthetize width'x'height versions of selected micro-textures using a patch-matching algorithm.  
  
If nbscales==0, the number of scales used is estimated from the image size.  

## Default values:

width=height=100%, nb\_scales=0, patch\_size=7, blending\_size=5 and precision=1.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> crop 25%,25%,75%,75% syntexturize\_matchpatch 512,512

  
[![](img/t_syntexturize_matchpatch.jpg)](img/f_syntexturize_matchpatch.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> crop 25%,25%,75%,75% syntexturize\_matchpatch 512,512**

---

# Command: tv_flow
**Category:** Filtering
**Source:** https://gmic.eu/reference/tv_flow.html#top

# tv\_flow

## Arguments:

* \_nb\_iter>=0,\_dt,\_keep\_sequence={ 0:No | 1:Yes }

## Description:

Apply iterations of the total variation flow on selected images.  

## Default values:

nb\_iter=10, dt=30 and keep\_sequence=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +tv\_flow 40

  

[![](img/t0_tv_flow.jpg)](img/f0_tv_flow.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +tv\_flow 40**

[![](img/t1_tv_flow.jpg)](img/f1_tv_flow.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +tv\_flow 40**

---

# Command: unsharp
**Category:** Filtering
**Source:** https://gmic.eu/reference/unsharp.html#top

# unsharp

## Arguments:

* radius[%]>=0,\_amount>=0,\_threshold[%]>=0

## Description:

Apply unsharp mask on selected images.  

## Default values:

amount=2 and threshold=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> blur 3 +unsharp 1.5,15 cut 0,255

  

[![](img/t0_unsharp.jpg)](img/f0_unsharp.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> blur 3 +unsharp 1.5,15 cut 0,255**

[![](img/t1_unsharp.jpg)](img/f1_unsharp.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> blur 3 +unsharp 1.5,15 cut 0,255**

---

# Command: unsharp_octave
**Category:** Filtering
**Source:** https://gmic.eu/reference/unsharp_octave.html#top

# unsharp\_octave

## Arguments:

* \_nb\_scales>0,\_radius[%]>=0,\_amount>=0,threshold[%]>=0

## Description:

Apply octave sharpening on selected images.  

## Default values:

nb\_scales=4, radius=1, amount=2 and threshold=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> blur 3 +unsharp\_octave 4,5,15 cut 0,255

  

[![](img/t0_unsharp_octave.jpg)](img/f0_unsharp_octave.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> blur 3 +unsharp\_octave 4,5,15 cut 0,255**

[![](img/t1_unsharp_octave.jpg)](img/f1_unsharp_octave.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> blur 3 +unsharp\_octave 4,5,15 cut 0,255**

---

# Command: vanvliet
**Category:** Filtering
**Source:** https://gmic.eu/reference/vanvliet.html#top

|  |  |
| --- | --- |
| vanvliet | Built-in command |

## Arguments:

* std\_deviation[%]>=0,order={ 0 | 1 | 2 | 3 },axis={ x | y | z | c },\_boundary\_conditions

## Description:

Apply Vanvliet recursive filter on selected images, along specified axis and with  
  
specified standard deviation, order and boundary conditions.  
boundary\_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.  

## Default values:

boundary\_conditions=1.

## Examples of use:

### • Example #1

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +vanvliet 3,1,x

  

[![](img/t0_vanvliet.jpg)](img/f0_vanvliet.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +vanvliet 3,1,x**

[![](img/t1_vanvliet.jpg)](img/f1_vanvliet.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +vanvliet 3,1,x**

### • Example #2

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +vanvliet 30,0,x vanvliet[-2] 30,0,y add

  
[![](img/t_vanvliet_2.jpg)](img/f_vanvliet_2.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +vanvliet 30,0,x vanvliet[-2] 30,0,y add**

---

# Command: voronoi
**Category:** Filtering
**Source:** https://gmic.eu/reference/voronoi.html#top

# voronoi

### No argumentsDescription:Compute the discrete Voronoi diagram of non-zero pixels in selected images. Example of use: 400,400 noise 0.2,2 eq 1 +label\_fg 0 voronoi[-1] +gradient[-1] xy,1 append[-2,-1] c norm[-1] ==[-1] 0 map[-2] 2,2 mul[-2,-1] normalize[-2] 0,255 dilate\_circ[-2] 4 reverse max Command: **400,400 noise 0.2,2 eq 1 +label\_fg 0 voronoi[-1] +gradient[-1] xy,1 append[-2,-1] c norm[-1] ==[-1] 0 map[-2] 2,2 mul[-2,-1] normalize[-2] 0,255 dilate\_circ[-2] 4 reverse max**

---

# Command: watermark_fourier
**Category:** Filtering
**Source:** https://gmic.eu/reference/watermark_fourier.html#top

# watermark\_fourier

## Arguments:

* text,\_size>0

## Description:

Add a textual watermark in the frequency domain of selected images.  

## Default values:

size=33.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +watermark\_fourier "Watermarked!" +display\_fft remove[-3,-1] normalize 0,255 append[-4,-2] y append[-2,-1] y

  

[![](img/t0_watermark_fourier.jpg)](img/f0_watermark_fourier.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +watermark\_fourier "Watermarked!" +display\_fft remove[-3,-1] normalize 0,255 append[-4,-2] y append[-2,-1] y**

[![](img/t1_watermark_fourier.jpg)](img/f1_watermark_fourier.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +watermark\_fourier "Watermarked!" +display\_fft remove[-3,-1] normalize 0,255 append[-4,-2] y append[-2,-1] y**

---

# Command: watershed
**Category:** Filtering
**Source:** https://gmic.eu/reference/watershed.html#top

|  |  |
| --- | --- |
| watershed | Built-in command |

## Arguments:

* [priority\_image],\_is\_high\_connectivity={ 0:No | 1:Yes }

## Description:

Compute the watershed transform of selected images.  

## Default values:

is\_high\_connectivity=1.

## Example of use:

400,400 noise 0.2,2 eq 1 +distance 1 mul[-1] -1 label[-2] watershed[-2] [-1] mod[-2] 256 map[-2] 0 reverse

  

[![](img/t0_watershed.jpg)](img/f0_watershed.jpg)

Command: **400,400 noise 0.2,2 eq 1 +distance 1 mul[-1] -1 label[-2] watershed[-2] [-1] mod[-2] 256 map[-2] 0 reverse**

[![](img/t1_watershed.jpg)](img/f1_watershed.jpg)

Command: **400,400 noise 0.2,2 eq 1 +distance 1 mul[-1] -1 label[-2] watershed[-2] [-1] mod[-2] 256 map[-2] 0 reverse**

---

# Command: area
**Category:** Features Extraction
**Source:** https://gmic.eu/reference/area.html#top

# area

## Arguments:

* tolerance>=0,is\_high\_connectivity={ 0:No | 1:Yes }

## Description:

Compute area of connected components in selected images.  

## Default values:

is\_high\_connectivity=0.

This command has a [tutorial page](https://gmic.eu/oldtutorial/_area).

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> luminance stencil[-1] 1 +area 0

  

[![](img/t0_area.jpg)](img/f0_area.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> luminance stencil[-1] 1 +area 0**

[![](img/t1_area.jpg)](img/f1_area.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> luminance stencil[-1] 1 +area 0**

---

# Command: area_fg
**Category:** Features Extraction
**Source:** https://gmic.eu/reference/area_fg.html#top

# area\_fg

## Arguments:

* tolerance>=0,is\_high\_connectivity={ 0:No | 1:Yes }

## Description:

Compute area of connected components for non-zero values in selected images.  
  
Similar to area except that 0-valued pixels are not considered.  

## Default values:

is\_high\_connectivity=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> luminance stencil[-1] 1 +area\_fg 0

  

[![](img/t0_area_fg.jpg)](img/f0_area_fg.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> luminance stencil[-1] 1 +area\_fg 0**

[![](img/t1_area_fg.jpg)](img/f1_area_fg.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> luminance stencil[-1] 1 +area\_fg 0**

---

# Command: at_curve
**Category:** Features Extraction
**Source:** https://gmic.eu/reference/at_curve.html#top

# at\_curve

## Arguments:

* x0[%],y0[%],z0[%],...,xN[%],yn[%],zn[%]

## Description:

Retrieve pixels of the selected images belonging to the specified cubic spline curve that passes across the specified points.  

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +at\_curve 0,0,0,80%,50%,0,100%,100%,0

  

[![](img/t0_at_curve.jpg)](img/f0_at_curve.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +at\_curve 0,0,0,80%,50%,0,100%,100%,0**

[![](img/t1_at_curve.jpg)](img/f1_at_curve.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +at\_curve 0,0,0,80%,50%,0,100%,100%,0**

---

# Command: at_quadrangle
**Category:** Features Extraction
**Source:** https://gmic.eu/reference/at_quadrangle.html#top

# at\_quadrangle

## Arguments:

* x0[%],y0[%],x1[%],y1[%],x2[%],y2[%],x3[%],y3[%],\_interpolation,\_boundary\_conditions    or
* x0[%],y0[%],z0[%],x1[%],y1[%],z1[%],x2[%],y2[%],z2[%],x3[%],y3[%],z3[%],\_interpolation,\_boundary\_conditions

## Description:

Retrieve pixels of the selected images belonging to the specified 2D or 3D quadrangle.  
  
interpolation can be { 0:Nearest-neighbor | 1:Linear | 2:Cubic }.  
boundary\_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.  

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> params=5%,5%,95%,5%,60%,95%,40%,95% +at\_quadrangle $params polygon.. 4,$params,0.5,255

  

[![](img/t0_at_quadrangle.jpg)](img/f0_at_quadrangle.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> params=5%,5%,95%,5%,60%,95%,40%,95% +at\_quadrangle $params polygon.. 4,$params,0.5,255**

[![](img/t1_at_quadrangle.jpg)](img/f1_at_quadrangle.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> params=5%,5%,95%,5%,60%,95%,40%,95% +at\_quadrangle $params polygon.. 4,$params,0.5,255**

---

# Command: barycenter
**Category:** Features Extraction
**Source:** https://gmic.eu/reference/barycenter.html#top

# barycenter

### No argumentsDescription:Compute the barycenter vector of pixel values. Example of use: 256,256 ellipse 50%,50%,20%,20%,0,1,1 deform 20 +barycenter +ellipse[-2] {@0,1},5,5,0,10 Command: **256,256 ellipse 50%,50%,20%,20%,0,1,1 deform 20 +barycenter +ellipse[-2] {@0,1},5,5,0,10** Command: **256,256 ellipse 50%,50%,20%,20%,0,1,1 deform 20 +barycenter +ellipse[-2] {@0,1},5,5,0,10** Command: **256,256 ellipse 50%,50%,20%,20%,0,1,1 deform 20 +barycenter +ellipse[-2] {@0,1},5,5,0,10**

---

# Command: betti
**Category:** Features Extraction
**Source:** https://gmic.eu/reference/betti.html#top

# betti

### No argumentsDescription:Compute Betti numbers B0,B1 and B2 from selected 3D binary shapes. Values B0,B1 and B2 are returned in the status. When multiple images are selected, the B0,B1,B2 of each image are concatenated in the status. (see https://en.wikipedia.org/wiki/Betti\_number for details about Betti numbers).

---

# Command: canny
**Category:** Features Extraction
**Source:** https://gmic.eu/reference/canny.html#top

# canny

## Arguments:

* \_sigma[%]>=0,\_low\_threshold>=0,\_high\_threshold>=0

## Description:

Locate image edges using Canny edge detector.  

## Default values:

sigma=1, low\_threshold=0.05, high\_threshold=0.15.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> canny 1

  
[![](img/t_canny.jpg)](img/f_canny.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> canny 1**

---

# Command: delaunay
**Category:** Features Extraction
**Source:** https://gmic.eu/reference/delaunay.html#top

# delaunay

## Arguments:

* \_output\_type={ 0:Image | 1:Coordinates/triangles }

## Description:

Generate discrete 2D Delaunay triangulation of non-zero pixels in selected images.  
  
Input images must be scalar.  
Each pixel of the output image is a triplet (a,b,c) meaning the pixel belongs to  
the Delaunay triangle ABC where a,b,c are the labels of the pixels A,B,C.  

## Examples of use:

### • Example #1

400,400 rand 32,255 100%,100% noise. 0.4,2 eq. 1 mul +delaunay

  

[![](img/t0_delaunay.jpg)](img/f0_delaunay.jpg)

Command: **400,400 rand 32,255 100%,100% noise. 0.4,2 eq. 1 mul +delaunay**

[![](img/t1_delaunay.jpg)](img/f1_delaunay.jpg)

Command: **400,400 rand 32,255 100%,100% noise. 0.4,2 eq. 1 mul +delaunay**

### • Example #2

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> 100%,100% noise. 2,2 eq. 1 delaunay. +blend shapeaverage0

  

[![](img/t0_delaunay_2.jpg)](img/f0_delaunay_2.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> 100%,100% noise. 2,2 eq. 1 delaunay. +blend shapeaverage0**

[![](img/t1_delaunay_2.jpg)](img/f1_delaunay_2.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> 100%,100% noise. 2,2 eq. 1 delaunay. +blend shapeaverage0**

[![](img/t2_delaunay_2.jpg)](img/f2_delaunay_2.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> 100%,100% noise. 2,2 eq. 1 delaunay. +blend shapeaverage0**

---

# Command: detect_skin
**Category:** Features Extraction
**Source:** https://gmic.eu/reference/detect_skin.html#top

# detect\_skin

## Arguments:

* 0<=tolerance<=1,\_skin\_x,\_skin\_y,\_skin\_radius>=0

## Description:

Detect skin in selected color images and output an appartenance probability map.  
  
Detection is performed using CbCr chromaticity data of skin pixels.  
If arguments skin\_x, skin\_y and skin\_radius are provided, skin pixels are learnt  
from the sample pixels inside the circle located at (skin\_x,skin\_y) with radius skin\_radius.  

## Default values:

tolerance=0.5 and skin\_x=skiny=radius=-1.

---

# Command: displacement
**Category:** Features Extraction
**Source:** https://gmic.eu/reference/displacement.html#top

|  |  |
| --- | --- |
| displacement | Built-in command |

## Arguments:

* [reference],\_smoothness>=0,\_precision>=0,\_nb\_scales>=0,\_iteration\_max>=0,mode={ 0:Backward | 1:Forward },\_[guide]

## Description:

Estimate displacement field between specified reference image and selected (target) images.  
  
If smoothness>=0, regularization type is set to isotropic, else to anisotropic.  
If nbscales==0, the number of scales used is estimated from the image size.  

## Default values:

smoothness=0.1, precision=7, nb\_scales=0, iteration\_max=1000, mode=0 and [guide]=(unused).

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +rotate 3,1,0,50%,50% +displacement[-1] [-2] quiver[-1] [-1],15,1,1,1,{1.5\*iM}

  

[![](img/t0_displacement.jpg)](img/f0_displacement.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +rotate 3,1,0,50%,50% +displacement[-1] [-2] quiver[-1] [-1],15,1,1,1,{1.5\*iM}**

[![](img/t1_displacement.jpg)](img/f1_displacement.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +rotate 3,1,0,50%,50% +displacement[-1] [-2] quiver[-1] [-1],15,1,1,1,{1.5\*iM}**

[![](img/t2_displacement.jpg)](img/f2_displacement.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +rotate 3,1,0,50%,50% +displacement[-1] [-2] quiver[-1] [-1],15,1,1,1,{1.5\*iM}**

---

# Command: distance
**Category:** Features Extraction
**Source:** https://gmic.eu/reference/distance.html#top

|  |  |
| --- | --- |
| distance | Built-in command |

## Arguments:

* isovalue[%],\_metric    or
* isovalue[%],[metric],\_method

## Description:

Compute the unsigned distance function to specified isovalue, opt. according to a custom metric.  
  
metric can be { 0:Chebyshev | 1:Manhattan | 2:Euclidean | 3:Squared-euclidean }.  
method can be { 0:Fast-marching | 1:Low-connectivity dijkstra | 2:High-connectivity dijkstra | 3:1+Return path | 4:2+Return path }.  

## Default values:

metric=2 and method=0.

This command has a [tutorial page](https://gmic.eu/oldtutorial/_distance).

## Examples of use:

### • Example #1

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> threshold 20% distance 0 pow 0.3

  
[![](img/t_distance.jpg)](img/f_distance.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> threshold 20% distance 0 pow 0.3**

### • Example #2

400,400 set 1,50%,50% +distance[0] 1,2 +distance[0] 1,1 distance[0] 1,0 mod 32 threshold 16 append c

  
[![](img/t_distance_2.jpg)](img/f_distance_2.jpg)

Command: **400,400 set 1,50%,50% +distance[0] 1,2 +distance[0] 1,1 distance[0] 1,0 mod 32 threshold 16 append c**

---

# Command: edgels
**Category:** Features Extraction
**Source:** https://gmic.eu/reference/edgels.html#top

# edgels

## Arguments:

* x0,y0,\_n0,\_is\_high\_connectivity={ 0:No | 1:Yes }

## Description:

Extract one or several lists of edgels (and their normals) that defines a 2D binary silhouette.  
  
When specified (i.e. !=-1), arguments x0,y0,n0 are the coordinates of the starting edgel, which must be located on an edge of the binary silhouette.  

If x0,y0 and n0 are specified, only a single list of edgels is returned.

If only x0,y0 are specified (meaning n0=-1), up to 4 lists of edgels can be returned, all starting from the same point (x0,y0).

If no arguments are specified (meaning x0=y0=n0=-1), all possible lists of edgels are returned.

A list of edgels is returned as an image with 3 channels [x,y,n] where x and y are the 2D coordinates of the edgel pixel, and n is the orientation of its associated canonical normal (which can be { 0:[1,0] | 1:[0,1] | 2:[-1,0] | 3:[0,-1] }.  

## Default values:

x0=y0=n0=-1 and is\_high\_connectivity=1.

---

# Command: edges
**Category:** Features Extraction
**Source:** https://gmic.eu/reference/edges.html#top

# edges

## Arguments:

* \_threshold[%]>=0

## Description:

Estimate contours of selected images.  

## Default values:

edges=15%

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +edges 15%

  

[![](img/t0_edges.jpg)](img/f0_edges.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +edges 15%**

[![](img/t1_edges.jpg)](img/f1_edges.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +edges 15%**

---

# Command: fftpolar
**Category:** Features Extraction
**Source:** https://gmic.eu/reference/fftpolar.html#top

# fftpolar

### No argumentsDescription:Compute fourier transform of selected images, as centered magnitude/phase images. Example of use: <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> fftpolar ellipse 50%,50%,10,10,0,1,0 ifftpolar Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> fftpolar ellipse 50%,50%,10,10,0,1,0 ifftpolar**

---

# Command: histogram
**Category:** Features Extraction
**Source:** https://gmic.eu/reference/histogram.html#top

|  |  |
| --- | --- |
| histogram | Built-in command |

## Arguments:

* nb\_levels[%]>0,\_min\_value[%],\_max\_value[%]

## Description:

Compute the histogram of selected images.  
  
If value range is set, the histogram is estimated only for pixels in the specified  
value range. Argument max\_value must be specified if min\_value is set.  

## Default values:

min\_value=0% and max\_value=100%.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +histogram 64 display\_graph[-1] 400,300,3

  

[![](img/t0_histogram.jpg)](img/f0_histogram.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +histogram 64 display\_graph[-1] 400,300,3**

[![](img/t1_histogram.jpg)](img/f1_histogram.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +histogram 64 display\_graph[-1] 400,300,3**

---

# Command: histogram_masked
**Category:** Features Extraction
**Source:** https://gmic.eu/reference/histogram_masked.html#top

# histogram\_masked

## Arguments:

* [mask],nb\_levels[%]>0,\_min\_value[%],\_max\_value[%]

## Description:

Compute the masked histogram of selected images.  

## Default values:

min\_value=0% and max\_value=100%.

---

# Command: histogram_nd
**Category:** Features Extraction
**Source:** https://gmic.eu/reference/histogram_nd.html#top

# histogram\_nd

## Arguments:

* nb\_levels[%]>0,\_value0[%],\_value1[%]

## Description:

Compute the 1D,2D or 3D histogram of selected multi-channels images (having 1,2 or 3 channels).  
  
If value range is set, the histogram is estimated only for pixels in the specified  
value range.  

## Default values:

value0=0% and value1=100%.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> channels 0,1 +histogram\_nd 256

  

[![](img/t0_histogram_nd.jpg)](img/f0_histogram_nd.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> channels 0,1 +histogram\_nd 256**

[![](img/t1_histogram_nd.jpg)](img/f1_histogram_nd.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> channels 0,1 +histogram\_nd 256**

---

# Command: histogram_cumul
**Category:** Features Extraction
**Source:** https://gmic.eu/reference/histogram_cumul.html#top

# histogram\_cumul

## Arguments:

* \_nb\_levels>0,\_is\_normalized={ 0:No | 1:Yes },\_val0[%],\_val1[%]

## Description:

Compute cumulative histogram of selected images.  

## Default values:

nb\_levels=256, is\_normalized=0, val0=0% and val1=100%.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +histogram\_cumul 256 histogram[0] 256 display\_graph 400,300,3

  

[![](img/t0_histogram_cumul.jpg)](img/f0_histogram_cumul.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +histogram\_cumul 256 histogram[0] 256 display\_graph 400,300,3**

[![](img/t1_histogram_cumul.jpg)](img/f1_histogram_cumul.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +histogram\_cumul 256 histogram[0] 256 display\_graph 400,300,3**

---

# Command: histogram_pointwise
**Category:** Features Extraction
**Source:** https://gmic.eu/reference/histogram_pointwise.html#top

# histogram\_pointwise

## Arguments:

* nb\_levels[%]>0,\_value0[%],\_value1[%]

## Description:

Compute the histogram of each vector-valued point of selected images.  
  
If value range is set, the histogram is estimated only for values in the specified  
value range.  

## Default values:

value0=0% and value1=100%.

---

# Command: hough
**Category:** Features Extraction
**Source:** https://gmic.eu/reference/hough.html#top

# hough

## Arguments:

* \_width>0,\_height>0,gradient\_norm\_voting={ 0:No | 1:Yes }

## Description:

Compute hough transform (theta,rho) of selected images.  

## Default values:

width=512, height=width and gradient\_norm\_voting=1.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +blur 1.5 hough[-1] 400,400 blur[-1] 0.5 add[-1] 1 log[-1]

  

[![](img/t0_hough.jpg)](img/f0_hough.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +blur 1.5 hough[-1] 400,400 blur[-1] 0.5 add[-1] 1 log[-1]**

[![](img/t1_hough.jpg)](img/f1_hough.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +blur 1.5 hough[-1] 400,400 blur[-1] 0.5 add[-1] 1 log[-1]**

---

# Command: huffman_tree
**Category:** Features Extraction
**Source:** https://gmic.eu/reference/huffman_tree.html#top

# huffman\_tree

### No argumentsDescription:Generate Huffman coding tree from the statistics of all selected images. Huffman tree is returned as a 1xN image inserted at the end of the image list, representing the N vector-valued leafs/nodes of the tree, encoded as [ value,parent,child0,child1 ]. Last row of the returned image corresponds to the tree root. Selected images must contain only positive integer values. Return maximal value of the input data in the status. See also:[compress\_huffman](compress_huffman.html), [decompress\_huffman](decompress_huffman.html).

---

# Command: ifftpolar
**Category:** Features Extraction
**Source:** https://gmic.eu/reference/ifftpolar.html#top

# ifftpolar

### No argumentsDescription:Compute inverse fourier transform of selected images, from centered magnitude/phase images.

---

# Command: img2patches
**Category:** Features Extraction
**Source:** https://gmic.eu/reference/img2patches.html#top

# img2patches

## Arguments:

* patch\_size>0,\_overlap[%]>0,\_boundary\_conditions

## Description:

Decompose selected 2D images into (possibly overlapping) patches and stack them along the z-axis.  
  
overlap must be in range [0,patch\_size-1].  
boundary\_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.  

## Default values:

overlap=0 and boundary\_conditions=0.

## See also:

[patches2img](patches2img.html).

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> img2patches 64

  
[![](img/t_img2patches.jpg)](img/f_img2patches.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> img2patches 64**

---

# Command: isophotes
**Category:** Features Extraction
**Source:** https://gmic.eu/reference/isophotes.html#top

# isophotes

## Arguments:

* \_nb\_levels>0

## Description:

Render isophotes of selected images on a transparent background.  

## Default values:

nb\_levels=64

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> blur 2 isophotes 6 dilate\_circ 5 display\_rgba

  
[![](img/t_isophotes.jpg)](img/f_isophotes.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> blur 2 isophotes 6 dilate\_circ 5 display\_rgba**

---

# Command: label
**Category:** Features Extraction
**Source:** https://gmic.eu/reference/label.html#top

|  |  |
| --- | --- |
| label | Built-in command |

## Arguments:

* \_tolerance>=0,is\_high\_connectivity={ 0:No | 1:Yes },\_is\_L2\_norm={ 0:No | 1:Yes }

## Description:

Label connected components in selected images.  
  
If is\_L2\_norm=1, tolerances are compared against L2-norm, otherwise L1-norm is used.  

## Default values:

tolerance=0, is\_high\_connectivity=0 and is\_L2\_norm=1.

This command has a [tutorial page](https://gmic.eu/oldtutorial/_label).

## Examples of use:

### • Example #1

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> luminance threshold 60% label normalize 0,255 map 0

  
[![](img/t_label.jpg)](img/f_label.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> luminance threshold 60% label normalize 0,255 map 0**

### • Example #2

400,400 set 1,50%,50% distance 1 mod 16 threshold 8 label mod 255 map 2

  
[![](img/t_label_2.jpg)](img/f_label_2.jpg)

Command: **400,400 set 1,50%,50% distance 1 mod 16 threshold 8 label mod 255 map 2**

---

# Command: label_fg
**Category:** Features Extraction
**Source:** https://gmic.eu/reference/label_fg.html#top

# label\_fg

## Arguments:

* tolerance>=0,is\_high\_connectivity={ 0:No | 1:Yes },\_is\_L2\_norm={ 0:No | 1:Yes }

## Description:

Label connected components for non-zero values (foreground) in selected images.  
  
Similar to label except that 0-valued pixels are not labeled.  
If is\_L2\_norm=1, tolerances are compared against L2-norm, otherwise L1-norm is used.  

## Default values:

is\_high\_connectivity=0.

---

# Command: laar
**Category:** Features Extraction
**Source:** https://gmic.eu/reference/laar.html#top

# laar

### No argumentsDescription:Extract the largest axis-aligned rectangle in non-zero areas of selected images. Rectangle coordinates are returned in status, as a sequence of numbers x0,y0,x1,y1. Example of use: shape\_cupid 256 coords=${-laar} normalize 0,255 to\_rgb rectangle $coords,0.5,0,128,0 Command: **shape\_cupid 256 coords=${-laar} normalize 0,255 to\_rgb rectangle $coords,0.5,0,128,0**

---

# Command: max_patch
**Category:** Features Extraction
**Source:** https://gmic.eu/reference/max_patch.html#top

# max\_patch

## Arguments:

* \_patch\_size>=1

## Description:

Return locations of maximal values in local patch-based neighborhood of given size for selected images.  

## Default values:

patch\_size=16.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> norm +max\_patch 16

  

[![](img/t0_max_patch.jpg)](img/f0_max_patch.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> norm +max\_patch 16**

[![](img/t1_max_patch.jpg)](img/f1_max_patch.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> norm +max\_patch 16**

---

# Command: min_patch
**Category:** Features Extraction
**Source:** https://gmic.eu/reference/min_patch.html#top

# min\_patch

## Arguments:

* \_patch\_size>=1

## Description:

Return locations of minimal values in local patch-based neighborhood of given size for selected images.  

## Default values:

patch\_size=16.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> norm +min\_patch 16

  

[![](img/t0_min_patch.jpg)](img/f0_min_patch.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> norm +min\_patch 16**

[![](img/t1_min_patch.jpg)](img/f1_min_patch.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> norm +min\_patch 16**

---

# Command: minimal_path
**Category:** Features Extraction
**Source:** https://gmic.eu/reference/minimal_path.html#top

# minimal\_path

## Arguments:

* x0[%]>=0,y0[%]>=0,z0[%]>=0,x1[%]>=0,y1[%]>=0,z1[%]>=0,\_is\_high\_connectivity={ 0:No | 1:Yes }

## Description:

Compute minimal path between two points on selected potential maps.  

## Default values:

is\_high\_connectivity=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +gradient\_norm fill[-1] 1/(1+i) minimal\_path[-1] 0,0,0,100%,100%,0 pointcloud[-1] 0 \*[-1] 280 to\_rgb[-1] ri[-1] [-2],0 or

  
[![](img/t_minimal_path.jpg)](img/f_minimal_path.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +gradient\_norm fill[-1] 1/(1+i) minimal\_path[-1] 0,0,0,100%,100%,0 pointcloud[-1] 0 \*[-1] 280 to\_rgb[-1] ri[-1] [-2],0 or**

---

# Command: mse
**Category:** Features Extraction
**Source:** https://gmic.eu/reference/mse.html#top

# mse

## Arguments:

* [reference]

## Description:

Return the MSE (Mean-Squared Error) between selected images and specified reference image.  
  
This command does not modify the images. It returns a value or a list of values in the status.

---

# Command: mse_matrix
**Category:** Features Extraction
**Source:** https://gmic.eu/reference/mse_matrix.html#top

# mse\_matrix

### No argumentsDescription:Compute MSE (Mean-Squared Error) matrix between selected images. Example of use: <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +noise 30 +noise[0] 35 +noise[0] 38 cut. 0,255 +mse\_matrix Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +noise 30 +noise[0] 35 +noise[0] 38 cut. 0,255 +mse\_matrix** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +noise 30 +noise[0] 35 +noise[0] 38 cut. 0,255 +mse\_matrix** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +noise 30 +noise[0] 35 +noise[0] 38 cut. 0,255 +mse\_matrix** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +noise 30 +noise[0] 35 +noise[0] 38 cut. 0,255 +mse\_matrix** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +noise 30 +noise[0] 35 +noise[0] 38 cut. 0,255 +mse\_matrix**

---

# Command: patches2img
**Category:** Features Extraction
**Source:** https://gmic.eu/reference/patches2img.html#top

# patches2img

## Arguments:

* width>0,height>0,\_overlap[%]>0,\_overlap\_std[%]

## Description:

Recompose 2D images from their selected patch representations.  
  
overlap must be in range [0,patch\_size-1] where patch\_size is the width/height of the selected image.  
overlap\_std is the standard deviation of the gaussian weights used for reconstructing overlapping patches.  
If overlap\_std is set to -1, uniform weights are used rather than gaussian.  

## Default values:

overlap=0 and overlap\_std=-1.

## See also:

[img2patches](img2patches.html).

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +img2patches 32,0,3 mirror[-1] xy patches2img[-1] {0,[w,h]}

  

[![](img/t0_patches2img.jpg)](img/f0_patches2img.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +img2patches 32,0,3 mirror[-1] xy patches2img[-1] {0,[w,h]}**

[![](img/t1_patches2img.jpg)](img/f1_patches2img.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +img2patches 32,0,3 mirror[-1] xy patches2img[-1] {0,[w,h]}**

---

# Command: patches
**Category:** Features Extraction
**Source:** https://gmic.eu/reference/patches.html#top

# patches

## Arguments:

* patch\_width>0,patch\_height>0,patch\_depth>0,x0,y0,z0,\_x1,\_y1,\_z1,...,\_xN,\_yN,\_zN

## Description:

Extract N+1 patches from selected images, centered at specified locations.  

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +patches 64,64,1,153,124,0,184,240,0,217,126,0,275,38,0

  

[![](img/t0_patches.jpg)](img/f0_patches.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +patches 64,64,1,153,124,0,184,240,0,217,126,0,275,38,0**

[![](img/t1_patches.jpg)](img/f1_patches.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +patches 64,64,1,153,124,0,184,240,0,217,126,0,275,38,0**

[![](img/t2_patches.jpg)](img/f2_patches.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +patches 64,64,1,153,124,0,184,240,0,217,126,0,275,38,0**

[![](img/t3_patches.jpg)](img/f3_patches.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +patches 64,64,1,153,124,0,184,240,0,217,126,0,275,38,0**

[![](img/t4_patches.jpg)](img/f4_patches.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +patches 64,64,1,153,124,0,184,240,0,217,126,0,275,38,0**

---

# Command: pca
**Category:** Features Extraction
**Source:** https://gmic.eu/reference/pca.html#top

# pca

## Arguments:

* \_output\_mode,\_target\_dim[%]>0,\_normalization\_mode={ 0:None | 1:Center | 2:Center+scale }

## Description:

Perform PCA (Principal Component Analysis) on selected images, viewed as sets of vector-valued samples Xk.  
  
  
Bits of output\_mode selects what output data are returned on the image stack:  

1: Output image of vector-valued samples Yk = Mt\*(Xk - avg)/std, that are the projections of the Xk in a vector sub-space of (lower) dimension target\_dim. avg is the average vector of all Xk (or zero vector if normalization\_mode==0). std is the standard deviation vector of all Xk (or all-ones vector if normalization\_mode<2). Mt is the transpose of M, the matrix of the target\_dim first eigenvectors (arranged by columns) of the covariance matrix of the Xk.

2: Output vector avg: average of the Xk.

4: Output vector std: standard deviations of the Xk.

8: Output matrix M: projection matrix (orthonormal).

  
Knowing avg, std and M makes it possible to (approximately) retro-project the Yk in the initial vector space, by computing Xk = avg + std\*M\*Yk for each image pixel.  

## Default values:

output\_mode=15, target\_dim=100% and normalization\_mode=1.

## Example of use:

shape\_dragonfly 400 mul 128 0 eval.. "i?da\_push([x,y])" da\_freeze. pca. 11,2 eval "C = I[#-2,0]; M = transpose(crop(#-1),2); repeat(2,k,polygon(#0,-2,C-1000\*M[2\*k,2],C+1000\*M[2\*k,2],1,0xF0F0F0F0,180)); ellipse(#0,C,5,5,0,1,255)" k[0]

  
[![](img/t_pca.jpg)](img/f_pca.jpg)

Command: **shape\_dragonfly 400 mul 128 0 eval.. "i?da\_push([x,y])" da\_freeze. pca. 11,2 eval "C = I[#-2,0]; M = transpose(crop(#-1),2); repeat(2,k,polygon(#0,-2,C-1000\*M[2\*k,2],C+1000\*M[2\*k,2],1,0xF0F0F0F0,180)); ellipse(#0,C,5,5,0,1,255)" k[0]**

---

# Command: matchpatch
**Category:** Features Extraction
**Source:** https://gmic.eu/reference/matchpatch.html#top

|  |  |
| --- | --- |
| matchpatch | Built-in command |

## Arguments:

* [patch\_image],patch\_width>=1,\_patch\_height>=1,\_patch\_depth>=1,\_nb\_iterations>=0,\_nb\_randoms>=0,\_occurence\_penalization,\_output\_score={ 0:No | 1:Yes },\_[guide]

## Description:

Estimate correspondence map between selected images and specified patch image, using  
  
a patch-matching algorithm.  
Each pixel of the returned correspondence map gives the location (p,q) of the closest patch in  
the specified patch image. If output\_score=1, the third channel also gives the corresponding  
matching score for each patch as well.  
If patch\_penalization is >=0, SSD is penalized with patch occurrences.  
If patch\_penalization is <0, SSD is inf-penalized when distance between patches are less than -patch\_penalization.  

## Default values:

patch\_height=patch\_width, patch\_depth=1, nb\_iterations=5, nb\_randoms=5, occurence\_penalization=0, output\_score=0 and guide=(undefined).

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> sample colorful +matchpatch[0] [1],3 +warp[-2] [-1],0

  

[![](img/t0_matchpatch.jpg)](img/f0_matchpatch.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> sample colorful +matchpatch[0] [1],3 +warp[-2] [-1],0**

[![](img/t1_matchpatch.jpg)](img/f1_matchpatch.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> sample colorful +matchpatch[0] [1],3 +warp[-2] [-1],0**

[![](img/t2_matchpatch.jpg)](img/f2_matchpatch.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> sample colorful +matchpatch[0] [1],3 +warp[-2] [-1],0**

[![](img/t3_matchpatch.jpg)](img/f3_matchpatch.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> sample colorful +matchpatch[0] [1],3 +warp[-2] [-1],0**

---

# Command: matchpatch_alt
**Category:** Features Extraction
**Source:** https://gmic.eu/reference/matchpatch_alt.html#top

# matchpatch\_alt

## Arguments:

* [patch\_image],\_patch\_width>=1,\_patch\_height>=1,\_patch\_depth>=1,\_nb\_iterations>=0,\_nb\_randoms>=0,\_occurrence\_penalization>=0,\_output\_score={ 0:No | 1:Yes },\_[guide]

## Description:

Implementation of the [matchpatch](matchpatch.html) command as an alternative custom command (slower).  

## Default values:

patch\_height=patch\_width, patch\_depth=1, nb\_iterations=5, nb\_randoms=5, occurrence\_penalization=0, output\_score=0 and guide=(undefined).

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> sample colorful +matchpatch\_alt[0] [1],3 +warp[-2] [-1],0

  

[![](img/t0_matchpatch_alt.jpg)](img/f0_matchpatch_alt.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> sample colorful +matchpatch\_alt[0] [1],3 +warp[-2] [-1],0**

[![](img/t1_matchpatch_alt.jpg)](img/f1_matchpatch_alt.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> sample colorful +matchpatch\_alt[0] [1],3 +warp[-2] [-1],0**

[![](img/t2_matchpatch_alt.jpg)](img/f2_matchpatch_alt.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> sample colorful +matchpatch\_alt[0] [1],3 +warp[-2] [-1],0**

[![](img/t3_matchpatch_alt.jpg)](img/f3_matchpatch_alt.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> sample colorful +matchpatch\_alt[0] [1],3 +warp[-2] [-1],0**

---

# Command: plot2value
**Category:** Features Extraction
**Source:** https://gmic.eu/reference/plot2value.html#top

# plot2value

### No argumentsDescription:Retrieve values from selected 2D graph plots. Example of use: 400,300,1,1,'y>300\*abs(cos(x/10+2\*u))' +plot2value +display\_graph[-1] 400,300 Command: **400,300,1,1,'y>300\*abs(cos(x/10+2\*u))' +plot2value +display\_graph[-1] 400,300** Command: **400,300,1,1,'y>300\*abs(cos(x/10+2\*u))' +plot2value +display\_graph[-1] 400,300** Command: **400,300,1,1,'y>300\*abs(cos(x/10+2\*u))' +plot2value +display\_graph[-1] 400,300**

---

# Command: pointcloud
**Category:** Features Extraction
**Source:** https://gmic.eu/reference/pointcloud.html#top

# pointcloud

## Arguments:

* \_type = { -X:-X-opacity | 0:Binary | 1:Cumulative | 2:Label | 3:Retrieve coordinates },\_width,\_height>0,\_depth>0

## Description:

Render a set of point coordinates, as a point cloud in a 1D/2D or 3D binary image  
  
(or do the reverse, i.e. retrieve coordinates of non-zero points from a rendered point cloud).  
Input point coordinates can be a NxMx1x1, Nx1x1xM or 1xNx1xM image, where N is the number of points,  
and M the point coordinates.  
If 'M'>3, the 3-to-M components sets the (M-3)-dimensional color at each point.  
Parameters width,height and depth are related to the size of the final image :  

If set to 0, the size is automatically set along the specified axis.

If set to N>0, the size along the specified axis is N.

If set to N<0, the size along the specified axis is at most N.

Points with coordinates that are negative or higher than specified (width,height,depth)  
are not plotted.  

## Default values:

type=0 and max\_width=max\_height=max\_depth=0.

## Examples of use:

### • Example #1

3000,2 rand 0,400 +pointcloud 0 dilate[-1] 3

  

[![](img/t0_pointcloud.jpg)](img/f0_pointcloud.jpg)

Command: **3000,2 rand 0,400 +pointcloud 0 dilate[-1] 3**

[![](img/t1_pointcloud.jpg)](img/f1_pointcloud.jpg)

Command: **3000,2 rand 0,400 +pointcloud 0 dilate[-1] 3**

### • Example #2

3000,2 rand 0,400 {w} {w},3 rand[-1] 0,255 append y +pointcloud 0 dilate[-1] 3

  

[![](img/t0_pointcloud_2.jpg)](img/f0_pointcloud_2.jpg)

Command: **3000,2 rand 0,400 {w} {w},3 rand[-1] 0,255 append y +pointcloud 0 dilate[-1] 3**

[![](img/t1_pointcloud_2.jpg)](img/f1_pointcloud_2.jpg)

Command: **3000,2 rand 0,400 {w} {w},3 rand[-1] 0,255 append y +pointcloud 0 dilate[-1] 3**

---

# Command: psnr
**Category:** Features Extraction
**Source:** https://gmic.eu/reference/psnr.html#top

# psnr

## Arguments:

* [reference],\_max\_value>0

## Description:

Return PSNR (Peak Signal-to-Noise Ratio) between selected images and specified reference image.  
  
This command does not modify the images. It returns a value or a list of values in the status.  

## Default values:

max\_value=255.

---

# Command: psnr_matrix
**Category:** Features Extraction
**Source:** https://gmic.eu/reference/psnr_matrix.html#top

# psnr\_matrix

## Arguments:

* \_max\_value>0

## Description:

Compute PSNR (Peak Signal-to-Noise Ratio) matrix between selected images.  

## Default values:

max\_value=255.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +noise 30 +noise[0] 35 +noise[0] 38 cut. 0,255 +psnr\_matrix

  

[![](img/t0_psnr_matrix.jpg)](img/f0_psnr_matrix.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +noise 30 +noise[0] 35 +noise[0] 38 cut. 0,255 +psnr\_matrix**

[![](img/t1_psnr_matrix.jpg)](img/f1_psnr_matrix.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +noise 30 +noise[0] 35 +noise[0] 38 cut. 0,255 +psnr\_matrix**

[![](img/t2_psnr_matrix.jpg)](img/f2_psnr_matrix.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +noise 30 +noise[0] 35 +noise[0] 38 cut. 0,255 +psnr\_matrix**

[![](img/t3_psnr_matrix.jpg)](img/f3_psnr_matrix.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +noise 30 +noise[0] 35 +noise[0] 38 cut. 0,255 +psnr\_matrix**

[![](img/t4_psnr_matrix.jpg)](img/f4_psnr_matrix.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +noise 30 +noise[0] 35 +noise[0] 38 cut. 0,255 +psnr\_matrix**

---

# Command: segment_watershed
**Category:** Features Extraction
**Source:** https://gmic.eu/reference/segment_watershed.html#top

# segment\_watershed

## Arguments:

* \_threshold>=0

## Description:

Apply watershed segmentation on selected images.  

## Default values:

threshold=2.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> segment\_watershed 2

  
[![](img/t_segment_watershed.jpg)](img/f_segment_watershed.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> segment\_watershed 2**

---

# Command: shape2bump
**Category:** Features Extraction
**Source:** https://gmic.eu/reference/shape2bump.html#top

# shape2bump

## Arguments:

* \_resolution>=0,0<=\_weight\_std\_max\_avg<=1,\_dilation,\_smoothness>=0

## Description:

Estimate bumpmap from binary shape in selected images.  

## Default values:

resolution=256, weight\_std\_max=0.75, dilation=0 and smoothness=100.

---

# Command: skeleton
**Category:** Features Extraction
**Source:** https://gmic.eu/reference/skeleton.html#top

# skeleton

## Arguments:

* \_boundary\_conditions={ 0:Dirichlet | 1:Neumann }

## Description:

Compute skeleton of binary shapes using distance transform and constrained thinning.  

## Default values:

boundary\_conditions=1.

## Example of use:

shape\_cupid 320 +skeleton 0

  

[![](img/t0_skeleton.jpg)](img/f0_skeleton.jpg)

Command: **shape\_cupid 320 +skeleton 0**

[![](img/t1_skeleton.jpg)](img/f1_skeleton.jpg)

Command: **shape\_cupid 320 +skeleton 0**

---

# Command: slic
**Category:** Features Extraction
**Source:** https://gmic.eu/reference/slic.html#top

# slic

## Arguments:

* size>0,\_regularity>=0,\_nb\_iterations>0

## Description:

Segment selected 2D images with superpixels, using the SLIC algorithm (Simple Linear Iterative Clustering).  
  
Scalar images of increasingly labeled pixels are returned.  
Reference paper: Achanta, R., Shaji, A., Smith, K., Lucchi, A., Fua, P., & Susstrunk, S. (2010). SLIC Superpixels (No. EPFL-REPORT-149300).  

## Default values:

size=16, regularity=10 and nb\_iterations=10.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +srgb2lab slic[-1] 16 +blend shapeaverage f[-2] "j(1,0)==i && j(0,1)==i" \*[-1] [-2]

  

[![](img/t0_slic.jpg)](img/f0_slic.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +srgb2lab slic[-1] 16 +blend shapeaverage f[-2] "j(1,0)==i && j(0,1)==i" \*[-1] [-2]**

[![](img/t1_slic.jpg)](img/f1_slic.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +srgb2lab slic[-1] 16 +blend shapeaverage f[-2] "j(1,0)==i && j(0,1)==i" \*[-1] [-2]**

[![](img/t2_slic.jpg)](img/f2_slic.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +srgb2lab slic[-1] 16 +blend shapeaverage f[-2] "j(1,0)==i && j(0,1)==i" \*[-1] [-2]**

---

# Command: ssd_patch
**Category:** Features Extraction
**Source:** https://gmic.eu/reference/ssd_patch.html#top

# ssd\_patch

## Arguments:

* [patch],\_use\_fourier={ 0:No | 1:Yes },\_boundary\_conditions

## Description:

Compute fields of SSD between selected images and specified patch.  
  
Argument boundary\_conditions is valid only when use\_fourier=0.  
boundary\_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.  

## Default values:

use\_fourier=0 and boundary\_conditions=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +crop 20%,20%,35%,35% +ssd\_patch[0] [1],0,0

  

[![](img/t0_ssd_patch.jpg)](img/f0_ssd_patch.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +crop 20%,20%,35%,35% +ssd\_patch[0] [1],0,0**

[![](img/t1_ssd_patch.jpg)](img/f1_ssd_patch.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +crop 20%,20%,35%,35% +ssd\_patch[0] [1],0,0**

[![](img/t2_ssd_patch.jpg)](img/f2_ssd_patch.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +crop 20%,20%,35%,35% +ssd\_patch[0] [1],0,0**

---

# Command: ssim
**Category:** Features Extraction
**Source:** https://gmic.eu/reference/ssim.html#top

# ssim

## Arguments:

* [reference],\_patch\_size>0,\_max\_value>0

## Description:

Compute the Structural Similarity Index Measure (SSIM) between selected images and specified reference image.  
  
This command does not modify the images, it just returns a value or a list of values in the status.  
When downsampling\_factor is specified with a ending %, its value is equal to 1+(patch\_size-1)\*spatial\_factor%.  
  
SSIM is a measure introduced int the following paper:  
Wang, Zhou, et al., "Image quality assessment: from error visibility to structural similarity.",  
in IEEE transactions on image processing 13.4 (2004): 600-612.  
  
The implementation of this command is a direct translation of the reference code (in Matlab), found at :  
https://ece.uwaterloo.ca/~z70wang/research/ssim/  

## Default values:

patch\_size=11, and max\_value=255.

---

# Command: ssim_matrix
**Category:** Features Extraction
**Source:** https://gmic.eu/reference/ssim_matrix.html#top

# ssim\_matrix

## Arguments:

* \_patch\_size>0,\_max\_value>0

## Description:

Compute SSIM (Structural Similarity Index Measure) matrix between selected images.  

## Default values:

patch\_size=11, and max\_value=255.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +noise 30 +noise[0] 35 +noise[0] 38 cut. 0,255 +ssim\_matrix

  

[![](img/t0_ssim_matrix.jpg)](img/f0_ssim_matrix.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +noise 30 +noise[0] 35 +noise[0] 38 cut. 0,255 +ssim\_matrix**

[![](img/t1_ssim_matrix.jpg)](img/f1_ssim_matrix.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +noise 30 +noise[0] 35 +noise[0] 38 cut. 0,255 +ssim\_matrix**

[![](img/t2_ssim_matrix.jpg)](img/f2_ssim_matrix.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +noise 30 +noise[0] 35 +noise[0] 38 cut. 0,255 +ssim\_matrix**

[![](img/t3_ssim_matrix.jpg)](img/f3_ssim_matrix.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +noise 30 +noise[0] 35 +noise[0] 38 cut. 0,255 +ssim\_matrix**

[![](img/t4_ssim_matrix.jpg)](img/f4_ssim_matrix.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +noise 30 +noise[0] 35 +noise[0] 38 cut. 0,255 +ssim\_matrix**

---

# Command: thinning
**Category:** Features Extraction
**Source:** https://gmic.eu/reference/thinning.html#top

# thinning

## Arguments:

* \_boundary\_conditions={ 0:Dirichlet | 1:Neumann }

## Description:

Compute skeleton of binary shapes using morphological thinning  
  
(beware, this is a quite slow iterative process)  

## Default values:

boundary\_conditions=1.

## Example of use:

shape\_cupid 320 +thinning

  

[![](img/t0_thinning.jpg)](img/f0_thinning.jpg)

Command: **shape\_cupid 320 +thinning**

[![](img/t1_thinning.jpg)](img/f1_thinning.jpg)

Command: **shape\_cupid 320 +thinning**

---

# Command: tones
**Category:** Features Extraction
**Source:** https://gmic.eu/reference/tones.html#top

# tones

## Arguments:

* N>0

## Description:

Get N tones masks from selected images.  

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +tones 3

  

[![](img/t0_tones.jpg)](img/f0_tones.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +tones 3**

[![](img/t1_tones.jpg)](img/f1_tones.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +tones 3**

[![](img/t2_tones.jpg)](img/f2_tones.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +tones 3**

[![](img/t3_tones.jpg)](img/f3_tones.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +tones 3**

---

# Command: topographic_map
**Category:** Features Extraction
**Source:** https://gmic.eu/reference/topographic_map.html#top

# topographic\_map

## Arguments:

* \_nb\_levels>0,\_smoothness

## Description:

Render selected images as topographic maps.  

## Default values:

nb\_levels=16 and smoothness=2.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> topographic\_map 10

  
[![](img/t_topographic_map.jpg)](img/f_topographic_map.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> topographic\_map 10**

---

# Command: tsp
**Category:** Features Extraction
**Source:** https://gmic.eu/reference/tsp.html#top

# tsp

## Arguments:

* \_precision>=0

## Description:

Try to solve the travelling salesman problem, using a combination of greedy search and 2-opt algorithms.  
  
Selected images must have dimensions Nx1x1xC to represent N cities each with C-dimensional coordinates.  
This command re-order the selected data along the x-axis so that the point sequence becomes a shortest path.  

## Default values:

precision=256.

## Example of use:

256,1,1,2 rand 0,512 tsp , 512,512,1,3 repeat w#0 circle[-1] {0,I[$>]},2,1,255,255,255 line[-1] {0,boundary=2;[I[$>],I[$>+1]]},1,255,128,0 done keep[-1]

  
[![](img/t_tsp.jpg)](img/f_tsp.jpg)

Command: **256,1,1,2 rand 0,512 tsp , 512,512,1,3 repeat w#0 circle[-1] {0,I[$>]},2,1,255,255,255 line[-1] {0,boundary=2;[I[$>],I[$>+1]]},1,255,128,0 done keep[-1]**

---

# Command: variance_patch
**Category:** Features Extraction
**Source:** https://gmic.eu/reference/variance_patch.html#top

# variance\_patch

## Arguments:

* \_patch\_size>=1

## Description:

Compute variance of each images patch centered at (x,y), in selected images.  

## Default values:

patch\_size=16

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +variance\_patch

  

[![](img/t0_variance_patch.jpg)](img/f0_variance_patch.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +variance\_patch**

[![](img/t1_variance_patch.jpg)](img/f1_variance_patch.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +variance\_patch**

---

# Command: arrow
**Category:** Image Drawing
**Source:** https://gmic.eu/reference/arrow.html#top

# arrow

## Arguments:

* x0[%],y0[%],x1[%],y1[%],\_thickness[%]>=0,\_head\_length[%]>=0,\_head\_thickness[%]>=0,\_opacity,\_pattern,\_color1,...

## Description:

Draw specified arrow on selected images.  
  
pattern is an hexadecimal number starting with 0x which can be omitted  
even if a color is specified. If a pattern is specified, the arrow is  
drawn outlined instead of filled.  

## Default values:

thickness=1%, head\_length=10%, head\_thickness=3%, opacity=1, pattern=(undefined) and color1=0.

## Example of use:

400,400,1,3 repeat 100 arrow 50%,50%,{u(100)}%,{u(100)}%,3,20,10,0.3,${-rgb} done

  
[![](img/t_arrow.jpg)](img/f_arrow.jpg)

Command: **400,400,1,3 repeat 100 arrow 50%,50%,{u(100)}%,{u(100)}%,3,20,10,0.3,${-rgb} done**

---

# Command: axes
**Category:** Image Drawing
**Source:** https://gmic.eu/reference/axes.html#top

# axes

## Arguments:

* x0,x1,y0,y1,\_font\_height>=0,\_opacity,\_pattern,\_color1,...

## Description:

Draw xy-axes on selected images.  
  
pattern is an hexadecimal number starting with 0x which can be omitted  
even if a color is specified.  
To draw only one x-axis at row Y, set both y0 and y1 to Y.  
To draw only one y-axis at column X, set both x0 and x1 to X.  

## Default values:

font\_height=14, opacity=1, pattern=(undefined) and color1=0.

## Example of use:

400,400,1,3,255 axes -1,1,1,-1

  
[![](img/t_axes.jpg)](img/f_axes.jpg)

Command: **400,400,1,3,255 axes -1,1,1,-1**

---

# Command: ball
**Category:** Image Drawing
**Source:** https://gmic.eu/reference/ball.html#top

# ball

## Arguments:

* \_size>0,\_R,\_G,\_B,\_ambient>=0,\_diffuse>=0,\_specular>=0,\_shininess>=0,\_light\_x,\_light\_y,\_light\_z

## Description:

Input a 2D RGBA colored ball sprite, rendered using the Phong illumination model.  

## Default values:

size=64, R=200, G=R, B=R, ambient=0.25, diffuse=1, specular=1, shininess=20, light\_x=1.5, light\_y=-1.5 and light\_z=1.

## Example of use:

repeat 9 { ball {int(1.5^($>+4))},${-rgb} } append\_tiles 3,3

  
[![](img/t_ball.jpg)](img/f_ball.jpg)

Command: **repeat 9 { ball {int(1.5^($>+4))},${-rgb} } append\_tiles 3,3**

---

# Command: chessboard
**Category:** Image Drawing
**Source:** https://gmic.eu/reference/chessboard.html#top

# chessboard

## Arguments:

* size1>0,\_size2>0,\_offset1,\_offset2,\_angle,\_opacity,\_color1,...,\_color2,...

## Description:

Draw chessboard on selected images.  

## Default values:

size2=size1, offset1=offset2=0, angle=0, opacity=1, color1=0 and color2=255.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> chessboard 32,32,0,0,25,0.3,255,128,0,0,128,255

  
[![](img/t_chessboard.jpg)](img/f_chessboard.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> chessboard 32,32,0,0,25,0.3,255,128,0,0,128,255**

---

# Command: cie1931
**Category:** Image Drawing
**Source:** https://gmic.eu/reference/cie1931.html#top

# cie1931

### No argumentsDescription:Draw CIE-1931 chromaticity diagram on selected images. Example of use: 500,400,1,3 cie1931 Command: **500,400,1,3 cie1931**

---

# Command: circle
**Category:** Image Drawing
**Source:** https://gmic.eu/reference/circle.html#top

# circle

## Arguments:

* x[%],y[%],R[%],\_opacity,\_pattern,\_color1,...

## Description:

Draw specified colored circle on selected images.  
  
A radius of 100% stands for sqrt(width^2+height^2).  
pattern is an hexadecimal number starting with 0x which can be omitted  
even if a color is specified. If a pattern is specified, the circle is  
drawn outlined instead of filled.  

## Default values:

opacity=1, pattern=(undefined) and color1=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> repeat 300 circle {u(100)}%,{u(100)}%,{u(30)},0.3,${-rgb} done circle 50%,50%,100,0.7,255

  
[![](img/t_circle.jpg)](img/f_circle.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> repeat 300 circle {u(100)}%,{u(100)}%,{u(30)},0.3,${-rgb} done circle 50%,50%,100,0.7,255**

---

# Command: close_binary
**Category:** Image Drawing
**Source:** https://gmic.eu/reference/close_binary.html#top

# close\_binary

## Arguments:

* 0<=\_endpoint\_rate<=100,\_endpoint\_connectivity>=0,\_spline\_distmax>=0,\_segment\_distmax>=0,0<=\_spline\_anglemax<=180,\_spline\_roundness>=0,\_area\_min>=0,\_allow\_self\_intersection={ 0:No | 1:Yes }

## Description:

Automatically close open shapes in binary images (defining white strokes on black background).  

## Default values:

endpoint\_rate=75, endpoint\_connectivity=2, spline\_distmax=80, segment\_distmax=20, spline\_anglemax=90, spline\_roundness=1,area\_min=100, allow\_self\_intersection=1.

---

# Command: curve
**Category:** Image Drawing
**Source:** https://gmic.eu/reference/curve.html#top

# curve

## Arguments:

* [xy\_coordinates],\_thickness>0,\_tilt,\_tilt\_strength[%],\_is\_closed={ 0:No | 1:Yes },\_opacity,\_color1,...

## Description:

Draw specified parameterized curve on selected images.  
  
Arguments are:  

[xy\_coordinates] is the set of XY-coordinates of the curve, specified as a 2-channels image.

thickness is the thickness of the drawing, specified in pixels.

tilt is an angle, specified in degrees.

tilt\_strength must be a float value in [0,1] (or in [0,100] if specified as a percentage).

is\_closed is a boolean which tells if the curve is closed or not.

## Default values:

thickness=0, tilt=45

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> srand 3 16,1,1,4,u s. c,2 rbf[-2,-1] 1000,0,1 n[-2] 10,{w#0-10} n[-1] 10,{h#0-10} a[-2,-1] c curve[-2] [-1],6,0,0,0,1,0,128,0

  

[![](img/t0_curve.jpg)](img/f0_curve.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> srand 3 16,1,1,4,u s. c,2 rbf[-2,-1] 1000,0,1 n[-2] 10,{w#0-10} n[-1] 10,{h#0-10} a[-2,-1] c curve[-2] [-1],6,0,0,0,1,0,128,0**

[![](img/t1_curve.jpg)](img/f1_curve.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> srand 3 16,1,1,4,u s. c,2 rbf[-2,-1] 1000,0,1 n[-2] 10,{w#0-10} n[-1] 10,{h#0-10} a[-2,-1] c curve[-2] [-1],6,0,0,0,1,0,128,0**

---

# Command: ellipse
**Category:** Image Drawing
**Source:** https://gmic.eu/reference/ellipse.html#top

|  |  |
| --- | --- |
| ellipse | Built-in command |

## Arguments:

* x[%],y[%],R[%],r[%],\_angle,\_opacity,\_pattern,\_color1,...

## Description:

Draw specified colored ellipse on selected images.  
  
A radius of 100% stands for sqrt(width^2+height^2).  
pattern is an hexadecimal number starting with 0x which can be omitted  
even if a color is specified. If a pattern is specified, the ellipse is  
drawn outlined instead of filled.  

## Default values:

opacity=1, pattern=(undefined) and color1=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> repeat 300 ellipse {u(100)}%,{u(100)}%,{u(30)},{u(30)},{u(180)},0.3,${-rgb} done ellipse 50%,50%,100,100,0,0.7,255

  
[![](img/t_ellipse.jpg)](img/f_ellipse.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> repeat 300 ellipse {u(100)}%,{u(100)}%,{u(30)},{u(30)},{u(180)},0.3,${-rgb} done ellipse 50%,50%,100,100,0,0.7,255**

---

# Command: flood
**Category:** Image Drawing
**Source:** https://gmic.eu/reference/flood.html#top

|  |  |
| --- | --- |
| flood | Built-in command |

## Arguments:

* x[%],\_y[%],\_z[%],\_tolerance>=0,\_is\_high\_connectivity={ 0:No | 1:Yes },\_opacity,\_color1,...

## Description:

Flood-fill selected images using specified value and tolerance.  

## Default values:

y=z=0, tolerance=0, is\_high\_connectivity=0, opacity=1 and color1=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> repeat 1000 flood {u(100)}%,{u(100)}%,0,20,0,1,${-rgb} done

  
[![](img/t_flood.jpg)](img/f_flood.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> repeat 1000 flood {u(100)}%,{u(100)}%,0,20,0,1,${-rgb} done**

---

# Command: gaussian
**Category:** Image Drawing
**Source:** https://gmic.eu/reference/gaussian.html#top

# gaussian

## Arguments:

* \_sigma1[%],\_sigma2[%],\_angle

## Description:

Draw a centered gaussian on selected images, with specified standard deviations and orientation.  

## Default values:

sigma1=3, sigma2=sigma1 and angle=0.

This command has a [tutorial page](https://gmic.eu/oldtutorial/_gaussian).

## Example of use:

400,400 gaussian 100,30,45

  
[![](img/t_gaussian.jpg)](img/f_gaussian.jpg)

Command: **400,400 gaussian 100,30,45**

---

# Command: graph
**Category:** Image Drawing
**Source:** https://gmic.eu/reference/graph.html#top

# graph

## Arguments:

* [function\_image],\_plot\_type,\_vertex\_type,\_ytop,\_ybottom,\_opacity,\_pattern,\_color1,...

## Description:

Draw specified function graph on selected images.  
  
plot\_type can be { 0:None | 1:Lines | 2:Splines | 3:Bar }.  
vertex\_type can be { 0:None | 1:Points | 2,3:Crosses | 4,5:Circles | 6,7:Squares }.  
pattern is an hexadecimal number starting with 0x which can be omitted  
even if a color is specified.  

## Default values:

plot\_type=1, vertex\_type=1, ytop=ybottom=0 (auto), opacity=1, pattern=(undefined)

and color1=0.  

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +rows 50% blur[-1] 3 split[-1] c div[0] 1.5 graph[0] [1],2,0,0,0,1,255,0,0 graph[0] [2],2,0,0,0,1,0,255,0 graph[0] [3],2,0,0,0,1,0,0,255 keep[0]

  
[![](img/t_graph.jpg)](img/f_graph.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +rows 50% blur[-1] 3 split[-1] c div[0] 1.5 graph[0] [1],2,0,0,0,1,255,0,0 graph[0] [2],2,0,0,0,1,0,255,0 graph[0] [3],2,0,0,0,1,0,0,255 keep[0]**

---

# Command: grid
**Category:** Image Drawing
**Source:** https://gmic.eu/reference/grid.html#top

# grid

## Arguments:

* size\_x[%]>=0,size\_y[%]>=0,\_offset\_x[%],\_offset\_y[%],\_opacity,\_pattern,\_color1,...

## Description:

Draw xy-grid on selected images.  
  
pattern is an hexadecimal number starting with 0x which can be omitted  
even if a color is specified.  

## Default values:

offset\_x=offset\_y=0, opacity=1, pattern=(undefined) and color1=0.

## Examples of use:

### • Example #1

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> grid 10%,10%,0,0,0.5,255

  
[![](img/t_grid.jpg)](img/f_grid.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> grid 10%,10%,0,0,0.5,255**

### • Example #2

400,400,1,3,255 grid 10%,10%,0,0,0.3,0xCCCCCCCC,128,32,16

  
[![](img/t_grid_2.jpg)](img/f_grid_2.jpg)

Command: **400,400,1,3,255 grid 10%,10%,0,0,0.3,0xCCCCCCCC,128,32,16**

---

# Command: image
**Category:** Image Drawing
**Source:** https://gmic.eu/reference/image.html#top

|  |  |
| --- | --- |
| image | Built-in command |

## Arguments:

* [sprite],\_x[%|~],\_y[%|~],\_z[%|~],\_c[%|~],\_opacity,\_[opacity\_mask],\_max\_opacity\_mask

## Description:

Draw specified sprite on selected images.  

(*equivalent to shortcut command* j).

  
If one of the x,y,z or c argument ends with a ~, its value is expected to be  
a centering ratio (in [0,1]) rather than a position.  
Usual centering ratio are { 0:left-justified | 0.5:centered | 1:right-justified }.  

## Default values:

x=y=z=c=0, opacity=1, opacity\_mask=(undefined) and max\_opacity\_mask=1.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +crop 40%,40%,60%,60% resize[-1] 200%,200%,1,3,5 frame[-1] xy,2,0 image[0] [-1],30%,30% keep[0]

  
[![](img/t_image.jpg)](img/f_image.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +crop 40%,40%,60%,60% resize[-1] 200%,200%,1,3,5 frame[-1] xy,2,0 image[0] [-1],30%,30% keep[0]**

---

# Command: imagealpha
**Category:** Image Drawing
**Source:** https://gmic.eu/reference/imagealpha.html#top

# imagealpha

## Arguments:

* [sprite],\_x[%|~],\_y[%|~],\_z[%|~],\_c[%|~],\_opacity

## Description:

Draw specified sprite on selected images, considering that the sprite's last channel is the drawing's alpha.  

(*equivalent to shortcut command* ja).

  
If one of the x,y,z or c argument ends with a ~, its value is expected to be  
a centering ratio (in [0,1]) rather than a position.  
Usual centering ratio are { 0:left-justified | 0.5:centered | 1:right-justified }.  

## Default values:

x=y=z=c=0 and opacity=1.

---

# Command: line
**Category:** Image Drawing
**Source:** https://gmic.eu/reference/line.html#top

|  |  |
| --- | --- |
| line | Built-in command |

## Arguments:

* x0[%],y0[%],x1[%],y1[%],\_opacity,\_pattern,\_color1,...

## Description:

Draw specified colored line on selected images.  
  
pattern is an hexadecimal number starting with 0x which can be omitted  
even if a color is specified.  

## Default values:

opacity=1, pattern=(undefined) and color1=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> repeat 500 line 50%,50%,{u(w)},{u(h)},0.5,${-rgb} done line 0,0,100%,100%,1,0xCCCCCCCC,255 line 100%,0,0,100%,1,0xCCCCCCCC,255

  
[![](img/t_line.jpg)](img/f_line.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> repeat 500 line 50%,50%,{u(w)},{u(h)},0.5,${-rgb} done line 0,0,100%,100%,1,0xCCCCCCCC,255 line 100%,0,0,100%,1,0xCCCCCCCC,255**

---

# Command: line_aa
**Category:** Image Drawing
**Source:** https://gmic.eu/reference/line_aa.html#top

# line\_aa

## Arguments:

* x0[%],y0[%],x1[%],y1[%],\_opacity,\_color1,...

## Description:

Draw specified antialiased colored line on selected images.  

## Default values:

opacity=1 and color1=0.

## Example of use:

512,512,1,3 repeat 100 line\_aa {v([w,h,w,h])-1},1,${-rgb} done

  
[![](img/t_line_aa.jpg)](img/f_line_aa.jpg)

Command: **512,512,1,3 repeat 100 line\_aa {v([w,h,w,h])-1},1,${-rgb} done**

---

# Command: spline
**Category:** Image Drawing
**Source:** https://gmic.eu/reference/spline.html#top

# spline

## Arguments:

* x0[%],y0[%],u0[%],v0[%],x1[%],y1[%],u1[%],v1[%],\_opacity,\_color1,...

## Description:

Draw specified colored spline curve on selected images (cubic hermite spline).  

## Default values:

opacity=1 and color1=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> repeat 30 { spline {u(100)}%,{u(100)}%,{u(-600,600)},{u(-600,600)},{u(100)}%,{u(100)}%,{u(-600,600)},{u(-600,600)},1,${-rgb} }

  
[![](img/t_spline.jpg)](img/f_spline.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> repeat 30 { spline {u(100)}%,{u(100)}%,{u(-600,600)},{u(-600,600)},{u(100)}%,{u(100)}%,{u(-600,600)},{u(-600,600)},1,${-rgb} }**

---

# Command: thickcircle
**Category:** Image Drawing
**Source:** https://gmic.eu/reference/thickcircle.html#top

# thickcircle

## Arguments:

* x[%],y[%],R[%],\_thickness>=0,\_opacity,\_color1,...

## Description:

Draw specified colored thick outlined circle on selected images.  

## Default values:

thickness=3, opacity=1 and color1=0.

## Example of use:

400,400 repeat 15 { R:=lerp(10,190,$%) thickcircle 200,200,$R,2,1,$R } n 0,255 map 7

  
[![](img/t_thickcircle.jpg)](img/f_thickcircle.jpg)

Command: **400,400 repeat 15 { R:=lerp(10,190,$%) thickcircle 200,200,$R,2,1,$R } n 0,255 map 7**

---

# Command: thickellipse
**Category:** Image Drawing
**Source:** https://gmic.eu/reference/thickellipse.html#top

# thickellipse

## Arguments:

* x[%],y[%],R[%],r[%],\_angle,\_thickness>=0,\_opacity,\_color1,...

## Description:

Draw specified colored thick outlined ellipse on selected images.  

## Default values:

thickness=3, opacity=1 and color1=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> repeat 300 thickellipse {u(100)}%,{u(100)}%,{u(50)},{u(50)},{u(180)},3,0.6,${-rgb} done thickellipse 50%,50%,200,100,0,5,0.7,255

  
[![](img/t_thickellipse.jpg)](img/f_thickellipse.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> repeat 300 thickellipse {u(100)}%,{u(100)}%,{u(50)},{u(50)},{u(180)},3,0.6,${-rgb} done thickellipse 50%,50%,200,100,0,5,0.7,255**

---

# Command: thickline
**Category:** Image Drawing
**Source:** https://gmic.eu/reference/thickline.html#top

# thickline

## Arguments:

* x0[%],y0[%],x1[%],y1[%],\_thickness,\_opacity,\_color1

## Description:

Draw specified colored thick line on selected images.  

## Default values:

thickness=2, opacity=1 and color1=0.

## Example of use:

400,400,1,3 repeat 100 thickline {u([w,h,w,h,5])},0.5,${-rgb} done

  
[![](img/t_thickline.jpg)](img/f_thickline.jpg)

Command: **400,400,1,3 repeat 100 thickline {u([w,h,w,h,5])},0.5,${-rgb} done**

---

# Command: thickpolygon
**Category:** Image Drawing
**Source:** https://gmic.eu/reference/thickpolygon.html#top

# thickpolygon

## Arguments:

* N>=1,x1[%],y1[%],...,xN[%],yN[%],\_thickness>=0,\_opacity,\_color1,...    or
* [coords],\_thickness>=0,\_opacity,\_color1,...

## Description:

Draw specified colored thick outlined N-vertices polygon on selected images.  
  
If thickness<0, the command draws an open polygon rather than a closed polygon.  

## Default values:

thickness=3, opacity=1, and color1=0.

## Examples of use:

### • Example #1

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> thickpolygon 4,20%,20%,80%,30%,80%,70%,20%,80%,5,1,0,255,0

  
[![](img/t_thickpolygon.jpg)](img/f_thickpolygon.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> thickpolygon 4,20%,20%,80%,30%,80%,70%,20%,80%,5,1,0,255,0**

### • Example #2

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> 2,16,1,1,'u(x?h#0:w#0)' thickpolygon[-2] [-1],5,1,255,0,255 remove[-1]

  
[![](img/t_thickpolygon_2.jpg)](img/f_thickpolygon_2.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> 2,16,1,1,'u(x?h#0:w#0)' thickpolygon[-2] [-1],5,1,255,0,255 remove[-1]**

---

# Command: thickspline
**Category:** Image Drawing
**Source:** https://gmic.eu/reference/thickspline.html#top

# thickspline

## Arguments:

* x0[%],y0[%],u0[%],v0[%],x1[%],y1[%],u1[%],v1[%],\_thickness,\_opacity,\_color1,...

## Description:

Draw specified colored thick spline curve on selected images (cubic hermite spline).  

## Default values:

thickness=3, opacity=1 and color1=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> repeat 30 { thickspline {u(100)}%,{u(100)}%,{u(-600,600)},{u(-600,600)},{u(100)}%,{u(100)}%,{u(-600,600)},{u(-600,600)},3,1,${-rgb} }

  
[![](img/t_thickspline.jpg)](img/f_thickspline.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> repeat 30 { thickspline {u(100)}%,{u(100)}%,{u(-600,600)},{u(-600,600)},{u(100)}%,{u(100)}%,{u(-600,600)},{u(-600,600)},3,1,${-rgb} }**

---

# Command: mandelbrot
**Category:** Image Drawing
**Source:** https://gmic.eu/reference/mandelbrot.html#top

# mandelbrot

## Arguments:

* z0r,z0i,z1r,z1i,\_iteration\_max>=0,\_is\_julia={ 0:No | 1:Yes },\_c0r,\_c0i,\_opacity

## Description:

Draw mandelbrot/julia fractal on selected images.  

## Default values:

iteration\_max=100, is\_julia=0, c0r=c0i=0 and opacity=1.

## Example of use:

400,400 mandelbrot -2.5,-2,2,2,1024 map 0 +blur 2 elevation3d[-1] -0.2

  

[![](img/t0_mandelbrot.jpg)](img/f0_mandelbrot.jpg)

Command: **400,400 mandelbrot -2.5,-2,2,2,1024 map 0 +blur 2 elevation3d[-1] -0.2**

[![](img/t1_mandelbrot.jpg)](img/f1_mandelbrot.jpg)

Command: **400,400 mandelbrot -2.5,-2,2,2,1024 map 0 +blur 2 elevation3d[-1] -0.2**

---

# Command: marble
**Category:** Image Drawing
**Source:** https://gmic.eu/reference/marble.html#top

# marble

## Arguments:

* \_image\_weight,\_pattern\_weight,\_angle,\_amplitude,\_sharpness>=0,\_anisotropy>=0,\_alpha,\_sigma,\_cut\_low>=0,\_cut\_high>=0

## Description:

Render marble like pattern on selected images.  

## Default values:

image\_weight=0.2, pattern\_weight=0.1, angle=45, amplitude=0, sharpness=0.4 and anisotropy=0.8,

  
alpha=0.6, sigma=1.1 and cut\_low=cut\_high=0.  

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +marble ,

  

[![](img/t0_marble.jpg)](img/f0_marble.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +marble ,**

[![](img/t1_marble.jpg)](img/f1_marble.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +marble ,**

---

# Command: maze
**Category:** Image Drawing
**Source:** https://gmic.eu/reference/maze.html#top

# maze

## Arguments:

* \_width>0,\_height>0,\_cell\_size>0

## Description:

Input maze with specified size.  

## Example of use:

maze 30,20 negate normalize 0,255

  
[![](img/t_maze.jpg)](img/f_maze.jpg)

Command: **maze 30,20 negate normalize 0,255**

---

# Command: maze_mask
**Category:** Image Drawing
**Source:** https://gmic.eu/reference/maze_mask.html#top

# maze\_mask

## Arguments:

* \_cellsize>0

## Description:

Input maze according to size and shape of selected mask images.  
  
Mask may contain disconnected shapes.  

## Example of use:

0 text "G'MIC",0,0,53,1,1 dilate 3 autocrop 0 frame xy,1,0 maze\_mask 8 dilate 3 negate mul 255

  
[![](img/t_maze_mask.jpg)](img/f_maze_mask.jpg)

Command: **0 text "G'MIC",0,0,53,1,1 dilate 3 autocrop 0 frame xy,1,0 maze\_mask 8 dilate 3 negate mul 255**

---

# Command: newton_fractal
**Category:** Image Drawing
**Source:** https://gmic.eu/reference/newton_fractal.html#top

# newton\_fractal

## Arguments:

* z0r,z0i,z1r,z1i,\_angle,0<=\_descent\_method<=2,\_iteration\_max>=0,\_convergence\_precision>0,\_expr\_p(z),\_expr\_dp(z),\_expr\_d2p(z)

## Description:

Draw newton fractal on selected images, for complex numbers in range (z0r,z0i) - (z1r,z1i).  
  
Resulting images have 3 channels whose meaning is [ last\_zr, last\_zi, nb\_iter\_used\_for\_convergence ].  
descent\_method can be { 0:Secant | 1:Newton | 2:Householder }.  

## Default values:

angle=0, descent\_method=1, iteration\_max=200, convergence\_precision=0.01, expr\_p(z)=z^^3-1, expr\_dp(z)=3\*z^^2 and expr\_d2z(z)=6\*z.

## Example of use:

400,400 newton\_fractal -1.5,-1.5,1.5,1.5,0,2,200,0.01,"z^^6 + z^^3 - 1","6\*z^^5 + 3\*z^^2","30\*z^^4 + 6\*z" f "[ atan2(i1,i0)\*90+20,1,cut(i2/30,0.2,0.7) ]" hsl2rgb

  
[![](img/t_newton_fractal.jpg)](img/f_newton_fractal.jpg)

Command: **400,400 newton\_fractal -1.5,-1.5,1.5,1.5,0,2,200,0.01,"z^^6 + z^^3 - 1","6\*z^^5 + 3\*z^^2","30\*z^^4 + 6\*z" f "[ atan2(i1,i0)\*90+20,1,cut(i2/30,0.2,0.7) ]" hsl2rgb**

---

# Command: pack_sprites
**Category:** Image Drawing
**Source:** https://gmic.eu/reference/pack_sprites.html#top

# pack\_sprites

## Arguments:

* [sprite\_set],\_nb\_scales>=1,0<\_min\_scale<=100,\_allow\_rotation={ 0:None | 1:180 deg. | 2:90 deg. | 3:Any },\_spacing,\_max\_attempts>0

## Description:

Try to randomly pack as many sprites as possible onto the empty areas of an image.  
  
Sprites can be eventually rotated and scaled during the packing process.  
Selected image is the canvas that will be filled with the sprites.  
The zero values of its alpha channel defines the potential locations for drawing the sprites.  
[sprite\_set] defines the set of sprites considered for filling the canvas.  
The zero values of their alpha channels defines the sprite shape.  
Sprite packing is done on random locations and iteratively with decreasing scales.  
nb\_scales sets the number of decreasing scales considered for all specified sprites to be packed.  
min\_scale (in %) sets the minimal size considered for packing (specified as a percentage of the  
original sprite size).  
spacing can be positive or negative.  
max\_attempts defines the maximum number of attempts to pack a sprite for each scale.  

## Default values:

nb\_scales=1, min\_scale=25, allow\_rotation=0, spacing=1 and max\_attempts=512.

## Example of use:

shape\_heart 512 negate normalize 0,255 channels -3,0 repeat 2 { ball 48,${-rgb} } +pack\_sprites[0] [^0],5,15

  

[![](img/t0_pack_sprites.jpg)](img/f0_pack_sprites.jpg)

Command: **shape\_heart 512 negate normalize 0,255 channels -3,0 repeat 2 { ball 48,${-rgb} } +pack\_sprites[0] [^0],5,15**

[![](img/t1_pack_sprites.jpg)](img/f1_pack_sprites.jpg)

Command: **shape\_heart 512 negate normalize 0,255 channels -3,0 repeat 2 { ball 48,${-rgb} } +pack\_sprites[0] [^0],5,15**

[![](img/t2_pack_sprites.jpg)](img/f2_pack_sprites.jpg)

Command: **shape\_heart 512 negate normalize 0,255 channels -3,0 repeat 2 { ball 48,${-rgb} } +pack\_sprites[0] [^0],5,15**

[![](img/t3_pack_sprites.jpg)](img/f3_pack_sprites.jpg)

Command: **shape\_heart 512 negate normalize 0,255 channels -3,0 repeat 2 { ball 48,${-rgb} } +pack\_sprites[0] [^0],5,15**

---

# Command: piechart
**Category:** Image Drawing
**Source:** https://gmic.eu/reference/piechart.html#top

# piechart

## Arguments:

* label\_height>=0,label\_R,label\_G,label\_B,"label1",value1,R1,G1,B1,...,"labelN",valueN,RN,GN,BN

## Description:

Draw pie chart on selected (RGB) images.  

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> piechart 25,0,0,0,"Red",55,255,0,0,"Green",40,0,255,0,"Blue",30,128,128,255,"Other",5,128,128,128

  
[![](img/t_piechart.jpg)](img/f_piechart.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> piechart 25,0,0,0,"Red",55,255,0,0,"Green",40,0,255,0,"Blue",30,128,128,255,"Other",5,128,128,128**

---

# Command: plasma
**Category:** Image Drawing
**Source:** https://gmic.eu/reference/plasma.html#top

# plasma

## Arguments:

* \_alpha,\_beta,\_scale>=0

## Description:

Draw a random colored plasma fractal on selected images.  
  
This command implements the so-called Diamond-Square algorithm.  

## Default values:

alpha=1, beta=1 and scale=8.

This command has a [tutorial page](https://gmic.eu/oldtutorial/_plasma).

## Example of use:

400,400,1,3 plasma 1

  
[![](img/t_plasma.jpg)](img/f_plasma.jpg)

Command: **400,400,1,3 plasma 1**

---

# Command: point
**Category:** Image Drawing
**Source:** https://gmic.eu/reference/point.html#top

|  |  |
| --- | --- |
| point | Built-in command |

## Arguments:

* x[%],\_y[%],\_z[%],\_opacity,\_color1,...

## Description:

Set specified colored pixel on selected images.  

## Default values:

z=0, opacity=1 and color1=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> repeat 10000 point {u(100)}%,{u(100)}%,0,1,${-rgb} done

  
[![](img/t_point.jpg)](img/f_point.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> repeat 10000 point {u(100)}%,{u(100)}%,0,1,${-rgb} done**

---

# Command: polka_dots
**Category:** Image Drawing
**Source:** https://gmic.eu/reference/polka_dots.html#top

# polka\_dots

## Arguments:

* diameter>=0,\_density,\_offset1,\_offset2,\_angle,\_aliasing,\_shading,\_opacity,\_color,...

## Description:

Draw dots pattern on selected images.  

## Default values:

density=20, offset1=offset2=50, angle=0, aliasing=10, shading=1, opacity=1 and color=255.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> polka\_dots 10,15,0,0,20,10,1,0.5,0,128,255

  
[![](img/t_polka_dots.jpg)](img/f_polka_dots.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> polka\_dots 10,15,0,0,20,10,1,0.5,0,128,255**

---

# Command: polygon
**Category:** Image Drawing
**Source:** https://gmic.eu/reference/polygon.html#top

|  |  |
| --- | --- |
| polygon | Built-in command |

## Arguments:

* N>=1,x1[%],y1[%],...,xN[%],yN[%],\_opacity,\_pattern,\_color1,...    or
* [coords],\_opacity,\_pattern,\_color1,...

## Description:

Draw specified colored N-vertices polygon on selected images.  
  
pattern is an hexadecimal number starting with 0x which can be omitted  
even if a color is specified. If a pattern is specified, the polygon is  
drawn outlined instead of filled.  
Adding a - sign before pattern makes the command draw an open polyline rather than a closed polygon.  

## Default values:

opacity=1, pattern=(undefined) and color1=0.

## Examples of use:

### • Example #1

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> polygon 4,20%,20%,80%,30%,80%,70%,20%,80%,0.3,0,255,0 polygon 4,20%,20%,80%,30%,80%,70%,20%,80%,1,0xCCCCCCCC,255

  
[![](img/t_polygon.jpg)](img/f_polygon.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> polygon 4,20%,20%,80%,30%,80%,70%,20%,80%,0.3,0,255,0 polygon 4,20%,20%,80%,30%,80%,70%,20%,80%,1,0xCCCCCCCC,255**

### • Example #2

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> 2,16,1,1,'u(x?h#0:w#0)' polygon[-2] [-1],0.6,255,0,255 remove[-1]

  
[![](img/t_polygon_2.jpg)](img/f_polygon_2.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> 2,16,1,1,'u(x?h#0:w#0)' polygon[-2] [-1],0.6,255,0,255 remove[-1]**

---

# Command: quiver
**Category:** Image Drawing
**Source:** https://gmic.eu/reference/quiver.html#top

# quiver

## Arguments:

* [function\_image],\_sampling[%]>0,\_factor>=0,\_is\_arrow={ 0:No | 1:Yes },\_opacity,\_color1,...

## Description:

Draw specified 2D vector/orientation field on selected images.  

## Default values:

sampling=5%, factor=1, is\_arrow=1, opacity=1, pattern=(undefined)

  
and color1=0.  

## Examples of use:

### • Example #1

100,100,1,2,'!c?x-w/2:y-h/2' 500,500,1,3,255 quiver[-1] [-2],10

  

[![](img/t0_quiver.jpg)](img/f0_quiver.jpg)

Command: **100,100,1,2,'!c?x-w/2:y-h/2' 500,500,1,3,255 quiver[-1] [-2],10**

[![](img/t1_quiver.jpg)](img/f1_quiver.jpg)

Command: **100,100,1,2,'!c?x-w/2:y-h/2' 500,500,1,3,255 quiver[-1] [-2],10**

### • Example #2

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +rescale2d ,600 luminance[0] gradient[0] mul[1] -1 reverse[0,1] append[0,1] c blur[0] 8 orientation[0] quiver[1] [0],20,1,1,0.8,255

  

[![](img/t0_quiver_2.jpg)](img/f0_quiver_2.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +rescale2d ,600 luminance[0] gradient[0] mul[1] -1 reverse[0,1] append[0,1] c blur[0] 8 orientation[0] quiver[1] [0],20,1,1,0.8,255**

[![](img/t1_quiver_2.jpg)](img/f1_quiver_2.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +rescale2d ,600 luminance[0] gradient[0] mul[1] -1 reverse[0,1] append[0,1] c blur[0] 8 orientation[0] quiver[1] [0],20,1,1,0.8,255**

---

# Command: rectangle
**Category:** Image Drawing
**Source:** https://gmic.eu/reference/rectangle.html#top

# rectangle

## Arguments:

* x0[%],y0[%],x1[%],y1[%],\_opacity,\_pattern,\_color1,...

## Description:

Draw specified colored rectangle on selected images.  
  
pattern is an hexadecimal number starting with 0x which can be omitted  
even if a color is specified. If a pattern is specified, the rectangle is  
drawn outlined instead of filled.  

## Default values:

opacity=1, pattern=(undefined) and color1=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> repeat 30 { rectangle {u(100)}%,{u(100)}%,{u(100)}%,{u(100)}%,0.3,${-rgb} }

  
[![](img/t_rectangle.jpg)](img/f_rectangle.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> repeat 30 { rectangle {u(100)}%,{u(100)}%,{u(100)}%,{u(100)}%,0.3,${-rgb} }**

---

# Command: rorschach
**Category:** Image Drawing
**Source:** https://gmic.eu/reference/rorschach.html#top

# rorschach

## Arguments:

* 'smoothness[%]>=0','mirroring={ 0:None | 1:X | 2:Y | 3:XY }

## Description:

Render rorschach-like inkblots on selected images.  

## Default values:

smoothness=5% and mirroring=1.

## Example of use:

400,400 rorschach 3%

  
[![](img/t_rorschach.jpg)](img/f_rorschach.jpg)

Command: **400,400 rorschach 3%**

---

# Command: sierpinski
**Category:** Image Drawing
**Source:** https://gmic.eu/reference/sierpinski.html#top

# sierpinski

## Arguments:

* recursion\_level>=0

## Description:

Draw Sierpinski triangle on selected images.  

## Default values:

recursion\_level=7.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> sierpinski 7

  
[![](img/t_sierpinski.jpg)](img/f_sierpinski.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> sierpinski 7**

---

# Command: spiralbw
**Category:** Image Drawing
**Source:** https://gmic.eu/reference/spiralbw.html#top

# spiralbw

## Arguments:

* width>0,\_height>0,\_is\_2dcoords={ 0:No | 1:Yes }

## Description:

Input a 2D rectangular spiral image with specified size.  

## Default values:

height=width and is\_2dcoords=0.

## Examples of use:

### • Example #1

spiralbw 16

  
[![](img/t_spiralbw.jpg)](img/f_spiralbw.jpg)

Command: **spiralbw 16**

### • Example #2

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> spiralbw {[w,h]},1 +warp[0] [1],0,1,1 +warp[2] [1],2,1,1

  

[![](img/t0_spiralbw_2.jpg)](img/f0_spiralbw_2.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> spiralbw {[w,h]},1 +warp[0] [1],0,1,1 +warp[2] [1],2,1,1**

[![](img/t1_spiralbw_2.jpg)](img/f1_spiralbw_2.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> spiralbw {[w,h]},1 +warp[0] [1],0,1,1 +warp[2] [1],2,1,1**

[![](img/t2_spiralbw_2.jpg)](img/f2_spiralbw_2.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> spiralbw {[w,h]},1 +warp[0] [1],0,1,1 +warp[2] [1],2,1,1**

[![](img/t3_spiralbw_2.jpg)](img/f3_spiralbw_2.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> spiralbw {[w,h]},1 +warp[0] [1],0,1,1 +warp[2] [1],2,1,1**

---

# Command: tetraedron_shade
**Category:** Image Drawing
**Source:** https://gmic.eu/reference/tetraedron_shade.html#top

# tetraedron\_shade

## Arguments:

* x0,y0,z0,x1,y1,z1,x2,y2,z2,x3,y3,z3,R0,G0,B0,...,R1,G1,B1,...,R2,G2,B2,...,R3,G3,B3,...

## Description:

Draw tetraedron with interpolated colors on selected (volumetric) images.

---

# Command: text
**Category:** Image Drawing
**Source:** https://gmic.eu/reference/text.html#top

|  |  |
| --- | --- |
| text | Built-in command |

## Arguments:

* text,\_x[%|~],\_y[%|~],\_{ font\_height[%]>=0 | custom\_font },\_opacity,\_color1,...

## Description:

Draw specified colored text string on selected images.  

(*equivalent to shortcut command* t).

  
If one of the x or y argument ends with a ~, its value is expected to be a centering ratio (in [0,1]) rather than a position.  
Usual centering ratio are { 0:left-justified | 0.5:centered | 1:right-justified }.  
Sizes 13 and 128 are special and correspond to binary fonts (no-antialiasing). Any other font size is rendered with anti-aliasing.  
Specifying an empty target image resizes it to new dimensions such that the image contains the entire text string.  
A custom font can be specified as a variable name that stores an image list of 256 or 512 items (512 for 256 character sprites + 256 associated opacities), or as an image selection that is a serialized version of such an image list.  

## Default values:

x=y=0.01~, font\_height=16, opacity=1 and color1=0.

## Examples of use:

### • Example #1

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rescale2d ,600 div 2 y=0 repeat 30 { text {2\*$>}" : This is a nice text!",10,$y,{2\*$>},0.9,255 y+={2\*$>} }

  
[![](img/t_text.jpg)](img/f_text.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rescale2d ,600 div 2 y=0 repeat 30 { text {2\*$>}" : This is a nice text!",10,$y,{2\*$>},0.9,255 y+={2\*$>} }**

### • Example #2

0 text "G'MIC",0,0,23,1,255

  
[![](img/t_text_2.jpg)](img/f_text_2.jpg)

Command: **0 text "G'MIC",0,0,23,1,255**

---

# Command: text_outline
**Category:** Image Drawing
**Source:** https://gmic.eu/reference/text_outline.html#top

# text\_outline

## Arguments:

* text,\_x[%|~],\_y[%|~],{ \_font\_height[%]>0 | custom\_font },\_outline>=0,\_opacity,\_color1,...

## Description:

Draw specified colored and outlined text string on selected images.  
  
If one of the x or y argument ends with a ~, its value is expected to be  
a centering ratio (in [0,1]) rather than a position.  
Usual centering ratio are { 0:left-justified | 0.5:centered | 1:right-justified }.  

## Default values:

x=y=0.01~, font\_height=7.5%, outline=2, opacity=1, color1=color2=color3=255 and color4=255.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> text\_outline "Hi there!",10,10,63,3

  
[![](img/t_text_outline.jpg)](img/f_text_outline.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> text\_outline "Hi there!",10,10,63,3**

---

# Command: triangle_shade
**Category:** Image Drawing
**Source:** https://gmic.eu/reference/triangle_shade.html#top

# triangle\_shade

## Arguments:

* x0,y0,x1,y1,x2,y2,R0,G0,B0,...,R1,G1,B1,...,R2,G2,B2,...

## Description:

Draw triangle with interpolated colors on selected images.  

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> triangle\_shade 20,20,400,100,120,200,255,0,0,0,255,0,0,0,255

  
[![](img/t_triangle_shade.jpg)](img/f_triangle_shade.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> triangle\_shade 20,20,400,100,120,200,255,0,0,0,255,0,0,0,255**

---

# Command: truchet
**Category:** Image Drawing
**Source:** https://gmic.eu/reference/truchet.html#top

# truchet

## Arguments:

* \_scale>0,\_radius>=0,\_pattern\_type={ 0:Straight | 1:Curved }

## Description:

Fill selected images with random truchet patterns.  

## Default values:

scale=32, radius=5 and pattern\_type=1.

## Example of use:

400,300 truchet ,

  
[![](img/t_truchet.jpg)](img/f_truchet.jpg)

Command: **400,300 truchet ,**

---

# Command: turbulence
**Category:** Image Drawing
**Source:** https://gmic.eu/reference/turbulence.html#top

# turbulence

## Arguments:

* \_radius>0,\_octaves={ 1,2,3...,12 },\_alpha>0,\_difference={ -10,10 },\_mode={ 0,1,2,3 }

## Description:

Render fractal noise or turbulence on selected images.  

## Default values:

radius=32, octaves=6, alpha=3, difference=0 and mode=0.

This command has a [tutorial page](https://gmic.eu/oldtutorial/_turbulence).

## Example of use:

400,400,1,3 turbulence 16

  
[![](img/t_turbulence.jpg)](img/f_turbulence.jpg)

Command: **400,400,1,3 turbulence 16**

---

# Command: yinyang
**Category:** Image Drawing
**Source:** https://gmic.eu/reference/yinyang.html#top

# yinyang

### No argumentsDescription:Draw a yin-yang symbol on selected images. Example of use: 400,400 yinyang Command: **400,400 yinyang**

---

# Command: boxfitting
**Category:** Artistic
**Source:** https://gmic.eu/reference/boxfitting.html#top

# boxfitting

## Arguments:

* \_min\_box\_size>=1,\_max\_box\_size>=0,\_initial\_density>=0,\_min\_spacing>0

## Description:

Apply box fitting effect on selected images, as displayed the web page:  
  
<http://www.complexification.net/gallery/machines/boxFittingImg/>.  

## Default values:

min\_box\_size=1, max\_box\_size=0, initial\_density=0.25 and min\_spacing=1.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> boxfitting ,

  
[![](img/t_boxfitting.jpg)](img/f_boxfitting.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> boxfitting ,**

---

# Command: brushify
**Category:** Artistic
**Source:** https://gmic.eu/reference/brushify.html#top

# brushify

## Arguments:

* [brush],\_brush\_nb\_sizes>=1,0<=\_brush\_min\_size\_factor<=1,\_brush\_nb\_orientations>=1,\_brush\_light\_type,0<=\_brush\_light\_strength<=1,\_brush\_opacity,\_painting\_density[%]>=0,0<=\_painting\_contours\_coherence<=1,0<=\_painting\_orientation\_coherence<=1,\_painting\_coherence\_alpha[%]>=0,\_painting\_coherence\_sigma[%]>=0,\_painting\_primary\_angle,0<=\_painting\_angle\_dispersion<=1

## Description:

Apply specified brush to create painterly versions of specified images.  
  
brush\_light\_type can be { 0:None | 1:Flat | 2:Darken | 3:Lighten | 4:Full }.  

## Default values:

brush\_nb\_sizes=3, brush\_min\_size\_factor=0.66, brush\_nb\_orientations=12, brush\_light\_type=0, brush\_light\_strength=0.25, brush\_opacity=0.8, painting\_density=20%, painting\_contours\_coherence=0.9, painting\_orientation\_coherence=0.9, painting\_coherence\_alpha=1, painting\_coherence\_sigma=1, painting\_primary\_angle=0, painting\_angle\_dispersion=0.2

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> 40,40 gaussian[-1] 10,4 spread[-1] 10,0 brushify[0] [1],1

  

[![](img/t0_brushify.jpg)](img/f0_brushify.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> 40,40 gaussian[-1] 10,4 spread[-1] 10,0 brushify[0] [1],1**

[![](img/t1_brushify.jpg)](img/f1_brushify.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> 40,40 gaussian[-1] 10,4 spread[-1] 10,0 brushify[0] [1],1**

---

# Command: cartoon
**Category:** Artistic
**Source:** https://gmic.eu/reference/cartoon.html#top

# cartoon

## Arguments:

* \_smoothness,\_sharpening,\_threshold>=0,\_thickness>=0,\_color>=0,quantization>0

## Description:

Apply cartoon effect on selected images.  

## Default values:

smoothness=3, sharpening=150, threshold=20, thickness=0.25, color=1.5 and quantization=8.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> cartoon 3,50,10,0.25,3,16

  
[![](img/t_cartoon.jpg)](img/f_cartoon.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> cartoon 3,50,10,0.25,3,16**

---

# Command: color_ellipses
**Category:** Artistic
**Source:** https://gmic.eu/reference/color_ellipses.html#top

# color\_ellipses

## Arguments:

* \_count>0,\_radius>=0,\_opacity>=0

## Description:

Add random color ellipses to selected images.  

## Default values:

count=400, radius=5 and opacity=0.1.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +color\_ellipses ,,0.15

  

[![](img/t0_color_ellipses.jpg)](img/f0_color_ellipses.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +color\_ellipses ,,0.15**

[![](img/t1_color_ellipses.jpg)](img/f1_color_ellipses.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +color\_ellipses ,,0.15**

---

# Command: cubism
**Category:** Artistic
**Source:** https://gmic.eu/reference/cubism.html#top

# cubism

## Arguments:

* \_density>=0,0<=\_thickness<=50,\_max\_angle,\_opacity,\_smoothness>=0

## Description:

Apply cubism effect on selected images.  

## Default values:

density=50, thickness=10, max\_angle=75, opacity=0.7 and smoothness=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> cubism ,

  
[![](img/t_cubism.jpg)](img/f_cubism.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> cubism ,**

---

# Command: draw_whirl
**Category:** Artistic
**Source:** https://gmic.eu/reference/draw_whirl.html#top

# draw\_whirl

## Arguments:

* \_amplitude>=0

## Description:

Apply whirl drawing effect on selected images.  

## Default values:

amplitude=100.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> draw\_whirl ,

  
[![](img/t_draw_whirl.jpg)](img/f_draw_whirl.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> draw\_whirl ,**

---

# Command: drop_shadow
**Category:** Artistic
**Source:** https://gmic.eu/reference/drop_shadow.html#top

# drop\_shadow

## Arguments:

* \_offset\_x[%],\_offset\_y[%],\_smoothness[%]>=0,curvature\_x>=0,curvature\_y>=0,\_expand\_size={ 0:No | 1:Yes },\_output\_separate\_layers={ 0:No | 1:Yes }

## Description:

Drop shadow behind selected images.  

## Default values:

offset\_x=20, offset\_y=offset\_x, smoothness=5, curvature\_x=curvature\_y=0, expand\_size=1 and output\_separate\_layers=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> drop\_shadow 10,20,5,0.5 display\_rgba

  
[![](img/t_drop_shadow.jpg)](img/f_drop_shadow.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> drop\_shadow 10,20,5,0.5 display\_rgba**

---

# Command: drop_shadow
**Category:** Artistic
**Source:** https://gmic.eu/reference/drop_shadow.html#top

# drop\_shadow

## Arguments:

* \_offset\_x[%],\_offset\_y[%],\_smoothness[%]>=0,curvature\_x>=0,curvature\_y>=0,\_expand\_size={ 0:No | 1:Yes },\_output\_separate\_layers={ 0:No | 1:Yes }

## Description:

Drop shadow behind selected images.  

## Default values:

offset\_x=20, offset\_y=offset\_x, smoothness=5, curvature\_x=curvature\_y=0, expand\_size=1 and output\_separate\_layers=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> drop\_shadow 10,20,5,0.5 display\_rgba

  
[![](img/t_drop_shadow.jpg)](img/f_drop_shadow.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> drop\_shadow 10,20,5,0.5 display\_rgba**

---

# Command: ellipsionism
**Category:** Artistic
**Source:** https://gmic.eu/reference/ellipsionism.html#top

# ellipsionism

## Arguments:

* \_R[%]>0,\_r[%]>0,\_smoothness[%]>=0,\_opacity,\_outline>0,\_density>0

## Description:

Apply ellipsionism filter to selected images.  

## Default values:

R=10, r=3, smoothness=1%, opacity=0.7, outline=8 and density=0.6.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> ellipsionism ,

  
[![](img/t_ellipsionism.jpg)](img/f_ellipsionism.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> ellipsionism ,**

---

# Command: fire_edges
**Category:** Artistic
**Source:** https://gmic.eu/reference/fire_edges.html#top

# fire\_edges

## Arguments:

* \_edges>=0,0<=\_attenuation<=1,\_smoothness>=0,\_threshold>=0,\_nb\_frames>0,\_starting\_frame>=0,frame\_skip>=0

## Description:

Generate fire effect from edges of selected images.  

## Default values:

edges=0.7, attenuation=0.25, smoothness=0.5, threshold=25, nb\_frames=1, starting\_frame=20 and frame\_skip=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> fire\_edges ,

  
[![](img/t_fire_edges.jpg)](img/f_fire_edges.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> fire\_edges ,**

---

# Command: fractalize
**Category:** Artistic
**Source:** https://gmic.eu/reference/fractalize.html#top

# fractalize

## Arguments:

* 0<=detail\_level<=1

## Description:

Randomly fractalize selected images.  

## Default values:

detail\_level=0.8

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> fractalize ,

  
[![](img/t_fractalize.jpg)](img/f_fractalize.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> fractalize ,**

---

# Command: glow
**Category:** Artistic
**Source:** https://gmic.eu/reference/glow.html#top

# glow

## Arguments:

* \_amplitude>=0

## Description:

Add soft glow on selected images.  

## Default values:

amplitude=1%.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> glow ,

  
[![](img/t_glow.jpg)](img/f_glow.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> glow ,**

---

# Command: halftone
**Category:** Artistic
**Source:** https://gmic.eu/reference/halftone.html#top

# halftone

## Arguments:

* nb\_levels>=2,\_size\_dark>=2,\_size\_bright>=2,\_shape={ 0:Square | 1:Diamond | 2:Circle | 3:inv-square | 4:inv-diamond | 5:inv-circle },\_smoothness[%]>=0

## Description:

Apply halftone dithering to selected images.  

## Default values:

nb\_levels=5, size\_dark=8, size\_bright=8, shape=5 and smoothnesss=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> halftone ,

  
[![](img/t_halftone.jpg)](img/f_halftone.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> halftone ,**

---

# Command: hardsketchbw
**Category:** Artistic
**Source:** https://gmic.eu/reference/hardsketchbw.html#top

# hardsketchbw

## Arguments:

* \_amplitude>=0,\_density>=0,\_opacity,0<=\_edge\_threshold<=100,\_is\_fast={ 0:No | 1:Yes }

## Description:

Apply hard B&W sketch effect on selected images.  

## Default values:

amplitude=1000, sampling=3, opacity=0.1, edge\_threshold=20 and is\_fast=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +hardsketchbw 200,70,0.1,10 median[-1] 2 +local reverse blur[-1] 3 blend[-2,-1] overlay done

  

[![](img/t0_hardsketchbw.jpg)](img/f0_hardsketchbw.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +hardsketchbw 200,70,0.1,10 median[-1] 2 +local reverse blur[-1] 3 blend[-2,-1] overlay done**

[![](img/t1_hardsketchbw.jpg)](img/f1_hardsketchbw.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +hardsketchbw 200,70,0.1,10 median[-1] 2 +local reverse blur[-1] 3 blend[-2,-1] overlay done**

[![](img/t2_hardsketchbw.jpg)](img/f2_hardsketchbw.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +hardsketchbw 200,70,0.1,10 median[-1] 2 +local reverse blur[-1] 3 blend[-2,-1] overlay done**

---

# Command: hearts
**Category:** Artistic
**Source:** https://gmic.eu/reference/hearts.html#top

# hearts

## Arguments:

* \_density>=0

## Description:

Apply heart effect on selected images.  

## Default values:

density=10.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> hearts ,

  
[![](img/t_hearts.jpg)](img/f_hearts.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> hearts ,**

---

# Command: houghsketchbw
**Category:** Artistic
**Source:** https://gmic.eu/reference/houghsketchbw.html#top

# houghsketchbw

## Arguments:

* \_density>=0,\_radius>0,0<=\_threshold<=100,0<=\_opacity<=1,\_votesize[%]>0

## Description:

Apply hough B&W sketch effect on selected images.  

## Default values:

density=100, radius=3, threshold=100, opacity=0.1 and votesize=100%.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +houghsketchbw ,

  

[![](img/t0_houghsketchbw.jpg)](img/f0_houghsketchbw.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +houghsketchbw ,**

[![](img/t1_houghsketchbw.jpg)](img/f1_houghsketchbw.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +houghsketchbw ,**

---

# Command: lightrays
**Category:** Artistic
**Source:** https://gmic.eu/reference/lightrays.html#top

# lightrays

## Arguments:

* 100<=\_density<=0,\_center\_x[%],\_center\_y[%],\_ray\_length>=0,\_ray\_attenuation>=0

## Description:

Generate ray lights from the edges of selected images.  

## Default values:

density=50%, center\_x=50%, center\_y=50%, ray\_length=0.9 and ray\_attenuation=0.5.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +lightrays , + cut 0,255

  
[![](img/t_lightrays.jpg)](img/f_lightrays.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +lightrays , + cut 0,255**

---

# Command: light_relief
**Category:** Artistic
**Source:** https://gmic.eu/reference/light_relief.html#top

# light\_relief

## Arguments:

* \_ambient\_light,\_specular\_lightness,\_specular\_size,\_darkness,\_light\_smoothness,\_xl,\_yl,\_zl,\_zscale,\_opacity\_is\_heightmap={ 0:No | 1:Yes }

## Description:

Apply relief light to selected images.  
  
Default values(s) : ambient\_light=0.3, specular\_lightness=0.5, specular\_size=0.2, darkness=0, xl=0.2, yl=zl=0.5,  
zscale=1, opacity=1 and opacity\_is\_heightmap=0.  

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> blur 2 light\_relief 0.3,4,0.1,0

  
[![](img/t_light_relief.jpg)](img/f_light_relief.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> blur 2 light\_relief 0.3,4,0.1,0**

---

# Command: linify
**Category:** Artistic
**Source:** https://gmic.eu/reference/linify.html#top

# linify

## Arguments:

* 0<=\_density<=100,\_spreading>=0,\_resolution[%]>0,\_line\_opacity>=0,\_line\_precision>0,\_mode={ 0:Subtractive | 1:Additive }

## Description:

Apply linify effect on selected images.  
  
The algorithm is inspired from the one described on the webpage <http://linify.me/about>.  

## Default values:

density=50, spreading=2, resolution=40%, line\_opacity=10, line\_precision=24 and mode=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> linify 60

  
[![](img/t_linify.jpg)](img/f_linify.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> linify 60**

---

# Command: mosaic
**Category:** Artistic
**Source:** https://gmic.eu/reference/mosaic.html#top

# mosaic

## Arguments:

* 0<=\_density<=100

## Description:

Create random mosaic from selected images.  

## Default values:

density=30.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> mosaic , +fill "I!=J(1) || I!=J(0,1)?[0,0,0]:I"

  

[![](img/t0_mosaic.jpg)](img/f0_mosaic.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> mosaic , +fill "I!=J(1) || I!=J(0,1)?[0,0,0]:I"**

[![](img/t1_mosaic.jpg)](img/f1_mosaic.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> mosaic , +fill "I!=J(1) || I!=J(0,1)?[0,0,0]:I"**

---

# Command: old_photo
**Category:** Artistic
**Source:** https://gmic.eu/reference/old_photo.html#top

# old\_photo

### No argumentsDescription:Apply old photo effect on selected images. Example of use: <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> old\_photo Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> old\_photo**

---

# Command: pencilbw
**Category:** Artistic
**Source:** https://gmic.eu/reference/pencilbw.html#top

# pencilbw

## Arguments:

* \_size>=0,\_amplitude>=0

## Description:

Apply B&W pencil effect on selected images.  

## Default values:

size=0.3 and amplitude=60.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> pencilbw ,

  
[![](img/t_pencilbw.jpg)](img/f_pencilbw.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> pencilbw ,**

---

# Command: pixelsort
**Category:** Artistic
**Source:** https://gmic.eu/reference/pixelsort.html#top

# pixelsort

## Arguments:

* \_ordering={ +:Increasing | -:Decreasing },\_axis={ x | y | z | xy | yx },\_[sorting\_criterion],\_[mask]

## Description:

Apply a pixel sorting algorithm on selected images, as described in the page :  
  
<http://satyarth.me/articles/pixel-sorting/>.  

## Default values:

ordering=+, axis=x and sorting\_criterion=mask=(undefined).

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +norm +ge[-1] 30% +pixelsort[0] +,y,[1],[2]

  

[![](img/t0_pixelsort.jpg)](img/f0_pixelsort.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +norm +ge[-1] 30% +pixelsort[0] +,y,[1],[2]**

[![](img/t1_pixelsort.jpg)](img/f1_pixelsort.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +norm +ge[-1] 30% +pixelsort[0] +,y,[1],[2]**

[![](img/t2_pixelsort.jpg)](img/f2_pixelsort.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +norm +ge[-1] 30% +pixelsort[0] +,y,[1],[2]**

[![](img/t3_pixelsort.jpg)](img/f3_pixelsort.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +norm +ge[-1] 30% +pixelsort[0] +,y,[1],[2]**

---

# Command: polaroid
**Category:** Artistic
**Source:** https://gmic.eu/reference/polaroid.html#top

# polaroid

## Arguments:

* \_size1>=0,\_size2>=0

## Description:

Create polaroid effect in selected images.  

## Default values:

size1=10 and size2=20.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> to\_rgba polaroid 5,30 rotate 20 drop\_shadow , drgba

  
[![](img/t_polaroid.jpg)](img/f_polaroid.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> to\_rgba polaroid 5,30 rotate 20 drop\_shadow , drgba**

---

# Command: polygonize
**Category:** Artistic
**Source:** https://gmic.eu/reference/polygonize.html#top

# polygonize

## Arguments:

* \_warp\_amplitude>=0,\_smoothness[%]>=0,\_min\_area[%]>=0,\_resolution\_x[%]>0,\_resolution\_y[%]>0

## Description:

Apply polygon effect on selected images.  

## Default values:

warp\_amplitude=300, smoothness=2%, min\_area=0.1%, resolution\_x=resolution\_y=10%.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +polygonize 100,10 fill[-1] "I!=J(1) || I!=J(0,1)?[0,0,0]:I"

  

[![](img/t0_polygonize.jpg)](img/f0_polygonize.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +polygonize 100,10 fill[-1] "I!=J(1) || I!=J(0,1)?[0,0,0]:I"**

[![](img/t1_polygonize.jpg)](img/f1_polygonize.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +polygonize 100,10 fill[-1] "I!=J(1) || I!=J(0,1)?[0,0,0]:I"**

---

# Command: poster_edges
**Category:** Artistic
**Source:** https://gmic.eu/reference/poster_edges.html#top

# poster\_edges

## Arguments:

* 0<=\_edge\_threshold<=100,0<=\_edge\_shade<=100,\_edge\_thickness>=0,\_edge\_antialiasing>=0,0<=\_posterization\_level<=15,\_posterization\_antialiasing>=0

## Description:

Apply poster edges effect on selected images.  

## Default values:

edge\_threshold=40, edge\_shade=5, edge\_thickness=0.5, edge\_antialiasing=10, posterization\_level=12 and posterization\_antialiasing=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> poster\_edges ,

  
[![](img/t_poster_edges.jpg)](img/f_poster_edges.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> poster\_edges ,**

---

# Command: poster_hope
**Category:** Artistic
**Source:** https://gmic.eu/reference/poster_hope.html#top

# poster\_hope

## Arguments:

* \_smoothness>=0

## Description:

Apply Hope stencil poster effect on selected images.  

## Default values:

smoothness=3.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> poster\_hope ,

  
[![](img/t_poster_hope.jpg)](img/f_poster_hope.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> poster\_hope ,**

---

# Command: rodilius
**Category:** Artistic
**Source:** https://gmic.eu/reference/rodilius.html#top

# rodilius

## Arguments:

* 0<=\_amplitude<=100,\_0<=thickness<=100,\_sharpness>=0,\_nb\_orientations>0,\_offset,\_color\_mode={ 0:Darker | 1:Brighter }

## Description:

Apply rodilius (fractalius-like) filter on selected images.  

## Default values:

amplitude=10, thickness=10, sharpness=400, nb\_orientations=7, offset=0 and color\_mode=1.

## Examples of use:

### • Example #1

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rodilius 12,10,300,10 normalize\_local 10,6

  
[![](img/t_rodilius.jpg)](img/f_rodilius.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> rodilius 12,10,300,10 normalize\_local 10,6**

### • Example #2

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> normalize\_local 10,16 rodilius 10,4,400,16 smooth 60,0,1,1,4 normalize\_local 10,16

  
[![](img/t_rodilius_2.jpg)](img/f_rodilius_2.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> normalize\_local 10,16 rodilius 10,4,400,16 smooth 60,0,1,1,4 normalize\_local 10,16**

---

# Command: sketchbw
**Category:** Artistic
**Source:** https://gmic.eu/reference/sketchbw.html#top

# sketchbw

## Arguments:

* \_nb\_angles>0,\_start\_angle,\_angle\_range>=0,\_length>=0,\_threshold>=0,\_opacity,\_bgfactor>=0,\_density>0,\_sharpness>=0,\_anisotropy>=0,\_smoothness>=0,\_coherence>=0,\_is\_boost={ 0:No | 1:Yes },\_is\_curved={ 0:No | 1:Yes }

## Description:

Apply sketch effect to selected images.  

## Default values:

nb\_angles=2, start\_angle=45, angle\_range=180, length=30, threshold=3, opacity=0.03, bgfactor=0, density=0.6, sharpness=0.1, anisotropy=0.6, smoothness=0.25, coherence=1, is\_boost=0 and is\_curved=1.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +sketchbw 1 reverse blur[-1] 3 blend[-2,-1] overlay

  
[![](img/t_sketchbw.jpg)](img/f_sketchbw.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +sketchbw 1 reverse blur[-1] 3 blend[-2,-1] overlay**

---

# Command: sponge
**Category:** Artistic
**Source:** https://gmic.eu/reference/sponge.html#top

# sponge

## Arguments:

* \_size>0

## Description:

Apply sponge effect on selected images.  

## Default values:

size=13.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> sponge ,

  
[![](img/t_sponge.jpg)](img/f_sponge.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> sponge ,**

---

# Command: stained_glass
**Category:** Artistic
**Source:** https://gmic.eu/reference/stained_glass.html#top

# stained\_glass

## Arguments:

* \_edges[%]>=0, shading>=0, is\_thin\_separators={ 0:No | 1:Yes }

## Description:

Generate stained glass from selected images.  

## Default values:

edges=40%, shading=0.2 and is\_precise=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> stained\_glass 20%,1 cut 0,20

  
[![](img/t_stained_glass.jpg)](img/f_stained_glass.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> stained\_glass 20%,1 cut 0,20**

---

# Command: stars
**Category:** Artistic
**Source:** https://gmic.eu/reference/stars.html#top

# stars

## Arguments:

* \_density[%]>=0,\_depth>=0,\_size>0,\_nb\_branches>=1,0<=\_thickness<=1,\_smoothness[%]>=0,\_R,\_G,\_B,\_opacity

## Description:

Add random stars to selected images.  

## Default values:

density=10%, depth=1, size=32, nb\_branches=5, thickness=0.38, smoothness=0.5, R=G=B=200 and opacity=1.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> stars ,

  
[![](img/t_stars.jpg)](img/f_stars.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> stars ,**

---

# Command: stencil
**Category:** Artistic
**Source:** https://gmic.eu/reference/stencil.html#top

# stencil

## Arguments:

* \_radius[%]>=0,\_smoothness>=0,\_iterations>=0

## Description:

Apply stencil filter on selected images.  

## Default values:

radius=3, smoothness=1 and iterations=8.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +norm stencil. 2,1,4 +mul rm[0]

  

[![](img/t0_stencil.jpg)](img/f0_stencil.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +norm stencil. 2,1,4 +mul rm[0]**

[![](img/t1_stencil.jpg)](img/f1_stencil.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +norm stencil. 2,1,4 +mul rm[0]**

---

# Command: stencilbw
**Category:** Artistic
**Source:** https://gmic.eu/reference/stencilbw.html#top

# stencilbw

## Arguments:

* \_edges>=0,\_smoothness>=0

## Description:

Apply B&W stencil effect on selected images.  

## Default values:

edges=15 and smoothness=10.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +stencilbw 40,4

  

[![](img/t0_stencilbw.jpg)](img/f0_stencilbw.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +stencilbw 40,4**

[![](img/t1_stencilbw.jpg)](img/f1_stencilbw.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +stencilbw 40,4**

---

# Command: stylize
**Category:** Artistic
**Source:** https://gmic.eu/reference/stylize.html#top

# stylize

## Arguments:

* [style\_image],\_fidelity\_finest,\_fidelity\_coarsest,\_fidelity\_smoothness\_finest>=0,\_fidelity\_smoothnes\_coarsest>=0,0<=\_fidelity\_chroma<=1,\_init\_type,\_init\_resolution>=0,init\_max\_gradient>=0,\_patch\_size\_analysis>0,\_patch\_size\_synthesis>0,\_patch\_size\_synthesis\_final>0,\_nb\_matches\_finest>=0,\_nb\_matches\_coarsest>=0,\_penalize\_repetitions>=0,\_matching\_precision>=0,\_scale\_factor>1,\_skip\_finest\_scales>=0,\_"image\_matching\_command"

## Description:

Transfer colors and textures from specified style image to selected images, using a multi-scale patch-mathing algorithm.  
  
If instant display window[0] is opened, the steps of the image synthesis are displayed on it.  
init\_type can be { 0:Best-match | 1:Identity | 2:Randomized }.  

## Default values:

fidelity\_finest=0.5, fidelity\_coarsest=2, fidelity\_smoothness\_finest=3, fidelity\_smoothness\_coarsest=0.5, fidelity\_chroma=0.1, init\_type=0, init\_resolution=16, init\_max\_gradient=0, patch\_size\_analysis=5, patch\_size\_synthesis=5, patch\_size\_synthesis\_final=5, nb\_matches\_finest=2, nb\_matchesc\_coarsest=30, penalize\_repetitions=2, matching\_precision=2, scale\_factor=1.85, skip\_finest\_scales=0 and 'image\_matching\_command'="s c,-3 match\_pca[0] [2] b[0,2] xy,0.7 n[0,2] 0,255 n[1,2] 0,200 a[0,1] c a[1,2] c"'.

---

# Command: tetris
**Category:** Artistic
**Source:** https://gmic.eu/reference/tetris.html#top

# tetris

## Arguments:

* \_scale>0

## Description:

Apply tetris effect on selected images.  

## Default values:

scale=10.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +tetris 10

  

[![](img/t0_tetris.jpg)](img/f0_tetris.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +tetris 10**

[![](img/t1_tetris.jpg)](img/f1_tetris.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +tetris 10**

---

# Command: warhol
**Category:** Artistic
**Source:** https://gmic.eu/reference/warhol.html#top

# warhol

## Arguments:

* \_M>0,\_N>0,\_smoothness>=0,\_color>=0

## Description:

Create MxN Andy Warhol-like artwork from selected images.  

## Default values:

M=3, N=M, smoothness=2 and color=20.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> warhol 3,3,3,40

  
[![](img/t_warhol.jpg)](img/f_warhol.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> warhol 3,3,3,40**

---

# Command: weave
**Category:** Artistic
**Source:** https://gmic.eu/reference/weave.html#top

# weave

## Arguments:

* \_density>=0,0<=\_thickness<=100,0<=\_shadow<=100,\_shading>=0,\_fibers\_amplitude>=0,\_fibers\_smoothness>=0,\_angle,-1<=\_x\_curvature<=1,-1<=\_y\_curvature<=1

## Description:

Apply weave effect to the selected images.  
  
angle can be { 0:0 deg. | 1:22.5 deg. | 2:45 deg. | 3:67.5 deg. }.  

## Default values:

density=6, thickness=65, shadow=40, shading=0.5, fibers\_amplitude=0, \_'fibers\_smoothness=0', angle=0 and curvature\_x=curvature\_y=0

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> weave ,

  
[![](img/t_weave.jpg)](img/f_weave.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> weave ,**

---

# Command: whirls
**Category:** Artistic
**Source:** https://gmic.eu/reference/whirls.html#top

# whirls

## Arguments:

* \_texture>=0,\_smoothness>=0,\_darkness>=0,\_lightness>=0

## Description:

Add random whirl texture to selected images.  

## Default values:

texture=3, smoothness=6, darkness=0.5 and lightness=1.8.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> whirls ,

  
[![](img/t_whirls.jpg)](img/f_whirls.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> whirls ,**

---

# Command: deform
**Category:** Warpings
**Source:** https://gmic.eu/reference/deform.html#top

# deform

## Arguments:

* \_amplitude[%]>=0,\_interpolation

## Description:

Apply random smooth deformation on selected images.  
  
interpolation can be { 0:None | 1:Linear | 2:Bicubic }.  

## Default values:

amplitude=10.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +deform[0] 10 +deform[0] 20

  

[![](img/t0_deform.jpg)](img/f0_deform.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +deform[0] 10 +deform[0] 20**

[![](img/t1_deform.jpg)](img/f1_deform.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +deform[0] 10 +deform[0] 20**

[![](img/t2_deform.jpg)](img/f2_deform.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +deform[0] 10 +deform[0] 20**

---

# Command: euclidean2polar
**Category:** Warpings
**Source:** https://gmic.eu/reference/euclidean2polar.html#top

# euclidean2polar

## Arguments:

* \_center\_x[%],\_center\_y[%],\_stretch\_factor>0,\_boundary\_conditions={ 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }

## Description:

Apply euclidean to polar transform on selected images.  

## Default values:

center\_x=center\_y=50%, stretch\_factor=1 and boundary\_conditions=3.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +euclidean2polar ,

  

[![](img/t0_euclidean2polar.jpg)](img/f0_euclidean2polar.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +euclidean2polar ,**

[![](img/t1_euclidean2polar.jpg)](img/f1_euclidean2polar.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +euclidean2polar ,**

---

# Command: equirectangular2nadirzenith
**Category:** Warpings
**Source:** https://gmic.eu/reference/equirectangular2nadirzenith.html#top

# equirectangular2nadirzenith

### No argumentsDescription:Transform selected equirectangular images to nadir/zenith rectilinear projections.

---

# Command: fisheye
**Category:** Warpings
**Source:** https://gmic.eu/reference/fisheye.html#top

# fisheye

## Arguments:

* \_center\_x,\_center\_y,0<=\_radius<=100,\_amplitude>=0

## Description:

Apply fish-eye deformation on selected images.  

## Default values:

x=y=50, radius=50 and amplitude=1.2.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +fisheye ,

  

[![](img/t0_fisheye.jpg)](img/f0_fisheye.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +fisheye ,**

[![](img/t1_fisheye.jpg)](img/f1_fisheye.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +fisheye ,**

---

# Command: flower
**Category:** Warpings
**Source:** https://gmic.eu/reference/flower.html#top

# flower

## Arguments:

* \_amplitude,\_frequency,\_offset\_r[%],\_angle,\_center\_x[%],\_center\_y[%],\_boundary\_conditions={ 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }

## Description:

Apply flower deformation on selected images.  

## Default values:

amplitude=30, frequency=6, offset\_r=0, angle=0, center\_x=center\_y=50% and boundary\_conditions=3.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +flower ,

  

[![](img/t0_flower.jpg)](img/f0_flower.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +flower ,**

[![](img/t1_flower.jpg)](img/f1_flower.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +flower ,**

---

# Command: kaleidoscope
**Category:** Warpings
**Source:** https://gmic.eu/reference/kaleidoscope.html#top

# kaleidoscope

## Arguments:

* \_center\_x[%],\_center\_y[%],\_radius,\_angle,\_boundary\_conditions={ 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }

## Description:

Create kaleidoscope effect from selected images.  

## Default values:

center\_x=center\_y=50%, radius=100, angle=30 and boundary\_conditions=3.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> kaleidoscope ,

  
[![](img/t_kaleidoscope.jpg)](img/f_kaleidoscope.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> kaleidoscope ,**

---

# Command: map_sphere
**Category:** Warpings
**Source:** https://gmic.eu/reference/map_sphere.html#top

# map\_sphere

## Arguments:

* \_width>0,\_height>0,\_radius,\_dilation>0,\_fading>=0,\_fading\_power>=0

## Description:

Map selected images on a sphere.  

## Default values:

width=height=512, radius=100, dilation=0.5, fading=0 and fading\_power=0.5.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> map\_sphere ,

  
[![](img/t_map_sphere.jpg)](img/f_map_sphere.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> map\_sphere ,**

---

# Command: nadirzenith2equirectangular
**Category:** Warpings
**Source:** https://gmic.eu/reference/nadirzenith2equirectangular.html#top

# nadirzenith2equirectangular

### No argumentsDescription:Transform selected nadir/zenith rectilinear projections to equirectangular images.

---

# Command: polar2euclidean
**Category:** Warpings
**Source:** https://gmic.eu/reference/polar2euclidean.html#top

# polar2euclidean

## Arguments:

* \_center\_x[%],\_center\_y[%],\_stretch\_factor>0,\_boundary\_conditions={ 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }

## Description:

Apply euclidean to polar transform on selected images.  

## Default values:

center\_x=center\_y=50%, stretch\_factor=1 and boundary\_conditions=3.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +euclidean2polar ,

  

[![](img/t0_polar2euclidean.jpg)](img/f0_polar2euclidean.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +euclidean2polar ,**

[![](img/t1_polar2euclidean.jpg)](img/f1_polar2euclidean.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +euclidean2polar ,**

---

# Command: raindrops
**Category:** Warpings
**Source:** https://gmic.eu/reference/raindrops.html#top

# raindrops

## Arguments:

* \_amplitude,\_density>=0,\_wavelength>=0,\_merging\_steps>=0

## Description:

Apply raindrops deformation on selected images.  

## Default values:

amplitude=80,density=0.1, wavelength=1 and merging\_steps=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +raindrops ,

  

[![](img/t0_raindrops.jpg)](img/f0_raindrops.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +raindrops ,**

[![](img/t1_raindrops.jpg)](img/f1_raindrops.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +raindrops ,**

---

# Command: ripple
**Category:** Warpings
**Source:** https://gmic.eu/reference/ripple.html#top

# ripple

## Arguments:

* \_amplitude,\_bandwidth,\_shape={ 0:Block | 1:Triangle | 2:Sine | 3:Sine+ | 4:Random },\_angle,\_offset

## Description:

Apply ripple deformation on selected images.  

## Default values:

amplitude=10, bandwidth=10, shape=2, angle=0 and offset=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +ripple ,

  

[![](img/t0_ripple.jpg)](img/f0_ripple.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +ripple ,**

[![](img/t1_ripple.jpg)](img/f1_ripple.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +ripple ,**

---

# Command: rotoidoscope
**Category:** Warpings
**Source:** https://gmic.eu/reference/rotoidoscope.html#top

# rotoidoscope

## Arguments:

* \_center\_x[%],\_center\_y[%],\_tiles>0,\_smoothness[%]>=0,\_boundary\_conditions={ 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }

## Description:

Create rotational kaleidoscope effect from selected images.  

## Default values:

center\_x=center\_y=50%, tiles=10, smoothness=1 and boundary\_conditions=3.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +rotoidoscope ,

  

[![](img/t0_rotoidoscope.jpg)](img/f0_rotoidoscope.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +rotoidoscope ,**

[![](img/t1_rotoidoscope.jpg)](img/f1_rotoidoscope.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +rotoidoscope ,**

---

# Command: spherize
**Category:** Warpings
**Source:** https://gmic.eu/reference/spherize.html#top

# spherize

## Arguments:

* \_radius[%]>=0,\_strength,\_smoothness[%]>=0,\_center\_x[%],\_center\_y[%],\_ratio\_x/y>0,\_angle,\_interpolation

## Description:

Apply spherize effect on selected images.  

## Default values:

radius=50%, strength=1, smoothness=0, center\_x=center\_y=50%, ratio\_x/y=1, angle=0 and interpolation=1.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> grid 5%,5%,0,0,0.6,255 spherize ,

  
[![](img/t_spherize.jpg)](img/f_spherize.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> grid 5%,5%,0,0,0.6,255 spherize ,**

---

# Command: symmetrize
**Category:** Warpings
**Source:** https://gmic.eu/reference/symmetrize.html#top

# symmetrize

## Arguments:

* \_x[%],\_y[%],\_angle,\_boundary\_conditions={ 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror },\_is\_antisymmetry={ 0:No | 1:Yes },\_swap\_sides={ 0:No | 1:Yes }

## Description:

Symmetrize selected images regarding specified axis.  

## Default values:

x=y=50%, angle=90, boundary\_conditions=3, is\_antisymmetry=0 and swap\_sides=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +symmetrize 50%,50%,45 +symmetrize[-1] 50%,50%,-45

  

[![](img/t0_symmetrize.jpg)](img/f0_symmetrize.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +symmetrize 50%,50%,45 +symmetrize[-1] 50%,50%,-45**

[![](img/t1_symmetrize.jpg)](img/f1_symmetrize.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +symmetrize 50%,50%,45 +symmetrize[-1] 50%,50%,-45**

[![](img/t2_symmetrize.jpg)](img/f2_symmetrize.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +symmetrize 50%,50%,45 +symmetrize[-1] 50%,50%,-45**

---

# Command: transform_polar
**Category:** Warpings
**Source:** https://gmic.eu/reference/transform_polar.html#top

# transform\_polar

## Arguments:

* "expr\_radius",\_"expr\_angle",\_center\_x[%],\_center\_y[%],\_boundary\_conditions={ 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }

## Description:

Apply user-defined transform on polar representation of selected images.  

## Default values:

expr\_radius=R-r, expr\_rangle=a, center\_x=center\_y=50% and boundary\_conditions=3.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +transform\_polar[0] R\*(r/R)^2,a +transform\_polar[0] r,2\*a

  

[![](img/t0_transform_polar.jpg)](img/f0_transform_polar.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +transform\_polar[0] R\*(r/R)^2,a +transform\_polar[0] r,2\*a**

[![](img/t1_transform_polar.jpg)](img/f1_transform_polar.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +transform\_polar[0] R\*(r/R)^2,a +transform\_polar[0] r,2\*a**

[![](img/t2_transform_polar.jpg)](img/f2_transform_polar.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +transform\_polar[0] R\*(r/R)^2,a +transform\_polar[0] r,2\*a**

---

# Command: twirl
**Category:** Warpings
**Source:** https://gmic.eu/reference/twirl.html#top

# twirl

## Arguments:

* \_amplitude,\_center\_x[%],\_center\_y[%],\_boundary\_conditions={ 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }

## Description:

Apply twirl deformation on selected images.  

## Default values:

amplitude=1, center\_x=center\_y=50% and boundary\_conditions=3.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> twirl 0.6

  
[![](img/t_twirl.jpg)](img/f_twirl.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> twirl 0.6**

---

# Command: warp
**Category:** Warpings
**Source:** https://gmic.eu/reference/warp.html#top

|  |  |
| --- | --- |
| warp | Built-in command |

## Arguments:

* [warping\_field],\_mode,\_interpolation,\_boundary\_conditions,\_nb\_frames>0

## Description:

Warp selected images with specified displacement field.  
  
mode can be { 0:Backward-absolute | 1:Backward-relative | 2:Forward-absolute | 3:Forward-relative }.  
interpolation can be { 0:Nearest-neighbor | 1:Linear | 2:Cubic }.  
boundary\_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.  

## Default values:

mode=0, interpolation=1, boundary\_conditions=0 and nb\_frames=1.

This command has a [tutorial page](https://gmic.eu/oldtutorial/_warp).

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> 100%,100%,1,2,'X=x/w-0.5;Y=y/h-0.5;R=(X\*X+Y\*Y)^0.5;A=atan2(Y,X);130\*R\*(!c?cos(4\*A):sin(8\*A))' warp[-2] [-1],1,1,0 quiver[-1] [-1],10,1,1,1,100

  

[![](img/t0_warp.jpg)](img/f0_warp.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> 100%,100%,1,2,'X=x/w-0.5;Y=y/h-0.5;R=(X\*X+Y\*Y)^0.5;A=atan2(Y,X);130\*R\*(!c?cos(4\*A):sin(8\*A))' warp[-2] [-1],1,1,0 quiver[-1] [-1],10,1,1,1,100**

[![](img/t1_warp.jpg)](img/f1_warp.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> 100%,100%,1,2,'X=x/w-0.5;Y=y/h-0.5;R=(X\*X+Y\*Y)^0.5;A=atan2(Y,X);130\*R\*(!c?cos(4\*A):sin(8\*A))' warp[-2] [-1],1,1,0 quiver[-1] [-1],10,1,1,1,100**

---

# Command: warp_patch
**Category:** Warpings
**Source:** https://gmic.eu/reference/warp_patch.html#top

# warp\_patch

## Arguments:

* [displacement\_map],patch\_width>=1,\_patch\_height>=1,\_patch\_depth>=1,\_std\_factor>0,\_boundary\_conditions,\_fast\_approximation={ 0:No | 1:Yes }

## Description:

Patch-warp selected images, with specified 2D or 3D displacement map (in backward-absolute mode).  
  
Argument std\_factor sets the std of the gaussian weights for the patch overlap,  
equal to std = std\_factor\*patch\_size.  
boundary\_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.  

## Default values:

std\_factor=0.3, boundary\_conditions=3 and fast\_approximation=0.

---

# Command: warp_perspective
**Category:** Warpings
**Source:** https://gmic.eu/reference/warp_perspective.html#top

# warp\_perspective

## Arguments:

* \_x-angle,\_y-angle,\_zoom>0,\_x-center,\_y-center,\_boundary\_conditions={ 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }

## Description:

Warp selected images with perspective deformation.  

## Default values:

x-angle=1.5, y-angle=0, zoom=1, x-center=y-center=50 and boundary\_conditions=2.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> warp\_perspective ,

  
[![](img/t_warp_perspective.jpg)](img/f_warp_perspective.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> warp\_perspective ,**

---

# Command: warp_rbf
**Category:** Warpings
**Source:** https://gmic.eu/reference/warp_rbf.html#top

# warp\_rbf

## Arguments:

* xs0[%],ys0[%],xt0[%],yt0[%],...,xsN[%],ysN[%],xtN[%],ytN[%]

## Description:

Warp selected images using RBF-based interpolation.  
  
Each argument (xsk,ysk)-(xtk,ytk) corresponds to the coordinates of a keypoint  
respectively on the source and target images. The set of all keypoints define the overall image deformation.  

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +warp\_rbf 0,0,0,0,100%,0,100%,0,100%,100%,100%,100%,0,100%,0,100%,50%,50%,70%,50%,25%,25%,25%,75%

  

[![](img/t0_warp_rbf.jpg)](img/f0_warp_rbf.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +warp\_rbf 0,0,0,0,100%,0,100%,0,100%,100%,100%,100%,0,100%,0,100%,50%,50%,70%,50%,25%,25%,25%,75%**

[![](img/t1_warp_rbf.jpg)](img/f1_warp_rbf.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +warp\_rbf 0,0,0,0,100%,0,100%,0,100%,100%,100%,100%,0,100%,0,100%,50%,50%,70%,50%,25%,25%,25%,75%**

---

# Command: warp_seamless
**Category:** Warpings
**Source:** https://gmic.eu/reference/warp_seamless.html#top

# warp\_seamless

## Arguments:

* [displacement\_map],\_sigma[%]>0,\_blend\_dimension={ 0:Auto | 1:1D | 2:2D | 3:3D }

## Description:

Warp selected 2D or 3D images by specified displacement field, using seamless blending.  

## Default values:

sigma=5% and blend\_dimension=0.

## Example of use:

sp colorful,512 100%,100%,1,2,[x,y] l. { s xy,8 sort\_list +,u append\_tiles , } +warp[0] [1] +warp\_seamless[0] [1]

  

[![](img/t0_warp_seamless.jpg)](img/f0_warp_seamless.jpg)

Command: **sp colorful,512 100%,100%,1,2,[x,y] l. { s xy,8 sort\_list +,u append\_tiles , } +warp[0] [1] +warp\_seamless[0] [1]**

[![](img/t1_warp_seamless.jpg)](img/f1_warp_seamless.jpg)

Command: **sp colorful,512 100%,100%,1,2,[x,y] l. { s xy,8 sort\_list +,u append\_tiles , } +warp[0] [1] +warp\_seamless[0] [1]**

[![](img/t2_warp_seamless.jpg)](img/f2_warp_seamless.jpg)

Command: **sp colorful,512 100%,100%,1,2,[x,y] l. { s xy,8 sort\_list +,u append\_tiles , } +warp[0] [1] +warp\_seamless[0] [1]**

[![](img/t3_warp_seamless.jpg)](img/f3_warp_seamless.jpg)

Command: **sp colorful,512 100%,100%,1,2,[x,y] l. { s xy,8 sort\_list +,u append\_tiles , } +warp[0] [1] +warp\_seamless[0] [1]**

---

# Command: water
**Category:** Warpings
**Source:** https://gmic.eu/reference/water.html#top

# water

## Arguments:

* \_amplitude,\_smoothness>=0,\_angle

## Description:

Apply water deformation on selected images.  

## Default values:

amplitude=30, smoothness=1.5 and angle=45.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> water ,

  
[![](img/t_water.jpg)](img/f_water.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> water ,**

---

# Command: wave
**Category:** Warpings
**Source:** https://gmic.eu/reference/wave.html#top

# wave

## Arguments:

* \_amplitude>=0,\_frequency>=0,\_center\_x,\_center\_y

## Description:

Apply wave deformation on selected images.  

## Default values:

amplitude=4, frequency=0.4 and center\_x=center\_y=50.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> wave ,

  
[![](img/t_wave.jpg)](img/f_wave.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> wave ,**

---

# Command: wind
**Category:** Warpings
**Source:** https://gmic.eu/reference/wind.html#top

# wind

## Arguments:

* \_amplitude>=0,\_angle,0<=\_attenuation<=1,\_threshold

## Description:

Apply wind effect on selected images.  

## Default values:

amplitude=20, angle=0, attenuation=0.7 and threshold=20.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +wind ,

  

[![](img/t0_wind.jpg)](img/f0_wind.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +wind ,**

[![](img/t1_wind.jpg)](img/f1_wind.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +wind ,**

---

# Command: zoom
**Category:** Warpings
**Source:** https://gmic.eu/reference/zoom.html#top

# zoom

## Arguments:

* \_factor,\_cx,\_cy,\_cz,\_boundary\_conditions={ 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }

## Description:

Apply zoom factor to selected images.  

## Default values:

factor=1, cx=cy=cz=0.5 and boundary\_conditions=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +zoom[0] 0.6 +zoom[0] 1.5

  

[![](img/t0_zoom.jpg)](img/f0_zoom.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +zoom[0] 0.6 +zoom[0] 1.5**

[![](img/t1_zoom.jpg)](img/f1_zoom.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +zoom[0] 0.6 +zoom[0] 1.5**

[![](img/t2_zoom.jpg)](img/f2_zoom.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +zoom[0] 0.6 +zoom[0] 1.5**

---

# Command: cracks
**Category:** Degradations
**Source:** https://gmic.eu/reference/cracks.html#top

# cracks

## Arguments:

* 0<=\_density<=100,\_is\_relief={ 0:No | 1:Yes },\_opacity,\_color1,...

## Description:

Draw random cracks on selected images with specified color.  

## Default values:

density=25, is\_relief=0, opacity=1 and color1=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +cracks ,

  

[![](img/t0_cracks.jpg)](img/f0_cracks.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +cracks ,**

[![](img/t1_cracks.jpg)](img/f1_cracks.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +cracks ,**

---

# Command: light_patch
**Category:** Degradations
**Source:** https://gmic.eu/reference/light_patch.html#top

# light\_patch

## Arguments:

* \_density>0,\_darkness>=0,\_lightness>=0

## Description:

Add light patches to selected images.  

## Default values:

density=10, darkness=0.9 and lightness=1.7.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +light\_patch 20,0.9,4

  

[![](img/t0_light_patch.jpg)](img/f0_light_patch.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +light\_patch 20,0.9,4**

[![](img/t1_light_patch.jpg)](img/f1_light_patch.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +light\_patch 20,0.9,4**

---

# Command: pixelize
**Category:** Degradations
**Source:** https://gmic.eu/reference/pixelize.html#top

# pixelize

## Arguments:

* \_scale\_x>0,\_scale\_y>0,\_scale\_z>0

## Description:

Pixelize selected images with specified scales.  

## Default values:

scale\_x=20 and scale\_y=scale\_z=scale\_x.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +pixelize ,

  

[![](img/t0_pixelize.jpg)](img/f0_pixelize.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +pixelize ,**

[![](img/t1_pixelize.jpg)](img/f1_pixelize.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +pixelize ,**

---

# Command: scanlines
**Category:** Degradations
**Source:** https://gmic.eu/reference/scanlines.html#top

# scanlines

## Arguments:

* \_amplitude,\_bandwidth,\_shape={ 0:Block | 1:Triangle | 2:Sine | 3:Sine+ | 4:Random },\_angle,\_offset

## Description:

Apply ripple deformation on selected images.  

## Default values:

amplitude=60, bandwidth=2, shape=0, angle=0 and offset=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +scanlines ,

  

[![](img/t0_scanlines.jpg)](img/f0_scanlines.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +scanlines ,**

[![](img/t1_scanlines.jpg)](img/f1_scanlines.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +scanlines ,**

---

# Command: shade_stripes
**Category:** Degradations
**Source:** https://gmic.eu/reference/shade_stripes.html#top

# shade\_stripes

## Arguments:

* \_frequency>=0,\_direction={ 0:Horizontal | 1:Vertical },\_darkness>=0,\_lightness>=0

## Description:

Add shade stripes to selected images.  

## Default values:

frequency=5, direction=1, darkness=0.8 and lightness=2.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +shade\_stripes 30

  

[![](img/t0_shade_stripes.jpg)](img/f0_shade_stripes.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +shade\_stripes 30**

[![](img/t1_shade_stripes.jpg)](img/f1_shade_stripes.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +shade\_stripes 30**

---

# Command: shadow_patch
**Category:** Degradations
**Source:** https://gmic.eu/reference/shadow_patch.html#top

# shadow\_patch

## Arguments:

* \_opacity>=0

## Description:

Add shadow patches to selected images.  

## Default values:

opacity=0.7.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +shadow\_patch 0.4

  

[![](img/t0_shadow_patch.jpg)](img/f0_shadow_patch.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +shadow\_patch 0.4**

[![](img/t1_shadow_patch.jpg)](img/f1_shadow_patch.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +shadow\_patch 0.4**

---

# Command: shuffle
**Category:** Degradations
**Source:** https://gmic.eu/reference/shuffle.html#top

# shuffle

### No argumentsDescription:Shuffle vectors of selected images with Fisher-Yates algorithm, as described in <https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle>. Example of use: uniform\_distribution 8,3 shuffle Command: **uniform\_distribution 8,3 shuffle**

---

# Command: spread
**Category:** Degradations
**Source:** https://gmic.eu/reference/spread.html#top

# spread

## Arguments:

* \_dx[%]>=0,\_dy[%]>=0,\_dz[%]>=0

## Description:

Spread pixel values of selected images randomly along x,y and z.  

## Default values:

dx=3, dy=dx and dz=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +spread 3

  

[![](img/t0_spread.jpg)](img/f0_spread.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +spread 3**

[![](img/t1_spread.jpg)](img/f1_spread.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +spread 3**

---

# Command: stripes_y
**Category:** Degradations
**Source:** https://gmic.eu/reference/stripes_y.html#top

# stripes\_y

## Arguments:

* \_frequency>=0

## Description:

Add vertical stripes to selected images.  

## Default values:

frequency=10.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +stripes\_y ,

  

[![](img/t0_stripes_y.jpg)](img/f0_stripes_y.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +stripes\_y ,**

[![](img/t1_stripes_y.jpg)](img/f1_stripes_y.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +stripes\_y ,**

---

# Command: texturize_canvas
**Category:** Degradations
**Source:** https://gmic.eu/reference/texturize_canvas.html#top

# texturize\_canvas

## Arguments:

* \_amplitude>=0,\_fibrousness>=0,\_emboss\_level>=0

## Description:

Add paint canvas texture to selected images.  

## Default values:

amplitude=20, fibrousness=3 and emboss\_level=0.6.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +texturize\_canvas ,

  

[![](img/t0_texturize_canvas.jpg)](img/f0_texturize_canvas.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +texturize\_canvas ,**

[![](img/t1_texturize_canvas.jpg)](img/f1_texturize_canvas.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +texturize\_canvas ,**

---

# Command: texturize_paper
**Category:** Degradations
**Source:** https://gmic.eu/reference/texturize_paper.html#top

# texturize\_paper

### No argumentsDescription:Add paper texture to selected images. Example of use: <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +texturize\_paper Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +texturize\_paper** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +texturize\_paper**

---

# Command: vignette
**Category:** Degradations
**Source:** https://gmic.eu/reference/vignette.html#top

# vignette

## Arguments:

* \_strength>=0,0<=\_radius\_min<=100,0<=\_radius\_max<=100

## Description:

Add vignette effect to selected images.  

## Default values:

strength=100, radius\_min=70 and radius\_max=90.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> vignette ,

  
[![](img/t_vignette.jpg)](img/f_vignette.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> vignette ,**

---

# Command: watermark_visible
**Category:** Degradations
**Source:** https://gmic.eu/reference/watermark_visible.html#top

# watermark\_visible

## Arguments:

* \_text,0<\_opacity<1,\_{ size>0 | font },\_angle,\_mode={ 0:Remove | 1:Add },\_smoothness>=0

## Description:

Add or remove a visible watermark on selected images (value range must be [0,255]).  

## Default values:

text=(c) G'MIC, opacity=0.3, size=53, angle=25, mode=1 and smoothness=0.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> watermark\_visible ,0.7

  
[![](img/t_watermark_visible.jpg)](img/f_watermark_visible.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> watermark\_visible ,0.7**

---

# Command: blend
**Category:** Blending and Fading
**Source:** https://gmic.eu/reference/blend.html#top

# blend

## Arguments:

* [layer],blending\_mode,\_opacity[%],\_selection\_is={ 0:Base-layers | 1:Top-layers }    or
* blending\_mode,\_opacity[%]

## Description:

Blend selected G,GA,RGB or RGBA images by specified layer or blend all selected images together,  
  
using specified blending mode.  
blending\_mode can be { add | alpha | and | average | blue | burn | darken | difference |  
divide | dodge | edges | exclusion | freeze | grainextract | grainmerge | green | hardlight |  
hardmix | hue | interpolation | lchlightness | lighten | lightness | linearburn | linearlight | luminance |  
multiply | negation | or | overlay | pinlight | red | reflect | saturation |  
screen | seamless | seamless\_mixed | shapeareamax | shapeareamax0 | shapeareamin | shapeareamin0 |  
shapeaverage | shapeaverage0 | shapemedian | shapemedian0 | shapemin | shapemin0 | shapemax | shapemax0 |  
shapeprevalent | softburn | softdodge | softlight | stamp | subtract | value | vividlight | xor }.  
opacity must be in range [0,1] (or [0%,100%]).  

## Default values:

blending\_mode=alpha, opacity=1 and selection\_is=0.

## Examples of use:

### • Example #1

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +drop\_shadow , rescale2d[-1] ,200 rotate[-1] 20 +blend alpha display\_rgba[-2]

  

[![](img/t0_blend.jpg)](img/f0_blend.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +drop\_shadow , rescale2d[-1] ,200 rotate[-1] 20 +blend alpha display\_rgba[-2]**

[![](img/t1_blend.jpg)](img/f1_blend.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +drop\_shadow , rescale2d[-1] ,200 rotate[-1] 20 +blend alpha display\_rgba[-2]**

[![](img/t2_blend.jpg)](img/f2_blend.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> +drop\_shadow , rescale2d[-1] ,200 rotate[-1] 20 +blend alpha display\_rgba[-2]**

### • Example #2

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} blend overlay

  
[![](img/t_blend_2.jpg)](img/f_blend_2.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} blend overlay**

### • Example #3

command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex add,alpha,and,average,blue,burn,darken

  

[![](img/t0_blend_3.jpg)](img/f0_blend_3.jpg)

Command: **command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex add,alpha,and,average,blue,burn,darken**

[![](img/t1_blend_3.jpg)](img/f1_blend_3.jpg)

Command: **command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex add,alpha,and,average,blue,burn,darken**

[![](img/t2_blend_3.jpg)](img/f2_blend_3.jpg)

Command: **command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex add,alpha,and,average,blue,burn,darken**

[![](img/t3_blend_3.jpg)](img/f3_blend_3.jpg)

Command: **command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex add,alpha,and,average,blue,burn,darken**

[![](img/t4_blend_3.jpg)](img/f4_blend_3.jpg)

Command: **command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex add,alpha,and,average,blue,burn,darken**

[![](img/t5_blend_3.jpg)](img/f5_blend_3.jpg)

Command: **command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex add,alpha,and,average,blue,burn,darken**

[![](img/t6_blend_3.jpg)](img/f6_blend_3.jpg)

Command: **command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex add,alpha,and,average,blue,burn,darken**

[![](img/t7_blend_3.jpg)](img/f7_blend_3.jpg)

Command: **command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex add,alpha,and,average,blue,burn,darken**

[![](img/t8_blend_3.jpg)](img/f8_blend_3.jpg)

Command: **command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex add,alpha,and,average,blue,burn,darken**

### • Example #4

command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex difference,divide,dodge,exclusion,freeze,grainextract,grainmerge

  

[![](img/t0_blend_4.jpg)](img/f0_blend_4.jpg)

Command: **command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex difference,divide,dodge,exclusion,freeze,grainextract,grainmerge**

[![](img/t1_blend_4.jpg)](img/f1_blend_4.jpg)

Command: **command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex difference,divide,dodge,exclusion,freeze,grainextract,grainmerge**

[![](img/t2_blend_4.jpg)](img/f2_blend_4.jpg)

Command: **command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex difference,divide,dodge,exclusion,freeze,grainextract,grainmerge**

[![](img/t3_blend_4.jpg)](img/f3_blend_4.jpg)

Command: **command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex difference,divide,dodge,exclusion,freeze,grainextract,grainmerge**

[![](img/t4_blend_4.jpg)](img/f4_blend_4.jpg)

Command: **command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex difference,divide,dodge,exclusion,freeze,grainextract,grainmerge**

[![](img/t5_blend_4.jpg)](img/f5_blend_4.jpg)

Command: **command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex difference,divide,dodge,exclusion,freeze,grainextract,grainmerge**

[![](img/t6_blend_4.jpg)](img/f6_blend_4.jpg)

Command: **command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex difference,divide,dodge,exclusion,freeze,grainextract,grainmerge**

[![](img/t7_blend_4.jpg)](img/f7_blend_4.jpg)

Command: **command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex difference,divide,dodge,exclusion,freeze,grainextract,grainmerge**

[![](img/t8_blend_4.jpg)](img/f8_blend_4.jpg)

Command: **command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex difference,divide,dodge,exclusion,freeze,grainextract,grainmerge**

### • Example #5

command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex green,hardlight,hardmix,hue,interpolation,lighten,lightness

  

[![](img/t0_blend_5.jpg)](img/f0_blend_5.jpg)

Command: **command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex green,hardlight,hardmix,hue,interpolation,lighten,lightness**

[![](img/t1_blend_5.jpg)](img/f1_blend_5.jpg)

Command: **command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex green,hardlight,hardmix,hue,interpolation,lighten,lightness**

[![](img/t2_blend_5.jpg)](img/f2_blend_5.jpg)

Command: **command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex green,hardlight,hardmix,hue,interpolation,lighten,lightness**

[![](img/t3_blend_5.jpg)](img/f3_blend_5.jpg)

Command: **command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex green,hardlight,hardmix,hue,interpolation,lighten,lightness**

[![](img/t4_blend_5.jpg)](img/f4_blend_5.jpg)

Command: **command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex green,hardlight,hardmix,hue,interpolation,lighten,lightness**

[![](img/t5_blend_5.jpg)](img/f5_blend_5.jpg)

Command: **command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex green,hardlight,hardmix,hue,interpolation,lighten,lightness**

[![](img/t6_blend_5.jpg)](img/f6_blend_5.jpg)

Command: **command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex green,hardlight,hardmix,hue,interpolation,lighten,lightness**

[![](img/t7_blend_5.jpg)](img/f7_blend_5.jpg)

Command: **command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex green,hardlight,hardmix,hue,interpolation,lighten,lightness**

[![](img/t8_blend_5.jpg)](img/f8_blend_5.jpg)

Command: **command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex green,hardlight,hardmix,hue,interpolation,lighten,lightness**

### • Example #6

command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex linearburn,linearlight,luminance,multiply,negation,or,overlay

  

[![](img/t0_blend_6.jpg)](img/f0_blend_6.jpg)

Command: **command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex linearburn,linearlight,luminance,multiply,negation,or,overlay**

[![](img/t1_blend_6.jpg)](img/f1_blend_6.jpg)

Command: **command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex linearburn,linearlight,luminance,multiply,negation,or,overlay**

[![](img/t2_blend_6.jpg)](img/f2_blend_6.jpg)

Command: **command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex linearburn,linearlight,luminance,multiply,negation,or,overlay**

[![](img/t3_blend_6.jpg)](img/f3_blend_6.jpg)

Command: **command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex linearburn,linearlight,luminance,multiply,negation,or,overlay**

[![](img/t4_blend_6.jpg)](img/f4_blend_6.jpg)

Command: **command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex linearburn,linearlight,luminance,multiply,negation,or,overlay**

[![](img/t5_blend_6.jpg)](img/f5_blend_6.jpg)

Command: **command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex linearburn,linearlight,luminance,multiply,negation,or,overlay**

[![](img/t6_blend_6.jpg)](img/f6_blend_6.jpg)

Command: **command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex linearburn,linearlight,luminance,multiply,negation,or,overlay**

[![](img/t7_blend_6.jpg)](img/f7_blend_6.jpg)

Command: **command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex linearburn,linearlight,luminance,multiply,negation,or,overlay**

[![](img/t8_blend_6.jpg)](img/f8_blend_6.jpg)

Command: **command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex linearburn,linearlight,luminance,multiply,negation,or,overlay**

### • Example #7

command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex pinlight,red,reflect,saturation,screen,shapeaverage,softburn

  

[![](img/t0_blend_7.jpg)](img/f0_blend_7.jpg)

Command: **command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex pinlight,red,reflect,saturation,screen,shapeaverage,softburn**

[![](img/t1_blend_7.jpg)](img/f1_blend_7.jpg)

Command: **command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex pinlight,red,reflect,saturation,screen,shapeaverage,softburn**

[![](img/t2_blend_7.jpg)](img/f2_blend_7.jpg)

Command: **command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex pinlight,red,reflect,saturation,screen,shapeaverage,softburn**

[![](img/t3_blend_7.jpg)](img/f3_blend_7.jpg)

Command: **command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex pinlight,red,reflect,saturation,screen,shapeaverage,softburn**

[![](img/t4_blend_7.jpg)](img/f4_blend_7.jpg)

Command: **command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex pinlight,red,reflect,saturation,screen,shapeaverage,softburn**

[![](img/t5_blend_7.jpg)](img/f5_blend_7.jpg)

Command: **command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex pinlight,red,reflect,saturation,screen,shapeaverage,softburn**

[![](img/t6_blend_7.jpg)](img/f6_blend_7.jpg)

Command: **command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex pinlight,red,reflect,saturation,screen,shapeaverage,softburn**

[![](img/t7_blend_7.jpg)](img/f7_blend_7.jpg)

Command: **command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex pinlight,red,reflect,saturation,screen,shapeaverage,softburn**

[![](img/t8_blend_7.jpg)](img/f8_blend_7.jpg)

Command: **command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex pinlight,red,reflect,saturation,screen,shapeaverage,softburn**

### • Example #8

command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex softdodge,softlight,stamp,subtract,value,vividlight,xor

  

[![](img/t0_blend_8.jpg)](img/f0_blend_8.jpg)

Command: **command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex softdodge,softlight,stamp,subtract,value,vividlight,xor**

[![](img/t1_blend_8.jpg)](img/f1_blend_8.jpg)

Command: **command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex softdodge,softlight,stamp,subtract,value,vividlight,xor**

[![](img/t2_blend_8.jpg)](img/f2_blend_8.jpg)

Command: **command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex softdodge,softlight,stamp,subtract,value,vividlight,xor**

[![](img/t3_blend_8.jpg)](img/f3_blend_8.jpg)

Command: **command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex softdodge,softlight,stamp,subtract,value,vividlight,xor**

[![](img/t4_blend_8.jpg)](img/f4_blend_8.jpg)

Command: **command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex softdodge,softlight,stamp,subtract,value,vividlight,xor**

[![](img/t5_blend_8.jpg)](img/f5_blend_8.jpg)

Command: **command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex softdodge,softlight,stamp,subtract,value,vividlight,xor**

[![](img/t6_blend_8.jpg)](img/f6_blend_8.jpg)

Command: **command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex softdodge,softlight,stamp,subtract,value,vividlight,xor**

[![](img/t7_blend_8.jpg)](img/f7_blend_8.jpg)

Command: **command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex softdodge,softlight,stamp,subtract,value,vividlight,xor**

[![](img/t8_blend_8.jpg)](img/f8_blend_8.jpg)

Command: **command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text\_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} ex softdodge,softlight,stamp,subtract,value,vividlight,xor**

---

# Command: nblend
**Category:** Blending and Fading
**Source:** https://gmic.eu/reference/nblend.html#top

# nblend

## Arguments:

* [layer],blending\_mode,\_opacity[%],\_selection\_is={ 0:Base-layers | 1:Top-layers }    or
* blending\_mode,\_opacity[%]

## Description:

---

# Command: blend_edges
**Category:** Blending and Fading
**Source:** https://gmic.eu/reference/blend_edges.html#top

# blend\_edges

## Arguments:

* smoothness[%]>=0

## Description:

Blend selected images togethers using edges mode.  

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} +blend\_edges 0.8

  

[![](img/t0_blend_edges.jpg)](img/f0_blend_edges.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} +blend\_edges 0.8**

[![](img/t1_blend_edges.jpg)](img/f1_blend_edges.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} +blend\_edges 0.8**

[![](img/t2_blend_edges.jpg)](img/f2_blend_edges.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} +blend\_edges 0.8**

---

# Command: blend_fade
**Category:** Blending and Fading
**Source:** https://gmic.eu/reference/blend_fade.html#top

# blend\_fade

## Arguments:

* [fading\_shape]

## Description:

Blend selected images together using specified fading shape.  

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} 100%,100%,1,1,'cos(y/10)' normalize[-1] 0,1 +blend\_fade[0,1] [2]

  

[![](img/t0_blend_fade.jpg)](img/f0_blend_fade.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} 100%,100%,1,1,'cos(y/10)' normalize[-1] 0,1 +blend\_fade[0,1] [2]**

[![](img/t1_blend_fade.jpg)](img/f1_blend_fade.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} 100%,100%,1,1,'cos(y/10)' normalize[-1] 0,1 +blend\_fade[0,1] [2]**

[![](img/t2_blend_fade.jpg)](img/f2_blend_fade.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} 100%,100%,1,1,'cos(y/10)' normalize[-1] 0,1 +blend\_fade[0,1] [2]**

[![](img/t3_blend_fade.jpg)](img/f3_blend_fade.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} 100%,100%,1,1,'cos(y/10)' normalize[-1] 0,1 +blend\_fade[0,1] [2]**

---

# Command: blend_median
**Category:** Blending and Fading
**Source:** https://gmic.eu/reference/blend_median.html#top

# blend\_median

### No argumentsDescription:Blend selected images together using median mode. Example of use: <a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} +mirror[0] y +blend\_median Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} +mirror[0] y +blend\_median** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} +mirror[0] y +blend\_median** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} +mirror[0] y +blend\_median** Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} +mirror[0] y +blend\_median**

---

# Command: blend_seamless
**Category:** Blending and Fading
**Source:** https://gmic.eu/reference/blend_seamless.html#top

# blend\_seamless

## Arguments:

* \_is\_mixed\_mode={ 0:No | 1:Yes },\_inner\_fading[%]>=0,\_outer\_fading[%]>=0

## Description:

Blend selected images using a seamless blending mode (Poisson-based).  

## Default values:

is\_mixed=0, inner\_fading=0 and outer\_fading=100%.

---

# Command: fade_diamond
**Category:** Blending and Fading
**Source:** https://gmic.eu/reference/fade_diamond.html#top

# fade\_diamond

## Arguments:

* 0<=\_start<=100,0<=\_end<=100

## Description:

Create diamond fading from selected images.  

## Default values:

start=80 and end=90.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} +fade\_diamond 80,85

  

[![](img/t0_fade_diamond.jpg)](img/f0_fade_diamond.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} +fade\_diamond 80,85**

[![](img/t1_fade_diamond.jpg)](img/f1_fade_diamond.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} +fade\_diamond 80,85**

[![](img/t2_fade_diamond.jpg)](img/f2_fade_diamond.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} +fade\_diamond 80,85**

---

# Command: fade_linear
**Category:** Blending and Fading
**Source:** https://gmic.eu/reference/fade_linear.html#top

# fade\_linear

## Arguments:

* \_angle,0<=\_start<=100,0<=\_end<=100

## Description:

Create linear fading from selected images.  

## Default values:

angle=45, start=30 and end=70.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} +fade\_linear 45,48,52

  

[![](img/t0_fade_linear.jpg)](img/f0_fade_linear.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} +fade\_linear 45,48,52**

[![](img/t1_fade_linear.jpg)](img/f1_fade_linear.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} +fade\_linear 45,48,52**

[![](img/t2_fade_linear.jpg)](img/f2_fade_linear.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} +fade\_linear 45,48,52**

---

# Command: fade_radial
**Category:** Blending and Fading
**Source:** https://gmic.eu/reference/fade_radial.html#top

# fade\_radial

## Arguments:

* 0<=\_start<=100,0<=\_end<=100

## Description:

Create radial fading from selected images.  

## Default values:

start=30 and end=70.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} +fade\_radial 30,70

  

[![](img/t0_fade_radial.jpg)](img/f0_fade_radial.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} +fade\_radial 30,70**

[![](img/t1_fade_radial.jpg)](img/f1_fade_radial.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} +fade\_radial 30,70**

[![](img/t2_fade_radial.jpg)](img/f2_fade_radial.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} +fade\_radial 30,70**

---

# Command: fade_x
**Category:** Blending and Fading
**Source:** https://gmic.eu/reference/fade_x.html#top

# fade\_x

## Arguments:

* 0<=\_start<=100,0<=\_end<=100

## Description:

Create horizontal fading from selected images.  

## Default values:

start=30 and end=70.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} +fade\_x 30,70

  

[![](img/t0_fade_x.jpg)](img/f0_fade_x.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} +fade\_x 30,70**

[![](img/t1_fade_x.jpg)](img/f1_fade_x.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} +fade\_x 30,70**

[![](img/t2_fade_x.jpg)](img/f2_fade_x.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} +fade\_x 30,70**

---

# Command: fade_y
**Category:** Blending and Fading
**Source:** https://gmic.eu/reference/fade_y.html#top

# fade\_y

## Arguments:

* 0<=\_start<=100,0<=\_end<=100

## Description:

Create vertical fading from selected images.  

## Default values:

start=30 and end=70.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} +fade\_y 30,70

  

[![](img/t0_fade_y.jpg)](img/f0_fade_y.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} +fade\_y 30,70**

[![](img/t1_fade_y.jpg)](img/f1_fade_y.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} +fade\_y 30,70**

[![](img/t2_fade_y.jpg)](img/f2_fade_y.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} +fade\_y 30,70**

---

# Command: fade_z
**Category:** Blending and Fading
**Source:** https://gmic.eu/reference/fade_z.html#top

# fade\_z

## Arguments:

* 0<=\_start<=100,0<=\_end<=100

## Description:

Create transversal fading from selected images.  

## Default values:

start=30 and end=70.

---

# Command: sub_alpha
**Category:** Blending and Fading
**Source:** https://gmic.eu/reference/sub_alpha.html#top

# sub\_alpha

## Arguments:

* [base\_image],0<=\_minimize\_alpha<=1

## Description:

Compute the alpha-channel difference (opposite of alpha blending) between the selected images  
  
and the specified base image.  
The alpha difference A-B is defined as the image having minimal opacity, such that alpha\_blend(B,A-B) = A.  
The min\_alpha argument is used to relax the alpha minimality constraint. When set to 1, alpha is constrained to be minimal. When set to 0, alpha is maximal (i.e. 255).  

## Default values:

minimize\_alpha=1.

## Example of use:

<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} +sub\_alpha[0] [1] display\_rgba

  

[![](img/t0_sub_alpha.jpg)](img/f0_sub_alpha.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} +sub\_alpha[0] [1] display\_rgba**

[![](img/t1_sub_alpha.jpg)](img/f1_sub_alpha.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} +sub\_alpha[0] [1] display\_rgba**

[![](img/t2_sub_alpha.jpg)](img/f2_sub_alpha.jpg)

Command: **<a href="image.jpg" class="highslide" onclick="return hs.expand(this)">image.jpg</a> testimage2d {w},{h} +sub\_alpha[0] [1] display\_rgba**