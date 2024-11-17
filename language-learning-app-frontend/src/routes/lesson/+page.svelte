<!-- src/routes/lesson/+page.svelte -->
<script>
    import { page } from '$app/stores';
    import { goto } from '$app/navigation';
    
    // Get lesson type and ID from URL params (you'll need to set up routing)
    $: lessonType = $page.url.searchParams.get('type') || 'grammar';
    $: lessonId = $page.url.searchParams.get('id') || '1';
    
    // Lesson content based on type
    const lessonContent = {
      grammar: {
        title: 'Basic Grammar Introduction',
        sections: [
          {
            type: 'explanation',
            content: 'Learn the fundamentals of English grammar structure.',
            examples: ['Subject + Verb + Object', 'The cat (S) drinks (V) milk (O)']
          },
          {
            type: 'exercise',
            question: 'Complete the sentence with correct word order:',
            options: ['drinks / cat / milk / the', 'the / cat / drinks / milk', 'milk / drinks / the / cat'],
            correct: 1
          }
        ]
      },
      audio: {
        title: 'Pronunciation Basics',
        sections: [
          {
            type: 'audio',
            title: 'Basic Vowel Sounds',
            audioUrl: '/lessons/audio/vowels.mp3',
            transcript: 'Repeat after me: A E I O U'
          },
          {
            type: 'practice',
            words: ['cat', 'pet', 'sit', 'hot', 'cut'],
            recordings: []
          }
        ]
      },
      vocabulary: {
        title: 'Essential Words',
        sections: [
          {
            type: 'flashcard',
            words: [
              { word: 'Hello', translation: 'Hola', example: 'Hello, how are you?' },
              { word: 'Goodbye', translation: 'Adiós', example: 'Goodbye, see you tomorrow!' }
            ]
          },
          {
            type: 'quiz',
            questions: [
              { word: 'Hello', options: ['Hola', 'Adiós', 'Gracias'], correct: 0 }
            ]
          }
        ]
      }
    };
  
    let currentSection = 0;
    let selectedAnswer = null;
    let isCorrect = null;
    let progress = 0;
  
    async function nextSection() {
    if (currentSection < lessonContent[lessonType].sections.length - 1) {
        currentSection++;
        updateProgress();
    } else {
        // Last section completed
        try {
            await apiService.updateLessonProgress(lessonType, lessonId);
            goto('/home');
        } catch (error) {
            console.error('Error updating progress:', error);
        }
    }
}
  
    function previousSection() {
      if (currentSection > 0) {
        currentSection--;
        updateProgress();
      }
    }
  
    function updateProgress() {
      progress = ((currentSection + 1) / lessonContent[lessonType].sections.length) * 100;
    }
  
    function checkAnswer(answer) {
      selectedAnswer = answer;
      const section = lessonContent[lessonType].sections[currentSection];
      if (section.type === 'exercise' || section.type === 'quiz') {
        isCorrect = answer === section.correct;
      }
    }
  
    function goBack() {
      goto('/home');
    }
    
  </script>
  
  <div class="app">
    <main class="content">
      <div class="header">
        <button class="back-button" on:click={goBack}>
          <span class="material-icons">arrow_back</span>
          Back
        </button>
        <h1>{lessonContent[lessonType].title}</h1>
      </div>
  
      <div class="progress-container">
        <div class="progress-bar">
          <div class="progress-fill" style="width: {progress}%"></div>
        </div>
        <div class="progress-text">{progress}% completed</div>
      </div>
  
      <div class="lesson-container">
        {#if lessonContent[lessonType]}
          {@const section = lessonContent[lessonType].sections[currentSection]}
          
          {#if section.type === 'explanation'}
            <div class="explanation-section">
              <p>{section.content}</p>
              <div class="examples">
                {#each section.examples as example}
                  <div class="example-item">{example}</div>
                {/each}
              </div>
            </div>
          {:else if section.type === 'exercise' || section.type === 'quiz'}
            <div class="exercise-section">
              <h3>{section.question}</h3>
              <div class="options">
                {#each section.options as option, i}
                  <button 
                    class="option-button"
                    class:selected={selectedAnswer === i}
                    class:correct={isCorrect && selectedAnswer === i}
                    class:incorrect={!isCorrect && selectedAnswer === i}
                    on:click={() => checkAnswer(i)}
                  >
                    {option}
                  </button>
                {/each}
              </div>
            </div>
          {:else if section.type === 'audio'}
            <div class="audio-section">
              <h3>{section.title}</h3>
              <audio controls src={section.audioUrl}></audio>
              <p class="transcript">{section.transcript}</p>
            </div>
          {:else if section.type === 'flashcard'}
            <div class="flashcard-section">
              {#each section.words as word}
                <div class="flashcard">
                  <div class="word">{word.word}</div>
                  <div class="translation">{word.translation}</div>
                  <div class="example">{word.example}</div>
                </div>
              {/each}
            </div>
          {/if}
        {/if}
      </div>
  
      <div class="navigation-buttons">
        <button 
          class="nav-button"
          disabled={currentSection === 0}
          on:click={previousSection}
        >
          <span class="material-icons">arrow_back</span>
          Previous
        </button>
        <button 
          class="nav-button"
          disabled={currentSection === lessonContent[lessonType].sections.length - 1}
          on:click={nextSection}
        >
          Next
          <span class="material-icons">arrow_forward</span>
        </button>
      </div>
    </main>
  </div>
  
  <style>
    .app {
      display: flex;
      height: 100vh;
      background-color: #FAFAFA;
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }

    .content {
      flex: 1;
      padding: 2rem 3rem;
      overflow-y: auto;
    }
  
    .back-button {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      background: none;
      border: none;
      color: #666;
      cursor: pointer;
      padding: 0.5rem;
      border-radius: 4px;
    }
  
    .back-button:hover {
      background-color: #f0f0f0;
    }
  
    .lesson-container {
      background: white;
      padding: 2rem;
      border-radius: 12px;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
      margin: 2rem 0;
      min-height: 400px;
    }
  
    .navigation-buttons {
      display: flex;
      justify-content: space-between;
      margin-top: 2rem;
    }
  
    .nav-button {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.75rem 1.5rem;
      border: none;
      background-color: #ff4f99;
      color: white;
      border-radius: 8px;
      cursor: pointer;
      transition: all 0.2s ease;
    }
  
    .nav-button:disabled {
      background-color: #ccc;
      cursor: not-allowed;
    }
  
    .nav-button:not(:disabled):hover {
      background-color: #e6447a;
    }
  
    .explanation-section, .exercise-section, .audio-section, .flashcard-section {
      max-width: 800px;
      margin: 0 auto;
    }
  
    .examples {
      margin-top: 1.5rem;
    }
  
    .example-item {
      background-color: #f8f8ff;
      padding: 1rem;
      border-radius: 8px;
      margin: 0.5rem 0;
    }
  
    .options {
      display: flex;
      flex-direction: column;
      gap: 1rem;
      margin-top: 1.5rem;
    }
  
    .option-button {
      padding: 1rem;
      border: 2px solid #eee;
      border-radius: 8px;
      background: none;
      cursor: pointer;
      transition: all 0.2s ease;
      text-align: left;
    }
  
    .option-button:hover {
      border-color: #ff4f99;
    }
  
    .option-button.selected {
      border-color: #ff4f99;
    }
  
    .option-button.correct {
      border-color: #4CAF50;
      background-color: #E8F5E9;
    }
  
    .option-button.incorrect {
      border-color: #F44336;
      background-color: #FFEBEE;
    }
  
    .audio-section {
      text-align: center;
    }
  
    .audio-section audio {
      margin: 1.5rem 0;
      width: 100%;
      max-width: 500px;
    }
  
    .transcript {
      color: #666;
      font-style: italic;
    }
  
    .flashcard-section {
      display: flex;
      flex-wrap: wrap;
      gap: 1.5rem;
      justify-content: center;
    }
  
    .flashcard {
      background-color: #f8f8ff;
      padding: 1.5rem;
      border-radius: 12px;
      width: 300px;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    }
  
    .flashcard .word {
      font-size: 1.5rem;
      font-weight: 600;
      margin-bottom: 0.5rem;
    }
  
    .flashcard .translation {
      color: #ff4f99;
      font-size: 1.25rem;
      margin-bottom: 1rem;
    }
  
    .flashcard .example {
      color: #666;
      font-style: italic;
    }

  .progress-container {
    background: white;
    padding: 1.5rem;
    border-radius: 12px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    margin-bottom: 2rem;
  }
  .progress-bar {
    height: 10px;
    background-color: #f0f0f0;
    border-radius: 5px;
    overflow: hidden;
  }

  .progress-fill {
    height: 100%;
    background-color: #ff4f99;
    transition: width 0.3s ease;
  }

  .progress-text {
    color: #666;
    font-size: 0.925rem;
    margin-top: 0.75rem;
    font-weight: 500;
  }
  </style>