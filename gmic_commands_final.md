# G'MIC Command Reference


---

# Command: apply_curve

## Arguments:

* 0<=smoothness<=1,x0,y0,x1,y1,x2,y2,...,xN,yN

## Description:

Apply curve transformation to image values.

## Default values:

smoothness=1, x0=0, y0=100.

```
gmic image.jpg +apply_curve 1,0,0,128,255,255,0
```

---

# Command: apply_gamma

## Arguments:

* gamma>=0

## Description:

Apply gamma correction to selected images.

```
gmic image.jpg +apply_gamma 2
```

---

# Command: apply_mask

## Arguments:

* "command",[opacity_mask],_max_opacity_mask

## Description:

Apply specified command on selected images but only inside the specified mask.

## Default values:

max_opacity_mask=1.

```
gmic image.jpg 100%,100% noise. 10 blur. 2%,0 ge. 50% blur. 0.5% normalize. 0,1 +apply_mask.. "sepia whirls",[-1]
```

---

# Command: balance_gamma

## Arguments:

* _ref_color1,...

## Description:

Compute gamma-corrected color balance of selected image, with respect to specified reference color.

## Default values:

ref_color1=128.

```
gmic image.jpg +balance_gamma 128,64,64
```

---

# Command: cast

## Arguments:

* datatype_source,datatype_target

## Description:

Cast datatype of image buffer from specified source type to specified target type.

datatype_source and datatype_target can be { uint8 | int8 | uint16 | int16 | uint32 | int32 | uint64 | int64 | float32 | float64 }.

---

# Command: complex2polar

### No argumentsDescription:Compute complex to polar transforms of selected images. ``` gmic image.jpg +fft complex2polar[-2,-1] log[-2] shift[-2] 50%,50%,0,0,2 remove[-1] ```

---

# Command: compress_clut

### No argumentsDescription:Compress selected color LUTs as sequences of colored keypoints.

---

# Command: compress_huffman

## Arguments:

* [huffman_tree],_max_leaf_value

## Description:

Compress selected images with Huffman coding.

## See also:

[decompress_huffman](decompress_huffman.html), [huffman_tree](huffman_tree.html).

---

# Command: compress_rle

## Arguments:

* _is_binary_data={ 0:No | 1:Yes },_maximum_sequence_length>=0

## Description:

Compress selected images as 2xN data matrices, using RLE algorithm.

Set maximum_sequence_length=0 to disable maximum length constraint.

## Default values:

is_binary_data=0 and maximum_sequence_length=0.

```
gmic image.jpg rescale2d ,100 quantize 4 round +compress_rle , +decompress_rle[-1]
```

---

# Command: cumulate

|  |  |
| --- | --- |
|  | Built-in command |

## Arguments:

* { x | y | z | c }...{ x | y | z | c }    or
* (no arg)

## Description:

Compute the cumulative function of specified image data, optionally along the specified axes.

```
gmic image.jpg +histogram 256 +cumulate[-1] display_graph[-2,-1] 400,300,3
```

---

# Command: decompress_clut

## Arguments:

* _width>0,_height>0,_depth>0

## Description:

Decompress selected colored keypoints into 3D CLUTs, using a mixed RBF/PDE approach.

## Default values:

width=height=depth=33 and reconstruction_colorspace=0.

---

# Command: decompress_from_keypoints

## Arguments:

* _width>0,_height>0,_depth>0    or
* (no arg)

## Description:

Decompress selected sets of keypoints as images (opt. of specified size).

A set of keypoints is defined as a vector-valued image, such that:

The first pixel is a vector which encodes the [ Width,Height,Depth ] of the decompressed image.

The second pixel is a vector which encodes [ Min,Max,Use_RBF ], where Min and Max defines the value range of the decompressed image, and Use_RBF tells is the decompression scheme must use RBFs (Use_RBF=1) or Multiscale Diffusion PDE's (Use_RBF=0).

The remaining pixels define the keypoint coordinates and values, as:

[ x_k,y_k,z_k, v1_k,...,vN_k ] for a 3D target image of N-valued vectors.

[ x_k,y_k, v1_k,...,vN_k ] for a 2D target image of N-valued vectors.

[ x_k, v1_k,...,vN_k ] for a 1D target image of N-valued vectors.

where the coordinates x_k, y_k and z_k are defined respectively in ranges [0,Width-1], [0,Height-1] and [0,Depth-1].
If the width, height and depth arguments are provided, they define the size of the decompressed image, : overriding then the original image size [ Width,Height,Depth ] defined in the keypoints header.

---

# Command: decompress_huffman

## Arguments:

* [huffman_tree]

## Description:

Decompress selected images with Huffman decoding.

## See also:

[compress_huffman](compress_huffman.html), [huffman_tree](huffman_tree.html).

```
gmic image.jpg huffman_tree compress_huffman.. . +decompress_huffman.. .
```

---

# Command: decompress_rle

### No argumentsDescription:Decompress selected data vectors, using RLE algorithm.

---

# Command: discard

|  |  |
| --- | --- |
|  | Built-in command |

## Arguments:

* _value1,_value2,...    or
* { x | y | z | c}...{ x | y | z | c},_value1,_value2,...    or
* (no arg)

## Description:

Discard specified values in selected images or discard neighboring duplicate values,

optionally only for the values along the first of a specified axis.
If no arguments are specified, neighboring duplicate values are discarded.
If all pixels of a selected image are discarded, an empty image is returned.

## Examples of use:

### • Example #1

```
gmic (1;2;3;4;3;2;1) +discard 2
```

### • Example #2

```
gmic (1,2,2,3,3,3,4,4,4,4) +discard x
```

---

# Command: eigen2tensor

### No argumentsDescription:Recompose selected pairs of eigenvalues/eigenvectors as 2x2 or 3x3 tensor fields. This command has a [tutorial page](https://gmic.eu/tutorial/eigen2tensor).

---

# Command: endian

|  |  |
| --- | --- |
|  | Built-in command |

## Arguments:

* _datatype

## Description:

Reverse data endianness of selected images, eventually considering the pixel being of the specified datatype.

datatype can be { bool | uint8 | int8 | uint16 | int16 | uint32 | int32 | uint64 | int64 | float32 | float64 }.
This command does nothing for bool, uint8 and int8 datatypes.

---

# Command: equalize

|  |  |
| --- | --- |
|  | Built-in command |

## Arguments:

* _nb_levels[%]>0,_value_min[%],_value_max[%]    or
* (no arg)

## Description:

Equalize histograms of selected images.

If value range is specified, the equalization is done only for pixels in the specified
value range.

## Default values:

nb_levels=256, value_min=0% and value_max=100%.

## Examples of use:

### • Example #1

```
gmic image.jpg +equalize
```

### • Example #2

```
gmic image.jpg +equalize 4,0,128
```

---

# Command: fill

|  |  |
| --- | --- |
|  | Built-in command |

## Arguments:

* value1,_value2,...    or
* [image]    or
* 'formula'

## Description:

Fill selected images with values read from the specified value list, existing image

or mathematical expression. Single quotes may be omitted in formula.

(*equivalent to shortcut command* f).

