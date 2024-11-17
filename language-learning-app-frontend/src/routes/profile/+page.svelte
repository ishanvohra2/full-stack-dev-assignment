<script>
  import { goto } from "$app/navigation";
  let languages = ["English", "Spanish", "French", "German", "Japanese", "Chinese", "Hindi"];
  let selectedLanguage = languages[0];

  const userProfile = {
    name: "John Doe",
    email: "john.doe@example.com",
    joinDate: "January 2024",
    streakDays: 15,
    totalPoints: 2750,
    learningLanguages: [
      { language: "Spanish", level: "Intermediate", progress: 65 },
      { language: "French", level: "Beginner", progress: 25 }
    ],
    achievements: [
      { title: "Fast Learner", description: "Completed 5 lessons in one day", icon: "speed" },
      { title: "Consistent", description: "Maintained a 7-day streak", icon: "auto_awesome" },
      { title: "Vocabulary Master", description: "Learned 100 new words", icon: "stars" }
    ],
    recentActivity: [
      { action: "Completed lesson", title: "Basic Grammar Introduction", date: "2 days ago", icon: "task_alt" },
      { action: "Earned achievement", title: "Fast Learner", date: "3 days ago", icon: "emoji_events" },
      { action: "Started course", title: "Business English", date: "1 week ago", icon: "play_circle" }
    ]
  };

  function addNewLanguage() {
    if (!userProfile.learningLanguages.find(l => l.language === selectedLanguage)) {
      userProfile.learningLanguages = [
        ...userProfile.learningLanguages,
        { language: selectedLanguage, level: "Beginner", progress: 0 }
      ];
    }
  }

  function removeLanguage(languageToRemove) {
    userProfile.learningLanguages = userProfile.learningLanguages.filter(
      l => l.language !== languageToRemove
    );
  }

  async function navigateTo(destination) {
    await goto(destination)
  }
</script>

