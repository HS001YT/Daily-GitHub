// ==========================================================
// Day 322 - CNN + Data Augmentation
// Frontend JavaScript
// ==========================================================


// ==========================================================
// Get HTML Elements
// ==========================================================

const imageInput = document.getElementById("image");

const previewContainer =
    document.getElementById("preview-container");

const previewImage =
    document.getElementById("preview-image");

const predictButton =
    document.getElementById("predict-button");

const uploadForm =
    document.querySelector(".upload-form");


// ==========================================================
// Allowed File Types
// ==========================================================

const allowedTypes = [

    "image/jpeg",

    "image/png",

    "image/webp"

];


// ==========================================================
// Maximum File Size
// ==========================================================

const MAX_FILE_SIZE = 10 * 1024 * 1024;


// ==========================================================
// Image Selection
// ==========================================================

imageInput.addEventListener(

    "change",

    function () {

        const file = this.files[0];


        // --------------------------------------------------
        // No File
        // --------------------------------------------------

        if (!file) {

            previewContainer.style.display = "none";

            previewImage.src = "";

            return;

        }


        // --------------------------------------------------
        // Check File Type
        // --------------------------------------------------

        if (!allowedTypes.includes(file.type)) {

            alert(

                "Please select a JPG, JPEG, PNG or WEBP image."

            );

            imageInput.value = "";

            previewContainer.style.display = "none";

            previewImage.src = "";

            return;

        }


        // --------------------------------------------------
        // Check File Size
        // --------------------------------------------------

        if (file.size > MAX_FILE_SIZE) {

            alert(

                "Image size must be less than 10 MB."

            );

            imageInput.value = "";

            previewContainer.style.display = "none";

            previewImage.src = "";

            return;

        }


        // --------------------------------------------------
        // Create Preview
        // --------------------------------------------------

        const reader = new FileReader();


        reader.onload = function (event) {

            previewImage.src = event.target.result;

            previewContainer.style.display = "flex";

        };


        reader.onerror = function () {

            alert(

                "Unable to preview this image."

            );

            previewContainer.style.display = "none";

        };


        reader.readAsDataURL(file);

    }

);


// ==========================================================
// Form Submission
// ==========================================================

uploadForm.addEventListener(

    "submit",

    function (event) {

        const file = imageInput.files[0];


        // --------------------------------------------------
        // Check File Again
        // --------------------------------------------------

        if (!file) {

            event.preventDefault();

            alert(

                "Please select an image first."

            );

            return;

        }


        // --------------------------------------------------
        // Disable Button
        // --------------------------------------------------

        predictButton.disabled = true;


        // --------------------------------------------------
        // Loading Text
        // --------------------------------------------------

        predictButton.textContent =

            "Classifying Image...";


        // --------------------------------------------------
        // Visual Loading State
        // --------------------------------------------------

        predictButton.style.opacity = "0.7";

    }

);


// ==========================================================
// Restore Button State
// ==========================================================

window.addEventListener(

    "pageshow",

    function () {

        predictButton.disabled = false;

        predictButton.textContent =

            "Classify Image";

        predictButton.style.opacity = "1";

    }

);