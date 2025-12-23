// ===== FLAREBOOK STORE - MAIN APPLICATION =====
class FlareBookStore {
    constructor() {
        // Load user IMMEDIATELY and synchronously
        this.currentUser = this.loadUser();
        this.lastScrollTop = 0;
        this.bookSuggestions = [
            "Harry Potter and the Philosopher's Stone",
            "The Great Gatsby",
            "To Kill a Mockingbird",
            "1984 by George Orwell",
            "Pride and Prejudice",
            "The Hobbit",
            "The Catcher in the Rye",
            "The Lord of the Rings",
            "Animal Farm",
            "Brave New World"
        ];
        this.init();
    }

    // Load user from localStorage (synchronous)
    loadUser() {
        try {
            const userData = localStorage.getItem('flarebook_current_user');
            if (userData) {
                return JSON.parse(userData);
            }
        } catch (error) {
            console.error('Error loading user:', error);
        }
        return null;
    }

    init() {
        console.log('FlareBook Store initialized');
        
        // Set active navigation FIRST
        this.setActiveNavLink();
        
        // Update UI IMMEDIATELY (no delay)
        this.updateUserUI();
        this.updateCartCount();
        this.updateWishlistCount();
        
        // Setup features
        this.setupHeaderScroll();
        this.setupScrollToTop();
        this.bindEvents();
        
        // Hide loading screen after everything is ready
        this.hideLoadingScreen();
    }

    // ===== NAVIGATION HELPERS =====
    
    // Get current page name from URL
    getCurrentPageName() {
        const path = window.location.pathname;
        
        if (path.includes('index.html') || path.endsWith('/') || path.includes('/flarebook-store/')) {
            return 'home';
        } else if (path.includes('category.html')) {
            return 'category';
        } else if (path.includes('about.html')) {
            return 'about';
        } else if (path.includes('login.html')) {
            return 'login';
        } else if (path.includes('cart.html')) {
            return 'cart';
        } else if (path.includes('wishlist.html')) {
            return 'wishlist';
        } else if (path.includes('orders.html')) {
            return 'orders';
        } else if (path.includes('profile.html')) {
            return 'profile';
        } else if (path.includes('settings.html')) {
            return 'settings';
        }
        
        return 'home'; // default
    }
    
    // Set active navigation link based on current page
setActiveNavLink() {
    const currentPage = this.getCurrentPageName();
    const navLinks = document.querySelectorAll('.nav-link');
    
    navLinks.forEach(link => {
        link.classList.remove('active');
        
        // Get page from data attribute
        const pageFromData = link.getAttribute('data-page');
        
        // If data-page matches current page, set active
        if (pageFromData === currentPage) {
            link.classList.add('active');
            console.log('Active link set:', pageFromData);
        }
    });
}

    // ===== SMART NAVIGATION FUNCTION =====
navigateToPage(pageName) {
    // Map page names to filenames
    const pageMap = {
        'home': 'index.html',
        'category': 'category.html',
        'about': 'about.html',
        'login': 'login.html',
        'cart': 'cart.html',
        'wishlist': 'wishlist.html',
        'orders': 'orders.html',
        'profile': 'profile.html',
        'settings': 'settings.html'
    };
    
    if (!pageMap[pageName]) {
        console.error('Unknown page:', pageName);
        return;
    }
    
    const filename = pageMap[pageName];
    let fullPath;
    
    // Get current location
    const currentPath = window.location.pathname;
    console.log('Current path:', currentPath);
    console.log('Navigating to:', pageName);
    
    // SPECIAL FIX FOR INDEX.HTML (ROOT FOLDER)
    // Check if we're on index.html or root folder
    const isOnIndexPage = currentPath.includes('index.html') || 
                          currentPath.endsWith('/') || 
                          currentPath.includes('/flarebook-store/');
    
    // Check if we're in assets/pages/ folder
    const isInPagesFolder = currentPath.includes('assets/pages/');
    
    // Check if we're in assets/components/ folder (header files)
    const isInComponentsFolder = currentPath.includes('assets/components/');
    
    // For HOME page (index.html)
    if (pageName === 'home') {
        if (isInPagesFolder) {
            fullPath = '../../index.html';        // From pages to root
        } else if (isInComponentsFolder) {
            fullPath = '../../index.html';     // From components to root
        } else {
            fullPath = 'index.html';           // Already at root
        }
    } 
    // For other pages (category, about, login, cart, etc.)
    else {
        if (isOnIndexPage) {
            // We're at ROOT/index.html
            fullPath = `assets/pages/${filename}`;
        } else if (isInPagesFolder) {
            // We're already in assets/pages/ folder
            fullPath = filename;  // Same folder
        } else if (isInComponentsFolder) {
            // We're in components folder (header files)
            fullPath = `../pages/${filename}`;
        } else {
            // Default fallback
            fullPath = `./assets/pages/${filename}`;
        }
    }
    
    console.log(`Final navigation path to ${pageName}:`, fullPath);
    window.location.href = fullPath;
}

