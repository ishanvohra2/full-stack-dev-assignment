<script>
    import { goto } from '$app/navigation';
    import { onMount } from 'svelte';
    import lottie from 'lottie-web';
  
    // Questions array
    const questions = [
      {
        id: 1,
        question: "What's your goal?",
        options: [
          { icon: "🌐", text: "Career and business" },
          { icon: "👶", text: "Lessons for kids" },
          { icon: "📚", text: "Exams and course work" },
          { icon: "🎨", text: "Culture, travel and hobby" }
        ]
      },
      {
        id: 2,
        question: "What's your goal?",
        options: [
          { icon: "🌐", text: "Career and business" },
          { icon: "👶", text: "Lessons for kids" },
          { icon: "📚", text: "Exams and course work" },
          { icon: "🎨", text: "Culture, travel and hobby" }
        ]
      },
      {
        id: 3,
        question: "What's your goal?",
        options: [
          { icon: "🌐", text: "Career and business" },
          { icon: "👶", text: "Lessons for kids" },
          { icon: "📚", text: "Exams and course work" },
          { icon: "🎨", text: "Culture, travel and hobby" }
        ]
      },
      // Add more questions here
    ];
  
    let currentQuestionIndex = 0;
    let selectedOption = null;
  
    onMount(() => {
      const initAnimation = async () => {
        try {
          // If the file is in the static folder
          const animation = lottie.loadAnimation({
            container: document.querySelector('.lottie-container'),
            renderer: 'svg',
            loop: true,
            autoplay: true,
            path: '/onboarding.json' // Note: path starts from static folder
          });

          return () => animation.destroy();
        } catch (error) {
          console.error('Error loading animation:', error);
        }
  };

  initAnimation();
});

    async function handleNext() {
      if (currentQuestionIndex < questions.length - 1) {
        currentQuestionIndex++;
        selectedOption = null;
      } else {
        // Navigate to home when all questions are answered
        await goto('/home');
      }
    }
  
    function handleSkip() {
      handleNext();
    }
  
    function handleOptionSelect(index) {
      selectedOption = index;
      // Auto-advance after short delay
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
      <div class="question-container">
        <h1>{questions[currentQuestionIndex].question}</h1>
        
        <div class="options-list">
          {#each questions[currentQuestionIndex].options as option, index}
            <button
              class="option-button"
              class:selected={selectedOption === index}
              on:click={() => handleOptionSelect(index)}
            >
              <span class="option-icon">{option.icon}</span>
              <span class="option-text">{option.text}</span>
              <span class="check-icon">✓</span>
            </button>
          {/each}
        </div>
  
        <button class="skip-button" on:click={handleSkip}>
          Skip this question
        </button>
      </div>
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
  
    .back-button {
      position: absolute;
      top: 2rem;
      left: 2rem;
      background: none;
      border: none;
      cursor: pointer;
      padding: 0.5rem;
    }
  
    .back-button:hover {
      opacity: 0.7;
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
  
    .skip-button {
      width: 100%;
      padding: 1rem;
      border: 1px solid #333;
      border-radius: 0.5rem;
      background: none;
      cursor: pointer;
      transition: all 0.2s;
    }
  
    .skip-button:hover {
      background-color: #f5f5f5;
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
  </style>