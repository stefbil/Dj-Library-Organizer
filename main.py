import os
import shutil
import librosa
import numpy as np
from tqdm import tqdm

VALID_KEYS = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

MAJOR_TO_RELATIVE_MINOR = {
    "A": "F#",
    "A#": "G",
    "B": "G#",
    "C": "A",
    "C#": "A#",
    "D": "B",
    "D#": "C",
    "E": "C#",
    "F": "D",
    "F#": "D#",
    "G": "E",
    "G#": "F"
}

# Major and minor profiles (based on intervals)
MAJOR_PROFILE = np.array([6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88])
MINOR_PROFILE = np.array([6.33, 2.68, 3.52, 5.38, 2.60, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17])

def detect_key_and_mode(file_path):
    try:
        y, sr = librosa.load(file_path, sr=None)
        chroma = librosa.feature.chroma_stft(y=y, sr=sr)
        chroma_sum = np.sum(chroma, axis=1)
        chroma_sum = chroma_sum / np.max(chroma_sum)
        major_corr = np.correlate(chroma_sum, MAJOR_PROFILE, mode='full')
        minor_corr = np.correlate(chroma_sum, MINOR_PROFILE, mode='full')

        if np.max(major_corr) > np.max(minor_corr):
            mode = "major"
        else:
            mode = "minor"
        key_index = np.argmax(chroma_sum)
        detected_key = VALID_KEYS[key_index]

        return detected_key, mode
    
    except Exception as e:
        print(f"Error detecting key for {file_path}: {e}")
        return None, None

def get_key(file_path):
    detected_key, mode = detect_key_and_mode(file_path)

    if detected_key is None:
        return None
    # if  key is major convert it to relative minor
    if mode == "major":
        detected_key = MAJOR_TO_RELATIVE_MINOR.get(detected_key, detected_key)

    return detected_key

def organize_music_library(library_path, sorted_path):
    if not os.path.exists(sorted_path):
        os.makedirs(sorted_path)

    files_to_process = []
    for root, dirs, files in os.walk(library_path):
        for file in files:
            if file.endswith(".mp3", ".wav", ".flac"):
                files_to_process.append(os.path.join(root, file))

    for file_path in tqdm(files_to_process, desc="Processing files", unit="file"):
        key = get_key(file_path)
        if key is None:
            print(f"No key found for {file_path}, skipping.")
            continue
        
        key_dir = os.path.join(sorted_path, key)
        if not os.path.exists(key_dir):
            os.makedirs(key_dir)
        
        new_file_path = os.path.join(key_dir, os.path.basename(file_path))
        shutil.copy2(file_path, new_file_path)  # Use copy2 to preserve metadata
        print(f"Copied: {file_path} to {new_file_path}")

if __name__ == "__main__":
    MUSIC_LIBRARY_PATH = input("Enter the path to your music library: ").strip()
    SORTED_LIBRARY_PATH = input("Enter the path where you want to store the sorted music: ").strip()

    if not os.path.exists(MUSIC_LIBRARY_PATH):
        print(f"The specified music library path does not exist: {MUSIC_LIBRARY_PATH}")
    elif not os.path.exists(SORTED_LIBRARY_PATH):
        print(f"The specified sorted directory does not exist. Creating it now: {SORTED_LIBRARY_PATH}")
        os.makedirs(SORTED_LIBRARY_PATH)

    organize_music_library(MUSIC_LIBRARY_PATH, SORTED_LIBRARY_PATH)