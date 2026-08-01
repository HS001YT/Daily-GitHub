// ==========================================================
// Student Performance Predictor
// ==========================================================

document.addEventListener(

    "DOMContentLoaded",

    function () {

        const form = document.querySelector("form");

        const button = document.querySelector(".predict-btn");

        const result = document.querySelector(".result-card");

        if (form) {

            form.addEventListener(

                "submit",

                function () {

                    button.disabled = true;

                    button.innerHTML = "Predicting...";

                }

            );

        }

        if (result) {

            result.scrollIntoView(

                {

                    behavior: "smooth",

                    block: "center"

                }

            );

        }

        const inputs = document.querySelectorAll(

            "input"

        );

        inputs.forEach(

            function (input) {

                input.addEventListener(

                    "input",

                    function () {

                        if (

                            input.value < 0

                        ) {

                            input.value = "";

                        }

                    }

                );

            }

        );

    }

);