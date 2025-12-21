// ===== GLOBAL STATE AND UTILITIES =====
class FlareBookStore {
    constructor() {
        this.currentPage = 'home';
        this.currentAuthTab = 'login';
        this.currentBusinessStep = 1;
        this.users = JSON.parse(localStorage.getItem('flarebook_users')) || [];
        this.currentUser = JSON.parse(localStorage.getItem('flarebook_current_user')) || null;
        this.init();
    }

    init() {
        // Simulate loading delay
        setTimeout(() => {
            this.hideLoadingScreen();
            this.loadPage(this.currentPage);
        }, 2000);

        // Initialize event listeners
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

    loadPage(page) {
        const contentDiv = document.getElementById('page-content');
        
        switch(page) {
            case 'home':
                this.renderHomePage(contentDiv);
                break;
            case 'auth':
                this.renderAuthPage(contentDiv);
                break;
            default:
                this.renderHomePage(contentDiv);
        }
    }

    // ===== PAGE RENDERING =====
    renderHomePage(container) {
        container.innerHTML = `
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
                <button class="enter-button" id="enter-login">
                    Enter Store <i class="fas fa-arrow-right"></i>
                </button>
            </div>
        `;
    }

    renderAuthPage(container) {
        container.innerHTML = `
            <div class="auth-container">
                <div class="auth-header">
                    <h1 class="auth-title">Welcome to FlareBook</h1>
                    <p class="auth-subtitle">Sign in to your account or create a new one</p>
                </div>
                
                <div class="auth-tabs">
                    <button class="auth-tab ${this.currentAuthTab === 'login' ? 'active' : ''}" data-tab="login">Login</button>
                    <button class="auth-tab ${this.currentAuthTab === 'register' ? 'active' : ''}" data-tab="register">Register</button>
                </div>
                
                <div class="auth-content ${this.currentAuthTab === 'login' ? 'active' : ''}" id="login-content">
                    ${this.renderLoginForm()}
                </div>
                
                <div class="auth-content ${this.currentAuthTab === 'register' ? 'active' : ''}" id="register-content">
                    ${this.renderRegisterForm()}
                </div>
            </div>
        `;
    }

    renderLoginForm() {
        const captchaQuestion = this.generateCaptcha();
        return `
            <form class="auth-form" id="login-form">
                <div class="form-group">
                    <label class="form-label" for="login-email">Email Address</label>
                    <input type="email" id="login-email" class="form-input" placeholder="you@example.com" required>
                    <div class="error-message" id="login-email-error"></div>
                </div>
                
                <div class="form-group">
                    <label class="form-label" for="login-password">Password</label>
                    <input type="password" id="login-password" class="form-input" placeholder="Enter your password" required>
                    <div class="error-message" id="login-password-error"></div>
                </div>
                
                <div class="captcha-container">
                    <div class="captcha-question">${captchaQuestion.question}</div>
                    <div class="captcha-options">
                        ${captchaQuestion.options.map(option => `
                            <button type="button" class="captcha-option" data-answer="${option.isCorrect}">
                                ${option.text}
                            </button>
                        `).join('')}
                    </div>
                    <input type="hidden" id="captcha-answer" value="">
                    <div class="error-message" id="captcha-error">Please select the correct answer</div>
                </div>
                
                <button type="submit" class="submit-btn">Sign In</button>
                
                <div class="form-divider">
                    <span>Or continue with</span>
                </div>
                
                <div class="social-login">
                    <button type="button" class="social-btn google">
                        <i class="fab fa-google"></i> Google
                    </button>
                    <button type="button" class="social-btn microsoft">
                        <i class="fab fa-microsoft"></i> Microsoft
                    </button>
                </div>
                
                <div class="form-footer">
                    Don't have an account? 
                    <button type="button" class="toggle-auth" data-target="register">Sign up here</button>
                </div>
            </form>
        `;
    }

    renderRegisterForm() {
        return `
            <form class="auth-form" id="register-form">
                <div class="form-tabs" style="margin-bottom: 30px;">
                    <button type="button" class="nav-btn register-type-btn active" data-type="personal">Personal Account</button>
                    <button type="button" class="nav-btn register-type-btn" data-type="business">Business Account</button>
                </div>
                
                <div id="personal-registration" class="registration-form">
                    ${this.renderPersonalRegistration()}
                </div>
                
                <div id="business-registration" class="registration-form" style="display: none;">
                    ${this.renderBusinessRegistrationStep1()}
                </div>
            </form>
        `;
    }

    renderPersonalRegistration() {
        return `
            <div class="form-group">
                <label class="form-label" for="personal-name">Full Name</label>
                <input type="text" id="personal-name" class="form-input" placeholder="John Doe" required>
                <div class="error-message" id="personal-name-error"></div>
            </div>
            
            <div class="form-group">
                <label class="form-label" for="personal-email">Email Address</label>
                <div class="verification-container">
                    <input type="email" id="personal-email" class="form-input verification-input" placeholder="you@example.com" required>
                    <button type="button" class="verify-btn" id="verify-personal-email">Verify</button>
                </div>
                <div class="error-message" id="personal-email-error"></div>
                <div class="verification-status" id="personal-email-status"></div>
            </div>
            
            <div class="form-row">
                <div class="form-group">
                    <label class="form-label" for="personal-password">Password</label>
                    <input type="password" id="personal-password" class="form-input" placeholder="Create password" required>
                    <div class="error-message" id="personal-password-error"></div>
                </div>
                
                <div class="form-group">
                    <label class="form-label" for="personal-confirm">Confirm Password</label>
                    <input type="password" id="personal-confirm" class="form-input" placeholder="Confirm password" required>
                    <div class="error-message" id="personal-confirm-error"></div>
                </div>
            </div>
            
            <div class="social-login">
                <button type="button" class="social-btn google">
                    <i class="fab fa-google"></i> Continue with Google
                </button>
                <button type="button" class="social-btn microsoft">
                    <i class="fab fa-microsoft"></i> Continue with Microsoft
                </button>
            </div>
            
            <button type="submit" class="submit-btn">Create Personal Account</button>
            
            <div class="form-footer">
                Already have an account? 
                <button type="button" class="toggle-auth" data-target="login">Sign in here</button>
            </div>
        `;
    }

    renderBusinessRegistrationStep1() {
        return `
            <div class="registration-step active" data-step="1">
                <h3 style="margin-bottom: 25px; color: var(--flare-secondary);">Step 1: Personal Information</h3>
                
                <div class="form-group">
                    <label class="form-label" for="business-name">Full Name</label>
                    <input type="text" id="business-name" class="form-input" placeholder="John Doe" required>
                    <div class="error-message" id="business-name-error"></div>
                </div>
                
                <div class="form-group">
                    <label class="form-label" for="business-email">Email Address</label>
                    <div class="verification-container">
                        <input type="email" id="business-email" class="form-input verification-input" placeholder="you@example.com" required>
                        <button type="button" class="verify-btn" id="verify-business-email">Verify</button>
                    </div>
                    <div class="error-message" id="business-email-error"></div>
                    <div class="verification-status" id="business-email-status"></div>
                </div>
                
                <div class="form-group">
                    <label class="form-label" for="business-phone">Phone Number</label>
                    <div class="verification-container">
                        <input type="tel" id="business-phone" class="form-input verification-input" placeholder="+91 9876543210" required>
                        <button type="button" class="verify-btn" id="verify-business-phone">Verify</button>
                    </div>
                    <div class="error-message" id="business-phone-error"></div>
                    <div class="verification-status" id="business-phone-status"></div>
                </div>
                
                <div class="form-row">
                    <div class="form-group">
                        <label class="form-label" for="business-password">Password</label>
                        <input type="password" id="business-password" class="form-input" placeholder="Create password" required>
                        <div class="error-message" id="business-password-error"></div>
                    </div>
                    
                    <div class="form-group">
                        <label class="form-label" for="business-confirm">Confirm Password</label>
                        <input type="password" id="business-confirm" class="form-input" placeholder="Confirm password" required>
                        <div class="error-message" id="business-confirm-error"></div>
                    </div>
                </div>
                
                <div class="form-navigation">
                    <div></div>
                    <button type="button" class="nav-btn next" id="next-business-step">Next Step</button>
                </div>
            </div>
            
            <div class="registration-step" data-step="2">
                ${this.renderBusinessRegistrationStep2()}
            </div>
        `;
    }

    renderBusinessRegistrationStep2() {
        return `
            <h3 style="margin-bottom: 25px; color: var(--flare-secondary);">Step 2: Business Information</h3>
            
            <div class="form-group">
                <label class="form-label" for="company-name">Business Name</label>
                <input type="text" id="company-name" class="form-input" placeholder="Your Business Name" required>
                <div class="error-message" id="company-name-error"></div>
            </div>
            
            <div class="form-group">
                <label class="form-label" for="gstin-toggle">Do you have GSTIN Number?</label>
                <div style="display: flex; gap: 20px; margin-top: 10px;">
                    <label style="display: flex; align-items: center; gap: 8px;">
                        <input type="radio" name="has-gstin" value="yes"> Yes
                    </label>
                    <label style="display: flex; align-items: center; gap: 8px;">
                        <input type="radio" name="has-gstin" value="no" checked> No
                    </label>
                </div>
            </div>
            
            <div class="form-group" id="gstin-field" style="display: none;">
                <label class="form-label" for="gstin-number">GSTIN Number</label>
                <input type="text" id="gstin-number" class="form-input" placeholder="22AAAAA0000A1Z5">
                <div class="error-message" id="gstin-error"></div>
            </div>
            
            <div class="form-group">
                <label class="form-label" for="designation">Personal Designation</label>
                <input type="text" id="designation" class="form-input" placeholder="e.g., Owner, Manager, CEO" required>
                <div class="error-message" id="designation-error"></div>
            </div>
            
            <div class="form-group">
                <label class="form-label" for="pan-number">PAN Number</label>
                <input type="text" id="pan-number" class="form-input" placeholder="ABCDE1234F" required>
                <div class="error-message" id="pan-error"></div>
            </div>
            
            <div class="form-group">
                <label class="form-label" for="business-address">Business Address</label>
                <textarea id="business-address" class="form-input" rows="3" placeholder="Complete business address" required></textarea>
                <div class="error-message" id="address-error"></div>
            </div>
            
            <div class="form-group">
                <label class="form-label" for="pincode">PIN Code</label>
                <input type="text" id="pincode" class="form-input" placeholder="110001" required>
                <div class="error-message" id="pincode-error"></div>
            </div>
            
            <div class="form-navigation">
                <button type="button" class="nav-btn" id="prev-business-step">Previous</button>
                <button type="submit" class="nav-btn next">Create Business Account</button>
            </div>
        `;
    }

    // ===== UTILITY FUNCTIONS =====
    generateCaptcha() {
        const questions = [
            {
                question: "Which of these is NOT a book?",
                options: [
                    { text: "Harry Potter", isCorrect: false },
                    { text: "To Kill a Mockingbird", isCorrect: false },
                    { text: "Avocado Toast", isCorrect: true },
                    { text: "1984", isCorrect: false }
                ]
            },
            {
                question: "What do you use to read an ebook?",
                options: [
                    { text: "Microwave", isCorrect: false },
                    { text: "Device/Reader", isCorrect: true },
                    { text: "Refrigerator", isCorrect: false },
                    { text: "Toaster", isCorrect: false }
                ]
            },
            {
                question: "Complete: 'The ___ in the Hat'",
                options: [
                    { text: "Dog", isCorrect: false },
                    { text: "Cat", isCorrect: true },
                    { text: "Fish", isCorrect: false },
                    { text: "Bird", isCorrect: false }
                ]
            }
        ];
        
        return questions[Math.floor(Math.random() * questions.length)];
    }

    validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    }

