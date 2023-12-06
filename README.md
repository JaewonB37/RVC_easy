# Simplified RVC Project

This project aims to simplify the process of training and inference in the Robust Voice Conversion (RVC) framework. It provides an intuitive workflow for users to train with their chosen audio files, perform voice conversion, and save the results. The project is structured into three main stages:

## 1. Selecting Files for Training
Users can select a directory containing the audio files they wish to train on. The process is as follows:
1. **Conversion to WAV Format**: All files in the selected directory are automatically converted to the `.wav` format.
2. **Background Music Removal**: The background music (MR) is removed from the training files.
3. **Training Process**: The files are then used in the training process to develop the voice conversion model.

## 2. Choosing Files for Inference
The inference stage involves the following steps:
1. **File Selection**: Users select the file they wish to use for inference.
2. **Pitch Adjustment**: The pitch of the selected file is adjusted to match the pitch of the trained voice.
3. **Music Removal**: The background music (MR) is separated from the inference file.
4. **Voice Conversion**: The voice conversion process is applied to the file.
5. **Recombination**: The background music is recombined with the converted voice file.

## 3. Selecting Output Directory
After the voice conversion, the following step is taken:
1. **Saving the Results**: Users can choose a directory where the final output will be saved.

### Getting Started
To get started with this project, clone the repository and follow the instructions in the documentation to set up the necessary environment and dependencies.

### Contributions
Contributions to this project are welcome. Please refer to the contribution guidelines for more information on how to contribute.


## Reference
Retrieval-based-Voice-Conversion-WebUI (https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI)
We would like to thank those who created or contributed to related projects.
