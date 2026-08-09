// ==========================================================
// CIFAR-10 Image Classifier
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


// ==========================================================
// Allowed File Types
// ==========================================================

const allowedTypes = [

    "image/jpeg",

    "image/png",

    "image/webp"

];


// ==========================================================
// Image Selection
// ==========================================================

imageInput.addEventListener(

    "change",

    function () {

        const file = this.files[0];


        // --------------------------------------------------
        // No File Selected
        // --------------------------------------------------

        if (!file) {

            previewContainer.style.display = "none";

            previewImage.src = "";

            return;

        }


        // --------------------------------------------------
        // Validate File Type
        // --------------------------------------------------

        if (!allowedTypes.includes(file.type)) {

            alert(

                "Please select a JPG, JPEG, PNG or WEBP image."

            );

            this.value = "";

            previewContainer.style.display = "none";

            previewImage.src = "";

            return;

        }


        // --------------------------------------------------
        // Validate File Size
        // --------------------------------------------------

        const maxSize = 10 * 1024 * 1024;


        if (file.size > maxSize) {

            alert(

                "Image size must be less than 10 MB."

            );

            this.value = "";

            previewContainer.style.display = "none";

            previewImage.src = "";

            return;

        }


        // --------------------------------------------------
        // Create Image Preview
        // --------------------------------------------------

        const reader = new FileReader();


        reader.onload = function (event) {

            previewImage.src = event.target.result;

            previewContainer.style.display = "flex";

        };


        reader.readAsDataURL(file);

    }

);


// ==========================================================
// Form Submission
// ==========================================================

const uploadForm = document.querySelector(

    ".upload-form"

);


uploadForm.addEventListener(

    "submit",

    function () {

        // --------------------------------------------------
        // Disable Button
        // --------------------------------------------------

        predictButton.disabled = true;


        // --------------------------------------------------
        // Change Button Text
        // --------------------------------------------------

        predictButton.textContent =

            "Classifying Image...";


        // --------------------------------------------------
        // Add Loading State
        // --------------------------------------------------

        predictButton.style.opacity = "0.7";

    }

);


// ==========================================================
// Reset Button State When Page Loads
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