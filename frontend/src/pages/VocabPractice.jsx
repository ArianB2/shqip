import { useState, useEffect } from 'react'
import { getVocabulary, getVocabCategories } from '../utils/api'
import { useDialect } from '../hooks/useDialect'
import VocabCard from '../components/VocabCard'
import DialectToggle from '../components/DialectToggle'

export default function VocabPractice() {
  const { dialect, toggleDialect } = useDialect()
  const [category, setCategory] = useState('greetings')
  const [categories, setCategories] = useState([])
  const [words, setWords] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    getVocabCategories()
      .then((res) => setCategories(res.data.categories))
      .catch(console.error)
  }, [])

  useEffect(() => {
    setLoading(true)
    getVocabulary(category, dialect)
      .then((res) => {
        setWords(res.data.words)
        setError(null)
      })
      .catch(() => setError('Could not load vocabulary. Is the backend running?'))
      .finally(() => setLoading(false))
  }, [category, dialect])

  return (
    <div className="max-w-5xl mx-auto px-4 py-10">

      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-8">
        <div>
          <h1 className="text-3xl font-bold text-gray-900">Vocabulary</h1>
          <p className="text-gray-500 mt-1">Tap a card to hear how it sounds</p>
        </div>
        <DialectToggle dialect={dialect} onToggle={toggleDialect} />
      </div>

      {/* Category selector */}
      <div className="flex gap-2 flex-wrap mb-8">
        {categories.map((cat) => (
          <button
            key={cat.id}
            onClick={() => setCategory(cat.id)}
            className={`px-4 py-2 rounded-full text-sm font-medium capitalize transition-colors ${
              category === cat.id
                ? 'bg-albania-red text-white'
                : 'bg-white border border-gray-200 text-gray-600 hover:bg-gray-50'
            }`}
          >
            {cat.label} <span className="text-xs opacity-60">({cat.word_count})</span>
          </button>
        ))}
      </div>

      {error && (
        <div className="bg-red-50 border border-red-100 rounded-xl p-6 text-center mb-6">
          <p className="text-red-600">{error}</p>
        </div>
      )}

      {/* Word grid */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
        {loading
          ? [...Array(6)].map((_, i) => (
              <div key={i} className="bg-white rounded-xl border border-gray-100 p-6 animate-pulse">
                <div className="h-3 bg-gray-100 rounded w-1/4 mb-4" />
                <div className="h-7 bg-gray-100 rounded w-1/2 mb-2" />
                <div className="h-4 bg-gray-100 rounded w-3/4" />
              </div>
            ))
          : words.map((word) => (
              <VocabCard key={word.id} word={word} dialect={dialect} />
            ))}
      </div>

      {/* Month 3 placeholder */}
      <div className="mt-12 bg-gradient-to-r from-red-50 to-orange-50 rounded-2xl p-8 border border-red-100 text-center">
        <div className="text-3xl mb-3">🤖</div>
        <h2 className="font-bold text-lg text-gray-900 mb-2">AI Conversation Tutor</h2>
        <p className="text-sm text-gray-500 max-w-md mx-auto">
          Coming in Month 3 — practice a full Albanian conversation with an AI tutor
          that knows both dialects and corrects your grammar in real time.
        </p>
      </div>
    </div>
  )
}
