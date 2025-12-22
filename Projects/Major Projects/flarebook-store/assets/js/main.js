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
        
        // Update UI IMMEDIATELY (no delay)
        this.updateUserUI();
        this.updateCartCount();
        this.updateWishlistCount();
        
        // Setup features
        this.setupHeaderScroll();
        this.bindEvents();
        
        // Hide loading screen after everything is ready
        this.hideLoadingScreen();
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
        }, 1500); // Reduced from 2000 to 1500 for faster loading
    }

    // ===== EVENT BINDINGS =====
    bindEvents() {
        // Login/Avatar button
        const loginBtn = document.getElementById('headerLoginBtn');
        if (loginBtn) {
            loginBtn.addEventListener('click', (e) => {
                e.preventDefault();
                if (this.currentUser) {
                    // Show user dropdown menu
                    this.showUserMenu();
                } else {
                    window.location.href = 'assets/pages/login.html';
                }
            });
        }
        
        // Cart button
        const cartBtn = document.getElementById('cartBtn');
        if (cartBtn) {
            cartBtn.addEventListener('click', (e) => {
                e.preventDefault();
                window.location.href = 'assets/pages/cart.html';
            });
        }
        
        // Favorites button
        const favoritesBtn = document.getElementById('favoritesBtn');
        if (favoritesBtn) {
            favoritesBtn.addEventListener('click', (e) => {
                e.preventDefault();
                window.location.href = 'assets/pages/wishlist.html';
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
        
        // Navigation links
        const navLinks = document.querySelectorAll('.nav-link');
        navLinks.forEach(link => {
            link.addEventListener('click', (e) => {
                if (link.getAttribute('href') === '#') {
                    e.preventDefault();
                    navLinks.forEach(l => l.classList.remove('active'));
                    link.classList.add('active');
                }
            });
        });
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
        
        if (this.currentUser.type === 'business') {
            userTypeDisplay = 'Business Account';
            statusBadge = '<span class="status-badge pending">Pending Verification</span>';
        }
        
        menu.innerHTML = `
            <div class="user-info">
                <div class="user-avatar-large">${this.currentUser.name ? this.currentUser.name.charAt(0).toUpperCase() : 'U'}</div>
                <div class="user-details">
                    <strong>${this.currentUser.name || 'User'}</strong>
                    <small>${this.currentUser.email || ''}</small>
                    <div class="user-type">${userTypeDisplay} ${statusBadge}</div>
                </div>
            </div>
            <div class="user-menu-options">
                <a href="#" class="menu-item coming-soon"><i class="fas fa-user-circle"></i> My Profile <span class="badge">Soon</span></a>
                <a href="#" class="menu-item coming-soon"><i class="fas fa-shopping-bag"></i> My Orders <span class="badge">Soon</span></a>
                <a href="#" class="menu-item coming-soon"><i class="far fa-heart"></i> My Wishlist <span class="badge">Soon</span></a>
                <a href="#" class="menu-item coming-soon"><i class="fas fa-cog"></i> Account Settings <span class="badge">Soon</span></a>
                ${this.currentUser.type === 'business' ? 
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
        
        // Logout functionality
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
        
        // Redirect to home if not already there
        if (!window.location.pathname.includes('index.html')) {
            window.location.href = 'index.html';
        }
    }
}

// Initialize the application IMMEDIATELY when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    window.flareBookApp = new FlareBookStore();
});

// ===== GLOBAL FUNCTIONS (for HTML onclick events) =====
// These are kept for compatibility with HTML onclick attributes

// Tab switching for login/register
function switchTab(tab) {
    document.querySelectorAll('.auth-tab').forEach(t => t.classList.remove('active'));
    document.querySelectorAll('.auth-content').forEach(c => c.classList.remove('active'));

    document.querySelector(`.auth-tab:nth-child(${tab === 'login' ? '1' : '2'})`).classList.add('active');
    document.getElementById(tab + '-content').classList.add('active');
}

// Business registration type switching
function switchRegType(type, clickedButton) {   
    document.querySelectorAll('.reg-type-tab').forEach(b => b.classList.remove('active'));
    clickedButton.classList.add('active');

    document.getElementById('personal-form').style.display = type === 'personal' ? 'block' : 'none';
    document.getElementById('business-form').style.display = type === 'business' ? 'block' : 'none';
}

// GSTIN field toggle
function toggleGstinField(show) {
    const gstinField = document.getElementById('gstin-field');
    if (gstinField) {
        gstinField.style.display = show ? 'block' : 'none';
    }
}