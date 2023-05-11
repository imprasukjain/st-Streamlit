# st-Streamlit
# Object Detection using YOLO V5

This project demonstrates object detection using the YOLO V5 algorithm and is hosted on Streamlit. YOLO (You Only Look Once) is a popular real-time object detection algorithm that achieves high accuracy and fast processing speed.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/imprasukjain/st-Streamlit.git
   ```

2. Install the required dependencies using pip:

   ```
   pip install -r requirements.txt
   ```

3. Download the pre-trained YOLO V5 weights from the official repository. Place the weights file `yolov5s.pt` in the project directory.

4. Start the Streamlit server:

   ```
   streamlit run Home.py
   ```

5. Open your browser and navigate to `http://localhost:8501` to access the application.

## Usage

Once the Streamlit server is running and you have accessed the application in your browser, follow these steps to perform object detection:

1. Click on the "Browse" button to upload an image file.

2. Click on the "Detect" button to start the object detection process.

3. The detected objects will be highlighted in the uploaded image or video, along with their respective labels and confidence scores.

## Project Structure

The project repository has the following structure:

- `Home.py`: The main Streamlit application script.
- `requirements.txt`: A text file containing the required Python dependencies.
- `yolov5s.pt`: The pre-trained YOLO V5 weights file (not included in the repository).
- `pages/`: A directory containing different pages for the web application.
- `models/`: A directory containing YOLO V5 model definitions.
- `Uploads/`: A sample image for testing purpose and for storing the images which are given to model as input (In Localhost).

## Contributions

Contributions to this project are welcome. If you find any issues or have suggestions for improvement, feel free to open an issue or submit a pull request on the project's GitHub repository.
I am looking for a person who can help me to deploy this web application for real time object detection also, Currently there are some issues in streamlit community server and there is no fix for that.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
