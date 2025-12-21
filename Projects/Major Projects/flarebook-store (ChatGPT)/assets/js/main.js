// ===== GLOBAL FLAREBOOK STORE APP =====
class FlareBookStore {
    constructor() {
        this.init();
    }

    init() {
        // Hide loading screen after delay
        setTimeout(() => {
            this.hideLoadingScreen();
            this.renderHomePage();
        }, 2000);

        this.bindEvents();
    }

    hideLoadingScreen() {
        const loadingScreen = document.getElementById('loading-screen');
        const mainContent = document.getElementById('main-content');
        
        loadingScreen.style.opacity = '0';
        loadingScreen.style.visibility = 'hidden';
        mainContent.classList.remove('hidden');
        
        setTimeout(() => {
            loadingScreen.remove();
        }, 500);
    }

    renderHomePage() {
        const contentDiv = document.getElementById('page-content');
        contentDiv.innerHTML = `
            <div class="home-page">
                <div class="logo-rectangle-placeholder">
                    <div class="flare-logo">
                        <h1>FLAREBOOK STORE</h1>
                        <div class="flare-line"></div>
                        <p class="slogan">IGNITE YOUR MIND</p>
                    </div>
                </div>
                <h2 class="tagline">Discover Books That Spark Your Imagination</h2>
                <p class="subtagline">Explore our curated collection of books across all genres. From classic literature to modern bestsellers, find your next favorite read.</p>
                <button class="enter-button" id="enter-login" onclick="window.location.href='login.html'">
                    Enter Store <i class="fas fa-arrow-right"></i>
                </button>
            </div>
        `;
    }

    bindEvents() {
        // Enter login button
        document.addEventListener('click', (e) => {
            if (e.target.id === 'enter-login' || e.target.closest('#enter-login')) {
                e.preventDefault();
                window.location.href = 'assets/pages/login.html';
            }
        });
    }
}

// Initialize the application
document.addEventListener('DOMContentLoaded', () => {
    new FlareBookStore();
});