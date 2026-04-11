---
name: annotate
description: >
  Annotate an image by drawing rectangles, circles, arrows, or text on it using ImageMagick.
  Use this skill when the user asks to highlight, encircle, frame, annotate, mark up, or draw
  attention to a specific part of an image or screenshot. Also trigger when the user says things
  like "encadre cette partie", "highlight the table", "circle the button", "add an arrow pointing
  to X", or "put a red box around Y". Requires ImageMagick installed on the system.
version: 1.0.0
---

# Annotate Skill

Draw annotations (rectangles, circles, arrows, text) on images using ImageMagick.
Highlight specific parts of screenshots or any image.

---

## Prerequisites

- ImageMagick 7+ installed

### Auto-install (runs once if `magick` is not found)

**Windows:**
```bash
winget install ImageMagick.ImageMagick --accept-source-agreements --accept-package-agreements
```

**macOS:**
```bash
brew install imagemagick
```

**Linux (Debian/Ubuntu):**
```bash
sudo apt-get install -y imagemagick
```

After install, verify:
```bash
magick --version
```

If `magick` is not in PATH on Windows, use:
```bash
export PATH="/c/Program Files/ImageMagick-7.1.2-Q16-HDRI:$PATH"
```

---

## Workflow

### Step 1 — Check ImageMagick and auto-install if needed

```bash
magick --version 2>/dev/null || echo "NOT_INSTALLED"
```

If `NOT_INSTALLED`, detect the OS and run the appropriate install command from Prerequisites above.
Do NOT ask the user — just install it automatically.

### Step 2 — Identify the image and annotation request

1. Confirm the user has provided an image path or a recently captured screenshot.
2. Get the image dimensions:
   ```bash
   magick identify "IMAGE_PATH"
   ```
3. Understand what the user wants to highlight. If they say a vague location like "top right" or "the table", **view the image first** with the Read tool to identify pixel coordinates.

### Step 3 — Map regions to coordinates

Use the image dimensions to estimate coordinates based on the user's description:

| User says | Coordinates (for 1280x1920 image) |
|-----------|-----------------------------------|
| "top left" | `rectangle 20,20 400,300` |
| "top right" | `rectangle 880,20 1260,300` |
| "center" | `rectangle 340,560 940,1160` |
| "bottom half" | `rectangle 20,960 1260,1900` |
| "the table" | View the image, find the table bounds |

For precise annotations, always **view the image first** with the Read tool.

### Step 4 — Apply the annotation

The output filename should be the input filename with `_annotated` appended before the extension.

**Red rectangle (most common):**
```bash
magick "INPUT.png" -stroke red -strokewidth 4 -fill none \
  -draw "rectangle X1,Y1 X2,Y2" "OUTPUT.png"
```

**Multiple rectangles:**
```bash
magick "INPUT.png" -stroke red -strokewidth 4 -fill none \
  -draw "rectangle X1,Y1 X2,Y2" \
  -draw "rectangle X3,Y3 X4,Y4" "OUTPUT.png"
```

**Circle:**
```bash
magick "INPUT.png" -stroke red -strokewidth 4 -fill none \
  -draw "circle CX,CY CX,CY+RADIUS" "OUTPUT.png"
```

**Arrow (line with arrowhead):**
```bash
magick "INPUT.png" -stroke red -strokewidth 3 -fill red \
  -draw "line X1,Y1 X2,Y2" \
  -draw "polygon X2,Y2 X2-10,Y2-10 X2+10,Y2-10" "OUTPUT.png"
```

**Text label:**
```bash
magick "INPUT.png" -stroke none -fill red -pointsize 36 \
  -annotate +X+Y "Label text" "OUTPUT.png"
```

**Custom color:** Replace `red` with any color: `blue`, `green`, `yellow`, `#FF6600`, etc.

**Custom stroke width:** Adjust `-strokewidth` (2 for thin, 6 for thick).

### Step 5 — Combine annotations

You can chain multiple annotations in one command:
```bash
magick "INPUT.png" \
  -stroke red -strokewidth 4 -fill none -draw "rectangle 30,100 400,300" \
  -stroke blue -strokewidth 3 -fill none -draw "circle 640,500 640,550" \
  -stroke none -fill red -pointsize 28 -annotate +420+95 "Important!" \
  "OUTPUT.png"
```

### Step 6 — View and report

1. Use the Read tool to visually verify the annotation.
2. Report the file path and what was annotated.

---

## Response format

```
Image annotated!

Location: /path/to/OUTPUT_annotated.png

Annotations: [Description of what was highlighted]
```
