
# Filtrox

Filtrox is a AI-assisted photo grading tool built around Streamlit, Gemini, and Darktable. It generates multiple edit variations, lets you iteratively pick the direction you like, and renders the result by patching Darktable XMP history entries instead of editing pixels directly in Python.

## What it does

- Takes a source image and a text prompt such as "warm cinematic sunset" or "clean bright portrait".
- Uses Gemini to generate multiple grading parameter sets.
- Applies those parameters through Darktable-compatible XMP/module settings.
- Lets you pick a preferred variation and generate the next round of refinements.
- Supports saved filters and batch application workflows in the Streamlit UI.

## Main pieces

- [app.py](/Users/cjtsai/ytp/filtrox/app.py): main Streamlit app.
- [src/photo_editing_agent.py](/Users/cjtsai/ytp/filtrox/src/photo_editing_agent.py): prompt construction and iterative variation logic.
- [src/llm_backend.py](/Users/cjtsai/ytp/filtrox/src/llm_backend.py): Gemini wrapper.
- [src/darktable_processor.py](/Users/cjtsai/ytp/filtrox/src/darktable_processor.py): render bridge.
- [src/xmp_gen.py](/Users/cjtsai/ytp/filtrox/src/xmp_gen.py): XMP patching and Darktable CLI execution.
- [system_prompt.md](/Users/cjtsai/ytp/filtrox/system_prompt.md): editing prompt used for generation.
- [saved_filters/filters.json](/Users/cjtsai/ytp/filtrox/saved_filters/filters.json): saved presets created from the UI.

## Requirements

- Python 3.10+
- [Darktable](https://www.darktable.org/) installed locally
- `darktable-cli` available in your shell, or an explicit path set in `.env`
- A Google Gemini API key

Python packages used by the app:

- `streamlit`
- `pillow`
- `python-dotenv`
- `google-generativeai`

## Setup

Create and activate a virtual environment, then install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install streamlit pillow python-dotenv google-generativeai
```

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
DARKTABLE_CLI_PATH=darktable-cli
```

If `darktable-cli` is not on your `PATH`, set `DARKTABLE_CLI_PATH` to the full executable path.

## Run

Start the Streamlit app:

```bash
streamlit run app.py
```

Then open the local Streamlit URL shown in the terminal.

## Typical workflow

1. Upload or select an image.
2. Enter a style request in natural language.
3. Review the generated variations.
4. Choose the closest result.
5. Iterate again, or give explicit feedback to push the look further.
6. Save a filter if you want to reuse it later.
7. Apply saved or current filters to a batch of images.

The app tracks preferred and disliked factor ranges across iterations so later generations stay closer to your selected direction.

## JSON preset format

Files like [C.json](/Users/cjtsai/ytp/filtrox/C.json), [a.json](/Users/cjtsai/ytp/filtrox/a.json), and [b.json](/Users/cjtsai/ytp/filtrox/b.json) are Darktable-style module presets used by the XMP patching pipeline.

The shape is:

```json
{
  "factors": {
    "exposure": 0.25,
    "temperature": 55,
    "tint": 1.2,
    "vibrance": 21,
    "saturation": 10.5
  },
  "modules": {
    "exposure": {
      "enabled": 1,
      "modversion": 7,
      "params": {
        "exposure": 0.3
      }
    }
  }
}
```

Notes:

- `factors` are the simplified high-level controls used for feedback and iteration.
- `modules` contains the actual Darktable module payloads that get written into XMP history.
- Each module usually includes `enabled`, `modversion`, and `params`.
- The available modules in the sample presets include `exposure`, `sigmoid`, `toneequal`, `temperature`, `diffuse`, and color-related modules such as `colorbalancergb`.

## Output and project data

- Generated sessions are written under [sessions](/Users/cjtsai/ytp/filtrox/sessions).
- Saved filters are stored in [saved_filters/filters.json](/Users/cjtsai/ytp/filtrox/saved_filters/filters.json).
- Sample images and XMP files in the repository are useful as test inputs and reference presets.

## Notes and limitations

- This project depends on external local software and an external API, so failures usually come from one of three places: missing `darktable-cli`, invalid Gemini credentials, or malformed preset/XMP data.
- The current LLM backend is Gemini-only by default.
- The repository does not currently include a pinned `requirements.txt` or automated test suite for the Streamlit app.

## Development ideas

- Add a `requirements.txt` or `pyproject.toml`.
- Add schema validation for preset JSON before render.
- Add smoke tests for XMP generation and CLI rendering.
- Split the Streamlit UI into smaller modules.
