<template>
  <form class="book-form" @submit.prevent="submitBook">
    <h2>Добавить книгу</h2>
    <p>Форма отправляет данные на сервер через POST /api/books.</p>

    <div class="form-grid">
      <label>
        Название
        <input v-model="form.title" type="text" required placeholder="Название книги" />
      </label>
      <label>
        Автор
        <input v-model="form.author" type="text" required placeholder="Имя автора" />
      </label>
      <label>
        Категория
        <input v-model="form.category" type="text" required placeholder="Например, Наука" />
      </label>
      <label>
        Язык
        <input v-model="form.language" type="text" required placeholder="Русский / English" />
      </label>
      <label>
        Издатель
        <input v-model="form.publisher" type="text" required placeholder="Издательство" />
      </label>
      <label>
        ISBN
        <input v-model="form.isbn" type="text" required placeholder="978-..." />
      </label>
      <label>
        Год
        <input v-model.number="form.year" type="number" min="1000" max="2100" required />
      </label>
      <label>
        Страниц
        <input v-model.number="form.pages" type="number" min="1" required />
      </label>
    </div>

    <label>
      Описание
      <textarea v-model="form.description" required rows="4" placeholder="Краткое описание книги"></textarea>
    </label>

    <button class="primary-button" type="submit" :disabled="loading">
      {{ loading ? 'Добавляем...' : 'Добавить книгу' }}
    </button>
  </form>
</template>

<script setup>
import { reactive, ref } from 'vue'

const emit = defineEmits(['create'])

const loading = ref(false)
const form = reactive({
  title: '',
  author: '',
  description: '',
  publisher: '',
  year: new Date().getFullYear(),
  pages: 100,
  isbn: '',
  language: 'Русский',
  category: '',
  cover_color: '#4f46e5',
  available_copies: 1,
  rating: 4.5,
  read_url: 'https://openlibrary.org/'
})

function resetForm() {
  form.title = ''
  form.author = ''
  form.description = ''
  form.publisher = ''
  form.year = new Date().getFullYear()
  form.pages = 100
  form.isbn = ''
  form.language = 'Русский'
  form.category = ''
}

async function submitBook() {
  loading.value = true
  const payload = {
    title: form.title,
    authors: [form.author],
    description: form.description,
    publisher: form.publisher,
    year: form.year,
    pages: form.pages,
    isbn: form.isbn,
    language: form.language,
    category: form.category,
    cover_color: form.cover_color,
    available_copies: form.available_copies,
    rating: form.rating,
    read_url: form.read_url
  }

  try {
    await emit('create', payload)
    resetForm()
  } finally {
    loading.value = false
  }
}
</script>
