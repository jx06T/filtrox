# 1. Basic Light & Contrast (Basic Adjustments)

## Command: adjust_colors

## Arguments:

- -100<=\_brightness<=100, -100<=\_contrast<=100, -100<=\_gamma<=100, -100<=\_hue_shift<=100, -100<=\_saturation<=100

## Description:

The primary tool for global adjustments. It handles Exposure (Brightness), Contrast, Midtone levels (Gamma), Hue, and Saturation in a single command.

```
gmic image.jpg +adjust_colors 5,10,0,0,15
```

---

## Command: apply_gamma

## Arguments:

- gamma>=0

## Description:

Adjusts the midtone brightness of the image. Values > 1 darken the image, while values < 1 brighten it (similar to Lightroom's Exposure/Midtones slider).

```
gmic image.jpg +apply_gamma 1.2
```

---

# 2. Color Calibration & Styles (Color Mixer)

## Command: balance_gamma

## Arguments:

- \_ref_color1, \_ref_color2, \_ref_color3

## Description:

Adjusts the color balance based on a reference color. Primarily used for White Balance correction to neutralize color casts.

```
gmic image.jpg +balance_gamma 128,128,128
```

---


## Command: mix_rgb

## Arguments:

- a11, a12, a13, a21, a22, a23, a31, a32, a33

## Description:

An RGB channel mixer. Functions like the "Calibration" panel in Lightroom, allowing for precise control over how red, green, and blue primary channels are blended.

```
gmic image.jpg +mix_rgb 0.9,0.1,0,0.1,0.9,0,0,0,1
```

---

# 3. Presence & Detail (Sharpening & Denoise)

## Command: sharpen

## Arguments:

- amplitude>=0, \_edge>=0

## Description:

Enhances image crispness. Directly corresponds to the "Amount" slider in the Lightroom Sharpening panel.

```
gmic image.jpg sharpen 100
```

```
gmic image.jpg blur 5 sharpen 300,1
```

---

## Command: unsharp

## Arguments:

- radius[%]>=0, \_amount>=0, \_threshold[%]>=0

## Description:

Applies Unsharp Masking. Ideal for final output sharpening to increase local edge contrast.

```
gmic image.jpg +unsharp 1.5,2,0
```

---

## Command: denoise_cnn

## Arguments:

- \_noise_level>=0

## Description:

Reduces digital noise using a Convolutional Neural Network. This is G'MIC’s most advanced noise reduction, similar to Lightroom's "Denoise AI" feature.

```
gmic image.jpg +denoise_cnn 15
```

---

## Command: rolling_guidance

## Arguments:

- std_deviation_s[%]>=0,std_deviation_r[%]>=0,\_precision>=0

## Description:

An edge-preserving filter. By adjusting the parameters, it can simulate Lightroom’s "Clarity" or "Texture" effects, enhancing mid-tone details without creating halos.

```
gmic image.jpg +rolling_guidance 4,10
```

---

# 4. Lens Correction & Geometry (Lens & Effects)

## Command: crop

## Arguments:

- x0[%], y0[%], x1[%], y1[%]

## Description:

The standard crop tool. Define the frame by specifying the top-left and bottom-right coordinates (pixels or percentages).

```
gmic image.jpg crop 10%,10%,90%,90%
```

---

## Command: undistort

## Arguments:

- -1<=\_amplitude<=1

## Description:

Corrects lens distortion. Use negative values to fix barrel distortion (wide angle) and positive values to fix pincushion distortion (telephoto).

```
gmic image.jpg undistort -0.2
```

---

## Command: warp_perspective

## Arguments:

- \_x-angle, \_y-angle, \_zoom

## Description:

Perspective correction. Equivalent to Lightroom’s "Upright" or "Geometry" tools, used to fix leaning buildings or keystone effects.

```
gmic image.jpg warp_perspective 2,0,1.2
```

---

## Command: vignette

## Arguments:

- \_strength, \_radius_min, \_radius_max

## Description:

Adds a vignette effect. Corresponds to Lightroom’s "Post-Crop Vignetting" in the Effects panel.

```
gmic image.jpg vignette 80,70,95
```

---

# 5. Local Adjustments (Masking)

## Command: apply_mask

## Arguments:

- "command", [mask_image]

## Description:

Applies a specific command only within a masked area. This simulates Lightroom’s local adjustment brushes or gradients (Linear/Radial masks).

```
gmic image.jpg (400,400,1,1,"y/h") -normalize. 0,1 +apply_mask.. "adjust_colors 20",[-1]
```

---

## Command: luminance

## Description:

Converts the color image to a grayscale intensity map. Essential for creating "Luminance Range Masks" to target adjustments specifically to highlights or shadows.

```
gmic image.jpg +luminance
```
