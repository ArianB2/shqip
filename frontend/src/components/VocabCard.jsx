/**
 * VocabCard
 * Displays a single Albanian word in both dialects.
 * Month 3: the speaker button will call Amazon Polly for real audio.
 *
 * Props:
 *   word    — vocabulary object from the API
 *   dialect — 'gheg' | 'tosk' (controls which form is shown "primary")
 */
export default function VocabCard({ word, dialect = 'tosk' }) {
  const primaryForm = word[dialect]
  const otherDialect = dialect === 'tosk' ? 'gheg' : 'tosk'
  const otherForm = word[otherDialect]
  const pronunciation = word[`pronunciation_${dialect}`]

  function handleSpeak() {
    // Month 3: replace with real Amazon Polly call
    if ('speechSynthesis' in window) {
      const utterance = new SpeechSynthesisUtterance(primaryForm)
      utterance.lang = 'sq'
      window.speechSynthesis.speak(utterance)
    }
  }

  return (
    <div className="vocab-card group">
      {/* English */}
      <p className="text-xs font-medium text-gray-400 uppercase tracking-wider mb-2">
        {word.english}
      </p>

      {/* Primary Albanian form */}
      <div className="flex items-center justify-between mb-1">
        <h3 className="text-2xl font-bold text-gray-900">{primaryForm}</h3>
        <button
          onClick={handleSpeak}
          className="opacity-0 group-hover:opacity-100 transition-opacity
                     text-albania-red hover:text-albania-dark p-1.5 rounded-lg
                     hover:bg-red-50"
          title="Hear pronunciation"
        >
          {/* Speaker icon */}
          <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2}
              d="M15.536 8.464a5 5 0 010 7.072M12 6v12m0 0l-3-3m3 3l3-3
                 M9.172 9.172a4 4 0 000 5.656" />
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2}
              d="M7 8H3v8h4l5 5V3L7 8z" />
          </svg>
        </button>
      </div>

      {/* Pronunciation guide */}
      {pronunciation && (
        <p className="text-sm text-gray-400 italic mb-3">/{pronunciation}/</p>
      )}

      {/* Other dialect comparison */}
      <div className="border-t border-gray-50 pt-3 mt-3">
        <span className="text-xs text-gray-400 capitalize">{otherDialect}: </span>
        <span className="text-sm text-gray-500">{otherForm}</span>
      </div>

      {/* Dialect note */}
      {word.notes && (
        <p className="text-xs text-gray-400 mt-2 leading-relaxed">{word.notes}</p>
      )}
    </div>
  )
}