    // ===== USER INTERFACE =====
    updateUserUI() {
        const loginBtn = document.getElementById('headerLoginBtn');
        if (!loginBtn) return;
        
        if (this.currentUser) {
            // User is logged in - show avatar immediately
            const firstName = this.currentUser.name ? this.currentUser.name.split(' ')[0] : 'U';
            const firstLetter = firstName.charAt(0).toUpperCase();
            
            loginBtn.innerHTML = `
                <div class="user-avatar">
                    ${firstLetter}
                </div>
            `;
            loginBtn.classList.add('user-avatar-btn');
            loginBtn.title = `Logged in as ${this.currentUser.name || 'User'}`;
        } else {
            // User is not logged in - show login button
            loginBtn.innerHTML = `
                <i class="fas fa-user"></i> Login
            `;
            loginBtn.classList.remove('user-avatar-btn');
            loginBtn.title = 'Login to your account';
        }
    }

    updateCartCount() {
        try {
            const cartItems = JSON.parse(localStorage.getItem('flarebook_cart')) || [];
            const cartBadge = document.querySelector('#cartBtn .icon-badge');
            if (cartBadge) {
                cartBadge.textContent = cartItems.length;
            }
        } catch (error) {
            console.error('Error updating cart count:', error);
        }
    }

    updateWishlistCount() {
        try {
            const wishlistItems = JSON.parse(localStorage.getItem('flarebook_wishlist')) || [];
            const wishlistBadge = document.querySelector('#favoritesBtn .icon-badge');
            if (wishlistBadge) {
                wishlistBadge.textContent = wishlistItems.length;
            }
        } catch (error) {
            console.error('Error updating wishlist count:', error);
        }
    }

    // ===== HEADER SCROLL EFFECT =====
    setupHeaderScroll() {
        const headerTop = document.getElementById('headerTop');
        const headerBottom = document.getElementById('headerBottom');
        
        if (!headerTop || !headerBottom) return;
        
        window.addEventListener('scroll', () => {
            const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
            
            // Show/hide top header based on scroll direction
            if (scrollTop > this.lastScrollTop && scrollTop > 100) {
                // Scrolling DOWN - hide top header
                headerTop.classList.add('hidden');
                headerBottom.classList.add('sticky');
            } else {
                // Scrolling UP - show top header
                headerTop.classList.remove('hidden');
                if (scrollTop <= 100) {
                    headerBottom.classList.remove('sticky');
                }
            }
            
            this.lastScrollTop = scrollTop <= 0 ? 0 : scrollTop;
        });
    }

    // ===== LOADING SCREEN =====
    hideLoadingScreen() {
        setTimeout(() => {
            const loadingScreen = document.getElementById('loading-screen');
            const mainContent = document.getElementById('main-content');
            
            if (loadingScreen && mainContent) {
                loadingScreen.style.opacity = '0';
                loadingScreen.style.visibility = 'hidden';
                mainContent.classList.remove('hidden');
                
                setTimeout(() => {
                    if (loadingScreen.parentNode) {
                        loadingScreen.remove();
                    }
                }, 500);
            }
        }, 1500);
    }

