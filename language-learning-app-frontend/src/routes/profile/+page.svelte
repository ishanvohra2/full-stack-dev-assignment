<!-- src/routes/profile/+page.svelte -->
<script>
    // Mock data - in a real app, this would likely come from your backend
    const progressPercentage = 95;
    
    const grammarLessons = [
      { title: 'Basic Grammar Introduction', completed: true },
      { title: 'Present Simple Tense', completed: false },
      { title: 'Past Simple Tense', completed: false },
      { title: 'Future Tense Forms', completed: false },
      { title: 'Modal Verbs Usage', completed: false }
    ];
  
    const audioExercises = [
      { title: 'Pronunciation Basics' },
      { title: 'Common Phrases' },
      { title: 'Daily Conversations' },
      { title: 'Business English' },
      { title: 'Advanced Speaking' }
    ];
  
    const vocabularyList = [
      { title: 'Essential Words' },
      { title: 'Business Vocabulary' },
      { title: 'Academic Terms' },
      { title: 'Idioms & Phrases' },
      { title: 'Advanced Vocabulary' }
    ];
  </script>
  
  <div class="max-w-7xl mx-auto p-6">
    <!-- Header -->
    <div class="bg-white rounded-lg shadow-sm p-6 mb-6">
      <h1 class="text-2xl font-bold mb-2">Welcome back!</h1>
      <p class="text-gray-600 mb-4">Learn English</p>
      
      <!-- Progress Bar -->
      <div class="w-full bg-gray-200 rounded-full h-2">
        <div
          class="bg-pink-500 h-2 rounded-full"
          style="width: {progressPercentage}%"
        ></div>
      </div>
      <p class="text-sm text-gray-600 mt-2">{progressPercentage}% completed</p>
    </div>
  
    <!-- Main Content Grid -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      <!-- Grammar Lessons -->
      <div class="bg-white rounded-lg shadow-sm p-6">
        <h2 class="text-xl font-semibold mb-4">Grammar Lessons</h2>
        <ul class="space-y-4">
          {#each grammarLessons as lesson}
            <li class="flex items-center justify-between">
              <div class="flex items-center">
                {#if lesson.completed}
                  <svg class="w-5 h-5 text-pink-500 mr-3" fill="currentColor" viewBox="0 0 20 20">
                    <path d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"></path>
                  </svg>
                {:else}
                  <svg class="w-5 h-5 text-pink-500 mr-3" fill="currentColor" viewBox="0 0 20 20">
                    <path d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z"></path>
                  </svg>
                {/if}
                <span class="text-gray-700">{lesson.title}</span>
              </div>
              <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
              </svg>
            </li>
          {/each}
        </ul>
      </div>
  
      <!-- Audio Exercises -->
      <div class="bg-white rounded-lg shadow-sm p-6">
        <h2 class="text-xl font-semibold mb-4">Audio Exercises</h2>
        <ul class="space-y-4">
          {#each audioExercises as exercise}
            <li class="flex items-center justify-between">
              <div class="flex items-center">
                <svg class="w-5 h-5 text-pink-500 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.536 8.464a5 5 0 010 7.072M12 9.5l3-3 3 3M9 11.5l3-3 3 3"></path>
                </svg>
                <span class="text-gray-700">{exercise.title}</span>
              </div>
              <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
              </svg>
            </li>
          {/each}
        </ul>
      </div>
  
      <!-- Vocabulary List -->
      <div class="bg-white rounded-lg shadow-sm p-6">
        <h2 class="text-xl font-semibold mb-4">Vocabulary list</h2>
        <ul class="space-y-4">
          {#each vocabularyList as vocab}
            <li class="flex items-center justify-between">
              <div class="flex items-center">
                <svg class="w-5 h-5 text-pink-500 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path>
                </svg>
                <span class="text-gray-700">{vocab.title}</span>
              </div>
              <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
              </svg>
            </li>
          {/each}
        </ul>
      </div>
    </div>
  </div>
  
  <style>
    :global(body) {
      background-color: #f9fafb;
    }
  </style>