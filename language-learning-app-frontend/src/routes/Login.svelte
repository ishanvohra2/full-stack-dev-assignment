<script>
  import apiService from '$lib/apiService/apiService';
  import { auth } from '$lib/firebase';
    import { GoogleAuthProvider, signInWithPopup } from 'firebase/auth';
    import { authStore } from '$lib/stores/authStores';
    import { goto } from '$app/navigation';
    import image from '../assets/undraw_teacher_re_sico.svg'
    let selectedLanguage = "English";
    let loading = false;
    let error = null;

    //TODO Get from server
    const languages = [
      "English",
      "Spanish",
      "French",
      "German",
      "Chinese",
      "Japanese"
    ];
  
    async function handleGoogleSignIn() {
        loading = true;
        error = null;
        
        try {
            const provider = new GoogleAuthProvider();
            const result = await signInWithPopup(auth, provider);
            
            // Get ID token
            const token = await result.user.getIdToken();
            
            console.log("AUTH TOKEN: ", token)

            // Store user and token in auth store
            authStore.setUser(result.user, token);

            // Verify token with backend
            await apiService.verifyGoogleToken(token);
            authStore.setUser(result.user, token);

            // Navigate to onboarding
            await goto('/onboarding', {
                invalidateAll: true
            });
        } catch (err) {
            console.error('Authentication error:', err);
            error = 'Failed to sign in with Google. Please try again.';
        } finally {
            loading = false;
        }
    }
  </script>
  
  <header>
    <div class="logo">Lingo</div>
  </header>

  <div class="container">
  
    <main>
      <div class="content">
        <h1>Find the right tutor for you.</h1>
        
        <p class="subtitle">
          Tell us how you'd like to learn to get a personalized choice of tutors
        </p>
        
        <div class="form-group">
          <label for="language">What do you want to learn?</label>
          
          <select id="language" bind:value={selectedLanguage}>
            {#each languages as language}
              <option value={language}>{language}</option>
            {/each}
          </select>
          
          <button on:click={handleGoogleSignIn} disabled={loading}>
            {#if loading}
                Loading...
            {:else}
                Get started with Google
                <svg viewBox="0 0 20 20" fill="currentColor">
                    <path d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" />
                </svg>
            {/if}
        </button>

        {#if error}
            <p class="error-message">{error}</p>
        {/if}
        </div>
      </div>
      
      <div class="image-container">
        <div class="image-wrapper">
          <img
            src={image}
            alt="Graphic"
          />
        </div>
      </div>
    </main>
  </div>
  
  <style>
    .container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 20px;
    }
  
    header {
      padding: 20px 20px;
    }
  
    .logo {
      font-size: 24px;
      font-weight: bold;
    }
  
    main {
      display: flex;
      gap: 48px;
      align-items: center;
      padding: 40px 0;
    }
  
    .content {
      flex: 1;
    }
  
    h1 {
      font-size: 48px;
      font-weight: bold;
      margin: 0 0 20px 0;
      line-height: 1.2;
    }
  
    .subtitle {
      font-size: 18px;
      color: #666;
      margin-bottom: 32px;
    }
  
    .form-group {
      display: flex;
      flex-direction: column;
      gap: 16px;
      max-width: 400px;
    }
  
    label {
      font-size: 14px;
      font-weight: 500;
      color: #333;
    }
  
    select {
      padding: 12px;
      border: 1px solid #ccc;
      border-radius: 8px;
      font-size: 16px;
      width: 100%;
    }
  
    select:focus {
      outline: none;
      border-color: #ff4f99;
      box-shadow: 0 0 0 2px rgba(255, 79, 153, 0.2);
    }
  
    button {
      display: inline-flex;
      align-items: center;
      padding: 12px 24px;
      background-color: #ff4f99;
      color: white;
      border: none;
      border-radius: 8px;
      font-size: 16px;
      cursor: pointer;
      transition: background-color 0.2s;
    }
  
    button:hover {
      background-color: #ff1a85;
    }
  
    button svg {
      width: 16px;
      height: 16px;
      margin-left: 8px;
    }
  
    .image-container {
      flex: 1;
      position: relative;
    }
  
    .image-wrapper {
      position: relative;
      width: 100%;
      aspect-ratio: 1;
    }
  
    .image-wrapper img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      border-radius: 8px;
      position: relative;
      z-index: 2;
    }
  
    .image-wrapper::before,
    .image-wrapper::after {
      content: '';
      position: absolute;
      border-radius: 8px;
      background-color: #f5f5f5;
    }
  
    .image-wrapper::before {
      top: 16px;
      left: -16px;
      right: -16px;
      bottom: -16px;
      z-index: 1;
    }
  
    .image-wrapper::after {
      top: 32px;
      left: -32px;
      right: -32px;
      bottom: -32px;
      z-index: 0;
      background-color: #fafafa;
    }
  
    @media (max-width: 768px) {
      main {
        flex-direction: column;
      }
  
      h1 {
        font-size: 36px;
      }
  
      .image-container {
        width: 100%;
        max-width: 500px;
        margin: 0 auto;
      }
    }

    .error-message {
        color: #ff4444;
        font-size: 0.9rem;
        margin-top: 0.5rem;
    }

    button:disabled {
        opacity: 0.7;
        cursor: not-allowed;
    }
  </style>