<!-- src/routes/+page.svelte -->
<script>
  let languages = [ "English", "Spanish", "French", "German", "Japanese", "Chinese", "Hindi" ]; // Selected language let selectedLanguage = languages[0];
  let selectedLanguage = languages[0];
  const progress = 95;
  
  const grammarLessons = [
    { title: 'Basic Grammar Introduction', completed: true },
    { title: 'Present Simple Tense', completed: false },
    { title: 'Past Simple Tense', completed: false },
    { title: 'Future Tense Forms', completed: false },
    { title: 'Modal Verbs Usage', completed: false }
  ];

  const audioExercises = [
    { title: 'Pronunciation Basics', completed: false },
    { title: 'Common Phrases', completed: false },
    { title: 'Daily Conversations', completed: false },
    { title: 'Business English', completed: false },
    { title: 'Advanced Speaking', completed: false }
  ];

  const vocabularyList = [
    { title: 'Essential Words', completed: false },
    { title: 'Business Vocabulary', completed: false },
    { title: 'Academic Terms', completed: false },
    { title: 'Idioms & Phrases', completed: false },
    { title: 'Advanced Vocabulary', completed: false }
  ];
</script>

<div class="app">
  <nav class="sidebar">
    <div class="logo">Lingo</div>
    <button class="nav-button active">
      <span class="material-icons">school</span>
      <span>LEARN</span>
    </button>
    <button class="nav-button">
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
            <div class="lesson-item">
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
            <div class="lesson-item">
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
            <div class="lesson-item">
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
  }
  
  .lesson-item:hover {
    background-color: #f8f8ff;
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

  .lesson-item:hover .arrow {
    transform: translateX(4px);
    color: #ff4f99;
  }
  .headerRow { display: flex; flex-direction: row; } 
  .headerItem { margin: 0 10px; }
</style>