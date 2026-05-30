<template>
  <article class="book-card">
    <div class="cover" :style="{ background: book.cover_color }">
      <span>{{ shortTitle }}</span>
    </div>

    <div class="book-info">
      <div class="book-topline">
        <span class="badge">{{ book.category }}</span>
        <span class="rating">★ {{ book.rating }}</span>
      </div>

      <h3>{{ book.title }}</h3>
      <p class="authors">{{ book.authors.join(', ') }}</p>
      <p class="description">{{ book.description }}</p>

      <dl class="meta">
        <div>
          <dt>Издатель</dt>
          <dd>{{ book.publisher }}</dd>
        </div>
        <div>
          <dt>Год</dt>
          <dd>{{ book.year }}</dd>
        </div>
        <div>
          <dt>Страниц</dt>
          <dd>{{ book.pages }}</dd>
        </div>
        <div>
          <dt>Язык</dt>
          <dd>{{ book.language }}</dd>
        </div>
      </dl>

      <div class="card-footer">
        <span :class="['availability', book.available_copies > 0 ? 'available' : 'unavailable']">
          {{ book.available_copies > 0 ? `${book.available_copies} коп. доступно` : 'Нет в наличии' }}
        </span>
        <a v-if="book.read_url" :href="book.read_url" target="_blank" rel="noreferrer">Открыть</a>
      </div>
    </div>
  </article>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  book: {
    type: Object,
    required: true
  }
})

const shortTitle = computed(() =>
  props.book.title
    .split(' ')
    .slice(0, 2)
    .map((word) => word[0])
    .join('')
    .toUpperCase()
)
</script>
