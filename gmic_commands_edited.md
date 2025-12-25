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

## Command: clut

## Arguments:

- "clut_name"

## Description:

Applies a Color Look-Up Table. This is the G'MIC equivalent of Lightroom Presets or Film Simulations. It includes hundreds of profiles for classic stocks like Kodak and Fuji.

## 1. Professional Film Simulations (Color)

These simulate actual analog film stocks, widely used for professional photography.

| CLUT Name                        | Description                                                    |
| :------------------------------- | :------------------------------------------------------------- |
| `agfa_apx_25`                    | High contrast, fine grain Agfa film look.                      |
| `agfa_precisa_100`               | Vibrant slide film with saturated blues and greens.            |
| `agfa_vista_200`                 | Classic consumer film with warm, nostalgic tones.              |
| `fuji_160c`                      | Professional portrait film with cool shadows and soft skin.    |
| `fuji_400h`                      | The "wedding look": airy, bright, and pastel greens.           |
| `fuji_800z`                      | High-speed film with vivid colors and slightly magenta skin.   |
| `fuji_astia_100f`                | Soft contrast and faithful skin tone reproduction.             |
| `fuji_fp_100c`                   | Simulation of the classic Fuji instant pull-apart film.        |
| `fuji_provia_100f`               | Standard transparency film with natural, balanced colors.      |
| `fuji_superia_400`               | Versatile consumer film with a slight green tint in shadows.   |
| `fuji_velvia_50`                 | Ultra-high saturation; the gold standard for landscapes.       |
| `fuji_xtrans_iii_classic_chrome` | Muted colors, hard contrast, documentary feel.                 |
| `kodak_ektar_100`                | Extremely fine grain and high saturation for nature.           |
| `kodak_ektachrome_100_vs`        | Vivid Saturation (VS) slide film for punchy colors.            |
| `kodak_gold_200`                 | Warm, golden-hour hues; quintessential family photo look.      |
| `kodak_kodachrome_64`            | Rich reds and deep blacks; iconic National Geographic look.    |
| `kodak_portra_160`               | Fine grain, very natural and smooth skin tones.                |
| `kodak_portra_400`               | **Most Popular.** Perfect balance of saturation and skin tone. |
| `kodak_portra_800`               | Saturated, warm, and works well for low light.                 |
| `kodak_tri-x_400`                | High contrast, gritty, and classic black and white.            |

## 2. Cinematic Movie Looks

Styles based on famous films or grading techniques used in cinema.

| CLUT Name                 | Description                                                    |
| :------------------------ | :------------------------------------------------------------- |
| `1917`                    | Desaturated, earthy, and gritty war-film aesthetic.            |
| `ad_astra`                | Deep space blues and high contrast industrial tones.           |
| `avengers_endgame`        | High contrast, modern superhero blockbuster grade.             |
| `blade_runner`            | Cyberpunk palette: neon pinks, cyans, and deep shadows.        |
| `bleach_bypass`           | High contrast, low saturation; creates a harsh, metallic look. |
| `classic_teal_and_orange` | **Essential.** Teal shadows and orange skin tones.             |
| `cineblue`                | Deep cinematic blues for a cold, nighttime feel.               |
| `cinema_noir`             | Gritty, high-contrast monochrome movie style.                  |
| `dunkirk`                 | Desaturated, cold, and heavy atmospheric look.                 |
| `fight_club`              | Sallow greens and yellow-tinted midtones.                      |
| `ford_v_ferrari`          | Vibrant, warm, 60s-inspired racing colors.                     |
| `inception`               | Neutral but heavy cinematic tones with clean whites.           |
| `joker`                   | Depressing greens, purples, and high-contrast shadows.         |
| `mad_max_fury_road`       | Intense saturation: bright oranges and deep desert blues.      |
| `matrix`                  | Famous digital green tint used throughout the film.            |
| `moonlight`               | Surreal deep blues and low-exposure aesthetic.                 |
| `parasite`                | Realistic but slightly cold and moody Korean drama look.       |
| `sicario`                 | Hot, dusty, high-contrast desert atmosphere.                   |
| `the_dark_knight`         | Cold, clinical blues and deep blacks.                          |
| `top_gun_maverick`        | Saturated, warm, high-action sunny aesthetic.                  |

## 3. Black & White (Monochrome)

Professional monochrome conversions and darkroom simulations.

| CLUT Name               | Description                                              |
| :---------------------- | :------------------------------------------------------- |
| `agfa_apx_100`          | Standard, well-balanced monochrome film.                 |
| `black_white_01`        | High contrast punchy B&W.                                |
| `black_white_06`        | Soft, high-key monochrome for portraits.                 |
| `fuji_neopan_acros_100` | Rich blacks and excellent highlight detail.              |
| `ilford_delta_100`      | Clean, modern, high-detail monochrome.                   |
| `ilford_hp5`            | Classic documentary B&W with a wide gray range.          |
| `ilford_pan_f_plus_50`  | Extremely high contrast with deep, crushed blacks.       |
| `kodak_t-max_400`       | Professional fine-grain B&W with linear response.        |
| `kodak_tri-x_400`       | Legendary news/street photography film; gritty and bold. |
| `rollei_retro_80s`      | High contrast, infrared-like sensitivity.                |
| `sepia`                 | Warm, brownish-red antique conversion.                   |
| `zilverfx_vintage_bw`   | Simulates aged, slightly yellowed B&W prints.            |

