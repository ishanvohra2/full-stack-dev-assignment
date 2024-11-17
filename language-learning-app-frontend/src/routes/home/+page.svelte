<!-- src/routes/+page.svelte -->
<script>
  import { goto } from '$app/navigation';
  let languages = ["English", "Spanish", "French", "German", "Japanese", "Chinese", "Hindi"];
  let selectedLanguage = languages[0];
  const progress = 95;
  
  const grammarLessons = [
    { id: '1', title: 'Basic Grammar Introduction', completed: true },
    { id: '2', title: 'Present Simple Tense', completed: false },
    { id: '3', title: 'Past Simple Tense', completed: false },
    { id: '4', title: 'Future Tense Forms', completed: false },
    { id: '5', title: 'Modal Verbs Usage', completed: false }
  ];

  const audioExercises = [
    { id: '1', title: 'Pronunciation Basics', completed: false },
    { id: '2', title: 'Common Phrases', completed: false },
    { id: '3', title: 'Daily Conversations', completed: false },
    { id: '4', title: 'Business English', completed: false },
    { id: '5', title: 'Advanced Speaking', completed: false }
  ];

  const vocabularyList = [
    { id: '1', title: 'Essential Words', completed: false },
    { id: '2', title: 'Business Vocabulary', completed: false },
    { id: '3', title: 'Academic Terms', completed: false },
    { id: '4', title: 'Idioms & Phrases', completed: false },
    { id: '5', title: 'Advanced Vocabulary', completed: false }
  ];

  async function navigateTo(destination) {
    await goto(destination);
  }

  async function openLesson(type, id) {
    await goto(`/lesson?type=${type}&id=${id}`);
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
        <h2>Vocabulary list</h2>
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
</style>