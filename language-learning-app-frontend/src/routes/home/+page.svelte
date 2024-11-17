<script>
  import { goto } from '$app/navigation';
  import { onMount } from 'svelte';
  import apiService from '$lib/apiService/apiService';

  let languages = [];
  let selectedLanguage = null;
  let progress = 95;
  let loading = true;
  let error = null;
  
  let grammarLessons = [];
  let audioExercises = [];
  let vocabularyList = [];

  onMount(async () => {
    try {
      // Fetch available languages
      const profile = await apiService.getUserProfile()
      languages = profile.languages
      selectedLanguage = languages[0].language;
      console.log("SELECTED LANGUAGE", selectedLanguage)
      // Load initial lessons
      await loadLessons(selectedLanguage);
      
      // Get user profile for progress
      const userProfile = await apiService.getUserProfile();
      if (userProfile.progress) {
        progress = userProfile.progress;
      }
    } catch (err) {
      error = 'Failed to load initial data. Please try again.';
      console.error('Initialization error:', err);
    } finally {
      loading = false;
    }
  });

  async function loadLessons(language) {
    try {
      loading = true;
      const lessonsData = await apiService.getLessons(language);
      
      // Sort lessons into their respective categories
      grammarLessons = lessonsData.grammar.sections.map((lesson, index) => ({
        id: (index + 1).toString(),
        title: lesson.content.split('.')[0], // Take first sentence as title
        completed: false // You might want to track this in your backend
      }));

      audioExercises = lessonsData.audio.sections
        .filter(section => section.type === 'audio')
        .map((exercise, index) => ({
          id: (index + 1).toString(),
          title: exercise.title,
          completed: false
        }));

      vocabularyList = lessonsData.vocabulary.sections.map((section, index) => ({
        id: (index + 1).toString(),
        title: section.type === 'flashcard' ? `Flashcard Set ${index + 1}` : 'Vocabulary Set',
        completed: false
      }));

    } catch (err) {
      error = 'Failed to load lessons. Please try again.';
      console.error('Error loading lessons:', err);
    } finally {
      loading = false;
    }
  }

  // Watch for language changes
  $: if (selectedLanguage) {
    loadLessons(selectedLanguage);
  }

  async function navigateTo(destination) {
    await goto(destination);
  }

  async function openLesson(type, id) {
    try {
      await goto(`/lesson?type=${type}&id=${id}&language=${selectedLanguage}`);
    } catch (err) {
      console.error('Navigation error:', err);
      error = 'Failed to open lesson. Please try again.';
    }
  }
</script>

