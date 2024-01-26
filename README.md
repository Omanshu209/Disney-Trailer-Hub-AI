<div align = "center">
  <h1>
    Disney Trailer Hub
  </h1>
</div>

The Disney Trailer App is a cross-platform application developed using the KivyMD framework in Python. This app provides information about Disney movies, allows users to explore details, watch trailers, and even predicts Disney characters using a built-in AI component.

## Features

- **Disney Movie List**
  - Browse a collection of Disney movies with images in a `swiper layout`.
  - Access additional information by clicking on the floating action button with an information icon.

<img src = "https://github.com/Omanshu209/Disney-Trailer-Hub-AI/assets/114089324/aefbcd1e-bc95-4816-b94f-bf56a7c182f3" align = "right" width = "500">
</img>


- **Movie Info & Trailer**
  - View detailed information about a selected Disney movie, including an image, title, and description.
  - Play the `movie trailer` by clicking on a dedicated button. The choice between webview and webbrowser modules depends on availability.

<img src = "https://github.com/Omanshu209/Disney-Trailer-Hub-AI/assets/114089324/b69bd42f-60a9-477a-a0ff-caa77c620563" align = "left" width = "500">
</img>

<img src = "https://github.com/Omanshu209/Disney-Trailer-Hub-AI/assets/114089324/edb0e353-5313-48ae-a9b3-047337afc1d6" align = "right" width = "500">
</img>


- **AI Predictor:**
  - Utilize the device's camera to capture an image.
  - Predict the Disney character in the captured image using a `pre-trained deep learning model`.
  - Display the prediction result in a visually appealing format.

<img src = "https://github.com/Omanshu209/Disney-Trailer-Hub-AI/assets/114089324/fe31925a-518b-463c-8624-b63c76bdd126" align = "left" width = "500">
</img>

<img src = "https://github.com/Omanshu209/Disney-Trailer-Hub-AI/assets/114089324/81a03156-e246-4b0a-b1f8-38b35eadb32e" align = "right" width = "500">
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

## Usage

- Navigate through the app using the bottom navigation bar:
  - **"Movies"** tab for the Disney Movie List.
  - **"Info & Trailer"** tab for detailed movie information and trailers.
  - **"AI"** tab for the AI Predictor using the device's camera.

## License

This project is licensed under the `MIT License`.

## Credits
- The app and AI were developed by **Omanshu**.