    validatePassword(password) {
        return password.length >= 8;
    }

    validatePhone(phone) {
        const re = /^[\+]?[1-9][\d]{0,15}$/;
        return re.test(phone.replace(/\D/g, ''));
    }

    showError(elementId, message) {
        const errorElement = document.getElementById(elementId);
        if (errorElement) {
            errorElement.textContent = message;
            errorElement.classList.add('show');
            const inputElement = document.getElementById(elementId.replace('-error', ''));
            if (inputElement) {
                inputElement.classList.add('error');
            }
        }
    }

    clearError(elementId) {
        const errorElement = document.getElementById(elementId);
        if (errorElement) {
            errorElement.textContent = '';
            errorElement.classList.remove('show');
            const inputElement = document.getElementById(elementId.replace('-error', ''));
            if (inputElement) {
                inputElement.classList.remove('error');
            }
        }
    }

    // ===== EVENT HANDLING =====
    bindEvents() {
        // Delegate events to document since content is dynamic
        document.addEventListener('click', (e) => {
            // Enter login button
            if (e.target.id === 'enter-login' || e.target.closest('#enter-login')) {
                e.preventDefault();
                this.currentPage = 'auth';
                this.loadPage('auth');
            }
            
            // Auth tabs
            if (e.target.classList.contains('auth-tab')) {
                const tab = e.target.dataset.tab;
                this.switchAuthTab(tab);
            }
            
            // Toggle auth (login/register)
            if (e.target.classList.contains('toggle-auth')) {
                const target = e.target.dataset.target;
                this.switchAuthTab(target);
            }
            
            // Register type buttons
            if (e.target.classList.contains('register-type-btn')) {
                const type = e.target.dataset.type;
                this.switchRegisterType(type);
            }
            
            // Captcha options
            if (e.target.classList.contains('captcha-option')) {
                this.selectCaptchaOption(e.target);
            }
            
            // Business registration next/prev
            if (e.target.id === 'next-business-step') {
                this.nextBusinessStep();
            }
            
            if (e.target.id === 'prev-business-step') {
                this.prevBusinessStep();
            }
            
            // GSTIN toggle
            if (e.target.name === 'has-gstin') {
                this.toggleGstinField(e.target.value === 'yes');
            }
            
            // Verify email/phone buttons
            if (e.target.id === 'verify-personal-email' || 
                e.target.id === 'verify-business-email' ||
                e.target.id === 'verify-business-phone') {
                this.simulateVerification(e.target.id);
            }
            
            // Form submissions
            if (e.target.classList.contains('submit-btn') || 
                (e.target.classList.contains('nav-btn') && e.target.type !== 'button')) {
                e.preventDefault();
                if (e.target.closest('#login-form')) {
                    this.handleLogin();
                } else if (e.target.closest('#register-form')) {
                    this.handleRegistration();
                }
            }
        });

        // Input validation on blur
        document.addEventListener('focusout', (e) => {
            if (e.target.classList.contains('form-input')) {
                this.validateField(e.target);
            }
        });
    }

