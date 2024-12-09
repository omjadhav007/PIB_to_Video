# **Automated Video Generation from PIB Press Releases**

This project automates the process of extracting data, summarizing content, generating speech, and creating a synchronized video featuring a 2D animated avatar.

---

## **Overview**

The project workflow consists of the following steps:

1. **Web Scraping**: Scrape press release data from the PIB website using `BeautifulSoup`.  
2. **Text Summarization**: Summarize the extracted data using the `T5-Large` model.  
3. **Audio Generation**: Generate natural-sounding speech using the `Tacotron 2` model.  
4. **Phoneme-to-Viseme Mapping**: Use Whisper to extract word timings and map phonemes to corresponding avatar image paths stored in a `.txt` file.  
5. **Video Creation (Without Audio)**: Create a video sequence from phoneme-mapped images using `FFmpeg`.  
6. **Combine Audio and Video**: Synchronize the generated video with audio using `MoviePy`.

---

## **Features**

- **Automated Content Extraction**: Scrapes press releases from the PIB website.  
- **Concise Summarization**: Summarizes lengthy text using the `T5-Large` model for easy understanding.  
- **Natural Speech Generation**: Generates high-quality speech with the `Tacotron 2` model.  
- **Avatar Animation**:  
   - Extracts word-level timings using **Whisper**.  
   - Maps phonemes to avatar image paths.  
   - Creates video sequences from images using **FFmpeg**.  
- **Audio-Video Integration**: Combines audio and video seamlessly using **MoviePy**.

---

## **Tech Stack**

The following tools and technologies are used in the project:

- **Web Scraping**: `BeautifulSoup`, `Requests`  
- **Text Summarization**: Hugging Face Transformers (`T5-Large`)  
- **Audio Generation**: `Tacotron 2` (Text-to-Speech), PyTorch  
- **Phoneme Mapping**: OpenAI Whisper for word timings  
- **Video Creation**:  
   - **FFmpeg** for generating video sequences without audio.  
   - **MoviePy** for combining video and audio.

---

## **System Workflow**

1. **Data Extraction**:  
   Scrape the PIB website to collect press release content.

2. **Summarization**:  
   The T5-Large model summarizes the scraped content.

3. **Audio Generation**:  
   Convert the summarized text into speech using the Tacotron 2 model.

4. **Phoneme Mapping**:  
   - Extract word timings from the audio using Whisper.  
   - Map each phoneme to its corresponding 2D avatar image (stored in a `.txt` file).

5. **Video Creation**:  
   - Use FFmpeg to create a video sequence without audio based on the phoneme-mapped image paths.  
   - Add the generated audio to the video using MoviePy.

---

## **Setup Instructions**

Follow these steps to set up and run the project:

### **Prerequisites**

- Python 3.8+  
- FFmpeg (ensure it’s installed and added to the system PATH)  
- Required Python Libraries:  
  - `beautifulsoup4`  
  - `requests`  
  - `transformers`  
  - `pytorch`  
  - `openai-whisper`  
  - `moviepy`  

### **Installation**

1. Clone the repository:  
   ```bash
   git clone https://github.com/omjadhav007/PIB_to_Video
   cd PIB_to_Video
   ```

2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure FFmpeg is installed:  
   - Download FFmpeg from [ffmpeg.org](https://ffmpeg.org).  
   - Add it to your system PATH.

4. Download pre-trained models:  
   - T5-Large (Hugging Face Transformers)  
   - Tacotron 2 (PyTorch Implementation)  
   - Whisper (OpenAI Model)  

---

## **Execution**

Run the main script to automate the workflow:  

```bash
python run.py
```

This script will:

1. Scrape PIB data.  
2. Summarize text.  
3. Generate speech audio.  
4. Extract word timings and map phonemes.  
5. Create video without audio using FFmpeg.  
6. Combine video and audio using MoviePy.  

---

## **Output**

The output includes:  

- **Audio File**: Generated from summarized text.  
- **Video File**: Avatar animation synchronized with audio.  

---

<!-- ## **Demo**

- Sample Video:  
  [Link to your demo video or screenshots] -->

---

## **Future Enhancements**

- Integrate 3D avatars for advanced animations.  
- Add support for multiple languages.  
- Automate publishing videos to platforms like YouTube.

---

## **Contributors**

- **Om Jadhav**