## 4. Vintage, Retro & Instant

Aesthetic looks based on old tech, instant cameras, and cross-processing.

| CLUT Name            | Description                                              |
| :------------------- | :------------------------------------------------------- |
| `60s_faded`          | Muted colors and low contrast 1960s photo look.          |
| `analog_film_1`      | Warm, slightly grainy analog camera simulation.          |
| `cross_process_cp_3` | High contrast with heavy blue/green color shifts.        |
| `expired_fade`       | Simulates an old photo that has sat in the sun too long. |
| `expired_polaroid`   | Greenish-yellow color shifts and faded blacks.           |
| `faded_analog`       | Dreamy, low-contrast, matte-finish look.                 |
| `faded_retro_01`     | Warm vintage look with lifted (gray) blacks.             |
| `lomo`               | High contrast, vignetted, saturated toy camera look.     |
| `polaroid_669`       | Classic cool-toned instant film simulation.              |
| `polaroid_px-70`     | Soft, warm, and creamy instant film aesthetic.           |
| `retro_brown_01`     | Heavy brown/orange tint for a historical feel.           |
| `vintage_05`         | Blue-tinted shadows and warm highlights (Split toning).  |

## 5. Modern Styles & Color Grading

Contemporary filters for social media and specific lighting conditions.

| CLUT Name              | Description                                          |
| :--------------------- | :--------------------------------------------------- |
| `aqua_and_orange_dark` | Darker, moodier version of Teal & Orange.            |
| `autumn`               | Boosts oranges and yellows; great for forest photos. |
| `bright_warm`          | High-key, sunny, and inviting warm tones.            |
| `cold_ice`             | Strong blue shift for winter and snowy scenes.       |
| `dark_orange_teal`     | Muted tones with a punchy orange/teal contrast.      |
| `deep_blue`            | Enhances sky and ocean colors significantly.         |
| `earth_tone_boost`     | Enhances browns, greens, and natural colors.         |
| `golden_bright`        | Warm, bright, and airy look.                         |
| `landscape_01`         | Enhances dynamic range and saturation for outdoors.  |
| `magenta_dream`        | Dreamy, purple-tinted aesthetic.                     |
| `natural_vivid`        | Boosts saturation without looking "overdone."        |
| `night_view`           | Enhances neon lights and deepens night skies.        |
| `portrait`             | Softens skin and emphasizes warm tones.              |
| `saturated_blue`       | Heavy emphasis on blue channels; very punchy.        |
| `sunset_aqua_orange`   | Simulates the colors of a vibrant beach sunset.      |
| `urban_03`             | Desaturated, high-contrast look for city streets.    |
| `vibrant`              | General-purpose saturation and contrast boost.       |
| `warm_fade`            | Warm tones with a matte, low-contrast finish.        |

## 6. Artistic & Specialty

Unique color mappings for specific creative needs.

| CLUT Name           | Description                                              |
| :------------------ | :------------------------------------------------------- |
| `anime`             | Bright colors and high-key shadows for an animated look. |
| `faux_infrared`     | Simulates the look of Aerochrome (Red leaves).           |
| `futuristicbleak_1` | Desaturated, cold, and dystopian atmosphere.             |
| `low_key_01`        | Keeps only the highlights; very dark and moody.          |
| `modern_film`       | A hybrid look of digital sharpness and film colors.      |
| `neon_770`          | High-saturation neon grading.                            |
| `only_red`          | Desaturates everything except red objects.               |
| `solarized_color`   | Partial color inversion for an avant-garde look.         |
| `subtle_yellow`     | Gives a light, clean, "Old Paper" tint.                  |
| `underwater`        | Removes red cast to fix colors for scuba photos.         |

---

### Tips for use:

- **For Landscapes:** Try `fuji_velvia_50`, `agfa_precisa_100`, or `sunset_aqua_orange`.
- **For Portraits:** Try `kodak_portra_400`, `fuji_400h`, or `portrait`.
- **For Street Photography:** Try `fuji_xtrans_iii_classic_chrome`, `kodak_tri-x_400`, or `urban_03`.
- **For Cinema Fans:** Try `classic_teal_and_orange`, `blade_runner`, or `joker`.


## Critical Usage Rule:

To actually apply the color effect to the user's image, you **MUST** append `+map_clut[0] [1]` immediately after generating the clut.

**Syntax Pattern:**
`clut PRESET_NAME +map_clut[0] [1]`

**Explanation of the stack logic:**

1. Start: `[0]` (Original Image)
2. Command `clut summer`: Generates CLUT. Stack becomes `[0] Original, [1] CLUT`.
3. Command `+map_clut[0] [1]`: Maps the colors of [1] onto [0] and creates a NEW result (`+`).
4. End Stack: `[0] Original, [1] CLUT, [2] Result`.
5. This ensures the final output is the colorized image.


```
gmic image.jpg clut fuji_provia_100f
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
