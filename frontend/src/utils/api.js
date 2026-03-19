import axios from 'axios'

// Base URL comes from the Vite environment variable.
// In development: http://localhost:8000 (or proxied through /api)
// In production:  your ECS service URL or API Gateway URL
const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000',
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
})

// ── Request interceptor ───────────────────────────────────────────────────
// Month 2: attach the Cognito auth token to every request automatically
api.interceptors.request.use((config) => {
  // const token = localStorage.getItem('shqip_token')  // uncomment in Month 2
  // if (token) config.headers.Authorization = `Bearer ${token}`
  return config
})

// ── Response interceptor ──────────────────────────────────────────────────
api.interceptors.response.use(
  (response) => response,
  (error) => {
    console.error('API error:', error.response?.data || error.message)
    return Promise.reject(error)
  }
)

// ── API methods ───────────────────────────────────────────────────────────

export const healthCheck = () =>
  api.get('/health')

export const getLessons = (dialect = 'tosk') =>
  api.get('/lessons', { params: { dialect } })

export const getLesson = (id, dialect = 'tosk') =>
  api.get(`/lessons/${id}`, { params: { dialect } })

export const getVocabulary = (category = 'greetings', dialect = 'tosk') =>
  api.get('/vocabulary', { params: { category, dialect } })

export const getVocabCategories = () =>
  api.get('/vocabulary/categories')

export default api
