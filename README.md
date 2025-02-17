---

# Music Library Organizer

## Overview

The **Music Library Organizer** is a Python-based tool designed to help DJs and music enthusiasts organize their music libraries efficiently. The script analyzes audio files in a specified directory, detects the musical key (and whether it's major or minor), and organizes the files into folders based on the detected keys.

If a major key is detected, the script automatically converts it to its relative minor key, ensuring that all files are organized under minor keys for consistency during DJ performances.

## Features

- **Key Detection**: Automatically detects the musical key of each track using chroma features extracted via the `librosa` library.
- **Major to Minor Conversion**: Converts major keys to their relative minor equivalents for consistent organization.
- **File Organization**: Copies files into folders named after their detected minor keys (e.g., `A`, `F#`, `G`, etc.).

## How It Works

1. **Key Detection**:
   - The script uses chroma features to analyze the pitch content of each audio file.
   - It determines whether the key is major or minor by comparing the chroma features against predefined major and minor profiles.
   - If the key is major, it is converted to its relative minor.

2. **File Organization**:
   - Files are copied (not moved) into folders named after their detected minor keys.
   - For example, a song in **C major** will be placed in the **A** folder (its relative minor).

3. **Progress Tracking**:
   - A progress bar is displayed to indicate the status of file processing, making it easy to track how many files have been processed.

## Requirements

- **Python 3.x**
- Required Python libraries:
  - `librosa` (for audio analysis)
  - `numpy` (for numerical operations)
  - `tqdm` (for progress bar visualization)

You can install the required libraries using pip:

```bash
pip install librosa numpy tqdm
```

## Usage

1. Run the script and provide the following inputs when prompted:
   - **Source Directory**: The path to your unorganized music library.
   - **Destination Directory**: The path where you want the sorted music files to be stored.

2. The script will process each file, detect its key, convert major keys to their relative minors, and copy the files into appropriately named folders.

## Future Enhancements

- **BPM Detection**: Optionally detect and organize files by BPM (beats per minute).
- **Parallel Processing**: Speed up key detection for large libraries using parallel processing.
- **Customizable Profiles**: Allow users to define custom major/minor profiles for improved accuracy.

## License

This project is open-source and available under the MIT License. Feel free to modify and adapt it to suit your needs!

---

### Notes

- This tool is particularly useful for DJs who need to quickly find tracks in specific keys for harmonic mixing.
- The script currently supports `.mp3` files, but it can be extended to handle other formats like `.flac` or `.wav`.

---