    // ===== EVENT BINDINGS =====
bindEvents() {
    // Check where we are
    const currentPath = window.location.pathname;
    const isOnIndexPage = currentPath.includes('index.html') || 
                          currentPath.endsWith('/') || 
                          currentPath.includes('/flarebook-store/');
    
    console.log('Current location:', currentPath, 'Is on index page?', isOnIndexPage);
    
    // Favorites button
    const favoritesBtn = document.getElementById('favoritesBtn');
    if (favoritesBtn) {
        favoritesBtn.addEventListener('click', (e) => {
            e.preventDefault();
            this.navigateToPage('wishlist');
        });
    }
    
    // Cart button
    const cartBtn = document.getElementById('cartBtn');
    if (cartBtn) {
        cartBtn.addEventListener('click', (e) => {
            e.preventDefault();
            this.navigateToPage('cart');
        });
    }
    
    // Login button
    const loginBtn = document.getElementById('headerLoginBtn');
    if (loginBtn) {
        loginBtn.addEventListener('click', (e) => {
            e.preventDefault();
            if (this.currentUser) {
                this.showUserMenu();
            } else {
                this.navigateToPage('login');
            }
        });
    }
    
    // Navigation links (Home, Category, About)
    const navLinks = document.querySelectorAll('.nav-link[data-page]');
    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            
            const pageName = link.getAttribute('data-page');
            console.log('Navigation link clicked:', pageName);
            
            // Update active state
            navLinks.forEach(l => l.classList.remove('active'));
            link.classList.add('active');
            
            // Navigate
            this.navigateToPage(pageName);
        });
    });
    
    // If no data attributes, fall back to text-based navigation
    if (navLinks.length === 0) {
        const fallbackLinks = document.querySelectorAll('.nav-link');
        fallbackLinks.forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                
                // Get the page name from link text
                const pageName = link.textContent.toLowerCase().trim();
                console.log('Fallback navigation link clicked:', pageName);
                
                // Update active state
                fallbackLinks.forEach(l => l.classList.remove('active'));
                link.classList.add('active');
                
                // Navigate
                this.navigateToPage(pageName);
            });
        });
    }
    
    // Search functionality
    const searchBtn = document.querySelector('.search-btn');
    if (searchBtn) {
        searchBtn.addEventListener('click', (e) => {
            e.preventDefault();
            this.performSearch();
        });
    }
    
    // Search input
    const searchInput = document.getElementById('searchInput');
    if (searchInput) {
        searchInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                e.preventDefault();
                this.performSearch();
            }
        });
        
        // Autocomplete
        searchInput.addEventListener('input', (e) => this.handleSearchInput(e));
        searchInput.addEventListener('focus', () => this.showAutocomplete());
        searchInput.addEventListener('blur', () => {
            setTimeout(() => this.hideAutocomplete(), 200);
        });
    }
}

    // ===== SEARCH FUNCTIONALITY =====
    handleSearchInput(e) {
        const query = e.target.value.toLowerCase().trim();
        const dropdown = document.getElementById('autocompleteDropdown');
        
        if (!dropdown) return;
        
        if (query.length < 2) {
            dropdown.innerHTML = '';
            dropdown.classList.remove('active');
            return;
        }
        
        // Filter suggestions
        const suggestions = this.bookSuggestions
            .filter(book => book.toLowerCase().includes(query))
            .slice(0, 5);
        
        if (suggestions.length > 0) {
            dropdown.innerHTML = suggestions.map(book => `
                <div class="suggestion-item" data-book="${book}">
                    <i class="fas fa-book"></i>
                    <span>${this.highlightMatch(book, query)}</span>
                </div>
            `).join('');
            dropdown.classList.add('active');
            
            // Add click handlers to suggestions
            dropdown.querySelectorAll('.suggestion-item').forEach(item => {
                item.addEventListener('click', () => {
                    document.getElementById('searchInput').value = item.dataset.book;
                    this.performSearch();
                    dropdown.classList.remove('active');
                });
            });
        } else {
            dropdown.innerHTML = '<div class="no-results">No books found</div>';
            dropdown.classList.add('active');
        }
    }

    highlightMatch(text, query) {
        if (!query) return text;
        const regex = new RegExp(`(${query})`, 'gi');
        return text.replace(regex, '<mark>$1</mark>');
    }

    showAutocomplete() {
        const searchInput = document.getElementById('searchInput');
        const dropdown = document.getElementById('autocompleteDropdown');
        
        if (searchInput && dropdown && searchInput.value.trim().length >= 2) {
            dropdown.classList.add('active');
        }
    }

    hideAutocomplete() {
        const dropdown = document.getElementById('autocompleteDropdown');
        if (dropdown) {
            dropdown.classList.remove('active');
        }
    }

    performSearch() {
        const searchInput = document.getElementById('searchInput');
        const dropdown = document.getElementById('autocompleteDropdown');
        const query = searchInput ? searchInput.value.trim() : '';
        
        if (dropdown) {
            dropdown.classList.remove('active');
        }
        
        if (query) {
            alert(`Searching for: "${query}"\n\nFull search functionality will be implemented with book database.`);
            if (searchInput) {
                searchInput.value = '';
            }
        } else if (searchInput) {
            searchInput.focus();
        }
    }

    // ===== USER MENU =====
    showUserMenu() {
        // First show the alert
        alert("📋 ACCOUNT FEATURES STATUS\n\n" +
              "🔄 Some settings are under Development\n" +
              "\n" +
              "Essential features are fully functional!\n" +
              "Some advanced settings are being developed.");
        
        // Remove existing menu if any
        const existingMenu = document.querySelector('.user-dropdown');
        if (existingMenu) {
            existingMenu.remove();
        }
        
        // Create user dropdown menu
        const menu = document.createElement('div');
        menu.className = 'user-dropdown';
        
        // Get user type display
        let userTypeDisplay = 'Personal Account';
        let statusBadge = '';
        
        if (this.currentUser && this.currentUser.type === 'business') {
            userTypeDisplay = 'Business Account';
            statusBadge = '<span class="status-badge pending">Pending Verification</span>';
        }
        
        const userName = this.currentUser ? this.currentUser.name || 'User' : 'User';
        const userEmail = this.currentUser ? this.currentUser.email || '' : '';
        const userInitial = userName.charAt(0).toUpperCase();
        
        menu.innerHTML = `
            <div class="user-info">
                <div class="user-avatar-large">${userInitial}</div>
                <div class="user-details">
                    <strong>${userName}</strong>
                    <small>${userEmail}</small>
                    <div class="user-type">${userTypeDisplay} ${statusBadge}</div>
                </div>
            </div>
            <div class="user-menu-options">
                <a href="#" class="menu-item coming-soon"><i class="fas fa-user-circle"></i> My Profile <span class="badge">Soon</span></a>
                <a href="#" class="menu-item coming-soon"><i class="fas fa-shopping-bag"></i> My Orders <span class="badge">Soon</span></a>
                <a href="#" class="menu-item coming-soon"><i class="fas fa-cog"></i> Account Settings <span class="badge">Soon</span></a>
                ${this.currentUser && this.currentUser.type === 'business' ? 
                    '<a href="#" class="menu-item coming-soon"><i class="fas fa-building"></i> Business Dashboard <span class="badge">Verifying</span></a>' : 
                    ''
                }
                <div class="menu-divider"></div>
                <a href="#" class="menu-item logout" id="logoutBtn"><i class="fas fa-sign-out-alt"></i> Logout</a>
            </div>
        `;
        
        // Position near the avatar button
        const loginBtn = document.getElementById('headerLoginBtn');
        if (loginBtn) {
            const rect = loginBtn.getBoundingClientRect();
            menu.style.position = 'fixed';
            menu.style.top = (rect.bottom + 10) + 'px';
            menu.style.right = (window.innerWidth - rect.right) + 'px';
            menu.style.zIndex = '9999';
        }
        
        document.body.appendChild(menu);
        
        // Add click outside to close
        const closeMenu = (e) => {
            if (!menu.contains(e.target) && e.target !== loginBtn) {
                menu.remove();
                document.removeEventListener('click', closeMenu);
            }
        };
        
        setTimeout(() => {
            document.addEventListener('click', closeMenu);
        }, 100);
        
        // Logout functionality - FIXED PATH
        const logoutBtn = menu.querySelector('#logoutBtn');
        if (logoutBtn) {
            logoutBtn.addEventListener('click', (e) => {
                e.preventDefault();
                this.logout();
                menu.remove();
            });
        }
        
        // Add coming soon alerts
        const comingSoonItems = menu.querySelectorAll('.coming-soon');
        comingSoonItems.forEach(item => {
            item.addEventListener('click', (e) => {
                e.preventDefault();
                alert('🚧 FEATURE UNDER DEVELOPMENT\n\nThis feature is currently being built and will be available soon!');
            });
        });
    }

    // ===== LOGOUT =====
