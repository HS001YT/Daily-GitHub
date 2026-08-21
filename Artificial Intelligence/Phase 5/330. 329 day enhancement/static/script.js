const imageInput = document.getElementById("image");

const dropZone = document.getElementById("dropZone");

const previewContainer =
    document.getElementById("previewContainer");

const imagePreview =
    document.getElementById("imagePreview");

const fileName =
    document.getElementById("fileName");

const fileSize =
    document.getElementById("fileSize");

const uploadForm =
    document.getElementById("uploadForm");

const classifyBtn =
    document.getElementById("classifyBtn");

const buttonText =
    document.getElementById("buttonText");

const loader =
    document.getElementById("loader");

const resetBtn =
    document.getElementById("resetBtn");


function showPreview(file) {

    if (!file) {
        return;
    }


    const allowedTypes = [
        "image/jpeg",
        "image/png",
        "image/webp"
    ];


    if (!allowedTypes.includes(file.type)) {

        alert(
            "Please select a JPG, JPEG, PNG or WEBP image."
        );

        resetUpload();

        return;
    }


    const maxSize = 5 * 1024 * 1024;


    if (file.size > maxSize) {

        alert(
            "Image size must be less than 5 MB."
        );

        resetUpload();

        return;
    }


    const reader = new FileReader();


    reader.onload = function (event) {

        imagePreview.src =
            event.target.result;

        fileName.textContent =
            file.name;

        fileSize.textContent =
            formatFileSize(file.size);

        previewContainer.classList.add(
            "show"
        );

    };


    reader.readAsDataURL(file);
}


function formatFileSize(bytes) {

    if (bytes < 1024) {

        return bytes + " B";
    }


    if (bytes < 1024 * 1024) {

        return (
            (bytes / 1024).toFixed(1)
            + " KB"
        );
    }


    return (
        (bytes / (1024 * 1024)).toFixed(2)
        + " MB"
    );
}


function resetUpload() {

    imageInput.value = "";

    imagePreview.src = "";

    fileName.textContent =
        "Selected image";

    fileSize.textContent =
        "0 KB";

    previewContainer.classList.remove(
        "show"
    );

    dropZone.classList.remove(
        "dragging"
    );
}


imageInput.addEventListener(
    "change",
    function () {

        const file =
            imageInput.files[0];

        showPreview(file);
    }
);


dropZone.addEventListener(
    "dragover",
    function (event) {

        event.preventDefault();

        dropZone.classList.add(
            "dragging"
        );
    }
);


dropZone.addEventListener(
    "dragleave",
    function () {

        dropZone.classList.remove(
            "dragging"
        );
    }
);


dropZone.addEventListener(
    "drop",
    function (event) {

        event.preventDefault();

        dropZone.classList.remove(
            "dragging"
        );


        const file =
            event.dataTransfer.files[0];


        if (!file) {
            return;
        }


        const dataTransfer =
            new DataTransfer();

        dataTransfer.items.add(file);

        imageInput.files =
            dataTransfer.files;


        showPreview(file);
    }
);


resetBtn.addEventListener(
    "click",
    function () {

        resetUpload();
    }
);


uploadForm.addEventListener(
    "submit",
    function (event) {

        if (!imageInput.files.length) {

            event.preventDefault();

            alert(
                "Please select an image first."
            );

            return;
        }


        classifyBtn.disabled = true;

        buttonText.textContent =
            "Classifying...";

        loader.classList.add(
            "show"
        );
    }
);