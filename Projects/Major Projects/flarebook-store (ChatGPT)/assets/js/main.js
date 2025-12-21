// LOADER
document.addEventListener("DOMContentLoaded", () => {
    const loader = document.getElementById("loader");
    const home = document.getElementById("home");

    if (!loader) return;

    // Primary removal
    setTimeout(() => {
        loader.style.display = "none";
        home?.classList.remove("hidden");
    }, 1200);

    // Failsafe (for local / asset issues)
    setTimeout(() => {
        loader.style.display = "none";
        home?.classList.remove("hidden");
    }, 3000);
});


// CAPTCHA
const captchaWords = ["banana", "unicorn", "pizza", "flare"];
const captchaText = captchaWords[Math.floor(Math.random() * captchaWords.length)];
document.getElementById("captchaText")?.append("Type: " + captchaText);

// LOGIN
function loginUser() {
    const input = document.getElementById("captchaInput").value;
    if (input !== captchaText) {
        alert("Captcha failed 😜");
        return;
    }
    alert("Login successful (prototype)");
}

// SWITCH FORMS
function showRegister() {
    document.querySelector(".auth-box").classList.add("hidden");
    document.getElementById("registerBox").classList.remove("hidden");
}

function showLogin() {
    document.getElementById("registerBox").classList.add("hidden");
    document.querySelector(".auth-box").classList.remove("hidden");
}

// BUSINESS TOGGLE
document.getElementById("accountType")?.addEventListener("change", (e) => {
    const businessFields = document.getElementById("businessFields");
    e.target.value === "business"
        ? businessFields.classList.remove("hidden")
        : businessFields.classList.add("hidden");
});

function switchTab(type) {
    document.querySelectorAll(".tab").forEach(t => t.classList.remove("active"));
    document.querySelectorAll(".form").forEach(f => f.classList.remove("active"));

    if (type === "login") {
        document.getElementById("loginForm").classList.add("active");
    } else if (type === "person") {
        document.getElementById("personForm").classList.add("active");
    } else {
        document.getElementById("businessForm").classList.add("active");
    }

    event.target.classList.add("active");
}
