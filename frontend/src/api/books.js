const API_URL = '/api'

async function request(path, options = {}) {
  const response = await fetch(`${API_URL}${path}`, {
    headers: {
      'Content-Type': 'application/json'
    },
    ...options
  })

  if (!response.ok) {
    const message = await response.text()
    throw new Error(message || 'Ошибка при запросе к API')
  }

  return response.json()
}

export function getBooks(filters = {}) {
  const params = new URLSearchParams()

  if (filters.search) params.set('search', filters.search)
  if (filters.category && filters.category !== 'all') params.set('category', filters.category)
  if (filters.language && filters.language !== 'all') params.set('language', filters.language)

  const query = params.toString()
  return request(`/books${query ? `?${query}` : ''}`)
}

export function getCategories() {
  return request('/categories')
}

export function getLanguages() {
  return request('/languages')
}

export function getStats() {
  return request('/stats')
}

export function createBook(book) {
  return request('/books', {
    method: 'POST',
    body: JSON.stringify(book)
  })
}
