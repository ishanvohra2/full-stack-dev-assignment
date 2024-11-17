<script>
  import { goto } from '$app/navigation';
  import { onMount } from 'svelte';
  import lottie from 'lottie-web';
  import apiService from '$lib/apiService/apiService';

  // Initialize with empty array
  let questions = [];
  let loading = true;
  let error = null;
  let currentQuestionIndex = 0;
  let selectedOption = null;
  let mounted = false;

  onMount(async () => {
      mounted = true;
      try {
          loading = true;
          const data = await apiService.getOnboardingQuestions();
          if (!data?.questions_list) {
              throw new Error('Invalid response format');
          }
          questions = data.questions_list;
          console.log("QUESTIONS: ", questions)
      } catch (err) {
          error = 'Failed to load questions. Please try again.';
          console.error('Error loading questions:', err);
      } finally {
          loading = false;
      }

      const initAnimation = async () => {
          try {
              if (!mounted) return;
              
              const animation = lottie.loadAnimation({
                  container: document.querySelector('.lottie-container'),
                  renderer: 'svg',
                  loop: true,
                  autoplay: true,
                  path: '/onboarding.json'
              });

              return () => {
                  if (animation) animation.destroy();
              };
          } catch (error) {
              console.error('Error loading animation:', error);
          }
      };

      const cleanup = await initAnimation();
      return () => {
          mounted = false;
          if (cleanup) cleanup();
      };
  });

  async function handleNext() {
      if (!questions || currentQuestionIndex >= questions.length - 1) {
          await goto('/home');
          return;
      }
      currentQuestionIndex++;
      selectedOption = null;
  }

  function handleOptionSelect(index) {
      selectedOption = index;
      setTimeout(handleNext, 800);
  }
</script>

<header>
  <div class="logo">Lingo</div>
</header>

<main>
  <div class="container">
      <!-- Left side - Lottie animation -->
      <div class="lottie-container"></div>

      <!-- Right side - Question form -->
      {#if loading}
          <div class="loading-container">
              <div class="spinner"></div>
              <p>Loading questions...</p>
          </div>
      {:else if error}
          <div class="error-message">
              {error}
          </div>
      {:else if !questions || questions.length === 0}
          <div class="error-message">
              No questions available
          </div>
      {:else if questions[currentQuestionIndex]}
          <div class="question-container">
              <h1>{questions[currentQuestionIndex].question}</h1>
              
              <div class="options-list">
                  {#each questions[currentQuestionIndex].options as option, index}
                      <button
                          class="option-button"
                          class:selected={selectedOption === index}
                          on:click={() => handleOptionSelect(index)}>

                          <span class="option-icon">{option.icon}</span>
                          <span class="option-text">{option.text}</span>
                          <span class="check-icon">✓</span>
                      </button>
                  {/each}
              </div>
          </div>
      {/if}
  </div>
</main>
  
  <style>
    header {
      padding: 20px 20px;
    }

    main {
      min-height: 100vh;
      background-color: #fdf2f4;
      padding: 2rem;
    }
  
    .container {
      max-width: 1200px;
      margin: 0 auto;
      display: flex;
      gap: 4rem;
      position: relative;
    }
  
    .lottie-container {
      flex: 1;
      max-width: 500px;
    }
  
    .question-container {
      flex: 1;
      padding: 2rem;
    }
  
    h1 {
      font-size: 48px;
      font-weight: bold;
      margin: 0 0 20px 0;
      line-height: 1.2;
    }

    .logo {
      font-size: 24px;
      font-weight: bold;
    }
  
    .options-list {
      display: flex;
      flex-direction: column;
      gap: 1rem;
      margin-bottom: 2rem;
    }
  
    .option-button {
      display: flex;
      align-items: center;
      padding: 1rem;
      border: 1px solid #ddd;
      border-radius: 0.5rem;
      background: white;
      cursor: pointer;
      transition: all 0.2s;
      width: 100%;
      text-align: left;
    }
  
    .option-button:hover {
      border-color: #ff4f84;
    }
  
    .option-button.selected {
      border-color: #ff4f84;
      background-color: #fff9fa;
    }
  
    .option-icon {
      font-size: 1.5rem;
      margin-right: 1rem;
    }
  
    .option-text {
      flex: 1;
      font-size: 1rem;
    }
  
    .check-icon {
      opacity: 0;
      color: #ff4f84;
    }
  
    .option-button.selected .check-icon {
      opacity: 1;
    }
  
    @media (max-width: 768px) {
      .container {
        flex-direction: column;
        gap: 2rem;
      }
  
      .lottie-container {
        max-width: 100%;
        height: 300px;
      }
    }

    .loading-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100vh;
    }

    .spinner {
        width: 40px;
        height: 40px;
        border: 4px solid #f3f3f3;
        border-top: 4px solid #3498db;
        border-radius: 50%;
        animation: spin 1s linear infinite;
    }

    .error-message {
        color: red;
        text-align: center;
        padding: 20px;
    }

    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
  </style>