    switchAuthTab(tab) {
        this.currentAuthTab = tab;
        this.renderAuthPage(document.getElementById('page-content'));
    }

    switchRegisterType(type) {
        const personalForm = document.getElementById('personal-registration');
        const businessForm = document.getElementById('business-registration');
        const buttons = document.querySelectorAll('.register-type-btn');
        
        buttons.forEach(btn => btn.classList.remove('active'));
        event.target.classList.add('active');
        
        if (type === 'personal') {
            personalForm.style.display = 'block';
            businessForm.style.display = 'none';
        } else {
            personalForm.style.display = 'none';
            businessForm.style.display = 'block';
        }
    }

    selectCaptchaOption(optionElement) {
        const options = document.querySelectorAll('.captcha-option');
        options.forEach(opt => opt.classList.remove('selected'));
        optionElement.classList.add('selected');
        
        const captchaAnswer = document.getElementById('captcha-answer');
        if (captchaAnswer) {
            captchaAnswer.value = optionElement.dataset.answer === 'true' ? 'correct' : 'incorrect';
        }
        
        this.clearError('captcha-error');
    }

    nextBusinessStep() {
        // Validate step 1
        const name = document.getElementById('business-name').value;
        const email = document.getElementById('business-email').value;
        const phone = document.getElementById('business-phone').value;
        const password = document.getElementById('business-password').value;
        const confirm = document.getElementById('business-confirm').value;
        
        let isValid = true;
        
        if (!name.trim()) {
            this.showError('business-name-error', 'Full name is required');
            isValid = false;
        }
        
        if (!this.validateEmail(email)) {
            this.showError('business-email-error', 'Valid email is required');
            isValid = false;
        }
        
        if (!this.validatePhone(phone)) {
            this.showError('business-phone-error', 'Valid phone number is required');
            isValid = false;
        }
        
        if (!this.validatePassword(password)) {
            this.showError('business-password-error', 'Password must be at least 8 characters');
            isValid = false;
        }
        
        if (password !== confirm) {
            this.showError('business-confirm-error', 'Passwords do not match');
            isValid = false;
        }
        
        if (isValid) {
            const currentStep = document.querySelector('.registration-step.active');
            const nextStep = document.querySelector('.registration-step[data-step="2"]');
            
            if (currentStep && nextStep) {
                currentStep.classList.remove('active');
                nextStep.classList.add('active');
            }
        }
    }

