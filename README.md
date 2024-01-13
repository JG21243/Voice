# AI Voiceover Script README

## Overview

This Python script offers a comprehensive solution for generating AI voiceovers for uploaded videos. It transforms a video into frames, generates narratives based on these frames using GPT-4 with visual capabilities (GPT4V), converts these narratives into audio, and finally combines the audio with the original video. The script also includes a user-friendly Streamlit interface.

## Features

- **Video Processing**: Converts a video into frames for further analysis.
- **Story Generation**: Utilizes OpenAI's GPT-4 with visual capabilities to generate a narrative script based on video frames.
- **Voiceover Generation**: Transforms text into speech using OpenAI's API.
- **Audio-Video Merging**: Merges the original video with the generated voiceover.
- **Streamlit Interface**: A user-friendly web interface for video uploads, voice type selection, and processed video preview.

## Installation

1. **Install Dependencies**: Make sure Python is installed, then install the necessary libraries: `pip install dotenv moviepy cv2 base64 openai streamlit requests`
2. **API Keys**: An API key from OpenAI is required. This key is to be set in a `.env.local` file.

## Usage

1. **Start the Streamlit Server**: `streamlit run script_name.py`
2. **Using the Web Interface**:
    - Upload your video file.
    - Select the voice type for the voiceover.
    - Provide a prompt for the story generation based on the video.
    - Click "START PROCESSING" to process the video.
3. **Results**: The final video with the AI-generated voiceover will be displayed in the Streamlit interface.

## Code Description

- **dotenv**: Loads API keys from a `.env.local` file.
- **moviepy**: Handles video and audio processing.
- **cv2 (OpenCV)**: Extracts frames from the video.
- **base64, io**: Encodes video frames and manages in-memory audio data.
- **openai**: Interacts with OpenAI's GPT-4 and text-to-speech models.
- **streamlit**: Creates the web interface.
- **tempfile**: Manages temporary files during processing.
- **requests**: Makes requests to the OpenAI API.

## Limitations

- The script currently supports specific video formats only.
- The accuracy of story generation is dependent on the quality of the frames and the capabilities of the GPT model.

## Contributing

Enhancements to improve the script's functionality or efficiency are welcome. Please adhere to standard open-source contribution guidelines.

## License

Specify your licensing terms here (e.g., MIT, GPL, Apache).