<div class="app">
  <nav class="sidebar">
    <div class="logo">Lingo</div>
    <button class="nav-button" on:click={ navigateTo('/home') }>
      <span class="material-icons">school</span>
      <span>LEARN</span>
    </button>
    <button class="nav-button active">
      <span class="material-icons">person</span>
      <span>PROFILE</span>
    </button>
  </nav>

  <main class="content">
    <div class="header">
      <div>
        <h1>Profile</h1>
        <p class="subtitle">Your learning journey</p>
      </div>
    </div>

    <div class="sections-grid">
      <section class="lesson-section profile-info">
        <div class="profile-header">
          <span class="material-icons profile-avatar">account_circle</span>
          <div>
            <h2>{userProfile.name}</h2>
            <p class="profile-email">{userProfile.email}</p>
            <p class="profile-join-date">Member since {userProfile.joinDate}</p>
          </div>
        </div>
        <div class="stats-grid">
          <div class="stat-item">
            <span class="material-icons stat-icon">local_fire_department</span>
            <div class="stat-info">
              <div class="stat-value">{userProfile.streakDays}</div>
              <div class="stat-label">Day Streak</div>
            </div>
          </div>
          <div class="stat-item">
            <span class="material-icons stat-icon">stars</span>
            <div class="stat-info">
              <div class="stat-value">{userProfile.totalPoints}</div>
              <div class="stat-label">Total Points</div>
            </div>
          </div>
        </div>
      </section>

      <section class="lesson-section">
        <h2>My Languages</h2>
        <div class="language-selector">
          <select bind:value={selectedLanguage} class="language-dropdown">
            {#each languages as language}
              <option value={language}>{language}</option>
            {/each}
          </select>
          <button class="add-language-btn" on:click={addNewLanguage}>
            <span class="material-icons">add</span>
            Add Language
          </button>
        </div>
        <div class="language-list">
          {#each userProfile.learningLanguages as lang}
            <div class="language-card">
              <div class="language-card-header">
                <div>
                  <h3 class="language-name">{lang.language}</h3>
                  <p class="language-level">{lang.level}</p>
                </div>
                <button 
                  class="remove-language-btn" 
                  on:click={() => removeLanguage(lang.language)}
                >
                  <span class="material-icons">close</span>
                </button>
              </div>
              <div class="language-progress">
                <div class="progress-bar">
                  <div class="progress-fill" style="width: {lang.progress}%"></div>
                </div>
                <span class="progress-text">{lang.progress}% Complete</span>
              </div>
            </div>
          {/each}
        </div>
      </section>

      <section class="lesson-section">
        <h2>Achievements</h2>
        <div class="lesson-list">
          {#each userProfile.achievements as achievement}
            <div class="lesson-item achievement-item">
              <div class="lesson-info">
                <span class="material-icons icon">{achievement.icon}</span>
                <div>
                  <div class="achievement-title">{achievement.title}</div>
                  <div class="achievement-description">{achievement.description}</div>
                </div>
              </div>
            </div>
          {/each}
        </div>
      </section>

      <section class="lesson-section">
        <h2>Recent Activity</h2>
        <div class="lesson-list">
          {#each userProfile.recentActivity as activity}
            <div class="lesson-item">
              <div class="lesson-info">
                <span class="material-icons icon">{activity.icon}</span>
                <div>
                  <div class="activity-title">{activity.action}</div>
                  <div class="activity-description">{activity.title}</div>
                  <div class="activity-date">{activity.date}</div>
                </div>
              </div>
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

  .profile-info {
    grid-column: 1 / -1;
  }

  .profile-header {
    display: flex;
    align-items: center;
    gap: 1.5rem;
    margin-bottom: 2rem;
  }

  .profile-avatar {
    font-size: 4rem;
    color: #ff4f99;
  }

  .profile-email {
    color: #666;
    margin: 0.25rem 0;
  }

  .profile-join-date {
    color: #888;
    font-size: 0.9rem;
    margin: 0.25rem 0;
  }

  .stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 1rem;
  }

  .stat-item {
    display: flex;
    align-items: center;
    gap: 1rem;
    padding: 1rem;
    background-color: #f8f8ff;
    border-radius: 8px;
  }

  .stat-icon {
    color: #ff4f99;
    font-size: 2rem;
  }

  .stat-info {
    display: flex;
    flex-direction: column;
  }

  .stat-value {
    font-size: 1.5rem;
    font-weight: 600;
    color: #333;
  }

  .stat-label {
    font-size: 0.9rem;
    color: #666;
  }

  h2 {
    font-size: 1.25rem;
    margin: 0 0 1.25rem;
    color: #333;
    font-weight: 600;
  }

  .language-selector {
    display: flex;
    gap: 1rem;
    margin-bottom: 1.5rem;
    align-items: center;
  }

  .language-dropdown {
    flex: 1;
    max-width: 200px;
    padding: 0.5rem 2rem 0.5rem 1rem;
    font-size: 0.95rem;
    color: #4a4a4a;
    background-color: white;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    cursor: pointer;
    appearance: none;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%23666' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E");
    background-repeat: no-repeat;
    background-position: right 0.5rem center;
    background-size: 1.2em;
  }

  .language-dropdown:hover {
    border-color: #ff4f99;
  }

  .language-dropdown:focus {
    outline: none;
    border-color: #ff4f99;
    box-shadow: 0 0 0 3px rgba(255, 79, 153, 0.1);
  }

  .add-language-btn {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.5rem 1rem;
    background-color: #ff4f99;
    color: white;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    font-size: 0.95rem;
    transition: background-color 0.2s ease;
  }

  .add-language-btn:hover {
    background-color: #ff3384;
  }

  .language-list {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  .language-card {
    background-color: #f8f8ff;
    border-radius: 8px;
    padding: 1.25rem;
  }

  .language-card-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 1rem;
  }

  .language-name {
    font-size: 1.1rem;
    font-weight: 600;
    color: #333;
    margin: 0;
  }

  .language-level {
    font-size: 0.9rem;
    color: #666;
    margin: 0.25rem 0 0 0;
  }

  .remove-language-btn {
    background: none;
    border: none;
    color: #666;
    cursor: pointer;
    padding: 0.25rem;
    border-radius: 4px;
    transition: all 0.2s ease;
  }

  .remove-language-btn:hover {
    background-color: #ffebf3;
    color: #ff4f99;
  }

  .language-progress {
    margin-top: 0.5rem;
  }

  .progress-bar {
    height: 8px;
    background-color: #e0e0e0;
    border-radius: 4px;
    overflow: hidden;
    margin-bottom: 0.5rem;
  }

  .progress-fill {
    height: 100%;
    background-color: #ff4f99;
    transition: width 0.3s ease;
  }

  .progress-text {
    font-size: 0.85rem;
    color: #666;
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

  .lesson-info {
    display: flex;
    align-items: center;
    gap: 0.75rem;
  }

  .icon {
    color: #ff4f99;
  }

  .achievement-title {
    font-weight: 500;
    color: #333;
  }

  .achievement-description {
    font-size: 0.9rem;
    color: #666;
    margin-top: 0.25rem;
  }

  .activity-title {
    font-weight: 500;
    color: #333;
  }

  .activity-description {
    font-size: 0.9rem;
    color: #666;
  }

  .activity-date {
    font-size: 0.8rem;
    color: #888;
    margin-top: 0.25rem;
  }
</style>

  