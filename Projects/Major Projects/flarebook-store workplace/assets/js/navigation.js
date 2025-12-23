// ===== GLOBAL NAVIGATION MANAGER =====
class NavigationManager {
    constructor() {
        this.hasShownInitialLoading = false;
        this.currentPage = this.getCurrentPage();
        this.init();
    }

    // Get current page name
    getCurrentPage() {
        const path = window.location.pathname;
        
        // Extract page name from path
        const page = path.split('/').pop().replace('.html', '');
        
        // Handle special cases
        if (page === '' || page === 'index' || page.includes('flarebook-store')) {
            return 'home';
        }
        
        return page;
    }

    // Check if current page is login page
    isLoginPage() {
        return this.currentPage === 'login';
    }

    // Check if current page has no loading screen
    isNoLoadingPage() {
        return this.currentPage === 'about' || 
               this.currentPage === 'category' ||
               this.currentPage === 'cart' ||
               this.currentPage === 'wishlist';
    }

    // Initialize the navigation manager
    init() {
        this.handleLoadingScreen();
        this.highlightCurrentPage();
        this.setupNavigation();
        this.setupMobileMenu();
        this.setupSmoothScroll();
        this.setupPageTransitions();
    }

    // ===== LOADING SCREEN MANAGEMENT =====
    handleLoadingScreen() {
        const showLoading = sessionStorage.getItem('showLoading') === 'true';
        const isFirstVisit = !sessionStorage.getItem('hasVisited');
        
        // Mark first visit
        if (isFirstVisit) {
            sessionStorage.setItem('hasVisited', 'true');
        }
        
        // Pages that don't have loading screen
        if (this.isNoLoadingPage()) {
            this.skipLoadingScreen();
            return;
        }
        
        // Show loading only on first visit OR login page
        if (this.isLoginPage() || (isFirstVisit && !this.isNoLoadingPage())) {
            this.hasShownInitialLoading = true;
            // Loading screen will show by default
        } else {
            this.skipLoadingScreen();
        }
        
        // Clear the showLoading flag
        if (showLoading) {
            sessionStorage.removeItem('showLoading');
        }
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

    // ===== NAVIGATION HIGHLIGHTING =====
    highlightCurrentPage() {
        const navLinks = document.querySelectorAll('.nav-link');
        navLinks.forEach(link => {
            // Check data-page attribute first
            const dataPage = link.getAttribute('data-page');
            if (dataPage && dataPage === this.currentPage) {
                link.classList.add('active');
                return;
            }
            
            // Check href attribute as fallback
            const href = link.getAttribute('href');
            if (href) {
                const linkPage = href.replace('.html', '').replace('index', 'home');
                if (linkPage === this.currentPage || 
                    (this.currentPage === 'home' && linkPage === 'index')) {
                    link.classList.add('active');
                } else {
                    link.classList.remove('active');
                }
            }
        });
        
        // Update document title based on page
        this.updatePageTitle();
    }

    updatePageTitle() {
        const pageTitles = {
            'home': 'FlareBook Store - Ignite Your Mind',
            'category': 'Browse Categories - FlareBook Store',
            'about': 'About Us - FlareBook Store',
            'login': 'Login - FlareBook Store',
            'cart': 'Shopping Cart - FlareBook Store',
            'wishlist': 'My Wishlist - FlareBook Store',
            'orders': 'My Orders - FlareBook Store',
            'profile': 'My Profile - FlareBook Store',
            'settings': 'Settings - FlareBook Store'
        };
        
        const newTitle = pageTitles[this.currentPage] || 'FlareBook Store';
        if (document.title !== newTitle) {
            document.title = newTitle;
        }
    }

    // ===== NAVIGATION HANDLING =====
    setupNavigation() {
        document.addEventListener('click', (e) => {
            const navLink = e.target.closest('.nav-link');
            if (navLink) {
                e.preventDefault();
                
                // Get page from data attribute or href
                let page = navLink.getAttribute('data-page');
                if (!page) {
                    const href = navLink.getAttribute('href');
                    page = href ? href.replace('.html', '').replace('index', 'home') : 'home';
                }
                
                this.navigateTo(page);
            }
        });
    }

    navigateTo(page) {
        // Show loading screen for navigation
        this.showPageTransition();
        
        // Build navigation path based on current location
        const currentPath = window.location.pathname;
        let targetUrl = '';
        
        // Determine base paths
        const isRoot = currentPath.includes('index.html') || 
                       currentPath.endsWith('/') || 
                       currentPath.includes('/flarebook-store/');
        const isInPages = currentPath.includes('assets/pages/');
        const isInComponents = currentPath.includes('assets/components/');
        
        // Handle different page destinations
        if (page === 'home') {
            if (isInPages) {
                targetUrl = '../../index.html';
            } else if (isInComponents) {
                targetUrl = '../../index.html';
            } else {
                targetUrl = 'index.html';
            }
        } else {
            // Other pages (category, about, etc.)
            if (isRoot) {
                targetUrl = `assets/pages/${page}.html`;
            } else if (isInPages) {
                targetUrl = `${page}.html`;
            } else if (isInComponents) {
                targetUrl = `../pages/${page}.html`;
            } else {
                targetUrl = `./assets/pages/${page}.html`;
            }
        }
        
        console.log(`Navigating from ${currentPath} to ${page}: ${targetUrl}`);
        
        // Set loading flag and navigate
        sessionStorage.setItem('showLoading', 'true');
        setTimeout(() => {
            window.location.href = targetUrl;
        }, 500);
    }

    // ===== PAGE TRANSITIONS =====
    showPageTransition() {
        const transition = document.createElement('div');
        transition.className = 'page-transition-overlay';
        transition.innerHTML = `
            <div class="page-transition-content">
                <div class="loading-spinner"></div>
                <p>Loading...</p>
            </div>
        `;
        document.body.appendChild(transition);
        
        // Add styles if not already present
        if (!document.getElementById('page-transition-styles')) {
            this.addPageTransitionStyles();
        }
        
        // Show transition
        setTimeout(() => {
            transition.classList.add('active');
        }, 10);
    }

    addPageTransitionStyles() {
        const styles = document.createElement('style');
        styles.id = 'page-transition-styles';
        styles.textContent = `
            .page-transition-overlay {
                position: fixed;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background: var(--flare-dark);
                z-index: 9999;
                display: flex;
                align-items: center;
                justify-content: center;
                opacity: 0;
                visibility: hidden;
                transition: opacity 0.3s ease, visibility 0.3s ease;
            }
            
            .page-transition-overlay.active {
                opacity: 1;
                visibility: visible;
            }
            
            .page-transition-content {
                text-align: center;
                color: white;
            }
            
            .loading-spinner {
                width: 50px;
                height: 50px;
                border: 3px solid rgba(255, 107, 0, 0.3);
                border-radius: 50%;
                border-top-color: var(--flare-primary);
                animation: spin 1s ease-in-out infinite;
                margin: 0 auto 20px;
            }
            
            @keyframes spin {
                to { transform: rotate(360deg); }
            }
        `;
        document.head.appendChild(styles);
    }

    // ===== MOBILE MENU =====
    setupMobileMenu() {
        // Create mobile menu toggle if it doesn't exist
        if (!document.querySelector('.mobile-menu-toggle')) {
            const headerTop = document.querySelector('.header-top .header-section');
            if (headerTop) {
                const toggle = document.createElement('button');
                toggle.className = 'mobile-menu-toggle';
                toggle.innerHTML = '<i class="fas fa-bars"></i>';
                headerTop.insertBefore(toggle, headerTop.firstChild);
                
                toggle.addEventListener('click', () => {
                    document.querySelector('.header-nav').classList.toggle('active');
                    toggle.classList.toggle('active');
                });
            }
        }
        
        // Add mobile menu styles
        if (!document.getElementById('mobile-menu-styles')) {
            this.addMobileMenuStyles();
        }
    }

    addMobileMenuStyles() {
        const styles = document.createElement('style');
        styles.id = 'mobile-menu-styles';
        styles.textContent = `
            .mobile-menu-toggle {
                display: none;
                background: none;
                border: none;
                color: var(--flare-text);
                font-size: 1.5rem;
                cursor: pointer;
                padding: 10px;
                transition: color var(--transition-normal);
            }
            
            .mobile-menu-toggle:hover {
                color: var(--flare-primary);
            }
            
            @media (max-width: 768px) {
                .mobile-menu-toggle {
                    display: block;
                }
                
                .header-nav {
                    position: fixed;
                    top: 70px;
                    left: 0;
                    right: 0;
                    background: var(--flare-dark);
                    flex-direction: column;
                    padding: 20px;
                    border-top: 1px solid var(--flare-gray);
                    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
                    transform: translateY(-100%);
                    opacity: 0;
                    visibility: hidden;
                    transition: all var(--transition-normal);
                    z-index: 1000;
                }
                
                .header-nav.active {
                    transform: translateY(0);
                    opacity: 1;
                    visibility: visible;
                }
                
                .header-nav .nav-link {
                    padding: 15px 0;
                    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
                    width: 100%;
                    text-align: center;
                }
                
                .header-nav .nav-link:last-child {
                    border-bottom: none;
                }
            }
        `;
        document.head.appendChild(styles);
    }

    // ===== SMOOTH SCROLL =====
    setupSmoothScroll() {
        // Add smooth scrolling to anchor links
        document.addEventListener('click', (e) => {
            const anchor = e.target.closest('a[href^="#"]');
            if (anchor && anchor.getAttribute('href') !== '#') {
                e.preventDefault();
                const targetId = anchor.getAttribute('href').substring(1);
                const targetElement = document.getElementById(targetId);
                
                if (targetElement) {
                    this.scrollToElement(targetElement);
                }
            }
        });
    }

    scrollToElement(element) {
        const headerHeight = document.querySelector('.header-bottom')?.offsetHeight || 70;
        const targetPosition = element.getBoundingClientRect().top + window.pageYOffset - headerHeight;
        
        window.scrollTo({
            top: targetPosition,
            behavior: 'smooth'
        });
    }

    // ===== PAGE TRANSITION ANIMATIONS =====
    setupPageTransitions() {
        // Add fade-in animation for page content
        if (!document.getElementById('page-fade-styles')) {
            const styles = document.createElement('style');
            styles.id = 'page-fade-styles';
            styles.textContent = `
                .main-content-area {
                    animation: fadeIn 0.5s ease;
                }
                
                @keyframes fadeIn {
                    from { opacity: 0; transform: translateY(20px); }
                    to { opacity: 1; transform: translateY(0); }
                }
                
                .book-card, .section {
                    animation: fadeInUp 0.6s ease backwards;
                }
                
                .book-card:nth-child(2) { animation-delay: 0.1s; }
                .book-card:nth-child(3) { animation-delay: 0.2s; }
                .book-card:nth-child(4) { animation-delay: 0.3s; }
                .book-card:nth-child(5) { animation-delay: 0.4s; }
                .book-card:nth-child(6) { animation-delay: 0.5s; }
                
                @keyframes fadeInUp {
                    from { opacity: 0; transform: translateY(30px); }
                    to { opacity: 1; transform: translateY(0); }
                }
            `;
            document.head.appendChild(styles);
        }
    }

    // ===== BREADCRUMBS (Optional Enhancement) =====
    setupBreadcrumbs() {
        const breadcrumbContainer = document.querySelector('.breadcrumb-container');
        if (!breadcrumbContainer) return;
        
        const breadcrumbs = {
            'home': 'Home',
            'category': 'Categories',
            'about': 'About Us',
            'login': 'Login',
            'cart': 'Shopping Cart',
            'wishlist': 'My Wishlist'
        };
        
        if (breadcrumbs[this.currentPage]) {
            breadcrumbContainer.innerHTML = `
                <a href="index.html">Home</a>
                <span class="breadcrumb-separator">/</span>
                <span class="current-page">${breadcrumbs[this.currentPage]}</span>
            `;
        }
    }
}

// Initialize navigation manager
document.addEventListener('DOMContentLoaded', () => {
    window.navigationManager = new NavigationManager();
});

// Export for use in other modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = NavigationManager;
}

// Initialize navigation manager AFTER header is loaded
function initializeNavigation() {
    // Check if header is loaded
    const checkHeaderLoaded = setInterval(() => {
        const navLinks = document.querySelectorAll('.nav-link');
        if (navLinks.length > 0) {
            clearInterval(checkHeaderLoaded);
            window.navigationManager = new NavigationManager();
            console.log('Navigation initialized successfully');
        }
    }, 100);
    
    // Timeout after 5 seconds
    setTimeout(() => {
        clearInterval(checkHeaderLoaded);
        console.warn('Header not found after 5 seconds');
    }, 5000);
}

// Start initialization
document.addEventListener('DOMContentLoaded', initializeNavigation);

// Initialize navigation manager
document.addEventListener('DOMContentLoaded', () => {
    // Wait for header to load
    setTimeout(() => {
        window.navigationManager = new NavigationManager();
    }, 300); // Wait 300ms for header to load
});