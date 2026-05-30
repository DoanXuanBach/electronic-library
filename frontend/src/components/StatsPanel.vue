<template>
  <section class="stats" aria-label="Статистика библиотеки">
    <article class="stat-card">
      <span class="stat-label">Книг в каталоге</span>
      <strong>{{ stats.total_books ?? '—' }}</strong>
    </article>
    <article class="stat-card">
      <span class="stat-label">Категорий</span>
      <strong>{{ stats.total_categories ?? '—' }}</strong>
    </article>
    <article class="stat-card">
      <span class="stat-label">Доступных копий</span>
      <strong>{{ stats.available_copies ?? '—' }}</strong>
    </article>
    <article class="stat-card">
      <span class="stat-label">Средний рейтинг</span>
      <strong>{{ stats.average_rating ?? '—' }}</strong>
    </article>
  </section>
</template>

<script setup>
defineProps({
  stats: {
    type: Object,
    default: () => ({})
  }
})
</script>
