import { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import { getLessons } from '../utils/api'
import { useDialect } from '../hooks/useDialect'
import DialectToggle from '../components/DialectToggle'

export default function Lessons() {
  const { dialect, toggleDialect } = useDialect()
  const [lessons, setLessons] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    setLoading(true)
    getLessons(dialect)
      .then((res) => {
        setLessons(res.data.lessons)
        setError(null)
      })
      .catch((err) => {
        setError('Could not load lessons. Is the backend running?')
        console.error(err)
      })
      .finally(() => setLoading(false))
  }, [dialect])

  return (
    <div className="max-w-4xl mx-auto px-4 py-10">

      <div className="flex items-center justify-between mb-8">
        <div>
          <h1 className="text-3xl font-bold text-gray-900">Lessons</h1>
          <p className="text-gray-500 mt-1">
            Learning <span className="font-medium text-albania-red capitalize">{dialect}</span> Albanian
          </p>
        </div>
        <DialectToggle dialect={dialect} onToggle={toggleDialect} />
      </div>

      {loading && (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {[...Array(4)].map((_, i) => (
            <div key={i} className="bg-white rounded-xl border border-gray-100 p-6 animate-pulse">
              <div className="h-4 bg-gray-100 rounded w-1/3 mb-3" />
              <div className="h-6 bg-gray-100 rounded w-2/3 mb-2" />
              <div className="h-4 bg-gray-100 rounded w-full" />
            </div>
          ))}
        </div>
      )}

      {error && (
        <div className="bg-red-50 border border-red-100 rounded-xl p-6 text-center">
          <p className="text-red-600 font-medium">{error}</p>
          <p className="text-sm text-red-400 mt-1">
            Make sure the backend is running: <code>docker-compose up</code>
          </p>
        </div>
      )}

      {!loading && !error && (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {lessons.map((lesson) => (
            <Link
              key={lesson.id}
              to={`/practice?lesson=${lesson.id}&dialect=${dialect}`}
              className="vocab-card flex items-start gap-4"
            >
              <div className="w-12 h-12 bg-red-50 rounded-lg flex items-center justify-center
                              text-albania-red font-bold text-lg flex-shrink-0">
                {lesson.id}
              </div>
              <div>
                <h3 className="font-semibold text-gray-900">{lesson.title}</h3>
                <p className="text-sm text-albania-red italic mb-1">{lesson.title_sq}</p>
                <p className="text-sm text-gray-500">{lesson.description}</p>
                <p className="text-xs text-gray-400 mt-2">{lesson.word_count} words</p>
              </div>
            </Link>
          ))}
        </div>
      )}
    </div>
  )
}