This command has a [tutorial page](https://gmic.eu/tutorial/fill).

## Examples of use:

### • Example #1

```
gmic 4,4 fill 1,2,3,4,5,6,7
```

### • Example #2

```
gmic 4,4 (1,2,3,4,5,6,7) fill[-2] [-1]
```

### • Example #3

```
gmic 400,400,1,3 fill "X=x-w/2; Y=y-h/2; R=sqrt(X^2+Y^2); a=atan2(Y,X); R<=180?255*abs(cos(c+200*(x/w-0.5)*(y/h-0.5))):850*(a%(0.1*(c+1)))"
```

---

# Command: icp

## Arguments:

* [reference],_affine_mode,_precision>0,_iter_max>=0

## Description:

Apply affine transformation on vector-valued points of selected images, to match specified set of reference vectors, using the ICP algorithm (Iterative Closest Point).

A description of ICP is available at <https://en.wikipedia.org/wiki/Iterative_closest_point>.
Argument affine_mode tells about the type of affine transform applied. It can be: { 0:Free | 1:Rotation+Scaling | 2:Rotation-Only }.

## Default values:

affine_mode=0, precision=1e-3 and iter_max=1000.

---

# Command: map

|  |  |
| --- | --- |
|  | Built-in command |

## Arguments:

* [palette],_boundary_conditions    or
* palette_name,_boundary_conditions

## Description:

Map specified vector-valued palette to selected indexed images.

Each output image has M\*N channels, where M and N are the numbers of channels of, respectively, the corresponding input image and the palette image.
palette_name can be { default | hsv | lines | hot | cool | jet | flag | cube | rainbow | algae | amp | balance | curl | deep | delta | dense | diff | gray | haline | ice | matter | oxy | phase | rain | solar | speed | tarn | tempo | thermal | topo | turbid | aurora | hocuspocus | srb2 | uzebox }
boundary_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.

## Default values:

boundary_conditions=0.

This command has a [tutorial page](https://gmic.eu/tutorial/map).

## Examples of use:

### • Example #1

```
gmic image.jpg +luminance map[-1] 3
```

### • Example #2

```
gmic image.jpg +rgb2ycbcr split[-1] c (0,255,0) resize[-1] 256,1,1,1,3 map[-4] [-1] remove[-1] append[-3--1] c ycbcr2rgb[-1]
```

---

# Command: mix_channels

## Arguments:

* (a00,...,aMN)    or
* [matrix]

## Description:

Apply specified matrix to channels of selected images.

```
gmic image.jpg +mix_channels (0,1,0;1,0,0;0,0,1)
```

---

# Command: negate

## Arguments:

* base_value    or
* (no arg)

## Description:

Negate image values.

## Default values:

base_value=(undefined).

```
gmic image.jpg +negate
```

---

# Command: noise

|  |  |
| --- | --- |
|  | Built-in command |

## Arguments:

* amplitude[%]>=0,_noise_type

## Description:

Add random noise to selected images.

noise_type can be { 0:Gaussian | 1:Uniform | 2:Salt&pepper | 3:Poisson | 4:Rice }.

## Default values:

noise_type=0.

## Examples of use:

### • Example #1

```
gmic image.jpg +noise[0] 50,0 +noise[0] 50,1 +noise[0] 10,2 cut 0,255
```

### • Example #2

```
gmic 300,300,1,3 [0] noise[0] 20,0 noise[1] 20,1 +histogram 100 display_graph[-2,-1] 400,300,3
```

---

# Command: noise_hurl

## Arguments:

* _amplitude>=0

## Description:

Add hurl noise to selected images.

## Default values:

amplitude=10.

```
gmic image.jpg +noise_hurl ,
```

---

# Command: noise_perlin

## Arguments:

* _scale_x[%]>0,_scale_y[%]>0,_scale_z[%]>0,_seed_x,_seed_y,_seed_z

## Description:

Render 2D or 3D Perlin noise on selected images, from specified coordinates.

The Perlin noise is a specific type of smooth noise,
described here : <https://en.wikipedia.org/wiki/Perlin_noise>.

## Default values:

scale_x=scale_y=scale_z=16 and seed_x=seed_y=seed_z=0.

```
gmic 500,500,1,3 noise_perlin ,
```

---

# Command: noise_poissondisk

## Arguments:

* _radius[%]>0,_max_sample_attempts>0,_p_norm>0

## Description:

Add poisson disk sampling noise to selected images.

Implements the algorithm from the article "Fast Poisson Disk Sampling in Arbitrary Dimensions",
by Robert Bridson (SIGGRAPH'2007).

## Default values:

radius=8, max_sample_attempts=30 and p_norm=2.

```
gmic 300,300 noise_poissondisk 8
```

---

# Command: normp

## Arguments:

* p>=0

## Description:

Compute the pointwise Lp-norm norm of vector-valued pixels in selected images.

## Default values:

p=2.

```
gmic image.jpg +normp[0] 0 +normp[0] 1 +normp[0] 2 +normp[0] inf
```

---

# Command: norm1

### No argumentsDescription:Compute the pointwise L1-norm of vector-valued pixels in selected images. This command has a [tutorial page](https://gmic.eu/oldtutorial/_norm1). ``` gmic image.jpg +norm1 ```

---

# Command: norm2

### No argumentsDescription:Compute the pointwise L2-norm (euclidean norm) of vector-valued pixels in selected images. This command has a [tutorial page](https://gmic.eu/oldtutorial/_norm2). ``` gmic image.jpg +norm ```

---

# Command: normalize

|  |  |
| --- | --- |
|  | Built-in command |

## Arguments:

* { value0[%] | [image0] },{ value1[%] | [image1] },_constant_case_ratio    or
* [image]

## Description:

Linearly normalize values of selected images in specified range.

(*equivalent to shortcut command* n).

This command has a [tutorial page](https://gmic.eu/tutorial/normalize).

```
gmic image.jpg split x,2 normalize[-1] 64,196 append x
```

---

# Command: normalize_l2

### No argumentsDescription:Normalize selected images such that they have a unit L2 norm.

---

# Command: normalize_sum

### No argumentsDescription:Normalize selected images such that they have a unit sum. ``` gmic image.jpg +histogram 256 normalize_sum[-1] display_graph[-1] 400,300 ```

---

# Command: orientation

### No argumentsDescription:Compute the pointwise orientation of vector-valued pixels in selected images. This command has a [tutorial page](https://gmic.eu/tutorial/orientation). ``` gmic image.jpg +orientation +norm[-2] negate[-1] mul[-2] [-1] reverse[-2,-1] ```

---

# Command: otsu

## Arguments:

* _nb_levels>0

## Description:

Hard-threshold selected images using Otsu's method.

The computed thresholds are returned as a list of values in the status.

## Default values:

nb_levels=256.

```
gmic image.jpg luminance +otsu ,
```

---

# Command: polar2complex

### No argumentsDescription:Compute polar to complex transforms of selected images.

---

# Command: quantize

## Arguments:

* nb_levels>=1,_keep_values={ 0:No | 1:Yes },_quantization_type={ -1:Median-cut | 0:K-means | 1:Uniform }

## Description:

Quantize selected images.

## Default values:

keep_values=1 and quantization_type=0.

## Examples of use:

### • Example #1

```
gmic image.jpg luminance +quantize 3
```

### • Example #2

```
gmic 200,200,1,1,'cos(x/10)*sin(y/10)' +quantize[0] 6 +quantize[0] 4 +quantize[0] 3 +quantize[0] 2
```

---

# Command: quantize_area

## Arguments:

* _min_area>0

## Description:

Quantize selected images such that each flat region has an area greater or equal to min_area.

## Default values:

min_area=10.

```
gmic image.jpg quantize 3 +blur 1 round[-1] +quantize_area[-1] 2
```

---

# Command: rand

|  |  |
| --- | --- |
|  | Built-in command |

## Arguments:

* { value0[%] | [image0] },_{ value1[%] | [image1] },_[pdf],_precision[%]    or
* [image]

## Description:

Fill selected images with random values in the specified range.

If no [pdf] (probability density function) is specified, random values follow a uniform distribution.
Argument precision tells about the number of distinct values that can be generated when a [pdf] is specified.

## Examples of use:

### • Example #1

```
gmic 400,400,1,3 rand -10,10 +blur 10 sign[-1]
```

### • Example #2

```
gmic (8,2,1) 50,50 rand[-1] 0,255,[-2]
```

### • Example #3

```
gmic 256 gaussian[-1] 30 line[-1] 47%,0,53%,0,1,0 500,500 rand[-1] 0,255,[-2] +histogram[-1] 256 display_graph[0,2] 640,480,3,0
```

---

# Command: rand_sum

## Arguments:

* sum>0,_random_function

## Description:

Fill selected images with strictly positive, random, integer values, that sums to sum.

For each image, sum must be greater or equal than width\*height\*depth\*spectrum.

## Default values:

random_function=u.

```
gmic 100 rand_sum 1000
```

---

# Command: replace

## Arguments:

* source,target

## Description:

Replace pixel values in selected images.

```
gmic (1;2;3;4) +replace 2,3
```

---

# Command: replace_inf

## Arguments:

* _expression

## Description:

Replace all infinite values in selected images by specified expression.

```
gmic (0;1;2) log +replace_inf 2
```

---

# Command: replace_infnan

## Arguments:

* _expression

## Description:

Replace all NaN and infinite values in selected images by specified expression.

---

# Command: replace_nan

## Arguments:

* _expression

## Description:

Replace all NaN values in selected images by specified expression.

```
gmic (-1;0;2) sqrt +replace_nan 2
```

---

# Command: replace_seq

## Arguments:

* "search_seq","replace_seq"

## Description:

Search and replace a sequence of values in selected images.

```
gmic (1;2;3;4;5) +replace_seq "2,3,4","7,8"
```

---

# Command: replace_str

## Arguments:

* "search_str","replace_str"

## Description:

Search and replace a string in selected images (viewed as strings, i.e. sequences of character codes).

```
gmic ('"Hello there, how are you ?"') +replace_str "Hello there","Hi David"
```

---

# Command: round

|  |  |
| --- | --- |
|  | Built-in command |

## Arguments:

* rounding_value>=0,_rounding_type    or
* (no arg)

## Description:

Round values of selected images.

rounding_type can be { -1:Backward | 0:Nearest | 1:Forward }.

## Default values:

rounding_type=0.

## Examples of use:

### • Example #1

```
gmic image.jpg +round 100
```

### • Example #2

```
gmic image.jpg mul {pi/180} sin +round
```

---

# Command: roundify

## Arguments:

* gamma>=0

## Description:

Apply roundify transformation on float-valued data, with specified gamma.

## Default values:

gamma=0.

```
gmic 1000 fill '4*x/w' repeat 5 { +roundify[0] {$>*0.2} } append c display_graph 400,300
```

---

# Command: set

|  |  |
| --- | --- |
|  | Built-in command |

## Arguments:

* value,_x[%],_y[%],_z[%],_c[%]

## Description:

Set pixel value in selected images, at specified coordinates.

(*equivalent to shortcut command* =).

If specified coordinates are outside the image bounds, no action is performed.

## Default values:

x=y=z=c=0.

## Examples of use:

### • Example #1

```
gmic 2,2 set 1,0,0 set 2,1,0 set 3,0,1 set 4,1,1
```

### • Example #2

```
gmic image.jpg repeat 10000 { set 255,{u(100)}%,{u(100)}%,0,{u(100)}% }
```

---

# Command: threshold

## Arguments:

* value[%],_is_soft_thresholding={ 0:No | 1:Yes }

## Description:

Threshold values of selected images.

soft can be { 0:Hard-thresholding | 1:Soft-thresholding }.

## Default values:

is_soft=0.

This command has a [tutorial page](https://gmic.eu/tutorial/threshold).

```
gmic image.jpg +threshold[0] 50% +threshold[0] 50%,1
```

---

# Command: vector2tensor

### No argumentsDescription:Convert selected vector fields to corresponding tensor fields.

---

# Command: adjust_colors

## Arguments:

* -100<=_brightness<=100,-100<=_contrast<=100,-100<=_gamma<=100,-100<=_hue_shift<=100,-100<=_saturation<=100,_value_min,_value_max

## Description:

Perform a global adjustment of colors on selected images.

Range of correct image values are considered to be in [value_min,value_max] (e.g. [0,255]).
If value_min==value_max==0, value range is estimated from min/max values of selected images.
Processed images have pixel values constrained in [value_min,value_max].

## Default values:

brightness=0, contrast=0, gamma=0, hue_shift=0, saturation=0, value_min=value_max=0.

```
gmic image.jpg +adjust_colors 0,30,0,0,30
```

---

# Command: apply_channels

## Arguments:

* "command",color_channels,_value_action={ 0:None | 1:Cut | 2:Normalize }

## Description:

Apply specified command on the chosen color channel(s) of each selected images.

(*equivalent to shortcut command* ac).

Argument color_channels refers to a colorspace, and can be basically one of
{ all | rgba | [s]rgb | ryb | lrgb | ycbcr | lab | lch | hsv | hsi | hsl | cmy | cmyk | yiq }.
You can also make the processing focus on a few particular channels of this colorspace,
by setting color_channels as colorspace_channel (e.g. hsv_h for the hue).
All channel values are considered to be provided in the [0,255] range.

## Default values:

value_action=0.

```
gmic image.jpg +apply_channels "equalize blur 2",ycbcr_cbcr
```

---

# Command: bayer2rgb

## Arguments:

* _GM_smoothness,_RB_smoothness1,_RB_smoothness2

## Description:

Transform selected RGB-Bayer sampled images to color images.

## Default values:

GM_smoothness=RB_smoothness=1 and RB_smoothness2=0.5.

```
gmic image.jpg rgb2bayer 0 +bayer2rgb 1,1,0.5
```

---

# Command: brightness

## Arguments:

* strength

## Description:

Change contrast of selected images, with specified strength.

If strength is positive, image brightness is amplified.

If strength is negative, image brightness is reduced.

A typical value range for parameter strength is [-100,100].

```
gmic image.jpg +brightness 20
```

---

# Command: clut

## Arguments:

* "clut_name",_resolution>0,_cut_and_round={ 0:No | 1:Yes }

## Description:

Insert one of the 1149 pre-defined CLUTs at the end of the image list.

clut_name can be { 12_years_a_slave | 1917 | 2-strip-process | 60s | 60s_faded | 60s_faded_alt | 7drk_21 | action_magenta_01 | action_red_01 | ad_astra | adventure_1453 | agfa_apx_100 | agfa_apx_25 | agfa_precisa_100 | agfa_ultra_color_100 | agfa_vista_200 | agressive_highligjtes_recovery_5 | aladdin | alberto_street | alien_green | ampio | amstragram | amstragram+ | analog_film_1 | analogfx_anno_1870_color | analogfx_old_style_i | analogfx_old_style_ii | analogfx_old_style_iii | analogfx_sepia_color | analogfx_soft_sepia_i | analogfx_soft_sepia_ii | anime | ant-man | apocalypse_this_very_moment | aqua | aqua_and_orange_dark | aquaman | arabica_12 | asistas | atomic_pink | atusa | autumn | autumn_leaves | ava_614 | avalanche | avengers_endgame | azrael_93 | baby_driver | bad_boys_for_life | basuco | bboyz_2 | bc_darkum | beach_aqua_orange | beach_faded_analog | beati | beauty_and_the_beast | berlin_sky | bisogno | black_and_white | black_panther | black_star | black_white_01 | black_white_02 | black_white_03 | black_white_04 | black_white_05 | black_white_06 | blade_runner | bleach_bypass | bleachbypass_1 | bleachbypass_2 | bleachbypass_3 | bleachbypass_4 | bleech_bypass_green | bleech_bypass_yellow_01 | blue_cold_fade | blue_dark | blue_house | blue_ice | blue_love_39 | blue_mono | blue_shadows_01 | bluearchitecture | bluehour | blues | bob_ford | bohemian_rhapsody | bombshell | bourbon_64 | boyado | bright_green_01 | bright_teal_orange | bright_warm | brightgreen | brown_mobster | brownbm | brownish | bw_1 | bw_10 | bw_2 | bw_3 | bw_4 | bw_5 | bw_6 | bw_7 | bw_8 | bw_9 | bw_but_yellow | byers_11 | calidum | candlelight | captain_marvel | caribe | chemical_168 | chrome_01 | cineblue | cinebm_4k | cinema | cinema_2 | cinema_3 | cinema_4 | cinema_5 | cinema_noir | cinematic-1 | cinematic-10 | cinematic-2 | cinematic-3 | cinematic-4 | cinematic-5 | cinematic-6 | cinematic-7 | cinematic-8 | cinematic-9 | cinematic_01 | cinematic_02 | cinematic_03 | cinematic_04 | cinematic_05 | cinematic_06 | cinematic_07 | cinematic_for_flog | cinematic_forest | cinematic_lady_bird | cinematic_mexico | city | city_7 | city_dust | city_of_god | classic_films_01 | classic_films_02 | classic_films_03 | classic_films_04 | classic_films_05 | classic_teal_and_orange | clayton_33 | clear | clear_teal_fade | clouseau_54 | cobi_3 | coffee_44 | cold_clear_blue | cold_clear_blue_1 | cold_ice | cold_simplicity_2 | coldchrome | color_rich | colore | colorful_0209 | colornegative | conflict_01 | contrail_35 | contrast_with_highlights_protection | contrasty_afternoon | contrasty_green | convold | cosa | creed_2 | crispautumn | crispromance | crispwarm | crispwinter | cross_process_cp_130 | cross_process_cp_14 | cross_process_cp_15 | cross_process_cp_16 | cross_process_cp_18 | cross_process_cp_3 | cross_process_cp_4 | cross_process_cp_6 | crushin | cubicle_99 | culor | d_o_1 | dark_blues_in_sunlight | dark_green_02 | dark_green_1 | dark_man_x | dark_orange_teal | dark_place_01 | darkandsomber | darkness | date_39 | day_4nite | day_for_night | day_to_night_kings_blue | deep | deep_blue | deep_dark_warm | deep_high_contrast | deep_teal_fade | deep_warm_fade | deepskintones_2 | deepskintones_3 | delicatessen | denoiser_simple_40 | desert_gold_37 | dimension | dimmer | directions_23 | django_25 | doctor_strange | domingo_145 | dream_1 | dream_85 | drop_green_tint_14 | dropblues | dunkirk | duotone_blue_red | earth_tone_boost | eda_0_2 | edgyember | elegance_38 | enchanted | ensaya | eterna_for_flog | expired_69 | expired_fade | expired_polaroid | extreme | fade | fade_to_green | faded | faded_47 | faded_alt | faded_analog | faded_extreme | faded_green | faded_pink-ish | faded_print | faded_retro_01 | faded_retro_02 | faded_vivid | fadedlook | fallcolors | falua | farkling | fatos | faux_infrared | faux_infrared_bw_1 | faux_infrared_color_p_2 | faux_infrared_color_p_3 | faux_infrared_color_r_0a | faux_infrared_color_r_0b | faux_infrared_color_yp_1 | fezzle | fg_cinebasic | fg_cinebright | fg_cinecold | fg_cinedrama | fg_cinetealorange_1 | fg_cinetealorange_2 | fg_cinevibrant | fg_cinewarm | fgcinebasic | fgcinebright | fgcinecold | fgcinedrama | fgcinetealorange_1 | fgcinetealorange_2 | fgcinevibrant | fgcinewarm | fight_club | film_0987 | film_9879 | film_gb-19 | film_high_contrast | film_print_01 | film_print_02 | filmic | filo | flat_30 | flat_blue_moon | flavin | flog_to_rec_709 | foggynight | folger_50 | ford_v_ferrari | foresta | formula_b | french_comedy | frosted | frostedbeachpicnic | fuji_160c | fuji_160c_+ | fuji_160c_++ | fuji_160c_- | fuji_3510_constlclip | fuji_3510_constlmap | fuji_3510_cuspclip | fuji_3513_constlclip | fuji_3513_constlmap | fuji_3513_cuspclip | fuji_400h | fuji_400h_+ | fuji_400h_++ | fuji_400h_- | fuji_800z | fuji_800z_+ | fuji_800z_++ | fuji_800z_- | fuji_astia_100_generic | fuji_astia_100f | fuji_fp-100c | fuji_fp-100c_+ | fuji_fp-100c_++ | fuji_fp-100c_+++ | fuji_fp-100c_++_alt | fuji_fp-100c_- | fuji_fp-100c_-- | fuji_fp-100c_alt | fuji_fp-100c_cool | fuji_fp-100c_cool_+ | fuji_fp-100c_cool_++ | fuji_fp-100c_cool_- | fuji_fp-100c_cool_-- | fuji_fp-100c_negative | fuji_fp-100c_negative_+ | fuji_fp-100c_negative_++ | fuji_fp-100c_negative_+++ | fuji_fp-100c_negative_++_alt | fuji_fp-100c_negative_- | fuji_fp-100c_negative_-- | fuji_fp-3000b | fuji_fp-3000b_+ | fuji_fp-3000b_++ | fuji_fp-3000b_+++ | fuji_fp-3000b_- | fuji_fp-3000b_-- | fuji_fp-3000b_hc | fuji_fp-3000b_negative | fuji_fp-3000b_negative_+ | fuji_fp-3000b_negative_++ | fuji_fp-3000b_negative_+++ | fuji_fp-3000b_negative_- | fuji_fp-3000b_negative_-- | fuji_fp-3000b_negative_early | fuji_fp_100c | fuji_hdr | fuji_neopan_1600 | fuji_neopan_1600_+ | fuji_neopan_1600_++ | fuji_neopan_1600_- | fuji_neopan_acros_100 | fuji_provia_100_generic | fuji_provia_100f | fuji_provia_400f | fuji_provia_400x | fuji_sensia_100 | fuji_superia_100 | fuji_superia_100_+ | fuji_superia_100_++ | fuji_superia_100_- | fuji_superia_1600 | fuji_superia_1600_+ | fuji_superia_1600_++ | fuji_superia_1600_- | fuji_superia_200 | fuji_superia_200_xpro | fuji_superia_400 | fuji_superia_400_+ | fuji_superia_400_++ | fuji_superia_400_- | fuji_superia_800 | fuji_superia_800_+ | fuji_superia_800_++ | fuji_superia_800_- | fuji_superia_hg_1600 | fuji_superia_reala_100 | fuji_superia_x-tra_800 | fuji_velvia_100_generic | fuji_velvia_50 | fuji_xtrans_iii_acros | fuji_xtrans_iii_acros+g | fuji_xtrans_iii_acros+r | fuji_xtrans_iii_acros+ye | fuji_xtrans_iii_astia | fuji_xtrans_iii_classic_chrome | fuji_xtrans_iii_mono | fuji_xtrans_iii_mono+g | fuji_xtrans_iii_mono+r | fuji_xtrans_iii_mono+ye | fuji_xtrans_iii_pro_neg_hi | fuji_xtrans_iii_pro_neg_std | fuji_xtrans_iii_provia | fuji_xtrans_iii_sepia | fuji_xtrans_iii_velvia | fusion_88 | futuristicbleak_1 | futuristicbleak_2 | futuristicbleak_3 | futuristicbleak_4 | going_for_a_walk | golden | golden_bright | golden_fade | golden_mono | golden_night_softner_43 | golden_sony_37 | golden_vibrant | goldengate | goldentime | goldfx_bright_spring_breeze | goldfx_bright_summer_heat | goldfx_hot_summer_heat | goldfx_perfect_sunset_01min | goldfx_perfect_sunset_05min | goldfx_perfect_sunset_10min | goldfx_spring_breeze | goldfx_summer_heat | good_morning | green_15 | green_2025 | green_action | green_afternoon | green_and_orange | green_blues | green_book | green_conflict | green_day_01 | green_day_02 | green_g_09 | green_indoor | green_light | green_mono | green_yellow | greenish_contrasty | greenish_fade | greenish_fade_1 | gremerta | greyhound | hackmanite | hallowen_dark | happyness_133 | hard_teal_orange | hardboost | harsh_day | harsh_sunset | helios | herderite | heulandite | hiddenite | highlights_protection | hilutite | hitman | hlg_1_1 | honey_light | hong_kong | horrorblue | howlite | huesio | husmes | huyan | hydracore | hyla_68 | hypersthene | hypnosis | hypressen | i_tonya | ideo | ilford_delta_100 | ilford_delta_3200 | ilford_delta_3200_+ | ilford_delta_3200_++ | ilford_delta_3200_- | ilford_delta_400 | ilford_fp_4_plus_125 | ilford_hp_5 | ilford_hp_5_+ | ilford_hp_5_++ | ilford_hp_5_- | ilford_hp_5_plus_400 | ilford_hps_800 | ilford_pan_f_plus_50 | ilford_xp_2 | inception | indoor_blue | industrial_33 | infrared_-_dust_pink | instantc | j | jarklin | jojo_rabbit | joker | jumanji_the_next_level | jurassic_world_fallen_kingdom | justice_league | justpeachy | jwick_21 | k_tone_vintage_kodachrome | kahve_3 | kh_1 | kh_10 | kh_2 | kh_3 | kh_4 | kh_5 | kh_6 | kh_7 | kh_8 | kh_9 | killstreak | kingsman_the_golden_circle | knives_out | kodak_2383_constlclip | kodak_2383_constlmap | kodak_2383_cuspclip | kodak_2393_constlclip | kodak_2393_constlmap | kodak_2393_cuspclip | kodak_bw_400_cn | kodak_e-100_gx_ektachrome_100 | kodak_ektachrome_100_vs | kodak_ektachrome_100_vs_generic | kodak_ektar_100 | kodak_elite_100_xpro | kodak_elite_chrome_200 | kodak_elite_chrome_400 | kodak_elite_color_200 | kodak_elite_color_400 | kodak_elite_extracolor_100 | kodak_hie_hs_infra | kodak_kodachrome_200 | kodak_kodachrome_25 | kodak_kodachrome_64 | kodak_kodachrome_64_generic | kodak_portra_160 | kodak_portra_160_+ | kodak_portra_160_++ | kodak_portra_160_- | kodak_portra_160_nc | kodak_portra_160_nc_+ | kodak_portra_160_nc_++ | kodak_portra_160_nc_- | kodak_portra_160_vc | kodak_portra_160_vc_+ | kodak_portra_160_vc_++ | kodak_portra_160_vc_- | kodak_portra_400 | kodak_portra_400_+ | kodak_portra_400_++ | kodak_portra_400_- | kodak_portra_400_nc | kodak_portra_400_nc_+ | kodak_portra_400_nc_++ | kodak_portra_400_nc_- | kodak_portra_400_uc | kodak_portra_400_uc_+ | kodak_portra_400_uc_++ | kodak_portra_400_uc_- | kodak_portra_400_vc | kodak_portra_400_vc_+ | kodak_portra_400_vc_++ | kodak_portra_400_vc_- | kodak_portra_800 | kodak_portra_800_+ | kodak_portra_800_++ | kodak_portra_800_- | kodak_portra_800_hc | kodak_t-max_100 | kodak_t-max_3200 | kodak_t-max_400 | kodak_tmax_3200 | kodak_tmax_3200_+ | kodak_tmax_3200_++ | kodak_tmax_3200_- | kodak_tmax_3200_alt | kodak_tri-x_400 | kodak_tri-x_400_+ | kodak_tri-x_400_++ | kodak_tri-x_400_- | kodak_tri-x_400_alt | korben_214 | la_la_land | landscape | landscape_01 | landscape_02 | landscape_03 | landscape_04 | landscape_05 | landscape_1 | landscape_10 | landscape_2 | landscape_3 | landscape_4 | landscape_5 | landscape_6 | landscape_7 | landscape_8 | landscape_9 | lateafternoonwanderlust | latesunset | lavark | lc_1 | lc_10 | lc_2 | lc_3 | lc_4 | lc_5 | lc_6 | lc_7 | lc_8 | lc_9 | lenox_340 | levex | life_giving_tree | light | light_blown | litore | little_women | logan | lomo | lomography_redscale_100 | lomography_x-pro_slide_200 | london_nights | longbeachmorning | loro | lotta | louetta | low_contrast_blue | low_key_01 | lucky_64 | lushgreen | lushgreensummer | mad_max_fury_road | maesky | magenta_day | magenta_day_01 | magenta_dream | magenta_yellow | magentacoffee | magichour | marriage_story | matrix | mckinnon_75 | memories | mercato | metropolis | milo_5 | minimalistcaffeination | modern_film | modern_films_01 | modern_films_02 | modern_films_03 | modern_films_04 | modern_films_05 | modern_films_06 | modern_films_07 | molti | mono_2 | mono_tinted | monochrome | monochrome_1 | monochrome_2 | moody_1 | moody_10 | moody_2 | moody_3 | moody_4 | moody_5 | moody_6 | moody_7 | moody_8 | moody_9 | moonlight | moonlight_01 | moonlight_2 | moonrise | morning_6 | morroco_16 | mostly_blue | mother! | motus | moviz_1 | moviz_10 | moviz_11 | moviz_12 | moviz_13 | moviz_14 | moviz_15 | moviz_16 | moviz_17 | moviz_18 | moviz_19 | moviz_2 | moviz_20 | moviz_21 | moviz_22 | moviz_23 | moviz_24 | moviz_25 | moviz_26 | moviz_27 | moviz_28 | moviz_29 | moviz_3 | moviz_30 | moviz_31 | moviz_32 | moviz_33 | moviz_34 | moviz_35 | moviz_36 | moviz_37 | moviz_38 | moviz_39 | moviz_4 | moviz_40 | moviz_41 | moviz_42 | moviz_43 | moviz_44 | moviz_45 | moviz_46 | moviz_47 | moviz_48 | moviz_5 | moviz_6 | moviz_7 | moviz_8 | moviz_9 | mucca | mute_shift | muted_01 | muted_fade | mysticpurplesunset | nah | natural_vivid | naturalboost | negative | nemesis | neon_770 | neutral | neutral_pump | neutral_teal_orange | neutral_warm_fade | newspaper | night_01 | night_02 | night_03 | night_04 | night_05 | night_blade_4 | night_king_141 | night_spy | night_view | nightfromday | nightlife | nigrum | no_time_to_die | nostalgiahoney | nostalgic | nw-1 | nw-10 | nw-2 | nw-3 | nw-4 | nw-5 | nw-6 | nw-7 | nw-8 | nw-9 | old_west | once_upon_a_time | once_upon_a_time_in_hollywood | onda | only_red | only_red_and_blue | operation_yellow | orange_dark_4 | orange_dark_7 | orange_dark_look | orange_tone | orange_underexposed | orangeandblue | oranges | padre | paladin | paladin_1875 | parasite | partia | pasadena_21 | passing_by | perso | picola | pink_fade | pirates_of_the_caribbean | pitaya_15 | pmcinematic_01 | pmcinematic_02 | pmcinematic_03 | pmcinematic_04 | pmcinematic_05 | pmcinematic_06 | pmcinematic_07 | pmnight_01 | pmnight_02 | pmnight_03 | pmnight_04 | pmnight_05 | polaroid_664 | polaroid_665 | polaroid_665_+ | polaroid_665_++ | polaroid_665_- | polaroid_665_-- | polaroid_665_negative | polaroid_665_negative_+ | polaroid_665_negative_- | polaroid_665_negative_hc | polaroid_667 | polaroid_669 | polaroid_669_+ | polaroid_669_++ | polaroid_669_+++ | polaroid_669_- | polaroid_669_-- | polaroid_669_cold | polaroid_669_cold_+ | polaroid_669_cold_- | polaroid_669_cold_-- | polaroid_672 | polaroid_690 | polaroid_690_+ | polaroid_690_++ | polaroid_690_- | polaroid_690_-- | polaroid_690_cold | polaroid_690_cold_+ | polaroid_690_cold_++ | polaroid_690_cold_- | polaroid_690_cold_-- | polaroid_690_warm | polaroid_690_warm_+ | polaroid_690_warm_++ | polaroid_690_warm_- | polaroid_690_warm_-- | polaroid_polachrome | polaroid_px-100uv+_cold | polaroid_px-100uv+_cold_+ | polaroid_px-100uv+_cold_++ | polaroid_px-100uv+_cold_+++ | polaroid_px-100uv+_cold_- | polaroid_px-100uv+_cold_-- | polaroid_px-100uv+_warm | polaroid_px-100uv+_warm_+ | polaroid_px-100uv+_warm_++ | polaroid_px-100uv+_warm_+++ | polaroid_px-100uv+_warm_- | polaroid_px-100uv+_warm_-- | polaroid_px-680 | polaroid_px-680_+ | polaroid_px-680_++ | polaroid_px-680_- | polaroid_px-680_-- | polaroid_px-680_cold | polaroid_px-680_cold_+ | polaroid_px-680_cold_++ | polaroid_px-680_cold_++_alt | polaroid_px-680_cold_- | polaroid_px-680_cold_-- | polaroid_px-680_warm | polaroid_px-680_warm_+ | polaroid_px-680_warm_++ | polaroid_px-680_warm_- | polaroid_px-680_warm_-- | polaroid_px-70 | polaroid_px-70_+ | polaroid_px-70_++ | polaroid_px-70_+++ | polaroid_px-70_- | polaroid_px-70_-- | polaroid_px-70_cold | polaroid_px-70_cold_+ | polaroid_px-70_cold_++ | polaroid_px-70_cold_- | polaroid_px-70_cold_-- | polaroid_px-70_warm | polaroid_px-70_warm_+ | polaroid_px-70_warm_++ | polaroid_px-70_warm_- | polaroid_px-70_warm_-- | polaroid_time_zero_expired | polaroid_time_zero_expired_+ | polaroid_time_zero_expired_++ | polaroid_time_zero_expired_- | polaroid_time_zero_expired_-- | polaroid_time_zero_expired_--- | polaroid_time_zero_expired_cold | polaroid_time_zero_expired_cold_- | polaroid_time_zero_expired_cold_-- | polaroid_time_zero_expired_cold_--- | portrait | portrait_1 | portrait_10 | portrait_2 | portrait_3 | portrait_4 | portrait_5 | portrait_6 | portrait_7 | portrait_8 | portrait_9 | progressen | protect_highlights_01 | prussian_blue | pseudogrey | purple | purple_2 | quraqqq_12 | randas | red_afternoon_01 | red_day_01 | red_dream_01 | redblueyellow | reds | reds_oranges_yellows | reeve_38 | remy_24 | rest_33 | retro | retro_brown_01 | retro_magenta_01 | retro_summer_3 | retro_yellow_01 | rocketman | rollei_ir_400 | rollei_ortho_25 | rollei_retro_100_tonal | rollei_retro_80s | rotate_muted | rotate_vibrant | rotated | rotated_crush | satid | saturated_blue | saving_private_damon | scala | science_fiction | scrittle | sea | seges | selor | sensum | separation | serenity | seringe_4 | serpent | seventies_magazine | sevsuz | shade_kings_ink | shadow_king_39 | shine | sicario | sino | skin_tones | slog_to_rec_709_basic | slog_to_rec_709_contrasty | slog_to_rec_709_crush_shadows | slog_to_rec_709_green_correction | smart_contrast | smokey | smooth_clear | smooth_cromeish | smooth_fade | smooth_green_orange | smooth_sailing | smooth_teal_orange | soft_fade | softblackandwhite | softwarming | solarized_color | solarized_color_2 | soldi | spider-man_far_from_home | spotlight | springmorning | sprocket_231 | spy_29 | standard | star_wars_the_rise_of_skywalker | strano | street | stringa | studio_skin_tone_shaper | subtle_blue | subtle_green | subtle_yellow | sully | summer | summer_alt | sunlight_love_11 | sunlightlove | sunny | sunny_alt | sunny_rich | sunny_warm | sunset | sunset_aqua_orange | sunset_intense_violet_blue | sunset_violet_mood | super_warm | super_warm_rich | sutro_fx | sweet_bubblegum | sweet_gelatto | taşdemirrr_1 | taiga | tarraco | teal-orange_for_flog | teal_fade | teal_moonlight | tealmagentagold | tealorange | tealorange_1 | tealorange_2 | tealorange_3 | technicalfx_backlight_filter | teigen_28 | tenet | tensiongreen_1 | tensiongreen_2 | tensiongreen_3 | tensiongreen_4 | terra_4 | the_dark_knight | the_darkest_hour | the_gentelmen | the_grand_budapest_hotel | the_hurt_locker | the_irishman | the_lighthouse | the_lobster | the_martian | the_matrices | the_revenant | the_shape_of_water | the_social_network | the_two_popes | the_way_back | thor_ragnarok | thriller_2 | tirare | toastedgarden | top_gun_maverick | trent_18 | true_colors_8 | turkiest_42 | tutto | tweed_71 | ultra_water | uncut_gems | undeniable | undeniable_2 | underwater | unknown | upglow | urban_01 | urban_02 | urban_03 | urban_04 | urban_05 | urban_cowboy | uzbek_bukhara | uzbek_marriage | uzbek_samarcande | valize | valsky | velvetia | venom | very_warm_greenish | vfb_21 | vibrant | vibrant_alien | vibrant_contrast | vibrant_cromeish | victory | vintage | vintage_01 | vintage_02 | vintage_03 | vintage_04 | vintage_05 | vintage_163 | vintage_alt | vintage_brighter | vintage_chrome | vintage_mob | vintage_warmth_1 | violet_taste | vireo_37 | vita | vivid | vubes | war_for_the_planet_of_the_apes | warm | warm_dark_contrasty | warm_fade | warm_fade_1 | warm_highlight | warm_neutral | warm_sunset_red | warm_teal | warm_vintage | warm_yellow | wavefire | waves | well_see | western | western_6 | westernlut_2 | westernlut_2_13 | whiter_whites | winterlighthouse | wipe | wolf_of_wall_street | wonder_woman | wooden_gold_20 | x-men_dark_phoenix | yangabuz_8 | yellow_55b | yellow_film_01 | yellowstone | you_can_do_it | zed_32 | zeke_39 | zilverfx_bw_solarization | zilverfx_infrared | zilverfx_vintage_bw | zombieland_double_tap }

## Default values:

resolution=33 and cut_and_round=1.

```
gmic clut summer clut alien_green,17 clut orange_dark4,48
```

---

# Command: clut2hald

### No argumentsDescription:Convert selected 3D CLUTs to 2D HaldCLUTs. ``` gmic clut summer +clut2hald ```

---

# Command: cmy2rgb

### No argumentsDescription:Convert color representation of selected images from CMY to RGB.

---

# Command: cmyk2rgb

### No argumentsDescription:Convert color representation of selected images from CMYK to RGB.

---

# Command: colorblind

## Arguments:

* type={ 0:Protanopia | 1:Protanomaly | 2:Deuteranopia | 3:Deuteranomaly | 4:Tritanopia | 5:Tritanomaly | 6:Achromatopsia | 7:Achromatomaly }

## Description:

Simulate color blindness vision.

Simulation method of Vienot, Brettel & Mollon 1999, "Digital video colourmaps for checking the legibility of displays by dichromats".
The dichromacy matrices of the paper were adapted to sRGB (RGB->XYZ).
Anomalous trichromacy simulated via linear interpolation with the identity and a factor of 0.6.

```
gmic image.jpg +colorblind 0
```

---

# Command: colormap

## Arguments:

* nb_levels>=0,_method={ 0:Median-cut | 1:K-means },_sort_vectors

## Description:

Estimate best-fitting colormap with nb_colors entries, to index selected images.

Set nb_levels==0 to extract all existing colors of an image.
sort_vectors can be { 0:Unsorted | 1:By increasing norm | 2:By decreasing occurrence }.

## Default values:

method=1 and sort_vectors=1.

This command has a [tutorial page](https://gmic.eu/oldtutorial/_colormap).

```
gmic image.jpg +colormap[0] 4 +colormap[0] 8 +colormap[0] 16
```

---

# Command: compose_channels

## Arguments:

* _operator

## Description:

Compose all channels of each selected image, using specified arithmetic operator (+,-,or,min,...).

## Default values:

operator=+.

This command has a [tutorial page](https://gmic.eu/tutorial/compose_channels).

```
gmic image.jpg +compose_channels and
```

---

# Command: contrast

## Arguments:

* strength

## Description:

Change contrast of selected images, with specified strength.

If strength is positive, image contrast is amplified.

If strength is negative, image contrast is reduced.

A typical value range for parameter strength is [-100,100].

```
gmic image.jpg +contrast 20
```

---

# Command: count_colors

## Arguments:

* _count_until={ 0:None | >0:Max number of counted colors }

## Description:

Count number of distinct colors in selected images until it reaches the specified max number of counted colors.

Set count_until to 0 to disable limit on counted colors.
This command returns the number of distinct colors for each image (separated by commas).

---

# Command: deltaE

## Arguments:

* [image],_metric={ 0:DeltaE_1976 | 1:DeltaE_2000 },"_to_Lab_command"

## Description:

Compute the CIE DeltaE color difference between selected images and specified [image].

Argument to_Lab_command is a command able to convert colors of [image] into a Lab representation.

## Default values:

metric=1 and to_Lab_command="srgb2lab".

```
gmic image.jpg +blur 2 +deltaE[0] [1],1,srgb2lab
```

---

# Command: direction2rgb

### No argumentsDescription:Compute RGB representation of selected 2D direction fields. ``` gmic image.jpg luminance gradient append c blur 2 orientation +direction2rgb ```

---

# Command: ditheredbw

### No argumentsDescription:Create dithered B&W version of selected images. ``` gmic image.jpg +equalize ditheredbw[-1] ```

---

# Command: fill_color

## Arguments:

* col1,...,colN

## Description:

Fill selected images with specified color.

(*equivalent to shortcut command* fc).

This command has a [tutorial page](https://gmic.eu/oldtutorial/_fill_color).

```
gmic image.jpg +fill_color 255,0,255
```

---

# Command: gradient2rgb

## Arguments:

* _is_orientation={ 0:No | 1:Yes }

## Description:

Compute RGB representation of 2D gradient of selected images.

## Default values:

is_orientation=0.

```
gmic image.jpg +gradient2rgb 0 equalize[-1]
```

---

# Command: hald2clut

### No argumentsDescription:Convert selected 2D HaldCLUTs to 3D CLUTs.

---

# Command: hcy2rgb

### No argumentsDescription:Convert color representation of selected images from HCY to RGB.

---

# Command: hsi2rgb

### No argumentsDescription:Convert color representation of selected images from HSI to RGB.

---

# Command: hsi82rgb

### No argumentsDescription:Convert color representation of selected images from HSI8 to RGB.

---

# Command: hsl2rgb

### No argumentsDescription:Convert color representation of selected images from HSL to RGB.

---

# Command: hsl82rgb

### No argumentsDescription:Convert color representation of selected images from HSL8 to RGB.

---

# Command: hsv2rgb

### No argumentsDescription:Convert color representation of selected images from HSV to RGB. ``` gmic (0,360;0,360^0,0;1,1^1,1;1,1) resize 400,400,1,3,3 hsv2rgb ```

---

# Command: hsv82rgb

### No argumentsDescription:Convert color representation of selected images from HSV8 to RGB.

---

# Command: int2rgb

### No argumentsDescription:Convert color representation of selected images from INT24 to RGB.

---

# Command: ipremula

### No argumentsDescription:Convert selected images with premultiplied alpha colors to normal colors. See also:[premula](premula.html).

---

# Command: jzazbz2rgb

## Arguments:

* illuminant={ 0:D50 | 1:D65 | 2:E }    or
* (no arg)

## Description:

Convert color representation of selected images from RGB to Jzazbz.

## Default values:

illuminant=2.

---

# Command: jzazbz2xyz

### No argumentsDescription:Convert color representation of selected images from RGB to XYZ.

---

# Command: lab2lch

### No argumentsDescription:Convert color representation of selected images from Lab to Lch.

---

# Command: lab2rgb

## Arguments:

* illuminant={ 0:D50 | 1:D65 | 2:E }    or
* (no arg)

## Description:

Convert color representation of selected images from Lab to RGB.

## Default values:

illuminant=2.

```
gmic (50,50;50,50^-3,3;-3,3^-3,-3;3,3) resize 400,400,1,3,3 lab2rgb
```

---

# Command: lab2srgb

## Arguments:

* illuminant={ 0:D50 | 1:D65 | 2:E }    or
* (no arg)

## Description:

Convert color representation of selected images from Lab to sRGB.

## Default values:

illuminant=2.

```
gmic (50,50;50,50^-3,3;-3,3^-3,-3;3,3) resize 400,400,1,3,3 lab2rgb
```

---

# Command: lab82srgb

## Arguments:

* illuminant={ 0:D50 | 1:D65 | 2:E }    or
* (no arg)

## Description:

Convert color representation of selected images from Lab8 to sRGB.

## Default values:

illuminant=2.

```
gmic (50,50;50,50^-3,3;-3,3^-3,-3;3,3) resize 400,400,1,3,3 lab2rgb
```

---

# Command: lab2xyz

## Arguments:

* illuminant={ 0:D50 | 1:D65 | 2:E }    or
* (no arg)

## Description:

Convert color representation of selected images from Lab to XYZ.

## Default values:

illuminant=2.

---

# Command: lab82rgb

## Arguments:

* illuminant={ 0:D50 | 1:D65 | 2:E }    or
* (no arg)

## Description:

Convert color representation of selected images from Lab8 to RGB.

## Default values:

illuminant=2.

---

# Command: lch2lab

### No argumentsDescription:Convert color representation of selected images from Lch to Lab.

---

# Command: lch2rgb

## Arguments:

* illuminant={ 0:D50 | 1:D65 | 2:E }    or
* (no arg)

## Description:

Convert color representation of selected images from Lch to RGB.

## Default values:

illuminant=2.

---

# Command: lch82rgb

## Arguments:

* illuminant={ 0:D50 | 1:D65 | 2:E }    or
* (no arg)

## Description:

Convert color representation of selected images from Lch8 to RGB.

## Default values:

illuminant=2.

---

# Command: luminance

### No argumentsDescription:Compute luminance of selected sRGB images. This command has a [tutorial page](https://gmic.eu/tutorial/luminance). ``` gmic image.jpg +luminance ```

---

# Command: lightness

### No argumentsDescription:Compute lightness of selected sRGB images. ``` gmic image.jpg +lightness ```

---

# Command: lut_contrast

## Arguments:

* _nb_colors>1,_min_rgb_value

## Description:

Generate a RGB colormap where consecutive colors have high contrast.

This function performs a specific score maximization to generate the result, so
it may take some time when nb_colors is high.

## Default values:

nb_colors=256 and min_rgb_value=64.

---

# Command: map_clut

## Arguments:

* [clut] | "clut_name"

## Description:

Map specified RGB color LUT to selected images.

```
gmic image.jpg uniform_distribution {2^6},3 mirror[-1] x +map_clut[0] [1]
```

---

# Command: match_histogram

## Arguments:

* [reference_image],_nb_levels>0,_color_channels

## Description:

Transfer histogram of the specified reference image to selected images.

Argument color channels is the same as with command apply_channels.

## Default values:

nb_levels=256 and color_channels=all.

```
gmic image.jpg 100,100,1,3,"u([256,200,100])" +match_histogram[0] [1]
```

---

# Command: match_pca

## Arguments:

* [reference_image],_color_channels

## Description:

Transfer mean and covariance matrix of specified vector-valued reference image to selected images.

Argument color channels is the same as with command apply_channels.

## Default values:

color_channels=all.

```
gmic sample lena,earth +match_pca[0] [1]
```

---

# Command: match_rgb

## Arguments:

* [reference],_gamma>=0,_regularization>=0,_luminosity_constraints>=0,_rgb_resolution>=0,_is_constraints={ 0:No | 1:Yes }

## Description:

Transfer colors from specified reference image (given as argument) to selected image.

gamma determines the importance of color occurrences in the matching process (0:None to 1:Huge).
regularization determines the number of guided filter iterations to remove quantization effects.
luminosity_constraints tells if luminosity constraints must be applied on non-confident matched colors.
is_constraints tells if additional hard color constraints must be set (opens an interactive window).

## Default values:

gamma=0.3,regularization=8, luminosity_constraints=0.1, rgb_resolution=64 and is_constraints=0.

```
gmic sample pencils,wall +match_rgb[0] [1],0,0.01
```

---

# Command: mix_rgb

## Arguments:

* a11,a12,a13,a21,a22,a23,a31,a32,a33

## Description:

Apply 3x3 specified matrix to RGB colors of selected images.

## Default values:

a11=1, a12=a13=a21=0, a22=1, a23=a31=a32=0 and a33=1.

This command has a [tutorial page](https://gmic.eu/tutorial/mix_rgb).

```
gmic image.jpg +mix_rgb 0,1,0,1,0,0,0,0,1
```

---

# Command: oklab2rgb

### No argumentsDescription:Convert color representation of selected images from OKlab to RGB. (see colorspace definition at: <https://bottosson.github.io/posts/oklab/> ). See also:[rgb2oklab](rgb2oklab.html).

---

# Command: palette

## Arguments:

* palette_name | palette_number

## Description:

Input specified color palette at the end of the image list.

palette_name can be { default | hsv | lines | hot | cool | jet | flag | cube | rainbow | parula | spring | summer | autumn | winter | bone | copper | pink | vga | algae | amp | balance | curl | deep | delta | dense | diff | gray | haline | ice | matter | oxy | phase | rain | solar | speed | tarn | tempo | thermal | topo | turbid | aurora | hocuspocus | srb2 | uzebox | amiga7800 | amiga7800mess | fornaxvoid1 }

```
gmic palette hsv
```

---

# Command: premula

### No argumentsDescription:Convert selected images with normal colors to premultiplied alpha colors. After conversion, alpha channel of resulting images has value in [0,1] range. See also:[ipremula](ipremula.html).

---

# Command: pseudogray

## Arguments:

* _max_increment>=0,_JND_threshold>=0,_bits_depth>0

## Description:

Generate pseudogray colormap with specified increment and perceptual threshold.

If JND_threshold is 0, no perceptual constraints are applied.

## Default values:

max_increment=5, JND_threshold=2.3 and bits_depth=8.

```
gmic pseudogray 5
```

---

# Command: random_clut

## Arguments:

* _seed = { >=0 | -1 }

## Description:

Generate a 33x33x33 random 3D color LUT.

If specified seed is positive, it is used as a seed for the random number generator @cli : (so that using the same seed will return the same CLUT).

```
gmic image.jpg random_clut +map_clut.. .
```

---

# Command: random_clut

## Arguments:

* _seed = { >=0 | -1 }

## Description:

Generate a 33x33x33 random 3D color LUT.

If specified seed is positive, it is used as a seed for the random number generator @cli : (so that using the same seed will return the same CLUT).

```
gmic image.jpg random_clut +map_clut.. .
```

---

# Command: replace_color

## Arguments:

* tolerance[%]>=0,smoothness[%]>=0,src1,src2,...,dest1,dest2,...

## Description:

Replace pixels from/to specified colors in selected images.

```
gmic image.jpg +replace_color 40,3,204,153,110,255,0,0
```

---

# Command: retinex

## Arguments:

* _value_offset>0,_colorspace={ hsi | hsv | lab | lrgb | rgb | ycbcr },0<=_min_cut<=100,0<=_max_cut<=100,_sigma_low>0,_sigma_mid>0,_sigma_high>0

## Description:

Apply multi-scale retinex algorithm on selected images to improve color consistency.

(as described in the page <http://www.ipol.im/pub/art/2014/107/>).

## Default values:

offset=1, colorspace=hsv, min_cut=1, max_cut=1, sigma_low=15,sigma_mid=80 and sigma_high=250.

---

# Command: rgb

## Arguments:

* _min_RGB_value,_max_RGB_value    or
* (no arg)

## Description:

Return a random int-valued RGB color.

---

# Command: rgba

## Arguments:

* _min_RGB_value,_max_RGB_value,_min_A_value,_max_A_value    or
* (no_arg)

## Description:

Return a random int-valued RGBA color.

---

# Command: rgb2bayer

## Arguments:

* _start_pattern=0,_color_grid=0

## Description:

Transform selected color images to RGB-Bayer sampled images.

## Default values:

start_pattern=0 and color_grid=0.

```
gmic image.jpg +rgb2bayer 0
```

---

# Command: rgb2cmy

### No argumentsDescription:Convert color representation of selected images from RGB to CMY. ``` gmic image.jpg rgb2cmy split c ```

---

# Command: rgb2cmyk

### No argumentsDescription:Convert color representation of selected images from RGB to CMYK. Examples of use:• Example #1 ``` gmic image.jpg rgb2cmyk split c ``` • Example #2 ``` gmic image.jpg rgb2cmyk split c fill[3] 0 append c cmyk2rgb ```

---

# Command: rgb2hcy

### No argumentsDescription:Convert color representation of selected images from RGB to HCY. ``` gmic image.jpg rgb2hcy split c ```

---

# Command: rgb2hsi

### No argumentsDescription:Convert color representation of selected images from RGB to HSI. ``` gmic image.jpg rgb2hsi split c ```

---

# Command: rgb2hsi8

### No argumentsDescription:Convert color representation of selected images from RGB to HSI8. ``` gmic image.jpg rgb2hsi8 split c ```

---

# Command: rgb2hsl

### No argumentsDescription:Convert color representation of selected images from RGB to HSL. Examples of use:• Example #1 ``` gmic image.jpg rgb2hsl split c ``` • Example #2 ``` gmic image.jpg rgb2hsl +split c add[-3] 100 mod[-3] 360 append[-3--1] c hsl2rgb ```

---

# Command: rgb2hsl8

### No argumentsDescription:Convert color representation of selected images from RGB to HSL8. ``` gmic image.jpg rgb2hsl8 split c ```

---

# Command: rgb2hsv

### No argumentsDescription:Convert color representation of selected images from RGB to HSV. Examples of use:• Example #1 ``` gmic image.jpg rgb2hsv split c ``` • Example #2 ``` gmic image.jpg rgb2hsv +split c add[-2] 0.3 cut[-2] 0,1 append[-3--1] c hsv2rgb ```

---

# Command: rgb2hsv8

### No argumentsDescription:Convert color representation of selected images from RGB to HSV8. ``` gmic image.jpg rgb2hsv8 split c ```

---

# Command: rgb2int

### No argumentsDescription:Convert color representation of selected images from RGB to INT24 scalars. ``` gmic image.jpg rgb2int ```

---

# Command: rgb2jzazbz

## Arguments:

* illuminant={ 0:D50 | 1:D65 | 2:E }    or
* (no arg)

## Description:

Convert color representation of selected images from RGB to Jzazbz.

## Default values:

illuminant=2.

---

# Command: rgb2lab

## Arguments:

* illuminant={ 0:D50 | 1:D65 | 2:E }    or
* (no arg)

## Description:

Convert color representation of selected images from RGB to Lab.

## Default values:

illuminant=2.

---

# Command: rgb2lab8

## Arguments:

* illuminant={ 0:D50 | 1:D65 | 2:E }    or
* (no arg)

## Description:

Convert color representation of selected images from RGB to Lab8.

## Default values:

illuminant=2.

```
gmic image.jpg rgb2lab8 split c
```

---

# Command: rgb2lch

## Arguments:

* illuminant={ 0:D50 | 1:D65 | 2:E }    or
* (no arg)

## Description:

Convert color representation of selected images from RGB to Lch.

## Default values:

illuminant=2.

```
gmic image.jpg rgb2lch split c
```

---

# Command: rgb2lch8

## Arguments:

* illuminant={ 0:D50 | 1:D65 | 2:E }    or
* (no arg)

## Description:

Convert color representation of selected images from RGB to Lch8.

## Default values:

illuminant=2.

```
gmic image.jpg rgb2lch8 split c
```

---

# Command: rgb2luv

### No argumentsDescription:Convert color representation of selected images from RGB to LUV. ``` gmic image.jpg rgb2luv split c ```

---

# Command: rgb2oklab

### No argumentsDescription:Convert color representation of selected images from RGB to Oklab. (see colorspace definition at: <https://bottosson.github.io/posts/oklab/> ). See also:[oklab2rgb](oklab2rgb.html).

---

# Command: rgb2ryb

### No argumentsDescription:Convert color representation of selected images from RGB to RYB. ``` gmic image.jpg rgb2ryb split c ```

---

# Command: rgb2srgb

### No argumentsDescription:Convert color representation of selected images from linear RGB to sRGB.

---

# Command: rgb2xyz

## Arguments:

* illuminant={ 0:D50 | 1:D65 | 2:E }    or
* (no arg)

## Description:

Convert color representation of selected images from RGB to XYZ.

## Default values:

illuminant=2.

```
gmic image.jpg rgb2xyz split c
```

---

# Command: rgb2xyz8

## Arguments:

* illuminant={ 0:D50 | 1:D65 | 2:E }    or
* (no arg)

## Description:

Convert color representation of selected images from RGB to XYZ8.

## Default values:

illuminant=2.

```
gmic image.jpg rgb2xyz8 split c
```

---

# Command: rgb2yiq

### No argumentsDescription:Convert color representation of selected images from RGB to YIQ. ``` gmic image.jpg rgb2yiq split c ```

---

# Command: rgb2yiq8

### No argumentsDescription:Convert color representation of selected images from RGB to YIQ8. ``` gmic image.jpg rgb2yiq8 split c ```

---

# Command: rgb2ycbcr

### No argumentsDescription:Convert color representation of selected images from RGB to YCbCr. ``` gmic image.jpg rgb2ycbcr split c ```

---

# Command: rgb2yuv

### No argumentsDescription:Convert color representation of selected images from RGB to YUV. ``` gmic image.jpg rgb2yuv split c ```

---

# Command: rgb2yuv8

### No argumentsDescription:Convert color representation of selected images from RGB to YUV8. ``` gmic image.jpg rgb2yuv8 split c ```

---

# Command: remove_opacity

### No argumentsDescription:Remove opacity channel of selected images.

---

# Command: ryb2rgb

### No argumentsDescription:Convert color representation of selected images from RYB to RGB.

---

# Command: select_color

## Arguments:

* tolerance[%]>=0,col1,...,colN

## Description:

Select pixels with specified color in selected images.

This command has a [tutorial page](https://gmic.eu/oldtutorial/_select_color).

```
gmic image.jpg +select_color 40,204,153,110
```

---

# Command: sepia

### No argumentsDescription:Apply sepia tones effect on selected images. ``` gmic image.jpg sepia ```

---

# Command: solarize

### No argumentsDescription:Solarize selected images. ``` gmic image.jpg solarize ```

---

# Command: split_colors

## Arguments:

* _tolerance>=0,_max_nb_outputs>0,_min_area>0

## Description:

Split selected images as several image containing a single color.

One selected image can be split as at most max_nb_outputs images.
Output images are sorted by decreasing area of extracted color regions and have an additional alpha-channel.

## Default values:

tolerance=0, max_nb_outputs=256 and min_area=8.

```
gmic image.jpg quantize 5 +split_colors , display_rgba
```

---

# Command: split_opacity

### No argumentsDescription:Split color and opacity parts of selected images. This command returns 1 or 2 images for each selected image, whether it has an opacity channel or not.

---

# Command: split_vector

## Arguments:

* keep_splitting_values={ +:Increasing | -:Decreasing },value1,_value2,...

## Description:

Split selected images into multiple parts, where specified vector [value1,_value2,...] is the separator.

---

# Command: srgb2lab

## Arguments:

* illuminant={ 0:D50 | 1:D65 | 2:E }    or
* (no arg)

## Description:

Convert color representation of selected images from sRGB to Lab.

## Default values:

illuminant=2.

## Examples of use:

### • Example #1

```
gmic image.jpg srgb2lab split c
```

### • Example #2

```
gmic image.jpg srgb2lab +split c mul[-2,-1] 2.5 append[-3--1] c lab2srgb
```

---

# Command: srgb2lab8

## Arguments:

* illuminant={ 0:D50 | 1:D65 | 2:E }    or
* (no arg)

## Description:

Convert color representation of selected images from sRGB to Lab8.

## Default values:

illuminant=2.

---

# Command: srgb2rgb

### No argumentsDescription:Convert color representation of selected images from sRGB to linear RGB.

---

# Command: to_a

### No argumentsDescription:Force selected images to have an alpha channel.

---

# Command: to_color

### No argumentsDescription:Force selected images to be in color mode (RGB or RGBA).

---

# Command: to_colormode

## Arguments:

* mode={ 0:Adaptive | 1:G | 2:GA | 3:RGB | 4:RGBA }

## Description:

Force selected images to be in a given color mode.

## Default values:

mode=0.

---

# Command: to_gray

### No argumentsDescription:Force selected images to be in GRAY mode. ``` gmic image.jpg +to_gray ```

---

# Command: to_graya

### No argumentsDescription:Force selected images to be in GRAYA mode.

---

# Command: to_pseudogray

## Arguments:

* _max_step>=0,_is_perceptual_constraint={ 0:No | 1:Yes },_bits_depth>0

## Description:

Convert selected scalar images ([0-255]-valued) to pseudo-gray color images.

## Default values:

max_step=5, is_perceptual_constraint=1 and bits_depth=8.

The original pseudo-gray technique has been introduced by Rich Franzen <http://r0k.us/graphics/pseudoGrey.html>.
Extension of this technique to arbitrary increments for more tones, has been done by David Tschumperlé.

---

# Command: to_rgb

### No argumentsDescription:Force selected images to be in RGB mode.

---

# Command: to_rgba

### No argumentsDescription:Force selected images to be in RGBA mode.

---

# Command: to_automode

### No argumentsDescription:Force selected images to be in the most significant color mode. This commands checks for useless alpha channel (all values equal to 255), as well as detects grayscale images encoded as color images.

---

# Command: xyz2jzazbz

### No argumentsDescription:Convert color representation of selected images from XYZ to RGB.

---

# Command: xyz2lab

## Arguments:

* illuminant={ 0:D50 | 1:D65 | 2:E }    or
* (no arg)

## Description:

Convert color representation of selected images from XYZ to Lab.

## Default values:

illuminant=2.

---

# Command: xyz2rgb

## Arguments:

* illuminant={ 0:D50 | 1:D65 | 2:E }    or
* (no arg)

## Description:

Convert color representation of selected images from XYZ to RGB.

## Default values:

illuminant=2.

---

# Command: xyz82rgb

## Arguments:

* illuminant={ 0:D50 | 1:D65 | 2:E }    or
* (no arg)

## Description:

Convert color representation of selected images from XYZ8 to RGB.

## Default values:

illuminant=2.

---

# Command: ycbcr2rgb

### No argumentsDescription:Convert color representation of selected images from YCbCr to RGB.

---

# Command: yiq2rgb

### No argumentsDescription:Convert color representation of selected images from YIQ to RGB.

---

# Command: yiq82rgb

### No argumentsDescription:Convert color representation of selected images from YIQ8 to RGB.

---

# Command: yuv2rgb

### No argumentsDescription:Convert color representation of selected images from YUV to RGB.

---

# Command: yuv82rgb

### No argumentsDescription:Convert selected images from YUV8 to RGB color bases.

---

# Command: append

|  |  |
| --- | --- |
|  | Built-in command |

## Arguments:

* [image],axis,_centering    or
* axis,_centering

## Description:

Append specified image to selected images, or all selected images together, along specified axis.

(*equivalent to shortcut command* a).

axis can be { x | y | z | c }.
Usual centering values are { 0:left-justified | 0.5:centered | 1:right-justified }.

## Default values:

centering=0.

## Examples of use:

### • Example #1

```
gmic image.jpg split y,10 reverse append y
```

### • Example #2

```
gmic image.jpg repeat 5 { +rows[0] 0,{10+18*$>}% } remove[0] append x,0.5
```

### • Example #3

```
gmic image.jpg append[0] [0],y
```

---

# Command: append_tiles

## Arguments:

* _M>=0,_N>=0,0<=_centering_x<=1,0<=_centering_y<=1

## Description:

Append MxN selected tiles as new images.

If N is set to 0, number of rows is estimated automatically.
If M is set to 0, number of columns is estimated automatically.
If M and N are both set to 0, auto-mode is used.
If M or N is set to 0, only a single image is produced.
centering_x and centering_y tells about the centering of tiles when they have different sizes.

## Default values:

M=0, N=0, centering_x=centering_y=0.5.

```
gmic image.jpg split xy,4 append_tiles ,
```

---

# Command: apply_scales

## Arguments:

* "command",number_of_scales>0,_min_scale[%]>=0,_max_scale[%]>=0,_scale_gamma>0,_interpolation

## Description:

Apply specified command on different scales of selected images.

interpolation can be { 0:None | 1:Nearest | 2:Average | 3:Linear | 4:Grid | 5:Bicubic | 6:Lanczos }.

## Default values:

min_scale=25%, max_scale=100% and interpolation=3.

```
gmic image.jpg apply_scales "blur 5 sharpen 1000",4
```

---

# Command: autocrop

## Arguments:

* _axes,_value1,_value2,...

## Description:

Autocrop selected images according to specified axes and values.

axes can be { x | y | z | c | xy | xz | xc | yz | yc | zc | xyz | xyc | xzc | yzc | xyzc }.
If no axes are provided, autocrop is assumed to be spatial only (e.g. axes=xyz).
If no value arguments are provided, cropping value is automatically guessed.

## Default values:

axes=xyz.

## See also:

[autocrop_coords](autocrop_coords.html).

```
gmic 400,400,1,3 fill_color 64,128,255 ellipse 50%,50%,120,120,0,1,255 +autocrop
```

---

# Command: autocrop_components

## Arguments:

* _threshold[%],_min_area[%]>=0,_is_high_connectivity={ 0:No | 1:Yes },_output_type={ 0:Crop | 1:Segmentation | 2:Coordinates }

## Description:

Autocrop and extract connected components in selected images, according to a mask given as the last channel of

each of the selected image (e.g. alpha-channel).

## Default values:

threshold=0%, min_area=0.1%, is_high_connectivity=0 and output_type=1.

```
gmic 256,256 noise 0.1,2 eq 1 dilate_circ 20 label_fg 0,1 normalize 0,255 +neq 0 *[-1] 255 append c +autocrop_components ,
```

---

# Command: autocrop_coords

## Arguments:

* _axes,_value1,_value2,...

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

## Arguments:

* value1,value2,... | auto

## Description:

Autocrop selected images using the crop geometry of the last one by specified vector-valued intensity,

or by automatic guessing the cropping value.

## Default values:

auto mode.

```
gmic image.jpg +fill[-1] 0 ellipse[-1] 50%,50%,30%,20%,0,1,1 autocrop_seq 0
```

---

# Command: channels

## Arguments:

* c0[%],_c1[%],_boundary_conditions

## Description:

Keep only specified channels of selected images.

boundary_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.

## Default values:

c1=c0 and boundary_conditions=0.

## Examples of use:

### • Example #1

```
gmic image.jpg channels 1
```

### • Example #2

```
gmic image.jpg luminance channels 0,2
```

---

# Command: columns

## Arguments:

* x0[%],_x1[%],_boundary_conditions

## Description:

Keep only specified columns of selected images.

boundary_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.

## Default values:

x1=x0 and boundary_conditions=0.

```
gmic image.jpg columns -25%,50%
```

---

# Command: crop

|  |  |
| --- | --- |
|  | Built-in command |

## Arguments:

* x0[%],x1[%],_boundary_conditions    or
* x0[%],y0[%],x1[%],y1[%],_boundary_conditions    or
* x0[%],y0[%],z0[%],x1[%],y1[%],z1[%],_boundary_conditions    or
* x0[%],y0[%],z0[%],c0[%],x1[%],y1[%],z1[%],c1[%],_boundary_conditions

## Description:

Crop selected images with specified region coordinates.

(*equivalent to shortcut command* z).

boundary_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.

## Default values:

boundary_conditions=0.

## Examples of use:

### • Example #1

```
gmic image.jpg +crop -230,-230,280,280,1 crop[0] -230,-230,280,280,0
```

### • Example #2

```
gmic image.jpg crop 25%,25%,75%,75%
```

---

# Command: elevate

## Arguments:

* _depth,_is_plain={ 0:No | 1:Yes },_is_colored={ 0:No | 1:Yes }

## Description:

Elevate selected 2D images into 3D volumes.

## Default values:

depth=64, is_plain=1 and is_colored=1.

```
gmic sample colorful,64 +elevate 32
```

---

# Command: expand

## Arguments:

* axes,size[%],_boundary_conditions={ 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }

## Description:

Expand selected images along the specified axes.

axes can be { x | y | z | c | xy | xz | xc | yz | yc | zc | xyz | xyc | xzc | yzc | xyzc }.

## Default values:

boundary_conditions=0.

```
gmic image.jpg expand xy,30
```

---

# Command: extract

## Arguments:

* "condition",_output_type={ 0:XYZC-coords | 1:XYZ-coords | 2:Scalar-values | 3:Vector-values | 4:XYZC-coords + scalar value | 5:XYZ-coords + vector-values }

## Description:

Extract a list of coordinates or values from selected image, where

specified mathematical condition holds.
For N coordinates matching, result is a 1xNx1x4 image.

## Default values:

output_type=0.

```
gmic sp lena +extract "norm(I)>128",3
```

---

# Command: extract_region

## Arguments:

* [label_image],_extract_xyz_coordinates={ 0:No | 1:Yes },_label_1,...,_label_M

## Description:

Extract all pixels of selected images whose corresponding label in [label_image] is equal to label_m,

and output them as M column images.

## Default values:

extract_xyz_coordinates=0.

```
gmic image.jpg +blur 3 quantize. 4,0 +extract_region[0] [1],0,1,3
```

---

# Command: montage

## Arguments:

* "_layout_code",_montage_mode={ 0<=centering<=1 | 2<=scale+2<=3 },_output_mode={ 0:Single layer | 1:Multiple layers },"_processing_command"

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

layout_code=X, montage_mode=2, output_mode='0' and processing_command="".

```
gmic image.jpg sample ? +plasma[0] 1 shape_cupid 256 normalize 0,255 frame xy,3,0 frame xy,10,255 to_rgb +montage A +montage[^-1] H1:V0:VH2:1H0:3
```

---

# Command: mirror

|  |  |
| --- | --- |
|  | Built-in command |

## Arguments:

* { x | y | z }...{ x | y | z }

## Description:

Mirror selected images along specified axes.

## Examples of use:

### • Example #1

```
gmic image.jpg +mirror y +mirror[0] c
```

### • Example #2

```
gmic image.jpg +mirror x +mirror y append_tiles 2,2
```

---

# Command: permute

|  |  |
| --- | --- |
|  | Built-in command |

## Arguments:

* permutation_string

## Description:

Permute selected image axes by specified permutation.

permutation is a combination of the character set {x|y|z|c},
e.g. xycz, cxyz, ...

```
gmic image.jpg permute yxzc
```

---

# Command: rescale2d

## Arguments:

* _width[%]={ 0:Any | >0 },_height[%]={ 0:Any | >0 },-1=<_interpolation<=6,_mode={ 0:Inside | 1:Padded-inside | 2:Outside | 3:Cropped-outside }

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

## Arguments:

* _width[%]={ 0:Any | >0 },_height[%]={ 0:Any | >0 },_depth[%]={ 0:Any | >0 },-1=<_interpolation<=6,_mode={ 0:Inside | 1:Padded-inside | 2:Outside | 3    or
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

|  |  |
| --- | --- |
|  | Built-in command |

## Arguments:

* {[image_w] | width[%]>0},_{[image_h] | height[%]>0},_{[image_d] | depth[%]>0},_{[image_s] | spectrum[%]>0},_interpolation,_boundary_conditions,_ax,_ay,_az,_ac

## Description:

Resize selected images with specified geometry.

(*equivalent to shortcut command* r).

interpolation can be { -1:None (memory content) | 0:None | 1:Nearest | 2:Average | 3:Linear | 4=Grid | 5=Bicubic | 6=Lanczos }.
boundary_conditions has different meanings, according to the chosen interpolation mode :
. When 'interpolation=={ -1 | 1 | 2 | 4 }', boundary_conditions is meaningless.
. When interpolation==0, boundary_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.
. When 'interpolation=={ 3 | 5 | 6 }', boundary_conditions can be { 0:None | 1:Neumann }.
ax,ay,az,ac set the centering along each axis when interpolation=0 or 4
(set to 0 by default, must be defined in range [0,1]).

## Default values:

interpolation=1, boundary_conditions=0 and ax=ay=az=ac=0.

```
gmic image.jpg +resize[-1] 256,128,1,3,2 +resize[-1] 120%,120%,1,3,0,1,0.5,0.5 +resize[-1] 120%,120%,1,3,0,0,0.2,0.2 +resize[-1] [0],[0],1,3,4
```

---

# Command: resize_as_image

## Arguments:

* [reference],_interpolation,_boundary_conditions,_ax,_ay,_az,_ac

## Description:

Resize selected images to the geometry of specified [reference] image.

(*equivalent to shortcut command* ri).

## Default values:

interpolation=1, boundary_conditions=0 and ax=ay=az=ac=0.

```
gmic image.jpg sample duck +resize_as_image[-1] [-2]
```

---

# Command: resize_displacement

## Arguments:

* width[%]>0,_height[%]>0,_depth[%]>0

## Description:

Resize selected displacement fields with specified geometry.

During the process, the displacement vectors are also scaled by the corresponding ratios along each axis.

## Default values:

height=100% and depth=100%.

---

# Command: resize_mn

## Arguments:

* width[%]>=0,_height[%]>=0,_depth[%]>=0,_B_value,_C_value

## Description:

Resize selected images with Mitchell-Netravali filter (cubic).

For details about the method, see: <https://de.wikipedia.org/wiki/Mitchell-Netravali-Filter>.

## Default values:

height=100%, depth=100%, B=0.3333 and C=0.3333.

```
gmic image.jpg rescale2d 32 resize_mn 800%,800%
```

---

# Command: resize_pow2

## Arguments:

* _interpolation,_boundary_conditions,_ax,_ay,_az,_ac

## Description:

Resize selected images so that each dimension is a power of 2.

interpolation can be { -1:None (memory content) | 0:None | 1:Nearest | 2:Average | 3:Linear | 4:Grid | 5:Bicubic | 6:Lanczos }.
boundary_conditions has different meanings, according to the chosen interpolation mode :
. When 'interpolation=={ -1 | 1 | 2 | 4 }', boundary_conditions is meaningless.
. When interpolation==0, boundary_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.
. When 'interpolation=={ 3 | 5 | 6 }', boundary_conditions can be { 0:None | 1:Neumann }.
ax,ay,az,ac set the centering along each axis when interpolation=0
(set to 0 by default, must be defined in range [0,1]).

## Default values:

interpolation=0, boundary_conditions=0 and ax=ay=az=ac=0.

```
gmic image.jpg +resize_pow2[-1] 0
```

---

# Command: rotate

|  |  |
| --- | --- |
|  | Built-in command |

## Arguments:

* angle,_interpolation,_boundary_conditions,_center_x[%],_center_y[%]    or
* u,v,w,angle,interpolation,boundary_conditions,_center_x[%],_center_y[%],_center_z[%]

## Description:

Rotate selected images with specified angle (in deg.), and optionally 3D axis (u,v,w).

interpolation can be { 0:None | 1:Linear | 2:Bicubic }.
boundary_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.
When a rotation center (cx,cy,_cz) is specified, the size of the image is preserved.

## Default values:

interpolation=1, boundary_conditions=0 and center_x=center_y=(undefined).

```
gmic image.jpg +rotate -25,1,2,50%,50% rotate[0] 25
```

---

# Command: rotate_tileable

## Arguments:

* angle,_max_size_factor>=0

## Description:

Rotate selected images by specified angle and make them tileable.

If resulting size of an image is too big, the image is replaced by a 1x1 image.

## Default values:

max_size_factor=8.

```
gmic sample colorful,128 +rotate_tileable 16
```

---

# Command: rows

## Arguments:

* y0[%],_y1[%],_boundary_conditions

## Description:

Keep only specified rows of selected images.

boundary_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.

## Default values:

y1=y0 and boundary_conditions=0.

```
gmic image.jpg rows -25%,50%
```

---

# Command: scale2x

### No argumentsDescription:Double XY-size of selected images, using the Scale2x algorithm. ``` gmic image.jpg threshold 50% resize 50%,50% +scale2x ```

---

# Command: scale2x_cnn

## Arguments:

* _sharpness>=0

## Description:

Double XY-size of selected images, using a convolutional neural network.

## Default values:

sharpness=1.25.

```
gmic image.jpg rescale2d 128 +scale2x_cnn ,
```

---

# Command: scale3x

### No argumentsDescription:Triple XY-size of selected images, using the Scale3x algorithm. ``` gmic image.jpg threshold 50% resize 33%,33% +scale3x ```

---

# Command: scale_dcci2x

## Arguments:

* _edge_threshold>=0,_exponent>0,_extend_1px={ 0:No | 1:Yes }

## Description:

Double XY-size of selected images, using a directional cubic convolution interpolation,

as described in <https://en.wikipedia.org/wiki/Directional_Cubic_Convolution_Interpolation>.

## Default values:

edge_threshold=1.15, exponent=5 and extend_1px=0.

```
gmic image.jpg rescale2d 128 +scale_dcci2x ,
```

---

# Command: seamcarve

## Arguments:

* _width[%]>=0,_height[%]>=0,_is_priority_channel={ 0:No | 1:Yes },_is_antialiasing={ 0:No | 1:Yes },_maximum_seams[%]>=0

## Description:

Resize selected images with specified 2D geometry, using the seam-carving algorithm.

## Default values:

height=100%, is_priority_channel=0, is_antialiasing=1 and maximum_seams=25%.

```
gmic image.jpg seamcarve 60%
```

---

# Command: shift

|  |  |
| --- | --- |
|  | Built-in command |

## Arguments:

* vx[%],_vy[%],_vz[%],_vc[%],_boundary_conditions,_interpolation={ 0:Nearest_neighbor | 1:Linear }

## Description:

Shift selected images by specified displacement vector.

Displacement vector can be non-integer in which case linear interpolation should be chosen.
boundary_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.

## Default values:

boundary_conditions=0 and interpolation=0.

```
gmic image.jpg +shift[0] 50%,50%,0,0,0 +shift[0] 50%,50%,0,0,1 +shift[0] 50%,50%,0,0,2
```

---

# Command: shrink

## Arguments:

* axes,size[%],_boundary_conditions={ 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }

## Description:

Shrink selected images along the specified axes.

axes can be { x | y | z | c | xy | xz | xc | yz | yc | zc | xyz | xyc | xzc | yzc | xyzc }.

## Default values:

boundary_conditions=0.

```
gmic image.jpg shrink xy,100
```

---

# Command: slices

## Arguments:

* z0[%],_z1[%],_boundary_conditions

## Description:

Keep only specified slices of selected images.

boundary_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.

## Default values:

z1=z0 and boundary_conditions=0.

---

# Command: sort

|  |  |
| --- | --- |
|  | Built-in command |

## Arguments:

* _ordering={ +:Increasing | -:Decreasing },_axis={ x | y | z | c }

## Description:

Sort pixel values of selected images.

If axis is specified, the sorting is done according to the data of the first column/row/slice/channel
of selected images.

## Default values:

ordering=+ and axis=(undefined).

```
gmic 64 rand 0,100 +sort display_graph 400,300,3
```

---

# Command: split

|  |  |
| --- | --- |
|  | Built-in command |

## Arguments:

* { x | y | z | c }...{ x | y | z | c },_split_mode[%],_max_parts>0    or
* keep_splitting_values={ +:Increasing | -:Decreasing },_{ x | y | z | c }...{ x | y | z | c },value1,_value2,...    or
* (no arg)

## Description:

Split selected images along specified axes, or regarding to a sequence of scalar values

(optionally along specified axes).

(*equivalent to shortcut command* s).

Argument split_mode determines how the split is done. It can be :

0: Split image according to consecutive constant values;

N (where N is a positive integer): Split image into N homogeneous parts;

-N[%] (where N is a positive integer): Split image as blocks of size N(opt. specified as a percentage of the image dimension).

When specified, max_parts defines a limit in the number of resulting images.

## Default values:

N=-1.

## Examples of use:

### • Example #1

```
gmic image.jpg split c
```

### • Example #2

```
gmic image.jpg split y,3
```

### • Example #3

```
gmic image.jpg split x,-128
```

### • Example #4

```
gmic image.jpg split x,-30%,2
```

### • Example #5

```
gmic 1,20,1,1,"1,2,3,4" +split -,2,3 append[1--1] y
```

### • Example #6

```
gmic (1,2,2,3,3,3,4,4,4,4) +split x,0 append[1--1] y
```

---

# Command: split_tiles

## Arguments:

* M!=0,_N!=0,_is_homogeneous={ 0:No | 1:Yes }

## Description:

Split selected images as a MxN array of tiles.

If M or N is negative, it stands for the tile size instead.

## Default values:

N=M and is_homogeneous=0.

```
gmic image.jpg +local split_tiles 5,4 blur 3,0 sharpen 700 append_tiles 4,5 done
```

---

# Command: undistort

## Arguments:

* -1<=_amplitude<=1,_aspect_ratio,_zoom,_center_x[%],_center_y[%],_boundary_conditions

## Description:

Correct barrel/pincushion distortions occurring with wide-angle lens.

References:
[1] Zhang Z. (1999). Flexible camera calibration by viewing a plane from unknown orientation.
[2] Andrew W. Fitzgibbon (2001). Simultaneous linear estimation of multiple view geometry and lens distortion.
boundary_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.

## Default values:

amplitude=0.25, aspect_ratio=0, zoom=0, center_x=center_y=50% and boundary_conditions=0.

---

# Command: unroll

|  |  |
| --- | --- |
|  | Built-in command |

## Arguments:

* _axis={ x | y | z | c }

## Description:

Unroll selected images along specified axis.

(*equivalent to shortcut command* y).

## Default values:

axis=y.

```
gmic (1,2,3;4,5,6;7,8,9) +unroll y
```

---

# Command: upscale_smart

## Arguments:

* width[%],_height[%],_depth,_smoothness>=0,_anisotropy=[0,1],sharpening>=0

## Description:

Upscale selected images with an edge-preserving algorithm.

## Default values:

height=100%, depth=100%, smoothness=2, anisotropy=0.4 and sharpening=10.

```
gmic image.jpg rescale2d ,100 +upscale_smart 500%,500% append x
```

---

# Command: volumetric2d

## Arguments:

* _x[%],_y[%],_z[%],_separator_size>=0

## Description:

Convert selected 3D volumetric images into a 2D representation.

## Default values:

x=y=z=50% and separator_size=0.

```
gmic image.jpg rescale2d 64 animate noise,0,100,50 cut 0,255 append z volumetric2d 50%,50%,50%,1
```

---

# Command: bandpass

## Arguments:

* _min_freq[%],_max_freq[%]

## Description:

Apply bandpass filter to selected images.

## Default values:

min_freq=0 and max_freq=20%.

This command has a [tutorial page](https://gmic.eu/oldtutorial/_bandpass).

```
gmic image.jpg bandpass 1%,3%
```

---

# Command: bilateral

|  |  |
| --- | --- |
|  | Built-in command |

## Arguments:

* [guide],std_deviation_s[%]>=0,std_deviation_r[%]>=0,_sampling_s>=0,_sampling_r>=0    or
* std_deviation_s[%]>=0,std_deviation_r[%]>=0,_sampling_s>=0,_sampling_r>=0

## Description:

Blur selected images by anisotropic (eventually joint/cross) bilateral filtering.

If a guide image is provided, it is used for drive the smoothing filter.
A guide image must be of the same xyz-size as the selected images.
Set sampling arguments to 0 for automatic adjustment.

```
gmic image.jpg repeat 5 { bilateral 10,10 }
```

---

# Command: blur

|  |  |
| --- | --- |
|  | Built-in command |

## Arguments:

* std_deviation[%]>=0,_boundary_conditions,_kernel    or
* axes,std_deviation[%]>=0,_boundary_conditions,_kernel

## Description:

Blur selected images by a Deriche or gaussian filter (recursive implementation).

(*equivalent to shortcut command* b).

boundary_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.
kernel can be { 0:Deriche | 1:Gaussian }.
When specified, argument axes is a sequence of { x | y | z | c }.
Specifying one axis multiple times apply also the blur multiple times.

## Default values:

boundary_conditions=1 and kernel=1.

This command has a [tutorial page](https://gmic.eu/oldtutorial/_blur).

## Examples of use:

### • Example #1

```
gmic image.jpg +blur 5,0 +blur[0] 5,1
```

### • Example #2

```
gmic image.jpg +blur y,10%
```

---

# Command: blur_angular

## Arguments:

* amplitude[%],_center_x[%],_center_y[%]

## Description:

Apply angular blur on selected images.

## Default values:

center_x=center_y=50%.

This command has a [tutorial page](https://gmic.eu/oldtutorial/_blur_angular).

```
gmic image.jpg blur_angular 2%
```

---

# Command: blur_bloom

## Arguments:

* _amplitude>=0,_ratio>=0,_nb_iter>=0,_blend_operator={ + | max | min },_kernel={ 0:Deriche | 1:Gaussian | 2:Box | 3:Triangle | 4:Quadratic },_normalize_scales={ 0:No | 1:Yes },_axes

## Description:

Apply a bloom filter that blend multiple blur filters of different radii,

resulting in a larger but sharper glare than a simple blur.
When specified, argument axes is a sequence of { x | y | z | c }.
Specifying one axis multiple times apply also the blur multiple times.
Reference: Masaki Kawase, "Practical Implementation of High Dynamic Range Rendering", GDC 2004.

## Default values:

amplitude=1, ratio=2, nb_iter=5, blend_operator=+, kernel=1, normalize_scales=0 and axes=(all)

```
gmic image.jpg blur_bloom ,
```

---

# Command: blur_linear

## Arguments:

* amplitude1[%],_amplitude2[%],_angle,_boundary_conditions={ 0:Dirichlet | 1:Neumann }

## Description:

Apply linear blur on selected images, with specified angle and amplitudes.

## Default values:

amplitude2=0, angle=0 and boundary_conditions=1.

This command has a [tutorial page](https://gmic.eu/oldtutorial/_blur_linear).

```
gmic image.jpg blur_linear 10,0,45
```

---

# Command: blur_radial

## Arguments:

* amplitude[%],_center_x[%],_center_y[%]

## Description:

Apply radial blur on selected images.

## Default values:

center_x=center_y=50%.

This command has a [tutorial page](https://gmic.eu/oldtutorial/_blur_radial).

```
gmic image.jpg blur_radial 2%
```

---

# Command: blur_selective

## Arguments:

* sigma>=0,_edges>0,_nb_scales>0

## Description:

Blur selected images using selective gaussian scales.

## Default values:

sigma=5, edges=0.5 and nb_scales=5.

This command has a [tutorial page](https://gmic.eu/oldtutorial/_blur_selective).

```
gmic image.jpg noise 20 cut 0,255 +local[-1] repeat 4 { blur_selective , } done
```

---

# Command: boxfilter

|  |  |
| --- | --- |
|  | Built-in command |

## Arguments:

* size[%]>=0,_order,_boundary_conditions,_nb_iter>=0    or
* axes,size[%]>=0,_order,_boundary_conditions,_nb_iter>=0

## Description:

Blur selected images by a box filter of specified size (fast recursive implementation).

order can be { 0:Smooth | 1:1st-derivative | 2:2nd-derivative }.
boundary_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.
When specified, argument axes is a sequence of { x | y | z | c }.
Specifying one axis multiple times apply also the blur multiple times.

## Default values:

order=0, boundary_conditions=1 and nb_iter=1.

## Examples of use:

### • Example #1

```
gmic image.jpg +boxfilter 5%
```

### • Example #2

```
gmic image.jpg +boxfilter y,3,1
```

---

# Command: bump2normal

### No argumentsDescription:Convert selected bumpmaps to normalmaps. ``` gmic 300,300 circle 50%,50%,128,1,255 blur 2% +bump2normal ```

---

# Command: closing

## Arguments:

* size>=0    or
* size_x>=0,size_y>=0,_size_z>=0    or
* [kernel],_boundary_conditions,_is_real={ 0:Binary-mode | 1:Real-mode }

## Description:

Apply morphological closing to selected images.

boundary_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.

## Default values:

size_z=1, boundary_conditions=1 and is_real=0.

```
gmic image.jpg +closing 10
```

---

# Command: closing_circ

## Arguments:

* _size>=0,_is_real={ 0:No | 1:Yes }

## Description:

Apply circular dilation of selected images by specified size.

## Default values:

boundary_conditions=1 and is_real=0.

```
gmic image.jpg +closing_circ 7
```

---

# Command: convolve

|  |  |
| --- | --- |
|  | Built-in command |

## Arguments:

* [mask],_boundary_conditions,_is_normalized={ 0:No | 1:Yes },_channel_mode,_xcenter,_ycenter,_zcenter,_xstride>0,_ystride>0,_zstride>0,_xdilation,_ydilation,_zdilation,_xoffset,_yoffset,_zoffset,_xsize>=0,_ysize>=0,_zsize>=0

## Description:

Convolve selected images by specified mask.

boundary_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.
channel_mode can be { 0:All | 1:One-for-one | 2:Partial sum | 3:Full sum }.

## Default values:

boundary_conditions=1, is_normalized=0, channel_mode=1, xcenter=ycenter=zcenter=(undefined), xstride=ystride=zstride=1, xdilation=ydilation=zdilation=1,xoffset=yoffset=zoffset=0 and xsize=ysize=zsize=(input_size/stride).

This command has a [tutorial page](https://gmic.eu/oldtutorial/_convolve).

## Examples of use:

### • Example #1

```
gmic image.jpg (0,1,0;1,-4,1;0,1,0) convolve[-2] [-1] keep[-2]
```

### • Example #2

```
gmic image.jpg (0,1,0) resize[-1] 130,1,1,1,3 +convolve[0] [1]
```

---

# Command: convolve_fft

## Arguments:

* [mask],_boundary_conditions

## Description:

Convolve selected images with specified mask, in the fourier domain.

boundary_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.

```
gmic image.jpg 100%,100% gaussian[-1] 20,1,45 +convolve_fft[0] [1]
```

---

# Command: correlate

|  |  |
| --- | --- |
|  | Built-in command |

## Arguments:

* [mask],_boundary_conditions,_is_normalized={ 0:No | 1:Yes },_channel_mode,_xcenter,_ycenter,_zcenter,_xstride>0,_ystride>0,_zstride>0,_xdilation,_ydilation,_zdilation,_xoffset,_yoffset,_zoffset,_xsize>=0,_ysize>=0,_zsize>=0

## Description:

Correlate selected images by specified mask.

boundary_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.
channel_mode can be { 0:All | 1:One-for-one | 2:Partial sum | 3:Full sum }.

## Default values:

boundary_conditions=1, is_normalized=0, channel_mode=1, xcenter=ycenter=zcenter=-1, xstride=ystride=zstride=1, xdilation=ydilation=zdilation=1,xoffset=yoffset=zoffset=0 and xsize=ysize=zsize=(input_size/stride).

## Examples of use:

### • Example #1

```
gmic image.jpg (0,1,0;1,-4,1;0,1,0) correlate[-2] [-1] keep[-2]
```

### • Example #2

```
gmic image.jpg +crop 40%,40%,60%,60% +correlate[0] [-1],0,1
```

---

# Command: cross_correlation

## Arguments:

* [mask]

## Description:

Compute cross-correlation of selected images with specified mask.

```
gmic image.jpg +shift -30,-20 +cross_correlation[0] [1]
```

---

# Command: curvature

### No argumentsDescription:Compute isophote curvatures on selected images. ``` gmic image.jpg blur 10 curvature ```

---

# Command: dct

## Arguments:

* _{ x | y | z }...{ x | y | z }    or
* (no arg)

## Description:

Compute the discrete cosine transform of selected images, optionally along the specified axes only.

Output images are always evenly sized, so this command may change the size of the selected images.

## Default values:

(no arg)

## See also:

[idct](idct.html).

This command has a [tutorial page](https://gmic.eu/oldtutorial/_dct-and-idct).

```
gmic image.jpg +dct +idct[-1] abs[-2] +[-2] 1 log[-2]
```

---

# Command: deblur

## Arguments:

* amplitude[%]>=0,_nb_iter>=0,_dt>=0,_regul>=0,_regul_type={ 0:Tikhonov | 1:Meancurv. | 2:TV }

## Description:

Deblur image using a regularized Jansson-Van Cittert algorithm.

## Default values:

nb_iter=10, dt=20, regul=0.7 and regul_type=1.

```
gmic image.jpg blur 3 +deblur 3,40,20,0.01
```

---

# Command: deblur_goldmeinel

## Arguments:

* sigma>=0,_nb_iter>=0,_acceleration>=0,_kernel_type={ 0:Deriche | 1:Gaussian }.

## Description:

Deblur selected images using Gold-Meinel algorithm

## Default values:

nb_iter=8, acceleration=1 and kernel_type=1.

```
gmic image.jpg +blur 1 +deblur_goldmeinel[-1] 1
```

---

# Command: deblur_richardsonlucy

## Arguments:

* sigma>=0, nb_iter>=0, _kernel_type={ 0:Deriche | 1:Gaussian }.

## Description:

Deblur selected images using Richardson-Lucy algorithm.

## Default values:

nb_iter=50 and kernel_type=1.

```
gmic image.jpg +blur 1 +deblur_richardsonlucy[-1] 1
```

---

# Command: deconvolve_fft

## Arguments:

* [kernel],_regularization>=0

## Description:

Deconvolve selected images by specified mask in the fourier space.

## Default values:

regularization>=0.

```
gmic image.jpg +gaussian 5 +convolve_fft[0] [1] +deconvolve_fft[-1] [1]
```

---

# Command: deinterlace

## Arguments:

* _method

## Description:

Deinterlace selected images (method can be { 0:Standard | 1:Motion-compensated }).

## Default values:

method=0.

```
gmic image.jpg +rotate 3,1,1,50%,50% resize 100%,50% resize 100%,200%,1,3,4 shift[-1] 0,1 add +deinterlace 1
```

---

# Command: denoise

|  |  |
| --- | --- |
|  | Built-in command |

## Arguments:

* [guide],std_deviation_s[%]>=0,std_deviation_r[%]>=0,_patch_size>0,_lookup_size>0,_smoothness,_fast_approx={ 0:No | 1:Yes }    or
* std_deviation_s[%]>=0,std_deviation_r[%]>=0,_patch_size>0,_lookup_size>0,_smoothness,_fast_approx={ 0:No | 1:Yes }

## Description:

Denoise selected images by non-local patch averaging.

## Default values:

patch_size=5, lookup_size=6 and smoothness=1.

```
gmic image.jpg +denoise 5,5,8
```

---

# Command: denoise_haar

## Arguments:

* _threshold>=0,_nb_scales>=0,_cycle_spinning>0

## Description:

Denoise selected images using haar-wavelet thresholding with cycle spinning.

Set nb_scales==0 to automatically determine the optimal number of scales.

## Default values:

threshold=1.4, nb_scale=0 and cycle_spinning=10.

```
gmic image.jpg noise 20 cut 0,255 +denoise_haar[-1] 0.8
```

---

# Command: denoise_cnn

## Arguments:

* _noise_level>=0,_patch_size>0

## Description:

Denoise selected images using a convolutional neural network (CNN).

Input value range should be [0,255]. Output value range is [0,255].
If std_noise==0, the noise level is automatically estimated for each selected image.

## Default values:

noise_level=0 (auto) and patch_size=64.

```
gmic image.jpg noise 20 cut 0,255 +denoise_cnn 0
```

---

# Command: denoise_patchpca

## Arguments:

* _strength>=0,_patch_size>0,_lookup_size>0,_spatial_sampling>0

## Description:

Denoise selected images using the patch-pca algorithm.

## Default values:

patch_size=7, lookup_size=11, details=1.8 and spatial_sampling=5.

```
gmic image.jpg +noise 20 cut[-1] 0,255 +denoise_patchpca[-1] ,
```

---

# Command: deriche

|  |  |
| --- | --- |
|  | Built-in command |

## Arguments:

* std_deviation[%]>=0,order={ 0 | 1 | 2 },axis={ x | y | z | c },_boundary_conditions

## Description:

Apply Deriche recursive filter on selected images, along specified axis and with

specified standard deviation, order and boundary conditions.
boundary_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.

## Default values:

boundary_conditions=1.

This command has a [tutorial page](https://gmic.eu/oldtutorial/_deriche).

## Examples of use:

### • Example #1

```
gmic image.jpg deriche 3,1,x
```

### • Example #2

```
gmic image.jpg +deriche 30,0,x deriche[-2] 30,0,y add
```

---

# Command: dilate

|  |  |
| --- | --- |
|  | Built-in command |

## Arguments:

* size[%]>=0    or
* size_x[%]>=0,size_y[%]>=0,size_z[%]>=0    or
* [kernel],_boundary_conditions,_is_real={ 0:Binary-mode | 1:Real-mode }

## Description:

Dilate selected images by a rectangular or the specified structuring element.

boundary_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.

## Default values:

size_z=1, boundary_conditions=1 and is_real=0.

```
gmic image.jpg +dilate 10
```

---

# Command: dilate_circ

## Arguments:

* _size[%]>=0,_boundary_conditions,_is_real={ 0:No | 1:Yes }

## Description:

Apply circular dilation of selected images by specified size.

boundary_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.

## Default values:

boundary_conditions=1 and is_real=0.

```
gmic image.jpg +dilate_circ 7
```

---

# Command: dilate_oct

## Arguments:

* _size[%]>=0,_boundary_conditions,_is_real={ 0:No | 1:Yes }

## Description:

Apply octagonal dilation of selected images by specified size.

## Default values:

boundary_conditions=1 and is_real=0.

```
gmic image.jpg +dilate_oct 7
```

---

# Command: dilate_threshold

## Arguments:

* size_x>=1,size_y>=1,size_z>=1,_threshold>=0,_boundary_conditions

## Description:

Dilate selected images in the (X,Y,Z,I) space.

boundary_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.

## Default values:

size_y=size_x, size_z=1, threshold=255 and boundary_conditions=1.

---

# Command: divergence

### No argumentsDescription:Compute divergence of selected vector fields. ``` gmic image.jpg luminance +gradient append[-2,-1] c divergence[-1] ```

---

# Command: dog

## Arguments:

* _sigma1[%]>=0,_sigma2[%]>=0

## Description:

Compute difference of gaussian on selected images.

## Default values:

sigma1=2% and sigma2=3%.

```
gmic image.jpg dog 2,3
```

---

# Command: diffusiontensors

## Arguments:

* _sharpness>=0,0<=_anisotropy<=1,_alpha[%],_sigma[%],is_sqrt={ 0:No | 1:Yes }

## Description:

Compute the diffusion tensors of selected images for edge-preserving smoothing algorithms.

## Default values:

sharpness=0.7, anisotropy=0.3, alpha=0.6, sigma=1.1 and is_sqrt=0.

This command has a [tutorial page](https://gmic.eu/oldtutorial/_diffusiontensors).

```
gmic image.jpg diffusiontensors 0.8 abs pow 0.2
```

---

# Command: erode

|  |  |
| --- | --- |
|  | Built-in command |

## Arguments:

* size[%]>=0    or
* size_x[%]>=0,size_y[%]>=0,_size_z[%]>=0    or
* [kernel],_boundary_conditions,_is_real={ 0:Binary-mode | 1:Real-mode }

## Description:

Erode selected images by a rectangular or the specified structuring element.

boundary_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.

## Default values:

size_z=1, boundary_conditions=1 and is_real=0.

```
gmic image.jpg +erode 10
```

---

# Command: erode_circ

## Arguments:

* _size[%]>=0,_boundary_conditions,_is_real={ 0:No | 1:Yes }

## Description:

Apply circular erosion of selected images by specified size.

boundary_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.

## Default values:

boundary_conditions=1 and is_real=0.

```
gmic image.jpg +erode_circ 7
```

---

# Command: erode_oct

## Arguments:

* _size[%]>=0,_boundary_conditions,_is_real={ 0:No | 1:Yes }

## Description:

Apply octagonal erosion of selected images by specified size.

## Default values:

boundary_conditions=1 and is_real=0.

```
gmic image.jpg +erode_oct 7
```

---

# Command: erode_threshold

## Arguments:

* size_x>=1,size_y>=1,size_z>=1,_threshold>=0,_boundary_conditions

## Description:

Erode selected images in the (X,Y,Z,I) space.

boundary_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.

## Default values:

size_y=size_x, size_z=1, threshold=255 and boundary_conditions=1.

---

# Command: fft

|  |  |
| --- | --- |
|  | Built-in command |

## Arguments:

* _{ x | y | z }...{ x | y | z }

## Description:

Compute the direct fourier transform (real and imaginary parts) of selected images,

optionally along the specified axes only.

## See also:

[ifft](ifft.html).

This command has a [tutorial page](https://gmic.eu/oldtutorial/_fft).

## Examples of use:

### • Example #1

```
gmic image.jpg luminance +fft append[-2,-1] c norm[-1] log[-1] shift[-1] 50%,50%,0,0,2
```

### • Example #2

```
gmic image.jpg w2:=int(w/2) h2:=int(h/2) fft shift $w2,$h2,0,0,2 ellipse $w2,$h2,30,30,0,1,0 shift -$w2,-$h2,0,0,2 ifft remove[-1]
```

---

# Command: gradient

## Arguments:

* { x | y | z | c }...{ x | y | z | c },_scheme,_boundary_conditions    or
* (no arg)

## Description:

Compute the gradient components (first derivatives) of selected images, along specified axes.

(*equivalent to shortcut command* g).

scheme can be { -1:Backward | 0:Centered | 1:Forward | 2:Sobel | 3:Rotation-invariant (default) | 4:Deriche | 5:Vanvliet | 6:FB-Maxabs }.
boundary_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.
(no arg) compute all significant components.

## Default values:

scheme=0 and boundary_conditions=1.

This command has a [tutorial page](https://gmic.eu/oldtutorial/_gradient).

```
gmic image.jpg gradient
```

---

# Command: gradient_norm

## Arguments:

* _scheme,_boundary_conditions    or
* (no arg)

## Description:

Compute the gradient norm of selected images.

scheme can be { -1:Backward | 0:Centered | 1:Forward | 2:Sobel | 3:Rotation-invariant (default) | 4:Deriche | 5:Vanvliet | 6:FB-Maxabs }.
boundary_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.

## Default values:

scheme=0 and boundary_conditions=1.

This command has a [tutorial page](https://gmic.eu/oldtutorial/_gradient_norm).

```
gmic image.jpg gradient_norm equalize
```

---

# Command: gradient_orientation

## Arguments:

* _dimension={ 1 | 2 | 3 }

## Description:

Compute N-d gradient orientation of selected images.

## Default values:

dimension=3.

```
gmic image.jpg +gradient_orientation 2
```

---

# Command: guided

|  |  |
| --- | --- |
|  | Built-in command |

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

```
gmic image.jpg +guided 5,400
```

---

# Command: haar

## Arguments:

* scale>0

## Description:

Compute the direct haar multiscale wavelet transform of selected images.

## See also:

[ihaar](ihaar.html).

This command has a [tutorial page](https://gmic.eu/oldtutorial/_haar).

---

# Command: heat_flow

## Arguments:

* _nb_iter>=0,_dt,_keep_sequence={ 0:No | 1:Yes }

## Description:

Apply iterations of the heat flow on selected images.

## Default values:

nb_iter=10, dt=30 and keep_sequence=0.

```
gmic image.jpg +heat_flow 20
```

---

# Command: hessian

## Arguments:

* { xx | xy | xz | yy | yz | zz }...{ xx | xy | xz | yy | yz | zz },_boundary_conditions    or
* (no arg) :

## Description:

Compute the hessian components (second derivatives) of selected images along specified axes.

boundary_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.
(no arg) compute all significant components.

## Default values:

boundary_conditions=1.

```
gmic image.jpg hessian
```

---

# Command: idct

## Arguments:

* _{ x | y | z }...{ x | y | z }    or
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

### No argumentsDescription:Compute gradient-orthogonal-directed 2nd derivative of image(s). ``` gmic image.jpg iee ```

---

# Command: ifft

|  |  |
| --- | --- |
|  | Built-in command |

## Arguments:

* _{ x | y | z }...{ x | y | z }

## Description:

Compute the inverse fourier transform (real and imaginary parts) of selected images.

optionally along the specified axes only.

## See also:

[fft](fft.html).

This command has a [tutorial page](https://gmic.eu/oldtutorial/_fft).

---

# Command: ihaar

## Arguments:

* scale>0

## Description:

Compute the inverse haar multiscale wavelet transform of selected images.

## See also:

[haar](haar.html).

This command has a [tutorial page](https://gmic.eu/oldtutorial/_haar).

---

# Command: ilaplacian

## Arguments:

* { nb_iterations>0 | 0 },_[initial_estimate]

## Description:

Invert selected Laplacian images.

If given nb_iterations is 0, inversion is done in Fourier space (single iteration),
otherwise, by applying nb_iterations of a Laplacian-inversion PDE flow.
Note that the resulting inversions are just estimation of possible/approximated solutions.

## Default values:

nb_iterations=0, axes=(undefined) and [initial_estimated]=(undefined).

```
gmic image.jpg +laplacian +ilaplacian[-1] 0
```

---

# Command: inn

### No argumentsDescription:Compute gradient-directed 2nd derivative of image(s). ``` gmic image.jpg inn ```

---

# Command: inpaint

|  |  |
| --- | --- |
|  | Built-in command |

## Arguments:

* [mask]    or
* [mask],0,_fast_method    or
* [mask],_patch_size>=1,_lookup_size>=1,_lookup_factor>=0,_lookup_increment!=0,_blend_size>=0,0<=_blend_threshold<=1,_blend_decay>=0,_blend_scales>=1,_is_blend_outer={ 0:No | 1:Yes }

## Description:

Inpaint selected images by specified mask.

If no patch size (or 0) is specified, inpainting is done using a fast average or median algorithm.
Otherwise, it used a patch-based reconstruction method, that can be very time consuming.
fast_method can be { 0:Low-connectivity average | 1:High-connectivity average | 2:Low-connectivity median | 3:High-connectivity median }.

## Default values:

patch_size=0, fast_method=1, lookup_size=22, lookup_factor=0.5, lookup_increment=1, blend_size=0, blend_threshold=0, blend_decay=0.05, blend_scales=10 and is_blend_outer=1.

## Examples of use:

### • Example #1

```
gmic image.jpg 100%,100% ellipse 50%,50%,30,30,0,1,255 ellipse 20%,20%,30,10,0,1,255 +inpaint[-2] [-1] remove[-2]
```

### • Example #2

```
gmic image.jpg 100%,100% circle 30%,30%,30,1,255,0,255 circle 70%,70%,50,1,255,0,255 +inpaint[0] [1],5,15,0.5,1,9,0 remove[1]
```

---

# Command: inpaint_pde

## Arguments:

* [mask],_nb_scales[%],_diffusion_type={ 0:Isotropic | 1:Delaunay-guided | 2:Edge-guided | 3:Mask-guided },_diffusion_iter>=0

## Description:

Inpaint selected images by specified mask using a multiscale transport-diffusion algorithm.

Argument nb_scales sets the number of scales used in the multi-scale resolution scheme.

When the % qualifier is used for nb_scales, the number of used scales is relative to nb_scales_max = ceil(log2(max(w,h,d))).

When nb_scales<0, it determines the minimum image size encountered at the lowest scale.

If diffusion_type==3, non-zero values of the mask (e.g. a distance function) are used
to guide the diffusion process.

## Default values:

nb_scales=-9, diffusion_type=1 and diffusion_iter=20.

```
gmic image.jpg 100%,100% ellipse[-1] 30%,30%,40,30,0,1,255 +inpaint_pde[0] [1]
```

---

# Command: inpaint_flow

## Arguments:

* [mask],_nb_global_iter>=0,_nb_local_iter>=0,_dt>0,_alpha>=0,_sigma>=0

## Description:

Apply iteration of the inpainting flow on selected images.

## Default values:

nb_global_iter=10, nb_local_iter=100, dt=5, alpha=1 and sigma=3.

```
gmic image.jpg 100%,100% ellipse[-1] 30%,30%,40,30,0,1,255 inpaint_flow[0] [1]
```

---

# Command: inpaint_holes

## Arguments:

* maximal_area[%]>=0,_tolerance>=0,_is_high_connectivity={ 0:No | 1:Yes }

## Description:

Inpaint all connected regions having an area less than specified value.

## Default values:

maximal_area=4, tolerance=0 and is_high_connectivity=0.

```
gmic image.jpg noise 5%,2 +inpaint_holes 8,40
```

---

# Command: inpaint_morpho

## Arguments:

* [mask]

## Description:

Inpaint selected images by specified mask using morphological operators.

```
gmic image.jpg 100%,100% ellipse[-1] 30%,30%,40,30,0,1,255 +inpaint_morpho[0] [1]
```

---

# Command: inpaint_matchpatch

## Arguments:

* [mask],_nb_scales={ 0:Auto | >0 },_patch_size>0,_nb_iterations_per_scale>0,_blend_size>=0,_allow_outer_blending={ 0:No | 1:Yes },_is_already_initialized={ 0:No | 1:Yes }

## Description:

Inpaint selected images by specified binary mask, using a multi-scale matchpatch algorithm.

## Default values:

nb_scales=0, patch_size=9, nb_iterations_per_scale=10, blend_size=5,allow_outer_blending=1 and is_already_initialized=0.

```
gmic image.jpg 100%,100% ellipse[-1] 30%,30%,40,30,0,1,255 +inpaint_matchpatch[0] [1]
```

---

# Command: kuwahara

## Arguments:

* size>0

## Description:

Apply Kuwahara filter of specified size on selected images.

```
gmic image.jpg kuwahara 9
```

---

# Command: laplacian

### No argumentsDescription:Compute Laplacian of selected images. ``` gmic image.jpg laplacian ```

---

# Command: lic

## Arguments:

* _amplitude>0,_channels>0

## Description:

Render LIC representation of selected vector fields.

## Default values:

amplitude=30 and channels=1.

```
gmic 400,400,1,2,'!c?x-w/2:y-h/2' +lic 200,3 quiver[-2] [-2],10,1,1,1,255
```

---

# Command: map_tones

## Arguments:

* _threshold>=0,_gamma>=0,_smoothness>=0,nb_iter>=0

## Description:

Apply tone mapping operator on selected images, based on Poisson equation.

## Default values:

threshold=0.1, gamma=0.8, smoothness=0.5 and nb_iter=30.

```
gmic image.jpg +map_tones ,
```

---

# Command: map_tones_fast

## Arguments:

* _radius[%]>=0,_power>=0

## Description:

Apply fast tone mapping operator on selected images.

## Default values:

radius=3% and power=0.3.

```
gmic image.jpg +map_tones_fast ,
```

---

# Command: meancurvature_flow

## Arguments:

* _nb_iter>=0,_dt,_keep_sequence={ 0:No | 1:Yes }

## Description:

Apply iterations of the mean curvature flow on selected images.

## Default values:

nb_iter=10, dt=30 and keep_sequence=0.

```
gmic image.jpg +meancurvature_flow 20
```

---

# Command: median

|  |  |
| --- | --- |
|  | Built-in command |

## Arguments:

* size>=0,_threshold>0

## Description:

Apply (opt. thresholded) median filter on selected images with structuring element size x size.

```
gmic image.jpg +median 5
```

---

# Command: merge_alpha

### No argumentsDescription:Merge selected alpha detail scales into a single image. Alpha detail scales have been obtained with command [split_alpha](split_alpha.html).

---

# Command: nlmeans

## Arguments:

* [guide],_patch_radius>0,_spatial_bandwidth>0,_tonal_bandwidth>0,_patch_measure_command    or
* _patch_radius>0,_spatial_bandwidth>0,_tonal_bandwidth>0,_patch_measure_command

## Description:

Apply non local means denoising of Buades et al, 2005. on selected images.

The patch is a gaussian function of std_patch_radius.
The spatial kernel is a rectangle of radius spatial_bandwidth.
The tonal kernel is exponential (exp(-d^2/_tonal_bandwidth^2))
with d the euclidean distance between image patches.

## Default values:

patch_radius=4, spatial_bandwidth=4, tonal_bandwidth=10 and patch_measure_command=-norm.

```
gmic image.jpg +noise 10 nlmeans[-1] 4,4,{0.6*${-std_noise}}
```

---

# Command: nlmeans_core

## Arguments:

* _reference_image,_scaling_map,_patch_radius>0,_spatial_bandwidth>0

## Description:

Apply non local means denoising using a image for weight and a map for scaling

---

# Command: normalize_local

## Arguments:

* _amplitude>=0,_radius>0,_n_smooth[%]>=0,_a_smooth[%]>=0,_is_cut={ 0:No | 1:Yes },_min=0,_max=255

## Description:

Normalize selected images locally.

## Default values:

amplitude=3, radius=16, n_smooth=4%, a_smooth=2%, is_cut=1, min=0 and max=255.

```
gmic image.jpg normalize_local 8,10
```

---

# Command: normalized_cross_correlation

## Arguments:

* [mask]

## Description:

Compute normalized cross-correlation of selected images with specified mask.

```
gmic image.jpg +shift -30,-20 +normalized_cross_correlation[0] [1]
```

---

# Command: opening

## Arguments:

* size>=0    or
* size_x>=0,size_y>=0,_size_z>=0    or
* [kernel],_boundary_conditions,_is_real={ 0:Binary-mode | 1:Real-mode }

## Description:

Apply morphological opening to selected images.

boundary_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.

## Default values:

size_z=1, boundary_conditions=1 and is_real=0.

```
gmic image.jpg +opening 10
```

---

# Command: opening_circ

## Arguments:

* _size>=0,_is_real={ 0:No | 1:Yes }

## Description:

Apply circular opening of selected images by specified size.

## Default values:

boundary_conditions=1 and is_real=0.

```
gmic image.jpg +opening_circ 7
```

---

# Command: percentile

## Arguments:

* [mask],0<=_min_percentile[%]<=100,0<=_max_percentile[%]<=100.

## Description:

Apply percentile averaging filter to selected images.

## Default values:

min_percentile=0 and max_percentile=100.

```
gmic image.jpg shape_circle 11,11 +percentile[0] [1],25,75
```

---

# Command: peronamalik_flow

## Arguments:

* K_factor>0,_nb_iter>=0,_dt,_keep_sequence={ 0:No | 1:Yes }

## Description:

Apply iterations of the Perona-Malik flow on selected images.

## Default values:

K_factor=20, nb_iter=5, dt=5 and keep_sequence=0.

```
gmic image.jpg +heat_flow 20
```

---

# Command: phase_correlation

## Arguments:

* [destination]

## Description:

Estimate translation vector between selected source images and specified destination.

```
gmic image.jpg +shift -30,-20 +phase_correlation[0] [1] unroll[-1] y
```

---

# Command: pde_flow

## Arguments:

* _nb_iter>=0,_dt,_velocity_command,_keep_sequence={ 0:No | 1:Yes }

## Description:

Apply iterations of a generic PDE flow on selected images.

## Default values:

nb_iter=10, dt=30, velocity_command=laplacian and keep_sequence=0.

```
gmic image.jpg +pde_flow 20
```

---

# Command: periodize_poisson

### No argumentsDescription:Periodize selected images using a Poisson solver in Fourier space. ``` gmic image.jpg +periodize_poisson array 2,2,2 ```

---

# Command: rbf

## Arguments:

* dx,_x0,_x1,_phi(r)    or
* dx,dy,_x0,_y0,_x1,_y1,_phi(r)    or
* dx,dy,dz,x0,y0,z0,x1,y1,z1,phi(r)

## Description:

Reconstruct 1D/2D or 3D image from selected sets of keypoints, by RBF-interpolation.

A set of keypoints is represented by a vector-valued image, where each pixel represents a single keypoint.
Vector components of a keypoint have the following meaning:

For 1D reconstruction: [ x_k, f1(x_k),...fN(x_k) ].

For 2D reconstruction: [ x_k,y_k, f1(x_k,y_k),...,fN(x_k,y_k) ].

For 3D reconstruction: [ x_k,y_k,z_k, f1(x_k,y_k,z_k),...,fN(x_k,y_k,z_k) ].

Values x_k,y_k and z_k are the spatial coordinates of keypoint k.
Values f1(),..,fN() are the N components of the vector value of keypoint k.
The command reconstructs an image with specified size dx'x'dy'x'dz, with N channels.

## Default values:

x0=y0=z0=0, x1=dx-1, y1=dy-1, z1=dz-1, phi(r)=r\*log(1+r).

## Examples of use:

### • Example #1

```
gmic sample colorful,400 100%,100% noise_poissondisk. 10 1,{is},1,5 eval[-2] "begin(p=0);i?(I[#-1,p++]=[x,y,I(#0)])" to_rgb[1] mul[0,1] dilate_circ[0] 5 +rbf[-1] {0,[w,h]} c[-1] 0,255
```

### • Example #2

```
gmic 32,1,1,5,u([400,400,255,255,255]) rbf 400,400 c 0,255
```

---

# Command: red_eye

## Arguments:

* 0<=_threshold<=100,_smoothness>=0,0<=attenuation<=1

## Description:

Attenuate red-eye effect in selected images.

## Default values:

threshold=75, smoothness=3.5 and attenuation=0.1.

```
gmic image.jpg +red_eye ,
```

---

# Command: remove_hotpixels

## Arguments:

* _mask_size>0, _threshold[%]>0

## Description:

Remove hot pixels in selected images.

## Default values:

mask_size=3 and threshold=10%.

```
gmic image.jpg noise 10,2 +remove_hotpixels ,
```

---

# Command: remove_pixels

## Arguments:

* number_of_pixels[%]>=0

## Description:

Remove specified number of pixels (i.e. set them to 0) from the set of non-zero pixels in selected images.

```
gmic image.jpg +remove_pixels 50%
```

---

# Command: rolling_guidance

## Arguments:

* std_deviation_s[%]>=0,std_deviation_r[%]>=0,_precision>=0

## Description:

Apply the rolling guidance filter on selected image.

Rolling guidance filter is a fast image abstraction filter, described in:
"Rolling Guidance Filter", Qi Zhang Xiaoyong, Shen Li, Xu Jiaya Jia, ECCV'2014.

## Default values:

std_deviation_s=4, std_deviation_r=10 and precision=0.5.

```
gmic image.jpg +rolling_guidance , +-
```

---

# Command: sharpen

## Arguments:

* amplitude>=0    or
* amplitude>=0,edge>=0,_alpha[%],_sigma[%]

## Description:

Sharpen selected images by inverse diffusion or shock filters methods.

edge must be specified to enable shock-filter method.

## Default values:

edge=0, alpha=0 and sigma=0.

## Examples of use:

### • Example #1

```
gmic image.jpg sharpen 300
```

### • Example #2

```
gmic image.jpg blur 5 sharpen 300,1
```

---

# Command: sharpen_alpha

## Arguments:

* _amplitude[%]>=0,_nb_scales>0,0<=_anisotropy<=1,0<=_minimize_alpha<=1

## Description:

Sharpen selected images using a multi-scale and alpha boosting algorithm.

## Default values:

amplitude=1, nb_scales=5, anisotropy=0 and minimize_alpha=1.

---

# Command: smooth

|  |  |
| --- | --- |
|  | Built-in command |

## Arguments:

* amplitude[%]>=0,_sharpness>=0,0<=_anisotropy<=1,_alpha[%],_sigma[%],_dl>0,_da>0,_precision>0,_interpolation,_fast_approx={ 0:No | 1:Yes }    or
* nb_iterations>=0,_sharpness>=0,_anisotropy,_alpha,_sigma,_dt>0,0    or
* [tensor_field],_amplitude>=0,_dl>0,_da>0,_precision>0,_interpolation,_fast_approx={ 0:No | 1:Yes }    or
* [tensor_field],_nb_iters>=0,_dt>0,0

## Description:

Smooth selected images anisotropically using diffusion PDE's, with specified field of

diffusion tensors.
interpolation can be { 0:Nearest | 1:Linear | 2:Runge-kutta }.

## Default values:

sharpness=0.7, anisotropy=0.3, alpha=0.6, sigma=1.1, dl=0.8, da=30, precision=2, interpolation=0 and fast_approx=1.

This command has a [tutorial page](https://gmic.eu/oldtutorial/_smooth).

## Examples of use:

### • Example #1

```
gmic image.jpg repeat 3 smooth 40,0,1,1,2 done
```

### • Example #2

```
gmic image.jpg 100%,100%,1,2 rand[-1] -100,100 repeat 2 smooth[-1] 100,0.2,1,4,4 done warp[0] [-1],1,1,1
```

---

# Command: split_freq

## Arguments:

* smoothness[%]>0

## Description:

Split selected images into low and high frequency parts.

```
gmic image.jpg split_freq 2%
```

---

# Command: solve_poisson

## Arguments:

* "laplacian_command",_nb_iterations>=0,_time_step>0,_nb_scales>=0

## Description:

Solve Poisson equation so that applying laplacian[n] is close to the result of laplacian_command[n].

Solving is performed using a multi-scale gradient descent algorithm.
If nb_scales=0, the number of scales is automatically determined.

## Default values:

nb_iterations=60, dt=5 and nb_scales=0.

```
gmic image.jpg command "foo : gradient x" +solve_poisson foo +foo[0] +laplacian[1]
```

---

# Command: split_alpha

## Arguments:

* _nb_scales[%]={ 0:Auto | -S<0 | N>0 },_subsample={ 0:No | 1:Yes },0<=_anisotropy<=1,0<=_minimize_alpha<=1

## Description:

Split selected images into alpha detail scales.

If nb_scales==-S, the lowest scale has a size of at least SxS.
Parameter anisotropy is only considered when subsample=0.
Image reconstruction is done with command [merge_alpha](merge_alpha.html).

## Default values:

nb_scales=0, subsample=0, anisotropy=0 and minimize_alpha=1.

---

# Command: split_details

## Arguments:

* _nb_scales[%]={ 0:Auto | -S<0 | N>0 },_base_scale[%]>=0,_detail_scale[%]>=0

## Description:

Split selected images into nb_scales detail scales.

If base_scale = detail_scale = 0, the image decomposition is done with a trous wavelets.
Otherwise, it uses laplacian pyramids with linear standard deviations.

## Default values:

nb_scales=0, base_scale=0 and detail_scale=0.

```
gmic image.jpg split_details ,
```

---

# Command: structuretensors

## Arguments:

* _scheme={ 0:Centered | 1:Forward/backward }

## Description:

Compute the structure tensor field of selected images.

## Default values:

scheme=0.

This command has a [tutorial page](https://gmic.eu/oldtutorial/_structuretensors).

```
gmic image.jpg structuretensors abs pow 0.2
```

---

# Command: solidify

## Arguments:

* _smoothness[%]>=0,_diffusion_type={ 0:Isotropic | 1:Delaunay-guided | 2:Edge-oriented },_diffusion_iter>=0

## Description:

Solidify selected transparent images.

## Default values:

smoothness=75%, diffusion_type=1 and diffusion_iter=20.

```
gmic image.jpg 100%,100% circle[-1] 50%,50%,25%,1,255 append c +solidify , display_rgba
```

---

# Command: syntexturize

## Arguments:

* _width[%]>0,_height[%]>0

## Description:

Resynthetize width'x'height versions of selected micro-textures by phase randomization.

The texture synthesis algorithm is a straightforward implementation of the method described in :
<http://www.ipol.im/pub/art/2011/ggm_rpn/>.

## Default values:

width=height=100%.

```
gmic image.jpg crop 2,282,50,328 +syntexturize 320,320
```

---

# Command: syntexturize_matchpatch

## Arguments:

* _width[%]>0,_height[%]>0,_nb_scales>=0,_patch_size>0,_blending_size>=0,_precision>=0

## Description:

Resynthetize width'x'height versions of selected micro-textures using a patch-matching algorithm.

If nbscales==0, the number of scales used is estimated from the image size.

## Default values:

width=height=100%, nb_scales=0, patch_size=7, blending_size=5 and precision=1.

```
gmic image.jpg crop 25%,25%,75%,75% syntexturize_matchpatch 512,512
```

---

# Command: tv_flow

## Arguments:

* _nb_iter>=0,_dt,_keep_sequence={ 0:No | 1:Yes }

## Description:

Apply iterations of the total variation flow on selected images.

## Default values:

nb_iter=10, dt=30 and keep_sequence=0.

```
gmic image.jpg +tv_flow 40
```

---

# Command: unsharp

## Arguments:

* radius[%]>=0,_amount>=0,_threshold[%]>=0

## Description:

Apply unsharp mask on selected images.

## Default values:

amount=2 and threshold=0.

```
gmic image.jpg blur 3 +unsharp 1.5,15 cut 0,255
```

---

# Command: unsharp_octave

## Arguments:

* _nb_scales>0,_radius[%]>=0,_amount>=0,threshold[%]>=0

## Description:

Apply octave sharpening on selected images.

## Default values:

nb_scales=4, radius=1, amount=2 and threshold=0.

```
gmic image.jpg blur 3 +unsharp_octave 4,5,15 cut 0,255
```

---

# Command: vanvliet

|  |  |
| --- | --- |
|  | Built-in command |

## Arguments:

* std_deviation[%]>=0,order={ 0 | 1 | 2 | 3 },axis={ x | y | z | c },_boundary_conditions

## Description:

Apply Vanvliet recursive filter on selected images, along specified axis and with

specified standard deviation, order and boundary conditions.
boundary_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.

## Default values:

boundary_conditions=1.

## Examples of use:

### • Example #1

```
gmic image.jpg +vanvliet 3,1,x
```

### • Example #2

```
gmic image.jpg +vanvliet 30,0,x vanvliet[-2] 30,0,y add
```

---

# Command: voronoi

### No argumentsDescription:Compute the discrete Voronoi diagram of non-zero pixels in selected images. ``` gmic 400,400 noise 0.2,2 eq 1 +label_fg 0 voronoi[-1] +gradient[-1] xy,1 append[-2,-1] c norm[-1] ==[-1] 0 map[-2] 2,2 mul[-2,-1] normalize[-2] 0,255 dilate_circ[-2] 4 reverse max ```

---

# Command: watermark_fourier

## Arguments:

* text,_size>0

## Description:

Add a textual watermark in the frequency domain of selected images.

## Default values:

size=33.

```
gmic image.jpg +watermark_fourier "Watermarked!" +display_fft remove[-3,-1] normalize 0,255 append[-4,-2] y append[-2,-1] y
```

---

# Command: watershed

|  |  |
| --- | --- |
|  | Built-in command |

## Arguments:

* [priority_image],_is_high_connectivity={ 0:No | 1:Yes }

## Description:

Compute the watershed transform of selected images.

## Default values:

is_high_connectivity=1.

```
gmic 400,400 noise 0.2,2 eq 1 +distance 1 mul[-1] -1 label[-2] watershed[-2] [-1] mod[-2] 256 map[-2] 0 reverse
```

---

# Command: area

## Arguments:

* tolerance>=0,is_high_connectivity={ 0:No | 1:Yes }

## Description:

Compute area of connected components in selected images.

## Default values:

is_high_connectivity=0.

This command has a [tutorial page](https://gmic.eu/oldtutorial/_area).

```
gmic image.jpg luminance stencil[-1] 1 +area 0
```

---

# Command: area_fg

## Arguments:

* tolerance>=0,is_high_connectivity={ 0:No | 1:Yes }

## Description:

Compute area of connected components for non-zero values in selected images.

Similar to area except that 0-valued pixels are not considered.

## Default values:

is_high_connectivity=0.

```
gmic image.jpg luminance stencil[-1] 1 +area_fg 0
```

---

# Command: at_curve

## Arguments:

* x0[%],y0[%],z0[%],...,xN[%],yn[%],zn[%]

## Description:

Retrieve pixels of the selected images belonging to the specified cubic spline curve that passes across the specified points.

```
gmic image.jpg +at_curve 0,0,0,80%,50%,0,100%,100%,0
```

---

# Command: at_quadrangle

## Arguments:

* x0[%],y0[%],x1[%],y1[%],x2[%],y2[%],x3[%],y3[%],_interpolation,_boundary_conditions    or
* x0[%],y0[%],z0[%],x1[%],y1[%],z1[%],x2[%],y2[%],z2[%],x3[%],y3[%],z3[%],_interpolation,_boundary_conditions

## Description:

Retrieve pixels of the selected images belonging to the specified 2D or 3D quadrangle.

interpolation can be { 0:Nearest-neighbor | 1:Linear | 2:Cubic }.
boundary_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.

```
gmic image.jpg params=5%,5%,95%,5%,60%,95%,40%,95% +at_quadrangle $params polygon.. 4,$params,0.5,255
```

---

# Command: barycenter

### No argumentsDescription:Compute the barycenter vector of pixel values. ``` gmic 256,256 ellipse 50%,50%,20%,20%,0,1,1 deform 20 +barycenter +ellipse[-2] {@0,1},5,5,0,10 ```

---

# Command: betti

### No argumentsDescription:Compute Betti numbers B0,B1 and B2 from selected 3D binary shapes. Values B0,B1 and B2 are returned in the status. When multiple images are selected, the B0,B1,B2 of each image are concatenated in the status. (see https://en.wikipedia.org/wiki/Betti_number for details about Betti numbers).

---

# Command: canny

## Arguments:

* _sigma[%]>=0,_low_threshold>=0,_high_threshold>=0

## Description:

Locate image edges using Canny edge detector.

## Default values:

sigma=1, low_threshold=0.05, high_threshold=0.15.

```
gmic image.jpg canny 1
```

---

# Command: delaunay

## Arguments:

* _output_type={ 0:Image | 1:Coordinates/triangles }

## Description:

Generate discrete 2D Delaunay triangulation of non-zero pixels in selected images.

Input images must be scalar.
Each pixel of the output image is a triplet (a,b,c) meaning the pixel belongs to
the Delaunay triangle ABC where a,b,c are the labels of the pixels A,B,C.

## Examples of use:

### • Example #1

```
gmic 400,400 rand 32,255 100%,100% noise. 0.4,2 eq. 1 mul +delaunay
```

### • Example #2

```
gmic image.jpg 100%,100% noise. 2,2 eq. 1 delaunay. +blend shapeaverage0
```

---

# Command: detect_skin

## Arguments:

* 0<=tolerance<=1,_skin_x,_skin_y,_skin_radius>=0

## Description:

Detect skin in selected color images and output an appartenance probability map.

Detection is performed using CbCr chromaticity data of skin pixels.
If arguments skin_x, skin_y and skin_radius are provided, skin pixels are learnt
from the sample pixels inside the circle located at (skin_x,skin_y) with radius skin_radius.

## Default values:

tolerance=0.5 and skin_x=skiny=radius=-1.

---

# Command: displacement

|  |  |
| --- | --- |
|  | Built-in command |

## Arguments:

* [reference],_smoothness>=0,_precision>=0,_nb_scales>=0,_iteration_max>=0,mode={ 0:Backward | 1:Forward },_[guide]

## Description:

Estimate displacement field between specified reference image and selected (target) images.

If smoothness>=0, regularization type is set to isotropic, else to anisotropic.
If nbscales==0, the number of scales used is estimated from the image size.

## Default values:

smoothness=0.1, precision=7, nb_scales=0, iteration_max=1000, mode=0 and [guide]=(unused).

```
gmic image.jpg +rotate 3,1,0,50%,50% +displacement[-1] [-2] quiver[-1] [-1],15,1,1,1,{1.5*iM}
```

---

# Command: distance

|  |  |
| --- | --- |
|  | Built-in command |

## Arguments:

* isovalue[%],_metric    or
* isovalue[%],[metric],_method

## Description:

Compute the unsigned distance function to specified isovalue, opt. according to a custom metric.

metric can be { 0:Chebyshev | 1:Manhattan | 2:Euclidean | 3:Squared-euclidean }.
method can be { 0:Fast-marching | 1:Low-connectivity dijkstra | 2:High-connectivity dijkstra | 3:1+Return path | 4:2+Return path }.

## Default values:

metric=2 and method=0.

This command has a [tutorial page](https://gmic.eu/oldtutorial/_distance).

## Examples of use:

### • Example #1

```
gmic image.jpg threshold 20% distance 0 pow 0.3
```

### • Example #2

```
gmic 400,400 set 1,50%,50% +distance[0] 1,2 +distance[0] 1,1 distance[0] 1,0 mod 32 threshold 16 append c
```

---

# Command: edgels

## Arguments:

* x0,y0,_n0,_is_high_connectivity={ 0:No | 1:Yes }

## Description:

Extract one or several lists of edgels (and their normals) that defines a 2D binary silhouette.

When specified (i.e. !=-1), arguments x0,y0,n0 are the coordinates of the starting edgel, which must be located on an edge of the binary silhouette.

If x0,y0 and n0 are specified, only a single list of edgels is returned.

If only x0,y0 are specified (meaning n0=-1), up to 4 lists of edgels can be returned, all starting from the same point (x0,y0).

If no arguments are specified (meaning x0=y0=n0=-1), all possible lists of edgels are returned.

A list of edgels is returned as an image with 3 channels [x,y,n] where x and y are the 2D coordinates of the edgel pixel, and n is the orientation of its associated canonical normal (which can be { 0:[1,0] | 1:[0,1] | 2:[-1,0] | 3:[0,-1] }.

## Default values:

x0=y0=n0=-1 and is_high_connectivity=1.

---

# Command: edges

## Arguments:

* _threshold[%]>=0

## Description:

Estimate contours of selected images.

## Default values:

edges=15%

```
gmic image.jpg +edges 15%
```

---

# Command: fftpolar

### No argumentsDescription:Compute fourier transform of selected images, as centered magnitude/phase images. ``` gmic image.jpg fftpolar ellipse 50%,50%,10,10,0,1,0 ifftpolar ```

---

# Command: histogram

|  |  |
| --- | --- |
|  | Built-in command |

## Arguments:

* nb_levels[%]>0,_min_value[%],_max_value[%]

## Description:

Compute the histogram of selected images.

If value range is set, the histogram is estimated only for pixels in the specified
value range. Argument max_value must be specified if min_value is set.

## Default values:

min_value=0% and max_value=100%.

```
gmic image.jpg +histogram 64 display_graph[-1] 400,300,3
```

---

# Command: histogram_masked

## Arguments:

* [mask],nb_levels[%]>0,_min_value[%],_max_value[%]

## Description:

Compute the masked histogram of selected images.

## Default values:

min_value=0% and max_value=100%.

---

# Command: histogram_nd

## Arguments:

* nb_levels[%]>0,_value0[%],_value1[%]

## Description:

Compute the 1D,2D or 3D histogram of selected multi-channels images (having 1,2 or 3 channels).

If value range is set, the histogram is estimated only for pixels in the specified
value range.

## Default values:

value0=0% and value1=100%.

```
gmic image.jpg channels 0,1 +histogram_nd 256
```

---

# Command: histogram_cumul

## Arguments:

* _nb_levels>0,_is_normalized={ 0:No | 1:Yes },_val0[%],_val1[%]

## Description:

Compute cumulative histogram of selected images.

## Default values:

nb_levels=256, is_normalized=0, val0=0% and val1=100%.

```
gmic image.jpg +histogram_cumul 256 histogram[0] 256 display_graph 400,300,3
```

---

# Command: histogram_pointwise

## Arguments:

* nb_levels[%]>0,_value0[%],_value1[%]

## Description:

Compute the histogram of each vector-valued point of selected images.

If value range is set, the histogram is estimated only for values in the specified
value range.

## Default values:

value0=0% and value1=100%.

---

# Command: hough

## Arguments:

* _width>0,_height>0,gradient_norm_voting={ 0:No | 1:Yes }

## Description:

Compute hough transform (theta,rho) of selected images.

## Default values:

width=512, height=width and gradient_norm_voting=1.

```
gmic image.jpg +blur 1.5 hough[-1] 400,400 blur[-1] 0.5 add[-1] 1 log[-1]
```

---

# Command: huffman_tree

### No argumentsDescription:Generate Huffman coding tree from the statistics of all selected images. Huffman tree is returned as a 1xN image inserted at the end of the image list, representing the N vector-valued leafs/nodes of the tree, encoded as [ value,parent,child0,child1 ]. Last row of the returned image corresponds to the tree root. Selected images must contain only positive integer values. Return maximal value of the input data in the status. See also:[compress_huffman](compress_huffman.html), [decompress_huffman](decompress_huffman.html).

---

# Command: ifftpolar

### No argumentsDescription:Compute inverse fourier transform of selected images, from centered magnitude/phase images.

---

# Command: img2patches

## Arguments:

* patch_size>0,_overlap[%]>0,_boundary_conditions

## Description:

Decompose selected 2D images into (possibly overlapping) patches and stack them along the z-axis.

overlap must be in range [0,patch_size-1].
boundary_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.

## Default values:

overlap=0 and boundary_conditions=0.

## See also:

[patches2img](patches2img.html).

```
gmic image.jpg img2patches 64
```

---

# Command: isophotes

## Arguments:

* _nb_levels>0

## Description:

Render isophotes of selected images on a transparent background.

## Default values:

nb_levels=64

```
gmic image.jpg blur 2 isophotes 6 dilate_circ 5 display_rgba
```

---

# Command: label

|  |  |
| --- | --- |
|  | Built-in command |

## Arguments:

* _tolerance>=0,is_high_connectivity={ 0:No | 1:Yes },_is_L2_norm={ 0:No | 1:Yes }

## Description:

Label connected components in selected images.

If is_L2_norm=1, tolerances are compared against L2-norm, otherwise L1-norm is used.

## Default values:

tolerance=0, is_high_connectivity=0 and is_L2_norm=1.

This command has a [tutorial page](https://gmic.eu/oldtutorial/_label).

## Examples of use:

### • Example #1

```
gmic image.jpg luminance threshold 60% label normalize 0,255 map 0
```

### • Example #2

```
gmic 400,400 set 1,50%,50% distance 1 mod 16 threshold 8 label mod 255 map 2
```

---

# Command: label_fg

## Arguments:

* tolerance>=0,is_high_connectivity={ 0:No | 1:Yes },_is_L2_norm={ 0:No | 1:Yes }

## Description:

Label connected components for non-zero values (foreground) in selected images.

Similar to label except that 0-valued pixels are not labeled.
If is_L2_norm=1, tolerances are compared against L2-norm, otherwise L1-norm is used.

## Default values:

is_high_connectivity=0.

---

# Command: laar

### No argumentsDescription:Extract the largest axis-aligned rectangle in non-zero areas of selected images. Rectangle coordinates are returned in status, as a sequence of numbers x0,y0,x1,y1. ``` gmic shape_cupid 256 coords=${-laar} normalize 0,255 to_rgb rectangle $coords,0.5,0,128,0 ```

---

# Command: max_patch

## Arguments:

* _patch_size>=1

## Description:

Return locations of maximal values in local patch-based neighborhood of given size for selected images.

## Default values:

patch_size=16.

```
gmic image.jpg norm +max_patch 16
```

---

# Command: min_patch

## Arguments:

* _patch_size>=1

## Description:

Return locations of minimal values in local patch-based neighborhood of given size for selected images.

## Default values:

patch_size=16.

```
gmic image.jpg norm +min_patch 16
```

---

# Command: minimal_path

## Arguments:

* x0[%]>=0,y0[%]>=0,z0[%]>=0,x1[%]>=0,y1[%]>=0,z1[%]>=0,_is_high_connectivity={ 0:No | 1:Yes }

## Description:

Compute minimal path between two points on selected potential maps.

## Default values:

is_high_connectivity=0.

```
gmic image.jpg +gradient_norm fill[-1] 1/(1+i) minimal_path[-1] 0,0,0,100%,100%,0 pointcloud[-1] 0 *[-1] 280 to_rgb[-1] ri[-1] [-2],0 or
```

---

# Command: mse

## Arguments:

* [reference]

## Description:

Return the MSE (Mean-Squared Error) between selected images and specified reference image.

This command does not modify the images. It returns a value or a list of values in the status.

---

# Command: mse_matrix

### No argumentsDescription:Compute MSE (Mean-Squared Error) matrix between selected images. ``` gmic image.jpg +noise 30 +noise[0] 35 +noise[0] 38 cut. 0,255 +mse_matrix ```

---

# Command: patches2img

## Arguments:

* width>0,height>0,_overlap[%]>0,_overlap_std[%]

## Description:

Recompose 2D images from their selected patch representations.

overlap must be in range [0,patch_size-1] where patch_size is the width/height of the selected image.
overlap_std is the standard deviation of the gaussian weights used for reconstructing overlapping patches.
If overlap_std is set to -1, uniform weights are used rather than gaussian.

## Default values:

overlap=0 and overlap_std=-1.

## See also:

[img2patches](img2patches.html).

```
gmic image.jpg +img2patches 32,0,3 mirror[-1] xy patches2img[-1] {0,[w,h]}
```

---

# Command: patches

## Arguments:

* patch_width>0,patch_height>0,patch_depth>0,x0,y0,z0,_x1,_y1,_z1,...,_xN,_yN,_zN

## Description:

Extract N+1 patches from selected images, centered at specified locations.

```
gmic image.jpg +patches 64,64,1,153,124,0,184,240,0,217,126,0,275,38,0
```

---

# Command: pca

## Arguments:

* _output_mode,_target_dim[%]>0,_normalization_mode={ 0:None | 1:Center | 2:Center+scale }

## Description:

Perform PCA (Principal Component Analysis) on selected images, viewed as sets of vector-valued samples Xk.

Bits of output_mode selects what output data are returned on the image stack:

1: Output image of vector-valued samples Yk = Mt\*(Xk - avg)/std, that are the projections of the Xk in a vector sub-space of (lower) dimension target_dim. avg is the average vector of all Xk (or zero vector if normalization_mode==0). std is the standard deviation vector of all Xk (or all-ones vector if normalization_mode<2). Mt is the transpose of M, the matrix of the target_dim first eigenvectors (arranged by columns) of the covariance matrix of the Xk.

2: Output vector avg: average of the Xk.

4: Output vector std: standard deviations of the Xk.

8: Output matrix M: projection matrix (orthonormal).

Knowing avg, std and M makes it possible to (approximately) retro-project the Yk in the initial vector space, by computing Xk = avg + std\*M\*Yk for each image pixel.

## Default values:

output_mode=15, target_dim=100% and normalization_mode=1.

```
gmic shape_dragonfly 400 mul 128 0 eval.. "i?da_push([x,y])" da_freeze. pca. 11,2 eval "C = I[#-2,0]; M = transpose(crop(#-1),2); repeat(2,k,polygon(#0,-2,C-1000*M[2*k,2],C+1000*M[2*k,2],1,0xF0F0F0F0,180)); ellipse(#0,C,5,5,0,1,255)" k[0]
```

---

# Command: matchpatch

|  |  |
| --- | --- |
|  | Built-in command |

## Arguments:

* [patch_image],patch_width>=1,_patch_height>=1,_patch_depth>=1,_nb_iterations>=0,_nb_randoms>=0,_occurence_penalization,_output_score={ 0:No | 1:Yes },_[guide]

## Description:

Estimate correspondence map between selected images and specified patch image, using

a patch-matching algorithm.
Each pixel of the returned correspondence map gives the location (p,q) of the closest patch in
the specified patch image. If output_score=1, the third channel also gives the corresponding
matching score for each patch as well.
If patch_penalization is >=0, SSD is penalized with patch occurrences.
If patch_penalization is <0, SSD is inf-penalized when distance between patches are less than -patch_penalization.

## Default values:

patch_height=patch_width, patch_depth=1, nb_iterations=5, nb_randoms=5, occurence_penalization=0, output_score=0 and guide=(undefined).

```
gmic image.jpg sample colorful +matchpatch[0] [1],3 +warp[-2] [-1],0
```

---

# Command: matchpatch_alt

## Arguments:

* [patch_image],_patch_width>=1,_patch_height>=1,_patch_depth>=1,_nb_iterations>=0,_nb_randoms>=0,_occurrence_penalization>=0,_output_score={ 0:No | 1:Yes },_[guide]

## Description:

Implementation of the [matchpatch](matchpatch.html) command as an alternative custom command (slower).

## Default values:

patch_height=patch_width, patch_depth=1, nb_iterations=5, nb_randoms=5, occurrence_penalization=0, output_score=0 and guide=(undefined).

```
gmic image.jpg sample colorful +matchpatch_alt[0] [1],3 +warp[-2] [-1],0
```

---

# Command: plot2value

### No argumentsDescription:Retrieve values from selected 2D graph plots. ``` gmic 400,300,1,1,'y>300*abs(cos(x/10+2*u))' +plot2value +display_graph[-1] 400,300 ```

---

# Command: pointcloud

## Arguments:

* _type = { -X:-X-opacity | 0:Binary | 1:Cumulative | 2:Label | 3:Retrieve coordinates },_width,_height>0,_depth>0

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

type=0 and max_width=max_height=max_depth=0.

## Examples of use:

### • Example #1

```
gmic 3000,2 rand 0,400 +pointcloud 0 dilate[-1] 3
```

### • Example #2

```
gmic 3000,2 rand 0,400 {w} {w},3 rand[-1] 0,255 append y +pointcloud 0 dilate[-1] 3
```

---

# Command: psnr

## Arguments:

* [reference],_max_value>0

## Description:

Return PSNR (Peak Signal-to-Noise Ratio) between selected images and specified reference image.

This command does not modify the images. It returns a value or a list of values in the status.

## Default values:

max_value=255.

---

# Command: psnr_matrix

## Arguments:

* _max_value>0

## Description:

Compute PSNR (Peak Signal-to-Noise Ratio) matrix between selected images.

## Default values:

max_value=255.

```
gmic image.jpg +noise 30 +noise[0] 35 +noise[0] 38 cut. 0,255 +psnr_matrix
```

---

# Command: segment_watershed

## Arguments:

* _threshold>=0

## Description:

Apply watershed segmentation on selected images.

## Default values:

threshold=2.

```
gmic image.jpg segment_watershed 2
```

---

# Command: shape2bump

## Arguments:

* _resolution>=0,0<=_weight_std_max_avg<=1,_dilation,_smoothness>=0

## Description:

Estimate bumpmap from binary shape in selected images.

## Default values:

resolution=256, weight_std_max=0.75, dilation=0 and smoothness=100.

---

# Command: skeleton

## Arguments:

* _boundary_conditions={ 0:Dirichlet | 1:Neumann }

## Description:

Compute skeleton of binary shapes using distance transform and constrained thinning.

## Default values:

boundary_conditions=1.

```
gmic shape_cupid 320 +skeleton 0
```

---

# Command: slic

## Arguments:

* size>0,_regularity>=0,_nb_iterations>0

## Description:

Segment selected 2D images with superpixels, using the SLIC algorithm (Simple Linear Iterative Clustering).

Scalar images of increasingly labeled pixels are returned.
Reference paper: Achanta, R., Shaji, A., Smith, K., Lucchi, A., Fua, P., & Susstrunk, S. (2010). SLIC Superpixels (No. EPFL-REPORT-149300).

## Default values:

size=16, regularity=10 and nb_iterations=10.

```
gmic image.jpg +srgb2lab slic[-1] 16 +blend shapeaverage f[-2] "j(1,0)==i && j(0,1)==i" *[-1] [-2]
```

---

# Command: ssd_patch

## Arguments:

* [patch],_use_fourier={ 0:No | 1:Yes },_boundary_conditions

## Description:

Compute fields of SSD between selected images and specified patch.

Argument boundary_conditions is valid only when use_fourier=0.
boundary_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.

## Default values:

use_fourier=0 and boundary_conditions=0.

```
gmic image.jpg +crop 20%,20%,35%,35% +ssd_patch[0] [1],0,0
```

---

# Command: ssim

## Arguments:

* [reference],_patch_size>0,_max_value>0

## Description:

Compute the Structural Similarity Index Measure (SSIM) between selected images and specified reference image.

This command does not modify the images, it just returns a value or a list of values in the status.
When downsampling_factor is specified with a ending %, its value is equal to 1+(patch_size-1)\*spatial_factor%.

SSIM is a measure introduced int the following paper:
Wang, Zhou, et al., "Image quality assessment: from error visibility to structural similarity.",
in IEEE transactions on image processing 13.4 (2004): 600-612.

The implementation of this command is a direct translation of the reference code (in Matlab), found at :
https://ece.uwaterloo.ca/~z70wang/research/ssim/

## Default values:

patch_size=11, and max_value=255.

---

# Command: ssim_matrix

## Arguments:

* _patch_size>0,_max_value>0

## Description:

Compute SSIM (Structural Similarity Index Measure) matrix between selected images.

## Default values:

patch_size=11, and max_value=255.

```
gmic image.jpg +noise 30 +noise[0] 35 +noise[0] 38 cut. 0,255 +ssim_matrix
```

---

# Command: thinning

## Arguments:

* _boundary_conditions={ 0:Dirichlet | 1:Neumann }

## Description:

Compute skeleton of binary shapes using morphological thinning

(beware, this is a quite slow iterative process)

## Default values:

boundary_conditions=1.

```
gmic shape_cupid 320 +thinning
```

---

# Command: tones

## Arguments:

* N>0

## Description:

Get N tones masks from selected images.

```
gmic image.jpg +tones 3
```

---

# Command: topographic_map

## Arguments:

* _nb_levels>0,_smoothness

## Description:

Render selected images as topographic maps.

## Default values:

nb_levels=16 and smoothness=2.

```
gmic image.jpg topographic_map 10
```

---

# Command: tsp

## Arguments:

* _precision>=0

## Description:

Try to solve the travelling salesman problem, using a combination of greedy search and 2-opt algorithms.

Selected images must have dimensions Nx1x1xC to represent N cities each with C-dimensional coordinates.
This command re-order the selected data along the x-axis so that the point sequence becomes a shortest path.

## Default values:

precision=256.

```
gmic 256,1,1,2 rand 0,512 tsp , 512,512,1,3 repeat w#0 circle[-1] {0,I[$>]},2,1,255,255,255 line[-1] {0,boundary=2;[I[$>],I[$>+1]]},1,255,128,0 done keep[-1]
```

---

# Command: variance_patch

## Arguments:

* _patch_size>=1

## Description:

Compute variance of each images patch centered at (x,y), in selected images.

## Default values:

patch_size=16

```
gmic image.jpg +variance_patch
```

---

# Command: arrow

## Arguments:

* x0[%],y0[%],x1[%],y1[%],_thickness[%]>=0,_head_length[%]>=0,_head_thickness[%]>=0,_opacity,_pattern,_color1,...

## Description:

Draw specified arrow on selected images.

pattern is an hexadecimal number starting with 0x which can be omitted
even if a color is specified. If a pattern is specified, the arrow is
drawn outlined instead of filled.

## Default values:

thickness=1%, head_length=10%, head_thickness=3%, opacity=1, pattern=(undefined) and color1=0.

```
gmic 400,400,1,3 repeat 100 arrow 50%,50%,{u(100)}%,{u(100)}%,3,20,10,0.3,${-rgb} done
```

---

# Command: axes

## Arguments:

* x0,x1,y0,y1,_font_height>=0,_opacity,_pattern,_color1,...

## Description:

Draw xy-axes on selected images.

pattern is an hexadecimal number starting with 0x which can be omitted
even if a color is specified.
To draw only one x-axis at row Y, set both y0 and y1 to Y.
To draw only one y-axis at column X, set both x0 and x1 to X.

## Default values:

font_height=14, opacity=1, pattern=(undefined) and color1=0.

```
gmic 400,400,1,3,255 axes -1,1,1,-1
```

---

# Command: ball

## Arguments:

* _size>0,_R,_G,_B,_ambient>=0,_diffuse>=0,_specular>=0,_shininess>=0,_light_x,_light_y,_light_z

## Description:

Input a 2D RGBA colored ball sprite, rendered using the Phong illumination model.

## Default values:

size=64, R=200, G=R, B=R, ambient=0.25, diffuse=1, specular=1, shininess=20, light_x=1.5, light_y=-1.5 and light_z=1.

```
gmic repeat 9 { ball {int(1.5^($>+4))},${-rgb} } append_tiles 3,3
```

---

# Command: chessboard

## Arguments:

* size1>0,_size2>0,_offset1,_offset2,_angle,_opacity,_color1,...,_color2,...

## Description:

Draw chessboard on selected images.

## Default values:

size2=size1, offset1=offset2=0, angle=0, opacity=1, color1=0 and color2=255.

```
gmic image.jpg chessboard 32,32,0,0,25,0.3,255,128,0,0,128,255
```

---

# Command: cie1931

### No argumentsDescription:Draw CIE-1931 chromaticity diagram on selected images. ``` gmic 500,400,1,3 cie1931 ```

---

# Command: circle

## Arguments:

* x[%],y[%],R[%],_opacity,_pattern,_color1,...

## Description:

Draw specified colored circle on selected images.

A radius of 100% stands for sqrt(width^2+height^2).
pattern is an hexadecimal number starting with 0x which can be omitted
even if a color is specified. If a pattern is specified, the circle is
drawn outlined instead of filled.

## Default values:

opacity=1, pattern=(undefined) and color1=0.

```
gmic image.jpg repeat 300 circle {u(100)}%,{u(100)}%,{u(30)},0.3,${-rgb} done circle 50%,50%,100,0.7,255
```

---

# Command: close_binary

## Arguments:

* 0<=_endpoint_rate<=100,_endpoint_connectivity>=0,_spline_distmax>=0,_segment_distmax>=0,0<=_spline_anglemax<=180,_spline_roundness>=0,_area_min>=0,_allow_self_intersection={ 0:No | 1:Yes }

## Description:

Automatically close open shapes in binary images (defining white strokes on black background).

## Default values:

endpoint_rate=75, endpoint_connectivity=2, spline_distmax=80, segment_distmax=20, spline_anglemax=90, spline_roundness=1,area_min=100, allow_self_intersection=1.

---

# Command: curve

## Arguments:

* [xy_coordinates],_thickness>0,_tilt,_tilt_strength[%],_is_closed={ 0:No | 1:Yes },_opacity,_color1,...

## Description:

Draw specified parameterized curve on selected images.

Arguments are:

[xy_coordinates] is the set of XY-coordinates of the curve, specified as a 2-channels image.

thickness is the thickness of the drawing, specified in pixels.

tilt is an angle, specified in degrees.

tilt_strength must be a float value in [0,1] (or in [0,100] if specified as a percentage).

is_closed is a boolean which tells if the curve is closed or not.

## Default values:

thickness=0, tilt=45

```
gmic image.jpg srand 3 16,1,1,4,u s. c,2 rbf[-2,-1] 1000,0,1 n[-2] 10,{w#0-10} n[-1] 10,{h#0-10} a[-2,-1] c curve[-2] [-1],6,0,0,0,1,0,128,0
```

---

# Command: ellipse

|  |  |
| --- | --- |
|  | Built-in command |

## Arguments:

* x[%],y[%],R[%],r[%],_angle,_opacity,_pattern,_color1,...

## Description:

Draw specified colored ellipse on selected images.

A radius of 100% stands for sqrt(width^2+height^2).
pattern is an hexadecimal number starting with 0x which can be omitted
even if a color is specified. If a pattern is specified, the ellipse is
drawn outlined instead of filled.

## Default values:

opacity=1, pattern=(undefined) and color1=0.

```
gmic image.jpg repeat 300 ellipse {u(100)}%,{u(100)}%,{u(30)},{u(30)},{u(180)},0.3,${-rgb} done ellipse 50%,50%,100,100,0,0.7,255
```

---

# Command: flood

|  |  |
| --- | --- |
|  | Built-in command |

## Arguments:

* x[%],_y[%],_z[%],_tolerance>=0,_is_high_connectivity={ 0:No | 1:Yes },_opacity,_color1,...

## Description:

Flood-fill selected images using specified value and tolerance.

## Default values:

y=z=0, tolerance=0, is_high_connectivity=0, opacity=1 and color1=0.

```
gmic image.jpg repeat 1000 flood {u(100)}%,{u(100)}%,0,20,0,1,${-rgb} done
```

---

# Command: gaussian

## Arguments:

* _sigma1[%],_sigma2[%],_angle

## Description:

Draw a centered gaussian on selected images, with specified standard deviations and orientation.

## Default values:

sigma1=3, sigma2=sigma1 and angle=0.

This command has a [tutorial page](https://gmic.eu/oldtutorial/_gaussian).

```
gmic 400,400 gaussian 100,30,45
```

---

# Command: graph

## Arguments:

* [function_image],_plot_type,_vertex_type,_ytop,_ybottom,_opacity,_pattern,_color1,...

## Description:

Draw specified function graph on selected images.

plot_type can be { 0:None | 1:Lines | 2:Splines | 3:Bar }.
vertex_type can be { 0:None | 1:Points | 2,3:Crosses | 4,5:Circles | 6,7:Squares }.
pattern is an hexadecimal number starting with 0x which can be omitted
even if a color is specified.

## Default values:

plot_type=1, vertex_type=1, ytop=ybottom=0 (auto), opacity=1, pattern=(undefined)

and color1=0.

```
gmic image.jpg +rows 50% blur[-1] 3 split[-1] c div[0] 1.5 graph[0] [1],2,0,0,0,1,255,0,0 graph[0] [2],2,0,0,0,1,0,255,0 graph[0] [3],2,0,0,0,1,0,0,255 keep[0]
```

---

# Command: grid

## Arguments:

* size_x[%]>=0,size_y[%]>=0,_offset_x[%],_offset_y[%],_opacity,_pattern,_color1,...

## Description:

Draw xy-grid on selected images.

pattern is an hexadecimal number starting with 0x which can be omitted
even if a color is specified.

## Default values:

offset_x=offset_y=0, opacity=1, pattern=(undefined) and color1=0.

## Examples of use:

### • Example #1

```
gmic image.jpg grid 10%,10%,0,0,0.5,255
```

### • Example #2

```
gmic 400,400,1,3,255 grid 10%,10%,0,0,0.3,0xCCCCCCCC,128,32,16
```

---

# Command: image

|  |  |
| --- | --- |
|  | Built-in command |

## Arguments:

* [sprite],_x[%|~],_y[%|~],_z[%|~],_c[%|~],_opacity,_[opacity_mask],_max_opacity_mask

## Description:

Draw specified sprite on selected images.

(*equivalent to shortcut command* j).

If one of the x,y,z or c argument ends with a ~, its value is expected to be
a centering ratio (in [0,1]) rather than a position.
Usual centering ratio are { 0:left-justified | 0.5:centered | 1:right-justified }.

## Default values:

x=y=z=c=0, opacity=1, opacity_mask=(undefined) and max_opacity_mask=1.

```
gmic image.jpg +crop 40%,40%,60%,60% resize[-1] 200%,200%,1,3,5 frame[-1] xy,2,0 image[0] [-1],30%,30% keep[0]
```

---

# Command: imagealpha

## Arguments:

* [sprite],_x[%|~],_y[%|~],_z[%|~],_c[%|~],_opacity

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

|  |  |
| --- | --- |
|  | Built-in command |

## Arguments:

* x0[%],y0[%],x1[%],y1[%],_opacity,_pattern,_color1,...

## Description:

Draw specified colored line on selected images.

pattern is an hexadecimal number starting with 0x which can be omitted
even if a color is specified.

## Default values:

opacity=1, pattern=(undefined) and color1=0.

```
gmic image.jpg repeat 500 line 50%,50%,{u(w)},{u(h)},0.5,${-rgb} done line 0,0,100%,100%,1,0xCCCCCCCC,255 line 100%,0,0,100%,1,0xCCCCCCCC,255
```

---

# Command: line_aa

## Arguments:

* x0[%],y0[%],x1[%],y1[%],_opacity,_color1,...

## Description:

Draw specified antialiased colored line on selected images.

## Default values:

opacity=1 and color1=0.

```
gmic 512,512,1,3 repeat 100 line_aa {v([w,h,w,h])-1},1,${-rgb} done
```

---

# Command: spline

## Arguments:

* x0[%],y0[%],u0[%],v0[%],x1[%],y1[%],u1[%],v1[%],_opacity,_color1,...

## Description:

Draw specified colored spline curve on selected images (cubic hermite spline).

## Default values:

opacity=1 and color1=0.

```
gmic image.jpg repeat 30 { spline {u(100)}%,{u(100)}%,{u(-600,600)},{u(-600,600)},{u(100)}%,{u(100)}%,{u(-600,600)},{u(-600,600)},1,${-rgb} }
```

---

# Command: thickcircle

## Arguments:

* x[%],y[%],R[%],_thickness>=0,_opacity,_color1,...

## Description:

Draw specified colored thick outlined circle on selected images.

## Default values:

thickness=3, opacity=1 and color1=0.

```
gmic 400,400 repeat 15 { R:=lerp(10,190,$%) thickcircle 200,200,$R,2,1,$R } n 0,255 map 7
```

---

# Command: thickellipse

## Arguments:

* x[%],y[%],R[%],r[%],_angle,_thickness>=0,_opacity,_color1,...

## Description:

Draw specified colored thick outlined ellipse on selected images.

## Default values:

thickness=3, opacity=1 and color1=0.

```
gmic image.jpg repeat 300 thickellipse {u(100)}%,{u(100)}%,{u(50)},{u(50)},{u(180)},3,0.6,${-rgb} done thickellipse 50%,50%,200,100,0,5,0.7,255
```

---

# Command: thickline

## Arguments:

* x0[%],y0[%],x1[%],y1[%],_thickness,_opacity,_color1

## Description:

Draw specified colored thick line on selected images.

## Default values:

thickness=2, opacity=1 and color1=0.

```
gmic 400,400,1,3 repeat 100 thickline {u([w,h,w,h,5])},0.5,${-rgb} done
```

---

# Command: thickpolygon

## Arguments:

* N>=1,x1[%],y1[%],...,xN[%],yN[%],_thickness>=0,_opacity,_color1,...    or
* [coords],_thickness>=0,_opacity,_color1,...

## Description:

Draw specified colored thick outlined N-vertices polygon on selected images.

If thickness<0, the command draws an open polygon rather than a closed polygon.

## Default values:

thickness=3, opacity=1, and color1=0.

## Examples of use:

### • Example #1

```
gmic image.jpg thickpolygon 4,20%,20%,80%,30%,80%,70%,20%,80%,5,1,0,255,0
```

### • Example #2

```
gmic image.jpg 2,16,1,1,'u(x?h#0:w#0)' thickpolygon[-2] [-1],5,1,255,0,255 remove[-1]
```

---

# Command: thickspline

## Arguments:

* x0[%],y0[%],u0[%],v0[%],x1[%],y1[%],u1[%],v1[%],_thickness,_opacity,_color1,...

## Description:

Draw specified colored thick spline curve on selected images (cubic hermite spline).

## Default values:

thickness=3, opacity=1 and color1=0.

```
gmic image.jpg repeat 30 { thickspline {u(100)}%,{u(100)}%,{u(-600,600)},{u(-600,600)},{u(100)}%,{u(100)}%,{u(-600,600)},{u(-600,600)},3,1,${-rgb} }
```

---

# Command: mandelbrot

## Arguments:

* z0r,z0i,z1r,z1i,_iteration_max>=0,_is_julia={ 0:No | 1:Yes },_c0r,_c0i,_opacity

## Description:

Draw mandelbrot/julia fractal on selected images.

## Default values:

iteration_max=100, is_julia=0, c0r=c0i=0 and opacity=1.

```
gmic 400,400 mandelbrot -2.5,-2,2,2,1024 map 0 +blur 2 elevation3d[-1] -0.2
```

---

# Command: marble

## Arguments:

* _image_weight,_pattern_weight,_angle,_amplitude,_sharpness>=0,_anisotropy>=0,_alpha,_sigma,_cut_low>=0,_cut_high>=0

## Description:

Render marble like pattern on selected images.

## Default values:

image_weight=0.2, pattern_weight=0.1, angle=45, amplitude=0, sharpness=0.4 and anisotropy=0.8,

alpha=0.6, sigma=1.1 and cut_low=cut_high=0.

```
gmic image.jpg +marble ,
```

---

# Command: maze

## Arguments:

* _width>0,_height>0,_cell_size>0

## Description:

Input maze with specified size.

```
gmic maze 30,20 negate normalize 0,255
```

---

# Command: maze_mask

## Arguments:

* _cellsize>0

## Description:

Input maze according to size and shape of selected mask images.

Mask may contain disconnected shapes.

```
gmic 0 text "G'MIC",0,0,53,1,1 dilate 3 autocrop 0 frame xy,1,0 maze_mask 8 dilate 3 negate mul 255
```

---

# Command: newton_fractal

## Arguments:

* z0r,z0i,z1r,z1i,_angle,0<=_descent_method<=2,_iteration_max>=0,_convergence_precision>0,_expr_p(z),_expr_dp(z),_expr_d2p(z)

## Description:

Draw newton fractal on selected images, for complex numbers in range (z0r,z0i) - (z1r,z1i).

Resulting images have 3 channels whose meaning is [ last_zr, last_zi, nb_iter_used_for_convergence ].
descent_method can be { 0:Secant | 1:Newton | 2:Householder }.

## Default values:

angle=0, descent_method=1, iteration_max=200, convergence_precision=0.01, expr_p(z)=z^^3-1, expr_dp(z)=3\*z^^2 and expr_d2z(z)=6\*z.

```
gmic 400,400 newton_fractal -1.5,-1.5,1.5,1.5,0,2,200,0.01,"z^^6 + z^^3 - 1","6*z^^5 + 3*z^^2","30*z^^4 + 6*z" f "[ atan2(i1,i0)*90+20,1,cut(i2/30,0.2,0.7) ]" hsl2rgb
```

---

# Command: pack_sprites

## Arguments:

* [sprite_set],_nb_scales>=1,0<_min_scale<=100,_allow_rotation={ 0:None | 1:180 deg. | 2:90 deg. | 3:Any },_spacing,_max_attempts>0

## Description:

Try to randomly pack as many sprites as possible onto the empty areas of an image.

Sprites can be eventually rotated and scaled during the packing process.
Selected image is the canvas that will be filled with the sprites.
The zero values of its alpha channel defines the potential locations for drawing the sprites.
[sprite_set] defines the set of sprites considered for filling the canvas.
The zero values of their alpha channels defines the sprite shape.
Sprite packing is done on random locations and iteratively with decreasing scales.
nb_scales sets the number of decreasing scales considered for all specified sprites to be packed.
min_scale (in %) sets the minimal size considered for packing (specified as a percentage of the
original sprite size).
spacing can be positive or negative.
max_attempts defines the maximum number of attempts to pack a sprite for each scale.

## Default values:

nb_scales=1, min_scale=25, allow_rotation=0, spacing=1 and max_attempts=512.

```
gmic shape_heart 512 negate normalize 0,255 channels -3,0 repeat 2 { ball 48,${-rgb} } +pack_sprites[0] [^0],5,15
```

---

# Command: piechart

## Arguments:

* label_height>=0,label_R,label_G,label_B,"label1",value1,R1,G1,B1,...,"labelN",valueN,RN,GN,BN

## Description:

Draw pie chart on selected (RGB) images.

```
gmic image.jpg piechart 25,0,0,0,"Red",55,255,0,0,"Green",40,0,255,0,"Blue",30,128,128,255,"Other",5,128,128,128
```

---

# Command: plasma

## Arguments:

* _alpha,_beta,_scale>=0

## Description:

Draw a random colored plasma fractal on selected images.

This command implements the so-called Diamond-Square algorithm.

## Default values:

alpha=1, beta=1 and scale=8.

This command has a [tutorial page](https://gmic.eu/oldtutorial/_plasma).

```
gmic 400,400,1,3 plasma 1
```

---

# Command: point

|  |  |
| --- | --- |
|  | Built-in command |

## Arguments:

* x[%],_y[%],_z[%],_opacity,_color1,...

## Description:

Set specified colored pixel on selected images.

## Default values:

z=0, opacity=1 and color1=0.

```
gmic image.jpg repeat 10000 point {u(100)}%,{u(100)}%,0,1,${-rgb} done
```

---

# Command: polka_dots

## Arguments:

* diameter>=0,_density,_offset1,_offset2,_angle,_aliasing,_shading,_opacity,_color,...

## Description:

Draw dots pattern on selected images.

## Default values:

density=20, offset1=offset2=50, angle=0, aliasing=10, shading=1, opacity=1 and color=255.

```
gmic image.jpg polka_dots 10,15,0,0,20,10,1,0.5,0,128,255
```

---

# Command: polygon

|  |  |
| --- | --- |
|  | Built-in command |

## Arguments:

* N>=1,x1[%],y1[%],...,xN[%],yN[%],_opacity,_pattern,_color1,...    or
* [coords],_opacity,_pattern,_color1,...

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

```
gmic image.jpg polygon 4,20%,20%,80%,30%,80%,70%,20%,80%,0.3,0,255,0 polygon 4,20%,20%,80%,30%,80%,70%,20%,80%,1,0xCCCCCCCC,255
```

### • Example #2

```
gmic image.jpg 2,16,1,1,'u(x?h#0:w#0)' polygon[-2] [-1],0.6,255,0,255 remove[-1]
```

---

# Command: quiver

## Arguments:

* [function_image],_sampling[%]>0,_factor>=0,_is_arrow={ 0:No | 1:Yes },_opacity,_color1,...

## Description:

Draw specified 2D vector/orientation field on selected images.

## Default values:

sampling=5%, factor=1, is_arrow=1, opacity=1, pattern=(undefined)

and color1=0.

## Examples of use:

### • Example #1

```
gmic 100,100,1,2,'!c?x-w/2:y-h/2' 500,500,1,3,255 quiver[-1] [-2],10
```

### • Example #2

```
gmic image.jpg +rescale2d ,600 luminance[0] gradient[0] mul[1] -1 reverse[0,1] append[0,1] c blur[0] 8 orientation[0] quiver[1] [0],20,1,1,0.8,255
```

---

# Command: rectangle

## Arguments:

* x0[%],y0[%],x1[%],y1[%],_opacity,_pattern,_color1,...

## Description:

Draw specified colored rectangle on selected images.

pattern is an hexadecimal number starting with 0x which can be omitted
even if a color is specified. If a pattern is specified, the rectangle is
drawn outlined instead of filled.

## Default values:

opacity=1, pattern=(undefined) and color1=0.

```
gmic image.jpg repeat 30 { rectangle {u(100)}%,{u(100)}%,{u(100)}%,{u(100)}%,0.3,${-rgb} }
```

---

# Command: rorschach

## Arguments:

* 'smoothness[%]>=0','mirroring={ 0:None | 1:X | 2:Y | 3:XY }

## Description:

Render rorschach-like inkblots on selected images.

## Default values:

smoothness=5% and mirroring=1.

```
gmic 400,400 rorschach 3%
```

---

# Command: sierpinski

## Arguments:

* recursion_level>=0

## Description:

Draw Sierpinski triangle on selected images.

## Default values:

recursion_level=7.

```
gmic image.jpg sierpinski 7
```

---

# Command: spiralbw

## Arguments:

* width>0,_height>0,_is_2dcoords={ 0:No | 1:Yes }

## Description:

Input a 2D rectangular spiral image with specified size.

## Default values:

height=width and is_2dcoords=0.

## Examples of use:

### • Example #1

```
gmic spiralbw 16
```

### • Example #2

```
gmic image.jpg spiralbw {[w,h]},1 +warp[0] [1],0,1,1 +warp[2] [1],2,1,1
```

---

# Command: tetraedron_shade

## Arguments:

* x0,y0,z0,x1,y1,z1,x2,y2,z2,x3,y3,z3,R0,G0,B0,...,R1,G1,B1,...,R2,G2,B2,...,R3,G3,B3,...

## Description:

Draw tetraedron with interpolated colors on selected (volumetric) images.

---

# Command: text

|  |  |
| --- | --- |
|  | Built-in command |

## Arguments:

* text,_x[%|~],_y[%|~],_{ font_height[%]>=0 | custom_font },_opacity,_color1,...

## Description:

Draw specified colored text string on selected images.

(*equivalent to shortcut command* t).

If one of the x or y argument ends with a ~, its value is expected to be a centering ratio (in [0,1]) rather than a position.
Usual centering ratio are { 0:left-justified | 0.5:centered | 1:right-justified }.
Sizes 13 and 128 are special and correspond to binary fonts (no-antialiasing). Any other font size is rendered with anti-aliasing.
Specifying an empty target image resizes it to new dimensions such that the image contains the entire text string.
A custom font can be specified as a variable name that stores an image list of 256 or 512 items (512 for 256 character sprites + 256 associated opacities), or as an image selection that is a serialized version of such an image list.

## Default values:

x=y=0.01~, font_height=16, opacity=1 and color1=0.

## Examples of use:

### • Example #1

```
gmic image.jpg rescale2d ,600 div 2 y=0 repeat 30 { text {2*$>}" : This is a nice text!",10,$y,{2*$>},0.9,255 y+={2*$>} }
```

### • Example #2

```
gmic 0 text "G'MIC",0,0,23,1,255
```

---

# Command: text_outline

## Arguments:

* text,_x[%|~],_y[%|~],{ _font_height[%]>0 | custom_font },_outline>=0,_opacity,_color1,...

## Description:

Draw specified colored and outlined text string on selected images.

If one of the x or y argument ends with a ~, its value is expected to be
a centering ratio (in [0,1]) rather than a position.
Usual centering ratio are { 0:left-justified | 0.5:centered | 1:right-justified }.

## Default values:

x=y=0.01~, font_height=7.5%, outline=2, opacity=1, color1=color2=color3=255 and color4=255.

```
gmic image.jpg text_outline "Hi there!",10,10,63,3
```

---

# Command: triangle_shade

## Arguments:

* x0,y0,x1,y1,x2,y2,R0,G0,B0,...,R1,G1,B1,...,R2,G2,B2,...

## Description:

Draw triangle with interpolated colors on selected images.

```
gmic image.jpg triangle_shade 20,20,400,100,120,200,255,0,0,0,255,0,0,0,255
```

---

# Command: truchet

## Arguments:

* _scale>0,_radius>=0,_pattern_type={ 0:Straight | 1:Curved }

## Description:

Fill selected images with random truchet patterns.

## Default values:

scale=32, radius=5 and pattern_type=1.

```
gmic 400,300 truchet ,
```

---

# Command: turbulence

## Arguments:

* _radius>0,_octaves={ 1,2,3...,12 },_alpha>0,_difference={ -10,10 },_mode={ 0,1,2,3 }

## Description:

Render fractal noise or turbulence on selected images.

## Default values:

radius=32, octaves=6, alpha=3, difference=0 and mode=0.

This command has a [tutorial page](https://gmic.eu/oldtutorial/_turbulence).

```
gmic 400,400,1,3 turbulence 16
```

---

# Command: yinyang

### No argumentsDescription:Draw a yin-yang symbol on selected images. ``` gmic 400,400 yinyang ```

---

# Command: boxfitting

## Arguments:

* _min_box_size>=1,_max_box_size>=0,_initial_density>=0,_min_spacing>0

## Description:

Apply box fitting effect on selected images, as displayed the web page:

<http://www.complexification.net/gallery/machines/boxFittingImg/>.

## Default values:

min_box_size=1, max_box_size=0, initial_density=0.25 and min_spacing=1.

```
gmic image.jpg boxfitting ,
```

---

# Command: brushify

## Arguments:

* [brush],_brush_nb_sizes>=1,0<=_brush_min_size_factor<=1,_brush_nb_orientations>=1,_brush_light_type,0<=_brush_light_strength<=1,_brush_opacity,_painting_density[%]>=0,0<=_painting_contours_coherence<=1,0<=_painting_orientation_coherence<=1,_painting_coherence_alpha[%]>=0,_painting_coherence_sigma[%]>=0,_painting_primary_angle,0<=_painting_angle_dispersion<=1

## Description:

Apply specified brush to create painterly versions of specified images.

brush_light_type can be { 0:None | 1:Flat | 2:Darken | 3:Lighten | 4:Full }.

## Default values:

brush_nb_sizes=3, brush_min_size_factor=0.66, brush_nb_orientations=12, brush_light_type=0, brush_light_strength=0.25, brush_opacity=0.8, painting_density=20%, painting_contours_coherence=0.9, painting_orientation_coherence=0.9, painting_coherence_alpha=1, painting_coherence_sigma=1, painting_primary_angle=0, painting_angle_dispersion=0.2

```
gmic image.jpg 40,40 gaussian[-1] 10,4 spread[-1] 10,0 brushify[0] [1],1
```

---

# Command: cartoon

## Arguments:

* _smoothness,_sharpening,_threshold>=0,_thickness>=0,_color>=0,quantization>0

## Description:

Apply cartoon effect on selected images.

## Default values:

smoothness=3, sharpening=150, threshold=20, thickness=0.25, color=1.5 and quantization=8.

```
gmic image.jpg cartoon 3,50,10,0.25,3,16
```

---

# Command: color_ellipses

## Arguments:

* _count>0,_radius>=0,_opacity>=0

## Description:

Add random color ellipses to selected images.

## Default values:

count=400, radius=5 and opacity=0.1.

```
gmic image.jpg +color_ellipses ,,0.15
```

---

# Command: cubism

## Arguments:

* _density>=0,0<=_thickness<=50,_max_angle,_opacity,_smoothness>=0

## Description:

Apply cubism effect on selected images.

## Default values:

density=50, thickness=10, max_angle=75, opacity=0.7 and smoothness=0.

```
gmic image.jpg cubism ,
```

---

# Command: draw_whirl

## Arguments:

* _amplitude>=0

## Description:

Apply whirl drawing effect on selected images.

## Default values:

amplitude=100.

```
gmic image.jpg draw_whirl ,
```

---

# Command: drop_shadow

## Arguments:

* _offset_x[%],_offset_y[%],_smoothness[%]>=0,curvature_x>=0,curvature_y>=0,_expand_size={ 0:No | 1:Yes },_output_separate_layers={ 0:No | 1:Yes }

## Description:

Drop shadow behind selected images.

## Default values:

offset_x=20, offset_y=offset_x, smoothness=5, curvature_x=curvature_y=0, expand_size=1 and output_separate_layers=0.

```
gmic image.jpg drop_shadow 10,20,5,0.5 display_rgba
```

---

# Command: drop_shadow

## Arguments:

* _offset_x[%],_offset_y[%],_smoothness[%]>=0,curvature_x>=0,curvature_y>=0,_expand_size={ 0:No | 1:Yes },_output_separate_layers={ 0:No | 1:Yes }

## Description:

Drop shadow behind selected images.

## Default values:

offset_x=20, offset_y=offset_x, smoothness=5, curvature_x=curvature_y=0, expand_size=1 and output_separate_layers=0.

```
gmic image.jpg drop_shadow 10,20,5,0.5 display_rgba
```

---

# Command: ellipsionism

## Arguments:

* _R[%]>0,_r[%]>0,_smoothness[%]>=0,_opacity,_outline>0,_density>0

## Description:

Apply ellipsionism filter to selected images.

## Default values:

R=10, r=3, smoothness=1%, opacity=0.7, outline=8 and density=0.6.

```
gmic image.jpg ellipsionism ,
```

---

# Command: fire_edges

## Arguments:

* _edges>=0,0<=_attenuation<=1,_smoothness>=0,_threshold>=0,_nb_frames>0,_starting_frame>=0,frame_skip>=0

## Description:

Generate fire effect from edges of selected images.

## Default values:

edges=0.7, attenuation=0.25, smoothness=0.5, threshold=25, nb_frames=1, starting_frame=20 and frame_skip=0.

```
gmic image.jpg fire_edges ,
```

---

# Command: fractalize

## Arguments:

* 0<=detail_level<=1

## Description:

Randomly fractalize selected images.

## Default values:

detail_level=0.8

```
gmic image.jpg fractalize ,
```

---

# Command: glow

## Arguments:

* _amplitude>=0

## Description:

Add soft glow on selected images.

## Default values:

amplitude=1%.

```
gmic image.jpg glow ,
```

---

# Command: halftone

## Arguments:

* nb_levels>=2,_size_dark>=2,_size_bright>=2,_shape={ 0:Square | 1:Diamond | 2:Circle | 3:inv-square | 4:inv-diamond | 5:inv-circle },_smoothness[%]>=0

## Description:

Apply halftone dithering to selected images.

## Default values:

nb_levels=5, size_dark=8, size_bright=8, shape=5 and smoothnesss=0.

```
gmic image.jpg halftone ,
```

---

# Command: hardsketchbw

## Arguments:

* _amplitude>=0,_density>=0,_opacity,0<=_edge_threshold<=100,_is_fast={ 0:No | 1:Yes }

## Description:

Apply hard B&W sketch effect on selected images.

## Default values:

amplitude=1000, sampling=3, opacity=0.1, edge_threshold=20 and is_fast=0.

```
gmic image.jpg +hardsketchbw 200,70,0.1,10 median[-1] 2 +local reverse blur[-1] 3 blend[-2,-1] overlay done
```

---

# Command: hearts

## Arguments:

* _density>=0

## Description:

Apply heart effect on selected images.

## Default values:

density=10.

```
gmic image.jpg hearts ,
```

---

# Command: houghsketchbw

## Arguments:

* _density>=0,_radius>0,0<=_threshold<=100,0<=_opacity<=1,_votesize[%]>0

## Description:

Apply hough B&W sketch effect on selected images.

## Default values:

density=100, radius=3, threshold=100, opacity=0.1 and votesize=100%.

```
gmic image.jpg +houghsketchbw ,
```

---

# Command: lightrays

## Arguments:

* 100<=_density<=0,_center_x[%],_center_y[%],_ray_length>=0,_ray_attenuation>=0

## Description:

Generate ray lights from the edges of selected images.

## Default values:

density=50%, center_x=50%, center_y=50%, ray_length=0.9 and ray_attenuation=0.5.

```
gmic image.jpg +lightrays , + cut 0,255
```

---

# Command: light_relief

## Arguments:

* _ambient_light,_specular_lightness,_specular_size,_darkness,_light_smoothness,_xl,_yl,_zl,_zscale,_opacity_is_heightmap={ 0:No | 1:Yes }

## Description:

Apply relief light to selected images.

Default values(s) : ambient_light=0.3, specular_lightness=0.5, specular_size=0.2, darkness=0, xl=0.2, yl=zl=0.5,
zscale=1, opacity=1 and opacity_is_heightmap=0.

```
gmic image.jpg blur 2 light_relief 0.3,4,0.1,0
```

---

# Command: linify

## Arguments:

* 0<=_density<=100,_spreading>=0,_resolution[%]>0,_line_opacity>=0,_line_precision>0,_mode={ 0:Subtractive | 1:Additive }

## Description:

Apply linify effect on selected images.

The algorithm is inspired from the one described on the webpage <http://linify.me/about>.

## Default values:

density=50, spreading=2, resolution=40%, line_opacity=10, line_precision=24 and mode=0.

```
gmic image.jpg linify 60
```

---

# Command: mosaic

## Arguments:

* 0<=_density<=100

## Description:

Create random mosaic from selected images.

## Default values:

density=30.

```
gmic image.jpg mosaic , +fill "I!=J(1) || I!=J(0,1)?[0,0,0]:I"
```

---

# Command: old_photo

### No argumentsDescription:Apply old photo effect on selected images. ``` gmic image.jpg old_photo ```

---

# Command: pencilbw

## Arguments:

* _size>=0,_amplitude>=0

## Description:

Apply B&W pencil effect on selected images.

## Default values:

size=0.3 and amplitude=60.

```
gmic image.jpg pencilbw ,
```

---

# Command: pixelsort

## Arguments:

* _ordering={ +:Increasing | -:Decreasing },_axis={ x | y | z | xy | yx },_[sorting_criterion],_[mask]

## Description:

Apply a pixel sorting algorithm on selected images, as described in the page :

<http://satyarth.me/articles/pixel-sorting/>.

## Default values:

ordering=+, axis=x and sorting_criterion=mask=(undefined).

```
gmic image.jpg +norm +ge[-1] 30% +pixelsort[0] +,y,[1],[2]
```

---

# Command: polaroid

## Arguments:

* _size1>=0,_size2>=0

## Description:

Create polaroid effect in selected images.

## Default values:

size1=10 and size2=20.

```
gmic image.jpg to_rgba polaroid 5,30 rotate 20 drop_shadow , drgba
```

---

# Command: polygonize

## Arguments:

* _warp_amplitude>=0,_smoothness[%]>=0,_min_area[%]>=0,_resolution_x[%]>0,_resolution_y[%]>0

## Description:

Apply polygon effect on selected images.

## Default values:

warp_amplitude=300, smoothness=2%, min_area=0.1%, resolution_x=resolution_y=10%.

```
gmic image.jpg +polygonize 100,10 fill[-1] "I!=J(1) || I!=J(0,1)?[0,0,0]:I"
```

---

# Command: poster_edges

## Arguments:

* 0<=_edge_threshold<=100,0<=_edge_shade<=100,_edge_thickness>=0,_edge_antialiasing>=0,0<=_posterization_level<=15,_posterization_antialiasing>=0

## Description:

Apply poster edges effect on selected images.

## Default values:

edge_threshold=40, edge_shade=5, edge_thickness=0.5, edge_antialiasing=10, posterization_level=12 and posterization_antialiasing=0.

```
gmic image.jpg poster_edges ,
```

---

# Command: poster_hope

## Arguments:

* _smoothness>=0

## Description:

Apply Hope stencil poster effect on selected images.

## Default values:

smoothness=3.

```
gmic image.jpg poster_hope ,
```

---

# Command: rodilius

## Arguments:

* 0<=_amplitude<=100,_0<=thickness<=100,_sharpness>=0,_nb_orientations>0,_offset,_color_mode={ 0:Darker | 1:Brighter }

## Description:

Apply rodilius (fractalius-like) filter on selected images.

## Default values:

amplitude=10, thickness=10, sharpness=400, nb_orientations=7, offset=0 and color_mode=1.

## Examples of use:

### • Example #1

```
gmic image.jpg rodilius 12,10,300,10 normalize_local 10,6
```

### • Example #2

```
gmic image.jpg normalize_local 10,16 rodilius 10,4,400,16 smooth 60,0,1,1,4 normalize_local 10,16
```

---

# Command: sketchbw

## Arguments:

* _nb_angles>0,_start_angle,_angle_range>=0,_length>=0,_threshold>=0,_opacity,_bgfactor>=0,_density>0,_sharpness>=0,_anisotropy>=0,_smoothness>=0,_coherence>=0,_is_boost={ 0:No | 1:Yes },_is_curved={ 0:No | 1:Yes }

## Description:

Apply sketch effect to selected images.

## Default values:

nb_angles=2, start_angle=45, angle_range=180, length=30, threshold=3, opacity=0.03, bgfactor=0, density=0.6, sharpness=0.1, anisotropy=0.6, smoothness=0.25, coherence=1, is_boost=0 and is_curved=1.

```
gmic image.jpg +sketchbw 1 reverse blur[-1] 3 blend[-2,-1] overlay
```

---

# Command: sponge

## Arguments:

* _size>0

## Description:

Apply sponge effect on selected images.

## Default values:

size=13.

```
gmic image.jpg sponge ,
```

---

# Command: stained_glass

## Arguments:

* _edges[%]>=0, shading>=0, is_thin_separators={ 0:No | 1:Yes }

## Description:

Generate stained glass from selected images.

## Default values:

edges=40%, shading=0.2 and is_precise=0.

```
gmic image.jpg stained_glass 20%,1 cut 0,20
```

---

# Command: stars

## Arguments:

* _density[%]>=0,_depth>=0,_size>0,_nb_branches>=1,0<=_thickness<=1,_smoothness[%]>=0,_R,_G,_B,_opacity

## Description:

Add random stars to selected images.

## Default values:

density=10%, depth=1, size=32, nb_branches=5, thickness=0.38, smoothness=0.5, R=G=B=200 and opacity=1.

```
gmic image.jpg stars ,
```

---

# Command: stencil

## Arguments:

* _radius[%]>=0,_smoothness>=0,_iterations>=0

## Description:

Apply stencil filter on selected images.

## Default values:

radius=3, smoothness=1 and iterations=8.

```
gmic image.jpg +norm stencil. 2,1,4 +mul rm[0]
```

---

# Command: stencilbw

## Arguments:

* _edges>=0,_smoothness>=0

## Description:

Apply B&W stencil effect on selected images.

## Default values:

edges=15 and smoothness=10.

```
gmic image.jpg +stencilbw 40,4
```

---

# Command: stylize

## Arguments:

* [style_image],_fidelity_finest,_fidelity_coarsest,_fidelity_smoothness_finest>=0,_fidelity_smoothnes_coarsest>=0,0<=_fidelity_chroma<=1,_init_type,_init_resolution>=0,init_max_gradient>=0,_patch_size_analysis>0,_patch_size_synthesis>0,_patch_size_synthesis_final>0,_nb_matches_finest>=0,_nb_matches_coarsest>=0,_penalize_repetitions>=0,_matching_precision>=0,_scale_factor>1,_skip_finest_scales>=0,_"image_matching_command"

## Description:

Transfer colors and textures from specified style image to selected images, using a multi-scale patch-mathing algorithm.

If instant display window[0] is opened, the steps of the image synthesis are displayed on it.
init_type can be { 0:Best-match | 1:Identity | 2:Randomized }.

## Default values:

fidelity_finest=0.5, fidelity_coarsest=2, fidelity_smoothness_finest=3, fidelity_smoothness_coarsest=0.5, fidelity_chroma=0.1, init_type=0, init_resolution=16, init_max_gradient=0, patch_size_analysis=5, patch_size_synthesis=5, patch_size_synthesis_final=5, nb_matches_finest=2, nb_matchesc_coarsest=30, penalize_repetitions=2, matching_precision=2, scale_factor=1.85, skip_finest_scales=0 and 'image_matching_command'="s c,-3 match_pca[0] [2] b[0,2] xy,0.7 n[0,2] 0,255 n[1,2] 0,200 a[0,1] c a[1,2] c"'.

---

# Command: tetris

## Arguments:

* _scale>0

## Description:

Apply tetris effect on selected images.

## Default values:

scale=10.

```
gmic image.jpg +tetris 10
```

---

# Command: warhol

## Arguments:

* _M>0,_N>0,_smoothness>=0,_color>=0

## Description:

Create MxN Andy Warhol-like artwork from selected images.

## Default values:

M=3, N=M, smoothness=2 and color=20.

```
gmic image.jpg warhol 3,3,3,40
```

---

# Command: weave

## Arguments:

* _density>=0,0<=_thickness<=100,0<=_shadow<=100,_shading>=0,_fibers_amplitude>=0,_fibers_smoothness>=0,_angle,-1<=_x_curvature<=1,-1<=_y_curvature<=1

## Description:

Apply weave effect to the selected images.

angle can be { 0:0 deg. | 1:22.5 deg. | 2:45 deg. | 3:67.5 deg. }.

## Default values:

density=6, thickness=65, shadow=40, shading=0.5, fibers_amplitude=0, _'fibers_smoothness=0', angle=0 and curvature_x=curvature_y=0

```
gmic image.jpg weave ,
```

---

# Command: whirls

## Arguments:

* _texture>=0,_smoothness>=0,_darkness>=0,_lightness>=0

## Description:

Add random whirl texture to selected images.

## Default values:

texture=3, smoothness=6, darkness=0.5 and lightness=1.8.

```
gmic image.jpg whirls ,
```

---

# Command: deform

## Arguments:

* _amplitude[%]>=0,_interpolation

## Description:

Apply random smooth deformation on selected images.

interpolation can be { 0:None | 1:Linear | 2:Bicubic }.

## Default values:

amplitude=10.

```
gmic image.jpg +deform[0] 10 +deform[0] 20
```

---

# Command: euclidean2polar

## Arguments:

* _center_x[%],_center_y[%],_stretch_factor>0,_boundary_conditions={ 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }

## Description:

Apply euclidean to polar transform on selected images.

## Default values:

center_x=center_y=50%, stretch_factor=1 and boundary_conditions=3.

```
gmic image.jpg +euclidean2polar ,
```

---

# Command: equirectangular2nadirzenith

### No argumentsDescription:Transform selected equirectangular images to nadir/zenith rectilinear projections.

---

# Command: fisheye

## Arguments:

* _center_x,_center_y,0<=_radius<=100,_amplitude>=0

## Description:

Apply fish-eye deformation on selected images.

## Default values:

x=y=50, radius=50 and amplitude=1.2.

```
gmic image.jpg +fisheye ,
```

---

# Command: flower

## Arguments:

* _amplitude,_frequency,_offset_r[%],_angle,_center_x[%],_center_y[%],_boundary_conditions={ 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }

## Description:

Apply flower deformation on selected images.

## Default values:

amplitude=30, frequency=6, offset_r=0, angle=0, center_x=center_y=50% and boundary_conditions=3.

```
gmic image.jpg +flower ,
```

---

# Command: kaleidoscope

## Arguments:

* _center_x[%],_center_y[%],_radius,_angle,_boundary_conditions={ 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }

## Description:

Create kaleidoscope effect from selected images.

## Default values:

center_x=center_y=50%, radius=100, angle=30 and boundary_conditions=3.

```
gmic image.jpg kaleidoscope ,
```

---

# Command: map_sphere

## Arguments:

* _width>0,_height>0,_radius,_dilation>0,_fading>=0,_fading_power>=0

## Description:

Map selected images on a sphere.

## Default values:

width=height=512, radius=100, dilation=0.5, fading=0 and fading_power=0.5.

```
gmic image.jpg map_sphere ,
```

---

# Command: nadirzenith2equirectangular

### No argumentsDescription:Transform selected nadir/zenith rectilinear projections to equirectangular images.

---

# Command: polar2euclidean

## Arguments:

* _center_x[%],_center_y[%],_stretch_factor>0,_boundary_conditions={ 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }

## Description:

Apply euclidean to polar transform on selected images.

## Default values:

center_x=center_y=50%, stretch_factor=1 and boundary_conditions=3.

```
gmic image.jpg +euclidean2polar ,
```

---

# Command: raindrops

## Arguments:

* _amplitude,_density>=0,_wavelength>=0,_merging_steps>=0

## Description:

Apply raindrops deformation on selected images.

## Default values:

amplitude=80,density=0.1, wavelength=1 and merging_steps=0.

```
gmic image.jpg +raindrops ,
```

---

# Command: ripple

## Arguments:

* _amplitude,_bandwidth,_shape={ 0:Block | 1:Triangle | 2:Sine | 3:Sine+ | 4:Random },_angle,_offset

## Description:

Apply ripple deformation on selected images.

## Default values:

amplitude=10, bandwidth=10, shape=2, angle=0 and offset=0.

```
gmic image.jpg +ripple ,
```

---

# Command: rotoidoscope

## Arguments:

* _center_x[%],_center_y[%],_tiles>0,_smoothness[%]>=0,_boundary_conditions={ 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }

## Description:

Create rotational kaleidoscope effect from selected images.

## Default values:

center_x=center_y=50%, tiles=10, smoothness=1 and boundary_conditions=3.

```
gmic image.jpg +rotoidoscope ,
```

---

# Command: spherize

## Arguments:

* _radius[%]>=0,_strength,_smoothness[%]>=0,_center_x[%],_center_y[%],_ratio_x/y>0,_angle,_interpolation

## Description:

Apply spherize effect on selected images.

## Default values:

radius=50%, strength=1, smoothness=0, center_x=center_y=50%, ratio_x/y=1, angle=0 and interpolation=1.

```
gmic image.jpg grid 5%,5%,0,0,0.6,255 spherize ,
```

---

# Command: symmetrize

## Arguments:

* _x[%],_y[%],_angle,_boundary_conditions={ 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror },_is_antisymmetry={ 0:No | 1:Yes },_swap_sides={ 0:No | 1:Yes }

## Description:

Symmetrize selected images regarding specified axis.

## Default values:

x=y=50%, angle=90, boundary_conditions=3, is_antisymmetry=0 and swap_sides=0.

```
gmic image.jpg +symmetrize 50%,50%,45 +symmetrize[-1] 50%,50%,-45
```

---

# Command: transform_polar

## Arguments:

* "expr_radius",_"expr_angle",_center_x[%],_center_y[%],_boundary_conditions={ 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }

## Description:

Apply user-defined transform on polar representation of selected images.

## Default values:

expr_radius=R-r, expr_rangle=a, center_x=center_y=50% and boundary_conditions=3.

```
gmic image.jpg +transform_polar[0] R*(r/R)^2,a +transform_polar[0] r,2*a
```

---

# Command: twirl

## Arguments:

* _amplitude,_center_x[%],_center_y[%],_boundary_conditions={ 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }

## Description:

Apply twirl deformation on selected images.

## Default values:

amplitude=1, center_x=center_y=50% and boundary_conditions=3.

```
gmic image.jpg twirl 0.6
```

---

# Command: warp

|  |  |
| --- | --- |
|  | Built-in command |

## Arguments:

* [warping_field],_mode,_interpolation,_boundary_conditions,_nb_frames>0

## Description:

Warp selected images with specified displacement field.

mode can be { 0:Backward-absolute | 1:Backward-relative | 2:Forward-absolute | 3:Forward-relative }.
interpolation can be { 0:Nearest-neighbor | 1:Linear | 2:Cubic }.
boundary_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.

## Default values:

mode=0, interpolation=1, boundary_conditions=0 and nb_frames=1.

This command has a [tutorial page](https://gmic.eu/oldtutorial/_warp).

```
gmic image.jpg 100%,100%,1,2,'X=x/w-0.5;Y=y/h-0.5;R=(X*X+Y*Y)^0.5;A=atan2(Y,X);130*R*(!c?cos(4*A):sin(8*A))' warp[-2] [-1],1,1,0 quiver[-1] [-1],10,1,1,1,100
```

---

# Command: warp_patch

## Arguments:

* [displacement_map],patch_width>=1,_patch_height>=1,_patch_depth>=1,_std_factor>0,_boundary_conditions,_fast_approximation={ 0:No | 1:Yes }

## Description:

Patch-warp selected images, with specified 2D or 3D displacement map (in backward-absolute mode).

Argument std_factor sets the std of the gaussian weights for the patch overlap,
equal to std = std_factor\*patch_size.
boundary_conditions can be { 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }.

## Default values:

std_factor=0.3, boundary_conditions=3 and fast_approximation=0.

---

# Command: warp_perspective

## Arguments:

* _x-angle,_y-angle,_zoom>0,_x-center,_y-center,_boundary_conditions={ 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }

## Description:

Warp selected images with perspective deformation.

## Default values:

x-angle=1.5, y-angle=0, zoom=1, x-center=y-center=50 and boundary_conditions=2.

```
gmic image.jpg warp_perspective ,
```

---

# Command: warp_rbf

## Arguments:

* xs0[%],ys0[%],xt0[%],yt0[%],...,xsN[%],ysN[%],xtN[%],ytN[%]

## Description:

Warp selected images using RBF-based interpolation.

Each argument (xsk,ysk)-(xtk,ytk) corresponds to the coordinates of a keypoint
respectively on the source and target images. The set of all keypoints define the overall image deformation.

```
gmic image.jpg +warp_rbf 0,0,0,0,100%,0,100%,0,100%,100%,100%,100%,0,100%,0,100%,50%,50%,70%,50%,25%,25%,25%,75%
```

---

# Command: warp_seamless

## Arguments:

* [displacement_map],_sigma[%]>0,_blend_dimension={ 0:Auto | 1:1D | 2:2D | 3:3D }

## Description:

Warp selected 2D or 3D images by specified displacement field, using seamless blending.

## Default values:

sigma=5% and blend_dimension=0.

```
gmic sp colorful,512 100%,100%,1,2,[x,y] l. { s xy,8 sort_list +,u append_tiles , } +warp[0] [1] +warp_seamless[0] [1]
```

---

# Command: water

## Arguments:

* _amplitude,_smoothness>=0,_angle

## Description:

Apply water deformation on selected images.

## Default values:

amplitude=30, smoothness=1.5 and angle=45.

```
gmic image.jpg water ,
```

---

# Command: wave

## Arguments:

* _amplitude>=0,_frequency>=0,_center_x,_center_y

## Description:

Apply wave deformation on selected images.

## Default values:

amplitude=4, frequency=0.4 and center_x=center_y=50.

```
gmic image.jpg wave ,
```

---

# Command: wind

## Arguments:

* _amplitude>=0,_angle,0<=_attenuation<=1,_threshold

## Description:

Apply wind effect on selected images.

## Default values:

amplitude=20, angle=0, attenuation=0.7 and threshold=20.

```
gmic image.jpg +wind ,
```

---

# Command: zoom

## Arguments:

* _factor,_cx,_cy,_cz,_boundary_conditions={ 0:Dirichlet | 1:Neumann | 2:Periodic | 3:Mirror }

## Description:

Apply zoom factor to selected images.

## Default values:

factor=1, cx=cy=cz=0.5 and boundary_conditions=0.

```
gmic image.jpg +zoom[0] 0.6 +zoom[0] 1.5
```

---

# Command: cracks

## Arguments:

* 0<=_density<=100,_is_relief={ 0:No | 1:Yes },_opacity,_color1,...

## Description:

Draw random cracks on selected images with specified color.

## Default values:

density=25, is_relief=0, opacity=1 and color1=0.

```
gmic image.jpg +cracks ,
```

---

# Command: light_patch

## Arguments:

* _density>0,_darkness>=0,_lightness>=0

## Description:

Add light patches to selected images.

## Default values:

density=10, darkness=0.9 and lightness=1.7.

```
gmic image.jpg +light_patch 20,0.9,4
```

---

# Command: pixelize

## Arguments:

* _scale_x>0,_scale_y>0,_scale_z>0

## Description:

Pixelize selected images with specified scales.

## Default values:

scale_x=20 and scale_y=scale_z=scale_x.

```
gmic image.jpg +pixelize ,
```

---

# Command: scanlines

## Arguments:

* _amplitude,_bandwidth,_shape={ 0:Block | 1:Triangle | 2:Sine | 3:Sine+ | 4:Random },_angle,_offset

## Description:

Apply ripple deformation on selected images.

## Default values:

amplitude=60, bandwidth=2, shape=0, angle=0 and offset=0.

```
gmic image.jpg +scanlines ,
```

---

# Command: shade_stripes

## Arguments:

* _frequency>=0,_direction={ 0:Horizontal | 1:Vertical },_darkness>=0,_lightness>=0

## Description:

Add shade stripes to selected images.

## Default values:

frequency=5, direction=1, darkness=0.8 and lightness=2.

```
gmic image.jpg +shade_stripes 30
```

---

# Command: shadow_patch

## Arguments:

* _opacity>=0

## Description:

Add shadow patches to selected images.

## Default values:

opacity=0.7.

```
gmic image.jpg +shadow_patch 0.4
```

---

# Command: shuffle

### No argumentsDescription:Shuffle vectors of selected images with Fisher-Yates algorithm, as described in <https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle>. ``` gmic uniform_distribution 8,3 shuffle ```

---

# Command: spread

## Arguments:

* _dx[%]>=0,_dy[%]>=0,_dz[%]>=0

## Description:

Spread pixel values of selected images randomly along x,y and z.

## Default values:

dx=3, dy=dx and dz=0.

```
gmic image.jpg +spread 3
```

---

# Command: stripes_y

## Arguments:

* _frequency>=0

## Description:

Add vertical stripes to selected images.

## Default values:

frequency=10.

```
gmic image.jpg +stripes_y ,
```

---

# Command: texturize_canvas

## Arguments:

* _amplitude>=0,_fibrousness>=0,_emboss_level>=0

## Description:

Add paint canvas texture to selected images.

## Default values:

amplitude=20, fibrousness=3 and emboss_level=0.6.

```
gmic image.jpg +texturize_canvas ,
```

---

# Command: texturize_paper

### No argumentsDescription:Add paper texture to selected images. ``` gmic image.jpg +texturize_paper ```

---

# Command: vignette

## Arguments:

* _strength>=0,0<=_radius_min<=100,0<=_radius_max<=100

## Description:

Add vignette effect to selected images.

## Default values:

strength=100, radius_min=70 and radius_max=90.

```
gmic image.jpg vignette ,
```

---

# Command: watermark_visible

## Arguments:

* _text,0<_opacity<1,_{ size>0 | font },_angle,_mode={ 0:Remove | 1:Add },_smoothness>=0

## Description:

Add or remove a visible watermark on selected images (value range must be [0,255]).

## Default values:

text=(c) G'MIC, opacity=0.3, size=53, angle=25, mode=1 and smoothness=0.

```
gmic image.jpg watermark_visible ,0.7
```

---

# Command: blend

## Arguments:

* [layer],blending_mode,_opacity[%],_selection_is={ 0:Base-layers | 1:Top-layers }    or
* blending_mode,_opacity[%]

## Description:

Blend selected G,GA,RGB or RGBA images by specified layer or blend all selected images together,

using specified blending mode.
blending_mode can be { add | alpha | and | average | blue | burn | darken | difference |
divide | dodge | edges | exclusion | freeze | grainextract | grainmerge | green | hardlight |
hardmix | hue | interpolation | lchlightness | lighten | lightness | linearburn | linearlight | luminance |
multiply | negation | or | overlay | pinlight | red | reflect | saturation |
screen | seamless | seamless_mixed | shapeareamax | shapeareamax0 | shapeareamin | shapeareamin0 |
shapeaverage | shapeaverage0 | shapemedian | shapemedian0 | shapemin | shapemin0 | shapemax | shapemax0 |
shapeprevalent | softburn | softdodge | softlight | stamp | subtract | value | vividlight | xor }.
opacity must be in range [0,1] (or [0%,100%]).

## Default values:

blending_mode=alpha, opacity=1 and selection_is=0.

## Examples of use:

### • Example #1

```
gmic image.jpg +drop_shadow , rescale2d[-1] ,200 rotate[-1] 20 +blend alpha display_rgba[-2]
```

### • Example #2

```
gmic image.jpg testimage2d {w},{h} blend overlay
```

### • Example #3

```
gmic command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" image.jpg testimage2d {w},{h} ex add,alpha,and,average,blue,burn,darken
```

### • Example #4

```
gmic command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" image.jpg testimage2d {w},{h} ex difference,divide,dodge,exclusion,freeze,grainextract,grainmerge
```

### • Example #5

```
gmic command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" image.jpg testimage2d {w},{h} ex green,hardlight,hardmix,hue,interpolation,lighten,lightness
```

### • Example #6

```
gmic command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" image.jpg testimage2d {w},{h} ex linearburn,linearlight,luminance,multiply,negation,or,overlay
```

### • Example #7

```
gmic command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" image.jpg testimage2d {w},{h} ex pinlight,red,reflect,saturation,screen,shapeaverage,softburn
```

### • Example #8

```
gmic command "ex : $""=arg repeat $""# +blend[0,1] ${arg{$>+1}} text_outline[-1] Mode:\" \"${arg{$>+1}},2,2,23,2,1,255 done" image.jpg testimage2d {w},{h} ex softdodge,softlight,stamp,subtract,value,vividlight,xor
```

---

# Command: nblend

## Arguments:

* [layer],blending_mode,_opacity[%],_selection_is={ 0:Base-layers | 1:Top-layers }    or
* blending_mode,_opacity[%]

## Description:

---

# Command: blend_edges

## Arguments:

* smoothness[%]>=0

## Description:

Blend selected images togethers using edges mode.

```
gmic image.jpg testimage2d {w},{h} +blend_edges 0.8
```

---

# Command: blend_fade

## Arguments:

* [fading_shape]

## Description:

Blend selected images together using specified fading shape.

```
gmic image.jpg testimage2d {w},{h} 100%,100%,1,1,'cos(y/10)' normalize[-1] 0,1 +blend_fade[0,1] [2]
```

---

# Command: blend_median

### No argumentsDescription:Blend selected images together using median mode. ``` gmic image.jpg testimage2d {w},{h} +mirror[0] y +blend_median ```

---

# Command: blend_seamless

## Arguments:

* _is_mixed_mode={ 0:No | 1:Yes },_inner_fading[%]>=0,_outer_fading[%]>=0

## Description:

Blend selected images using a seamless blending mode (Poisson-based).

## Default values:

is_mixed=0, inner_fading=0 and outer_fading=100%.

---

# Command: fade_diamond

## Arguments:

* 0<=_start<=100,0<=_end<=100

## Description:

Create diamond fading from selected images.

## Default values:

start=80 and end=90.

```
gmic image.jpg testimage2d {w},{h} +fade_diamond 80,85
```

---

# Command: fade_linear

## Arguments:

* _angle,0<=_start<=100,0<=_end<=100

## Description:

Create linear fading from selected images.

## Default values:

angle=45, start=30 and end=70.

```
gmic image.jpg testimage2d {w},{h} +fade_linear 45,48,52
```

---

# Command: fade_radial

## Arguments:

* 0<=_start<=100,0<=_end<=100

## Description:

Create radial fading from selected images.

## Default values:

start=30 and end=70.

```
gmic image.jpg testimage2d {w},{h} +fade_radial 30,70
```

---

# Command: fade_x

## Arguments:

* 0<=_start<=100,0<=_end<=100

## Description:

Create horizontal fading from selected images.

## Default values:

start=30 and end=70.

```
gmic image.jpg testimage2d {w},{h} +fade_x 30,70
```

---

# Command: fade_y

## Arguments:

* 0<=_start<=100,0<=_end<=100

## Description:

Create vertical fading from selected images.

## Default values:

start=30 and end=70.

```
gmic image.jpg testimage2d {w},{h} +fade_y 30,70
```

---

# Command: fade_z

## Arguments:

* 0<=_start<=100,0<=_end<=100

## Description:

Create transversal fading from selected images.

## Default values:

start=30 and end=70.

---

# Command: sub_alpha

## Arguments:

* [base_image],0<=_minimize_alpha<=1

## Description:

Compute the alpha-channel difference (opposite of alpha blending) between the selected images

and the specified base image.
The alpha difference A-B is defined as the image having minimal opacity, such that alpha_blend(B,A-B) = A.
The min_alpha argument is used to relax the alpha minimality constraint. When set to 1, alpha is constrained to be minimal. When set to 0, alpha is maximal (i.e. 255).

## Default values:

minimize_alpha=1.

```
gmic image.jpg testimage2d {w},{h} +sub_alpha[0] [1] display_rgba
```
