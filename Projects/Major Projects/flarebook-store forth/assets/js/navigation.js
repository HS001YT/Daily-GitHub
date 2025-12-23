// ===== GLOBAL NAVIGATION MANAGER =====
class NavigationManager {
    constructor() {
        this.hasShownInitialLoading = false;
        this.currentPage = window.location.pathname;
        
        // Check if we should show loading
        const showLoading = sessionStorage.getItem('showLoading') === 'true';
        const isFirstVisit = !sessionStorage.getItem('hasVisited');
        
        if (isFirstVisit) {
            sessionStorage.setItem('hasVisited', 'true');
        }
        
        // Show loading only on first visit OR login page
        if (this.isLoginPage() || (isFirstVisit && !this.isInternalPage())) {
            this.hasShownInitialLoading = true;
        } else {
            this.skipLoadingScreen();
        }
        
        // Clear the showLoading flag
        if (showLoading) {
            sessionStorage.removeItem('showLoading');
        }
    }

    isLoginPage() {
        return this.currentPage.includes('login.html');
    }

    isInternalPage() {
        return this.currentPage.includes('about.html') || 
               this.currentPage.includes('category.html');
    }

    skipLoadingScreen() {
        const loadingScreen = document.getElementById('loading-screen');
        const mainContent = document.getElementById('main-content');
        
        if (loadingScreen) {
            loadingScreen.style.display = 'none';
        }
        if (mainContent) {
            mainContent.classList.remove('hidden');
        }
    }
}

// Initialize navigation manager
document.addEventListener('DOMContentLoaded', () => {
    // Don't initialize on About/Category pages (they don't have loading screens)
    if (!window.location.pathname.includes('about.html') && 
        !window.location.pathname.includes('category.html')) {
        window.navigationManager = new NavigationManager();
    }
});