<div class="app">
  <nav class="sidebar">
    <div class="logo">Lingo</div>
    <button class="nav-button active">
      <span class="material-icons">school</span>
      <span>LEARN</span>
    </button>
    <button class="nav-button" on:click={() => navigateTo('/profile')}>
      <span class="material-icons">person</span>
      <span>PROFILE</span>
    </button>
  </nav>
  
  <main class="content">
    {#if loading}
      <div class="loading">Loading...</div>
    {:else if error}
      <div class="error">
        {error}
        <button on:click={() => window.location.reload()}>Retry</button>
      </div>
    {:else}
      <div class="header">
        <div>
          <h1>Welcome back!</h1>
          <div class="headerRow">
            <div class="headerItem">
              <p class="subtitle">Learn</p>
            </div>
            <div class="headerItem">
              <select bind:value={selectedLanguage}> 
                {#each languages as language} 
                  <option value={language}>{language}</option>
                {/each} 
              </select>
            </div>
          </div>
        </div>
      </div>
      
      <div class="progress-container">
        <div class="progress-bar">
          <div class="progress-fill" style="width: {progress}%"></div>
        </div>
        <div class="progress-text">{progress}% completed</div>
      </div>
      
      <div class="sections-grid">
        <section class="lesson-section">
          <h2>Grammar Lessons</h2>
          <div class="lesson-list">
            {#each grammarLessons as lesson}
              <div 
                class="lesson-item"
                on:click={() => openLesson('grammar', lesson.id)}
                on:keydown={(e) => e.key === 'Enter' && openLesson('grammar', lesson.id)}
                tabindex="0"
                role="button"
                aria-label={`Open ${lesson.title} grammar lesson`}
              >
                <div class="lesson-info">
                  <span class="material-icons icon">{lesson.completed ? 'check_circle' : 'play_circle'}</span>
                  <span class="lesson-title">{lesson.title}</span>
                </div>
                <span class="material-icons arrow">chevron_right</span>
              </div>
            {/each}
          </div>
        </section>
        
        <section class="lesson-section">
          <h2>Audio Exercises</h2>
          <div class="lesson-list">
            {#each audioExercises as exercise}
              <div 
                class="lesson-item"
                on:click={() => openLesson('audio', exercise.id)}
                on:keydown={(e) => e.key === 'Enter' && openLesson('audio', exercise.id)}
                tabindex="0"
                role="button"
                aria-label={`Open ${exercise.title} audio exercise`}
              >
                <div class="lesson-info">
                  <span class="material-icons icon">headphones</span>
                  <span class="lesson-title">{exercise.title}</span>
                </div>
                <span class="material-icons arrow">chevron_right</span>
              </div>
            {/each}
          </div>
        </section>
        
        <section class="lesson-section">
          <h2>Vocabulary List</h2>
          <div class="lesson-list">
            {#each vocabularyList as item}
              <div 
                class="lesson-item"
                on:click={() => openLesson('vocabulary', item.id)}
                on:keydown={(e) => e.key === 'Enter' && openLesson('vocabulary', item.id)}
                tabindex="0"
                role="button"
                aria-label={`Open ${item.title} vocabulary lesson`}
              >
                <div class="lesson-info">
                  <span class="material-icons icon">menu_book</span>
                  <span class="lesson-title">{item.title}</span>
                </div>
                <span class="material-icons arrow">chevron_right</span>
              </div>
            {/each}
          </div>
        </section>
      </div>
    {/if}
  </main>
</div>

<style>
  .app {
    display: flex;
    height: 100vh;
    background-color: #FAFAFA;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  }
  
  .sidebar {
    width: 100px;
    background-color: white;
    padding: 1.5rem 1rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1.5rem;
    box-shadow: 2px 0 8px rgba(0, 0, 0, 0.05);
  }
  
  .logo {
    font-weight: bold;
    font-size: 1.25rem;
    color: #333;
    margin-bottom: 1rem;
  }
  
  .nav-button {
    width: 100%;
    padding: 0.75rem;
    border: none;
    background: none;
    cursor: pointer;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.5rem;
    font-size: 0.75rem;
    color: #666;
    border-radius: 8px;
    transition: all 0.2s ease;
  }

  .nav-button.active {
    background-color: #f0f0ff;
    color: #8f003b;
  }
  
  .nav-button:hover {
    background-color: #f5f5f5;
  }
  
  .content {
    flex: 1;
    padding: 2rem 3rem;
    overflow-y: auto;
  }
  
  .header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 2rem;
  }
  
  h1 {
    margin: 0;
    font-size: 2rem;
    color: #1a1a1a;
    font-weight: 600;
  }
  
  .subtitle {
    margin: 0.5rem 0 0;
    color: #666;
    font-size: 1.1rem;
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
  
  .sections-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
  }
  
  .lesson-section {
    background: white;
    padding: 1.5rem;
    border-radius: 12px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
  }
  
  h2 {
    font-size: 1.25rem;
    margin: 0 0 1.25rem;
    color: #333;
    font-weight: 600;
  }
  
  .lesson-list {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
  }
  
  .lesson-item {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0.75rem;
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.2s ease;
    outline: none;
  }
  
  .lesson-item:hover, .lesson-item:focus {
    background-color: #f8f8ff;
  }

  .lesson-item:focus-visible {
    box-shadow: 0 0 0 2px #ff4f99;
  }

  .lesson-info {
    display: flex;
    align-items: center;
    gap: 0.75rem;
  }

  .lesson-title {
    font-size: 0.95rem;
    color: #4a4a4a;
  }

  .icon {
    color: #ff4f99;
  }

  .arrow {
    color: #ccc;
    transition: transform 0.2s ease;
  }

  .lesson-item:hover .arrow,
  .lesson-item:focus .arrow {
    transform: translateX(4px);
    color: #ff4f99;
  }
  
  .headerRow { 
    display: flex; 
    flex-direction: row; 
  } 
  
  .headerItem { 
    margin: 0 10px; 
  }

  .loading {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
    font-size: 1.2rem;
    color: #666;
  }

  .error {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
    padding: 2rem;
    color: #d32f2f;
    text-align: center;
  }

  .error button {
    padding: 0.5rem 1rem;
    background-color: #ff4f99;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.2s ease;
  }

  .error button:hover {
    background-color: #ff1a75;
  }
</style>