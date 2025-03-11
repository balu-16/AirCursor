# AirCursor #

# 🖐️ Hand Gesture Virtual Mouse 🖱️✨

This Python project implements a virtual mouse controlled by hand gestures using OpenCV, MediaPipe, and autopy. It allows users to interact with their computer without a physical mouse. 🚀

## ✨ Features ✨

* **Hand Tracking:** 🔍 Utilizes MediaPipe for accurate hand tracking and landmark detection. 🎯
* **Virtual Mouse Control:** 🖱️ Moves the mouse cursor based on the position of the index finger. 👆
* **Left Click (Drag):** 🖱️⬅️ Performs a left click and drag when the thumb and index finger touch. 🤏
* **Right Click:** 🖱️➡️ Performs a right click when the thumb and middle finger touch. 🤞
* **FPS Display:** 📊 Shows the frames per second (FPS) on the screen for performance monitoring. 📈
* **Customizable Frame Region:** 🖼️ Defines a specific region within the camera feed for mouse control. 📏
* **Smooth Mouse Movement:** 🌊 Implements smoothing to provide a more natural mouse movement experience. 💫

## ⚙️ Dependencies ⚙️

* **OpenCV (cv2):** 📷 For image processing and camera input.
* **MediaPipe (mediapipe):** ✋ For hand tracking and landmark detection.
* **NumPy (numpy):** 🔢 For numerical operations.
* **autopy:** 💻 For controlling the mouse cursor and clicks.

## 🚀 Getting Started 🚀

### Pre-requisites

* **Python 3.6+:** 🐍 Ensure you have Python 3.6 or a later version installed.
* **Install Dependencies:** 📦 Install the required Python libraries using pip:

    ```bash
    pip install opencv-python mediapipe numpy autopy
    ```

### Usage

1.  **Clone the Repository:** 📂 Clone this repository to your local machine.
2.  **Run the Main Script:** ▶️ Execute the `main.py` script:

    ```bash
    python main.py
    ```

3.  **Hand Gestures:** 👋
    * Move your index finger to move the mouse cursor. 👆
    * Touch your thumb and index finger to perform a left click (drag). 🤏
    * Touch your thumb and middle finger to perform a right click. 🤞
    * Close all fingers to stop dragging. 🖐️

## 📂 Code Structure 📂

* **`main.py`:**
    * This is the main Python script.
    * It handles camera input using OpenCV.
    * It uses MediaPipe to detect hand landmarks.
    * It calculates finger positions and gestures.
    * It controls the mouse cursor and clicks using autopy.
    * It includes the `handDetector` class, which encapsulates hand tracking functionality.
    * It displays the video feed with hand landmarks and FPS.

## 🛠️ Future Improvements 🛠️

* **Gesture Customization:** 🎨 Add more customizable gestures for various actions.
* **Sensitivity Adjustment:** ⚙️ Allow users to adjust mouse sensitivity and smoothing.
* **GUI Interface:** 🖥️ Develop a graphical user interface for easy configuration.
* **More Robust Error Handling:** 🛡️ Improve error handling for camera and input issues.
* **Multi-Monitor Support:** 🌐 Add support for multi-monitor setups.

## 🙌 Contributing 🙌

Contributions are welcome! 🤝 Please feel free to submit pull requests or open issues. 🐛
