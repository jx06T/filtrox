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

# 6. Geometric & Lens Distortions (幾何與鏡頭扭曲)
用於修正透視問題或進行創意形變（例如液化效果）。

## Command: fisheye

## Arguments:
* center_x, center_y, radius, amplitude

## Description:
Simulates a fisheye lens effect or corrects it. It creates a spherical distortion centered on a specific point.

```bash
gmic image.jpg +fisheye 50,50,50,1.5
```

---

## Command: twirl

## Arguments:
* amplitude, center_x, center_y

## Description:
Rotates pixels around a center point, creating a whirlpool effect. Useful for creative abstract edits.

```bash
gmic image.jpg +twirl 1.0,50%,50%
```

---

## Command: deform

## Arguments:
* amplitude, interpolation

## Description:
Applies a random, smooth "liquid" deformation. In photo editing, this can be used to add subtle organic variety or "warp" certain areas.

```bash
gmic image.jpg +deform 10,1
```

---

## Command: spherize

## Arguments:
* radius, strength, center_x, center_y

## Description:
Wraps the image around a 3D sphere shape. Often used to create "crystal ball" effects or to correct bloated lens distortion.

```bash
gmic image.jpg +spherize 50%,1.5,50%,50%
```

---

# 7. Advanced Retouching (進階人像與修復)
這些是專業修圖師在 Lightroom 之外，通常需要到 Photoshop 才能完成的操作。

## Command: split_freq

## Arguments:
* smoothness

## Description:
**Frequency Separation.** Splits the image into "Low Frequency" (colors/tones) and "High Frequency" (texture/details). Essential for high-end skin retouching.

```bash
gmic image.jpg split_freq 2%
```

---

## Command: inpaint

## Arguments:
* [mask]

## Description:
**Content-Aware Fill.** Removes unwanted objects from a photo (like power lines or skin blemishes) by reconstructing the area based on surrounding pixels.

```bash
gmic image.jpg mask.png +inpaint[0] [1]
```

---

## Command: solidify

## Description:
Fills in transparent or "missing" areas of an image with a smooth color gradient based on the edges. Great for fixing edges after a heavy rotation or warp.

```bash
gmic image.jpg +solidify 75%
```

---

# 8. Lighting & Atmospheric Effects (光影與大氣)
用於增加照片的氛圍感（例如光暈、光束）。

## Command: lightrays

## Arguments:
* density, center_x, center_y, ray_length, ray_attenuation

## Description:
**Volumetric Lighting.** Generates "God Rays" or light beams emanating from a light source or bright edges in the photo.

```bash
gmic image.jpg +lightrays 50%,50%,50%,0.9,0.5
```

---

## Command: blur_bloom

## Arguments:
* amplitude, ratio, nb_iter

## Description:
Creates a soft, ethereal glow on the highlights. Similar to using a "Mist" or "Pro-Mist" filter on a lens.

```bash
gmic image.jpg +blur_bloom 1,2,5
```

---

## Command: glow

## Arguments:
* amplitude

## Description:
Adds a romantic, soft-focus glow to the entire image. Popular in wedding and dream-style photography.

```bash
gmic image.jpg +glow 1.5%
```

---

# 9. Texture & Analog Feel (質感與底片感疊加)
增加照片的物質層次感。

## Command: texturize_paper

## Description:
Overlays a realistic paper texture onto the image. Ideal for making digital photos look like printed art.

```bash
gmic image.jpg +texturize_paper
```

---

## Command: texturize_canvas

## Arguments:
* amplitude, fibrousness, emboss_level

## Description:
Simulates a painting on canvas. It adds a woven fiber texture and subtle relief lighting.

```bash
gmic image.jpg +texturize_canvas 20,3,0.6
```

---

## Command: noise

## Arguments:
* amplitude, noise_type

## Description:
**Film Grain.** While technically "noise," using Gaussian noise (type 0) at low amplitudes is the standard way to simulate film grain.

```bash
gmic image.jpg +noise 5,2
```

---

## Command: halftone

## Arguments:
* nb_levels, size_dark, size_bright, shape

## Description:
Converts the image into a "dot" pattern. Used for pop-art styles or newspaper print effects.

```bash
gmic image.jpg +halftone 5,8,8,2
```

---

# 10. Utility & Finishing (實用工具)

## Command: watermark_visible

## Arguments:
* text, opacity, size, angle

## Description:
Adds a visible text watermark. Unlike simple text, this can be blended more naturally with the image values.

```bash
gmic image.jpg +watermark_visible "Copyright 2024",0.3,50,25
```

---

## Command: upscale_smart

## Arguments:
* width, height, smoothness, sharpening

## Description:
**AI Upscaling.** Enlarges an image while attempting to preserve edges and remove pixelation artifacts.

```bash
gmic image.jpg +upscale_smart 200%,200%,2,10
```
---

# 11. Vignetting (暗角)
Used to darken the edges of an image to focus the viewer's attention on the center.

## Command: vignette

## Arguments:
* _strength>=0, 0<=_radius_min<=100, 0<=_radius_max<=100

## Description:
Adds a classic darkening effect to the corners of the image. 
- **Strength**: How dark the corners become.
- **Radius Min/Max**: Defines where the darkening starts and ends (as a percentage of the image size).

```bash
gmic image.jpg +vignette 100,70,90
```

---

# 12. Glow & Bloom (光暈與柔光)
It is used to increase the atmosphere of the picture, especially to make the highlight area exude a dreamy atmosphere.

## Command: glow

## Arguments:
* _amplitude>=0

## Description:
Adds a soft, romantic glow to the entire image. It works by blurring the highlights and blending them back. This is similar to a "Soft Focus" or "Dreamy" filter.

```bash
gmic image.jpg +glow 1.5%
```

---

## Command: blur_bloom

## Arguments:
* _amplitude>=0, _ratio>=0, _nb_iter>=0

## Description:
Creates a more sophisticated cinematic glow (Bloom). It simulates light bleeding from bright sources. 
- **Amplitude**: Intensity of the effect.
- **Ratio/Iter**: Controls the spread and smoothness of the light bleeding.

```bash
gmic image.jpg +blur_bloom 2,2,5
```

---

# 13. Blur (模糊效果)
Simulates blur outside of lens focus, or can be used to add a sense of dynamics.
## Command: blur

## Arguments:
* std_deviation[%]>=0, _boundary_conditions, _kernel

## Description:
General purpose Gaussian blur. Used to soften the entire image or specific parts. 
- **Std_deviation**: The strength of the blur (radius).

```bash
gmic image.jpg +blur 5
```

---

## Command: blur_radial

## Arguments:
* amplitude[%], _center_x[%], _center_y[%]

## Description:
**Zoom/Spin Blur.** Creates a blur that radiates from a center point. It creates a sense of fast movement or explosion towards the viewer.

```bash
gmic image.jpg +blur_radial 2%,50%,50%
```

---

## Command: blur_linear

## Arguments:
* amplitude1[%], _amplitude2[%], _angle

## Description:
**Motion Blur.** Simulates the effect of the camera or the subject moving in a straight line during exposure.
- **Angle**: The direction of the movement (in degrees).

```bash
gmic image.jpg +blur_linear 10,0,45
```

---

## Command: blur_selective

## Arguments:
* sigma>=0, _edges>0, _nb_scales>0

## Description:
**Surface Blur.** Blurs the image while attempting to preserve sharp edges. This is often used for skin smoothing or noise reduction without losing detail.

```bash
gmic image.jpg +blur_selective 5,0.5,5
```