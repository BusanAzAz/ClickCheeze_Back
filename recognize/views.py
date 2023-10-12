from django.shortcuts import render
from django.http import HttpResponse
from forms import ImageUploadForm
import cv2
import numpy as np
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

from .utils.Visualization import visualize


def detect_faces(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']

            # STEP 2: Create a FaceDetector object.
            base_options = python.BaseOptions(model_asset_path='detector.tflite')
            options = vision.FaceDetectorOptions(base_options=base_options)
            detector = vision.FaceDetector.create_from_options(options)

            # STEP 3: Load the input image.
            image_data = image.read()
            image = mp.Image(input_data=image_data)

            # STEP 4: Detect faces in the input image.
            detection_result = detector.detect(image)

            # STEP 5: Process the detection result and visualize it.
            image_copy = np.copy(image.numpy_view())
            annotated_image = visualize(image_copy, detection_result)
            rgb_annotated_image = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)

            return render(request, 'result.html', {'image': rgb_annotated_image})
    else:
        form = ImageUploadForm()
    return render(request, 'upload.html', {'form': form})
