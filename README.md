<div align = "center">
  <h1>
    Disney Trailer Hub
  </h1>
</div>

The Disney Trailer App is a cross-platform application developed using the KivyMD framework in Python. This app provides information about Disney movies, allows users to explore details, watch trailers, and even predicts Disney characters using a built-in AI component.

<img src = "https://github.com/Omanshu209/Disney-Trailer-Hub-AI/assets/114089324/3efdfb43-1427-4d43-9d54-7c87ba62fc6f" align = "right" width = "500">
</img>

## Features

- **Disney Movie List**
  - Browse a collection of Disney movies with images in a `swiper layout`.
  - Access additional information by clicking on the floating action button with an information icon.

<img src = "https://github.com/Omanshu209/Disney-Trailer-Hub-AI/assets/114089324/e7d5193a-96e7-4634-bea6-a902ed7331e6" align = "left" width = "500">
</img>

- **Movie Info & Trailer**
  - View detailed information about a selected Disney movie, including an image, title, and description.
  - Play the `movie trailer` by clicking on a dedicated button. The choice between webview and webbrowser modules depends on availability.

<img src = "https://github.com/Omanshu209/Disney-Trailer-Hub-AI/assets/114089324/b69bd42f-60a9-477a-a0ff-caa77c620563" align = "right" width = "500">
</img>

- **AI Predictor:**
  - Utilize the device's camera to capture an image.
  - Predict the Disney character in the captured image using a `pre-trained deep learning model`.
  - Display the prediction result in a visually appealing format.

<img src = "https://github.com/Omanshu209/Disney-Trailer-Hub-AI/assets/114089324/1d71c006-e654-4d32-a392-abc0e75cec27" align = "left" width = "500">
</img>

## Requirements

> `Python 3.x`
>
> `Kivy (v2.0.0)`
>
> `KivyMD (v1.1.1)`
>
> `webview-android (v0.10)` (**optional**, for enhanced trailer viewing)
>
> `torch (v1.9.1)`
>
> `torchvision (v0.10.0)`
>
> `PIL (Python Imaging Library)`

<img src = "https://github.com/Omanshu209/Disney-Trailer-Hub-AI/assets/114089324/edb0e353-5313-48ae-a9b3-047337afc1d6" align = "right" width = "500">
</img>

## Installation

1. **Clone** the repository:

    ```bash
    git clone https://github.com/Omanshu209/Disney-Trailer-Hub-AI.git
    ```

2. **Install** dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. **Run** the app:

    ```bash
    python3 main.py
    ```

<img src = "https://github.com/Omanshu209/Disney-Trailer-Hub-AI/assets/114089324/81a03156-e246-4b0a-b1f8-38b35eadb32e" align = "left" width = "500">
</img>

## Usage

- Navigate through the app using the bottom navigation bar:
  - **"Movies"** tab for the Disney Movie List.
  - **"Info & Trailer"** tab for detailed movie information and trailers.
  - **"AI"** tab for the AI Predictor using the device's camera.

## License

This project is licensed under the `MIT License`.

## Credits
- The app and AI were developed by **Omanshu**.