logout() {
    localStorage.removeItem('flarebook_current_user');
    this.currentUser = null;
    
    // Update UI IMMEDIATELY
    this.updateUserUI();
    
    alert('Logged out successfully!');
    
    // Get current location
    const currentPath = window.location.pathname;
    let homePath;
    
    // Determine correct path to home based on current location
    if (currentPath.includes('assets/pages/')) {
        homePath = '../../index.html';        // From pages to root
    } else if (currentPath.includes('assets/components/')) {
        homePath = '../../index.html';     // From components to root
    } else {
        homePath = 'index.html';           // Already at root
    }
    
    console.log('Logout redirecting to:', homePath);
    window.location.href = homePath;

    
}
// Add this method to the FlareBookStore class:

// ===== SCROLL TO TOP FUNCTIONALITY =====
setupScrollToTop() {
    const scrollBtn = document.getElementById('scrollToTopBtn');
    if (!scrollBtn) return;
    
    // Show/hide button based on scroll position
    window.addEventListener('scroll', () => {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        const windowHeight = window.innerHeight;
        const documentHeight = document.documentElement.scrollHeight;
        
        // Show button after scrolling 300px
        if (scrollTop > 300) {
            scrollBtn.classList.add('visible');
            
            // Add "near-top" class when close to top (last 20% of scroll)
            const scrollPercentage = (scrollTop / (documentHeight - windowHeight)) * 100;
            if (scrollPercentage < 20) {
                scrollBtn.classList.add('near-top');
            } else {
                scrollBtn.classList.remove('near-top');
            }
        } else {
            scrollBtn.classList.remove('visible');
            scrollBtn.classList.remove('near-top');
        }
    });
    
    // Scroll to top with variable speed
    scrollBtn.addEventListener('click', () => {
        this.scrollToTopWithVariableSpeed();
    });
    
    // Add to keyboard navigation
    scrollBtn.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            this.scrollToTopWithVariableSpeed();
        }
    });
}