    prevBusinessStep() {
        const currentStep = document.querySelector('.registration-step.active');
        const prevStep = document.querySelector('.registration-step[data-step="1"]');
        
        if (currentStep && prevStep) {
            currentStep.classList.remove('active');
            prevStep.classList.add('active');
        }
    }

    toggleGstinField(show) {
        const gstinField = document.getElementById('gstin-field');
        if (gstinField) {
            gstinField.style.display = show ? 'block' : 'none';
            if (show) {
                document.getElementById('gstin-number').required = true;
            } else {
                document.getElementById('gstin-number').required = false;
            }
        }
    }

    simulateVerification(buttonId) {
        const statusMap = {
            'verify-personal-email': 'personal-email-status',
            'verify-business-email': 'business-email-status',
            'verify-business-phone': 'business-phone-status'
        };
        
        const statusId = statusMap[buttonId];
        if (!statusId) return;
        
        const statusElement = document.getElementById(statusId);
        const button = document.getElementById(buttonId);
        
        if (statusElement && button) {
            button.disabled = true;
            button.textContent = 'Sending...';
            statusElement.textContent = 'Verification code sent to your email/phone';
            statusElement.className = 'verification-status pending';
            
            // Simulate verification process
            setTimeout(() => {
                statusElement.textContent = '✓ Verified successfully';
                statusElement.className = 'verification-status verified';
                button.textContent = 'Verified';
                button.style.background = 'var(--flare-secondary)';
            }, 2000);
        }
    }

