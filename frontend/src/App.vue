<template>
  <HeaderBar />

  <main class="page-shell">
    <StatsPanel :stats="stats" />

    <section class="toolbar">
      <label class="search-box">
        <span>Поиск</span>
        <input v-model="filters.search" type="search" placeholder="Название, автор, описание" @input="loadBooks" />
      </label>

      <label>
        <span>Категория</span>
        <select v-model="filters.category" @change="loadBooks">
          <option value="all">Все категории</option>
          <option v-for="category in categories" :key="category" :value="category">{{ category }}</option>
        </select>
      </label>

      <label>
        <span>Язык</span>
        <select v-model="filters.language" @change="loadBooks">
          <option value="all">Все языки</option>
          <option v-for="language in languages" :key="language" :value="language">{{ language }}</option>
        </select>
      </label>
    </section>

    <p v-if="error" class="error-message">{{ error }}</p>
    <p v-else-if="loading" class="empty-message">Загрузка каталога...</p>
    <p v-else-if="books.length === 0" class="empty-message">Книги не найдены. Попробуйте изменить фильтр.</p>

    <section v-else class="book-grid">
      <BookCard v-for="book in books" :key="book.id" :book="book" />
    </section>

    <BookForm @create="addBook" />
  </main>
</template>

<script setup>
import { onMounted, reactive, ref } from 'vue'
import HeaderBar from './components/HeaderBar.vue'
import StatsPanel from './components/StatsPanel.vue'
import BookCard from './components/BookCard.vue'
import BookForm from './components/BookForm.vue'
import { createBook, getBooks, getCategories, getLanguages, getStats } from './api/books'

const books = ref([])
const categories = ref([])
const languages = ref([])
const stats = ref({})
const loading = ref(false)
const error = ref('')

const filters = reactive({
  search: '',
  category: 'all',
  language: 'all'
})

async function loadBooks() {
  loading.value = true
  error.value = ''

  try {
    books.value = await getBooks(filters)
  } catch (apiError) {
    error.value = 'Не удалось загрузить книги. Проверьте, запущен ли backend на порту 8000.'
    console.error(apiError)
  } finally {
    loading.value = false
  }
}

async function loadDictionaries() {
  try {
    const [categoryList, languageList, libraryStats] = await Promise.all([
      getCategories(),
      getLanguages(),
      getStats()
    ])
    categories.value = categoryList
    languages.value = languageList
    stats.value = libraryStats
  } catch (apiError) {
    console.error(apiError)
  }
}

async function addBook(payload) {
  await createBook(payload)
  await Promise.all([loadBooks(), loadDictionaries()])
}

onMounted(async () => {
  await Promise.all([loadBooks(), loadDictionaries()])
})
</script>