scrollToTopWithVariableSpeed() {
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    const documentHeight = document.documentElement.scrollHeight;
    const scrollPercentage = (scrollTop / documentHeight) * 100;
    
    // Variable duration based on scroll position
    let duration;
    if (scrollPercentage > 80) {
        duration = 800; // Fast when at bottom
    } else if (scrollPercentage > 50) {
        duration = 1200; // Medium speed
    } else if (scrollPercentage > 20) {
        duration = 1600; // Slower
    } else {
        duration = 2000; // Slowest when near top
    }
    
    // Easing function for smooth animation
    const easeInOutCubic = (t) => {
        return t < 0.5 ? 4 * t * t * t : (t - 1) * (2 * t - 2) * (2 * t - 2) + 1;
    };
    
    const startTime = performance.now();
    const startPosition = scrollTop;
    
    const animateScroll = (currentTime) => {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        const easeProgress = easeInOutCubic(progress);
        
        window.scrollTo(0, startPosition * (1 - easeProgress));
        
        if (progress < 1) {
            requestAnimationFrame(animateScroll);
        }
    };
    
    requestAnimationFrame(animateScroll);
}
}

// Initialize the application IMMEDIATELY when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    window.flareBookApp = new FlareBookStore();
});

// ===== GLOBAL FUNCTIONS (for HTML onclick events) =====

function switchTab(tab) {
    document.querySelectorAll('.auth-tab').forEach(t => t.classList.remove('active'));
    document.querySelectorAll('.auth-content').forEach(c => c.classList.remove('active'));

    document.querySelector(`.auth-tab:nth-child(${tab === 'login' ? '1' : '2'})`).classList.add('active');
    document.getElementById(tab + '-content').classList.add('active');
}

function switchRegType(type, clickedButton) {   
    document.querySelectorAll('.reg-type-tab').forEach(b => b.classList.remove('active'));
    clickedButton.classList.add('active');

    document.getElementById('personal-form').style.display = type === 'personal' ? 'block' : 'none';
    document.getElementById('business-form').style.display = type === 'business' ? 'block' : 'none';
}

function toggleGstinField(show) {
    const gstinField = document.getElementById('gstin-field');
    if (gstinField) {
        gstinField.style.display = show ? 'block' : 'none';
    }
}