    validateField(field) {
        const fieldId = field.id;
        const value = field.value.trim();
        
        if (fieldId.includes('email')) {
            if (!this.validateEmail(value)) {
                this.showError(`${fieldId}-error`, 'Please enter a valid email address');
            } else {
                this.clearError(`${fieldId}-error`);
            }
        }
        
        if (fieldId.includes('password') && !fieldId.includes('confirm')) {
            if (!this.validatePassword(value)) {
                this.showError(`${fieldId}-error`, 'Password must be at least 8 characters');
            } else {
                this.clearError(`${fieldId}-error`);
            }
        }
        
        if (fieldId.includes('confirm')) {
            const passwordField = document.getElementById(fieldId.replace('confirm', 'password'));
            if (passwordField && value !== passwordField.value) {
                this.showError(`${fieldId}-error`, 'Passwords do not match');
            } else {
                this.clearError(`${fieldId}-error`);
            }
        }
        
        if (fieldId.includes('phone')) {
            if (!this.validatePhone(value)) {
                this.showError(`${fieldId}-error`, 'Please enter a valid phone number');
            } else {
                this.clearError(`${fieldId}-error`);
            }
        }
    }

    handleLogin() {
        const email = document.getElementById('login-email').value.trim();
        const password = document.getElementById('login-password').value;
        const captchaAnswer = document.getElementById('captcha-answer').value;
        
        let isValid = true;
        
        // Validate email
        if (!this.validateEmail(email)) {
            this.showError('login-email-error', 'Please enter a valid email');
            isValid = false;
        }
        
        // Validate password
        if (!password) {
            this.showError('login-password-error', 'Please enter your password');
            isValid = false;
        }
        
        // Validate captcha
        if (captchaAnswer !== 'correct') {
            this.showError('captcha-error', 'Please select the correct answer');
            isValid = false;
        }
        
        if (isValid) {
            // Check if user exists
            const user = this.users.find(u => u.email === email && u.password === password);
            
            if (user) {
                // Successful login
                this.currentUser = user;
                localStorage.setItem('flarebook_current_user', JSON.stringify(user));
                
                // Show success message
                alert(`Welcome back, ${user.name}! Login successful.`);
                
                // Redirect to home (in a real app, this would navigate to dashboard)
                this.currentPage = 'home';
                this.loadPage('home');
                
                // Update UI to show user is logged in
                this.updateAuthState();
            } else {
                // Invalid credentials
                this.showError('login-password-error', 'Invalid email or password');
            }
        }
    }

