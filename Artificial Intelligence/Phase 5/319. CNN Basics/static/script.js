// ==========================================================
// Image Preview
// ==========================================================

const imageInput = document.getElementById("image");

const previewContainer = document.getElementById("preview-container");

const previewImage = document.getElementById("preview-image");

const form = document.querySelector("form");

const button = document.querySelector(".predict-btn");

if(imageInput){

    imageInput.addEventListener(

        "change",

        function(){

            const file = this.files[0];

            if(!file){

                previewContainer.style.display = "none";

                return;

            }

            const allowedTypes = [

                "image/png",

                "image/jpeg",

                "image/jpg"

            ];

            if(!allowedTypes.includes(file.type)){

                alert(

                    "Please upload a PNG, JPG or JPEG image."

                );

                imageInput.value = "";

                previewContainer.style.display = "none";

                return;

            }

            const reader = new FileReader();

            reader.onload = function(event){

                previewImage.src = event.target.result;

                previewContainer.style.display = "flex";

            };

            reader.readAsDataURL(file);

        }

    );

}

// ==========================================================
// Disable Button While Predicting
// ==========================================================

if(form){

    form.addEventListener(

        "submit",

        function(){

            button.disabled = true;

            button.innerHTML = "Predicting...";

        }

    );

}

// ==========================================================
// Auto Scroll to Result
// ==========================================================

const result = document.querySelector(".result-card");

if(result){

    result.scrollIntoView(

        {

            behavior:"smooth",

            block:"center"

        }

    );

}