    handleRegistration() {
        // Determine which form is active
        const personalForm = document.getElementById('personal-registration');
        const isPersonal = personalForm && personalForm.style.display !== 'none';
        
        if (isPersonal) {
            this.registerPersonal();
        } else {
            this.registerBusiness();
        }
    }

    registerPersonal() {
        const name = document.getElementById('personal-name').value.trim();
        const email = document.getElementById('personal-email').value.trim();
        const password = document.getElementById('personal-password').value;
        const confirm = document.getElementById('personal-confirm').value;
        
        let isValid = true;
        
        // Validate all fields
        if (!name) {
            this.showError('personal-name-error', 'Full name is required');
            isValid = false;
        }
        
        if (!this.validateEmail(email)) {
            this.showError('personal-email-error', 'Valid email is required');
            isValid = false;
        }
        
        if (!this.validatePassword(password)) {
            this.showError('personal-password-error', 'Password must be at least 8 characters');
            isValid = false;
        }
        
        if (password !== confirm) {
            this.showError('personal-confirm-error', 'Passwords do not match');
            isValid = false;
        }
        
        if (isValid) {
            // Check if user already exists
            if (this.users.find(u => u.email === email)) {
                this.showError('personal-email-error', 'An account with this email already exists');
                return;
            }
            
            // Create user object
            const user = {
                id: Date.now(),
                name,
                email,
                password, // In real app, this would be hashed
                type: 'personal',
                createdAt: new Date().toISOString()
            };
            
            // Save to local storage
            this.users.push(user);
            localStorage.setItem('flarebook_users', JSON.stringify(this.users));
            
            // Auto login
            this.currentUser = user;
            localStorage.setItem('flarebook_current_user', JSON.stringify(user));
            
            // Show success
            alert(`Welcome to FlareBook, ${name}! Your account has been created.`);
            
            // Redirect
            this.currentPage = 'home';
            this.loadPage('home');
        }
    }

    registerBusiness() {
        // This would handle business registration
        // For now, just show a success message
        alert('Business registration form submitted successfully! (Backend integration pending)');
        
        // Switch to login
        this.switchAuthTab('login');
    }

    updateAuthState() {
        // This would update UI based on authentication state
        // For example, show user menu instead of login button
        console.log('User logged in:', this.currentUser);
    }
}

// Initialize the application when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    window.flareBookApp = new FlareBookStore();
});